from .models_MFA_dependencies import models_MFA_dependencies
from .models_MFA_query import models_MFA_query
from SBaaS_base.sbaas_template_io import sbaas_template_io

class models_MFA_io(models_MFA_query,
                    models_MFA_dependencies,
                    sbaas_template_io):
    def import_dataStage02IsotopomerModel_sbml(self, model_id_I, date_I, model_sbml):
        '''import isotopomer model from file'''
        dataStage02IsotopomerModelRxns_data = [];
        dataStage02IsotopomerModelMets_data = [];
        dataStage02IsotopomerModels_data,\
            dataStage02IsotopomerModelRxns_data,\
            dataStage02IsotopomerModelMets_data = self._parse_model_sbml(model_id_I, date_I, model_sbml)
        self.add_data_stage02_isotopomer_modelMetabolites(dataStage02IsotopomerModelMets_data);
        self.add_data_stage02_isotopomer_modelReactions(dataStage02IsotopomerModelRxns_data);
        self.add_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);
    def import_dataStage02IsotopomerModel_json(self, model_id_I, date_I, model_json):
        '''import isotopomer model from file'''
        dataStage02IsotopomerModelRxns_data = [];
        dataStage02IsotopomerModelMets_data = [];
        dataStage02IsotopomerModels_data,\
            dataStage02IsotopomerModelRxns_data,\
            dataStage02IsotopomerModelMets_data = self._parse_model_json(model_id_I, date_I, model_json)
        self.add_data_stage02_isotopomer_modelMetabolites(dataStage02IsotopomerModelMets_data);
        self.add_data_stage02_isotopomer_modelReactions(dataStage02IsotopomerModelRxns_data);
        self.add_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);
    def import_dataStage02IsotopomerModelAtomMapping_sbmlAndCsv(self, model_id_I, date_I, model_sbml, isotopomer_mapping):
        '''import isotopomer model from file'''
        dataStage02IsotopomerModels_data = [];
        dataStage02IsotopomerModelRxns_data_tmp = [];
        dataStage02IsotopomerModelMets_data = [];
        dataStage02IsotopomerModels_data,\
            dataStage02IsotopomerModelRxns_data_tmp,\
            dataStage02IsotopomerModelMets_data = self._parse_model_sbml(model_sbml)
        isotopomer_mapping_data = self._parse_isotopomer_mapping_csvToDict(isotopomer_mapping)
        # combine model_data and isotopomer_mapping_data
        dataStage02IsotopomerModelRxns_data = [];
        for r in dataStage02IsotopomerModelRxns_data_tmp:
            if r['rxn_id'] in isotopomer_mapping_data:
                r['reactants_stoichiometry_tracked'] = isotopomer_mapping_data[r['rxn_id']]['reactants_stoichiometry_tracked'];
                r['products_stoichiometry_tracked'] = isotopomer_mapping_data[r['rxn_id']]['products_stoichiometry_tracked'];
                r['reactants_ids_tracked'] = isotopomer_mapping_data[r['rxn_id']]['reactants_ids_tracked'];
                r['products_ids_tracked'] = isotopomer_mapping_data[r['rxn_id']]['products_ids_tracked'];
                r['reactants_mapping'] = isotopomer_mapping_data[r['rxn_id']]['reactants_mapping'];
                r['products_mapping'] = isotopomer_mapping_data[r['rxn_id']]['products_mapping'];
                r['reactants_elements_tracked'] = isotopomer_mapping_data[r['rxn_id']]['reactants_elements_tracked'];
                r['products_elements_tracked'] = isotopomer_mapping_data[r['rxn_id']]['products_elements_tracked'];
                r['mapping_id'] = isotopomer_mapping_data[r['rxn_id']]['mapping_id'];
                r['rxn_equation'] = isotopomer_mapping_data[r['rxn_id']]['rxn_equation'];
                dataStage02sotopomerModelRxns_data.append(r);
        self.add_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);
        self.add_data_stage02_isotopomer_modelReactions(dataStage02IsotopomerModelRxns_tmp);
        self.add_data_stage02_isotopomer_modelMetabolites(dataStage02IsotopomerModelMets);
        self.add_data_stage02_isotopomer_atomMappingReactions(isotopomer_mapping_data);
    def import_dataStage02IsotopomerAtomMapping_csv(self, isotopomer_mapping):
        '''import isotopomer atom mapping from file'''
        isotopomer_mapping_data = self._parse_isotopomer_mapping_csv(isotopomer_mapping)
        self.add_data_stage02_isotopomer_atomMappingReactions(isotopomer_mapping_data);
    def export_data_stage02_isotopomer_models(self,model_id_I,filename_I):
        '''export the model to json or sbml'''

        cobra_model_sbml = None;
        cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id_I);
        # write the model to a temporary file
        if cobra_model_sbml['file_type'] == 'sbml':
            with open(filename_I,'w') as file:
                file.write(cobra_model_sbml['model_file']);
                file.close()
        elif cobra_model_sbml['file_type'] == 'json':
            with open(filename_I,'w') as file:
                file.write(cobra_model_sbml['model_file']);
                file.close()
        else:
            print('file_type not supported');
    
    def import_data_stage02_isotopomer_models_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_data_stage02_isotopomer_models(data.data);
        data.clear_data();
    def import_data_stage02_isotopomer_modelReactions_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_data_stage02_isotopomer_modelReactions(data.data);
        data.clear_data();
    def import_data_stage02_isotopomer_modelMetabolites_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_data_stage02_isotopomer_modelMetabolites(data.data);
        data.clear_data();
    def import_data_stage02_isotopomer_atomMappingReactions_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_data_stage02_isotopomer_atomMappingReactions(data.data);
    def import_data_stage02_isotopomer_atomMappingMetabolites_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_data_stage02_isotopomer_atomMappingMetabolites(data.data);
        data.clear_data(); 
    def import_data_stage02_isotopomer_atomMappingReactions_update(self, filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        #data.read_json(filename);
        data.format_data();
        self.update_data_stage02_isotopomer_atomMappingReactions(data.data);
        data.clear_data();
    def import_data_stage02_isotopomer_atomMappingMetabolites_update(self, filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        #data.read_json(filename);
        data.format_data();
        self.update_data_stage02_isotopomer_atomMappingMetabolites(data.data);
        data.clear_data();
    # TODO: refactor into multiple sub-functions
    def import_dataStage02IsotopomerModelAndAtomMappingReactions_INCA(self,model_id_I=None,mapping_id_I=None, date_I=None,
                                                                      model_INCA_I=None, model_rxn_conversion_I=None,
                                                                      model_met_conversion_I=None,model_rxn_CBM_I=None,
                                                                      element_tracked_I = 'C',
                                                                      add_model_I = True, add_rxns_I = True,
                                                                      add_mets_I = True, add_rxn_mappings_I=True,
                                                                      update_model_I = False, update_rxns_I = False,
                                                                      update_mets_I = False, update_rxn_mappings_I=False,
                                                                      addunique_mets_I = False):
        '''load and parse INCA isotopomer model (i.e., ecoli_inca01)
        INPUT:
        model_id_I
        mapping_id_I
        date_I
        model_INCA_I
        model_rxn_conversion_I
        model_met_conversion_I
        model_rxn_CBM_I
        element_tracked_I
        add_model_I
        add_rxns_I
        add_mets_I
        add_rxn_mappings_I
        update_model_I
        update_rxns_I
        update_mets_I
        update_rxn_mappings_I
        addunique_mets_I

        TODO: add in ability to parse elements/mapping in use cases such as '(C1:a,C2:b1,C3:c2)' or '(C1:a,C2:b3,H1:d)' '''

        #read in the data:
        model_INCA = {};
        model_rxn_conversion = {};
        model_met_conversion = {};
        model_rxn_cbm = {};

        data = base_importData();
        data.read_csv(model_INCA_I);
        for d in data.data:
            model_INCA[d['rxn_id_INCA']]=d['rxn_equation_INCA'];
            #model_INCA.append(d);
        data.clear_data();

        if model_rxn_conversion_I:
            data = base_importData();
            data.read_csv(model_rxn_conversion_I);
            for d in data.data:
                model_rxn_conversion[d['rxn_id_INCA']]=d['rxn_id'];
            data.clear_data();

        if model_met_conversion_I:
            data = base_importData();
            data.read_csv(model_met_conversion_I);
            for d in data.data:
                model_met_conversion[d['met_id_INCA']]=d['met_id'];
            data.clear_data();

        if model_rxn_CBM_I:
            data = base_importData();
            data.read_csv(model_rxn_CBM_I);
            for d in data.data:
                genes = [];
                genes_str = d['genes'];
                genes = genes_str.replace('{','').replace('}','').split(',');
                fixed =None;
                if d['fixed']: fixed = d['fixed']
                free= None;
                if d['free']: free = d['free']
                weight = None;
                if d['weight']:  weight = d['weight']
                model_rxn_cbm[d['rxn_id_INCA']]={'comment_':d['comment_'],
                    'lower_bound':float(d['lower_bound']),
                    'upper_bound':float(d['upper_bound']),
                    'objective_coefficient':float(d['objective_coefficient']),
                    'subsystem':d['subsystem'],'gpr':d['gpr'],'genes':genes,
                    'flux_units':d['flux_units'],'fixed':fixed,'free':free,'weight': weight,
                    'used_':d['used_'],'reversibility':d['reversibility'],
                    };
            data.clear_data();

        modelReactions = [];
        atomMappingReactions = [];
        atomMappingReactions_reverse = [];
        model_met_ids = [];
        #parse the rxn network into modelReactions and atomMappingReactions
        for id,rxn_eqn in model_INCA.items():
            #if id == 'HEX1':
            #    print 'check'
            #initialize the data structure for modelReactions:
            modelReactions_row = {};
            modelReactions_row['model_id']=model_id_I;
            if model_rxn_conversion_I: modelReactions_row['rxn_id']=model_rxn_conversion[id];
            else: modelReactions_row['rxn_id']=id;
            modelReactions_row['equation']=None;
            modelReactions_row['subsystem']=None;
            modelReactions_row['gpr']=None;
            modelReactions_row['genes']=None;
            modelReactions_row['reactants_stoichiometry']=[];
            modelReactions_row['products_stoichiometry']=[];
            modelReactions_row['reactants_ids']=[];
            modelReactions_row['products_ids']=[];
            if model_rxn_CBM_I:
                modelReactions_row['subsystem']=model_rxn_cbm[id]['subsystem'];
                modelReactions_row['gpr']=model_rxn_cbm[id]['gpr'];
                modelReactions_row['genes']=model_rxn_cbm[id]['genes'];
                modelReactions_row['lower_bound']=model_rxn_cbm[id]['lower_bound'];
                modelReactions_row['upper_bound']=model_rxn_cbm[id]['upper_bound'];
                modelReactions_row['objective_coefficient']=model_rxn_cbm[id]['objective_coefficient'];
                modelReactions_row['flux_units']=model_rxn_cbm[id]['flux_units'];
                modelReactions_row['fixed']=model_rxn_cbm[id]['fixed'];
                modelReactions_row['free']=model_rxn_cbm[id]['free'];
                modelReactions_row['reversibility']=model_rxn_cbm[id]['reversibility'];
                modelReactions_row['weight']=model_rxn_cbm[id]['weight'];
                modelReactions_row['used_']=model_rxn_cbm[id]['used_'];
                modelReactions_row['comment_']=model_rxn_cbm[id]['comment_'];
            else:
                modelReactions_row['lower_bound']=-1000;
                modelReactions_row['upper_bound']=1000;
                if model_rxn_conversion[id]=='Ec_Biomass_INCA':
                    modelReactions_row['objective_coefficient']=1.0;
                else:
                    modelReactions_row['objective_coefficient']=0.0;
                modelReactions_row['flux_units']='mmol*gDW-1*hr-1';
                modelReactions_row['fixed']=None;
                modelReactions_row['free']=None;
                modelReactions_row['reversibility']=None;
                modelReactions_row['weight']=None;
                modelReactions_row['used_']=True;
                modelReactions_row['comment_']=None
            #initialize the data structure for atomMappingReactions:
            atomMappingReactions_row = {};
            atomMappingReactions_row['mapping_id']=mapping_id_I;
            if model_rxn_conversion_I: atomMappingReactions_row['rxn_id']=model_rxn_conversion[id];
            else: atomMappingReactions_row['rxn_id']=id;
            atomMappingReactions_row['rxn_description']='';
            atomMappingReactions_row['rxn_equation']=rxn_eqn;
            atomMappingReactions_row['reactants_stoichiometry_tracked']=[]
            atomMappingReactions_row['products_stoichiometry_tracked']=[]
            atomMappingReactions_row['reactants_ids_tracked']=[]
            atomMappingReactions_row['products_ids_tracked']=[]
            atomMappingReactions_row['reactants_elements_tracked']=[]
            atomMappingReactions_row['products_elements_tracked']=[]
            atomMappingReactions_row['reactants_positions_tracked']=[]
            atomMappingReactions_row['products_positions_tracked']=[]
            atomMappingReactions_row['reactants_mapping']=[]
            atomMappingReactions_row['products_mapping']=[]
            atomMappingReactions_row['used_']=True
            atomMappingReactions_row['comment_']=None
            #split into reactants and products and determine the reversibility
            model_INCA_reactants = '';
            model_INCA_products = '';
            rxn_eqn.strip();
            if '<->' in rxn_eqn or '<=>' in rxn_eqn:
                modelReactions_row['reversibility'] = True;
                if '<->' in rxn_eqn and rxn_eqn.split('<->')[0]: model_INCA_reactants = rxn_eqn.split('<->')[0];
                if '<->' in rxn_eqn and rxn_eqn.split('<->')[1]: model_INCA_products = rxn_eqn.split('<->')[1];
                if '<=>' in rxn_eqn and rxn_eqn.split('<=>')[0]: model_INCA_reactants = rxn_eqn.split('<=>')[0];
                if '<=>' in rxn_eqn and rxn_eqn.split('<=>')[1]: model_INCA_products = rxn_eqn.split('<=>')[1];
                if not model_rxn_CBM_I: 
                    modelReactions_row['lower_bound']=-1000;
                    modelReactions_row['upper_bound']=1000;
            elif '->' in rxn_eqn or '-->' in rxn_eqn:
                modelReactions_row['reversibility'] = False;
                if '-->' in rxn_eqn:
                    if rxn_eqn.split('-->')[0]: model_INCA_reactants = rxn_eqn.split('-->')[0];
                    if rxn_eqn.split('-->')[1]: model_INCA_products = rxn_eqn.split('-->')[1];
                else:
                    if rxn_eqn.split('->')[0]: model_INCA_reactants = rxn_eqn.split('->')[0];
                    if rxn_eqn.split('->')[1]: model_INCA_products = rxn_eqn.split('->')[1];
                if not model_rxn_CBM_I: 
                    modelReactions_row['lower_bound']=0;
                    modelReactions_row['upper_bound']=1000;
            else:
                print('no valid forward/reverse reaction identifier found')
            #parse the reactants
            met_id_tmp = None;
            met_stoichiometry_tmp = None;
            model_INCA_reactants_list = model_INCA_reactants.replace('*',' ').split(' ')
            rxn_mapping_bool = False;
            rxn_mapping_str = '';
            pos_cnt = 0;
            positions = [];
            elements = [];
            for rxn_token in model_INCA_reactants_list:
                #check for extra whitespace
                if rxn_token == '' or rxn_token == ' ': continue;
                #check for mapping
                elif ')' in rxn_token:
                    rxn_mapping = rxn_token.strip(')');
                    #TODO: will break on use cases such as '(C1:a C2:b1 C3:c2)'
                    if ':' in rxn_mapping:
                        rxn_mapping = rxn_mapping.split(':')[1];
                    atomMappingReactions_row['reactants_ids_tracked'].append(met_id_tmp);
                    atomMappingReactions_row['reactants_stoichiometry_tracked'].append(met_stoichiometry_tmp);
                    rxn_mapping_str+= '['+rxn_mapping+']';
                    elements.append(element_tracked_I);
                    positions.append(pos_cnt);
                    atomMappingReactions_row['reactants_positions_tracked'].append(positions)
                    atomMappingReactions_row['reactants_elements_tracked'].append(elements)
                    rxn_mapping_bool = False;
                    atomMappingReactions_row['reactants_mapping'].append(rxn_mapping_str);
                    rxn_mapping_str='';
                    pos_cnt=0;
                    positions = [];
                    elements = [];
                elif rxn_mapping_bool:
                    #TODO: will break on use cases such as '(C1:a C2:b1 C3:c2)'
                    rxn_mapping = rxn_token;
                    if ':' in rxn_mapping:
                        rxn_mapping = rxn_mapping.split(':')[1];
                    rxn_mapping_str+= '['+rxn_mapping+']';
                    elements.append(element_tracked_I);
                    positions.append(pos_cnt);
                    pos_cnt+=1;
                elif '(' in rxn_token:
                    rxn_mapping = rxn_token.strip('(');
                    #TODO: will break on use cases such as '(C1:a C2:b1 C3:c2)'
                    if ':' in rxn_mapping:
                        rxn_mapping = rxn_mapping.split(':')[1];
                    rxn_mapping_str+= '['+rxn_mapping+']';
                    elements.append(element_tracked_I);
                    positions.append(pos_cnt);
                    rxn_mapping_bool = True;
                    pos_cnt+=1;
                #check for stoichiometry
                elif rxn_token.replace('.','').replace('-','').replace('E','').isdigit():
                    met_stoichiometry_tmp = -abs(float(rxn_token));
                    modelReactions_row['reactants_stoichiometry'].append(met_stoichiometry_tmp)
                #check for the next metabolite
                elif '+' in rxn_token:
                    met_id_tmp = None;
                    met_stoichiometry_tmp = None;
                #met_id
                else:
                    if model_met_conversion_I: met_id_tmp = model_met_conversion[rxn_token.strip()];
                    else: met_id_tmp = rxn_token.strip();
                    modelReactions_row['reactants_ids'].append(met_id_tmp)
                    model_met_ids.append(met_id_tmp)
                    if not met_stoichiometry_tmp: #implicit stoichiometry of 1
                        met_stoichiometry_tmp = -1.0;
                        modelReactions_row['reactants_stoichiometry'].append(met_stoichiometry_tmp);
            #parse the products
            met_id_tmp = None;
            met_stoichiometry_tmp = None;
            model_INCA_products_list = model_INCA_products.replace('*',' ').split(' ')
            rxn_mapping_bool = False;
            rxn_mapping_str = '';
            pos_cnt = 0;
            positions = [];
            elements = [];
            for rxn_token in model_INCA_products_list:
                #check for extra whitespace
                if rxn_token == '' or rxn_token == ' ': continue;
                #check for mapping
                elif ')' in rxn_token:
                    rxn_mapping = rxn_token.strip(')');
                    #TODO: will break on use cases such as '(C1:a C2:b1 C3:c2)'
                    if ':' in rxn_mapping:
                        rxn_mapping = rxn_mapping.split(':')[1];
                    atomMappingReactions_row['products_ids_tracked'].append(met_id_tmp);
                    atomMappingReactions_row['products_stoichiometry_tracked'].append(met_stoichiometry_tmp);
                    rxn_mapping_str+= '['+rxn_mapping+']';
                    elements.append(element_tracked_I);
                    positions.append(pos_cnt);
                    atomMappingReactions_row['products_positions_tracked'].append(positions)
                    atomMappingReactions_row['products_elements_tracked'].append(elements)
                    rxn_mapping_bool = False;
                    atomMappingReactions_row['products_mapping'].append(rxn_mapping_str);
                    rxn_mapping_str='';
                    pos_cnt=0;
                    positions = [];
                    elements = [];
                elif rxn_mapping_bool:
                    rxn_mapping = rxn_token;
                    #TODO: will break on use cases such as '(C1:a C2:b1 C3:c2)'
                    if ':' in rxn_mapping:
                        rxn_mapping = rxn_mapping.split(':')[1];
                    rxn_mapping_str+= '['+rxn_mapping+']';
                    elements.append(element_tracked_I);
                    positions.append(pos_cnt);
                    pos_cnt+=1;
                elif '(' in rxn_token:
                    rxn_mapping = rxn_token.strip('(');
                    #TODO: will break on use cases such as '(C1:a C2:b1 C3:c2)'
                    if ':' in rxn_mapping:
                        rxn_mapping = rxn_mapping.split(':')[1];
                    rxn_mapping_str+= '['+rxn_mapping+']';
                    elements.append(element_tracked_I);
                    positions.append(pos_cnt);
                    rxn_mapping_bool = True;
                    pos_cnt+=1;
                #check for stoichiometry
                elif rxn_token.replace('.','').replace('-','').replace('E','').isdigit():
                    met_stoichiometry_tmp = abs(float(rxn_token));
                    modelReactions_row['products_stoichiometry'].append(met_stoichiometry_tmp)
                #check for the next metabolite
                elif '+' in rxn_token:
                    met_id_tmp = None;
                    met_stoichiometry_tmp = None;
                #met_id
                else:
                    if model_met_conversion_I: met_id_tmp = model_met_conversion[rxn_token.strip()];
                    else: met_id_tmp = rxn_token.strip();
                    modelReactions_row['products_ids'].append(met_id_tmp)
                    model_met_ids.append(met_id_tmp)
                    if not met_stoichiometry_tmp: #implicit stoichiometry of 1
                        met_stoichiometry_tmp = 1.0;
                        modelReactions_row['products_stoichiometry'].append(met_stoichiometry_tmp);
            #met_id_tmp = None;
            #met_stoichiometry_tmp = None;
            #for rxn_token in model_INCA_products.replace('*',' ').split(' '):
            #    #check for extra whitespace
            #    if rxn_token == '' or rxn_token == ' ': continue;
            #    #check for mapping
            #    elif '(' in rxn_token or ')' in rxn_token:
            #        rxn_mapping = rxn_token.strip('(').strip(')');
            #        #TODO: will break on use cases such as '(C1:a,C2:b1,C3:c2)'
            #        if ':' in rxn_mapping:
            #            rxn_mapping = rxn_mapping.split(':')[1];
            #        atomMappingReactions_row['products_ids_tracked'].append(met_id_tmp);
            #        atomMappingReactions_row['products_stoichiometry_tracked'].append(met_stoichiometry_tmp);
            #        atomMappingReactions_row['products_mapping'].append(rxn_mapping);
            #        elements = [];
            #        positions = [];
            #        for pos,mapping in enumerate(rxn_mapping):
            #            positions.append(pos);
            #            elements.append(element_tracked_I);
            #        atomMappingReactions_row['products_positions_tracked'].append(positions)
            #        atomMappingReactions_row['products_elements_tracked'].append(elements)
            #    #check for stoichiometry
            #    elif rxn_token.replace('.','').replace('-','').replace('E','').isdigit():
            #        met_stoichiometry_tmp = abs(float(rxn_token));
            #        modelReactions_row['products_stoichiometry'].append(met_stoichiometry_tmp)
            #    #check for the next metabolite
            #    elif '+' in rxn_token:
            #        met_id_tmp = None;
            #        met_stoichiometry_tmp = None;
            #    #met_id
            #    else:
            #        if model_met_conversion_I: met_id_tmp = model_met_conversion[rxn_token.strip()];
            #        else: met_id_tmp = rxn_token.strip();
            #        modelReactions_row['products_ids'].append(met_id_tmp)
            #        model_met_ids.append(met_id_tmp)
            #        if not met_stoichiometry_tmp: #implicit stoichiometry of 1
            #            met_stoichiometry_tmp = 1.0;
            #            modelReactions_row['products_stoichiometry'].append(met_stoichiometry_tmp);
            #append to list
            modelReactions.append(modelReactions_row);
            atomMappingReactions.append(atomMappingReactions_row);
            #check for a potential reverse reaction:
            if modelReactions_row['reversibility']:
                #initialize the data structure for atomMappingReactions_reverse:
                atomMappingReactions_reverse_row = {};
                atomMappingReactions_reverse_row['mapping_id']=mapping_id_I;
                if model_rxn_conversion_I: atomMappingReactions_reverse_row['rxn_id']=model_rxn_conversion[id]+'_reverse';
                else: atomMappingReactions_reverse_row['rxn_id']=id+'_reverse';
                atomMappingReactions_reverse_row['rxn_description']=atomMappingReactions_row['rxn_description'];
                atomMappingReactions_reverse_row['rxn_equation']=atomMappingReactions_row['rxn_equation'];
                atomMappingReactions_reverse_row['reactants_stoichiometry_tracked']=[-abs(s) for s in atomMappingReactions_row['products_stoichiometry_tracked']]
                atomMappingReactions_reverse_row['products_stoichiometry_tracked']=[abs(s) for s in atomMappingReactions_row['reactants_stoichiometry_tracked']]
                atomMappingReactions_reverse_row['reactants_ids_tracked']=atomMappingReactions_row['products_ids_tracked']
                atomMappingReactions_reverse_row['products_ids_tracked']=atomMappingReactions_row['reactants_ids_tracked']
                atomMappingReactions_reverse_row['reactants_elements_tracked']=atomMappingReactions_row['products_elements_tracked']
                atomMappingReactions_reverse_row['products_elements_tracked']=atomMappingReactions_row['reactants_elements_tracked']
                atomMappingReactions_reverse_row['reactants_positions_tracked']=atomMappingReactions_row['products_positions_tracked']
                atomMappingReactions_reverse_row['products_positions_tracked']=atomMappingReactions_row['reactants_positions_tracked']
                atomMappingReactions_reverse_row['reactants_mapping']=atomMappingReactions_row['products_mapping']
                atomMappingReactions_reverse_row['products_mapping']=atomMappingReactions_row['reactants_mapping']
                atomMappingReactions_reverse_row['used_']=True
                atomMappingReactions_reverse_row['comment_']=None
                atomMappingReactions_reverse.append(atomMappingReactions_reverse_row)

        #lookup the metabolite information from the database to generate modelMetabolites
        model_met_ids_unique = list(set(model_met_ids));
        modelMetabolites = [];
        for model_met_id in model_met_ids_unique:
            met_id = model_met_id.split('.')[0]
            INCA_compartment = None;
            if '.' in model_met_id:
                INCA_compartment = model_met_id.split('.')[1]
            modelMetabolites_row = {};
            modelMetabolites_row = self.stage02_isotopomer_query.get_row_modelIDAndMetID_dataStage02PhysiologyModelMetabolites('iJO1366',met_id);
            if not modelMetabolites_row:
                modelMetabolites_row['met_name']='';
                modelMetabolites_row['formula']='';
                modelMetabolites_row['charge']=0;
                modelMetabolites_row['bound']=0;
                modelMetabolites_row['constraint_sense']='E';
                modelMetabolites_row['lower_bound']=None;
                modelMetabolites_row['upper_bound']=None;
                modelMetabolites_row['fixed']=None;
                modelMetabolites_row['used_']=True;
                modelMetabolites_row['comment_']='INCA-specific metabolite'
            if INCA_compartment:
                modelMetabolites_row['balanced']=False;
                modelMetabolites_row['met_id']=met_id + '.' + INCA_compartment;
                modelMetabolites_row['compartment']=INCA_compartment;
            else:
                modelMetabolites_row['balanced']=True;
                modelMetabolites_row['met_id']=met_id
                compartment = met_id.split('_')[-1]
                modelMetabolites_row['compartment']=compartment;
            modelMetabolites_row['model_id']=model_id_I;
            modelMetabolites.append(modelMetabolites_row);

        #create the model from modelReactions and modelMetabolites
        cobra_model = self.create_modelFromReactionsAndMetabolitesTables(modelReactions,modelMetabolites)
        convert_to_irreversible(cobra_model);
        save_json_model(cobra_model,'cobra_model_tmp.json')

        # add the model information to the database
        dataStage02IsotopomerModelRxns_data = [];
        dataStage02IsotopomerModelMets_data = [];
        dataStage02IsotopomerModels_data,\
            dataStage02IsotopomerModelRxns_data,\
            dataStage02IsotopomerModelMets_data = self._parse_model_json(model_id_I, date_I,'cobra_model_tmp.json')

        # add modelReactions to the database
        #if add_rxns_I: self.add_data_stage02_isotopomer_modelReactions(dataStage02IsotopomerModelRxns_data);
        # add in equations to modelReactions:
        for rxn1_cnt,rxn1 in enumerate(modelReactions):
            for rxn2_cnt,rxn2 in enumerate(dataStage02IsotopomerModelRxns_data):
                if rxn1['rxn_id']==rxn2['rxn_id']:
                    modelReactions[rxn1_cnt]['equation'] = rxn2['equation'];
        if add_rxns_I: self.add_data_stage02_isotopomer_modelReactions(modelReactions);
        elif update_rxns_I: self.update_data_stage02_isotopomer_modelReactions(modelReactions);
        
        # add modelMetabolites to the database
        #self.add_data_stage02_isotopomer_modelMetabolites(modelMetabolites);
        if add_mets_I: self.add_data_stage02_isotopomer_modelMetabolites(dataStage02IsotopomerModelMets_data);
        elif update_mets_I: self.update_data_stage02_isotopomer_modelMetabolites(dataStage02IsotopomerModelMets_data);
        elif addunique_mets_I: 
            existing_mets = [];
            existing_mets = self.stage02_isotopomer_query.get_metIDs_modelID_dataStage02IsotopomerModelMetabolites(model_id_I);
            all_mets = self.stage02_isotopomer_query.get_metIDs_modelID_dataStage02IsotopomerModelReactions(model_id_I);
            new_mets = [];
            for met in all_mets:
                if not met in existing_mets:
                    new_mets.append(met);
            new_mets_add = [];
            for row in dataStage02IsotopomerModelMets_data:
                if row['met_id'] in new_mets:
                    new_mets_add.append(row);
            self.add_data_stage02_isotopomer_modelMetabolites(new_mets_add);

        # add model to the database
        if add_model_I: self.add_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);
        elif update_model_I: self.update_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);

        #add atomMappingReactions to the database
        if add_rxn_mappings_I: 
            self.add_data_stage02_isotopomer_atomMappingReactions(atomMappingReactions);
            self.add_data_stage02_isotopomer_atomMappingReactions(atomMappingReactions_reverse);
        elif update_rxn_mappings_I: 
            self.update_data_stage02_isotopomer_atomMappingReactions(atomMappingReactions);
            self.update_data_stage02_isotopomer_atomMappingReactions(atomMappingReactions_reverse);

        print('model and mapping added');
    # Deprecated
    def import_dataStage02IsotopomerModelAndAtomMappingReactions_mat(self,model_id_I='iJS2012',mapping_id_I='iJS2012_01', date_I='120101', model_mat_I='data\iJS2012_centralMets.mat',model_mat_name_I='iJS2012'):
        '''load and parse matlab isotopomer model (i.e., iJS2012)'''

        '''DELETE previous uploads of iJS2012:
        DELETE FROM data_stage02_isotopomer_models WHERE model_id LIKE 'iJS2012';
        DELETE FROM "data_stage02_isotopomer_modelReactions" WHERE model_id LIKE 'iJS2012';
        DELETE FROM "data_stage02_isotopomer_modelMetabolites" WHERE model_id LIKE 'iJS2012';
        DELETE FROM "data_stage02_isotopomer_atomMappingMetabolites" WHERE mapping_id LIKE 'iJS2012_01';
        DELETE FROM "data_stage02_isotopomer_atomMappingReactions" WHERE mapping_id LIKE 'iJS2012_01';'''

        #load the matlab model
        cobra_model = load_matlab_model(model_mat_I)
        #check and correct the reaction ids
        rxn_ids = [];
        for rxn in cobra_model.reactions:
            rxn_id_old = copy(rxn.id)
            rxn_id_new = copy(rxn.id)
            rxn_id_new = rxn_id_new.replace('_Full','');
            rxn_id_new = rxn_id_new.replace("'",'');
            rxn_id_new = rxn_id_new.replace("_noMatch",'');
            rxn_id_new = rxn_id_new.replace("_nomatch",'');
            cobra_model.reactions.get_by_id(rxn_id_old).id = rxn_id_new;
            cobra_model.repair();
            rxn_ids.append(rxn_id_new);
        #load the isotopomer data
        isotopomer_data = scipy.io.loadmat(model_mat_I)[model_mat_name_I]['isotopomer'][0][0]
        atomMappingReactions=[];
        #parse the isotopomer data
        for rxn,mapping_numpy in enumerate(isotopomer_data):
            #intialize the row
            row={}
            row['mapping_id']=mapping_id_I;
            row['rxn_id']=rxn_ids[rxn];
            row['rxn_description']='';
            row['rxn_equation']='';
            row['reactants_stoichiometry_tracked']=[]
            row['products_stoichiometry_tracked']=[]
            row['reactants_ids_tracked']=[]
            row['products_ids_tracked']=[]
            row['reactants_elements_tracked']=[]
            row['products_elements_tracked']=[]
            row['reactants_positions_tracked']=[]
            row['products_positions_tracked']=[]
            row['reactants_mapping']=[]
            row['products_mapping']=[]
            row['used_']=True
            row['comment_']=None
            if not mapping_numpy:
                # append
                atomMappingReactions.append(row);
            else:
                mapping = mapping_numpy[0][0];
                # parse into tracked metabolites and their mapping
                mapping_list = mapping.split('!');
                mets_info_list = mapping_list[0].split('>'); # parse each into reactants and products
                mapping_info_list = mapping_list[1].split('>'); # parse each into reactants and products
                                                                #only the first mapping will be used
                # parse tracked metabolite information
                mets_info_list[0] = mets_info_list[0].strip().split(' ')
                mets_info_list[1] = mets_info_list[1].strip().split(' ')
                stoich = True;
                for cnt,c in enumerate(mets_info_list[0]):
                    c.strip()
                    if not c or cnt==0: continue #first string is the reaction id
                    if stoich:#c.isnumeric():
                        row['reactants_stoichiometry_tracked'].append(-abs(float(c)))
                        stoich=False;
                    else:
                        row['reactants_ids_tracked'].append(c[1:]) #first character is always an 'x'
                        stoich = True;
                for cnt,c in enumerate(mets_info_list[1]):
                    c.strip()
                    if not c: continue
                    if stoich:#c.isnumeric():
                        row['products_stoichiometry_tracked'].append(float(c))
                        stoich=False;
                    else:
                        row['products_ids_tracked'].append(c[1:])
                        stoich = True;
                # parse mapping information
                mapping_info_list[0] = mapping_info_list[0].strip().split(' ')
                mapping_info_list[1] = mapping_info_list[1].strip().split(' ')
                for cnt,m in enumerate(mapping_info_list[0]):
                    if not m: continue
                    row['reactants_mapping'].append(m.strip('#'))
                    elements = [];
                    positions = [];
                    for pos,element in enumerate(m.strip('#')):
                        positions.append(pos);
                        elements.append('C');
                    row['reactants_positions_tracked'].append(positions);
                    row['reactants_elements_tracked'].append(elements);
                for cnt,m in enumerate(mapping_info_list[1]):
                    if not m: continue
                    row['products_mapping'].append(m.strip('#'))
                    elements = [];
                    positions = [];
                    for pos,element in enumerate(m.strip('#')):
                        positions.append(pos);
                        elements.append('C');
                    row['products_positions_tracked'].append(positions);
                    row['products_elements_tracked'].append(elements);
                # append
                atomMappingReactions.append(row);
        # update selected reactions to account for new metabolites
        acon = Metabolite('acon_DASH_C_c','C6H3O6','cis-Aconitate','c');
        cit = cobra_model.metabolites.get_by_id('cit_c')
        icit = cobra_model.metabolites.get_by_id('icit_c')
        for rxn,row in enumerate(atomMappingReactions):
            if rxn_ids[rxn] == 'ACONTa':
                # Update ACONTa
                aconta_mets = {};
                aconta_mets[cit] = -1;
                aconta_mets[acon] = 1;
                aconta = Reaction('ACONTa');
                aconta.add_metabolites(aconta_mets);
                cobra_model.remove_reactions(['ACONTa']);
                cobra_model.add_reactions([aconta]);
                cobra_model.repair();
                # Update the mapping ids
                atomMappingReactions[rxn]['products_ids_tracked']=['acon_DASH_C_c']
                atomMappingReactions[rxn]['comment_']='updated'
            elif rxn_ids[rxn] == 'ACONTa_reverse':
                aconta_reverse_mets = {};
                aconta_reverse_mets[cit] = 1;
                aconta_reverse_mets[acon] = -1;
                aconta_reverse = Reaction('ACONTa_reverse');
                aconta_reverse.add_metabolites(aconta_reverse_mets);
                cobra_model.remove_reactions(['ACONTa_reverse']);
                cobra_model.add_reactions([aconta_reverse]);
                cobra_model.repair();
                # Update the mapping ids
                atomMappingReactions[rxn]['reactants_ids_tracked']=['acon_DASH_C_c']
                atomMappingReactions[rxn]['comment_']='updated'
            elif rxn_ids[rxn] == 'EX_co2_LPAREN_e_RPAREN__reverse':
                # Correct atomMapping
                atomMappingReactions[rxn]['mapping_id']=mapping_id_I;
                atomMappingReactions[rxn]['rxn_id']=rxn_ids[rxn];
                atomMappingReactions[rxn]['rxn_description']='';
                atomMappingReactions[rxn]['rxn_equation']='';
                atomMappingReactions[rxn]['reactants_stoichiometry_tracked']=[]
                atomMappingReactions[rxn]['products_stoichiometry_tracked']=[1]
                atomMappingReactions[rxn]['reactants_ids_tracked']=[]
                atomMappingReactions[rxn]['products_ids_tracked']=['co2_e']
                atomMappingReactions[rxn]['reactants_elements_tracked']=[]
                atomMappingReactions[rxn]['products_elements_tracked']=[["C"]]
                atomMappingReactions[rxn]['reactants_positions_tracked']=[]
                atomMappingReactions[rxn]['products_positions_tracked']=[[0]]
                atomMappingReactions[rxn]['reactants_mapping']=[]
                atomMappingReactions[rxn]['products_mapping']=['a']
                atomMappingReactions[rxn]['used_']=True
                atomMappingReactions[rxn]['comment_']=None
        # add in ACONTb
        acontb_mets = {};
        acontb_mets[acon] = -1;
        acontb_mets[icit] = 1;
        acontb = Reaction('ACONTb');
        acontb.add_metabolites(acontb_mets);
        cobra_model.add_reactions([acontb]);
        cobra_model.repair();
        # add in ACONTb mapping
        row={};
        row['mapping_id']=mapping_id_I;
        row['rxn_id']='ACONTb';
        row['rxn_description']='';
        row['rxn_equation']='';
        row['reactants_stoichiometry_tracked']=[-1]
        row['products_stoichiometry_tracked']=[1]
        row['reactants_ids_tracked']=['acon_DASH_C_c']
        row['products_ids_tracked']=['icit_c']
        row['reactants_elements_tracked']=[["C", "C", "C", "C", "C", "C"]]
        row['products_elements_tracked']=[["C", "C", "C", "C", "C", "C"]]
        row['reactants_positions_tracked']=[[0, 1, 2, 3, 4, 5]]
        row['products_positions_tracked']=[[0, 1, 2, 3, 4, 5]]
        row['reactants_mapping']=['abcdef']
        row['products_mapping']=['abcdef']
        row['used_']=True
        row['comment_']='added'
        atomMappingReactions.append(row)
        # add in ACONTb_reverse
        acontb_reverse_mets = {};
        acontb_reverse_mets[acon] = 1;
        acontb_reverse_mets[icit] = -1;
        acontb_reverse = Reaction('ACONTb_reverse');
        acontb_reverse.add_metabolites(acontb_reverse_mets);
        cobra_model.add_reactions([acontb_reverse]);
        cobra_model.repair();
        # add in ACONTb_reverse mapping
        row={};
        row['mapping_id']=mapping_id_I;
        row['rxn_id']='ACONTb_reverse';
        row['rxn_description']='';
        row['rxn_equation']='';
        row['reactants_stoichiometry_tracked']=[-1]
        row['products_stoichiometry_tracked']=[1]
        row['reactants_ids_tracked']=['icit_c']
        row['products_ids_tracked']=['acon_DASH_C_c']
        row['reactants_elements_tracked']=[["C", "C", "C", "C", "C", "C"]]
        row['products_elements_tracked']=[["C", "C", "C", "C", "C", "C"]]
        row['reactants_positions_tracked']=[[0, 1, 2, 3, 4, 5]]
        row['products_positions_tracked']=[[0, 1, 2, 3, 4, 5]]
        row['reactants_mapping']=['abcdef']
        row['products_mapping']=['abcdef']
        row['used_']=True
        row['comment_']='added'
        atomMappingReactions.append(row)
        # update exchanges
        cobra_model_sbml = None; # get the cobra model
        cobra_model_sbml = self.stage02_isotopomer_query.get_row_modelID_dataStage02IsotopomerModels('140407_iDM2014');
        if cobra_model_sbml['file_type'] == 'sbml':
            with open('data/cobra_model_tmp.xml','w') as file:
                file.write(cobra_model_sbml['model_file']);
                file.close()
            cobra_model1 = None;
            cobra_model1 = create_cobra_model_from_sbml_file('data/cobra_model_tmp.xml', print_time=True);
        elif cobra_model_sbml['file_type'] == 'json':
            with open('data/cobra_model_tmp.json','w') as file:
                file.write(cobra_model_sbml['model_file']);
                file.close()
            cobra_model1 = None;
            cobra_model1 = load_json_model('data/cobra_model_tmp.json');
        else:
            print('file_type not supported')
        # delete exchange reactions:
        cobra_model.remove_reactions([cobra_model.reactions.get_by_id('EX_h_LPAREN_e_RPAREN_'),
                                   cobra_model.reactions.get_by_id('EX_h2o_LPAREN_e_RPAREN_'),
                                   cobra_model.reactions.get_by_id('EX_nh4_LPAREN_e_RPAREN_'),
                                   cobra_model.reactions.get_by_id('EX_o2_LPAREN_e_RPAREN_'),
                                   cobra_model.reactions.get_by_id('EX_pi_LPAREN_e_RPAREN_'),
                                   cobra_model.reactions.get_by_id('EX_so4_LPAREN_e_RPAREN_')]);
        cobra_model.repair();
        # add in exchange reactions:
        cobra_model.add_reactions([cobra_model1.reactions.get_by_id('EX_h_LPAREN_e_RPAREN_'),
                                   cobra_model1.reactions.get_by_id('EX_h_LPAREN_e_RPAREN__reverse'),
                                   cobra_model1.reactions.get_by_id('EX_h2o_LPAREN_e_RPAREN_'),
                                   cobra_model1.reactions.get_by_id('EX_h2o_LPAREN_e_RPAREN__reverse'),
                                   cobra_model1.reactions.get_by_id('EX_nh4_LPAREN_e_RPAREN__reverse'),
                                   cobra_model1.reactions.get_by_id('EX_o2_LPAREN_e_RPAREN__reverse'),
                                   cobra_model1.reactions.get_by_id('EX_pi_LPAREN_e_RPAREN__reverse'),
                                   cobra_model1.reactions.get_by_id('EX_so4_LPAREN_e_RPAREN__reverse')]);
        cobra_model.repair();
        # ensure that there are no reversible reactions
        #NOTE: reactions do not involved tracked metabolites, so there is no need to update the atomMappingReactions
        convert_to_irreversible(cobra_model);
        # repair EX_glc_LPAREN_e_RPAREN__reverse
        if cobra_model.reactions.has_id('EX_glc_LPAREN_e_RPAREN__reverse'):
            cobra_model.remove_reactions(['EX_glc_LPAREN_e_RPAREN_'])
            lb,ub = cobra_model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN__reverse').lower_bound,cobra_model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN__reverse').upper_bound;
            EX_glc_mets = {};
            EX_glc_mets[cobra_model.metabolites.get_by_id('glc_DASH_D_e')] = -1;
            EX_glc = Reaction('EX_glc_LPAREN_e_RPAREN_');
            EX_glc.add_metabolites(EX_glc_mets);
            cobra_model.add_reaction(EX_glc)
            cobra_model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_').lower_bound = -ub;
            cobra_model.reactions.get_by_id('EX_glc_LPAREN_e_RPAREN_').upper_bound = lb;
            cobra_model.remove_reactions(['EX_glc_LPAREN_e_RPAREN__reverse'])
        # lookup metabolite information from the database
        for met in cobra_model.metabolites:
            met_info = {};
            met_info = self.stage02_isotopomer_query.get_row_modelIDAndMetID_dataStage02PhysiologyModelMetabolites('iJO1366',met.id);
            if met_info:
                cobra_model.metabolites.get_by_id(met.id).charge = met_info['charge'];
                cobra_model.metabolites.get_by_id(met.id).compartment = met_info['compartment'];
                cobra_model.metabolites.get_by_id(met.id).formula = met_info['formula'];
                cobra_model.metabolites.get_by_id(met.id).name = met_info['met_name'];
                cobra_model.repair();
            elif met.id == '2kmb_c':
                cobra_model.metabolites.get_by_id(met.id).charge = -1;
                cobra_model.metabolites.get_by_id(met.id).compartment = 'c';
                cobra_model.metabolites.get_by_id(met.id).formula = 'C5H7O3S';
                cobra_model.metabolites.get_by_id(met.id).name = '2-keto-4-methylthiobutyrate';
                cobra_model.repair();
            elif met.id == 'dkmpp_c':
                cobra_model.metabolites.get_by_id(met.id).charge = -2;
                cobra_model.metabolites.get_by_id(met.id).compartment = 'c';
                cobra_model.metabolites.get_by_id(met.id).formula = 'C6H9O6PS';
                cobra_model.metabolites.get_by_id(met.id).name = '2,3-diketo-5-methylthio-1-phosphopentane';
                cobra_model.repair();
            else:
                # correct for 'EC'
                if 'EC' in met.id:
                    met_id_old = met.id
                    met_id_new_list = met.id.split('_')[:-1]
                    met_id_new = '_'.join(met_id_new_list)
                    met_id_new += '_e';
                    cobra_model.metabolites.get_by_id(met_id_old).id = met_id_new;
                    cobra_model.repair();
                compartment = met.id.split('_')[-1];
                cobra_model.metabolites.get_by_id(met.id).compartment = compartment;
                cobra_model.metabolites.get_by_id(met.id).charge = 0;
                cobra_model.metabolites.get_by_id(met.id).formula = '';
                cobra_model.metabolites.get_by_id(met.id).name = '';
                cobra_model.repair();
        # write the model to a temporary file
        #write_cobra_model_to_sbml_file(cobra_model,'data/cobra_model_tmp.xml')
        save_json_model(cobra_model,'data/cobra_model_tmp.json')
        # add the model information to the database
        dataStage02IsotopomerModelRxns_data = [];
        dataStage02IsotopomerModelMets_data = [];
        dataStage02IsotopomerModels_data,\
            dataStage02IsotopomerModelRxns_data,\
            dataStage02IsotopomerModelMets_data = self._parse_model_json(model_id_I, date_I, 'data/cobra_model_tmp.json')
        self.add_data_stage02_isotopomer_modelMetabolites(dataStage02IsotopomerModelMets_data);
        self.add_data_stage02_isotopomer_modelReactions(dataStage02IsotopomerModelRxns_data);
        self.add_data_stage02_isotopomer_models(dataStage02IsotopomerModels_data);
        # add the mapping information to the database
        self.add_data_stage02_isotopomer_atomMappingReactions(atomMappingReactions);