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
            'left',
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
                svgtileheader='BioCyc Reaction',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I= {
                            #"svgtype":'treelayout2d_01',
                            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                            "svgwidth":500,
                            "svgheight":500,
                            "svgduration":750,
                            "datalastchild":'right',
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