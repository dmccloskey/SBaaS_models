import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
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

# generate the exclusion list of non-carbon and cofactor metabolites
exclusion_noC_str = '2fe1s,2fe2s,3fe4s,4fe4s,ag,apoACP,aso3,aso4,tsul,\
dsbdox,dsbdrd,fe2,fe3,flxr,flxso,grxox,grxrd,h,h2,h2o,h2o2,h2s,hg2,iscs,\
iscssh,iscu,iscu_DASH_2fe2s,iscu_DASH_2fe2s2,iscu_DASH_4fe4s,k,mg2,mn2,mobd,\
n2o,na1,nh4,ni2,no,no2,no3,o2,o2s,pi,ppi,pppi,sel,seln,selnp,slnt,so2,so3,\
so4,sufbcd,sufbcd_DASH_2fe2s,sufbcd_DASH_2fe2s2,sufbcd_DASH_4fe4s,sufse,\
sufsesh,trdox,trdrd,trnaala,trnaarg,trnaasp,trnacys,trnagln,trnaglu,trnagly,\
trnahis,trnaile,trnaleu,trnalys,trnamet,trnaphe,trnapro,trnasecys,trnaser,\
trnathr,trnatrp,trnatyr,trnaval,tungs,zn2,ppt,alpp,dsbaox,dsbard,dsbcox,dsbcrd,\
dsbgox,dsbgrd'
exclusion_noC = exclusion_noC_str.split(',');
exclusion_other = ['co2','co']
exclusion_cofactors = [
        'nad','nadh','nadp','nadph',
        'atp','adp','amp','gtp','gdp','gmp',
        'utp','udp','ump','ctp','cdp','cmp',
        'itp','idp','imp',
        'fad','fadh','fadh2',
        'coa',
        'glu_DASH_L','gln_DASH_L','akg',
        'mql8','mql8h2','2dmmql8','2dmmql8h2','q8','q8h2',
        'thf',
        'ACP'
        ]
exclusion_mets = [];
exclusion_mets.extend(exclusion_noC)
exclusion_mets.extend(exclusion_cofactors)
exclusion_mets.extend(exclusion_other)
exclusion_list = ['F6PA'];
for met in exclusion_mets:
    exclusion_list.append(met+'_c')
    exclusion_list.append(met+'_p')
    exclusion_list.append(met+'_e')

# define other inputs
nodes_startAndStop = [
    ['g6p_c','icit_c'],
    ['g6p_c','r5p_c'],
    ['g6p_c','gthrd_c'],
    ];
algorithms_params = [
    {'algorithm':'all_shortest_paths','params':{'weight':'weight'}},
    {'algorithm':'all_simple_paths','params':{'cutoff':25}},
    {'algorithm':'astar_path','params':{'weight':'weight'}},
                     ];

#make the COBRA table
from SBaaS_models.models_COBRA_execute import models_COBRA_execute
exCOBRA01 = models_COBRA_execute(session,engine,pg_settings.datadir_settings);
exCOBRA01.initialize_supportedTables();
exCOBRA01.initialize_COBRA_models();

from SBaaS_COBRA.stage02_physiology_sampledData_query import stage02_physiology_sampledData_query
qSampledData01 = stage02_physiology_sampledData_query(session,engine,pg_settings.datadir_settings);
qSampledData01.initialize_supportedTables();
qSampledData01.initialize_tables();

# use the average of the sampled fluxes as the weights
rows=qSampledData01.get_rows_simulationID_dataStage02PhysiologySampledData(
    "ALEsKOs01_151026_iDM2015_full05_OxicEvo04gndEvo01EPEcoliGlc_11",
)
weights = {d['rxn_id']:d['sampling_ave'] for d in rows};
weights_reverse = {d['rxn_id']+'_reverse':-d['sampling_ave'] for d in rows};
weights.update(weights_reverse);

# run the analysis for different algorithms/params
shortestPaths_O = [];
for row in algorithms_params:
    shortestPaths = exCOBRA01.execute_findShortestPath_nodes(
        '150526_iDM2015',
        nodes_startAndStop_I = nodes_startAndStop,
        algorithm_I=row['algorithm'],
        exclusion_list_I=exclusion_list,
        params_I=row['params'],    
        weights_I=weights
        )
    shortestPaths_O.append(shortestPaths);
    for sp in shortestPaths:
        str = "start: %s, stop: %s, min: %s, max: %s, average: %s, " \
                %(sp['start'],sp['stop'],sp['path_min'],
                  sp['path_max'],sp['path_average'])
        print(str)
