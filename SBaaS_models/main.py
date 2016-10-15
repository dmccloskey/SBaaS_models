﻿import sys
#sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
sys.path.append('C:/Users/dmccloskey/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
#filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
#filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_labtop.ini';
filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_remote.ini';
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

#regulation_O = biocyc01.getJoin_regulatorsAndRegulatedEntities_database_modelsBioCycRegulationAndAll('ECOLI')

from io_utilities.import_webData import import_webData
i_webData = import_webData();

#server = "ftp://ftp.ebi.ac.uk"
server = "ftp.ebi.ac.uk"
ext = "/pub/databases/chebi/Flat_file_tab_delimited/"
filename = "chebiId_inchi_3star.tsv"
file = i_webData.get_ftp(server,ext,filename)

#parse the binary data
chebi2inchi_I = i_webData.parse_binaryFile(file,encoding = 'utf-8',deliminator = '\t',headers = [])

from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

iobase = base_importData();
iobase.read_json(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc2COBRA_regulation.json');
BioCyc2COBRA_regulation_I = iobase.data;

COBRA_metabolites_I = cobra01.get_rows_modelID_dataStage02PhysiologyModelMetabolites(
    'iJO1366')

iobase = base_importData();
iobase.read_json(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc_compounds.json');
BioCyc_compounds_I = iobase.data;

BioCyc2COBRA_regulators_O = biocyc01.convertAndMap_BioCycTranscriptionFactor2COBRA(
    BioCyc2COBRA_regulation_I,
    BioCyc_compounds_I,
    COBRA_metabolites_I,
    chebi2inchi_I
    );

BioCyc2COBRA_regulation_all = [];
#iterate through each row of regulation
for row in BioCyc2COBRA_regulation_I:
    unique = {
        'regulator':row['regulator'],
        'regulated_entity':row['regulated_entity'],
        'mode':row['mode'],
        'mechanism':row['mechanism'],
        'name':row['name']
    }
    tmp = {
        'left_EcoCyc':[],
        'left_COBRA':[],
        'right_EcoCyc':[],
        'right_COBRA':[],
    }
    if row['regulator'] in BioCyc2COBRA_regulators_O.keys():
        tmp = {
            'left_EcoCyc':BioCyc2COBRA_regulators_O[row['regulator']]['ligands']['BioCyc_name'],
            'left_COBRA':BioCyc2COBRA_regulators_O[row['regulator']]['ligands']['COBRA_met_id'],
            'right_EcoCyc':BioCyc2COBRA_regulators_O[row['regulator']]['tus'],
            'right_COBRA':BioCyc2COBRA_regulators_O[row['regulator']]['tus'],
            'regulator':row['regulator'],
            'regulated_entity':row['regulated_entity'],
            'mode':BioCyc2COBRA_regulators_O[row['regulator']]['mode'],
            'mechanism':'ligand-transcription factor-binding',
            'name':row['name']
        };
        BioCyc2COBRA_regulation_all.append(tmp);
        tmp = {
            'left_EcoCyc':BioCyc2COBRA_regulators_O[row['regulator']]['genes'],
            'left_COBRA':BioCyc2COBRA_regulators_O[row['regulator']]['genes'],
            'right_EcoCyc':BioCyc2COBRA_regulators_O[row['regulator']]['tus'],
            'right_COBRA':BioCyc2COBRA_regulators_O[row['regulator']]['tus'],
            'regulator':row['regulator'],
            'regulated_entity':row['regulated_entity'],
            'mode':BioCyc2COBRA_regulators_O[row['regulator']]['mode'],
            'mechanism':'genes-to-transcription factor',
            'name':row['name']
        };
        BioCyc2COBRA_regulation_all.append(tmp);
        BioCyc2COBRA_regulation_all.append(tmp);
        tmp = {
            'left_EcoCyc':BioCyc2COBRA_regulators_O[row['regulator']]['ligands']['BioCyc_name'],
            'left_COBRA':BioCyc2COBRA_regulators_O[row['regulator']]['ligands']['COBRA_met_id'],
            'right_EcoCyc':row['regulated_entities_EcoCyc'],
            'right_COBRA':row['regulated_entities_COBRA'],
            'regulator':row['regulator'],
            'regulated_entity':row['regulated_entity'],
            'mode':'("+" "-")',
            'mechanism':'ligand-transcription factor-target gene',
            'name':row['name']
        };
        BioCyc2COBRA_regulation_all.append(tmp);
    else:
        tmp = {
            'left_EcoCyc':row['regulators_EcoCyc'],
            'left_COBRA':row['regulators_COBRA'],
            'right_EcoCyc':row['regulated_entities_EcoCyc'],
            'right_COBRA':row['regulated_entities_COBRA'],
        };
        tmp.update(unique);
        BioCyc2COBRA_regulation_all.append(tmp);

iobase = base_exportData(BioCyc2COBRA_regulation_all);
iobase.write_dict2json(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc2COBRA_regulation_all.json');
iobase.write_dict2csv(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc2COBRA_regulation_all.csv');