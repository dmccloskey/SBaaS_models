import sys
#sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
sys.path.append('C:/Users/dmccloskey/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
#filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_labtop.ini';
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

#make the BioCyc table
from SBaaS_models.models_BioCyc_execute import models_BioCyc_execute
biocyc01 = models_BioCyc_execute(session,engine,pg_settings.datadir_settings);
biocyc01.initialize_supportedTables()
biocyc01.initialize_tables()

#genes tested: 'tpiA','gloA','nrdA','mgsA'   'pfkA'
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

table1 = [{'age':27, 'person':"Jonah"},
          {'age':18, 'person':"Alan"},
          {'age':28, 'person':"Glory"},
          {'age':18, 'person':"Popeye"},
          {'age':28, 'person':"Alan"}]
table2 = [{'person':"Jonah", 'book':"Whales"},
          {'person':"Jonah", 'book':"Spiders"},
          {'person':"Alan", 'book':"Ghosts"},
          {'person':"Alan", 'book':"Zombies"},
          {'person':"Glory", 'book':"Buffy"}]
		  
table3 = biocyc01.hashJoin(table1, 'person', table2, 'person');

#table1 = [(27, "Jonah"),
#            (18, "Alan"),
#            (28, "Glory"),
#            (18, "Popeye"),
#            (28, "Alan")]
#table2 = [("Jonah", "Whales"),
#            ("Jonah", "Spiders"),
#            ("Alan", "Ghosts"),
#            ("Alan", "Zombies"),
#            ("Glory", "Buffy")]

#table3 = biocyc01.hashJoin(table1, 1, table2, 0);

biocyc01.getJoin_regulatorsAndRegulatedEntities_database_modelsBioCycRegulationAndAll('ECOLI')
