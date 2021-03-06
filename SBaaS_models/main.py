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

#BioCyc dependencies
from SBaaS_models.models_BioCyc_dependencies import models_BioCyc_dependencies
biocyc01_dep = models_BioCyc_dependencies();

#BioCyc dependencies
from SBaaS_models.models_COBRA_dependencies import models_COBRA_dependencies
cobra01_dep = models_COBRA_dependencies();

sys.path.append(pg_settings.datadir_settings['workspace']+'/sbaas_shared')
from ALEsKOs01_shared.ALEsKOs01_commonRoutines import *

#import the analysis table
iobase = base_importData();
iobase.read_csv(
    pg_settings.datadir_settings['workspace_data']+\
    '/ALEsKOs01_impFeats/ALEsKOs01_0_11_plsScores.csv');
analysis_table_I = iobase.data;

#import the analysis table
iobase = base_importData();
iobase.read_csv(
    pg_settings.datadir_settings['workspace_data']+\
    '/ALEsKOs01_impFeats/ALEsKOs01_0_11_plsScoresRelative.csv');
relative_table_I = iobase.data;

plsScoresDistances,plsScoresDistancesRelative = execute_PLSScoresDistance(
    session,
    analysis_table_I,
    relative_table_I,
    naxis_I=2,
    center_I='median')

iobase = base_exportData(plsScoresDistances);
iobase.write_dict2csv(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/ALEsKOs01_0_11_plsScoresDistances.csv');

iobase = base_exportData(plsScoresDistancesRelative);
iobase.write_dict2csv(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/ALEsKOs01_0_11_plsScoresDistancesRelative.csv');

###################################################################################
##add additional regulation for bad TF to RNA mappings in EcoCyc
#iobase = base_importData();
#iobase.read_csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/BioCyc2COBRA_regulation_mapping/BioCyc2COBRA_regulationAndInteraction_consensusAddOns.csv');
#BioCyc2COBRA_regulationAndInteraction = iobase.data;

##list of metabolite ids
#met_ids_deformatted_str = '23dpg,6pgc,accoa,acon-C,ade,adn,adp,adpglc,akg,ala-L,amp,arg-L,asn-L,atp,camp,chor,cit,citr-L,cmp,coa,ctp,dadp,damp,datp,dcdp,dcmp,dctp,dhap,dimp,dtdpglu,dtmp,dttp,dump,dutp,f6p,fad,fdp,fum,g1p,g6p,gam6p,gdp,gln-L,glu-L,glutacon,glx,glyc3p,glyclt,gmp,gsn,gthox,gthrd,gtp,gua,his-L,hxan,icit,imp,ins,itp,lac-D,Lcystin,mal-L,met-L,mmal,nad,nadh,nadp,nadph,orn,pep,phe-L,phpyr,Pool_2pg_3pg,pyr,r5p,ru5p-D,s7p,ser-L,skm,succ,thr-L,trp-L,tyr-L,udp,udpg,udpglcur,ump,ura,uri,utp'
#met_ids_deformatted = met_ids_deformatted_str.split(',')

#_ta_ids_Metabolomics_str = 'ALEsKOs01_Metabolomics_0_evo04_0_11_evo04gndEvo01,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04gndEvo02,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04gndEvo03,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04sdhCBEvo01,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04sdhCBEvo02,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04sdhCBEvo03,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04tpiAEvo01,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04tpiAEvo02,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04tpiAEvo03,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04tpiAEvo04,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04ptsHIcrrEvo01,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04ptsHIcrrEvo02,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04ptsHIcrrEvo03,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04ptsHIcrrEvo04,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo01,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo02,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo03,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo04,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo05,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo06,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo07,\
#ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo08'
#analysis_ids_RNASequencing_str = 'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gndEvo01,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gndEvo02,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gndEvo03,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCBEvo01,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCBEvo02,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCBEvo03,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo01,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo02,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo03,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo04,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo01,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo02,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo03,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo04,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo01,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo02,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo03,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo04,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo05,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo06,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo07,\
#ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo08'
#analysis_ids_sampledFluxes_str = 'ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04gndEvo01,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04gndEvo02,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04gndEvo03,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04sdhCBEvo01,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04sdhCBEvo02,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04sdhCBEvo03,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04tpiAEvo01,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04tpiAEvo02,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04tpiAEvo03,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04tpiAEvo04,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04ptsHIcrrEvo01,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04ptsHIcrrEvo02,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04ptsHIcrrEvo03,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04ptsHIcrrEvo04,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo01,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo02,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo03,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo04,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo05,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo06,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo07,\
#ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo08'

#analysis_ids = ','.join([analysis_ids_Metabolomics_str,
#    analysis_ids_RNASequencing_str,
#    analysis_ids_sampledFluxes_str]);

#sigMets,sigExpression,sigFluxes = execute_getSignificantComponents(
#    session,
#    analysis_ids_Metabolomics_str,
#    analysis_ids_RNASequencing_str,
#    analysis_ids_sampledFluxes_str
#    )
##sigComponents = {};
##sigComponents.update(sigMets);
##sigComponents.update(sigExpression);
##sigComponents.update(sigFluxes);

##read in 1reg consensus and all reg consesus
#iobase = base_importData();
#iobase.read_csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc2COBRA_1reg_consensusPerRegulator.csv');
#consensusPerRegulator_1 = iobase.data;

##reformat into a dictionary
##add entries for pvalue and correlation_coefficient
#consensusPerRegulator_dict = {};
#for d in consensusPerRegulator_1:
#    aid = d['analysis_id'].replace('Metabolomics_','')\
#            .replace('RNASequencing_','')\
#            .replace('sampledFluxes_','');
#    regulator = d['regulator'];
#    if not aid in consensusPerRegulator_dict.keys():
#        consensusPerRegulator_dict[aid]={};
#    if not regulator in consensusPerRegulator_dict[aid].keys():
#        consensusPerRegulator_dict[aid][regulator] = [];
#    tmp = copy.copy(d);
#    tmp['pvalue']=1e-3;
#    #ensure only positive patternMatch
#    if d['pattern_match']=='1/1/2000':
#        d['pattern_match'] = '1-1-0';
#    elif d['pattern_match']=='2/1/2000':
#        d['pattern_match'] = '2-1-0';
#    if d['pattern_match_description'][-1]=='-':
#        tmp['pattern_match_description'],tmp['pattern_match'] = invert_pattern(d['pattern_match_description'],d['pattern_match'])
#        tmp['correlation_coefficient']=-1.0;
#    else:
#        tmp['correlation_coefficient']=1.0;
#    consensusPerRegulator_dict[aid][regulator].append(tmp);

#patternMatch_I='novel +,\
#overcompensation +,\
#partially-restored +,\
#reinforced +,\
#restored fast +,\
#unrestored +';

#ccu = 'log2(FC),\
#mmol*gDW-1*hr-1_FC-mean_normalized,\
#umol*gDW-1_glog_normalized';

##optional_constraint_I = 'AND (correlation_coefficient > 0.88 OR correlation_coefficient < -0.88)';
#optional_constraint_I = None;

#correlation_coefficient_threshold_I = 0.88;

#data_O = execute_regulationAgreementCorrelationPatterns(
#    session,
#    BioCyc2COBRA_regulationAndInteraction,
#    met_ids_deformatted,
#    cobra01_dep,
#    analysis_ids,
#    sigComponents=sigExpression,
#    cgn=None,
#    sna=None,
#    patternMatch=patternMatch_I,
#    ccu=ccu,
#    distanceMeasure=None,
#    table_name = "data_stage02_quantification_correlationPattern",
#    optional_constraint_I=optional_constraint_I,
#    pvalue_threshold_I=None,
#    correlation_coefficient_threshold_I=correlation_coefficient_threshold_I,
#    left_data_I={},
#    right_data_I=consensusPerRegulator_dict,
#    )   

#iobase = base_exportData(data_O);
#iobase.write_dict2csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc2COBRA_1reg_regulationAndInteractionConsensusCorrelationPattern_data_O.csv');
##     '/_output/BioCyc2COBRA_regulationAndInteractionConsensusCorrelationPattern_data_O.csv');

#dataSummary_O = count_regulationAgreementCorrelation(
#    data_O,
#    pvalue_threshold = None,
#    correlation_coefficient_threshold = None)

#iobase = base_exportData(dataSummary_O);
#iobase.write_dict2csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc2COBRA_1reg_regulationAndInteractionConsensusCorrelationPattern_dataSummary_O.csv');
##     '/_output/BioCyc2COBRA_regulationAndInteractionConsensusCorrelationPattern_dataSummary_O.csv');
#####################################################################################################


#############################
##make a dummy set of sigComponents for metSum
#def makeSigComponents_sigPairWiseAgreementCorrelationPatterns(sigMets):
#    from SBaaS_models.models_COBRA_dependencies import models_COBRA_dependencies
#    cobra01_dep = models_COBRA_dependencies();

#    sigMetsSum = {};
#    for k,v in sigMets.items():
#        analysis_id = k.replace('Metabolomics','sampledFluxes');
#        sigMetsSum[analysis_id]=[]
#        for met_id in v:
#            met_id1 = met_id.split('.')[0];
#            metSum_id = cobra01_dep.format_metid(met_id1,'c')\
#                .replace('23dpg_c','13dpg_c')\
#                .replace('Pool_2pg_3pg_c','3pg_c')\
#                .replace('adpglc_c','glycogen_c')\
#                .replace('udpglcur_c','uacgam_c')\
#                .replace('gam6p_c','uacgam_c');
#            sigMetsSum[analysis_id].append(metSum_id);
#    sigComponents1 = {}
#    sigComponents1.update(sigMets);
#    sigComponents1.update(sigMetsSum);
#    return sigComponents1;

#sigComponents1 = makeSigComponents_sigPairWiseAgreementCorrelationPatterns(sigMets)

##make a custom constraint function
#def constraint_sigPairWiseAgreementCorrelationPatterns(component1,component2):
#    ''' '''
#    from SBaaS_models.models_COBRA_dependencies import models_COBRA_dependencies
#    cobra01_dep = models_COBRA_dependencies();
#    cgn1 = component1[1];
#    cgn2 = cobra01_dep.deformat_metid(component2[1])\
#            .replace('13dpg','23dpg')\
#            .replace('3pg','Pool_2pg_3pg')\
#            .replace('glycogen','adpglc')\
#            .replace('uacgam','udpglcur')\
#            .replace('uacgam','gam6p');
#    return cgn1==cgn2;

#filename_I = pg_settings.datadir_settings['workspace_data']+\
#    '/ALEsKOs01_impFeats/ALEsKOs01_0_11_correlationPatterns_metSumMetConc.csv'
    
#iobase = base_importData();
#iobase.read_csv(filename_I);
#analysis_table_I = iobase.data; 

#data1 = execute_sigPairWiseAgreementCorrelationPatterns(
#    session,
#    analysis_table_I,
#    pvalue_I = None,
#    correlation_coefficient_I = 0.88,
#    sigComponents_I=sigComponents1,
#    redundancy_I=True,
#    self_vs_self_I=True,
#    optional_constraint_I=None,
#    ccu1=['umol*gDW-1_glog_normalized','height_ratio'],
#    ccu2=['mmol*gDW-1*hr-1_metSum_FC-mean_normalized'],
#    custom_constraint_func_I=constraint_sigPairWiseAgreementCorrelationPatterns
#    )

#sigPairWiseAgreementCorrelationPatterns = count_sigPairWiseAgreementCorrelation(
#    data_I=data1);

#filename_O = pg_settings.datadir_settings['workspace_data']+\
#    '/_output/ALEsKOs01_0_11_sigPairWiseAgreementCorrelationPattern.csv'
    
#iobase = base_exportData(sigPairWiseAgreementCorrelation);
#iobase.write_dict2csv(filename_O);
#############################


#####################
#filename_I = pg_settings.datadir_settings['workspace_data']+\
#    '/BioCyc2COBRA_regulation_data/ALEsKOs01_0_11_biomassProducingPathwaysCorrelationPatterns.json'
    
#iobase = base_importData();
#iobase.read_json(filename_I);
#biomassProducingPathwaysCorrelation = iobase.data;

#subpathwayPromotersInhibitorsGrowth = count_biomassProducingPathwaysCorrelationPatterns(
#    biomassProducingPathwaysCorrelation);

#filename_O = pg_settings.datadir_settings['workspace_data']+\
#    '/_output/ALEsKOs01_0_11_biomassProducingPathwaysCorrelationPatterns_subpathwayPromotersInhibitorsGrowth.csv'
    
#iobase = base_exportData(subpathwayPromotersInhibitorsGrowth);
#iobase.write_dict2csv(filename_O);

#filename_I = pg_settings.datadir_settings['workspace_data']+\
#    '/BioCyc2COBRA_regulation_data/ALEsKOs01_0_11_biomassProducingPathwaysCorrelationPatterns_subpathwayPromotersInhibitorsGrowth.csv'

#iobase = base_importData();
#iobase.read_csv(filename_I);
#subpathwayPromotersInhibitorsGrowth = iobase.data;

#from ddt_python.ddt_container_heatmap import ddt_container_heatmap

#data_1 = [d for d in subpathwayPromotersInhibitorsGrowth if d['category_id']=='expression']
#data1_keys = [
#    'analysis_id',
#    'pathway_id',
#    'category_id',
#    ]
#data1_nestkeys = [
#    'analysis_id',
#    'pathway_id'
#    ];
#data1_keymap = {
#    'xdata':'analysis_index',
#    'ydata':'pathway_index',
#    'zdata':'promoting_or_inhibiting',
#    'rowslabel':'analysis_id',
#    'columnslabel':'pathway_id',
#    'rowsindex':'analysis_index',
#    'columnsindex':'pathway_index',
#    'rowsleaves':'analysis_index',
#    'columnsleaves':'pathway_index'
#    };

## make the ddt .js file
#nsvgtable = ddt_container_heatmap();
#nsvgtable.make_container_heatmap(
#    data_1=data_1,
#    svgcolorcategory='blue2gold64RBG',
#    svgcolordomain='min,max',
#    data1_keymap=data1_keymap,
#    data1_nestkeys=data1_nestkeys,
#    data1_keys=data1_keys,
#     svgparameters_I= {
#         'svgcellsize':18,
#         'svgmargin':{ 'top': 200, 'right': 50, 'bottom': 100, 'left': 200 },
#         'svgcolorscale':'quantile',
#         'svgcolorcategory':'blue2gold64RBG',
#         'svgcolordomain':'min,max',
#         'svgcolordatalabel':'value',
#         'svgdatalisttileid':'tile1'}
#        );

##write the file to disk
#filename_str = pg_settings.datadir_settings['visualization_data']+\
#    '/tmp/ALEsKOs01_0_11_biomassProducingPathwaysCorrelationPatterns_difference.json'
#with open(filename_str,'w') as file:
#    file.write(nsvgtable.get_allObjects());
#######################

#######################
#analysis_ids = [
## 'ALEsKOs01_0_11',
## 'ALEsKOs01_0_evo04_0_11_evo04gnd',
## 'ALEsKOs01_0_evo04_0_11_evo04pgi',
## 'ALEsKOs01_0_evo04_0_11_evo04ptsHIcrr',
## 'ALEsKOs01_0_evo04_0_11_evo04sdhCB',
## 'ALEsKOs01_0_evo04_0_11_evo04tpiA',
#'ALEsKOs01_0_evo04_0_11_evo04gndEvo01',
##'ALEsKOs01_0_evo04_0_11_evo04gndEvo02',
##'ALEsKOs01_0_evo04_0_11_evo04gndEvo03',
##'ALEsKOs01_0_evo04_0_11_evo04sdhCBEvo01',
##'ALEsKOs01_0_evo04_0_11_evo04sdhCBEvo02',
##'ALEsKOs01_0_evo04_0_11_evo04sdhCBEvo03',
##'ALEsKOs01_0_evo04_0_11_evo04tpiAEvo01',
##'ALEsKOs01_0_evo04_0_11_evo04tpiAEvo02',
##'ALEsKOs01_0_evo04_0_11_evo04tpiAEvo03',
##'ALEsKOs01_0_evo04_0_11_evo04tpiAEvo04',
##'ALEsKOs01_0_evo04_0_11_evo04ptsHIcrrEvo01',
##'ALEsKOs01_0_evo04_0_11_evo04ptsHIcrrEvo02',
##'ALEsKOs01_0_evo04_0_11_evo04ptsHIcrrEvo03',
##'ALEsKOs01_0_evo04_0_11_evo04ptsHIcrrEvo04',
##'ALEsKOs01_0_evo04_0_11_evo04pgiEvo01',
##'ALEsKOs01_0_evo04_0_11_evo04pgiEvo02',
##'ALEsKOs01_0_evo04_0_11_evo04pgiEvo03',
##'ALEsKOs01_0_evo04_0_11_evo04pgiEvo04',
##'ALEsKOs01_0_evo04_0_11_evo04pgiEvo05',
##'ALEsKOs01_0_evo04_0_11_evo04pgiEvo06',
##'ALEsKOs01_0_evo04_0_11_evo04pgiEvo07',
##'ALEsKOs01_0_evo04_0_11_evo04pgiEvo08'
#];

#data1 = execute_sigPairWiseAgreementCorrelation(
#    session,
#    analysis_ids,
#    cgn1=None,
#    cgn2=None,
#    ccu1=[ #exclude metSum and frequency
#    #'log2(FC)',
#    #'mmol*gDW-1*hr-1_FC-mean_normalized',
#    'umol*gDW-1_log2(FC-median)_normalized'
#   ],
#    ccu2=[ #exclude metSum and frequency
#    #'log2(FC)',
#    #'mmol*gDW-1*hr-1_FC-mean_normalized',
#    'umol*gDW-1_log2(FC-median)_normalized'
#   ],
#    distanceMeasure='spearman',
#    table_name = "statistics_pairWiseCorrFeat",
#    pvalue_threshold_I=None,
#    correlation_coefficient_threshold_I=0.88,
#    sigComponents_I=sigComponents)

#sigPairWiseAgreementCorrelation = count_sigPairWiseAgreementCorrelation(
#    data_I=data1);

#filename_O = pg_settings.datadir_settings['workspace_data']+\
#    '/_output/ALEsKOs01_0_11_sigPairWiseAgreementCorrelation.csv'
    
#iobase = base_exportData(sigPairWiseAgreementCorrelation);
#iobase.write_dict2csv(filename_O);
#########################
