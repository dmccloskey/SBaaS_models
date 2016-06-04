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
        return regulated_entity