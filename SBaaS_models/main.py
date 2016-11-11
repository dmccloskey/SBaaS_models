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

#hypergeomitric using model subsystems
analysis_ids = 'ALEsKOs01_Metabolomics_0_evo04_0_11_evo04gnd,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04pgi,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04ptsHIcrr,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04sdhCB,\
ALEsKOs01_Metabolomics_0_evo04_0_11_evo04tpiA,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04gnd,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04pgi,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04ptsHIcrr,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04sdhCB,\
ALEsKOs01_RNASequencing_0_evo04_0_11_evo04tpiA,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04gnd,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04pgi,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04ptsHIcrr,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04sdhCB,\
ALEsKOs01_sampledFluxes_0_evo04_0_11_evo04tpiA';
enrichment_method = 'hypergeometric';
test_description='hypergeometric';
pvalue_threshold=1e-3;
ccu1='umol*gDW-1_glog_normalized,log2(FC),\
geometricFC(mean),\
log2(FC)'
table_name = "data_stage02_quantification_pairWiseEnrichment"
data_1 = execute_sigPairWiseEnrichment(
    session,    
    analysis_ids,
    ccu1,
    enrichment_method = enrichment_method,
    test_description=test_description,
    pvalue_threshold=pvalue_threshold,
    table_name = table_name
    )