from .models_BioCyc_io import models_BioCyc_io
from .models_BioCyc_dependencies import models_BioCyc_dependencies

from .models_COBRA_query import models_COBRA_query
from .models_BioCyc_dependencies import models_BioCyc_dependencies

import copy

class models_BioCyc_execute(models_BioCyc_io):

    def execute_convertAndMap_BioCycRegulation2COBRA(
        self,
        ):
        ''' '''
        pass;

    def join_BioCyc2COBRAregulationWithCOBRAinteractions(self,
        BioCyc2COBRA_regulation,
        COBRA_interaction,
        BioCyc_alt_id = {},
        COBRA_alt_id = {},
        COBRA_alt_id2 = {},
        deformat_met_id_I = True
        ):
        '''
        return a list mapped and unmapped components
        INPUT:
        BioCyc2COBRA_regulation =  [{left:[string],right:[string],mode:[string],
                parent_classes:[string],mechanism:[string]},
                {left_EcoCyc:[string],right_EcoCyc:[string]]
        COBRA_interaction =  [{left:[string],right:[string],mode:[string],
                parent_classes:[string],mechanism:[string]}]
        BioCyc_alt_id = {name:{'synonym':[],'common_name':[],'accession_1':[],'accession_2':[]}}
            output from get_alternativeGeneIdentifiers_modelsBioCycPolymerSegments
        COBRA_alt_id = {rxn_id:'pathways':[],'stoichiometry':[]}}
            output from get_rowsDict_modelID_dataStage02PhysiologyModelPathways
                        convert_netRxnDict2rxnNetRxnDict
        COBRA_alt_id2 = {bnumber:'bnumber':'','gene_name':[]}}
        OUTPUT:
        data_O = [{left:[string],right:[string],mode:[string],parent_classes:[string]}]
        '''

        from .models_COBRA_dependencies import models_COBRA_dependencies
        COBRA_dependencies = models_COBRA_dependencies();

        def deformatAndConvert_metID(met_id_I):
            met_id_O = None;
            if '_c' in met_id_I:
                met_id_O = COBRA_dependencies.deformat_metid(met_id_I)\
                    .replace('13dpg','23dpg')\
                    .replace('3pg','Pool_2pg_3pg')\
                    .replace('glycogen','adpglc')\
                    .replace('uacgam','udpglcur');
            return met_id_O;

        data_tmp = []
        #BioCyc
        for row in BioCyc2COBRA_regulation:
            if not row['used_']: continue;
            unique = {
                    #'left':row['left'],
                    #'right':row['right'],
                    'mode':row['mode'],
                    'mechanism':row['mechanism'],
                    #'name':row['name'],
                    'parent_classes':row['parent_classes']
                };
            #BioCyc Left identifiers
            left_ids=[];
            if type(row['left'])!=type([]) and row['left'] in BioCyc_alt_id.keys():
                left_alt_ids = list(set(BioCyc_alt_id[row['left']]['common_name']+\
                                        BioCyc_alt_id[row['left']]['synonym']+\
                                        [row['left']]))
                left_ids.extend(left_alt_ids)          
            elif type(row['left_EcoCyc'])!=type([]) and row['left_EcoCyc'] in BioCyc_alt_id.keys():
                left_alt_ids = list(set(BioCyc_alt_id[row['left_EcoCyc']]['common_name']+\
                                        BioCyc_alt_id[row['left_EcoCyc']]['synonym']+\
                                        [row['left_EcoCyc']]))
                left_ids.extend(left_alt_ids)
            elif type(row['left'])!=type([]) and row['left'] in COBRA_alt_id.keys():
                left_ids.append(row['left']) 
                left_ids.extend(COBRA_alt_id[row['left']]['pathways'])
            elif row['left']:
                left_ids.append(row['left'])  
            if row['left']:
                met_id_left = deformatAndConvert_metID(row['left'])
                if met_id_left:
                    left_ids.append(met_id_left)
            #BioCyc Right identifiers
            right_ids=[];
            if type(row['right'])!=type([]) and row['right'] in BioCyc_alt_id.keys():
                right_alt_ids = list(set(BioCyc_alt_id[row['right']]['common_name']+\
                                        BioCyc_alt_id[row['right']]['synonym']+\
                                        [row['right']]))
                right_ids.extend(right_alt_ids)          
            elif type(row['right_EcoCyc'])!=type([]) and row['right_EcoCyc'] in BioCyc_alt_id.keys():
                right_alt_ids = list(set(BioCyc_alt_id[row['right_EcoCyc']]['common_name']+\
                                        BioCyc_alt_id[row['right_EcoCyc']]['synonym']+\
                                        [row['right_EcoCyc']]))
                right_ids.extend(right_alt_ids)
            elif type(row['right'])!=type([]) and row['right'] in COBRA_alt_id.keys():
                right_ids.append(row['right'])
                right_ids.extend(COBRA_alt_id[row['right']]['pathways'])
            elif row['right']:
                right_ids.append(row['right'])  
            if row['right']:
                met_id_right = deformatAndConvert_metID(row['right'])
                if met_id_right:
                    right_ids.append(met_id_right)
            #Flatten left and right identifiers
            for l in left_ids:
                for r in right_ids:
                    tmp = {}
                    tmp['left'] = l;
                    tmp['right'] = r;
                    tmp.update(unique);
                    data_tmp.append(tmp);
        #COBRA
        for row in COBRA_interaction:
            unique = {
                    #'left':row['left'],
                    #'right':row['right'],
                    'mode':row['mode'],
                    'mechanism':row['mechanism'],
                    #'name':'',
                    'parent_classes':row['parent_classes']
                };
            left_ids=[];
            left_ids.append(row['left']) 
            if row['left'] in COBRA_alt_id2.keys():
                left_alt_ids = list(set(COBRA_alt_id2[row['left']]['gene_name']))
                left_ids.extend(left_alt_ids)
            met_id_left = deformatAndConvert_metID(row['left'])
            if met_id_left:
                left_ids.append(met_id_left)
            right_ids=[];
            right_ids.append(row['right']) 
            if row['right'] in COBRA_alt_id2.keys():
                left_alt_ids = list(set(COBRA_alt_id2[row['right']]['gene_name']))
            met_id_right = deformatAndConvert_metID(row['right'])
            if met_id_right:
                right_ids.append(met_id_right)
            #Flatten left and right identifiers
            for l in left_ids:
                for r in right_ids:
                    tmp = {}
                    tmp['left'] = l;
                    tmp['right'] = r;
                    tmp.update(unique);
                    data_tmp.append(tmp);
                    
        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        data_O = [];
        for row in data_tmp:
            if not row in data_O:
                data_O.append(row);

        return data_O;

    def update_BioCyc2COBRAregulation_mappings(self,
        BioCyc2COBRA_regulation_all,
        BioCyc2COBRA_met_mappings,
        BioCyc2COBRA_rxn_mappings,
        BioCyc_exclusion_names=[]
        ):
        '''Update the listDict of BioCyc2COBRA_regulation with
        manually mapped entries
        INPUT:
        BioCyc2COBRA_regulation_all = [{}]
        BioCyc2COBRA_met_mappings = [{'BioCyc':[string],'BiGG':[string],'used_':[boolean],'comment_':[string]}]
        BioCyc2COBRA_rxn_mappings = [{'BioCyc':[string],'BiGG':[string],'used_':[boolean],'comment_':[string]}]
        BioCyc_exclusion_names = []
        OUTPUT:
        BioCyc2COBRA_regulation_mapped = [{}]
        '''
        #add in metabolite mappings
        BioCyc2COBRA_regulation_all_1 = [];
        for d in BioCyc2COBRA_regulation_all:
            if d['name'] in BioCyc_exclusion_names: continue;
            d['used_']=True;
            d['comment_']=None;  
            #metabolites
            if d['left_EcoCyc'] in BioCyc2COBRA_met_mappings.keys():
                for row in BioCyc2COBRA_met_mappings[d['left_EcoCyc']]:
                    tmp = copy.copy(d) 
                    #check for null mappings
                    if row['used_'] is None or row['used_'] == "":
                        if d not in BioCyc2COBRA_regulation_all_1:
                            BioCyc2COBRA_regulation_all_1.append(d);                
                    #check for false mappings
                    elif row['BiGG']==tmp['left'] and \
                        (row['used_'] == "FALSE" or not row['used_']):
                        tmp['used_']=row['used_']
                        tmp['comment_']=row['comment_']
                        BioCyc2COBRA_regulation_all_1.append(tmp);
                    #add in true mappings
                    elif row['used_'] == "TRUE" or row['used_']:
                        tmp['left']=row['BiGG']
                        tmp['comment_']=row['comment_']
                        BioCyc2COBRA_regulation_all_1.append(tmp);
                    else:
                        if d not in BioCyc2COBRA_regulation_all_1:
                            BioCyc2COBRA_regulation_all_1.append(d);
            else:
                BioCyc2COBRA_regulation_all_1.append(d);
        #add in reaction mappings
        BioCyc2COBRA_regulation_all_2 = [];
        for d in BioCyc2COBRA_regulation_all_1:             
            #reactions
            if d['right_EcoCyc'] in BioCyc2COBRA_rxn_mappings.keys():
                for row in BioCyc2COBRA_rxn_mappings[d['right_EcoCyc']]:
                    tmp = copy.copy(d)   
                    #check for null mappings
                    if row['used_'] is None or row['used_'] == "":
                        if d not in BioCyc2COBRA_regulation_all_2:
                            BioCyc2COBRA_regulation_all_2.append(d);  
                    #check for false mappings
                    elif row['BiGG']==tmp['right'] and \
                        (row['used_'] == "FALSE" or not row['used_']):
                        tmp['used_']=row['used_']
                        tmp['comment_']=row['comment_']
                        BioCyc2COBRA_regulation_all_2.append(tmp);
                    #add in true mappings
                    elif row['used_'] == "TRUE" or row['used_']:
                        tmp['right']=row['BiGG']
                        tmp['comment_']=row['comment_']
                        BioCyc2COBRA_regulation_all_2.append(tmp);
                    else:
                        if d not in BioCyc2COBRA_regulation_all_2:
                            BioCyc2COBRA_regulation_all_2.append(d);
            else:
                BioCyc2COBRA_regulation_all_2.append(d);
        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        BioCyc2COBRA_regulation_all = [];
        for row in BioCyc2COBRA_regulation_all_2:
            if not row in BioCyc2COBRA_regulation_all:
                BioCyc2COBRA_regulation_all.append(row);
        return BioCyc2COBRA_regulation_all;

    def join_BioCyc2COBRA_regulationAndTranscriptionFactors(
        self,
        BioCyc2COBRA_regulation_I,
        BioCyc2COBRA_TFs_I
        ):
        '''Join converted and mapped BioCyc regulation and Transcription factor reactions
        INPUT:
        BioCyc2COBRA_regulation_I = output from convertAndMap_BioCycRegulation2COBRA
        BioCyc2COBRA_TFs_I = output from convertAndMap_BioCycTranscriptionFactor2COBRA
    
        OUTPUT:
    
        '''
        BioCyc2COBRA_regulation_all = [];
        #iterate through each row of regulation
        for row in BioCyc2COBRA_regulation_I:
            unique = {
                'regulator':row['regulator'],
                'regulated_entity':row['regulated_entity'],
                'mode':row['mode'],
                'mechanism':row['mechanism'],
                'name':row['name'],
                'parent_classes':row['parent_classes']
            }
            tmp = {
                'left_EcoCyc':[],
                'left':[],
                'right_EcoCyc':[],
                'right':[],
            }
            if row['regulator'] in BioCyc2COBRA_TFs_I.keys():
                for reg in BioCyc2COBRA_TFs_I[row['regulator']]:
                    for i in range(len(reg['ligands']['BioCyc_name'])):
                        tmp = {
                            'left_EcoCyc':reg['ligands']['BioCyc_name'][i],
                            'left':reg['ligands']['COBRA_met_id'][i],
                            'right_EcoCyc':reg['tu'],
                            'right':None,
                            'regulator':row['regulator'],
                            'regulated_entity':row['regulated_entity'],
                            'mode':reg['mode'],
                            'mechanism':row['mechanism'],
                            'parent_classes':'("Protein-Ligand-Binding-Reactions")',
                            'name':row['name']
                        };
                        BioCyc2COBRA_regulation_all.append(tmp);
                    for i in range(len(reg['genes'])):
                        tmp = {
                            'left_EcoCyc':reg['genes'][i],
                            'left':reg['genes'][i],
                            'right_EcoCyc':reg['tu'],
                            'right':None,
                            'regulator':row['regulator'],
                            'regulated_entity':row['regulated_entity'],
                            'mode':reg['mode'],
                            'mechanism':row['mechanism'],
                            'parent_classes':'("DNA-to-Protein")',
                            'name':row['name']
                        };
                        BioCyc2COBRA_regulation_all.append(tmp);
                    for i in range(len(reg['ligands']['BioCyc_name'])):
                        tmp = {
                            'left_EcoCyc':reg['ligands']['BioCyc_name'][i],
                            'left':reg['ligands']['COBRA_met_id'][i],
                            'right_EcoCyc':row['regulated_entities_EcoCyc'],
                            'right':row['regulated_entities_COBRA'],
                            'regulator':row['regulator'],
                            'regulated_entity':row['regulated_entity'],
                            'mode':reg['mode']+row['mode'],
                            'mechanism':row['mechanism'],
                            'parent_classes':'("Protein-Ligand-DNA-Binding-Reactions")',
                            'name':row['name']
                        };
                        BioCyc2COBRA_regulation_all.append(tmp);
                    for i in range(len(reg['genes'])):
                        tmp = {
                            'left_EcoCyc':reg['genes'][i],
                            'left':reg['genes'][i],
                            'right_EcoCyc':row['regulated_entities_EcoCyc'],
                            'right':row['regulated_entities_COBRA'],
                            'regulator':row['regulator'],
                            'regulated_entity':row['regulated_entity'],
                            'mechanism':row['mechanism'],
                            'mode':row['mode'],
                            'parent_classes':'("DNA-to-Protein-DNA-Binding-Reactions")',
                            'name':row['name']
                        };
                        BioCyc2COBRA_regulation_all.append(tmp);
                tmp = {
                    'left_EcoCyc':row['regulators_EcoCyc'],
                    'left':row['regulators_COBRA'],
                    'right_EcoCyc':row['regulated_entities_EcoCyc'],
                    'right':row['regulated_entities_COBRA'],
                };
                tmp.update(unique);
                BioCyc2COBRA_regulation_all.append(tmp);
            else:
                tmp = {
                    'left_EcoCyc':row['regulators_EcoCyc'],
                    'left':row['regulators_COBRA'],
                    'right_EcoCyc':row['regulated_entities_EcoCyc'],
                    'right':row['regulated_entities_COBRA'],
                };
                tmp.update(unique);
                BioCyc2COBRA_regulation_all.append(tmp);

        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        data_O = [];
        for row in BioCyc2COBRA_regulation_all:
            if not row in data_O:
                data_O.append(row);
        return data_O;

    def convertAndMap_BioCycTranscriptionFactor2COBRA(
        self,
        BioCyc2COBRA_regulation_I,
        BioCyc_polymerSegments_I = None,
        BioCyc_compounds_I = None,
        COBRA_metabolites_I = None,
        chebi2inchi_I = None,
        ):
        '''Convert and map BioCyc Transcription factor (ligand-binding) reactions
        to COBRA model ids
        INPUT:
        BioCyc2COBRA_regulation_I = output from convertAndMap_BioCycRegulation2COBRA
        BioCyc_polymerSegments_I = (TODO) listDict of models_BioCyc_polymerSegments
        BioCyc_compounds_I = listDict of models_BioCyc_compounds
        COBRA_metabolites_I = listDict of models_COBRA_metabolites
        chebi2inchi_I = listDict of CHEBI_ID to InCHI
    
        OUTPUT:
    
        '''
        
        from SBaaS_models.models_BioCyc_dependencies import models_BioCyc_dependencies
        BioCyc_dependencies = models_BioCyc_dependencies();

        if not BioCyc2COBRA_regulation_I is None and BioCyc2COBRA_regulation_I:
            BioCyc2COBRA_regulators = list(set([r['regulator'] for r in BioCyc2COBRA_regulation_I \
                if 'DNA-binding transcriptional dual regulator' in r['regulator']]));
        else:
            BioCyc2COBRA_regulators=BioCyc2COBRA_regulation_I;
        if not chebi2inchi_I is None and chebi2inchi_I:
            chebi2inchi_dict_I = {r['CHEBI_ID']:r['InChI'] for r in chebi2inchi_I}
        else:
            chebi2inchi_dict_I=chebi2inchi_I;
        if not BioCyc_compounds_I is None and BioCyc_compounds_I:
            #BioCyc_compounds_dict_I = {r['name']:r for r in BioCyc_compounds_I}
            BioCyc_compounds_dict_I = {}
            for row in BioCyc_compounds_I:
                keys = [];
                keys.append(row['name'])
                keys = list(set([k for k in keys if k!='']))
                for k in keys:
                    if not k in BioCyc_compounds_dict_I.keys():
                        BioCyc_compounds_dict_I[k]=[];
                    if not row in BioCyc_compounds_dict_I[k]:
                        BioCyc_compounds_dict_I[k].append(row);
        else:
            BioCyc_compounds_dict_I=BioCyc_compounds_I;
        if not BioCyc_polymerSegments_I is None and BioCyc_polymerSegments_I:
            BioCyc_polymerSegments_dict_I = {}
            for r in BioCyc_polymerSegments_I:
                products = models_BioCyc_dependencies.convert_bioCycList2List(r['product'])
                for p in products:
                    if not p in BioCyc_polymerSegments_dict_I.keys():
                        BioCyc_polymerSegments_dict_I[p]=[];
                    else:
                        BioCyc_polymerSegments_dict_I[p].append(r);
        else:
            BioCyc_polymerSegments_dict_I = BioCyc_polymerSegments_I

        BioCyc2COBRA_regulators_O = {}
        for e in BioCyc2COBRA_regulators:
            BioCyc2COBRA_regulators_O[e]=[];
            #spot checks:
            if e == 'Cra DNA-binding transcriptional dual regulator':
                #error mapping fdp_c
                print('check');
            elif e == 'GalR DNA-binding transcriptional dual regulator':
                #gene is being identified as a TU
                print('check');
            elif e == '&beta;-D-galactose':
                #not a transcription factor
                print('check');
            tmp = self.get_rows_substratesAndParentClassesAndDatabase_modelsBioCycReactions(
                e,
                database_I='ECOLI',
                query_I={},
                output_O='listDict',
                dictColumn_I=None
                );
            for t in tmp:
                ligands = {'COBRA_met_id': [], 
                           'BioCyc_name': []};
                genes = [];
                tus = [];
                #parse left and right
                left = BioCyc_dependencies.convert_bioCycList2List(t['left'])
                right = BioCyc_dependencies.convert_bioCycList2List(t['right'])
                #check for tus
                if e in left:
                    tus.append(e);
                    mode = '("-")';
                elif e in right:
                    tus.append(e);
                    mode = '("+")';
                else:
                    continue;
                #query proteins to look up the gene
                #query compounds to look up the ligands
                for l in left:
                    proteins,compounds = [],[];
                    proteins = self.get_rows_nameAndDatabase_modelsBioCycProteins(
                        l,database_I = 'ECOLI'
                        );
                    compounds = self.get_rows_nameAndDatabase_modelsBioCycCompounds(
                        l,database_I = 'ECOLI'
                        );
                    if proteins:
                        for p in proteins:
                            #1. parse genes directly
                            genes.extend(BioCyc_dependencies.convert_bioCycList2List(p['gene']));  
                            #2. if genes are not specified (i.e., protein complex) query and parse polymerSegments
                            names = BioCyc_dependencies.convert_bioCycList2List(p['names'])
                            for n in names:
                                ##TODO: test
                                #if n in BioCyc_polymerSegments_dict_I.keys():
                                #    for row in BioCyc_polymerSegments_dict_I[n]:
                                #        genes.append(row['name'])
                                rows = self.get_rows_productAndDatabase_modelsBioCycPolymerSegments(
                                    n,database_I = 'ECOLI');
                                genes.extend(r['name'] for r in rows);
                    elif compounds:
                        #map the ligand names...
                        original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                            compounds,
                            #[c['name'] for c in compounds],
                            BioCyc_components_dict_I=BioCyc_compounds_dict_I,
                            BioCyc2COBRA_func_I=BioCyc_dependencies.map_BioCycCompound2COBRA,
                            BioCyc2COBRA_params_I={
                                'COBRA_metabolites_I':COBRA_metabolites_I,
                                'chebi2inchi_dict_I':chebi2inchi_dict_I,
                            }
                        );
                        ligands['BioCyc_name'].extend([c['name'] for c in original])
                        #ligands['BioCyc_name'].extend(original)
                        ligands['COBRA_met_id'].extend(converted)
                for r in right:
                    proteins,compounds = [],[];
                    proteins = self.get_rows_nameAndDatabase_modelsBioCycProteins(
                        r,database_I = 'ECOLI'
                        );
                    compounds = self.get_rows_nameAndDatabase_modelsBioCycCompounds(
                        r,database_I = 'ECOLI'
                        );
                    if proteins:
                        for p in proteins:
                            #1. parse genes directly
                            genes.extend(BioCyc_dependencies.convert_bioCycList2List(p['gene']));  
                            #2. if genes are not specified (i.e., protein complex) query and parse polymerSegments
                            names = BioCyc_dependencies.convert_bioCycList2List(p['names'])
                            for n in names:
                                ##TODO: test
                                #if n in BioCyc_polymerSegments_dict_I.keys():
                                #    for row in BioCyc_polymerSegments_dict_I[n]:
                                #        genes.append(row['name'])
                                rows = self.get_rows_productAndDatabase_modelsBioCycPolymerSegments(
                                    n,database_I = 'ECOLI');
                                genes.extend(r['name'] for r in rows);
                    elif compounds:
                        original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                            compounds,
                            #[c['name'] for c in compounds],
                            BioCyc_components_dict_I=BioCyc_compounds_dict_I,
                            BioCyc2COBRA_func_I=BioCyc_dependencies.map_BioCycCompound2COBRA,
                            BioCyc2COBRA_params_I={
                                'COBRA_metabolites_I':COBRA_metabolites_I,
                                'chebi2inchi_dict_I':chebi2inchi_dict_I,
                            }
                        );
                        ligands['BioCyc_name'].extend([c['name'] for c in original])
                        #ligands['BioCyc_name'].extend(original)
                        ligands['COBRA_met_id'].extend(converted)
                genes = list(set([g for g in genes if g!=''])) 
                #check that there is only 1 tu:
                assert(len(tus)==1); #only 1 tu
                tu = tus[0];
                #NOTE: there can be multiple ligands/genes associated with the tu
                BioCyc2COBRA_regulators_O[e].append({
                    'ligands':ligands,
                    'genes':genes,
                    'tu':tu,
                    'regulator':e,
                    'mode':mode,
                    });
        return BioCyc2COBRA_regulators_O;

    def convertAndMap_BioCycRegulation2COBRA(
        self,
        BioCyc_regulation_I,
        BioCyc_reactions_I = None,
        BioCyc_enzymaticReactions2PolymerSegments_I = None,
        BioCyc_compounds_I = None,
        COBRA_reactions_I = None,
        COBRA_metabolites_I = None,
        chebi2inchi_I = None,
        #chebi2database_I = None,
        MetaNetX_reactions_I = None,
        MetaNetX_metabolites_I = None,):
        '''Convert and map BioCyc Regulation
        to COBRA model ids
        INPUT:
        BioCyc_regulation_I = listDict
        BioCyc_reactions_I = listDict of models_BioCyc_reactions
        BioCyc_enzymaticReactions2PolymerSegments_I = listDict of 
            join between models_BioCyc_enzymaticReactions and 
            models_BioCyc_polymerSegments
            (getJoin_genes_namesAndDatabase_modelsBioCycEnzymaticReactionsAndPolymerSegments)
        BioCyc_compounds_I = listDict of models_BioCyc_compounds
        COBRA_reactions_I = listDict of models_COBRA_reactions
        COBRA_metabolites_I = listDict of models_COBRA_metabolites
        chebi2inchi_I = listDict of CHEBI_ID to InCHI
        MetaNetX_reactions_I = listDict of MetaNetX reaction xrefs
        MetaNetX_metabolites_I = listDict of MetaNetX chemical xrefs
    
        OUTPUT:
    
        '''
        BioCyc_dependencies = models_BioCyc_dependencies();

        #reformat input into a dict for fast traversal
        if not chebi2inchi_I is None and chebi2inchi_I:
            chebi2inchi_dict_I = {r['CHEBI_ID']:r['InChI'] for r in chebi2inchi_I}
        else:
            chebi2inchi_dict_I=chebi2inchi_I;
            
        #if not chebi2database_I is None and chebi2database_I:
        #    chebi2database_dict_I = {r['CHEBI_ID']:r['InChI'] for r in chebi2database_I}
        #else:
        #    chebi2database_dict_I=chebi2database_I;

        if not BioCyc_compounds_I is None and BioCyc_compounds_I:
            #BioCyc_compounds_dict_I = {r['name']:r for r in BioCyc_compounds_I}
            BioCyc_compounds_dict_I = {}
            for row in BioCyc_compounds_I:
                keys = [];
                keys.append(row['name'])
                keys = list(set([k for k in keys if k!='']))
                for k in keys:
                    if not k in BioCyc_compounds_dict_I.keys():
                        BioCyc_compounds_dict_I[k]=[];
                    if not row in BioCyc_compounds_dict_I[k]:
                        BioCyc_compounds_dict_I[k].append(row);
        else:
            BioCyc_compounds_dict_I=BioCyc_compounds_I;

        if not BioCyc_reactions_I is None and BioCyc_reactions_I:
            BioCyc_reactions_dict_I = {}
            for row in BioCyc_reactions_I:
                keys = [];
                keys.append(row['common_name'])
                keys.extend(BioCyc_dependencies.convert_bioCycList2List(row['enzymatic_reaction']))
                keys = list(set([k for k in keys if k!='']))
                for k in keys:
                    if not k in BioCyc_reactions_dict_I.keys():
                        BioCyc_reactions_dict_I[k]=[];
                    if not row in BioCyc_reactions_dict_I[k]:
                        BioCyc_reactions_dict_I[k].append(row);
        else:
            BioCyc_reactions_dict_I=BioCyc_reactions_I;

        if not BioCyc_enzymaticReactions2PolymerSegments_I is None and BioCyc_enzymaticReactions2PolymerSegments_I:
            BioCyc_enzymaticReactions_dict_I = {}
            for row in BioCyc_enzymaticReactions2PolymerSegments_I:
                try:
                    if not row['name'] in BioCyc_enzymaticReactions_dict_I.keys():
                        BioCyc_enzymaticReactions_dict_I[row['name']]={
                            'name':'',
                            'enzyme':[],
                            'gene_ids':[],
                            'accession_1':[],
                            }
                    BioCyc_enzymaticReactions_dict_I[row['name']]['name']=row['name'];
                    BioCyc_enzymaticReactions_dict_I[row['name']]['enzyme'].append(row['enzyme']);
                    BioCyc_enzymaticReactions_dict_I[row['name']]['gene_ids'].extend(row['gene_ids']);
                    BioCyc_enzymaticReactions_dict_I[row['name']]['accession_1'].extend(row['accession_1']);
                except Exception as e:
                    print(e)
        else:
            BioCyc_enzymaticReactions_dict_I=BioCyc_enzymaticReactions2PolymerSegments_I;

        if not MetaNetX_reactions_I is None and MetaNetX_reactions_I:
            MetaNetX_reactions_dict_I = {}
            for row in MetaNetX_reactions_I:
                try:
                    if not row['MNX_ID'] in MetaNetX_reactions_dict_I.keys():
                        MetaNetX_reactions_dict_I[row['MNX_ID']]={}
                    key_value = row['#XREF'].split(':')
                    MetaNetX_reactions_dict_I[row['MNX_ID']][key_value[0]]=key_value[1];
                except Exception as e:
                    print(e)
                    #print(row)
        else:
            MetaNetX_reactions_dict_I=MetaNetX_reactions_I;

        if not MetaNetX_metabolites_I is None and MetaNetX_metabolites_I:
            MetaNetX_metabolites_dict_I = {}
            for row in MetaNetX_metabolites_I:
                try:
                    if not row['MNX_ID'] in MetaNetX_metabolites_dict_I.keys():
                        MetaNetX_metabolites_dict_I[row['MNX_ID']]={}
                    key_value = row['#XREF'].split(':')
                    MetaNetX_metabolites_dict_I[row['MNX_ID']][key_value[0]]=key_value[1];
                except Exception as e:
                    print(e)
                    #print(row)
        else:
            MetaNetX_metabolites_dict_I=MetaNetX_metabolites_I;

    
        regulation_O = [];
        for i,reg in enumerate(BioCyc_regulation_I):
            #if reg['name'] == 'Regulation of galSp by GalR DNA-binding transcriptional dual regulator':
            #    print('check')
            #elif reg['name'] == 'Regulation of ribonucleoside-diphosphate reductase by dATP':
            #    print('check');
            #elif reg['regulated_entity_enzymaticReaction'] == 'formate dehydrogenase':
            #    print('check');
            unique = {
                'regulator':reg['regulator'],
                'regulated_entity':reg['regulated_entity'],
                'mode':reg['mode'],
                'mechanism':reg['mechanism'],
                'name':reg['name'],
                'parent_classes':reg['parent_classes']
            }
            tmp = {
                'regulators_EcoCyc':[],
                'regulators_COBRA':[],
                'regulated_entities_EcoCyc':[],
                'regulated_entities_COBRA':[],
            }
            #convert the regulators
            if reg['regulator_gene']:
                original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                    reg['regulator_gene'],
                    BioCyc2COBRA_func_I=None,
                    BioCyc2COBRA_params_I={}
                );
                tmp['regulators_EcoCyc']=original;
                tmp['regulators_COBRA']=converted;
            elif reg['regulator_protein']:
                original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                    reg['regulator_protein'],
                    BioCyc2COBRA_func_I=None,
                    BioCyc2COBRA_params_I={}
                );
                tmp['regulators_EcoCyc']=original;
                tmp['regulators_COBRA']=converted;
            elif reg['regulator_RNA']:
                original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                    reg['regulator_RNA'],
                    BioCyc2COBRA_func_I=None,
                    BioCyc2COBRA_params_I={}
                );
                tmp['regulators_EcoCyc']=original;
                tmp['regulators_COBRA']=converted;
            elif reg['regulator_compound']:
            
                original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                    reg['regulator_compound'],
                    BioCyc_components_dict_I=BioCyc_compounds_dict_I,
                    BioCyc2COBRA_func_I=BioCyc_dependencies.map_BioCycCompound2COBRA,
                    BioCyc2COBRA_params_I={
                        'COBRA_metabolites_I':COBRA_metabolites_I,
                        'chebi2inchi_dict_I':chebi2inchi_dict_I,
                        'MetaNetX_metabolites_dict_I':MetaNetX_metabolites_dict_I,
                    }
                );
                tmp['regulators_EcoCyc']=original;
                tmp['regulators_COBRA']=converted;
            #convert the regulated_entities
            if reg['regulated_entity_gene']:
                original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                    reg['regulated_entity_gene'],
                    BioCyc2COBRA_func_I=None,
                    BioCyc2COBRA_params_I={}
                );
                tmp['regulated_entities_EcoCyc']=original;
                tmp['regulated_entities_COBRA']=converted;
            elif reg['regulated_entity_enzymaticReaction']:
                original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                    reg['regulated_entity_enzymaticReaction'],
                    BioCyc_components_dict_I=BioCyc_reactions_dict_I,
                    BioCyc2COBRA_func_I=BioCyc_dependencies.map_BioCycReaction2COBRA,
                    BioCyc2COBRA_params_I={
                        'COBRA_reactions_I':COBRA_reactions_I,
                        'MetaNetX_reactions_dict_I':MetaNetX_reactions_dict_I,
                        'BioCyc_reaction2Genes_dict_I':BioCyc_enzymaticReactions_dict_I,
                    }
                );
                tmp['regulated_entities_EcoCyc']=original;
                tmp['regulated_entities_COBRA']=converted;
            elif reg['regulated_entity_promoter']:
                original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                    reg['regulated_entity_promoter'],
                    BioCyc2COBRA_func_I=None,
                    BioCyc2COBRA_params_I={}
                );
                tmp['regulated_entities_EcoCyc']=original;
                tmp['regulated_entities_COBRA']=converted;
            elif reg['regulated_entity_product']:
                original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                    reg['regulated_entity_product'],
                    BioCyc2COBRA_func_I=None,
                    BioCyc2COBRA_params_I={}
                );
                tmp['regulated_entities_EcoCyc']=original;
                tmp['regulated_entities_COBRA']=converted;
            elif reg['regulated_entity_protein']:
                original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                    reg['regulated_entity_protein'],
                    BioCyc2COBRA_func_I=None,
                    BioCyc2COBRA_params_I={}
                );
                tmp['regulated_entities_EcoCyc']=original;
                tmp['regulated_entities_COBRA']=converted;
            #check that mappings/conversions took place
            if not tmp['regulators_EcoCyc'] or not tmp['regulated_entities_EcoCyc'] or \
                not tmp['regulators_COBRA'] or not tmp['regulated_entities_COBRA']:
                continue;
            #flatten
            EcoCyc_flattened = BioCyc_dependencies.crossMultiple_2lists(
                tmp['regulators_EcoCyc'],
                tmp['regulated_entities_EcoCyc'],
                'regulators_EcoCyc',
                'regulated_entities_EcoCyc',
            )
            COBRA_flattened = BioCyc_dependencies.crossMultiple_2lists(
                tmp['regulators_COBRA'],
                tmp['regulated_entities_COBRA'],
                'regulators_COBRA',
                'regulated_entities_COBRA',
            )
            for i in range(len(EcoCyc_flattened)):
                tmp1 = {};
                tmp1.update(EcoCyc_flattened[i])
                tmp1.update(COBRA_flattened[i])
                tmp1.update(unique)        
                regulation_O.append(tmp1);
                        
        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        data_O = [];
        for row in regulation_O:
            if not row in data_O:
                data_O.append(row);
        return data_O;

    def execute_getBiomassProducingPathwayComponents_BioCycAndCOBRA(
        self,
        biomassProducingPathways,
        ):
        ''' '''
        pathways = [d['Subpathway'] for d in biomassProducingPathways if d['used_']=="TRUE"]

        #reorganize into subpathways
        subpathways_dict = {};
        for d in biomassProducingPathways:
            if d['used_'] and d['used_']=="TRUE":
                if not d['Pathway'] in subpathways_dict.keys():
                    subpathways_dict[d['Pathway']]={};
                if not d['Pathway'] in subpathways_dict[d['Pathway']].keys():
                    subpathways_dict[d['Pathway']][d['Pathway']]=[];
                if not d['Subpathway'] in subpathways_dict[d['Pathway']].keys():
                    subpathways_dict[d['Pathway']][d['Subpathway']]=[];
                subpathways_dict[d['Pathway']][d['Subpathway']].append(d['Subpathway']);
                subpathways_dict[d['Pathway']][d['Pathway']].append(d['Subpathway']);
        subpathways_dict['all']={'all':pathways};

        #map the subpathway components        
        subpathways2components_dict = {};
        for k1,v1 in subpathways_dict.items():
            subpathways2components_dict[k1]={};
            for k2,v2 in v1.items():
                gene_ids,rxn_ids,met_ids,met_ids_deformated = \
                    self.get_geneIDsAndRxnIDsAndMetIDs_modelsBioCycAndModelsCOBRA(v2)
                subpathways2components_dict[k1][k2]={
                    'gene_ids':gene_ids,
                    'rxn_ids':rxn_ids,
                    'met_ids':met_ids,
                    'met_ids_deformated':met_ids_deformated,
                };  
        return subpathways2components_dict;

    def get_geneIDsAndRxnIDsAndMetIDs_modelsBioCycAndModelsCOBRA(
        self,
        pathways):

        #initialize supporting objects
        cobra01 = models_COBRA_query(self.session,self.engine,self.settings);
        cobra01.initialize_supportedTables();
        cobra_dependencies = models_BioCyc_dependencies();

        #query the pathways
        biocyc_pathways = self.getParsed_genesAndPathwaysAndReactions_namesAndDatabase_modelsBioCycPathways(
            names_I=pathways,
            database_I='ECOLI',
            query_I={},
            output_O='listDict',
            dictColumn_I=None);
        genes = list(set([g['gene'] for g in biocyc_pathways if g['gene']!='']));
        #join list of genes with alternative identifiers
        biocyc_genes = self.getParsed_genesAndAccessionsAndSynonyms_namesAndDatabase_modelsBioCycPolymerSegments(
            names_I=genes,
            database_I='ECOLI',
            query_I={},
            output_O='listDict',
            dictColumn_I=None);
        gene_ids = list(set(genes + [g['synonym'] for g in biocyc_genes if g['synonym']]));
        accession_1 = list(set([g['accession_1'] for g in biocyc_genes if g['accession_1']!='']));
        #Join accession_1 with COBRA reactions
        cobra_rxnIDs = cobra01.get_rows_modelIDAndOrderedLocusNames_dataStage02PhysiologyModelReactions(
            model_id_I='150526_iDM2015',
            ordered_locus_names_I=accession_1,
            query_I={},
            output_O='listDict',
            dictColumn_I=None)
        rxn_ids = list(set([g['rxn_id'].replace('_reverse','') for g in cobra_rxnIDs if g['rxn_id']!='']));
        #COBRA metabolites
        met_ids = list(set([p for g in cobra_rxnIDs if g['products_ids'] for p in g['products_ids']]+\
            [p for g in cobra_rxnIDs if g['reactants_ids'] for p in g['reactants_ids']]));
        #deformat met_ids
        from SBaaS_models.models_COBRA_dependencies import models_COBRA_dependencies
        cobra_dependencies = models_COBRA_dependencies();
        met_ids_deformated = list(set([cobra_dependencies.deformat_metid(m).replace('13dpg','23dpg')\
            .replace('3pg','Pool_2pg_3pg')\
            .replace('glycogen','adpglc')\
            .replace('uacgam','udpglcur') for m in met_ids]));
        #return values
        return gene_ids,rxn_ids,met_ids,met_ids_deformated;