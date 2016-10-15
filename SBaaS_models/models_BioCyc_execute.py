from .models_BioCyc_io import models_BioCyc_io
from .models_BioCyc_dependencies import models_BioCyc_dependencies

class models_BioCyc_execute(models_BioCyc_io):

    def execute_convertAndMap_BioCycRegulation2COBRA(
        self,
        ):
        ''' '''
        pass;

    def convertAndMap_BioCycTranscriptionFactor2COBRA(
        self,
        BioCyc2COBRA_regulation_I,
        BioCyc_compounds_I,
        COBRA_metabolites_I,
        chebi2inchi_I
        ):
        ''' '''
        
        from SBaaS_models.models_BioCyc_dependencies import models_BioCyc_dependencies
        BioCyc_dependencies = models_BioCyc_dependencies();

        BioCyc2COBRA_regulators = list(set([r['regulator'] for r in BioCyc2COBRA_regulation_I]));
        chebi2inchi_dict_I = {r['CHEBI_ID']:r['InChI'] for r in chebi2inchi_I}
        BioCyc_compounds_dict_I = {r['name']:r for r in BioCyc_compounds_I}

        BioCyc2COBRA_regulators_O = {}
        for e in BioCyc2COBRA_regulators:
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
                            genes.extend(BioCyc_dependencies.convert_bioCycList2List(p['gene']));  
                    elif compounds:
                        #map the ligand names...
                        original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                            [c['name'] for c in compounds],
                            BioCyc_components_dict_I=BioCyc_compounds_dict_I,
                            BioCyc2COBRA_func_I=BioCyc_dependencies.map_BioCycCompound2COBRA,
                            BioCyc2COBRA_params_I={
                                'COBRA_metabolites_I':COBRA_metabolites_I,
                                'chebi2inchi_dict_I':chebi2inchi_dict_I,
                            }
                        );
                        ligands['BioCyc_name'].extend(original)
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
                            genes.extend(BioCyc_dependencies.convert_bioCycList2List(p['gene'])); 
                    elif compounds:
                        original,converted = BioCyc_dependencies.map_BioCyc2COBRA(
                            [c['name'] for c in compounds],
                            BioCyc_components_dict_I=BioCyc_compounds_dict_I,
                            BioCyc2COBRA_func_I=BioCyc_dependencies.map_BioCycCompound2COBRA,
                            BioCyc2COBRA_params_I={
                                'COBRA_metabolites_I':COBRA_metabolites_I,
                                'chebi2inchi_dict_I':chebi2inchi_dict_I,
                            }
                        );
                        ligands['BioCyc_name'].extend(original)
                        ligands['COBRA_met_id'].extend(converted)
                #check for tus
                if e in left:
                    tus.append(e);
                    mode = '("-")';
                if e in right:
                    tus.append(e);
                    mode = '("+")';
                genes = [g for g in genes if g!='']  
                ##flatten
                #EcoCyc_flattened = BioCyc_dependencies.crossMultiple_2lists(
                #    tmp['regulators_EcoCyc'],
                #    tmp['regulated_entities_EcoCyc'],
                #    'regulators_EcoCyc',
                #    'regulated_entities_EcoCyc',
                #)
                #COBRA_flattened = BioCyc_dependencies.crossMultiple_2lists(
                #    tmp['regulators_COBRA'],
                #    tmp['regulated_entities_COBRA'],
                #    'regulators_COBRA',
                #    'regulated_entities_COBRA',
                #)
                #for i in range(len(EcoCyc_flattened)):
                #    tmp1 = {};
                #    tmp1.update(EcoCyc_flattened[i])
                #    tmp1.update(COBRA_flattened[i])
                #    tmp1.update(unique)        
                #    regulation_O.append(tmp1);
                BioCyc2COBRA_regulators_O[e] = {
                    'ligands':ligands,
                    'genes':genes,
                    'tus':tus,
                    'regulator':e,
                    'mode':mode,
                    };
        return BioCyc2COBRA_regulators_O;

    def convertAndMap_BioCycRegulation2COBRA(
        self,
        BioCyc_regulation_I,
        BioCyc_reactions_I,
        BioCyc_compounds_I,
        COBRA_reactions_I,
        COBRA_metabolites_I,
        chebi2inchi_I):
        '''Convert and map BioCyc Regulation
        to COBRA model ids
        INPUT:
        BioCyc_regulation_I
        COBRA_reactions_I
        COBRA_metabolites_I
    
        OUTPUT:
    
        '''
        BioCyc_dependencies = models_BioCyc_dependencies();

        #reformat input into a dict for fast traversal
        chebi2inchi_dict_I = {r['CHEBI_ID']:r['InChI'] for r in chebi2inchi_I}
        BioCyc_reactions_dict_I = {r['common_name']:r for r in BioCyc_reactions_I}
        BioCyc_compounds_dict_I = {r['name']:r for r in BioCyc_compounds_I}
    
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