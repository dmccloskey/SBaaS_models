﻿import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
#sys.path.append('C:/Users/dmccloskey/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
#filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_labtop.ini';
#filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_remote.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_base')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_models')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_COBRA')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')
sys.path.append(pg_settings.datadir_settings['github']+'/genomeScale_MFA')
sys.path.append(pg_settings.datadir_settings['github']+'/genomeScale_MFA_INCA')

#make the COBRA table
from SBaaS_models.models_COBRA_execute import models_COBRA_execute
cobra01 = models_COBRA_execute(session,engine,pg_settings.datadir_settings);
cobra01.initialize_supportedTables()
cobra01.initialize_tables()

#make the BioCyc table
from SBaaS_models.models_BioCyc_execute import models_BioCyc_execute
biocyc01 = models_BioCyc_execute(session,engine,pg_settings.datadir_settings);
biocyc01.initialize_supportedTables()
biocyc01.initialize_tables()

#genes tested: 'tpiA','gloA','nrdA','mgsA','pfkA'
#biocyc01.export_geneRegulators_js('icd','ECOLI');
#biocyc01.export_geneReactions_js('icd','ECOLI');
#biocyc01.export_geneEnzymaticReactions_js('icd','ECOLI');
#biocyc01.export_geneRegulators_js('fli%','ECOLI');
#biocyc01.export_geneRegulatedEntities_js('spf','ECOLI');
#biocyc01.export_geneProteinFeatures_js('zwf','ECOLI');

#biocyc01.export_geneAndMetaboliteRegulatedEntities_sankeyDiagram_js(
#    genes_I=['soxR','soxS','oxyR','oxyS','marA','rob'],
#    metabolites_I = ['putrescine'],
#    database_I = 'ECOLI');
#biocyc01.export_geneTranscriptionUnitRegulators_sankeyDiagram_js(
#    genes_I=['glnE'],
#    database_I = 'ECOLI');

#biocyc01.export_geneReactionAndEnzymaticReactionRegulators_sankeyDiagram_js(
#    genes_I=['glnD'],
#    database_I = 'ECOLI');

#biocyc01.export_geneReactions_forceDirectedGraph_js(
#    genes_I=['glnL','glnG','glnB','glnD','glnE','glnK','glnA'],
#    database_I = 'ECOLI');
#biocyc01.export_geneReactionsAndEnzymaticReactions_forceDirectedGraph_js(
#    genes_I=['glnL','glnG','glnB','glnD','glnE','glnK','glnA'],
#    database_I = 'ECOLI');

#stringList_I = 'gadA,gadX,gadB,gadC'
#str_list = stringList_I.split(',');
#biocyc01.export_geneParentClasses_js(str_list,'ECOLI');

#stringList_I = 'bglG,bglGFB,leuO,molR_1,sfsB,yecT,ygiZ,yidL,ykiA,ynbABCD,ynjI,yqhG,adiC,aslB,cadBA,gadAX,slp-dctR,yhiM,csgDEFG,flhDC,rcsA,wza-wzb-wzc-wcaAB,yjbE,yjbEFGH'
#str_list = stringList_I.split(',');
#biocyc01.export_transcriptionUnitParentClassesHistogram_js(str_list,'ECOLI',single_plot_I=True);

#biocyc01.export_GOTermGenes_js('GO:0046034','ECOLI');

#BioCycReactions2Genes = biocyc01.getJoin_genes_namesAndDatabase_modelsBioCycEnzymaticReactionsAndPolymerSegments(
#    names_I='[protein-PII] uridylyltransferase',database_I='ECOLI',
#    query_I={},
#    )

#regulation_O = biocyc01.getJoin_regulatorsAndRegulatedEntities_database_modelsBioCycRegulationAndAll('ECOLI')

from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

#iobase = base_importData();
#iobase.read_json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc_regulation.json');
#regulation_O = iobase.data;

#COBRA_reactions = cobra01.get_rows_modelID_dataStage02PhysiologyModelReactions(
#    'iJO1366')
#COBRA_metabolites = cobra01.get_rows_modelID_dataStage02PhysiologyModelMetabolites(
#    'iJO1366')

#iobase = base_importData();
#iobase.read_json(
#   pg_settings.datadir_settings['workspace_data']+\
#   '/_output/chebiId_inchi_3star.json');
#chebi2inchi = iobase.data;

#iobase = base_importData();
#iobase.read_json(
#   pg_settings.datadir_settings['workspace_data']+\
#   '/_output/metanetx_reac_xref.json');
#metanetx_reac_xref = iobase.data;

#iobase = base_importData();
#iobase.read_json(
#   pg_settings.datadir_settings['workspace_data']+\
#   '/_output/metanetx_chem_xref.json');
#metanetx_chem_xref = iobase.data;

#iobase = base_importData();
#iobase.read_json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc_reactions.json');
#BioCyc_reactions = iobase.data;

#iobase = base_importData();
#iobase.read_json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc_compounds.json');
#BioCyc_compounds = iobase.data;

#BioCyc_enzymaticReactions2PolymerSegments = biocyc01.getJoin_genes_enzymaticReactionsAndDatabase_modelsBioCycEnzymaticReactionsAndPolymerSegments(
#    BioCyc_reactions,
#    database_I='ECOLI',
#    query_I={},
#    output_O='listDict',
#    dictColumn_I=None
#    )

#iobase = base_exportData(BioCyc_enzymaticReactions2PolymerSegments);
#iobase.write_dict2json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc_enzymaticReactions2PolymerSegments.json');
#iobase.write_dict2csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc_enzymaticReactions2PolymerSegments.csv');

#iobase = base_importData();
#iobase.read_json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc_enzymaticReactions2PolymerSegments.json');
#BioCyc_enzymaticReactions2PolymerSegments = iobase.data;

#BioCyc2COBRA_regulation = biocyc01.convertAndMap_BioCycRegulation2COBRA(
#    BioCyc_regulation_I = regulation_O,
#    BioCyc_reactions_I = BioCyc_reactions,
#    BioCyc_enzymaticReactions2PolymerSegments_I = BioCyc_enzymaticReactions2PolymerSegments,
#    BioCyc_compounds_I = BioCyc_compounds,
#    COBRA_reactions_I = COBRA_reactions,
#    COBRA_metabolites_I = COBRA_metabolites,
#    chebi2inchi_I = chebi2inchi,
#    MetaNetX_reactions_I = metanetx_reac_xref,
#    MetaNetX_metabolites_I = metanetx_chem_xref,
#    );

#iobase = base_exportData(BioCyc2COBRA_regulation);
#iobase.write_dict2json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc2COBRA_regulation.json');
#iobase.write_dict2csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc2COBRA_regulation.csv');

#iobase = base_importData();
#iobase.read_json(
#     pg_settings.datadir_settings['workspace_data']+\
#     '/_output/BioCyc2COBRA_regulation.json');
#BioCyc2COBRA_regulation = iobase.data;

#BioCyc2COBRA_TFs = biocyc01.convertAndMap_BioCycTranscriptionFactor2COBRA(
#    BioCyc2COBRA_regulation_I = BioCyc2COBRA_regulation,
#    BioCyc_polymerSegments_I = None,
#    BioCyc_compounds_I = None,
#    COBRA_metabolites_I = COBRA_metabolites,
#    chebi2inchi_I = chebi2inchi,
#    );

#iobase = base_exportData(BioCyc2COBRA_TFs);
#iobase.write_dict2json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc2COBRA_TFs.json');

#reactions,metabolites = cobra01.execute_convertNetRxns2IndividualRxns(
#    model_id_netRxns_I='150526_iDM2015',
#    model_id_template_I='iJO1366_ALEWt_irreversible',
#    pathway_model_id_I='iJO1366_ALEWt_irreversible',
#    convert2Irreversible_I = False
#    );

## get the model reactions from table
#netRxns = cobra01.get_rows_modelID_dataStage02PhysiologyModelReactions(
#    '150526_iDM2015'
#    );
## get pathways from table (needed for conversion from iJO1366 to iDM2015)
#pathway2Reactions = cobra01.get_rowsDict_modelID_dataStage02PhysiologyModelPathways(
#    'iJO1366')
## create a reverse pathway lookup dict
#reactions2Pathway = cobra01.convert_netRxnDict2rxnNetRxnDict(
#    pathway_dict_I = pathway2Reactions,
#    convert2Irreversible_I = True
#    )
#print('check')

iobase = base_importData();
iobase.read_json(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc2COBRA_regulation_all_mapped.json');
BioCyc2COBRA_regulation_all = iobase.data;

# get the model reactions from table
reactions = cobra01.get_rows_modelID_dataStage02PhysiologyModelReactions(
    '150526_iDM2015'
    );
#convert rxns list to directed graph
interactionGraph = cobra01.convert_modelReactionsTable2InteractionGraph(
    reactions,
    attributes_I={},
    exclusion_list_I=[]);

# get pathways from table (needed for conversion from iJO1366 to iDM2015)
pathway2Reactions = cobra01.get_rowsDict_modelID_dataStage02PhysiologyModelPathways(
    'iJO1366')
# create a reverse pathway lookup dict
reactions2Pathway = cobra01.convert_netRxnDict2rxnNetRxnDict(
    pathway_dict_I = pathway2Reactions,
    convert2Irreversible_I = True
    )

#BioCyc dependencies
from SBaaS_models.models_BioCyc_dependencies import models_BioCyc_dependencies
biocyc01_dep = models_BioCyc_dependencies();
#get mapped and unmapped components
components,components_EcoCyc = biocyc01_dep.get_componentsFromBioCyc2COBRAregulation(
    BioCyc2COBRA_regulation_all)

#get alternative gene_ids from unmapped components
biocyc_genes,gene_ids,accession_1 = biocyc01.get_alternativeGeneIdentifiers_modelsBioCycPolymerSegments(
    components_EcoCyc)

data_O = biocyc01.join_BioCyc2COBRAregulationWithCOBRAinteractions(
    BioCyc2COBRA_regulation = BioCyc2COBRA_regulation_all,
    COBRA_interaction = interactionGraph,
    BioCyc_alt_id = biocyc_genes,
    COBRA_alt_id = reactions2Pathway
    )
iobase = base_exportData(data_O);
iobase.write_dict2json(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc2COBRA_regulationAndInteraction.json');
iobase.write_dict2csv(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc2COBRA_regulationAndInteraction.csv');