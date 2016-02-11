# Dependencies from cobra
from cobra.io.sbml import create_cobra_model_from_sbml_file, write_cobra_model_to_sbml_file
from cobra.manipulation.modify import convert_to_irreversible
from cobra import Model, Metabolite, Reaction
from cobra.io.json import load_json_model, save_json_model
# Resources
from molmass.molmass import Formula
# System dependencies
import re
class models_MFA_dependencies():
    def _parse_model_sbml(self,model_id_I,date_I,filename_I):
        # Read in the sbml file and define the model conditions
        cobra_model = create_cobra_model_from_sbml_file(filename_I, print_time=True)
        model_data = [];
        model_data_tmp = {};
        # parse out model metadata
        model_data_tmp['model_id'] = model_id_I;
        model_data_tmp['model_name'] = None;
        model_data_tmp['date'] = date_I;
        model_data_tmp['model_description'] = cobra_model.description;
        with open(filename_I, 'r') as f:
            model_data_tmp['model_file'] = f.read();
        model_data_tmp['file_type'] = 'sbml'
        model_data.append(model_data_tmp)
        reaction_data = [];
        # parse out reaction data
        for r in cobra_model.reactions:
            reaction_data_dict = {};
            reaction_data_dict['model_id'] = model_id_I
            reaction_data_dict['rxn_id'] = r.id
            reaction_data_dict['rxn_name'] = r.name
            reaction_data_dict['equation'] = r.build_reaction_string()
            reaction_data_dict['subsystem'] = r.subsystem
            reaction_data_dict['gpr'] = r.gene_reaction_rule
            reaction_data_dict['genes'] = []
            genes = r.genes;
            for g in genes:
                reaction_data_dict['genes'].append(g.id);
            reaction_data_dict['reactants_stoichiometry'] = [];
            reaction_data_dict['reactants_ids'] = [];
            reactants = r.reactants;
            for react in reactants:
                reaction_data_dict['reactants_stoichiometry'].append(r.get_coefficient(react.id));
                reaction_data_dict['reactants_ids'].append(react.id);
            reaction_data_dict['products_stoichiometry'] = [];
            reaction_data_dict['products_ids'] = [];
            products = r.products;
            for prod in products:
                reaction_data_dict['products_stoichiometry'].append(r.get_coefficient(prod.id));
                reaction_data_dict['products_ids'].append(prod.id);
            reaction_data_dict['lower_bound'] = r.lower_bound
            reaction_data_dict['upper_bound'] = r.upper_bound
            reaction_data_dict['objective_coefficient'] = r.objective_coefficient
            reaction_data_dict['flux_units'] = 'mmol*gDW-1*hr-1'
            reaction_data_dict['reversibility'] = r.reversibility
            #reaction_data_dict['reactants_stoichiometry_tracked'] = None;
            #reaction_data_dict['products_stoichiometry_tracked'] = None;
            #reaction_data_dict['reactants_ids_tracked'] = None;
            #reaction_data_dict['products_ids_tracked'] = None;
            #reaction_data_dict['reactants_mapping'] = None;
            #reaction_data_dict['products_mapping'] = None;
            #reaction_data_dict['rxn_equation'] = None;
            reaction_data_dict['fixed'] = None;
            reaction_data_dict['free'] = None;
            reaction_data_dict['weight'] = None;
            reaction_data_dict['used_'] = True
            reaction_data_dict['comment_'] = None;
            reaction_data.append(reaction_data_dict);
        metabolite_data = [];
        # parse out metabolite data
        for met in cobra_model.metabolites:
            metabolite_data_tmp = {};
            metabolite_data_tmp['model_id'] = model_id_I
            metabolite_data_tmp['met_name'] = met.name;
            metabolite_data_tmp['met_id'] = met.id;
            formula = {};
            for k,v in met.formula.elements.items():
                formula[k] = {0:v};
            tmp = Formula()
            tmp._elements=formula
            metabolite_data_tmp['formula'] = tmp.formula;
            metabolite_data_tmp['charge'] = met.charge
            metabolite_data_tmp['compartment'] = met.compartment
            metabolite_data_tmp['bound'] = met._bound
            metabolite_data_tmp['constraint_sense'] = met._constraint_sense
            #metabolite_data_tmp['met_elements'] = None;
            #metabolite_data_tmp['met_atompositions'] = None;
            #metabolite_data_tmp['balanced'] = None;
            #metabolite_data_tmp['met_symmetry'] = None;
            #metabolite_data_tmp['met_symmetry_atompositions'] = None;
            metabolite_data_tmp['used_'] = True
            metabolite_data_tmp['comment_'] = None;
            metabolite_data.append(metabolite_data_tmp);

        return model_data,reaction_data,metabolite_data
    def _parse_isotopomer_mapping_csvToDict(self,filename_I):
        #Read in the isotopomer mappings
        # Output:
        # isotopomer_mapping = {
        #    'rxn_id':{'reactants_mapping':reactants_mapping,
        #              'reactants_stoichiometry_tracked':reactants_stoichiometry_tracked,
        #              'reactants_ids_tracked':reactants_ids_tracked,
        #              'products_mapping':products_mapping,
        #              'products_stoichiometry_tracked':products_stoichiometry_tracked,
        #              'products_ids_tracked':products_ids_tracked};
        
        isotopomer_mapping = {};
        with open(filename_I,mode='r') as infile:
            reader = csv.DictReader(infile);
            for r in reader:
                reactants_mapping = r['reactants_mapping'].strip().split('+');
                reactants_stoichiometry_tracked = [];
                reactants_ids_tracked = [];
                #print r['reactants_ids_tracked']
                reactants = r['reactants_ids_tracked'].strip().split('+');
                reactants_elements_tracked = [];
                if reactants and reactants[0]:
                    for react in reactants:
                        tmp = react.split('*');
                        reactants_stoichiometry_tracked.append(-abs(float(tmp[0]))); #ensure it is negative!
                        reactants_ids_tracked.append(tmp[1]);
                        reactants_elements_tracked.append(r['reactants_elements_tracked']);
                products_mapping = r['products_mapping'].strip().split('+');
                products_stoichiometry_tracked = [];
                products_ids_tracked = [];
                products = r['products_ids_tracked'].strip().split('+');
                #print r['products_ids_tracked']
                products_elements_tracked = [];
                if products and products[0]:
                    for prod in products:
                        tmp = prod.split('*');
                        products_stoichiometry_tracked.append(float(tmp[0]));
                        products_ids_tracked.append(tmp[1]);
                        products_elements_tracked.append(r['products_elements_tracked']);
                isotopomer_mapping[r['rxn_id']] = {'reactants_mapping':reactants_mapping,
                                                   'rxn_id':r['rxn_id'],
                                                   'reactants_stoichiometry_tracked':reactants_stoichiometry_tracked,
                                                   'reactants_ids_tracked':reactants_ids_tracked,
                                                   'reactants_elements_tracked':reactants_elements_tracked,
                                                   'products_mapping':products_mapping,
                                                   'products_stoichiometry_tracked':products_stoichiometry_tracked,
                                                   'products_ids_tracked':products_ids_tracked,
                                                   'products_elements_tracked':products_ids_tracked,
                                                   'mapping_id':r['mapping_id'],
                                                   'rxn_equation':r['rxn_equation'],
                                                   'rxn_description':r['rxn_description'],
                                                   'used_':r['used_'],
                                                   'comment_':r['comment_']};
        return isotopomer_mapping
    def _parse_isotopomer_mapping_csv(self,filename_I):
        #Read in the isotopomer mappings
        
        isotopomer_mapping = [];
        with open(filename_I,mode='r') as infile:
            reader = csv.DictReader(infile);
            for r in reader:
                reactants_mapping = r['reactants_mapping'].strip().split('+');
                reactants_stoichiometry_tracked = [];
                reactants_ids_tracked = [];
                #print r['reactants_ids_tracked']
                reactants = r['reactants_ids_tracked'].strip().split('+');
                reactants_elements_tracked = [];
                if reactants and reactants[0]:
                    for react in reactants:
                        tmp = react.split('*');
                        reactants_stoichiometry_tracked.append(-abs(float(tmp[0]))); #ensure it is negative!
                        reactants_ids_tracked.append(tmp[1]);
                        reactants_elements_tracked.append(r['reactants_elements_tracked']);
                products_mapping = r['products_mapping'].strip().split('+');
                products_stoichiometry_tracked = [];
                products_ids_tracked = [];
                products = r['products_ids_tracked'].strip().split('+');
                #print r['products_ids_tracked']
                products_elements_tracked = [];
                if products and products[0]:
                    for prod in products:
                        tmp = prod.split('*');
                        products_stoichiometry_tracked.append(float(tmp[0]));
                        products_ids_tracked.append(tmp[1]);
                        products_elements_tracked.append(r['products_elements_tracked']);
                isotopomer_mapping.append({'reactants_mapping':reactants_mapping,
                                                   'rxn_id':r['rxn_id'],
                                                   'reactants_stoichiometry_tracked':reactants_stoichiometry_tracked,
                                                   'reactants_ids_tracked':reactants_ids_tracked,
                                                   'reactants_elements_tracked':reactants_elements_tracked,
                                                   'products_mapping':products_mapping,
                                                   'products_stoichiometry_tracked':products_stoichiometry_tracked,
                                                   'products_ids_tracked':products_ids_tracked,
                                                   'products_elements_tracked':products_elements_tracked,
                                                   'mapping_id':r['mapping_id'],
                                                   'rxn_equation':r['rxn_equation'],
                                                   'rxn_description':r['rxn_description'],
                                                   'used_':r['used_'],
                                                   'comment_':r['comment_']});
        return isotopomer_mapping
    def _parse_model_json(self,model_id_I,date_I,filename_I):
        # Read in the sbml file and define the model conditions
        cobra_model = load_json_model(filename_I);
        model_data = [];
        model_data_tmp = {};
        # parse out model metadata
        model_data_tmp['model_id'] = model_id_I;
        model_data_tmp['model_name'] = None;
        model_data_tmp['date'] = date_I;
        model_data_tmp['model_description'] = cobra_model.description;
        with open(filename_I, 'r') as f:
            model_data_tmp['model_file'] = f.read();
        model_data_tmp['file_type'] = 'json'
        model_data.append(model_data_tmp)
        reaction_data = [];
        # parse out reaction data
        for r in cobra_model.reactions:
            reaction_data_dict = {};
            reaction_data_dict['model_id'] = model_id_I
            reaction_data_dict['rxn_id'] = r.id
            reaction_data_dict['rxn_name'] = r.name
            reaction_data_dict['equation'] = r.build_reaction_string()
            reaction_data_dict['subsystem'] = r.subsystem
            reaction_data_dict['gpr'] = r.gene_reaction_rule
            reaction_data_dict['genes'] = []
            genes = r.genes;
            for g in genes:
                reaction_data_dict['genes'].append(g.id);
            reaction_data_dict['reactants_stoichiometry'] = [];
            reaction_data_dict['reactants_ids'] = [];
            reactants = r.reactants;
            for react in reactants:
                reaction_data_dict['reactants_stoichiometry'].append(r.get_coefficient(react.id));
                reaction_data_dict['reactants_ids'].append(react.id);
            reaction_data_dict['products_stoichiometry'] = [];
            reaction_data_dict['products_ids'] = [];
            products = r.products;
            for prod in products:
                reaction_data_dict['products_stoichiometry'].append(r.get_coefficient(prod.id));
                reaction_data_dict['products_ids'].append(prod.id);
            reaction_data_dict['lower_bound'] = r.lower_bound
            reaction_data_dict['upper_bound'] = r.upper_bound
            reaction_data_dict['objective_coefficient'] = r.objective_coefficient
            reaction_data_dict['flux_units'] = 'mmol*gDW-1*hr-1'
            reaction_data_dict['reversibility'] = r.reversibility
            #reaction_data_dict['reactants_stoichiometry_tracked'] = None;
            #reaction_data_dict['products_stoichiometry_tracked'] = None;
            #reaction_data_dict['reactants_ids_tracked'] = None;
            #reaction_data_dict['products_ids_tracked'] = None;
            #reaction_data_dict['reactants_mapping'] = None;
            #reaction_data_dict['products_mapping'] = None;
            #reaction_data_dict['rxn_equation'] = None;
            reaction_data_dict['fixed'] = None;
            reaction_data_dict['free'] = None;
            reaction_data_dict['weight'] = None;
            reaction_data_dict['used_'] = True
            reaction_data_dict['comment_'] = None;
            reaction_data.append(reaction_data_dict);
        metabolite_data = [];
        # parse out metabolite data
        for met in cobra_model.metabolites:
            metabolite_data_tmp = {};
            metabolite_data_tmp['model_id'] = model_id_I
            metabolite_data_tmp['met_name'] = met.name;
            metabolite_data_tmp['met_id'] = met.id;
            if met.formula:
                if met.formula != 'None' and met.formula.formula != 'None' and not 'X' in met.formula.formula:
                    try:
                        tmp = Formula(met.formula.formula);
                        metabolite_data_tmp['formula'] = tmp.formula;
                    except Exception as e:
                        print(e);
                        print(met.id)
                        metabolite_data_tmp['formula']= met.formula.formula;
                else: 
                    metabolite_data_tmp['formula'] = met.formula.formula;
            else: 
                metabolite_data_tmp['formula'] = None;
            metabolite_data_tmp['charge'] = met.charge
            metabolite_data_tmp['compartment'] = met.compartment
            metabolite_data_tmp['bound'] = met._bound
            metabolite_data_tmp['constraint_sense'] = met._constraint_sense
            #metabolite_data_tmp['met_elements'] = None;
            #metabolite_data_tmp['met_atompositions'] = None;
            metabolite_data_tmp['balanced'] = None;
            metabolite_data_tmp['fixed'] = None;
            #metabolite_data_tmp['met_symmetry'] = None;
            #metabolite_data_tmp['met_symmetry_atompositions'] = None;
            metabolite_data_tmp['used_'] = True
            metabolite_data_tmp['comment_'] = None;
            metabolite_data_tmp['lower_bound'] = None;
            metabolite_data_tmp['upper_bound'] = None;

            metabolite_data.append(metabolite_data_tmp);

        return model_data,reaction_data,metabolite_data
    def create_modelFromReactionsAndMetabolitesTables(self,rxns_table_I,mets_table_I):
        '''generate a cobra model from isotopomer_modelReactions and isotopomer_modelMetabolites tables'''
        
        cobra_model = Model(rxns_table_I[0]['model_id']);
        for rxn_cnt,rxn_row in enumerate(rxns_table_I):
            #if rxn_row['rxn_id'] == 'HEX1':
            #    print 'check'
            mets = {}
            print(rxn_row['rxn_id'])
            # parse the reactants
            for rxn_met_cnt,rxn_met in enumerate(rxn_row['reactants_ids']):
                for met_cnt,met_row in enumerate(mets_table_I):
                    if met_row['met_id']==rxn_met:# and met_row['balanced']:
                        compartment = met_row['compartment']
                        if not compartment:
                            met_id_tmp = met_row['met_id'].split('.')[0]
                            compartment = met_id_tmp.split('_')[-1];
                        met_tmp = Metabolite(met_row['met_id'],met_row['formula'],met_row['met_name'],compartment)
                        met_tmp.charge = met_row['charge']
                        # check for duplicate metabolites
                        met_keys = list(mets.keys());
                        met_keys_ids = {};
                        if met_keys: 
                            for cnt,met in enumerate(met_keys):
                                met_keys_ids[met.id]=cnt;
                        if met_tmp.id in list(met_keys_ids.keys()):
                            mets[met_keys[met_keys_ids[met_tmp.id]]]-=1
                        else:
                            mets[met_tmp] = rxn_row['reactants_stoichiometry'][rxn_met_cnt];
                        break;
            # parse the products
            for rxn_met_cnt,rxn_met in enumerate(rxn_row['products_ids']):
                for met_cnt,met_row in enumerate(mets_table_I):
                    if met_row['met_id']==rxn_met:# and met_row['balanced']:
                        compartment = met_row['compartment']
                        if not compartment:
                            met_id_tmp = met_row['met_id'].split('.')[0]
                            compartment = met_id_tmp.split('_')[-1];
                        met_tmp = Metabolite(met_row['met_id'],met_row['formula'],met_row['met_name'],compartment)
                        met_tmp.charge = met_row['charge']
                        # check for duplicate metabolites
                        met_keys = list(mets.keys());
                        met_keys_ids = {};
                        if met_keys: 
                            for cnt,met in enumerate(met_keys):
                                met_keys_ids[met.id]=cnt;
                        if met_tmp.id in list(met_keys_ids.keys()):
                            mets[met_keys[met_keys_ids[met_tmp.id]]]+=1
                        else:
                            mets[met_tmp] = rxn_row['products_stoichiometry'][rxn_met_cnt];
                        break;
            rxn = None;
            rxn = Reaction(rxn_row['rxn_id']);
            rxn.add_metabolites(mets);
            rxn.lower_bound=rxn_row['lower_bound'];
            rxn.upper_bound=rxn_row['upper_bound'];
            rxn.subsystem=rxn_row['subsystem'];
            rxn.gpr=rxn_row['gpr'];
            rxn.objective_coefficient=rxn_row['objective_coefficient'];
            cobra_model.add_reactions([rxn]);
            cobra_model.repair();
        return cobra_model
    def test_model(self,cobra_model_I,ko_list=[],flux_dict={},description=None):
        '''simulate a cobra model'''

        cobra_model = cobra_model_I;
        # implement optimal KOs and flux constraints:
        for ko in ko_list:
            cobra_model.reactions.get_by_id(ko).lower_bound = 0.0;
            cobra_model.reactions.get_by_id(ko).upper_bound = 0.0;
        for rxn,flux in flux_dict.items():
            if rxn in cobra_model.reactions:
                cobra_model.reactions.get_by_id(rxn).lower_bound = flux['lb'];
                cobra_model.reactions.get_by_id(rxn).upper_bound = flux['ub'];
            else:
                print('rxn_id ' + rxn + ' not found.');
        # change description, if any:
        if description:
            cobra_model.description = description;
        # test for a solution:
        cobra_model.optimize();
        #cobra_model.optimize(solver='gurobi');
        if not cobra_model.solution.f:
            return False;
        else:
            print(cobra_model.solution.f);
            return True;
    def writeAndLoad_modelTable(self,cobra_model_table_I):
        '''Load a cobra model from models table'''
                           
        # write the model to a temporary file
        if cobra_model_table_I['file_type'] == 'sbml':
            with open('cobra_model_tmp.xml','w') as file:
                file.write(cobra_model_table_I['model_file']);
                file.close()
            cobra_model = None;
            cobra_model = create_cobra_model_from_sbml_file('cobra_model_tmp.xml', print_time=True);
        elif cobra_model_table_I['file_type'] == 'json':
            with open('cobra_model_tmp.json','w') as file:
                file.write(cobra_model_table_I['model_file']);
                file.close()
            cobra_model = None;
            cobra_model = load_json_model('cobra_model_tmp.json');
        else:
            print('file_type not supported')
            return None;
        return cobra_model;
    def constrain_modelModelVariables(self,cobra_model,
                          ko_list=[],flux_dict={}):
        '''Constrain the model
        INPUT:
        ko_list = list of reactions to constrain to zero flux
        flux_dict = dictionary of fluxes to constrain the model'''
        # Apply KOs, if any:
        for ko in ko_list:
            cobra_model.reactions.get_by_id(ko).lower_bound = 0.0;
            cobra_model.reactions.get_by_id(ko).upper_bound = 0.0;
        # Apply flux constraints, if any:
        for rxn,flux in flux_dict.items():
            cobra_model.reactions.get_by_id(rxn).lower_bound = flux['lb'];
            cobra_model.reactions.get_by_id(rxn).upper_bound = flux['ub'];