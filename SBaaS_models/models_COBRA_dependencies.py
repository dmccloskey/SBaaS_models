# Dependencies from cobra
from cobra.io.sbml import create_cobra_model_from_sbml_file, write_cobra_model_to_sbml_file
from cobra.manipulation.modify import convert_to_irreversible
from cobra import Model, Metabolite, Reaction
from cobra.io.json import load_json_model, save_json_model
# Resources
from molmass.molmass import Formula
# System dependencies
import re
import copy
class models_COBRA_dependencies():
    def _parse_model_sbml(self,model_id_I,date_I,filename_I):
        # Read in the sbml file
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
            metabolite_data_tmp['used_'] = True
            metabolite_data_tmp['comment_'] = None;
            metabolite_data.append(metabolite_data_tmp);

        return model_data,reaction_data,metabolite_data
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
    def format_metid(self,met_id_I,compartment_id_I):
        met_formatted = met_id_I
        met_formatted = re.sub('-','_DASH_',met_formatted)
        met_formatted = re.sub('[(]','_LPARANTHES_',met_formatted)
        met_formatted = re.sub('[)]','_RPARANTHES_',met_formatted)
        met_formatted +='_' + compartment_id_I;
        return met_formatted;
    def deformat_metid(self,met_id_I):
        met_deformatted = met_id_I
        met_deformatted = re.sub('_DASH_','-',met_deformatted)
        met_deformatted = re.sub('_LPARANTHES_','[(]',met_deformatted)
        met_deformatted = re.sub('_RPARANTHES_','[)]',met_deformatted)
        met_deformatted_lst = met_deformatted.split('_')[:-1]; #remove the compartment
        met_deformatted = '_'.join(met_deformatted_lst);
        return met_deformatted;
    def convert_metid2escherid(self,met_id_I):
        met_formatted = met_id_I;
        met_formatted = re.sub('_DASH_','__',met_formatted)
        met_formatted = re.sub('_LPARANTHES_','__',met_formatted)
        met_formatted = re.sub('_RPARANTHES_','__',met_formatted)
        return met_formatted;
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
    def load_model(self,model_file_name_I):
        '''load a cobra model from json or sbml
        INPUT:
        model_file_name_I = name of file
        OUTPUT:
        cobra_model
        '''
        
        cobra_model=None;
        # check for the file type
        if '.json' in model_file_name_I:
            # Read in the sbml file and define the model conditions
            cobra_model = load_json_model(model_file_name_I, print_time=True);
        elif '.xml' in model_file_name_I:
            # Read in the sbml file and define the model conditions
            cobra_model = create_cobra_model_from_sbml_file(model_file_name_I, print_time=True);
        else: 
            print('file type not supported');
        return cobra_model;
    def repair_irreversibleModel(self,cobra_model):
        '''Repair an irreversible model that does not contain the "reflection" note
        INPUT:
        cobra_model
        '''
        for rxn in cobra_model.reactions:
            if rxn.id.endswith('_reverse') and not "reflection" in rxn.notes:
                forward_rxn_id = rxn.id.replace('_reverse','');
                rxn.notes.update({"reflection":forward_rxn_id});
    def revert2reversible(self,cobra_model,ignore_reflection=False):
        '''custom implementation of revert_to_reversible'''
        if ignore_reflection:
            reverse_reactions = [x for x in cobra_model.reactions
                          if x.id.endswith('_reverse')]
        else:
            reverse_reactions = [x for x in cobra_model.reactions
                          if "reflection" in x.notes and
                          x.id.endswith('_reverse')]
        if len(reverse_reactions) == 0:
            return;
        for reverse in reverse_reactions:
            if ignore_reflection: 
                forward_rev = cobra_model.reactions.get_by_id(reverse.id)
                forward_id = forward_rev.id.replace('_reverse','');
            else: 
                forward_id = reverse.notes.pop("reflection")
            if forward_id in cobra_model.reactions:
                forward = cobra_model.reactions.get_by_id(forward_id);
                forward.lower_bound = -reverse.upper_bound
                if forward.upper_bound == 0 or reverse.upper_bound == 0.0:
                    forward.upper_bound = -reverse.lower_bound
            else:
                forward_rev = cobra_model.reactions.get_by_id(reverse.id)
                forward_id = forward_rev.id.replace('_reverse','');
                # Make the new reaction by flipping the forward and reverse
                forward_mets = {};
                for reactant in forward_rev.reactants:
                    forward_mets[cobra_model.metabolites.get_by_id(reactant.id)] = 1;
                for product in forward_rev.products:
                    forward_mets[cobra_model.metabolites.get_by_id(product.id)] = -1;
                forward = Reaction(forward_id);
                forward.add_metabolites(forward_mets);
                forward.lower_bound = -reverse.upper_bound
                forward.upper_bound = 0.0;
                # Add the new reaction to the model
                cobra_model.add_reaction(forward);
        cobra_model.remove_reactions(reverse_reactions)
        cobra_model.repair();
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
    def convert_lumpedRxn2IndividualRxn(self,net_rxn_I,individual_rxns_I):
        '''Convert lumped reactions to individual reactions
        INPUT:
        net_rxn_I = net rxn
        individual_rxns_I = list of individual reactions'''
        return;
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
    def _diagnose_modelLBAndUB_adjust(self,adjustment_cnt,adjustment_cnt_max,flux_dict,rxn_id,lower_bound,upper_bound):
        '''adjust the lb/ub'''
        if adjustment_cnt<adjustment_cnt_max:
            lb_new = flux_dict[rxn_id]['lb']-flux_dict[rxn_id]['stdev'];
            ub_new = flux_dict[rxn_id]['ub']+flux_dict[rxn_id]['stdev'];
            if lb_new < lower_bound:
                lb_new = lower_bound;
            if ub_new > upper_bound:
                ub_new = upper_bound;
            flux_dict[rxn_id]['lb'] = lb_new;
            flux_dict[rxn_id]['ub'] = ub_new;
            adjustment_cnt+=1;
        elif adjustment_cnt<adjustment_cnt_max*2:
            lb_new = flux_dict[rxn_id]['lb']-flux_dict[rxn_id]['stdev']*2;
            ub_new = flux_dict[rxn_id]['ub']+flux_dict[rxn_id]['stdev']*2;
            if lb_new < lower_bound:
                lb_new = lower_bound;
            if ub_new > upper_bound:
                ub_new = upper_bound;
            flux_dict[rxn_id]['lb'] = lb_new;
            flux_dict[rxn_id]['ub'] = ub_new;
            adjustment_cnt+=1;
        elif adjustment_cnt<adjustment_cnt_max*3:
            lb_new = flux_dict[rxn_id]['lb']-flux_dict[rxn_id]['stdev']*5;
            ub_new = flux_dict[rxn_id]['ub']+flux_dict[rxn_id]['stdev']*5;
            if lb_new < lower_bound:
                lb_new = lower_bound;
            if ub_new > upper_bound:
                ub_new = upper_bound;
            flux_dict[rxn_id]['lb'] = lb_new;
            flux_dict[rxn_id]['ub'] = ub_new;
            adjustment_cnt+=1;
        elif adjustment_cnt<adjustment_cnt_max*4:
            lb_new = flux_dict[rxn_id]['lb']-flux_dict[rxn_id]['stdev']*10;
            ub_new = flux_dict[rxn_id]['ub']+flux_dict[rxn_id]['stdev']*10;
            if lb_new < lower_bound:
                lb_new = lower_bound;
            if ub_new > upper_bound:
                ub_new = upper_bound;
            flux_dict[rxn_id]['lb'] = lb_new;
            flux_dict[rxn_id]['ub'] = ub_new;
            adjustment_cnt+=1;
        else:
            flux_dict[rxn_id]['lb'] = lower_bound;
            flux_dict[rxn_id]['ub'] = upper_bound;
            adjustment_cnt=0;
        return adjustment_cnt;
    def _diagnose_modelLBAndUB_1(self,cobra_model,ko_list,flux_dict,rxn_id,bad_lbub_1,
                                 adjustment_1_I,adjustment_cnt,adjustment_cnt_max=5,lower_bound=-1000.0,upper_bound=1000.0):
        '''Individual test and adjust each lb/ub'''

        cobra_model_copy = cobra_model.copy();
        test = False;
        try:
            test = self.test_model(cobra_model_I=cobra_model_copy,
                                                ko_list=ko_list,
                                                flux_dict={rxn_id:flux_dict[rxn_id]},
                                                description=None);
        except Exception as e:
            print(e);
        if not test:
            print('fluxes for rxn_id ' + rxn_id + ' break the model');
            if not rxn_id in bad_lbub_1:
               bad_lbub_1.append(rxn_id);
            # re-adjust the bounds:
            if adjustment_1_I:
                adjustment_cnt = self._diagnose_modelLBAndUB_adjust(adjustment_cnt,adjustment_cnt_max,flux_dict,rxn_id,lower_bound,upper_bound);
                self._diagnose_modelLBAndUB_1(cobra_model,ko_list,flux_dict,rxn_id,bad_lbub_1,adjustment_1_I,adjustment_cnt,adjustment_cnt_max,lower_bound,upper_bound);
                flux_dict[rxn_id]['used_']=True;
                flux_dict[rxn_id]['comment_']='adjusted';
            else:
                flux_dict[rxn_id]['used_']=False;
                flux_dict[rxn_id]['comment_']='breaks the model';
        else:
            adjustment_cnt=0;
            #return flux_dict;
    def _diagnose_modelLBAndUB_2(self,cobra_model,cobra_model_copy,ko_list,flux_dict,rxn_id,bad_lbub_2,
                                 adjustment_2_I,adjustment_cnt,adjustment_cnt_max=10,lower_bound=-1000.0,upper_bound=1000.0):
        '''Test and adjust each lb/ub incrementally'''
        test = False;
        try:
            test = self.test_model(cobra_model_I=cobra_model_copy,
                                                ko_list=ko_list,
                                                flux_dict={rxn_id:flux_dict[rxn_id]},
                                                description=None);
        except Exception as e:
            print(e);
        if not test:
            print('fluxes for rxn_id ' + rxn_id + ' break the model');
            if not rxn_id in bad_lbub_2:
                bad_lbub_2.append(rxn_id);
            # re-adjust the bounds:
            if adjustment_2_I:
                cobra_model_copy = cobra_model.copy();
                adjustment_cnt = self._diagnose_modelLBAndUB_adjust(adjustment_cnt,adjustment_cnt_max,flux_dict,rxn_id,lower_bound,upper_bound);
                self._diagnose_modelLBAndUB_2(cobra_model,cobra_model_copy,ko_list,flux_dict,rxn_id,bad_lbub_2,adjustment_cnt,adjustment_cnt_max,lower_bound,upper_bound);
                flux_dict[rxn_id]['used_']=True;
                flux_dict[rxn_id]['comment_']='adjusted';
            else:
                flux_dict[rxn_id]['used_']=False;
                flux_dict[rxn_id]['comment_']='breaks the model';
        else:
            cobra_model.reactions.get_by_id(rxn_id).lower_bound = flux_dict[rxn_id]['lb'];
            cobra_model.reactions.get_by_id(rxn_id).upper_bound = flux_dict[rxn_id]['ub'];
            adjustment_cnt=0;
            #return flux_dict,cobra_model;
    def diagnose_modelLBAndUB(self,cobra_model,ko_list,flux_dict,
                              adjustment_1_I=True,adjustment_2_I=True,
                              adjustment_cnt_max_I=5,lower_bound_I=-1000.0,upper_bound_I=1000.0):
        '''diagnose LB and UB constraints
        INPUT:
        adjustment_1_I = adjust bounds when diagnosing each lb/ub individually
        adjustment_2_I = adjust bounds when diagnosing each lb/ub cummulatively
                        if false, the reaction lb/ub will not be included
        adjustment_cnt_max_I = maximum number of adjustments that can be made for a single variable before
                             increasing to the next factor (+/- stdev, +/- stdev*2,+/- stdev*5,+/- stdev*10,+/- lower/upper_bound)
        lower_bound_I = maximum lower bound
        upper_bound_I = maximum upper bound'''

        summary_O = {};

        #check each flux individually
        rxn_ids = list(flux_dict.keys());
        rxn_ids.sort();
        bad_lbub_1 = [];
        for rxn_id in rxn_ids:
            print('checking bounds for flux ' + rxn_id);
            #adjustments are made in place
            adjustment_cnt=0;
            #flux_dict=self._diagnose_modelLBAndUB_1(cobra_model,ko_list,flux_dict,rxn_id,bad_lbub_1,adjustment_cnt,adjustment_cnt_max_I,lower_bound_I,upper_bound_I);
            self._diagnose_modelLBAndUB_1(cobra_model,ko_list,flux_dict,rxn_id,bad_lbub_1,adjustment_1_I,adjustment_cnt,adjustment_cnt_max_I,lower_bound_I,upper_bound_I);
        #add in each flux lb/ub 1 by 1
        bad_lbub_2 = [];
        cobra_model_copy = cobra_model.copy();
        for rxn_id in rxn_ids:
            #if rxn_id in bad_lbub_1: continue;
            print('checking bounds for flux ' + rxn_id);
            adjustment_cnt=0;
            #flux_dict,cobra_model=self._diagnose_modelLBAndUB_2(cobra_model,cobra_model_copy,ko_list,flux_dict,rxn_id,bad_lbub_2,adjustment_cnt,adjustment_cnt_max_I,lower_bound_I,upper_bound_I);
            self._diagnose_modelLBAndUB_2(cobra_model,cobra_model_copy,ko_list,flux_dict,rxn_id,bad_lbub_2,adjustment_cnt,adjustment_cnt_max_I,lower_bound_I,upper_bound_I);
        # record the variables
        summary_O['bad_lbub_1']=bad_lbub_1;
        summary_O['bad_lbub_2']=bad_lbub_2;
        return summary_O;

    def find_shortestPath_nodes(self,
            graph_I,node_start_I,node_stop_I,
            algorithm_I='astar_path_length',params_I={},
            ):
        '''Find the minimum node distance between two metabolites
        INPUT:
        graph_I: list of dictionaries with keys for 'left', 'right', and 'weight' [list]
        cobra_model_I: cobra model object [class]
        node_start_I: metabolite id source [string]
        node_stop_I: metabolite id sink [string]
        algorithmn_I: search algorith to use [string]
            list of algorithms: http://networkx.readthedocs.io/en/networkx-1.11/reference/algorithms.shortest_paths.html
        params_I: list of additional parameters to pass to the shortest path algorithm
        OUTPUT:
        nodeDist_O: dictionary of metabolite ids and distances
            {met_id [string]: distance [float]}
        NOTES: http://networkx.readthedocs.io/en/networkx-1.11/tutorial/tutorial.html
        import networkx as nx
        G = nx.DiGraph()
        G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
        astar_path_length(G, source, target, heuristic=None, weight='weight')

        '''
        distance_O = None;
        #instantiate the networkx graph utility
        import networkx as nx
        G = nx.DiGraph()
        #build the networkx graph
        nx_input = [(row['left'],row['right'],row) for row in graph_I];
        G.add_edges_from(nx_input);
        #call the algorithm
        if hasattr(nx, algorithm_I):
            algorithm = getattr(nx,algorithm_I);
            distance_O = algorithm(G, node_start_I, node_stop_I, **params_I)
        else:
            print('shortest path algorithm not recognized');
        return distance_O;
    def convert_modelReactionsTable2DirectedAcyclicGraph(
            self,rxns_I,
            weights_I=None,
            attributes_I=[],
            exclusion_list_I=[]):
        '''Convert a cobramodel to a directed acyclic graph
        INPUT:
        rxns_I: list of cobra model reactions [list]
        attributes_I = list of other keys to add in to each element of the output list [string]
        weights_I = edge weights
            [string]: column id to use as the weight
            [dict]: {rxn_id [string]: weight [float]}
            [None]: default, 1.0 (i.e., unit weight)
        exclusion_list_I = [list of nodes to exclude]
        OUTPUT:
        cobra_model_graph_O: [{left:[string],right:[string],weight:[float]}]
        '''
        cobra_model_graph_O = [];
        for rxn in rxns_I:
            if rxn['rxn_id'] in exclusion_list_I: continue;
            if not weights_I:
                weight = 1.0;
            elif type(weights_I)==type(''):
                weight = rxn[weights_I];
            elif type(weights_I)==type({}) and rxn['rxn_id'] in weights_I.keys():
                weight = weights_I[rxn['rxn_id']];
            else: 
                weight = 1.0;
            if weight <= 0: continue;
            for reactant in rxn['reactants_ids']:
                if reactant in exclusion_list_I: continue;
                for product in rxn['products_ids']:
                    if product in exclusion_list_I: continue;
                    tmp = {};
                    # add in other attributes
                    if attributes_I:
                        for attr in attributes_I:
                            tmp[attr]=rx[attr];
                    if weight > 0:
                        # add in weights
                        tmp['weight']=weight;
                        # define the left and right nodes
                        tmp1 = copy.copy(tmp)
                        tmp1['left']=reactant;
                        tmp1['right']=rxn['rxn_id'];
                        cobra_model_graph_O.append(tmp1);
                        tmp1 = copy.copy(tmp)
                        tmp1['left']=rxn['rxn_id'];
                        tmp1['right']=product;
                        cobra_model_graph_O.append(tmp1);
                        ## check for reversibility
                        #if rxn['reversibility']:
                        #    tmp1 = copy.copy(tmp)
                        #    tmp1['left']=product;
                        #    tmp1['right']=rxn['rxn_id'];
                        #    cobra_model_graph_O.append(tmp1);
                        #    tmp1 = copy.copy(tmp)
                        #    tmp1['left']=rxn['rxn_id'];
                        #    tmp1['right']=reactant;
                    elif weight < 0:
                        # add in weights
                        tmp['weight']=-weight;
                        # define the left and right nodes
                        tmp1 = copy.copy(tmp)
                        tmp1['left']=product;
                        tmp1['right']=rxn['rxn_id'];
                        cobra_model_graph_O.append(tmp1);
                        tmp1 = copy.copy(tmp)
                        tmp1['left']=rxn['rxn_id'];
                        tmp1['right']=reactant;
                        cobra_model_graph_O.append(tmp1);
                        ## check for reversibility
                        #if rxn['reversibility']:
                        #    tmp1 = copy.copy(tmp)
                        #    tmp1['left']=reactant;
                        #    tmp1['right']=rxn['rxn_id'];
                        #    cobra_model_graph_O.append(tmp1);
                        #    tmp1 = copy.copy(tmp)
                        #    tmp1['left']=rxn['rxn_id'];
                        #    tmp1['right']=product;

        return cobra_model_graph_O;


                        

        