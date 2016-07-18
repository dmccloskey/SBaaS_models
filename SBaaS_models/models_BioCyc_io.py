#SBaaS
from .models_BioCyc_query import models_BioCyc_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
from .models_BioCyc_dependencies import models_BioCyc_dependencies
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from ddt_python.ddt_container import ddt_container
from ddt_python.ddt_container_filterMenuAndChart2dAndTable import ddt_container_filterMenuAndChart2dAndTable
from listDict.listDict import listDict
import copy

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
                #svgtype='indentedtreelayout2d_01',
                #svgtype='treelayout2d_01',
                svgtype='forcelayout2d_01',
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
                            "datalastchild":'regulator',
                            'colclass':"col-sm-12"
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
        # get data
        data_O = self.getJoin_regulatedEntities_geneAndDatabase_modelsBioCycProteinAndRegulationAndPolymerSegment(
            gene_I,database_I=database_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        #for d in data_O:
        #    # convert mode to float
        #    if d['mode'] == '+': mode = 1
        #    elif d['mode'] == '-': mode = -1
        #    d['mode_'] = mode;

        # make the data parameters
        data1_keys = [
                    'regulator',
                    'gene',
                    #'protein_name',
                    'transcription_unit',
                    'regulated_entity',
                    ];
        data1_nestkeys = [
            'gene',
            'regulator',
            #'protein_name',
            'mode',
            'regulated_entity',
            #'transcription_unit',
                          ];
        data1_keymap = {'xdata':'mode_',
                        'ydata':'mode_',
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
                #svgtype='indentedtreelayout2d_01',
                #svgtype='radialtreelayout2d_01',
                #svgtype='treelayout2d_01',
                svgtype='forcelayout2d_01',
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
                            "svgradius":250,
                            "datalastchild":'transcription_unit',
                            'colclass':"col-sm-12"
                            }
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_geneReactions_js(self,gene_I,database_I='ECOLI',query_I={},data_dir_I='tmp'):
        '''Export force diagram
        INPUT:
        OUTPUT:
        '''
        
        data_O = [];
        # get data
        data_O = self.getJoin_reactions_geneAndDatabase_modelsBioCycProteinAndPolymerSegmentAndReaction(
            gene_I,database_I=database_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        # make the data parameters
        data1_keys = [
                    'gene',
                    'parent_classes',
                    'left',
                    'right',
                    'in_pathway',
                    'name'
                    ];
        data1_nestkeys = [
            'gene',
            'parent_classes',
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
                #svgtype='treelayout2d_01',
                svgtype='forcelayout2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='',
                svgy1axislabel='',
                tablekeymap = [data1_keymap],
                svgkeymap = [data1_keymap],
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=[0],
                svgfilters=None,
                svgtileheader='BioCyc Reaction',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I= {
                            #"svgtype":'treelayout2d_01',
                            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                            "svgwidth":500,
                            "svgheight":500,
                            "svgduration":750,
                            "datalastchild":'name',
                            'colclass':"col-sm-12"
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
        
        data_O = [];
        # get fpkm tracking data
        data_O = self.getJoin_genesAndNamesFeatures_geneAndDatabase_modelsBioCycProteinsAndProteinFeatures(
            gene_I,database_I=database_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        # make the data parameters
        data1_keys = [
                    'gene',
                    'protein_name',
                    'feature_of',
                    'parent_classes',
                    'protein_feature',
                    ];
        data1_nestkeys = [
            'gene',
            'feature_of',
            ];
        data1_keymap = {'xdata':'protein_feature',
                        'ydata':'gene',
                        'serieslabel':'',
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
                svgtileheader='BioCyc Protein Features',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I= {
                            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                            "svgwidth":500,
                            "svgheight":500,
                            "svgduration":750,
                            "datalastchild":'protein_feature',
                            'colclass':"col-sm-12"
                            }
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_geneEnzymaticReactions_js(self,gene_I,database_I='ECOLI',query_I={},data_dir_I='tmp'):
        '''Export force diagram
        INPUT:
        OUTPUT:
        '''
        
        data_O = [];
        # get data
        data_O = self.getJoin_enzymaticReactions_geneAndDatabase_modelsBioCycProteinAndPolymerSegmentAndEnzymaticReactions(
            gene_I,database_I=database_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        # make the data parameters
        data1_keys = [
                    'gene',
                    'enzyme',
                    'cofactors',
                    'regulated_by',
                    'name'
                    ];
        data1_nestkeys = [
            'gene',
            'enzyme',
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
                #svgtype='treelayout2d_01',
                svgtype='forcelayout2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='',
                svgy1axislabel='',
                tablekeymap = [data1_keymap],
                svgkeymap = [data1_keymap],
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=[0],
                svgfilters=None,
                svgtileheader='BioCyc Reaction',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I= {
                            #"svgtype":'treelayout2d_01',
                            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                            "svgwidth":500,
                            "svgheight":500,
                            "svgduration":750,
                            "datalastchild":'reaction',
                            'colclass':"col-sm-12"
                            }
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_GOTermGenes_js(self,go_term_I,database_I='ECOLI',query_I={},data_dir_I='tmp'):
        '''Export force diagram of GO Terms (MF only) to genes
        INPUT:
        OUTPUT:
        '''
        
        data_O = [];
        # get fpkm tracking data
        data_O = self.getParsed_genesAndNames_GOTermAndDatabase_modelsBioCycProteins(
            go_term_I,database_I=database_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        # make the data parameters
        data1_keys = [
                    'go_term',
                    'gene',
                    'protein_name',
                    'component_of'
                    ];
        data1_nestkeys = [
            'go_term',
            'gene',
            'protein_name',
            ];
        data1_keymap = {'xdata':'go_terms',
                        'ydata':'gene',
                        'serieslabel':'',
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
                svgtype='indentedtreelayout2d_01',
                #svgtype='treelayout2d_01',
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
                svgtileheader='BioCyc GO Mapping',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I= {
                            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                            "svgwidth":500,
                            "svgheight":500,
                            "svgduration":750,
                            "datalastchild":'component_of',
                            'colclass':"col-sm-12"
                            }
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_geneParentClasses_js(self,genes_I,database_I='ECOLI',query_I={},data_dir_I='tmp'):
        '''Export force diagram
        INPUT:
        OUTPUT:
        '''
        
        data_O = [];
        # get fpkm tracking data
        data_O = self.getParsed_nameAndProductAndParentClasses_namesAndDatabase_modelsBioCycPolymerSegments(
            genes_I,database_I=database_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        # make the data parameters
        data1_keys = [
                    'gene',
                    'product',
                    'parent_class',
                    ];
        data1_nestkeys = [
            'parent_class',
                    'gene',
            ];
        data1_keymap = {'xdata':'parent_class',
                        'ydata':'gene',
                        'serieslabel':'',
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
                svgtileheader='BioCyc Gene Parent Classes',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I= {
                            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                            "svgwidth":500,
                            "svgheight":500,
                            "svgduration":750,
                            "datalastchild":'product',
                            'colclass':"col-sm-12"
                            }
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_transcriptionUnitParentClassesHistogram_js(self,
        tus_I,database_I='ECOLI',query_I={},n_bins_I=[],single_plot_I=False,data_dir_I="tmp"):
        '''

        '''
        dependencies = models_BioCyc_dependencies();

        if single_plot_I:
            #get the table data
            data_table_O = [];
            data_query = self.getComplex_transcriptionUnitParentClasses(tus_I,database_I=database_I,query_I=query_I);
            data_table_O = dependencies.count_parentClasses(data_query);
            for d in data_table_O:
                d['transcription_unit']='all';
                d['parent_class'] = d['parent_class'].replace(',',";");
        else:
            #get the table data
            #get the table data and data as a dictionary for each feature
            data_table_O = [];
            data_dict_O = {};
            for tu in tus_I:
                data_query = self.getComplex_transcriptionUnitParentClasses([tu],database_I=database_I,query_I=query_I);
                data_count = dependencies.count_parentClasses(data_query);
                data_dict_O[tu]=[];
                for d in data_count:
                    d['transcription_unit']=tu;
                    d['parent_class'] = d['parent_class'].replace(',',";");
                    data_dict_O[tu].append(d);
                    data_table_O.append(d);

        # initialize the ddt objects
        dataobject_O = [];
        parametersobject_O = [];
        tile2datamap_O = {};
        
        # visualization parameters
        data1_keys = ['transcription_unit',
                      'parent_class',
                      ];
        data1_nestkeys = [
            #'parent_class'
            'transcription_unit'
            ];
        data1_keymap = {
                'xdata':'parent_class',
                'ydata':'frequency',
                #'serieslabel':'transcription_unit',
                'serieslabel':'parent_class',
                'featureslabel':'parent_class',
                'tooltiplabel':'parent_class',
                'ydatalb':None,
                'ydataub':None};

        # make the tile parameter objects
        # tile 0: form
        formtileparameters_O = {
            'tileheader':'Filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"};
        formparameters_O = {
            'htmlid':'filtermenuform1',
            'htmltype':'form_01',
            "formsubmitbuttonidtext":{'id':'submit1','text':'submit'},
            "formresetbuttonidtext":{'id':'reset1','text':'reset'},
            "formupdatebuttonidtext":{'id':'update1','text':'update'}
            };
        formtileparameters_O.update(formparameters_O);

        dataobject_O.append({"data":data_table_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(formtileparameters_O);
        tile2datamap_O.update({"filtermenu1":[0]});

        # tile 1-n features: count
        if not single_plot_I:
            rowcnt = 1;
            colcnt = 1;
            cnt = 0;
            for k,v in data_dict_O.items():
                svgtileid = "tilesvg"+str(cnt);
                svgid = 'svg'+str(cnt);
                iter=cnt+1; #start at 1
                if (cnt % 2 == 0): 
                    rowcnt = rowcnt+1;#even 
                    colcnt = 1;
                else:
                    colcnt = colcnt+1;
                # make the svg object
                svgparameters1_O = {
                    "svgtype":'verticalbarschart2d_01',
                    "svgkeymap":[data1_keymap],
                    'svgid':'svg'+str(cnt),
                    "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "svgwidth":350,
                    "svgheight":250,
                    "svgy1axislabel":"frequency"            
                        };
                svgtileparameters1_O = {
                    'tileheader':'Histogram',
                    'tiletype':'svg',
                    'tileid':svgtileid,
                    'rowid':"row"+str(rowcnt),
                    'colid':"col"+str(colcnt),
                    'tileclass':"panel panel-default",
                    'rowclass':"row",
                    'colclass':"col-sm-6"};
                dataobject_O.append({"data":v,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
                svgtileparameters1_O.update(svgparameters1_O);
                parametersobject_O.append(svgtileparameters1_O);
                tile2datamap_O.update({svgtileid:[iter]});
                cnt+=1;
        else:
            cnt = 0;
            svgtileid = "tilesvg"+str(cnt);
            svgid = 'svg'+str(cnt);
            rowcnt = 2;
            colcnt = 1;
            # make the svg object
            svgparameters1_O = {
                "svgtype":'verticalpieschart2d_01',
                #"svgtype":'verticalbarschart2d_01',
                "svgkeymap":[data1_keymap],
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":350,
                "svgheight":250,
                "svgy1axislabel":"frequency"            
                    };
            svgtileparameters1_O = {
                'tileheader':'Histogram',
                'tiletype':'svg',
                'tileid':svgtileid,
                'rowid':"row"+str(rowcnt),
                'colid':"col"+str(colcnt),
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-6"};
            svgtileparameters1_O.update(svgparameters1_O);
            parametersobject_O.append(svgtileparameters1_O);
            tile2datamap_O.update({svgtileid:[0]});
            
        # make the table object
        tableparameters1_O = {
            "tabletype":'responsivetable_01',
            'tableid':'table1',
            "tablefilters":None,
            "tableclass":"table  table-condensed table-hover",
    		'tableformtileid':'tile1',
            };
        tabletileparameters1_O = {
            'tileheader':'Histogram',
            'tiletype':'table',
            'tileid':"tabletile1",
            'rowid':"row"+str(rowcnt+1),
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"
            };
        tabletileparameters1_O.update(tableparameters1_O);

        parametersobject_O.append(tabletileparameters1_O);
        tile2datamap_O.update({"tabletile1":[0]})

        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
            
    def export_geneAndMetaboliteRegulatedEntities_sankeyDiagram_js(self,
                genes_I,metabolites_I,database_I='ECOLI',
                query_I={},
                data_dir_I='tmp'
                ):
        '''export a binary sankey diagram
        INPUT:

        query_I = {} of additional SQL query operators
        data_dir_I
        OUTPUT:
        '''

        #get the data
        data_O = [];
        for gene in genes_I:
            data_tmp = self.getJoin_regulatedEntities_geneAndDatabase_modelsBioCycProteinAndRegulationAndPolymerSegment(
                gene,database_I=database_I,
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);
            data_O.extend(data_tmp);
        for met in metabolites_I:
            data_tmp = self.getParsed_geneAndRows_metaboliteAndDatabase_modelsBioCycRegulation(
                met,database_I=database_I,
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);
            data_O.extend(data_tmp);

        #group regulators and regulated TUs
        regulator_tu = [];
        regulator = {};
        transcription_unit = {};
        parent_classes = {};
        regulator_cnt=1
        transcription_unit_cnt=1
        parent_classes_cnt=1
        for d in data_O:
            reg_tu_dict = {};
            reg_tu_dict['gene'] = d['gene']
            # convert regulator to float
            if not d['regulator'] in regulator.keys():
                regulator[d['regulator']] = regulator_cnt;
                regulator_cnt+=1;
            reg_tu_dict['regulator'] = d['regulator']
            reg_tu_dict['regulator_'] = regulator[d['regulator']];
            # convert transcription unit to float
            if not d['transcription_unit'] in transcription_unit.keys():
                transcription_unit[d['transcription_unit']] = transcription_unit_cnt;
                transcription_unit_cnt+=1;
            reg_tu_dict['transcription_unit'] = d['transcription_unit']
            reg_tu_dict['transcription_unit_'] = transcription_unit[d['transcription_unit']];
            # convert mode to float
            if d['mode'] == '+': mode = 1
            elif d['mode'] == '-': mode = 2
            #if d['mode'] == '+': mode = 1
            #elif d['mode'] == '-': mode = -1
            reg_tu_dict['mode'] = d['mode'];
            reg_tu_dict['mode_'] = mode;
            # convert parent class to float
            if not d['parent_classes'] in parent_classes.keys():
                parent_classes[d['parent_classes']] = parent_classes_cnt;
                parent_classes_cnt+=1;
            reg_tu_dict['parent_classes'] = d['parent_classes'];
            reg_tu_dict['parent_classes_'] = parent_classes[d['parent_classes']];
            # make interaction float
            interaction = parent_classes[d['parent_classes']]*mode;
            reg_tu_dict['interaction'] = interaction;
            if not reg_tu_dict in regulator_tu:
                regulator_tu.append(reg_tu_dict);

        #data1 = filter menu and table
        data1_keys = [
                    'gene',
                    'regulator',
                    'transcription_unit',
                    'parent_classes',
                    'mode',
                    ];
        data1_nestkeys = [
                    'regulator',
                    #'transcription_unit',
            #'regulator',
            #'transcription_unit',
            #'parent_classes',
            #'mode',
            ];
        data1_keymap = {
            'xdata':'',
            'ydata':'',
            'zdata':'',
            'rowslabel':'',
            'columnslabel':'',
            'tooltipdata':'',};
         
        #data2 = svg
        #if single plot, data2 = filter menu, data2, and table
        data2_keys = [
                    'regulator',
                    'transcription_unit',
                    ];
        data2_nestkeys = [
            'regulator',];
        data2_keymap = {
            'xdata':'mode_',
            'ydata':'mode_',
            #'xdata':'regulator_',
            #'ydata':'transcription_unit_',
            'xdatalabel':'regulator',
            'ydatalabel':'regulator',
            'serieslabel':'regulator',
            'featureslabel':'transcription_unit',
            #'tooltiplabel':'component_name',
            };

        svgparameters = {
            'svgradius':250,
            'svgouterradius':200,
            'svginnerradius':190,
            "svgwidth":150,
            "svgheight":500,
            "datalastchild":'transcription_unit',
            'svgcolorcategory':'blue2red64',
            'svgcolordomain':'min,max',
			'svgcolordatalabel':'mode_',
            'svgcolorscale':'quantile',
            };
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
            data_filtermenu=regulator_tu,
            data_filtermenu_keys=data1_keys,
            data_filtermenu_nestkeys=data1_nestkeys,
            data_filtermenu_keymap=data1_keymap,
            data_svg_keys=None,
            data_svg_nestkeys=None,
            data_svg_keymap=data2_keymap,
            data_table_keys=None,
            data_table_nestkeys=None,
            data_table_keymap=None,
            data_svg=None,
            data_table=None,
            svgtype='sankeydiagram2d_01',
            #svgtype='bundlediagram2d_01',
            #svgtype='chorddiagram2d_01',
            tabletype='responsivetable_01',
            svgx1axislabel='',
            svgy1axislabel='',
            tablekeymap = [data1_keymap],
            svgkeymap = [data2_keymap],
            formtile2datamap=[0],
            tabletile2datamap=[0],
            svgtile2datamap=[0], #calculated on the fly
            svgfilters=None,
            svgtileheader='chord diagram',
            svgparameters_I=svgparameters,
            tablefilters=None,
            tableheaders=None
            );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_geneRegulators_sankeyDiagram_js(self,
                genes_I,database_I='ECOLI',
                query_I={},
                data_dir_I='tmp'
                ):
        '''export a binary sankey diagram
        INPUT:

        query_I = {} of additional SQL query operators
        data_dir_I
        OUTPUT:
        '''

        #get the data
        data_O = [];
        for gene in genes_I:
            data_tmp = self.getJoin_regulators_geneAndDatabase_modelsBioCycProteinAndRegulationAndPolymerSegment(
                gene,database_I=database_I,
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);
            data_O.extend(data_tmp);

        #group regulators and regulated TUs
        regulator_tu = [];
        regulator = {};
        transcription_unit = {};
        parent_classes = {};
        regulator_cnt=1
        transcription_unit_cnt=1
        parent_classes_cnt=1
        for d in data_O:
            reg_tu_dict = {};
            reg_tu_dict['gene'] = d['gene']
            # convert regulator to float
            if not d['regulator'] in regulator.keys():
                regulator[d['regulator']] = regulator_cnt;
                regulator_cnt+=1;
            reg_tu_dict['regulator'] = d['regulator']
            reg_tu_dict['regulator_'] = regulator[d['regulator']];
            # convert transcription unit to float
            if not d['transcription_unit'] in transcription_unit.keys():
                transcription_unit[d['transcription_unit']] = transcription_unit_cnt;
                transcription_unit_cnt+=1;
            reg_tu_dict['transcription_unit'] = d['transcription_unit']
            reg_tu_dict['transcription_unit_'] = transcription_unit[d['transcription_unit']];
            # convert mode to float
            if d['mode'] == '+': mode = 1
            elif d['mode'] == '-': mode = 2
            #if d['mode'] == '+': mode = 1
            #elif d['mode'] == '-': mode = -1
            reg_tu_dict['mode'] = d['mode'];
            reg_tu_dict['mode_'] = mode;
            # convert parent class to float
            if not d['parent_classes'] in parent_classes.keys():
                parent_classes[d['parent_classes']] = parent_classes_cnt;
                parent_classes_cnt+=1;
            reg_tu_dict['parent_classes'] = d['parent_classes'];
            reg_tu_dict['parent_classes_'] = parent_classes[d['parent_classes']];
            # make interaction float
            interaction = parent_classes[d['parent_classes']]*mode;
            reg_tu_dict['interaction'] = interaction;
            if not reg_tu_dict in regulator_tu:
                regulator_tu.append(reg_tu_dict);

        #data1 = filter menu and table
        data1_keys = [
                    'gene',
                    'regulator',
                    'transcription_unit',
                    'parent_classes',
                    'mode',
                    ];
        data1_nestkeys = [
                    'parent_classes',
                    'regulator',
                    'transcription_unit',
            ];
        data1_keymap = {
            'xdata':'',
            'ydata':'',
            'zdata':'',
            'rowslabel':'',
            'columnslabel':'',
            'tooltipdata':'',};
         
        #data2 = svg
        #if single plot, data2 = filter menu, data2, and table
        data2_keys = [
                    'regulator',
                    'transcription_unit',
                    ];
        data2_nestkeys = [
            'regulator',];
        data2_keymap = {
            'xdata':'mode_',
            'ydata':'mode_',
            #'xdata':'regulator_',
            #'ydata':'transcription_unit_',
            'xdatalabel':'regulator',
            'ydatalabel':'regulator',
            'serieslabel':'regulator',
            'featureslabel':'transcription_unit',
            #'tooltiplabel':'component_name',
            };

        svgparameters = {
            'svgradius':250,
            'svgouterradius':200,
            'svginnerradius':190,
            "svgwidth":300,#150,
            "svgheight":500,
            #"datalastchild":'transcription_unit',
            'svgcolorcategory':'blue2red64',
            'svgcolordomain':'min,max',
			'svgcolordatalabel':'mode_',
            'svgcolorscale':'quantile',
            };
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
            data_filtermenu=regulator_tu,
            data_filtermenu_keys=data1_keys,
            data_filtermenu_nestkeys=data1_nestkeys,
            data_filtermenu_keymap=data1_keymap,
            data_svg_keys=None,
            data_svg_nestkeys=None,
            data_svg_keymap=data2_keymap,
            data_table_keys=None,
            data_table_nestkeys=None,
            data_table_keymap=None,
            data_svg=None,
            data_table=None,
            #svgtype='forcedirectedgraph2d_01',
            svgtype='sankeydiagram2d_01',
            #svgtype='bundlediagram2d_01',
            #svgtype='chorddiagram2d_01',
            tabletype='responsivetable_01',
            svgx1axislabel='',
            svgy1axislabel='',
            tablekeymap = [data1_keymap],
            svgkeymap = [data2_keymap],
            formtile2datamap=[0],
            tabletile2datamap=[0],
            svgtile2datamap=[0], #calculated on the fly
            svgfilters=None,
            svgtileheader='chord diagram',
            svgparameters_I=svgparameters,
            tablefilters=None,
            tableheaders=None
            );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_geneReactions_forceDirectedGraph_js(self,genes_I,database_I='ECOLI',query_I={},data_dir_I='tmp'):
        '''Export force diagram
        INPUT:
        OUTPUT:
        '''
        
        dependencies = models_BioCyc_dependencies();

        data_O = [];
        # get data
        for gene in genes_I:
            data_tmp = self.getJoin_reactions_geneAndDatabase_modelsBioCycProteinAndPolymerSegmentAndReaction(
                gene,database_I=database_I,
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);
            data_O.extend(data_tmp);

        # break into individual reactions
        data_reactions = [];
        for d in data_O:
            d['flux']=1;
            left = dependencies.convert_bioCycList2List(d['left']);
            right = dependencies.convert_bioCycList2List(d['right']);
            reaction = d['gene'];
            for l in left:
                tmp = copy.copy(d);
                tmp['left'] = l;
                tmp['right'] = reaction;
                data_reactions.append(tmp);
            for r in right:
                tmp = copy.copy(d);
                tmp['left'] = reaction;
                tmp['right'] = r;
                data_reactions.append(tmp);

        # make the data parameters
        data1_keys = [
                    'gene',
                    'parent_classes',
                    'left',
                    'right',
                    'in_pathway',
                    'name'
                    ];
        data1_nestkeys = [
            'left',
            #'name',
            'right',
                          ];
        data1_keymap = {'xdata':'parent_classes',
                        'ydata':'mode',
                        'serieslabel':'mode',
                        'featureslabel':''};

        data2_keymap = {
            'xdata':'parent_classes',
            'ydata':'flux',
            'xdatalabel':'parent_classes',
            'ydatalabel':'name',
            'serieslabel':'regulator',
            'featureslabel':'transcription_unit',
            #'tooltiplabel':'component_name',
            };

        svgparameters = {
            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
            "svgwidth":500,
            "svgheight":500,
            "svgduration":750,
            'colclass':"col-sm-12",
            'svgcolorcategory':'blue2red64',
            'svgcolordomain':'min,max',
			'svgcolordatalabel':'parent_classes',
            'svgcolorscale':'quantile',
            };
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
            data_filtermenu=data_reactions,
            data_filtermenu_keys=data1_keys,
            data_filtermenu_nestkeys=data1_nestkeys,
            data_filtermenu_keymap=data1_keymap,
            data_svg_keys=None,
            data_svg_nestkeys=None,
            data_svg_keymap=data2_keymap,
            data_table_keys=None,
            data_table_nestkeys=None,
            data_table_keymap=None,
            data_svg=None,
            data_table=None,
            #svgtype='sankeydiagram2d_01',
            svgtype='forcedirectedgraph2d_01',
            tabletype='responsivetable_01',
            svgx1axislabel='',
            svgy1axislabel='',
            tablekeymap = [data1_keymap],
            svgkeymap = [data2_keymap],
            formtile2datamap=[0],
            tabletile2datamap=[0],
            svgtile2datamap=[0],
            svgfilters=None,
            svgtileheader='BioCyc Reaction',
            tablefilters=None,
            tableheaders=None,
            svgparameters_I= svgparameters,
            );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_geneReactionsAndEnzymaticReactions_forceDirectedGraph_js(self,genes_I,database_I='ECOLI',query_I={},data_dir_I='tmp'):
        '''Export force diagram
        INPUT:
        OUTPUT:
        '''
        
        dependencies = models_BioCyc_dependencies();

        data1_O = [];
        data2_O = [];
        # get data
        for gene in genes_I:
            data_tmp = self.getJoin_enzymaticReactions_geneAndDatabase_modelsBioCycProteinAndPolymerSegmentAndEnzymaticReactionsAndRegulation(
                gene,database_I=database_I,
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);
            data1_O.extend(data_tmp);
            data_tmp = self.getJoin_reactions_geneAndDatabase_modelsBioCycProteinAndPolymerSegmentAndReaction(
                gene,database_I=database_I,
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);
            data2_O.extend(data_tmp);

        # break into individual reactions
        data_reactions = [];
        for d in data1_O:
            d['flux']=1;
            #d['mode_']={'+':2,'-':3,'':1}[d['mode']];
            d['marker']=1;
            reaction = d['name'];
            rxn_lst = dependencies.convert_bioCycList2List(d['reaction']);
            cofactors = dependencies.convert_bioCycList2List(d['cofactors']);
            if len(rxn_lst)>1: print('more than one reaction found');
            for rxn in rxn_lst:
                left,right = dependencies.convert_bioCycRxn2LeftAndRight(rxn);
                # correct left/right based on reaction direction
                if not 'LEFT-TO-RIGHT' in d['reaction_direction']:
                    right,left=left,right;
                for l in left:
                    tmp = copy.copy(d);
                    tmp['left'] = l;
                    tmp['right'] = reaction;
                    tmp['mode']='none'
                    data_reactions.append(tmp);
                for r in right:
                    tmp = copy.copy(d);
                    tmp['left'] = reaction;
                    tmp['right'] = r;
                    tmp['mode']='none'
                    data_reactions.append(tmp);  
                # add in pseudo reaction for regulators              
                if d['regulator']:
                    tmp = copy.copy(d);
                    tmp['left'] = d['regulator'];
                    tmp['right'] = reaction;
                    data_reactions.append(tmp);
                # add in pseudo reaction and mode for cofactors
                for cofactor in cofactors:
                    tmp = copy.copy(d);
                    tmp['left'] = cofactor;
                    tmp['right'] = reaction;
                    tmp['mode'] = 'cofactor';
                    data_reactions.append(tmp);
        for d in data2_O:
            d['flux']=1;
            d['marker']=1;
            left = dependencies.convert_bioCycList2List(d['left']);
            right = dependencies.convert_bioCycList2List(d['right']);
            reaction = d['gene'];
            d['reaction'] = d['name'];
            d['name'] = d['frame_id'];
            d['enzyme'] = d['ec_number'];
            for l in left:
                tmp = copy.copy(d);
                tmp['left'] = l;
                tmp['right'] = reaction;
                tmp['mode']='none'
                data_reactions.append(tmp);
            for r in right:
                tmp = copy.copy(d);
                tmp['left'] = reaction;
                tmp['right'] = r;
                tmp['mode']='none'
                data_reactions.append(tmp);

        # make the data parameters
        data1_keys = [
                    'gene',
                    'parent_classes',
                    'left',
                    'right',
                    'enzyme',
                    'name',
                    'mode'
                    ];
        data1_nestkeys = [
            'left',
            #'name',
            'right',
                          ];
        data1_keymap = {'xdata':'parent_classes',
                        'ydata':'mode',
                        'serieslabel':'mode',
                        'featureslabel':''};

        data2_keymap = {
            'xdata':'parent_classes',
            'ydata':'flux',
            'zdata':'marker',
            'xdatalabel':'parent_classes',
            'ydatalabel':'mode',
            'zdatalabel':'marker',
            'serieslabel':'regulator',
            'featureslabel':'transcription_unit',
            #'tooltiplabel':'component_name',
            };

        svgparameters = {
            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
            "svgwidth":500,
            "svgheight":500,
            "svgduration":750,
            'colclass':"col-sm-12",
   #         'svgcolorcategory':'blue2red64',
   #         'svgcolordomain':'min,max',
   #		 'svgcolordatalabel':'parent_classes',
   #         'svgcolorscale':'quantile',
            };
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
            data_filtermenu=data_reactions,
            data_filtermenu_keys=data1_keys,
            data_filtermenu_nestkeys=data1_nestkeys,
            data_filtermenu_keymap=data1_keymap,
            data_svg_keys=None,
            data_svg_nestkeys=None,
            data_svg_keymap=data2_keymap,
            data_table_keys=None,
            data_table_nestkeys=None,
            data_table_keymap=None,
            data_svg=None,
            data_table=None,
            #svgtype='sankeydiagram2d_01',
            svgtype='forcedirectedgraph2d_01',
            tabletype='responsivetable_01',
            svgx1axislabel='',
            svgy1axislabel='',
            tablekeymap = [data1_keymap],
            svgkeymap = [data2_keymap],
            formtile2datamap=[0],
            tabletile2datamap=[0],
            svgtile2datamap=[0],
            svgfilters=None,
            svgtileheader='BioCyc Reaction',
            tablefilters=None,
            tableheaders=None,
            svgparameters_I= svgparameters,
            );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());