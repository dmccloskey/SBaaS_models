# Resources
from molmass.molmass import Formula
# System dependencies
import re
class models_BioCyc_dependencies():
    def convert_bioCycRxn2LeftAndRight(self,rxn_str_I):
        '''Convert biocyc reaction string to left and right components
        
        INPUT:
        rxn_str_I = string
        OUTPUT:
        left_O = list of strings
        right_O = list of strings'''

        #break into left/right
        rxn_lst = rxn_str_I.split('  &rarr;  ');
        left = rxn_lst[0].split(' + ');
        right = rxn_lst[1].split(' + ');
        return left,right;
    def convert_bioCycList2List(self,list_I):
        '''Convert biocyc string list to list
        INPUT:
        list_I = string
        OUTPUT:
        list_O = list
        '''
        list_O = [];
        try:
            list_tmp = list_I.replace('(','').replace(')','').split('" "');
            list_O = [s.replace('"','') for s in list_tmp]
        except Exception as e:
            print(e);
        return list_O;
    def convert_gene2RegulatedEntity(self,gene_I):
        '''Convert gene to biocyc regulated entity
        INPUT:
        gene_I = string
        OUTPUT:
        regulatedEntity_O = string
        '''
        regulatedEntity_O = '';
        try:
            regulatedEntity_O = ('%sp' %(gene_I));
        except Exception as e:
            print(e);
        return regulatedEntity_O;
    def extract_regulatedEntityFromComponents(self,components_I):
        '''extract out regulated entities from biocyc polymerSegment components'''

        components_lst = self.convert_bioCycList2List(components_I);
        regulated_entity = None;
        for component in components_lst:
            if self.check_promoter(component):
                regulated_entity = component;
        return regulated_entity;
    def check_promoter(self,component_I):
        ''' '''
        promoter_O=False;
        patterns = ['[a-z][a-z][a-z][A-Z]p[0-9]',
                   '[a-z][a-z][a-z][A-Z]p',
                   '[a-z][a-z][a-z]p']
        for pattern in patterns:
            if not re.match(pattern,component_I) is None:
                promoter_O=True;
                break;
        return promoter_O;
    def parse_transcriptionUnit(self,tu_I):
        '''Parse a TU string into individual genes
        INPUT:
        tu_I = string, e.g. gadAX-wxa-wcAB
        OUTPUT:
        genes_O = list of genes
        '''

        genes_O = [];
        tus = tu_I.split('-');
        for tu in tus:
            if len(tu)==3:
                #3 letter gene
                genes_O.append(tu);
            elif len(tu)==4:
                #4 letter gene
                genes_O.append(tu);
            else:
                #4 letter genes
                gene_base = tu[:3];
                gene_ends = tu[3:];
                for end in gene_ends:
                    gene = '%s%s' %(gene_base,end);
                    genes_O.append(gene);
        return genes_O;
    def count_parentClasses(self,data_I):
        '''Count the frequency of parent classes
        INPUT:
        data_I = listDict
        OUTPUT:
        data_O = listDict [{'parent_class':string,'frequency',int}]'''
        
        #generate a list of unique parent clases
        parent_classes = [d['parent_class'] for d in data_I];
        parent_classes = list(set(parent_classes));
        #generate the dict iterator for the counts
        counts_O = {pc:0 for pc in parent_classes};
        #count unique parent classes
        for d in data_I:
            counts_O[d['parent_class']]+=1;
        #reformat the counts into a list of dictionaries
        data_O = [{'parent_class':k,'frequency':v} for k,v in counts_O.items()];
        return data_O;

    ##Mapping between BioCyc And COBRA functions
    def map_BioCyc2COBRA(
        self,
        BioCyc_components_I,
        BioCyc_components_dict_I=None,
        BioCyc2COBRA_func_I=None,
        BioCyc2COBRA_params_I={}
        ):
        '''Map BioCyc 2 Cobra component
        INPUT:
        BioCyc_components_I = list of bioCyc components
        BioCyc_components_dict_I = dictDict: {bioCyc component:{'id1':,'id2':,...},...}
        BioCyc2COBRA_func_I = function object to map bioCyc to COBRA ID
        BioCyc2COBRA_params_I = dict of parameters for BioCyc2COBRA_func_I
        OUTPUT:
        original = list, original biocyc component names that were matched
        converted = list, converted COBRA component names that were matched
    
        '''
        original = [];
        converted = [];
        for component in BioCyc_components_I:
            if component == 'fructose 1,6-bisphosphate':
                print('check');
            elif component == 'glutamine synthetase':
                print('check');
            elif component == 'isocitrate lyase':
                print('check');
            conv = None;
            if not BioCyc2COBRA_func_I is None:
                component_dict = None;
                if not BioCyc_components_dict_I is None and \
                    component in BioCyc_components_dict_I.keys():
                    components = BioCyc_components_dict_I[component]
                    for component_dict in components:
                        conv = BioCyc2COBRA_func_I(component_dict,**BioCyc2COBRA_params_I);
                        original.append(component);
                        converted.append(conv);
                elif type(component)==type({}):
                    conv = BioCyc2COBRA_func_I(component,**BioCyc2COBRA_params_I);
                    original.append(component);
                    converted.append(conv);
                else:
                    original.append(component);
                    converted.append(conv);
            else:
                original.append(component);
                converted.append(conv);
        return original,converted;
    def crossMultiple_2lists(
        self,
        list_1,list_2,listKey_1='l1',listKey_2='l2'):
        '''Cross multiply two lists'''
        list_O = [];
        for l1 in list_1:
            for l2 in list_2:
                list_O.append({
                        listKey_1:l1,
                        listKey_2:l2
                    });
        return list_O;
    def map_BioCycReaction2COBRA(
        self,
        BioCyc_reaction_I,
        COBRA_reactions_I,
        MetaNetX_reactions_dict_I={},
        BioCyc_reaction2Genes_dict_I={}
        ):
        '''map biocyc reaction to COBRA rxn_id
        INPUT:
        BioCyc_reaction_I = BioCyc reaction identifier
        COBRA_reactions_I = listDict representation of COBRA reaction information
        MetaNetX_reactions_dict_I = dictionary of {"MNX_ID":{'bigg':,'metacyc':,...},...}
        OUTPUT:
        rxn_id_O = string, rxn_id
        '''
        rxn_id_O = None;
        for row in COBRA_reactions_I:
            if self.match_BioCycReaction2COBRA(
                BioCyc_reaction_I,row,
                MetaNetX_reactions_dict_I,
                BioCyc_reaction2Genes_dict_I):
                rxn_id_O = row['rxn_id'];
                break;
        return rxn_id_O;
    def match_BioCycReaction2COBRA(
        self,
        BioCyc_reaction_I,
        COBRA_reaction_I,
        MetaNetX_reactions_dict_I,
        BioCyc_reaction2Genes_dict_I):
        '''match biocyc reaction to COBRA rxn_id
        INPUT:
        BioCyc_reaction_I = BioCyc reaction identifier
        COBRA_reactions_I = Dict representation of COBRA reaction information
        MetaNetX_reactions_dict_I = dictionary of {"MNX_ID":{'bigg':,'metacyc':,...},...}
        BioCyc_reaction2Genes_dict_I = dictionary of {"name":{'gene_ids':,'accession_1':,...},...}
        OUTPUT:
        match = boolean
        '''
        #parse biocyc reaction_ids
        biocyc_names = [];
        biocyc_names.append(BioCyc_reaction_I['common_name'])
        biocyc_names.extend(self.convert_bioCycList2List(
            BioCyc_reaction_I['names']
        ));
        biocyc_names.extend(self.convert_bioCycList2List(
            BioCyc_reaction_I['synonyms']
        ));
        biocyc_names.extend(self.convert_bioCycList2List(
            BioCyc_reaction_I['enzymatic_reaction']
        ));
        biocyc_names = list(set([r.lower() for r in biocyc_names if r!='']))
        biocyc_ec_numbers = self.convert_bioCycList2List(
            BioCyc_reaction_I['ec_number']
        );
        biocyc_frame_ids = [BioCyc_reaction_I['frame_id']];
        biocyc_accessions = [];
        #parse cobra reaction_ids
        cobra_ec_numbers = []
        cobra_frame_ids = []
        cobra_metanetx_ids = []
        cobra_accessions = []
        cobra_name = COBRA_reaction_I['rxn_name'].lower();
        if not 'database_links' in COBRA_reaction_I.keys() or \
            COBRA_reaction_I['database_links'] is None:
            print('no database_links provided for mapping')
        else:
            if 'EC Number' in COBRA_reaction_I['database_links']:
                for row in COBRA_reaction_I['database_links']['EC Number']:
                    cobra_ec_number = row['id'];
                    cobra_ec_numbers.append(cobra_ec_number)
            if 'BioCyc' in COBRA_reaction_I['database_links']:
                for row in COBRA_reaction_I['database_links']['BioCyc']:
                    cobra_frame_id = row['id'].replace('META:','')
                    cobra_frame_ids.append(cobra_frame_id)
            if 'MetaNetX (MNX) Equation' in COBRA_reaction_I['database_links']:
                for row in COBRA_reaction_I['database_links']['MetaNetX (MNX) Equation']:
                    if row['id'] in MetaNetX_reactions_dict_I.keys() and \
                        'metacyc' in MetaNetX_reactions_dict_I[row['id']].keys():
                        cobra_metanetx_id = MetaNetX_reactions_dict_I[row['id']]['metacyc']
                        cobra_metanetx_ids.append(cobra_metanetx_id)
        if BioCyc_reaction2Genes_dict_I:
            for e in self.convert_bioCycList2List(
                BioCyc_reaction_I['enzymatic_reaction']
                ):
                if e in BioCyc_reaction2Genes_dict_I.keys():
                    biocyc_accessions.extend(BioCyc_reaction2Genes_dict_I[e]['accession_1']);
                    cobra_accessions.extend(COBRA_reaction_I['genes']);
            #spot check            
            if '6-phosphofructokinase' in self.convert_bioCycList2List(
                    BioCyc_reaction_I['enzymatic_reaction']
                    ):
                print('Check')
            if not biocyc_accessions:
                print('Check')
        #remove duplicates
        cobra_ec_numbers = list(set(cobra_ec_numbers))
        cobra_frame_ids = list(set(cobra_frame_ids))
        cobra_metanetx_ids = list(set(cobra_metanetx_ids))
        biocyc_accessions = list(set(biocyc_accessions))
        cobra_accessions = list(set(cobra_accessions))
        #match
        match = False;
        if biocyc_names and \
            cobra_name in biocyc_names:
            match = True;
        if biocyc_frame_ids and cobra_frame_ids and \
            len(list(set(biocyc_frame_ids+cobra_frame_ids)))<\
            len(biocyc_frame_ids+cobra_frame_ids):
                match = True;
        if biocyc_frame_ids and cobra_metanetx_ids and \
            len(list(set(biocyc_frame_ids+cobra_metanetx_ids)))<\
            len(biocyc_frame_ids+cobra_metanetx_ids):
                match = True;
        if biocyc_ec_numbers and cobra_ec_numbers and \
            len(list(set(biocyc_ec_numbers+cobra_ec_numbers)))<\
            len(biocyc_ec_numbers+cobra_ec_numbers):
                match = True;
        if biocyc_accessions and cobra_accessions and \
            len(list(set(biocyc_accessions+cobra_accessions)))<\
            len(biocyc_accessions+cobra_accessions):
                match = True;
        return match; 
    def map_BioCycCompound2COBRA(
        self,
        BioCyc_metabolite_I,
        COBRA_metabolites_I,
        chebi2inchi_dict_I={},
        MetaNetX_metabolites_dict_I={}
        ):
        '''map biocyc reaction to COBRA rxn_id
        INPUT:
        BioCyc_metabolite_I = BioCyc metabolite identifier
        COBRA_metabolites_I = listDict representation of COBRA metabolite information
        chebi2inchi_dict_I = dictionary of {"CHEBI_ID":"INCHI"}
        MetaNetX_metabolites_dict_I = dictionary of {"MNX_ID":{'bigg':,'metacyc':,...},...}
        OUTPUT:
        met_id_O = string, met_id
        '''
        met_id_O = None;
        for row in COBRA_metabolites_I:
            if self.match_BioCycMetabolite2COBRA(
                BioCyc_metabolite_I,row,
                chebi2inchi_dict_I,
                MetaNetX_metabolites_dict_I):
                met_id_O = row['met_id'];
                break;
        return met_id_O;
    def match_BioCycMetabolite2COBRA(
        self,
        BioCyc_metabolite_I,
        COBRA_metabolite_I,
        chebi2inchi_dict_I,
        MetaNetX_metabolites_dict_I={}):
        '''match biocyc metabolite to COBRA rxn_id
        INPUT:
        BioCyc_metabolite_I = BioCyc metabolite identifier
        COBRA_metabolites_I = Dict representation of COBRA metabolite information
        chebi2inchi_dict_I = dictionary of {"CHEBI_ID":"INCHI"}
        MetaNetX_metabolites_dict_I = dictionary of {"MNX_ID":{'bigg':,'metacyc':,...},...}
        OUTPUT:
        match = boolean
        '''
        #parse biocyc metabolite_ids
        biocyc_names = [];
        biocyc_names.append(BioCyc_metabolite_I['systematic_name'])
        biocyc_names.append(BioCyc_metabolite_I['common_name'])
        biocyc_names.extend(self.convert_bioCycList2List(
            BioCyc_metabolite_I['names']
        ));
        biocyc_names.extend(self.convert_bioCycList2List(
            BioCyc_metabolite_I['synonyms']
        ));
        biocyc_names = list(set([r.lower() for r in biocyc_names if r!='']))
        biocyc_inchi_numbers = self.convert_bioCycList2List(
            BioCyc_metabolite_I['inchi']
        );
        biocyc_frame_ids = [BioCyc_metabolite_I['frame_id']];
        #parse cobra metabolite_ids
        cobra_inchi_numbers = []
        cobra_frame_ids = []
        cobra_metanetx_ids = []
        cobra_name = COBRA_metabolite_I['met_name'].lower();
        if not 'database_links' in COBRA_metabolite_I.keys() or \
            COBRA_metabolite_I['database_links'] is None:
            print('no database_links provided for mapping')
        else:
            if 'CHEBI' in COBRA_metabolite_I['database_links']:
                for row in COBRA_metabolite_I['database_links']['CHEBI']:
                    cobra_chebi_number = row['id'].replace('CHEBI:','');
                    if cobra_chebi_number in chebi2inchi_dict_I.keys():
                        cobra_inchi_number = chebi2inchi_dict_I[cobra_chebi_number]
                        cobra_inchi_numbers.append(cobra_inchi_number)
            if 'BioCyc' in COBRA_metabolite_I['database_links']:
                for row in COBRA_metabolite_I['database_links']['BioCyc']:
                    cobra_frame_id = row['id'].replace('META:','')
                    cobra_frame_ids.append(cobra_frame_id)
            if 'MetaNetX (MNX) Chemical' in COBRA_metabolite_I['database_links']:
                for row in COBRA_metabolite_I['database_links']['MetaNetX (MNX) Chemical']:
                    if row['id'] in MetaNetX_metabolites_dict_I.keys() and \
                        'metacyc' in MetaNetX_metabolites_dict_I[row['id']].keys():
                        cobra_metanetx_id = MetaNetX_metabolites_dict_I[row['id']]['metacyc']
                        cobra_metanetx_ids.append(cobra_metanetx_id)
        #remove duplicates
        cobra_inchi_numbers = list(set(cobra_inchi_numbers))
        cobra_frame_ids = list(set(cobra_frame_ids))
        cobra_metanetx_ids = list(set(cobra_metanetx_ids))
        #match
        match = False;
        if biocyc_names and \
            cobra_name in biocyc_names:
            match = True;
        if biocyc_frame_ids and cobra_frame_ids and \
            len(list(set(biocyc_frame_ids+cobra_frame_ids)))<\
            len(biocyc_frame_ids+cobra_frame_ids):
                match = True;
        if biocyc_frame_ids and cobra_metanetx_ids and \
            len(list(set(biocyc_frame_ids+cobra_metanetx_ids)))<\
            len(biocyc_frame_ids+cobra_metanetx_ids):
                match = True;
        if biocyc_inchi_numbers and cobra_inchi_numbers and \
            len(list(set(biocyc_inchi_numbers+cobra_inchi_numbers)))<\
            len(biocyc_inchi_numbers+cobra_inchi_numbers):
                match = True;
        return match; 