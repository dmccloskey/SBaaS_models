#SBaaS
from .models_BioCyc_query import models_BioCyc_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from ddt_python.ddt_container import ddt_container
from ddt_python.ddt_container_filterMenuAndChart2dAndTable import ddt_container_filterMenuAndChart2dAndTable
from listDict.listDict import listDict

class models_BioCyc_io(models_BioCyc_query,
                    sbaas_template_io):
    def export_geneRegulators_js(self,gene_I,database_I='ECOLI',query_I={},data_dir_I='tmp'):
        '''Export force diagram
        INPUT:
        OUTPUT:
        '''
        
        data_O = [];
        # get fpkm tracking data
        data_O = self.getJoin_regulators_geneAndDatabase_modelsBioCycProteinAndRegulationAndPolymerSegment(
            gene_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        # make the data parameters
        data1_keys = [
                    'regulator',
                    'gene',
                    'transcription_unit',
                    'protein_name',
                    'regulated_entity',
                    'mode',
                    ];
        data1_nestkeys = [
            'gene',
            'transcription_unit',
            'regulated_entity',
            'mode',
            #'regulator',
            #'protein_name',
            ];
        data1_keymap = {'xdata':'parent_classes',
                        'ydata':'mode',
                        'serieslabel':'mode',
                        'featureslabel':''};
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
                data_filtermenu=data_O,
                data_filtermenu_keys=data1_keys,
                data_filtermenu_nestkeys=data1_nestkeys,
                data_filtermenu_keymap=data1_keymap,
                data_svg_keys=None,
                data_svg_nestkeys=None,
                data_svg_keymap=None,
                data_table_keys=None,
                data_table_nestkeys=None,
                data_table_keymap=None,
                data_svg=None,
                data_table=None,
                svgtype='treelayout2d_01',
                #svgtype='forcelayout2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='',
                svgy1axislabel='',
                tablekeymap = [data1_keymap],
                svgkeymap = [data1_keymap],
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=[0],
                svgfilters=None,
                svgtileheader='BioCyc Regulation',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I= {
                            #"svgtype":'treelayout2d_01',
                            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                            "svgwidth":500,
                            "svgheight":500,
                            "svgduration":750,
                            "datalastchild":'regulator'
                            }
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_geneRegulatedEntities_js(self,gene_I,database_I='ECOLI',query_I={},data_dir_I='tmp'):
        '''Export force diagram
        INPUT:
        OUTPUT:
        '''
        
        data_O = [];
        # get fpkm tracking data
        data_O = self.getJoin_regulatedEntities_geneAndDatabase_modelsBioCycProteinAndRegulationAndPolymerSegment(
            gene_I,database_I=database_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        # make the data parameters
        data1_keys = [
                    'regulator',
                    'gene',
                    'protein_name',
                    'transcription_unit',
                    'regulated_entity',
                    ];
        data1_nestkeys = [
            'gene',
            #'protein_name',
            'mode',
            'regulated_entity',
            #'transcription_unit',
                          ];
        data1_keymap = {'xdata':'parent_classes',
                        'ydata':'mode',
                        'serieslabel':'mode',
                        'featureslabel':''};
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
                data_filtermenu=data_O,
                data_filtermenu_keys=data1_keys,
                data_filtermenu_nestkeys=data1_nestkeys,
                data_filtermenu_keymap=data1_keymap,
                data_svg_keys=None,
                data_svg_nestkeys=None,
                data_svg_keymap=None,
                data_table_keys=None,
                data_table_nestkeys=None,
                data_table_keymap=None,
                data_svg=None,
                data_table=None,
                svgtype='treelayout2d_01',
                #svgtype='forcelayout2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='',
                svgy1axislabel='',
                tablekeymap = [data1_keymap],
                svgkeymap = [data1_keymap],
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=[0],
                svgfilters=None,
                svgtileheader='BioCyc Regulation',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I= {
                            #"svgtype":'treelayout2d_01',
                            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                            "svgwidth":500,
                            "svgheight":500,
                            "svgduration":750,
                            "datalastchild":'transcription_unit'
                            }
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());

    def export_geneProteinFeatures_js(self,gene_I,database_I='ECOLI',query_I={},data_dir_I='tmp'):
        '''Export force diagram
        INPUT:
        OUTPUT:
        '''
        pass;

    '''
	
    INPUT: gene_id
    OUTPUT: protein_features

    name FROM models_biocyc_proteins

    models_biocyc_proteinFeatures
	    feature_of LIKE '%%s%' %(protein_name)
    '''