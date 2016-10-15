from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete
from SBaaS_base.sbaas_template_query import sbaas_template_query
from .models_BioCyc_postgresql_models import *
from .models_BioCyc_dependencies import models_BioCyc_dependencies
#resources
import copy
class models_BioCyc_query(sbaas_template_query):
    def initialize_supportedTables(self):
        tables_supported = {
        'models_biocyc_regulation':models_biocyc_regulation,
        'models_biocyc_publications':models_biocyc_publications,
        'models_biocyc_enzymaticReactions':models_biocyc_enzymaticReactions,
        'models_biocyc_proteinFeatures':models_biocyc_proteinFeatures,
        'models_biocyc_pathways':models_biocyc_pathways,
        'models_biocyc_proteins':models_biocyc_proteins,
        'models_biocyc_reactions':models_biocyc_reactions,
        'models_biocyc_polymerSegments':models_biocyc_polymerSegments,
        'models_biocyc_compounds':models_biocyc_compounds,
        'models_biocyc_RNAs':models_biocyc_RNAs,
        }
        self.set_supportedTables(tables_supported)

    
    #models_biocyc_pathways
    def get_rows_superPathwayAndDatabase_modelsBioCycPathways(
        self,super_pathway_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_pathways
        WHERE super_pathway LIKE '''
        
        tables = ['models_biocyc_pathways']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        super_pathway_where = '("%s")' %(super_pathway_I)

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'super_pathways',
            'value':super_pathway_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'genes_of_pathway',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_nameAndDatabase_modelsBioCycPathways(
        self,name_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_pathways
        WHERE super_pathway LIKE '''
        
        tables = ['models_biocyc_pathways']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'genes_of_pathway',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_namesAndDatabase_modelsBioCycPathways(
        self,names_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_pathways
        WHERE super_pathway LIKE '''
        
        tables = ['models_biocyc_pathways']
        
        names_str = self.convert_list2string(names_I);
        names = "('{%s}'::text[])" %names_str;

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':names,
            'operator':'=ANY',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'genes_of_pathway',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;

    #models_biocyc_proteins
    def get_genesAndNamesAndComponentOfs_GOTermAndDatabase_modelsBioCycProteins(
        self,go_term_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT gene,regulates,name FROM models_biocyc_proteins
        WHERE gene LIKE '''
        
        tables = ['models_biocyc_proteins']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'gene'},
            {"table_name":tables[0],'column_name':'name'},
            {"table_name":tables[0],'column_name':'component_of'},
            {"table_name":tables[0],'column_name':'go_terms'},
            ];

        go_term_where = "%s%s%s" %('%',go_term_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'go_terms',
            'value':go_term_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'gene',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_geneAndRegulatesAndName_geneAndDatabase_modelsBioCycProteins(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT gene,regulates,name FROM models_biocyc_proteins
        WHERE gene LIKE '''
        
        tables = ['models_biocyc_proteins']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'gene'},
            {"table_name":tables[0],'column_name':'regulates'},
            {"table_name":tables[0],'column_name':'name'},
            ];

        gene_where = "%s%s%s" %('%',gene_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'gene',
            'value':gene_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            #{"table_name":tables[0],
            #'column_name':'analysis_id',
            #'value':analysis_ids_query,
            #'operator':'=ANY',
            #'connector':'AND'
            #    },
            #{"table_name":tables[0],
            #'column_name':'gene_short_name',
            #'value':gene_short_names_query,
            #'operator':'=ANY',
            #'connector':'AND'
            #    },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'gene',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulates',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_geneAndRegulatesAndNameAndComponentOf_geneAndDatabase_modelsBioCycProteins(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT gene,regulates,name,component_of FROM models_biocyc_proteins
        WHERE gene LIKE '''
        
        tables = ['models_biocyc_proteins']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'component_of'},
            ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_geneAndRegulatesAndName_geneAndDatabase_modelsBioCycProteins(
            gene_I=gene_I,
            database_I=database_I,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_geneAndDatabase_modelsBioCycProteins(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_proteins
        WHERE gene LIKE '''
        
        tables = ['models_biocyc_proteins']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        #gene_short_names_str = ','.join(gene_short_names_I);
        #gene_short_names_query = ("('{%s}'::text[])" %(gene_short_names_str))
        #analysis_ids_str = ','.join(analysis_ids_I);
        #analysis_ids_query = ("('{%s}'::text[])" %(analysis_ids_str))
        gene_where = "%s%s%s" %('%',gene_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'gene',
            'value':gene_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'gene',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def getGroup_geneAndDatabase_modelsBioCycProteins(
        self,
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT gene,database
        FROM models_biocyc_proteins
        GROUP BY gene,database
        ORDER BY database ASC, gene ASC
        '''
        
        tables = ['models_biocyc_proteins']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'gene'},
            {"table_name":tables[0],'column_name':'database'},
            ];

        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'database',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'gene',
            'order':'ASC',
            },
        ];
        query['group_by'] = [
            {"table_name":tables[0],
            'column_name':'database',
            },
            {"table_name":tables[0],
            'column_name':'gene',
            },
        ]

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_nameAndDatabase_modelsBioCycProteins(
        self,name_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_proteins
        WHERE gene LIKE '''
        
        tables = ['models_biocyc_proteins']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;

    #models_biocyc_regulation
    def get_rows_databaseAndNotNull_modelsBioCycRegulation(
        self,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT *
        FROM models_biocyc_regulation
        WHERE LIKE '''
        
        tables = ['models_biocyc_regulation']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            #{"table_name":tables[0],
            #'column_name':'regulated_entity ',
            #'value':'',
            #'operator':'!=',
            #'connector':'AND'
            #    },
            #{"table_name":tables[0],
            #'column_name':'regulator  ',
            #'value':'',
            #'operator':'!=',
            #'connector':'AND'
            #    },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'mode',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulator',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulated_entity',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_regulatedEntityAndRegulatorAndModeAndParentClasses_geneAndDatabase_modelsBioCycRegulation(
        self,name_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT regulated_entity,mode,parent_classes,regulator
        FROM models_biocyc_regulation
        WHERE LIKE '''
        
        tables = ['models_biocyc_regulation']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'regulated_entity'},
            {"table_name":tables[0],'column_name':'mode'},
            {"table_name":tables[0],'column_name':'parent_classes'},
            {"table_name":tables[0],'column_name':'regulator'},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'mode',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulator',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulated_entity',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_nameAndDatabase_modelsBioCycRegulation(
        self,name_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT regulated_entity,mode,parent_classes,regulator
        FROM models_biocyc_regulation
        WHERE LIKE '''
        
        tables = ['models_biocyc_regulation']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'mode',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulator',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulated_entity',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatedEntityAndDatabase_modelsBioCycRegulation(
        self,regulatedEntity_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT regulated_entity,mode,parent_classes,regulator
        FROM models_biocyc_regulation
        WHERE regulated_entity LIKE '''
        
        tables = ['models_biocyc_regulation']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'regulated_entity'},
            {"table_name":tables[0],'column_name':'mode'},
            {"table_name":tables[0],'column_name':'parent_classes'},
            {"table_name":tables[0],'column_name':'regulator'},
            ];

        #regulatedEntity_where = "%s%s%s" %('%',regulatedEntity_I,'%')
        regulatedEntity_where = regulatedEntity_I

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'regulated_entity',
            'value':regulatedEntity_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'mode',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulator',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulated_entity',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_regulatedEntityAndDatabase_modelsBioCycRegulation(
        self,regulatedEntity_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT regulated_entity,mode,parent_classes,regulator
        FROM models_biocyc_regulation
        WHERE regulated_entity LIKE '''
        
        tables = ['models_biocyc_regulation']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        #regulatedEntity_where = "%s%s%s" %('%',regulatedEntity_I,'%')
        regulatedEntity_where = regulatedEntity_I

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'regulated_entity',
            'value':regulatedEntity_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'mode',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulator',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulated_entity',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatorAndDatabase_modelsBioCycRegulation(
        self,regulator_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT regulated_entity,mode,parent_classes,regulator 
        FROM models_biocyc_regulation
        WHERE regulator LIKE '''
        tables = ['models_biocyc_regulation']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'regulated_entity'},
            {"table_name":tables[0],'column_name':'mode'},
            {"table_name":tables[0],'column_name':'parent_classes'},
            {"table_name":tables[0],'column_name':'regulator'},
            ];

        regulator_where = "%s%s%s" %('%',regulator_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'regulator',
            'value':regulator_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'mode',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulator',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulated_entity',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_regulatorAndDatabase_modelsBioCycRegulation(
        self,regulator_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT regulated_entity,mode,parent_classes,regulator 
        FROM models_biocyc_regulation
        WHERE regulator LIKE '''
        tables = ['models_biocyc_regulation']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        regulator_where = "%s%s%s" %('%',regulator_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'regulator',
            'value':regulator_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'mode',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulator',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'regulated_entity',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;

    #models_biocyc_polymerSegments
    def get_nameAndProductsAndParentClasses_nameAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
        self,
        name_I,
        parentClasses_I = '("Transcription-Units")',
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT name FROM models_biocyc_polymerSegments
        WHERE name LIKE [] AND parent_classes NOT LIKE []'''
        
        tables = ['models_biocyc_polymerSegments']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'name'},
            {"table_name":tables[0],'column_name':'product'},
            {"table_name":tables[0],'column_name':'parent_classes'},
            ];

        name_where = '%s' %(name_I)

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'value':parentClasses_I,
            'operator':'NOT LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_nameAndComponents_componentsAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
        self,
        components_I,
        parentClasses_I = '("Transcription-Units")',
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT name FROM models_biocyc_polymerSegments
        WHERE components LIKE '''
        
        tables = ['models_biocyc_polymerSegments']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'name'},
            {"table_name":tables[0],'column_name':'components'},
            {"table_name":tables[0],'column_name':'regulated_by'},
            ];

        components_where = '%s"%s"%s' %('%',components_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'components',
            'value':components_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'value':parentClasses_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'components',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_nameAndComponentsAndRegulatedBy_componentsAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
        self,
        components_I,
        parentClasses_I = '("Transcription-Units")',
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT name,components,regulated_by FROM models_biocyc_polymerSegments
        WHERE components LIKE '''
        
        tables = ['models_biocyc_polymerSegments']

        # add in extra query block
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'regulated_by'},
            ];
        
        data_O = self.get_nameAndComponents_componentsAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
            components_I,
            parentClasses_I = '("Transcription-Units")',
            database_I=database_I,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_nameAndProductAndParentClasses_namesAndDatabase_modelsBioCycPolymerSegments(
        self,
        names_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT name,product,parent_classes FROM models_biocyc_polymerSegments
        WHERE name =ANY ('{...}'::text[]) '''
        
        tables = ['models_biocyc_polymerSegments']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'name'},
            {"table_name":tables[0],'column_name':'product'},
            {"table_name":tables[0],'column_name':'parent_classes'},
            ];
        
        names_str = ','.join(names_I);
        names_query = ("('{%s}'::text[])" %(names_str))

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':names_query,
            'operator':'=ANY',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'product',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_nameAndAccession1_database_modelsBioCycPolymerSegments(
        self,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT name,accession_1 FROM models_biocyc_polymerSegments
        WHERE name =ANY ('{...}'::text[]) '''
        
        tables = ['models_biocyc_polymerSegments']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'name'},
            {"table_name":tables[0],'column_name':'accession_1'},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'accession_1',
            'value':'',
            'operator':'!=',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['group_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            },
            {"table_name":tables[0],
            'column_name':'accession_1',
            },
        ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'accession_1',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_nameAndDatabase_modelsBioCycPolymerSegments(
        self,
        name_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_polymerSegments
        WHERE name LIKE '''
        
        tables = ['models_biocyc_polymerSegments']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_namesAndDatabase_modelsBioCycPolymerSegments(
        self,
        names_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_polymerSegments
        WHERE name LIKE '''
        
        tables = ['models_biocyc_polymerSegments']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];
        
        names_str = self.convert_list2string(names_I);
        names = "('{%s}'::text[])" %names_str;

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':names,
            'operator':'=ANY',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_componentsAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
        self,
        components_I,
        parentClasses_I = '("Transcription-Units")',
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT name FROM models_biocyc_polymerSegments
        WHERE components LIKE '''
        
        tables = ['models_biocyc_polymerSegments']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        components_where = '%s"%s"%s' %('%',components_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'components',
            'value':components_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'value':parentClasses_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'components',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;

    #models_biocyc_proteinFeatures
    def get_rows_featureOfAndDatabase_modelsBioCycProteinFeatures(
        self,featureOf_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_proteinFeatures
        WHERE feature_of LIKE '''
        
        tables = ['models_biocyc_proteinFeatures']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        featureOf_where = "%s%s%s" %('%',featureOf_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'feature_of',
            'value':featureOf_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'feature_of',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_nameAndFeatureOfAndDatabase_modelsBioCycProteinFeatures(
        self,name_I,featureOf_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_proteinFeatures
        WHERE name LIKE '''
        
        tables = ['models_biocyc_proteinFeatures']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        name_where = "%s" %(name_I)
        featureOf_where = "%s%s%s" %('%',featureOf_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'feature_of',
            'value':featureOf_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'feature_of',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    
    #models_biocyc_reactions
    def get_rows_leftAndDatabase_modelsBioCycReactions(
        self,left_I,quote_left_I=False,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_reactions
        WHERE left LIKE AND parent_classes LIKE 
        
        INPUT:
        left_I,
        quote_I = if True, encapsulate left_I in ""
        database_I
        ...
        '''
        
        tables = ['models_biocyc_reactions']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];
        
        if quote_left_I:
            left_where = "%s%s%s" %('%"',left_I,'"%')
        else:
            left_where = "%s%s%s" %('%',left_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'left',
            'value':left_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_leftAndParentClassesAndDatabase_modelsBioCycReactions(
        self,left_I,
        parentClasses_I = '("Protein-Ligand-Binding-Reactions")',
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_reactions
        WHERE left LIKE AND parent_classes LIKE '''
        
        tables = ['models_biocyc_reactions']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];
        
        left_where = "%s%s%s" %('%"',left_I,'"%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'left',
            'value':left_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'parent_classes',
            'value':parentClasses_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_commonNamesAndDatabase_modelsBioCycReactions(
        self,common_names_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_reactions
        WHERE common_name =ANY 
        
        INPUT:
        common_names_I = string or list
        database_I
        ...
        '''
        
        tables = ['models_biocyc_reactions']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];
        
        common_names_str = ','.join(common_names_I);
        common_names = "('{%s}::text[])" %(common_names_str);

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'common_name',
            'value':common_names,
            'operator':'=ANY',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'common_name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_commonNameAndDatabase_modelsBioCycReactions(
        self,common_name_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_reactions
        WHERE common_name LIKE 
        
        INPUT:
        common_name_I = string
        database_I
        ...
        '''
        
        tables = ['models_biocyc_reactions']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'common_name',
            'value':common_name_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'common_name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_enzymaticReactionAndDatabase_modelsBioCycReactions(
        self,enzymatic_reaction_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_reactions
        WHERE common_name LIKE 
        
        INPUT:
        enzymatic_reaction_I = string
        database_I
        ...
        '''
        
        tables = ['models_biocyc_reactions']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        enzymatic_reaction_where = '%s"%s"%s'%('%',enzymatic_reaction_I,'%')

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'enzymatic_reaction',
            'value':enzymatic_reaction_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'common_name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    
    #models_biocyc_enzymaticReactions
    def get_rows_enzymeAndDatabase_modelsBioCycEnzymaticReactions(
        self,enzyme_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_enzymaticReactions
        WHERE enzyme LIKE '''
        
        tables = ['models_biocyc_enzymaticReactions']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];
        
        enzyme_where = "%s" %(enzyme_I);

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'enzyme',
            'value':enzyme_where,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def get_rows_nameAndDatabase_modelsBioCycEnzymaticReactions(
        self,name_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_enzymaticReactions
        WHERE enzyme LIKE '''
        
        tables = ['models_biocyc_enzymaticReactions']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;

    #models_biocyc_compounds
    def get_rows_nameAndDatabase_modelsBioCycCompounds(
        self,name_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_compounds
        WHERE name LIKE %s AND database LIKE %s
        '''
        
        tables = ['models_biocyc_compounds']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;

    #models_biocyc_RNAs
    def get_rows_nameAndDatabase_modelsBioCycRNAs(
        self,name_I,
        database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_RNAs
        WHERE name LIKE %s AND database LIKE %s
        '''
        
        tables = ['models_biocyc_RNAs']

        # make the query
        query = {};
        query['select'] = [
            {"table_name":tables[0]},
            ];

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'value':name_I,
            'operator':'LIKE',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':'database',
            'value':database_I,
            'operator':'LIKE',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k] = [];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;

    #Joins
    def getJoin_regulators_geneAndDatabase_modelsBioCycProteinAndRegulationAndPolymerSegment(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''
        SELECT models_biocyc_regulation.*,models_biocyc_polymerSegment.name AS transcription_unit,
         models_biocyc_protein.gene, models_biocyc_protein.regulates, models_biocyc_protein.name AS protein_name
         FROM models_biocyc_protein,models_biocyc_regulation,models_biocyc_protein 
         WHERE models_biocyc_protein.gene LIKE '''

        dependencies = models_BioCyc_dependencies();

        #get the proteins from the gene
        biocyc_proteins_parsed = self.getParsed_geneAndRegulatesAndNameAndComponentOf_geneAndDatabase_modelsBioCycProteins(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        if not biocyc_proteins_parsed:
            tmp = {};
            tmp['gene'] = gene_I;
            tmp['regulates'] = [''];
            tmp['protein_name'] =  None; #required for proteinFeatures
            tmp['component_of'] = [''];
            biocyc_proteins_parsed.append(tmp)

        biocyc_polymerSegments=[];
        for row in biocyc_proteins_parsed:
            tmp = self.get_nameAndComponents_componentsAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
            row['gene'],
            parentClasses_I = '("Transcription-Units")',
            database_I=database_I,
            query_I=query_I,
            );

            for t in tmp:
                t['gene']=row['gene'];
                t['regulates']=row['regulates'];
                t['protein_name']=row['protein_name'];
                t['component_of']=row['component_of'];
                t['transcription_unit']=t['name'];
                t['component']=dependencies.extract_regulatedEntityFromComponents(
                    t['components'])
                biocyc_polymerSegments.append(t);

        #check reactions and enzymatic reactions for regulation
        #glutamine synthetase adenylyltransferase / glutamine synthetase deadenylase

        biocyc_regulation = [];
        for row in biocyc_polymerSegments:
            #regulators of the polymerase
            regulators_polymerase=[];
            #regulators_polymerase = self.get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatedEntityAndDatabase_modelsBioCycRegulation(
            if row['component']:
                regulators_polymerase = self.get_rows_regulatedEntityAndDatabase_modelsBioCycRegulation(
                    row['component'],database_I=database_I,
                    query_I=query_I,
                    );
            #regulators of the transcript
            regulators_tu = []
            #regulators_tu = self.get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatedEntityAndDatabase_modelsBioCycRegulation(
            if row['transcription_unit']:
                regulators_tu = self.get_rows_regulatedEntityAndDatabase_modelsBioCycRegulation(
                    row['transcription_unit'],database_I=database_I,
                    query_I=query_I,
                    );
            #regulators of the protein/RNA
            regulators_peptide = []
            #regulators_peptide = self.get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatedEntityAndDatabase_modelsBioCycRegulation(
            if row['protein_name']:
                regulators_peptide = self.get_rows_regulatedEntityAndDatabase_modelsBioCycRegulation(
                    row['protein_name'],database_I=database_I,
                    query_I=query_I,
                    );
            #regulators of the complex
            regulators_complex = []
            if row['component_of'][0]:
                for regulator in row['component_of']:
                    tmp = [];
                    tmp = self.get_rows_regulatedEntityAndDatabase_modelsBioCycRegulation(
                        regulator,database_I=database_I,
                        query_I=query_I,
                        );
                    regulators_complex.extend(tmp); 
            #regulated_entities of the protein/RNA
            regulated_entities=[];
            #if row['regulates'][0]:
            #    for regulator in row['regulates']:
            #        tmp = self.get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatorAndDatabase_modelsBioCycRegulation(
            #            regulator,database_I=database_I,
            #            query_I=query_I,
            #            );      
            #        regulated_entities.extend(tmp);  

            regulators_all = regulators_polymerase + regulators_tu + \
                regulators_peptide + regulated_entities + regulators_complex;
            if regulators_all:
                for regulator in regulators_all:
                    regulator['gene']=row['gene'];
                    regulator['protein_name']=row['protein_name'];
                    regulator['transcription_unit']=row['transcription_unit'];
                    #regulator['regulated_entity']=None;
                    modes = dependencies.convert_bioCycList2List(regulator['mode'])
                    if len(modes)>1: print('more than one mode of regulation found');
                    regulator['mode']=modes[0];
                    parent_classes = dependencies.convert_bioCycList2List(regulator['parent_classes']);
                    if len(parent_classes)>1: print('more than one parent_classes found');
                    regulator['parent_classes']=parent_classes[0];
                    #regulator['regulator']=None;
                    biocyc_regulation.append(regulator);
            if not regulators_polymerase: #ensure there is an entry for TUs without a regulator
                tmp = {};
                tmp['gene']=row['gene'];
                tmp['protein_name']=row['protein_name'];
                tmp['transcription_unit']=row['transcription_unit'];
                tmp['regulated_entity']=row['component'];
                tmp['mode']='0';
                tmp['parent_classes']='No regulation';
                tmp['regulator']='No regulator';
                biocyc_regulation.append(tmp);

        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        data_O = [];
        for row in biocyc_regulation:
            if not row in data_O:
                data_O.append(row);

        return data_O;

    def getJoin_regulatedEntities_geneAndDatabase_modelsBioCycProteinAndRegulationAndPolymerSegment(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_proteinFeatures
        WHERE feature_of LIKE '''

        dependencies = models_BioCyc_dependencies();

        # get the protein regulators
        biocyc_proteins_parsed = self.getParsed_geneAndRegulatesAndNameAndComponentOf_geneAndDatabase_modelsBioCycProteins(
            gene_I,database_I=database_I,
            query_I=query_I,
            );

        # get the polymer regulators
        biocyc_polymerSegments = self.get_nameAndProductsAndParentClasses_nameAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_polymerSegments_parsed = [];
        for row in biocyc_polymerSegments:
            tmp = {};
            tmp['gene'] = row['name'];
            tmp['product'] = list(set(dependencies.convert_bioCycList2List(row['product'])));
            biocyc_proteins_parsed.append(tmp)

        biocyc_regulation = [];
        for row in biocyc_proteins_parsed + biocyc_polymerSegments_parsed:
            #regulated_entities of the protein/RNA
            regulated_entities=[];
            if 'regulates' in row.keys() and row['regulates'][0]:
                for name in row['regulates']:
                    tmp = [];
                    tmp = self.get_rows_nameAndDatabase_modelsBioCycRegulation(
                        name,database_I=database_I,
                        query_I=query_I,
                        );      
                    regulated_entities.extend(tmp);
            if 'component_of' in row.keys() and row['component_of'][0]:
                for regulator in row['component_of']:
                    tmp = [];
                    tmp = self.get_rows_regulatorAndDatabase_modelsBioCycRegulation(
                        regulator,database_I=database_I,
                        query_I=query_I,
                        );      
                    regulated_entities.extend(tmp);  
            if 'product' in row.keys() and row['product'][0]:
                for regulator in row['product']:
                    tmp = [];
                    tmp = self.get_rows_regulatorAndDatabase_modelsBioCycRegulation(
                        regulator,database_I=database_I,
                        query_I=query_I,
                        );      
                    regulated_entities.extend(tmp); 

            #if regulated_entities:
            for regulator in regulated_entities:
                regulator['gene']=row['gene'];
                #regulator['protein_name']=row['protein_name'];
                #regulator['regulated_entity']=None;
                modes = dependencies.convert_bioCycList2List(regulator['mode'])
                if len(modes)>1: print('more than one mode of regulation found');
                regulator['mode']=modes[0];
                parent_classes = dependencies.convert_bioCycList2List(regulator['parent_classes']);
                if len(parent_classes)>1: print('more than one parent_classes found');
                regulator['parent_classes']=parent_classes[0];
                #regulator['regulator']=None;
                biocyc_regulation.append(regulator);

        biocyc_polymerSegments=[];
        for row in biocyc_regulation:
            #TODO: add a check ensure that the component does not pull out the same gene
            transcription_units = self.get_nameAndComponentsAndRegulatedBy_componentsAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
                row['regulated_entity'],
                parentClasses_I = '("Transcription-Units")',
                database_I=database_I,
                query_I=query_I,
                );
            for tu in transcription_units:
                tmp = copy.copy(row);
                tmp['transcription_unit']=tu['name'];
                biocyc_polymerSegments.append(tmp);

        #TODO: recursively pull out all of the regulator components

        return biocyc_polymerSegments

    def getJoin_reactions_geneAndDatabase_modelsBioCycProteinAndPolymerSegmentAndReaction(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_proteinFeatures
        WHERE feature_of LIKE '''

        dependencies = models_BioCyc_dependencies();

        # get the proteins
        biocyc_proteins = self.get_geneAndRegulatesAndNameAndComponentOf_geneAndDatabase_modelsBioCycProteins(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_proteins_parsed = [];
        for row in biocyc_proteins:
            tmp = {};
            tmp['gene'] = dependencies.convert_bioCycList2List(row['gene'])[0];
            tmp['protein_name'] =  row['name']; #required for proteinFeatures
            components_of = dependencies.convert_bioCycList2List(row['component_of']);
            tmp['component_of'] = components_of;
            biocyc_proteins_parsed.append(tmp)

        # get the polymers
        biocyc_polymerSegments = self.get_nameAndProductsAndParentClasses_nameAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_polymerSegments_parsed = [];
        for row in biocyc_polymerSegments:
            tmp = {};
            tmp['gene'] = row['name'];
            tmp['product'] = list(set(dependencies.convert_bioCycList2List(row['product'])));
            biocyc_proteins_parsed.append(tmp)

        biocyc_reactions = [];
        for row in biocyc_proteins_parsed + biocyc_polymerSegments_parsed:
            #get the reactions
            general_reaction=[];
            if 'protein_name' in row.keys() and row['protein_name']:
                tmp1 = [];
                tmp1 = self.get_rows_leftAndDatabase_modelsBioCycReactions(
                    row['protein_name'],database_I=database_I,
                    query_I=query_I,
                    );    
                general_reaction.extend(tmp1);
            if 'component_of' in row.keys() and row['component_of'][0]:
                for left in row['component_of']:
                    tmp1 = [];
                    tmp1 = self.get_rows_leftAndDatabase_modelsBioCycReactions(
                        left,database_I=database_I,
                        query_I=query_I,
                        );    
                    general_reaction.extend(tmp1); 
            if 'product' in row.keys() and row['product'][0]:
                for left in row['product']:
                    tmp1 = [];
                    tmp1 = self.get_rows_leftAndDatabase_modelsBioCycReactions(
                        left,database_I=database_I,
                        query_I=query_I,
                        );    
                    general_reaction.extend(tmp1); 

            for reaction in general_reaction:
                reaction['gene']=row['gene'];
                parent_classes = dependencies.convert_bioCycList2List(reaction['parent_classes']);
                if len(parent_classes)>1: print('more than one parent_classes found');
                reaction['parent_classes']='-'.join(parent_classes);
                biocyc_reactions.append(reaction);

        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        data_O = [];
        for row in biocyc_reactions:
            if not row in data_O:
                data_O.append(row);

        return data_O;

    def getJoin_enzymaticReactions_geneAndDatabase_modelsBioCycProteinAndPolymerSegmentAndEnzymaticReactions(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''
        '''

        dependencies = models_BioCyc_dependencies();

        # get the proteins
        biocyc_proteins = self.get_geneAndRegulatesAndNameAndComponentOf_geneAndDatabase_modelsBioCycProteins(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_proteins_parsed = [];
        for row in biocyc_proteins:
            tmp = {};
            tmp['gene'] = dependencies.convert_bioCycList2List(row['gene'])[0];
            tmp['protein_name'] =  row['name']; #required for proteinFeatures
            components_of = dependencies.convert_bioCycList2List(row['component_of']);
            tmp['component_of'] = components_of;
            biocyc_proteins_parsed.append(tmp)

        # get the polymers
        biocyc_polymerSegments = self.get_nameAndProductsAndParentClasses_nameAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_polymerSegments_parsed = [];
        for row in biocyc_polymerSegments:
            tmp = {};
            tmp['gene'] = row['name'];
            tmp['product'] = list(set(dependencies.convert_bioCycList2List(row['product'])));
            biocyc_proteins_parsed.append(tmp)

        biocyc_reactions = [];
        for row in biocyc_proteins_parsed + biocyc_polymerSegments_parsed:
            #get the reactions
            general_reaction=[];
            if 'protein_name' in row.keys() and row['protein_name']:
                tmp1 = [];
                tmp1 = self.get_rows_enzymeAndDatabase_modelsBioCycEnzymaticReactions(
                    row['protein_name'],database_I=database_I,
                    query_I=query_I,
                    );    
                general_reaction.extend(tmp1);
            if 'component_of' in row.keys() and row['component_of'][0]:
                for left in row['component_of']:
                    tmp1 = [];
                    tmp1 = self.get_rows_enzymeAndDatabase_modelsBioCycEnzymaticReactions(
                        left,database_I=database_I,
                        query_I=query_I,
                        );    
                    general_reaction.extend(tmp1); 
            if 'product' in row.keys() and row['product'][0]:
                for left in row['product']:
                    tmp1 = [];
                    tmp1 = self.get_rows_enzymeAndDatabase_modelsBioCycEnzymaticReactions(
                        left,database_I=database_I,
                        query_I=query_I,
                        );    
                    general_reaction.extend(tmp1); 

            for reaction in general_reaction:
                reaction['gene']=row['gene'];
                parent_classes = dependencies.convert_bioCycList2List(reaction['parent_classes']);
                if len(parent_classes)>1: print('more than one parent_classes found');
                reaction['parent_classes']='-'.join(parent_classes);
                biocyc_reactions.append(reaction);

        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        data_O = [];
        for row in biocyc_reactions:
            if not row in data_O:
                data_O.append(row);

        return data_O;

    def getJoin_enzymaticReactions_geneAndDatabase_modelsBioCycProteinAndPolymerSegmentAndEnzymaticReactionsAndRegulation(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''
        '''
        
        data_O = [];
        dependencies = models_BioCyc_dependencies();

        enzymatic_reactions = self.getJoin_enzymaticReactions_geneAndDatabase_modelsBioCycProteinAndPolymerSegmentAndEnzymaticReactions(
            gene_I,database_I=database_I,
            query_I=query_I,
            output_O='listDict',
            dictColumn_I=None);

        if not enzymatic_reactions: return data_O;

        biocyc_regulation = [];
        for row in enzymatic_reactions:
            #regulated_entities of the protein/RNA
            regulated_entities=[];
            regulated_by = dependencies.convert_bioCycList2List(row['regulated_by']);
            if regulated_by and regulated_by[0]:
                for regulated in regulated_by:
                    tmp = self.get_rows_nameAndDatabase_modelsBioCycRegulation(
                        regulated,database_I=database_I,
                        query_I=query_I,
                        );      
                    regulated_entities.extend(tmp);

            if regulated_entities:
                for regulator in regulated_entities:
                    modes = dependencies.convert_bioCycList2List(regulator['mode'])
                    if len(modes)>1: print('more than one mode of regulation found');
                    regulator['mode']=modes[0];
                    parent_classes = dependencies.convert_bioCycList2List(regulator['parent_classes']);
                    if len(parent_classes)>1: print('more than one parent_classes found');
                    regulator['regulation_parent_classes']=parent_classes[0];
                    regulator.update(row);
                    biocyc_regulation.append(regulator);
            else:
                row['mode']='none'
                row['regulation_parent_classes']='none'
                row['regulator']='none'
                biocyc_regulation.append(row);

        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        for row in biocyc_regulation:
            if not row in data_O:
                data_O.append(row);

        return data_O;
    
    def getJoin_genesAndNamesFeatures_geneAndDatabase_modelsBioCycProteinsAndProteinFeatures(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''
        SELECT models_biocyc_proteinFeatures.*
         FROM models_biocyc_protein,models_biocyc_proteinFeatures 
         WHERE models_biocyc_protein.gene LIKE '''

        dependencies = models_BioCyc_dependencies();
        
        biocyc_proteins = self.get_rows_geneAndDatabase_modelsBioCycProteins(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_proteins_parsed = [];
        for row in biocyc_proteins:
            tmp = {};
            tmp['gene'] = dependencies.convert_bioCycList2List(row['gene'])[0];
            tmp['protein_name'] = row['name']; #required for proteinFeatures
            tmp['locations'] = row['locations'];
            tmp['molecular_weight_kd'] = row['molecular_weight_kd'];
            #parse features
            features = dependencies.convert_bioCycList2List(row['features']);
            tmp['features'] = features; 
            #parse components of
            #tmp['component_of'] = row['component_of']
            component_of = dependencies.convert_bioCycList2List(row['component_of']);
            if component_of[0]:
                for component in component_of:
                    tmp1 = copy.copy(tmp);
                    tmp1['component_of'] = component;
                    biocyc_proteins_parsed.append(tmp1)
            else:
                tmp['component_of'] = None; 
                biocyc_proteins_parsed.append(tmp)

        biocyc_features = [];
        for row in biocyc_proteins_parsed:
            #proteinFeatures
            features=[];
            if row['features'][0]:
                for feature in row['features']:
                    tmp1 = [];
                    if not row['component_of'] is None:
                        tmp1 = self.get_rows_nameAndFeatureOfAndDatabase_modelsBioCycProteinFeatures(
                            feature,row['component_of'],database_I=database_I,
                            query_I=query_I,
                            );   
                    tmp2 = [];
                    tmp2 = self.get_rows_nameAndFeatureOfAndDatabase_modelsBioCycProteinFeatures(
                        feature,row['protein_name'],database_I=database_I,
                        query_I=query_I,
                        );         
                    features.extend(tmp1);
                    features.extend(tmp2);
            for tmp in features:
                #copies from row
                tmp['gene'] = row['gene'];
                tmp['protein_name'] =  row['protein_name'];
                #changes to features
                tmp['protein_feature'] = tmp['name'];
                tmp['feature_of'] = dependencies.convert_bioCycList2List(tmp['feature_of'])[0];
                biocyc_features.append(tmp);                

        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        data_O = [];
        for row in biocyc_features:
            if not row in data_O:
                data_O.append(row);

        return data_O;

    def getJoin_regulatorsAndRegulatedEntities_database_modelsBioCycRegulationAndAll(
        self,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''
        SELECT 
         FROM  
         WHERE  LIKE '''

        dependencies = models_BioCyc_dependencies();

        data_O = [];
        regulation_1 = {};
        #get regulators and regulated entities
        regulation = self.get_rows_databaseAndNotNull_modelsBioCycRegulation(
            database_I=database_I,
            query_I=query_I,
            output_O=output_O,
            dictColumn_I=dictColumn_I
            );
        for reg in regulation:
            if reg['regulator']=='' and reg['regulated_entity']=='':continue;
            #remove keys
            for key in list(reg.keys())[:]:
                if key not in ['mode','regulator','regulated_entity','mechanism','name']:
                    del reg[key];
            #add in keys to fill
            #reg.update({
            #    'regulated_entity_gene':'',
            #    'regulated_entity_enzymaticReaction':'',
            #    'regulated_entity_promoter':'',
            #    'regulated_entity_product':'',
            #    'regulated_entity_protein':'',
            #    'regulator_gene':'',
            #    'regulator_protein':'',
            #    'regulator_RNA':'',
            #    'regulator_compound':''})
            unique1 = (reg['regulator'],reg['regulated_entity'],
                       reg['mode'],reg['mechanism'],reg['name'])
            #unique1 = reg['name']
            if not unique1 in regulation_1.keys():
                regulation_1[unique1]={};
                reg.update({
                    'regulated_entity_gene':[],
                    'regulated_entity_enzymaticReaction':[],
                    'regulated_entity_promoter':[],
                    'regulated_entity_product':[],
                    'regulated_entity_protein':[],
                    'regulator_gene':[],
                    'regulator_protein':[],
                    'regulator_RNA':[],
                    'regulator_compound':[]})
                regulation_1[unique1].update(reg);
            #lookup the regulated_entities
            regulated_entities_proteins = self.get_rows_nameAndDatabase_modelsBioCycProteins(
                name_I = reg['regulated_entity'],
                database_I = database_I)
            for reps in regulated_entities_proteins:
                genes = dependencies.convert_bioCycList2List(reps['gene']);
                regulation_1[unique1]['regulated_entity_protein'].append(reps['name']);
                regulation_1[unique1]['regulated_entity_gene'].extend(genes);
                #for gene in genes:
                #    #parse out genes and proteins
                #    tmp = copy.copy(reg);
                #    tmp['regulated_entity_protein'] = reps['name'];
                #    tmp['regulated_entity_gene'] = gene;
                #    regulation_1[unique1].append(tmp);
            regulated_entities_enzymaticReactions = self.get_rows_nameAndDatabase_modelsBioCycEnzymaticReactions(
                name_I = reg['regulated_entity'],
                database_I = database_I)
            for reps in regulated_entities_enzymaticReactions:
                genes = dependencies.convert_bioCycList2List(reps['name']);
                regulation_1[unique1]['regulated_entity_enzymaticReaction'].extend(genes);
                #for gene in genes:
                #    #parse out genes and proteins
                #    tmp = copy.copy(reg);
                #    tmp['regulated_entity_enzymaticReaction'] = gene;
                #    regulation_1[unique1].append(tmp);
            regulated_entities_polymerSegments = self.get_rows_nameAndDatabase_modelsBioCycPolymerSegments(
                name_I = reg['regulated_entity'],
                database_I = database_I)
            for reps in regulated_entities_polymerSegments:
                products = dependencies.convert_bioCycList2List(reps['product'])
                regulation_1[unique1]['regulated_entity_gene'].append(reps['name']);
                regulation_1[unique1]['regulated_entity_product'].extend(products);
                #for product in products:
                #    #gene/promoter
                #    #parse out the products
                #    tmp = copy.copy(reg);
                #    tmp['regulated_entity_gene'] = reps['name'];
                #    tmp['regulated_entity_product'] = product;
                #    regulation_1[unique1].append(tmp);
            regulated_entities_polymerSegments = self.get_rows_componentsAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
                components_I = reg['regulated_entity'],
                database_I = database_I)
            for reps in regulated_entities_polymerSegments:
                genes = dependencies.parse_transcriptionUnit(reps['name']);
                regulation_1[unique1]['regulated_entity_promoter'].append(reps['name']);
                regulation_1[unique1]['regulated_entity_gene'].extend(genes);
                #for gene in genes:
                #    #gene/promoter
                #    #parse out transcription units then genes
                #    tmp = copy.copy(reg);
                #    tmp['regulated_entity_promoter'] = reps['name'];
                #    tmp['regulated_entity_gene'] = gene;
                #    regulation_1[unique1].append(tmp);
            #lookup the regulators
            regulators_compounds = self.get_rows_nameAndDatabase_modelsBioCycCompounds(
                name_I = reg['regulator'],
                database_I = database_I)
            for regs in regulators_compounds:
                regulation_1[unique1]['regulator_compound'].append(regs['name']);
                #tmp = copy.copy(reg);
                #tmp['regulator_compound'] = regs['name'];
                #regulation_1[unique1].append(tmp);
            regulators_proteins = self.get_rows_nameAndDatabase_modelsBioCycProteins(
                name_I = reg['regulator'],
                database_I = database_I)
            for regs in regulators_proteins:
                genes = dependencies.convert_bioCycList2List(regs['gene']);
                regulation_1[unique1]['regulator_protein'].append(regs['name']);
                regulation_1[unique1]['regulator_gene'].extend(genes);
                #for gene in genes:
                #    #parse out genes and proteins
                #    tmp = copy.copy(reg);
                #    tmp['regulator_protein'] = regs['name'];
                #    tmp['regulator_gene'] = gene;
                #    regulation_1[unique1].append(tmp);
            regulators_RNAs = self.get_rows_nameAndDatabase_modelsBioCycRNAs(
                name_I = reg['regulator'],
                database_I = database_I)
            for regs in regulators_RNAs:
                genes = dependencies.convert_bioCycList2List(regs['gene']);
                regulation_1[unique1]['regulator_RNA'].append(regs['name']);
                regulation_1[unique1]['regulator_gene'].extend(genes);
                #for gene in genes:
                #    #parse out genes and rans
                #    tmp = copy.copy(reg);
                #    tmp['regulator_RNA'] = regs['name'];
                #    tmp['regulator_gene'] = gene;
                #    regulation_1[unique1].append(tmp);
            #lookup the names (alternative to regulators)
            #models_biocyc_proteins.regulates LIKE '%"[]"%' -> models_biocyc_proteins.gene (parse string list)
            #models_biocyc_RNAs.regulates LIKE '%"[]"%' -> models_biocyc_RNAs.gene (parse string list)
            #models_biocyc_compounds.regulates LIKE 'u%"[]"%' -> models_biocyc_compounds.name      
            
        #remove duplicate entries
        #(NOTE: only works because each dictionary is constructed identically)
        regulation_O = {};
        for k,v in regulation_1.items():
            if not k in regulation_O.keys():
                regulation_O[k]=[];
            row = {};
            for k1,v1 in v.items():
                #remove non-valid gene ids
                if type(v1)==type([]) and k1=='regulated_entity_gene':
                    tmp = [r for r in v1 if not dependencies.check_promoter(r)];
                    v1 = tmp;
                #remove duplicates in the list
                if type(v1)==type([]):
                    v1 = list(set(v1)); 
                    v1.sort();
                #remove empty lists
                if type(v1)==type([]) and v1 and v1[0]=='':
                    v1=[];
                row[k1]=v1;
            regulation_O[k].append(row);

        return regulation_O;
    
    #Parsed queries only
    def getParsed_genesAndPathwaysAndReactions_superPathwayAndDatabase_modelsBioCycPathways(
        self,super_pathway_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT models_biocyc_protein.genes_of_pathway,
        models_biocyc_pathways.name,
        models_biocyc_pathways.primaries
        FROM models_biocyc_pathways
        WHERE models_biocyc_pathways.super_pathway LIKE
        AND models_biocyc_pathways.database LIKE '''

        dependencies = models_BioCyc_dependencies();

        data_O = [];
        biocyc_pathways = self.get_rows_superPathwayAndDatabase_modelsBioCycPathways(
            super_pathway_I,database_I='ECOLI',
            query_I={},
            output_O='listDict',
            dictColumn_I=None);
        for pathway in biocyc_pathways:
            genes = dependencies.convert_bioCycList2List(pathway['genes_of_pathway']);
            for gene in genes:
                tmp = {};
                tmp['pathway'] = pathway['name'];
                tmp['primaries'] = pathway['primaries'];
                tmp['gene'] = gene;
                data_O.append(tmp);
        return data_O;
    
    def getParsed_genesAndPathwaysAndReactions_namesAndDatabase_modelsBioCycPathways(
        self,names_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT models_biocyc_protein.genes_of_pathway,
        models_biocyc_pathways.name,
        models_biocyc_pathways.primaries
        FROM models_biocyc_pathways
        WHERE models_biocyc_pathways.name =ANY
        AND models_biocyc_pathways.database LIKE '''

        dependencies = models_BioCyc_dependencies();

        data_O = [];
        biocyc_pathways = self.get_rows_namesAndDatabase_modelsBioCycPathways(
            names_I,database_I='ECOLI',
            query_I={},
            output_O='listDict',
            dictColumn_I=None);
        for pathway in biocyc_pathways:
            genes = dependencies.convert_bioCycList2List(pathway['genes_of_pathway']);
            for gene in genes:
                tmp = {};
                tmp['pathway'] = pathway['name'];
                tmp['primaries'] = pathway['primaries'];
                tmp['gene'] = gene;
                data_O.append(tmp);
            #if genes and genes[0]!='':
            #    for gene in genes:
            #        tmp = {};
            #        tmp['pathway'] = pathway['name'];
            #        tmp['primaries'] = pathway['primaries'];
            #        tmp['gene'] = gene;
            #        data_O.append(tmp);
            #else:
            #    tmp = {};
            #    tmp['pathway'] = pathway['name'];
            #    tmp['primaries'] = pathway['primaries'];
            #    tmp['gene'] = None;
            #    data_O.append(tmp);
        return data_O;
    
    def getParsed_genesAndAccessionsAndSynonyms_namesAndDatabase_modelsBioCycPolymerSegments(
        self,names_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT models_biocyc_polymerSegments.name,
        models_biocyc_polymerSegments.common_name,
        models_biocyc_polymerSegments.accession_1,
        models_biocyc_polymerSegments.synonyms
        FROM models_biocyc_polymerSegments
        WHERE models_biocyc_polymerSegments.name =ANY
        AND models_biocyc_polymerSegments.database LIKE '''

        dependencies = models_BioCyc_dependencies();

        data_O = [];
        biocyc_polymerSegments = self.get_rows_namesAndDatabase_modelsBioCycPolymerSegments(
            names_I,database_I='ECOLI',
            query_I={},
            output_O='listDict',
            dictColumn_I=None);
        for polymerSegment in biocyc_polymerSegments:
            if not polymerSegment['accession_1']: continue;
            synonyms = dependencies.convert_bioCycList2List(polymerSegment['synonyms']);
            for synonym in synonyms:
                tmp = {};
                tmp['gene'] = polymerSegment['name'];
                tmp['common_name'] = polymerSegment['common_name'];
                tmp['accession_1'] = polymerSegment['accession_1'];
                tmp['accession_2'] = polymerSegment['accession_2'];
                tmp['synonym'] = synonym;
                data_O.append(tmp);
            #if synonyms and synonyms[0]!='':
            #    for synonym in synonyms:
            #        tmp = {};
            #        tmp['gene'] = polymerSegment['name'];
            #        tmp['common_name'] = polymerSegment['common_name'];
            #        tmp['accession_1'] = polymerSegment['accession_1'];
            #        tmp['accession_2'] = polymerSegment['accession_2'];
            #        tmp['synonym'] = synonym;
            #        data_O.append(tmp);
            #else:
            #    tmp = {};
            #    tmp['gene'] = polymerSegment['name'];
            #    tmp['common_name'] = polymerSegment['common_name'];
            #    tmp['accession_1'] = polymerSegment['accession_1'];
            #    tmp['accession_2'] = polymerSegment['accession_2'];
            #    tmp['synonym'] = [];
            #    data_O.append(tmp);

        return data_O;

    def getParsed_genesAndNames_GOTermAndDatabase_modelsBioCycProteins(
        self,go_term_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''
        SELECT models_biocyc_protein.gene, models_biocyc_protein.name AS protein_name,
        models_biocyc_protein.component_of
         FROM models_biocyc_protein,models_biocyc_regulation,models_biocyc_protein 
         WHERE models_biocyc_protein.gene LIKE 
        
        TODO: recursively pull genes from child go_classes         
        '''

        dependencies = models_BioCyc_dependencies();
        
        biocyc_proteins = self.get_genesAndNamesAndComponentOfs_GOTermAndDatabase_modelsBioCycProteins(
            go_term_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_proteins_parsed = [];
        for row in biocyc_proteins:
            tmp = {};
            tmp['go_term'] = go_term_I;
            tmp['gene'] = dependencies.convert_bioCycList2List(row['gene'])[0];
            tmp['protein_name'] =  row['name']; #required for proteinFeatures
            tmp['go_terms'] =  row['go_terms'];
            component_of = dependencies.convert_bioCycList2List(row['component_of']);
            if component_of[0]:
                for component in component_of:
                    tmp1 = copy.copy(tmp);
                    tmp1['component_of'] = component;
                    biocyc_proteins_parsed.append(tmp1)
            else:
                tmp['component_of'] = row['name']; 
                biocyc_proteins_parsed.append(tmp)
        return biocyc_proteins_parsed;
    
    def getParsed_genesAndNamesFeatures_geneAndDatabase_modelsBioCycProteins(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''
        SELECT *
         FROM models_biocyc_protein,models_biocyc_regulation,models_biocyc_protein 
         WHERE models_biocyc_protein.gene LIKE '''

        dependencies = models_BioCyc_dependencies();
        
        biocyc_proteins = self.get_rows_geneAndDatabase_modelsBioCycProteins(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_proteins_parsed = [];
        for row in biocyc_proteins:
            tmp = {};
            tmp['gene'] = dependencies.convert_bioCycList2List(row['gene'])[0];
            tmp['protein_name'] =  row['name']; #required for proteinFeatures
            tmp['component_of'] = row['component_of']
            #component_of = dependencies.convert_bioCycList2List(row['component_of']);
            #if component_of[0]:
            #    for component in component_of:
            #        tmp['component_of'] = component;
            #        biocyc_proteins_parsed.append(tmp)
            #else:
            #    tmp['component_of'] = row['name']; 
            #    biocyc_proteins_parsed.append(tmp)
            tmp['locations'] = row['locations'];
            tmp['molecular_weight_kd'] = row['molecular_weight_kd'];
            features = dependencies.convert_bioCycList2List(row['features']);
            if features[0]:
                for component in features:
                    tmp1 = copy.copy(tmp);
                    tmp1['features'] = component;
                    biocyc_proteins_parsed.append(tmp1)
            else:
                tmp['features'] = "no features"; 
                biocyc_proteins_parsed.append(tmp)
        return biocyc_proteins_parsed;

    def getParsed_nameAndProductAndParentClasses_namesAndDatabase_modelsBioCycPolymerSegments(
        self,names_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''
        '''

        dependencies = models_BioCyc_dependencies();
        
        biocyc_polymerSegments = self.get_nameAndProductAndParentClasses_namesAndDatabase_modelsBioCycPolymerSegments(
            names_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_polymerSegments_parsed = [];
        for row in biocyc_polymerSegments:
            tmp = {};
            tmp['gene'] = row['name'];
            tmp['product'] =  dependencies.convert_bioCycList2List(row['product'])[0];
            parent_classes = dependencies.convert_bioCycList2List(row['parent_classes']);
            if parent_classes[0]:
                for parent_class in parent_classes:
                    if parent_class == 'Transcription-Units': continue;
                    tmp1 = copy.copy(tmp);
                    tmp1['parent_class'] = parent_class;
                    biocyc_polymerSegments_parsed.append(tmp1)
            else:
                tmp['parent_class'] = 'None'; 
                biocyc_polymerSegments_parsed.append(tmp);

        return biocyc_polymerSegments_parsed;

    def getParsed_geneAndRegulatesAndNameAndComponentOf_geneAndDatabase_modelsBioCycProteins(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''
        '''
        dependencies = models_BioCyc_dependencies();
        # get the protein regulators
        biocyc_proteins = self.get_geneAndRegulatesAndNameAndComponentOf_geneAndDatabase_modelsBioCycProteins(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_proteins_parsed = [];
        for row in biocyc_proteins:
            tmp = {};
            tmp['gene'] = dependencies.convert_bioCycList2List(row['gene'])[0];
            tmp['regulates'] = list(set(dependencies.convert_bioCycList2List(row['regulates'])));
            tmp['protein_name'] =  row['name']; #required for proteinFeatures
            components_of = dependencies.convert_bioCycList2List(row['component_of']);
            # check for protein-ligands
            for component_of in components_of[:]:
                tmp1 = [];
                tmp1 = self.get_rows_leftAndParentClassesAndDatabase_modelsBioCycReactions(
                    component_of,
                    parentClasses_I = '("Protein-Ligand-Binding-Reactions")',
                    database_I='ECOLI',
                    query_I={},
                    output_O='listDict',
                    dictColumn_I=None);
                for t1 in tmp1:
                    right = dependencies.convert_bioCycList2List(t1['right']);
                    components_of.extend(right);
            tmp['component_of'] = components_of;
            biocyc_proteins_parsed.append(tmp)
        return biocyc_proteins_parsed;

    def getParsed_geneAndRows_metaboliteAndDatabase_modelsBioCycRegulation(
        self,metabolite_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_proteinFeatures
        WHERE feature_of LIKE '''

        dependencies = models_BioCyc_dependencies();

        # format the metabolite regulators
        biocyc_metabolites_parsed = [];
        tmp = {};
        tmp['gene']=None;
        tmp['regulator']=metabolite_I;
        biocyc_metabolites_parsed.append(tmp)

        biocyc_regulation = [];
        for row in biocyc_metabolites_parsed:
            #regulated_entities of the protein/RNA
            regulated_entities=[];
            regulated_entities = self.get_rows_regulatorAndDatabase_modelsBioCycRegulation(
                row['regulator'],database_I=database_I,
                query_I=query_I,
                );      

            #if regulated_entities:
            for regulator in regulated_entities:
                regulator['gene']=row['gene'];
                modes = dependencies.convert_bioCycList2List(regulator['mode'])
                if len(modes)>1: print('more than one mode of regulation found');
                regulator['mode']=modes[0];
                parent_classes = dependencies.convert_bioCycList2List(regulator['parent_classes']);
                if len(parent_classes)>1: print('more than one parent_classes found');
                regulator['parent_classes']=parent_classes[0];
                biocyc_regulation.append(regulator);

        biocyc_polymerSegments=[];
        for row in biocyc_regulation:
            #TODO: add a check ensure that the component does not pull out the same gene
            transcription_units = self.get_nameAndComponentsAndRegulatedBy_componentsAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
                row['regulated_entity'],
                parentClasses_I = '("Transcription-Units")',
                database_I=database_I,
                query_I=query_I,
                );
            for tu in transcription_units:
                tmp = copy.copy(row);
                tmp['transcription_unit']=tu['name'];
                biocyc_polymerSegments.append(tmp);

        #TODO: recursively pull out all of the regulator components

        return biocyc_polymerSegments

    #Complex queries
    def getComplex_transcriptionUnitParentClasses(self,tus_I,database_I='ECOLI',query_I={}):
        '''convert a list of transcription units into individual genes
        and map the parent classes to the gene names
        INPUT:
        tus_I = list of tus
        OUTPUT:
        data_O = listDict of tus and parent classes
        '''
        dependencies = models_BioCyc_dependencies();
        data_O = [];
        for tu in tus_I:
            genes = dependencies.parse_transcriptionUnit(tu);
            tmp = [];
            tmp = self.getParsed_nameAndProductAndParentClasses_namesAndDatabase_modelsBioCycPolymerSegments(
                genes,database_I=database_I,query_I=query_I,
                output_O='listDict',dictColumn_I=None);
            for t in tmp:
                t['transcription_unit'] = tu;
                data_O.append(t);
        return data_O;
