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

    #models_biocyc_proteins
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

    #models_biocyc_regulation
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
    def get_rows_geneAndDatabase_modelsBioCycRegulation(
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

        biocyc_proteins = self.get_geneAndRegulatesAndName_geneAndDatabase_modelsBioCycProteins(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_proteins_parsed = [];
        for row in biocyc_proteins:
            tmp = {};
            tmp['gene'] = dependencies.convert_bioCycList2List(row['gene'])[0];
            tmp['regulates'] = dependencies.convert_bioCycList2List(row['regulates']);
            tmp['protein_name'] =  row['name']; #required for proteinFeatures
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
                t['transcription_unit']=t['name'];
                t['component']=dependencies.extract_regulatedEntityFromComponents(
                    t['components'])
                biocyc_polymerSegments.append(t);

        biocyc_regulation = [];
        for row in biocyc_polymerSegments:
            #regulators of the polymerase
            regulators_polymerase=[];
            #regulators_polymerase = self.get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatedEntityAndDatabase_modelsBioCycRegulation(
            regulators_polymerase = self.get_rows_regulatedEntityAndDatabase_modelsBioCycRegulation(
                row['component'],database_I=database_I,
                query_I=query_I,
                );
            #regulators of the transcript
            regulators_tu = []
            #regulators_tu = self.get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatedEntityAndDatabase_modelsBioCycRegulation(
            regulators_tu = self.get_rows_regulatedEntityAndDatabase_modelsBioCycRegulation(
                row['transcription_unit'],database_I=database_I,
                query_I=query_I,
                );
            #regulators of the protein/RNA
            regulators_peptide = []
            #regulators_peptide = self.get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatedEntityAndDatabase_modelsBioCycRegulation(
            regulators_peptide = self.get_rows_regulatedEntityAndDatabase_modelsBioCycRegulation(
                row['protein_name'],database_I=database_I,
                query_I=query_I,
                );
            #regulated_entities of the protein/RNA
            regulated_entities=[];
            #if row['regulates'][0]:
            #    for regulator in row['regulates']:
            #        tmp = self.get_regulatedEntityAndRegulatorAndModeAndParentClasses_regulatorAndDatabase_modelsBioCycRegulation(
            #            regulator,database_I=database_I,
            #            query_I=query_I,
            #            );      
            #        regulated_entities.extend(tmp);  

            regulators_all = regulators_polymerase + regulators_tu + regulators_peptide + regulated_entities;
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

        return biocyc_regulation;

    def getJoin_regulatedEntities_geneAndDatabase_modelsBioCycProteinAndRegulationAndPolymerSegment(
        self,gene_I,database_I='ECOLI',
        query_I={},
        output_O='listDict',
        dictColumn_I=None):
        '''SELECT * FROM models_biocyc_proteinFeatures
        WHERE feature_of LIKE '''

        dependencies = models_BioCyc_dependencies();

        biocyc_proteins = self.get_geneAndRegulatesAndName_geneAndDatabase_modelsBioCycProteins(
            gene_I,database_I=database_I,
            query_I=query_I,
            );
        biocyc_proteins_parsed = [];
        for row in biocyc_proteins:
            tmp = {};
            tmp['gene'] = dependencies.convert_bioCycList2List(row['gene'])[0];
            tmp['regulates'] = dependencies.convert_bioCycList2List(row['regulates']);
            tmp['protein_name'] =  row['name']; #required for proteinFeatures
            biocyc_proteins_parsed.append(tmp)

        biocyc_regulation = [];
        for row in biocyc_proteins_parsed:
            #regulated_entities of the protein/RNA
            regulated_entities=[];
            if row['regulates'][0]:
                for name in row['regulates']:
                    tmp = self.get_rows_geneAndDatabase_modelsBioCycRegulation(
                        name,database_I=database_I,
                        query_I=query_I,
                        );      
                    regulated_entities.extend(tmp);  

            #if regulated_entities:
            for regulator in regulated_entities:
                regulator['gene']=row['gene'];
                regulator['protein_name']=row['protein_name'];
                #regulator['regulated_entity']=None;
                modes = dependencies.convert_bioCycList2List(regulator['mode'])
                if len(modes)>1: print('more than one mode of regulation found');
                regulator['mode']=modes[0];
                parent_classes = dependencies.convert_bioCycList2List(regulator['parent_classes']);
                if len(parent_classes)>1: print('more than one parent_classes found');
                regulator['parent_classes']=parent_classes[0];
                #regulator['regulator']=None;
                biocyc_regulation.append(regulator);
            #if not regulators_polymerase: #ensure there is an entry for TUs without a regulator
            #    tmp = {};
            #    tmp['gene']=row['gene'];
            #    tmp['protein_name']=row['protein_name'];
            #    tmp['transcription_unit']=row['transcription_unit'];
            #    tmp['regulated_entity']=row['component'];
            #    tmp['mode']='0';
            #    tmp['parent_classes']='No regulation';
            #    tmp['regulator']='No regulator';
            #    biocyc_regulation.append(tmp);

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
                #tu['component']=dependencies.extract_regulatedEntityFromComponents(
                #    tu['components']);
                ##parse through the regulated components
                #regulated_by = [];
                #regulated_by = dependencies.convert_bioCycList2List(
                #    tu['regulated_by']);
                #if regulated_by[0]:
                #    for regulated in regulated_by:
                #        tu['regulated_by']=regulated
                #        biocyc_polymerSegments.append(tu);
                #else: 
                #    tu['regulated_by']="No regulators"
                #    biocyc_polymerSegments.append(tu);
                biocyc_polymerSegments.append(tmp);

        #TODO: recursively pull out all of the regulator components

        return biocyc_polymerSegments;
