# Resources
from molmass.molmass import Formula
# System dependencies
import re
class models_BioCyc_dependencies():
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
        patterns = ['[a-z][a-z][a-z][A-Z]p[0-9]',
                   '[a-z][a-z][a-z][A-Z]p',
                   '[a-z][a-z][a-z]p']
        for component in components_lst:
            for pattern in patterns:
                if not re.match(pattern,component) is None:
                    regulated_entity = component;
                    break;
        return regulated_entity;

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