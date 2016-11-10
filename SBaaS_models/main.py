import sys
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

#BioCyc dependencies
from SBaaS_models.models_BioCyc_dependencies import models_BioCyc_dependencies
biocyc01_dep = models_BioCyc_dependencies();

#BioCyc dependencies
from SBaaS_models.models_COBRA_dependencies import models_COBRA_dependencies
cobra01_dep = models_COBRA_dependencies();

sys.path.append(pg_settings.datadir_settings['workspace']+'/sbaas_shared')
from ALEsKOs01_shared.ALEsKOs01_commonRoutines import *

iobase = base_importData();
iobase.read_json(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc2COBRA_regulationAndInteraction.json');
BioCyc2COBRA_regulationAndInteraction = iobase.data;

#get mapped and unmapped components
components = [];
for row in BioCyc2COBRA_regulationAndInteraction:
    if row['left']:
        components.append(row['left'])
    if row['left']:
        components.append(row['right'])
components = list(set(components))
print(len(components)) #5844

#list of metabolite ids
met_ids_deformatted_str = '23dpg,6pgc,accoa,acon-C,ade,adn,adp,adpglc,akg,ala-L,amp,arg-L,asn-L,atp,camp,chor,cit,citr-L,cmp,coa,ctp,dadp,damp,datp,dcdp,dcmp,dctp,dhap,dimp,dtdpglu,dtmp,dttp,dump,dutp,f6p,fad,fdp,fum,g1p,g6p,gam6p,gdp,gln-L,glu-L,glutacon,glx,glyc3p,glyclt,gmp,gsn,gthox,gthrd,gtp,gua,his-L,hxan,icit,imp,ins,itp,lac-D,Lcystin,mal-L,met-L,mmal,nad,nadh,nadp,nadph,orn,pep,phe-L,phpyr,Pool_2pg_3pg,pyr,r5p,ru5p-D,s7p,ser-L,skm,succ,thr-L,trp-L,tyr-L,udp,udpg,udpglcur,ump,ura,uri,utp'
met_ids_deformatted = met_ids_deformatted_str.split(',')

analysis_ids_Metabolomics_str = 'ALEsKOs01_Metabolomics_0_evo04_0_11_evo04gndEvo01,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04gndEvo02,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04gndEvo03,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04sdhCBEvo01,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04sdhCBEvo02,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04sdhCBEvo03,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04tpiAEvo01,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04tpiAEvo02,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04tpiAEvo03,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04tpiAEvo04,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04ptsHIcrrEvo01,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04ptsHIcrrEvo02,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04ptsHIcrrEvo03,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04ptsHIcrrEvo04,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo01,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo02,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo03,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo04,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo05,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo06,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo07,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgiEvo08'
analysis_ids_RNASequencing_str = 'ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gndEvo01,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gndEvo02,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gndEvo03,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCBEvo01,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCBEvo02,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCBEvo03,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo01,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo02,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo03,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiAEvo04,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo01,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo02,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo03,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrrEvo04,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo01,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo02,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo03,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo04,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo05,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo06,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo07,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgiEvo08'
analysis_ids_sampledFluxes_str = 'ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04gndEvo01,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04gndEvo02,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04gndEvo03,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04sdhCBEvo01,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04sdhCBEvo02,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04sdhCBEvo03,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04tpiAEvo01,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04tpiAEvo02,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04tpiAEvo03,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04tpiAEvo04,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04ptsHIcrrEvo01,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04ptsHIcrrEvo02,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04ptsHIcrrEvo03,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04ptsHIcrrEvo04,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo01,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo02,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo03,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo04,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo05,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo06,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo07,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgiEvo08'
analysis_ids = ','.join([analysis_ids_Metabolomics_str,
    analysis_ids_RNASequencing_str,
    analysis_ids_sampledFluxes_str]);

data_O = [];

patternMatch_I='novel +,\
overcompensation +,\
partially-restored +,\
pattern_match_description,\
reinforced +,\
restored fast +,\
unrestored +';

ccu = 'log2(FC),\
mmol*gDW-1*hr-1_FC-mean_normalized,\
umol*gDW-1_glog_normalized';

#optional_constraint_I = 'AND (correlation_coefficient > 0.88 OR correlation_coefficient < -0.88)';
optional_constraint_I = None;

correlation_coefficient_threshold_I = 0.88;

data_O = execute_regulationAggreementCorrelationPatterns(
    session,
    BioCyc2COBRA_regulationAndInteraction,
    met_ids_deformatted,
    cobra01_dep,
    analysis_ids,
    cgn=None,
    sna=None,
    patternMatch=patternMatch_I,
    ccu=ccu,
    distanceMeasure=None,
    table_name = "data_stage02_quantification_correlationPattern",
    optional_constraint_I=optional_constraint_I,
    pvalue_threshold_I=None,
    correlation_coefficient_threshold_I=correlation_coefficient_threshold_I,
    )    

iobase = base_exportData(data_O);
iobase.write_dict2json(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc2COBRA_regulationAndInteractionCorrelationPattern_data_O.json');
iobase.write_dict2csv(
    pg_settings.datadir_settings['workspace_data']+\
    '/_output/BioCyc2COBRA_regulationAndInteractionCorrelationPattern_data_O.csv');