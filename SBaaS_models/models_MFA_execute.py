#System
import json
#SBaaS
from .models_MFA_io import models_MFA_io  
# Resources
from genomeScale_MFA.MFA_netRxns import isotopomer_netRxns
# Dependencies from cobra
from cobra.io.sbml import create_cobra_model_from_sbml_file, write_cobra_model_to_sbml_file
from cobra.io.json import load_json_model, save_json_model
from cobra.io import save_json_model, load_json_model
from cobra.flux_analysis.variability import flux_variability_analysis
from cobra.flux_analysis.parsimonious import optimize_minimal_flux
from cobra.flux_analysis import flux_variability_analysis

class models_MFA_execute(models_MFA_io):
    def make_modelAndMappingFromRxnsAndMetsTables(self,model_id_I=None,model_id_O=None,mapping_id_I=None,mapping_id_O=None,date_O=None,ko_list=[],flux_dict={},description=None):
        '''make/update the model AND model mappings using the modelReactions and modelMetabolites table'''
        
        if model_id_I and model_id_O and mapping_id_I and mapping_id_O: #make a new model based off of a modification of an existing model in the database
            # get the model reactions and metabolites from the database
            reactions = [];
            metabolites = [];
            reactions = self.get_rows_modelID_dataStage02IsotopomerModelReactions(model_id_I);
            metabolites = self.get_rows_modelID_dataStage02IsotopomerModelMetabolites(model_id_I);
            reactions_mappings = [];
            metabolites_mappings = [];
            reactions_mappings = self.get_rows_mappingID_dataStage02IsotopomerAtomMappingReactions(mapping_id_I);
            metabolites_mappings = self.get_rows_mappingID_dataStage02IsotopomerAtomMappingMetabolites(mapping_id_I);
            # rename the reactions and metabolite model_ids
            for rxn_cnt,rxn in enumerate(reactions):
                reactions[rxn_cnt]['model_id'] = model_id_O;
            for met_cnt,met in enumerate(metabolites):
                metabolites[met_cnt]['model_id'] = model_id_O;
            # rename the reactions and metabolite mapping_ids
            for rxn_cnt,rxn in enumerate(reactions_mappings):
                reactions_mappings[rxn_cnt]['mapping_id'] = mapping_id_O;
            for met_cnt,met in enumerate(metabolites_mappings):
                metabolites_mappings[met_cnt]['mapping_id'] = mapping_id_O;
            # create the model
            cobra_model = self.create_modelFromReactionsAndMetabolitesTables(reactions,metabolites)
            # Apply KOs, if any:
            for ko in ko_list:
                cobra_model.reactions.get_by_id(ko).lower_bound = 0.0;
                cobra_model.reactions.get_by_id(ko).upper_bound = 0.0;
            # Apply flux constraints, if any:
            for rxn,flux in flux_dict.items():
                cobra_model.reactions.get_by_id(rxn).lower_bound = flux['lb'];
                cobra_model.reactions.get_by_id(rxn).upper_bound = flux['ub'];
            # Change description, if any:
            if description:
                cobra_model.description = description;
            # test the model
            if self.test_model(cobra_model):
                # write the model to a temporary file
                save_json_model(cobra_model,'cobra_model_tmp.json')
                # add the model information to the database
                dataStage02IsotopomerModelRxns_data = [];
                dataStage02IsotopomerModelMets_data = [];
                dataStage02IsotopomerModels_data,\
                    dataStage02IsotopomerModelRxns_data,\
                    dataStage02IsotopomerModelMets_data = self._parse_model_json(model_id_O, date_O, 'cobra_model_tmp.json')
                self.add_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);
                # add the metabolite and reaction information to the database
                self.add_data_stage02_isotopomer_modelReactions(reactions);
                self.add_data_stage02_isotopomer_modelMetabolites(metabolites);
                # add the metabolites and reactions mappings to the database
                self.add_data_dataStage02IsotopomerAtomMappingReactions(reactions_mappings);
                self.add_data_dataStage02IsotopomerAtomMappingMetabolites(metabolites_mappings);
        elif model_id_I and not model_id_O and mapping_id_I and not mapping_id_O:  #update an existing model in the database
            # get the model reactions and metabolites from the database
            reactions = [];
            metabolites = [];
            reactions = self.get_rows_modelID_dataStage02IsotopomerModelReactions(model_id_I);
            metabolites = self.get_rows_modelID_dataStage02IsotopomerModelMetabolites(model_id_I);
            # creat the model
            cobra_model = self.create_modelFromReactionsAndMetabolitesTables(reactions,metabolites)
            # Apply KOs, if any:
            for ko in ko_list:
                cobra_model.reactions.get_by_id(ko).lower_bound = 0.0;
                cobra_model.reactions.get_by_id(ko).upper_bound = 0.0;
            # Apply flux constraints, if any:
            for rxn,flux in flux_dict.items():
                cobra_model.reactions.get_by_id(rxn).lower_bound = flux['lb'];
                cobra_model.reactions.get_by_id(rxn).upper_bound = flux['ub'];
            # Change description, if any:
            if description:
                cobra_model.description = description;
            # test the model
            if self.test_model(cobra_model):
                # write the model to a temporary file
                save_json_model(cobra_model,'cobra_model_tmp.json')
                # upload the model to the database
                # add the model information to the database
                dataStage02IsotopomerModelRxns_data = [];
                dataStage02IsotopomerModelMets_data = [];
                dataStage02IsotopomerModels_data,\
                    dataStage02IsotopomerModelRxns_data,\
                    dataStage02IsotopomerModelMets_data = self._parse_model_json(model_id_I, date_I, 'cobra_model_tmp.json')
                self.update_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);

        else:
            print('need to specify an existing model_id/mapping_id!')
        return
    def simulate_model(self,model_id_I,ko_list=[],flux_dict={},measured_flux_list=[],description=None):
        '''simulate a cobra model'''

        # get the xml model
        cobra_model_sbml = ''
        cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id_I);
        # load the model
        if cobra_model_sbml:
            cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
        # implement optimal KOs and flux constraints:
        for ko in ko_list:
            cobra_model.reactions.get_by_id(ko).lower_bound = 0.0;
            cobra_model.reactions.get_by_id(ko).upper_bound = 0.0;
        for rxn,flux in flux_dict.items():
            cobra_model.reactions.get_by_id(rxn).lower_bound = flux['lb'];
            cobra_model.reactions.get_by_id(rxn).upper_bound = flux['ub'];
        for flux in measured_flux_list:
            cobra_model.reactions.get_by_id(flux['rxn_id']).lower_bound = flux['flux_lb'];
            cobra_model.reactions.get_by_id(flux['rxn_id']).upper_bound = flux['flux_ub'];
        # change description, if any:
        if description:
            cobra_model.description = description;
        # test for a solution:
        cobra_model.optimize();
        if not cobra_model.solution.f:
            print("model does not converge to a solution");
        ##find minimal flux solution:
        #pfba = optimize_minimal_flux(cobra_model,True);

        return cobra_model;
    def make_Model(self,model_id_I=None,model_id_O=None,date_O=None,model_file_name_I=None,ko_list=[],flux_dict={},description=None):
        '''make a new model'''

        if model_id_I and model_id_O and date_O: #make a new model based off of a modification of an existing model in the database
            cobra_model_sbml = None;
            cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id_I);
            # write the model to a temporary file
            cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
            # Constrain the model
            self.constrain_modelModelVariables(cobra_model=cobra_model,ko_list=ko_list,flux_dict=flux_dict);
            # Change description, if any:
            if description:
                cobra_model.description = description;
            # test the model
            if self.test_model(cobra_model):
                # write the model to a temporary file
                with open('cobra_model_tmp.xml','w') as file:
                    file.write(cobra_model);
                # upload the model to the database
                self.import_dataStage02Model_sbml(model_id_O, date_O, 'cobra_model_tmp.xml');
        elif model_file_name_I and model_id_O and date_O: #modify an existing model in not in the database
            # check for the file type
            if '.json' in model_file_name_I:
                # Read in the sbml file and define the model conditions
                cobra_model = load_json_model(model_file_name_I, print_time=True);
            elif '.xml' in model_file_name_I:
                # Read in the sbml file and define the model conditions
                cobra_model = create_cobra_model_from_sbml_file(model_file_name_I, print_time=True);
            else: print('file type not supported')
            # Constrain the model
            self.constrain_modelModelVariables(cobra_model=cobra_model,ko_list=ko_list,flux_dict=flux_dict);
            # Change description, if any:
            if description:
                cobra_model.description = description;
            # test the model
            if self.test_model(cobra_model):
                # write the model to a temporary file
                filename = '';
                if '.xml' in model_file_name_I:
                    filename = 'cobra_model_tmp.xml'
                    with open(filename,'w') as file:
                        file.write(cobra_model);
                        file.close()
                elif '.json' in model_file_name_I:
                    filename = 'cobra_model_tmp.json';
                    with open(filename,'w') as file:
                        file.write(cobra_model);
                        file.close()
                else: print('file type not supported')
                # upload the model to the database
                self.import_dataStage02Model_sbml(model_id_O, date_O, filename);
        else:
            print('need to specify either an existing model_id or model_file_name!')
    def make_modelFromRxnsAndMetsTables(self,model_id_I=None,model_id_O=None,date_O=None,ko_list=[],flux_dict={},description=None):
        '''make/update the model using the modelReactions and modelMetabolites table'''
        
        if model_id_I and model_id_O: #make a new model based off of a modification of an existing model in the database
            # get the model reactions and metabolites from the database
            reactions = [];
            metabolites = [];
            reactions = self.get_rows_modelID_dataStage02IsotopomerModelReactions(model_id_I);
            metabolites = self.get_rows_modelID_dataStage02IsotopomerModelMetabolites(model_id_I);
            # creat the model
            cobra_model = self.create_modelFromReactionsAndMetabolitesTables(reactions,metabolites)
            # Constrain the model
            self.constrain_modelModelVariables(cobra_model=cobra_model,ko_list=ko_list,flux_dict=flux_dict);
            # Change description, if any:
            if description:
                cobra_model.description = description;
            # test the model
            if self.test_model(cobra_model):
                # write the model to a temporary file
                save_json_model(cobra_model,'cobra_model_tmp.json')
                # add the model information to the database
                dataStage02IsotopomerModelRxns_data = [];
                dataStage02IsotopomerModelMets_data = [];
                dataStage02IsotopomerModels_data,\
                    dataStage02IsotopomerModelRxns_data,\
                    dataStage02IsotopomerModelMets_data = self._parse_model_json(model_id_O, date_O, 'cobra_model_tmp.json')
                self.add_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);
        elif model_id_I and not model_id_O:  #update an existing model in the database
            # get the model reactions and metabolites from the database
            reactions = [];
            metabolites = [];
            reactions = self.get_rows_modelID_dataStage02IsotopomerModelReactions(model_id_I);
            metabolites = self.get_rows_modelID_dataStage02IsotopomerModelMetabolites(model_id_I);
            # creat the model
            cobra_model = self.create_modelFromReactionsAndMetabolitesTables(reactions,metabolites)
            # Constrain the model
            self.constrain_modelModelVariables(cobra_model=cobra_model,ko_list=ko_list,flux_dict=flux_dict);
            # Change description, if any:
            if description:
                cobra_model.description = description;
            # test the model
            if self.test_model(cobra_model):
                # write the model to a temporary file
                save_json_model(cobra_model,'cobra_model_tmp.json')
                # upload the model to the database
                # add the model information to the database
                dataStage02IsotopomerModelRxns_data = [];
                dataStage02IsotopomerModelMets_data = [];
                dataStage02IsotopomerModels_data,\
                    dataStage02IsotopomerModelRxns_data,\
                    dataStage02IsotopomerModelMets_data = self._parse_model_json(model_id_I, date_O, 'cobra_model_tmp.json')
                self.update_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);

        else:
            print('need to specify either an existing model_id!')
        return
    def export_modelFromTable(self,model_id_I,filename_I):
        '''export a cobra model
        INPUT:
        model_id_I = model id
        filename_I = filename
        '''
        
        # get the model
        cobra_model_sbml = {};
        cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id_I);
        if not cobra_model_sbml:
            print('model not found');
            return;
        if cobra_model_sbml['file_type'] == 'sbml':
            with open(filename_I,'w') as file:
                file.write(cobra_model_sbml['model_file']);
                file.close();
        elif cobra_model_sbml['file_type'] == 'json':
            with open(filename_I,'w') as file:
                file.write(cobra_model_sbml['model_file']);
                file.close();
        else:
            print('file_type not supported')
    def export_model(self,model_id_I,filename_I,filetype_I = 'sbml',ko_list=[],flux_dict={}):
        '''export a cobra model
        INPUT:
        model_id_I = model id
        filename_I = filename
        filetype_I = if specified, the model will be written to the desired filetype
                    default: model file in the database
        '''
        
        # get the model
        cobra_model_sbml = {};
        cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id_I);
        if not cobra_model_sbml:
            print('model not found');
            return;
        # load the model
        cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
        # Constrain the model
        self.constrain_modelModelVariables(cobra_model=cobra_model,ko_list=ko_list,flux_dict=flux_dict);
        # export the model
        if filetype_I == 'sbml':
            cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
            #export the model to sbml
            write_cobra_model_to_sbml_file(cobra_model,filename_I);
        elif filetype_I == 'json':
            cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
            #export the model to json
            save_json_model(cobra_model,filename_I);
        else:
            print('file_type not supported')
    def execute_testModel(self,cobra_model_I=None,model_id_I=None,ko_list=[],flux_dict={},description=None):
        '''simulate a cobra model'''

        test_O = False;
        if model_id_I:
            # get the xml model
            cobra_model_sbml = [];
            cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id_I);
            if cobra_model_sbml:
                cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
            else:
                print('model not found');
        elif cobra_model_I:
            cobra_model = cobra_model_I;
        test_O = self.test_model(cobra_model_I=cobra_model,ko_list=ko_list,flux_dict=flux_dict,description=description);
        return test_O;
    def get_models(self,model_ids_I=[]):
        '''Retreive multiple MFA models
        INPUT:
        models_ids_I = list of model_id
        OUTPUT:
        models_dict_O = dictionary of COBRA models where the key is the model_id'''
        models_dict_O = {};
        # get the model ids:
        for model_id in model_ids_I:
            # get the cobra model
            cobra_model_sbml = None;
            cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id);
            cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
            models_dict_O[model_id]=cobra_model;
        return models_dict_O;
    def get_model(self,model_id_I):
        '''Retreive an MFA models
        INPUT:
        models_ids_I = list of model_id
        OUTPUT:
        models_dict_O = dictionary of COBRA models where the key is the model_id'''
        # get the cobra model
        cobra_model_sbml = None;
        cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id_I);
        cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
        return cobra_model;

    
    def execute_findShortestPath_nodes(self,model_id_I,
            nodes_startAndStop_I,
            algorithm_I='all_simple_paths',params_I={'cutoff':25},
            exclusion_list_I=[],
            weights_I=None
            ):
        '''
        INPUT:
        model_id_I: model id [string]
        nodes_startAndStop_I: list of node start/stops
            e.g., [[nad_c,nadh_c],[g6p_c,f6p_c],...]
        OUTPUT:
        shortest_path_O = [{[nad_c,nadh_c]:algorithm_I output},...]

        distance = (len(sp['shortest_path'])-1)/2
        '''
        shortest_path_O = [];
        # get the model reactions from table
        reactions = self.get_rows_modelID_dataStage02IsotopomerModelReactions(model_id_I);
        #convert rxns list to directed graph
        aCyclicGraph = self.convert_modelReactionsTable2DirectedAcyclicGraph(
            reactions,weights_I=weights_I,attributes_I={},
            exclusion_list_I=exclusion_list_I);
        # find the shortest paths
        for startAndStop in nodes_startAndStop_I:
            tmp = {'start':startAndStop[0],'stop':startAndStop[1]};

            ## find shortest path for each node_start and stop pair
            #algorithm_I = 'astar_path';
            #params_I={}
            #output1 = self.find_shortestPath_nodes(
            #    aCyclicGraph,startAndStop[0],startAndStop[1],
            #    algorithm_I=algorithm_I,params_I=params_I);
            #distance = (len(output1)-1)/2;
            #tmp['shortest_path'] = distance;

            # find maximum and average path for each node_start and stop pair
            #algorithm_I='all_simple_paths';
            #params_I={'cutoff':25};
            output2 = self.find_shortestPath_nodes(
                aCyclicGraph,startAndStop[0],startAndStop[1],
                algorithm_I=algorithm_I,params_I=params_I);
            paths = [o for o in output2];
            distances = [(len(p)-1)/2 for p in paths]
            dist_ave = sum(distances)/len(paths);
            dist_max = max(distances);
            dist_min = min(distances);
            tmp['longest_path'] = dist_max;
            tmp['average_path'] = dist_ave;
            tmp['shortest_path'] = dist_min;
            shortest_path_O.append(tmp);
        return shortest_path_O;