from .models_BioCyc_io import models_BioCyc_io
from .models_BioCyc_dependencies import models_BioCyc_dependencies

class models_BioCyc_execute(models_BioCyc_io):

    def execute_convertAndMap_BioCycRegulation2COBRA(
        self,
        ):
        ''' '''
        pass;

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
                'name':row['name']
            }
            tmp = {
                'left_EcoCyc':[],
                'left_COBRA':[],
                'right_EcoCyc':[],
                'right_COBRA':[],
            }
            if row['regulator'] in BioCyc2COBRA_TFs_I.keys():
                for reg in BioCyc2COBRA_TFs_I[row['regulator']]:
                    for i in range(len(reg['ligands']['BioCyc_name'])):
                        tmp = {
                            'left_EcoCyc':reg['ligands']['BioCyc_name'][i],
                            'left_COBRA':reg['ligands']['COBRA_met_id'][i],
                            'right_EcoCyc':reg['tu'],
                            'right_COBRA':reg['tu'],
                            'regulator':row['regulator'],
                            'regulated_entity':row['regulated_entity'],
                            'mode':reg['mode'],
                            'mechanism':'ligand-transcription factor-binding',
                            'name':row['name']
                        };
                        BioCyc2COBRA_regulation_all.append(tmp);
                    for i in range(len(reg['genes'])):
                        tmp = {
                            'left_EcoCyc':reg['genes'][i],
                            'left_COBRA':reg['genes'][i],
                            'right_EcoCyc':reg['tu'],
                            'right_COBRA':reg['tu'],
                            'regulator':row['regulator'],
                            'regulated_entity':row['regulated_entity'],
                            'mode':reg['mode'],
                            'mechanism':'gene-transcription factor',
                            'name':row['name']
                        };
                        BioCyc2COBRA_regulation_all.append(tmp);
                    for i in range(len(reg['ligands']['BioCyc_name'])):
                        tmp = {
                            'left_EcoCyc':reg['ligands']['BioCyc_name'][i],
                            'left_COBRA':reg['ligands']['COBRA_met_id'][i],
                            'right_EcoCyc':row['regulated_entities_EcoCyc'],
                            'right_COBRA':row['regulated_entities_COBRA'],
                            'regulator':row['regulator'],
                            'regulated_entity':row['regulated_entity'],
                            'mode':reg['mode']+row['mode'],
                            'mechanism':'ligand-transcription factor-gene',
                            'name':row['name']
                        };
                        BioCyc2COBRA_regulation_all.append(tmp);
                    for i in range(len(reg['genes'])):
                        tmp = {
                            'left_EcoCyc':reg['genes'][i],
                            'left_COBRA':reg['genes'][i],
                            'right_EcoCyc':row['regulated_entities_EcoCyc'],
                            'right_COBRA':row['regulated_entities_COBRA'],
                            'regulator':row['regulator'],
                            'regulated_entity':row['regulated_entity'],
                            'mode':row['mode'],
                            'mechanism':'gene-transcription factor-gene',
                            'name':row['name']
                        };
                        BioCyc2COBRA_regulation_all.append(tmp);
                tmp = {
                    'left_EcoCyc':row['regulators_EcoCyc'],
                    'left_COBRA':row['regulators_COBRA'],
                    'right_EcoCyc':row['regulated_entities_EcoCyc'],
                    'right_COBRA':row['regulated_entities_COBRA'],
                };
                tmp.update(unique);
                BioCyc2COBRA_regulation_all.append(tmp);
            else:
                tmp = {
                    'left_EcoCyc':row['regulators_EcoCyc'],
                    'left_COBRA':row['regulators_COBRA'],
                    'right_EcoCyc':row['regulated_entities_EcoCyc'],
                    'right_COBRA':row['regulated_entities_COBRA'],
                };
                tmp.update(unique);
                BioCyc2COBRA_regulation_all.append(tmp);
        return BioCyc2COBRA_regulation_all;

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
            BioCyc2COBRA_regulators = list(set([r['regulator'] for r in BioCyc2COBRA_regulation_I]));
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
            ##spot checks:
            #if e == 'Cra DNA-binding transcriptional dual regulator':
            #    #error mapping fdp_c
            #    print('check');
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
            unique = {
                'regulator':reg['regulator'],
                'regulated_entity':reg['regulated_entity'],
                'mode':reg['mode'],
                'mechanism':reg['mechanism'],
                'name':reg['name']
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
                        'COBRA_reactions_I':COBRA_reactions_I
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
        return regulation_O;