from .models_COBRA_io import models_COBRA_io
# Query objects from LIMS
from SBaaS_LIMS.lims_biologicalMaterial_query import lims_biologicalMaterial_query
# Dependencies from cobra
from cobra.io.sbml import create_cobra_model_from_sbml_file, write_cobra_model_to_sbml_file
from cobra.io.json import load_json_model, save_json_model
from cobra.flux_analysis.variability import flux_variability_analysis
from cobra.flux_analysis.parsimonious import optimize_minimal_flux
from cobra.flux_analysis import flux_variability_analysis
from cobra.manipulation.modify import convert_to_irreversible, revert_to_reversible
# Resources
from python_statistics.calculate_interface import calculate_interface
from math import sqrt

class models_COBRA_execute(models_COBRA_io):
    def execute_makeModel(self,
            model_id_I=None,
            model_file_name_I=None,
            model_id_O=None,date_O=None,
            ko_list=[],flux_dict={},rxn_include_list=[],
            model_id_template_I='iJO1366',
            description=None,convert2irreversible_I=False,revert2reversible_I=False):
        '''make the model
        INPUT:
        model_id_I = existing model_id (if specified, an existing model in the database will be retrieved and modified)
        model_file_name_I = new model from file (if specified, a new model from file will be retrieved and modified)
        model_id_O = new model_id
        date_O = date the model was made
        description = description for the model
        INPUT (constraints in order):
        ko_list = list of reactions to constrain to zero flux
        flux_dict = dictionary of fluxes to constrain the model
        INPUT (model manipulation in order):
        rxn_include_list = list of reactions to include in the new model
        convert2irreversible_I = boolean, if True, the model will be converted to irreversible from reversible
        revert2reversible_I = boolean, if True, the model will be revert to reversible from irreversible

        Not yet implemented
        #----
        rxn_add_list = list of reactions to add from a different model
        model_add = model to add reactions from
        #----

        '''
        # retreive the model
        if model_id_I and model_id_O and date_O: #modify an existing model in the database
            cobra_model_sbml = None;
            cobra_model_sbml = self.get_row_modelID_dataStage02PhysiologyModels(model_id_I);
            cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
        elif model_file_name_I and model_id_O and date_O: #modify an existing model not in the database
            # check for the file type
            cobra_model = self.load_model(model_file_name_I);
        else:
            print('need to specify either an existing model_id or model_file_name!')
            return;
        # Constrain the model
        self.constrain_modelModelVariables(cobra_model,
                          ko_list=ko_list,flux_dict=flux_dict);
        # Use only a subset of reactions, if specified
        if rxn_include_list:
            remove_reactions=[];
            for rxn in cobra_model.reactions:
                if not rxn.id in rxn_include_list:
                    remove_reactions.append(rxn);
            cobra_model.remove_reactions(remove_reactions,delete=True,remove_orphans=True);
        if convert2irreversible_I: convert_to_irreversible(cobra_model);
        if revert2reversible_I: 
            self.repair_irreversibleModel(cobra_model);
            self.revert2reversible(cobra_model);
            #revert_to_reversible(cobra_model,update_solution = False)
        # Change description, if any:
        if description:
            cobra_model.description = description;
        # test the model
        if self.test_model(cobra_model):
            # write the model to a temporary file
            write_cobra_model_to_sbml_file(cobra_model, 'cobra_model_tmp.xml');
            # upload the model to the database
            self.import_dataStage02PhysiologyModel_sbml(model_id_O, date_O, 'cobra_model_tmp.xml');
    def make_modelFromRxnsAndMetsTables(self,
                model_id_I=None,model_id_O=None,date_O=None,description=None,                       
                ko_list=[],flux_dict={},rxn_include_list=[],
                convert2irreversible_I=False,revert2reversible_I=False,
                convertPathway2individualRxns_I=False,
                model_id_template_I='iJO1366',pathway_model_id_I=None
                ):
        '''make/update the model using the modelReactions and modelMetabolites table
        INPUT:
        model_id_I = existing model_id (if specified, an existing model in the database will be retrieved and modified)
        model_file_name_I = new model from file (if specified, a new model form file will be retrieved and modified)
        model_id_O = new model_id
        date_O = date the model was made
        description = description for the model
        INPUT (constraints in order):
        ko_list = list of reactions to constrain to zero flux
        flux_dict = dictionary of fluxes to constrain the model
        INPUT (model manipulation in order):
        rxn_include_list = list of reactions to include in the new model
        convertPathway2individualRxns_I = boolean, if True, lumped rxns will be converted to individual rxns
        template_model_id_I = model_id to use as a template when adding in new reactions
        pathway_model_id_I = model_id for the pathway
        convert2irreversible_I = boolean, if True, the model will be converted to irreversible from reversible
        revert2reversible_I = boolean, if True, the model will be revert to reversible from irreversible
        '''
        
        # get the model reactions and metabolites from the database
        reactions = [];
        metabolites = [];
        reactions = self.get_rows_modelID_dataStage02PhysiologyModelReactions(model_id_I);
        metabolites = self.get_rows_modelID_dataStage02PhysiologyModelMetabolites(model_id_I);
        # break apart lumped reactions
        if convertPathway2individualRxns_I:
            metabolites_O = [];
            reactions,metabolites_O = self.convert_lumpedRxns2IndividualRxns(
                        model_id_template_I=model_id_template_I,
                        pathway_model_id_I=pathway_model_id_I,
                        reactions_I=reactions);
            # add in any new metabolites that may have been found
            met_ids = [x['met_id'] for x in metabolites];
            for met in metabolites_O:
                if not met['met_id'] in met_ids:
                    metabolites.append(met);
        # create the model
        cobra_model = self.create_modelFromReactionsAndMetabolitesTables(reactions,metabolites)
        # Constrain the model
        self.constrain_modelModelVariables(cobra_model,
                            ko_list=ko_list,flux_dict=flux_dict);
        # Use only a subset of reactions, if specified
        if rxn_include_list:
            remove_reactions=[];
            for rxn in cobra_model.reactions:
                if not rxn.id in rxn_include_list:
                    remove_reactions.append(rxn);
            cobra_model.remove_reactions(remove_reactions,delete=True,remove_orphans=True);
        if convert2irreversible_I: convert_to_irreversible(cobra_model);
        if revert2reversible_I: 
            self.repair_irreversibleModel(cobra_model);
            self.revert2reversible(cobra_model);
        # Change description, if any:
        if description:
            cobra_model.description = description;
        # test the model
        if self.test_model(cobra_model):
            # write the model to a temporary file
            save_json_model(cobra_model,'cobra_model_tmp.json')
            # add the model information to the database
            dataStage02PhysiologyModelRxns_data = [];
            dataStage02PhysiologyModelMets_data = [];
            dataStage02PhysiologyModels_data,\
                dataStage02PhysiologyModelRxns_data,\
                dataStage02PhysiologyModelMets_data = self._parse_model_json(model_id_O, date_O, 'cobra_model_tmp.json')
            if model_id_I and model_id_O: #make a new model based off of a modification of an existing model in the database
                self.add_dataStage02PhysiologyModelMetabolites(dataStage02PhysiologyModelMets_data);
                self.add_dataStage02PhysiologyModelReactions(dataStage02PhysiologyModelRxns_data);
                self.add_dataStage02PhysiologyModels(dataStage02PhysiologyModels_data);
            elif model_id_I and not model_id_O:  #update an existing model in the database
                self.update_data_stage02_isotopomer_models(dataStage02PhysiologyModels_data);
            else:
                print('need to specify either an existing model_id!')
        return
    def execute_testModel(self,cobra_model_I=None,model_id_I=None,ko_list=[],flux_dict={},description=None):
        '''simulate a cobra model'''

        test_O = False;
        if model_id_I:
            # get the xml model
            cobra_model_sbml = [];
            cobra_model_sbml = self.get_row_modelID_dataStage02PhysiologyModels(model_id_I);
            if cobra_model_sbml:
                cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
            else:
                print('model not found');
        elif cobra_model_I:
            cobra_model = cobra_model_I;
        test_O = self.test_model(cobra_model_I=cobra_model,ko_list=ko_list,flux_dict=flux_dict,description=description);
        return test_O;
    def get_models(self,model_ids_I=[]):
        '''Retreive multiple COBRA models
        INPUT:
        models_ids_I = list of model_id
        OUTPUT:
        models_dict_O = dictionary of COBRA models where the key is the model_id'''
        models_dict_O = {};
        # get the model ids:
        for model_id in model_ids_I:
            # get the cobra model
            cobra_model_sbml = None;
            cobra_model_sbml = self.get_row_modelID_dataStage02PhysiologyModels(model_id);
            cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
            models_dict_O[model_id]=cobra_model;
        return models_dict_O;
    def convert_lumpedRxns2IndividualRxns(self,
                model_id_template_I,
                pathway_model_id_I,
                reactions_I):
        '''make the model
        INPUT:
        model_id_I = string, model_id for net reactions
        reactions_I = [{}] from modelReactions table
        OUTPUT:
        reactions_O = [{}] without lumped reactions
        metabolites_O = [{}] metabolites for reactions

        '''
        
        reactions_O = [];
        metabolites_O = [];
        # get the pathways
        pathways = {};
        pathways = self.get_rowsDict_modelID_dataStage02PhysiologyModelPathways(pathway_model_id_I);
        for rxn in reactions_I:
            if rxn['rxn_id'] in pathways.keys():
                for rxn_id in pathways[rxn['rxn_id']]['reactions']:
                    #if rxn_id == 'AIRC3':
                    #    print('check');
                    # lookup the reaction
                    rxn_tmp = {};
                    rxn_tmp = self.get_row_modelIDAndRxnID_dataStage02PhysiologyModelReactions(model_id_template_I,rxn_id);
                    if rxn_tmp:
                        reactions_O.append(rxn_tmp);
                        # lookup the metabolites
                        for met_id in rxn_tmp['products_ids']+rxn_tmp['reactants_ids']:
                            met_tmp = {};
                            met_tmp = self.get_row_modelIDAndMetID_dataStage02PhysiologyModelMetabolites(model_id_template_I,met_id);
                            metabolites_O.append(met_tmp);
                    else:
                        print('rxn_id ' + rxn_id + ' not found in template model.');
            else:
                reactions_O.append(rxn);
        return reactions_O,metabolites_O;
    def execute_convertNetRxns2IndividualRxns(self,
                model_id_netRxns_I,
                model_id_template_I,
                pathway_model_id_I,
                convert2Irreversible_I = False):
        '''make the model
        INPUT:
        model_id_I = string, model_id for net reactions
        reactions_I = [{}] from modelReactions table
        OUTPUT:
        reactions_O = [{}] without lumped reactions
        metabolites_O = [{}] metabolites for reactions

        '''
        
        reactions_O = [];
        metabolites_O = [];
        # get the model reactions and metabolites from the database
        reactions = [];
        metabolites = [];
        reactions = self.get_rows_modelID_dataStage02PhysiologyModelReactions(model_id_netRxns_I);
        metabolites = self.get_rows_modelID_dataStage02PhysiologyModelMetabolites(model_id_netRxns_I);
        met_ids = [met['met_id'] for met in metabolites]
        # get the model reactions and metabolites for the template from the database
        reactions_template = self.get_rows_modelID_dataStage02PhysiologyModelReactions(model_id_template_I);
        reactions_template_dict = {rxn['rxn_id']:rxn for rxn in reactions_template}
        metabolites_template = self.get_rows_modelID_dataStage02PhysiologyModelMetabolites(model_id_template_I);
        metabolites_template_dict = {met['met_id']:met for met in metabolites_template}
        # get the pathways
        pathways = {};
        pathways = self.get_rowsDict_modelID_dataStage02PhysiologyModelPathways(pathway_model_id_I);
        for rxn in reactions:
            if rxn['rxn_id'] in pathways.keys():
                rxn_ids = self.convert_netRxn2IndividualRxns(
                    rxn['rxn_id'],
                    pathway_dict_I = pathways,
                    convert2Irreversible_I = convert2Irreversible_I
                    )
                for rxn_id in rxn_ids:
                    # lookup the reaction
                    rxn_tmp = {};
                    #rxn_tmp = self.get_row_modelIDAndRxnID_dataStage02PhysiologyModelReactions(model_id_template_I,rxn_id);
                    if rxn_id in reactions_template_dict.keys():
                        rxn_tmp = reactions_template_dict[rxn_id];
                    if rxn_tmp:
                        reactions_O.append(rxn_tmp);
                        # lookup the metabolites
                        for met_id in rxn_tmp['products_ids']+rxn_tmp['reactants_ids']:
                            met_tmp = {};
                            #met_tmp = self.get_row_modelIDAndMetID_dataStage02PhysiologyModelMetabolites(model_id_template_I,met_id);
                            if met_id in metabolites_template_dict.keys():
                                met_tmp = metabolites_template_dict[met_id];
                            if met_tmp:
                                if not met_id in met_ids:
                                    metabolites_O.append(met_tmp)
                            else:
                                print('met_id ' + met_id + ' not found in template model.');
                    else:
                        print('rxn_id ' + rxn_id + ' not found in template model.');
            else:
                reactions_O.append(rxn);
        metabolites_O = metabolites + metabolites_O;
        return reactions_O,metabolites_O;
    def map_rxnIDs2GeneNames(
        self,model_id_I,rxn_ids_I=[],
        biologicalmaterial_I = None):
        '''map model rxn_ids to gene_names
        INPUT:
        model_Id_I = string, name of the model
        rxn_ids_I = list of reactions
        biologicalmaterial_I = string, name of the biological material to map
        OUTPUT:
        data_O = listDict of model_id,rxn_id,biological_material,gene_name,ordered_locus_name'''

        biologicalmaterial_query = lims_biologicalMaterial_query(self.session,self.engine,self.settings);

        data_O = [];
        for rxn_id in rxn_ids_I:
            bnumbers = self.get_geneIDs_modelIDAndRxnID_dataStage02PhysiologyModelReactions(model_id_I,rxn_id);
            for bnum in bnumbers:
                gene_names = biologicalmaterial_query.get_geneName_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(
                    biologicalmaterial_I,bnum);
                for gene_name in gene_names:
                    tmp = {};
                    tmp['ordered_locus_name'] = bnum;
                    tmp['gene_name'] = gene_name['gene_name'];
                    tmp['rxn_id'] = rxn_id;
                    tmp['model_id'] = model_id_I;
                    data_O.append(tmp);
        return data_O;
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
        calc = calculate_interface();
        shortest_path_O = [];
        # get the model reactions from table
        reactions = self.get_rows_modelID_dataStage02PhysiologyModelReactions(model_id_I);
        #convert rxns list to directed graph
        aCyclicGraph = self.convert_modelReactionsTable2DirectedAcyclicGraph(
            reactions,weights_I=weights_I,attributes_I={},
            exclusion_list_I=exclusion_list_I);
        # find the shortest paths
        for startAndStop in nodes_startAndStop_I:
            tmp = {'start':startAndStop[0],'stop':startAndStop[1]};
            try:
                output2 = self.find_shortestPath_nodes(
                    aCyclicGraph,startAndStop[0],startAndStop[1],
                    algorithm_I=algorithm_I,params_I=params_I);
                if str(type(output2))=="<class 'generator'>":
                    paths = [o for o in output2];
                    distances = [(len(p)-1)/2 for p in paths]
                else:
                    paths = [output2];
                    distances = [(len(output2)-1)/2];
            except Exception as e:
                print(e);
                print('algorithm = ' + algorithm_I + '; start = ' + startAndStop[0] + '; stop = ' + startAndStop[1]);
                continue;
            #calculate descriptive statistics on the paths
            try:
                data_ave_O, data_var_O, data_lb_O, data_ub_O = calc.calculate_ave_var(distances,confidence_I = 0.95);
                if data_ave_O:
                    data_cv_O = sqrt(data_var_O)/data_ave_O*100;
                else:
                    data_cv_O = None;
                min_O, max_O, median_O, iq_1_O, iq_3_O=calc.calculate_interquartiles(distances);
            except Exception as e:
                print(e);
                print('algorithm = ' + algorithm_I + '; start = ' + startAndStop[0] + '; stop = ' + startAndStop[1]);
                continue;
            tmp['all_paths'] = paths;
            tmp['algorithm'] = algorithm_I;
            tmp['params'] = params_I;
            tmp['path_max'] = max_O;
            tmp['path_min'] = min_O;
            tmp['path_iq_1'] = iq_1_O;
            tmp['path_iq_3'] = iq_3_O;
            tmp['path_median'] = median_O;
            tmp['path_average'] = data_ave_O;
            tmp['path_var'] = data_var_O;
            tmp['path_n'] = len(paths);
            tmp['path_cv'] = data_cv_O;
            tmp['path_ci_lb'] = data_lb_O;
            tmp['path_ci_ub'] = data_ub_O;
            tmp['path_ci_level'] = 0.95;
            shortest_path_O.append(tmp);
        return shortest_path_O;

