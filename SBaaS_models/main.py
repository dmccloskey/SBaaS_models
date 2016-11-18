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

#iobase = base_importData();
#iobase.read_csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/ALEsKOs01_shortestPaths/ALEsKOs01_0_11_metaboliteCategories.csv');
#metaboliteCategories = iobase.data 

#metaboliteCategoriesCounts = count_metaboliteCategoryAgreementCorrelationPatterns(
#    metaboliteCategories)

#iobase = base_exportData(metaboliteCategoriesCounts);
#iobase.write_dict2csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/ALEsKOs01_0_11_metaboliteCategoriesCounts.csv');

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

sigMets,sigExpression,sigFluxes = execute_getSignificantComponents(
    session,
    analysis_ids_Metabolomics_str,
    analysis_ids_RNASequencing_str,
    analysis_ids_sampledFluxes_str
    )
sigComponents = {};
sigComponents.update(sigMets);
sigComponents.update(sigExpression);
sigComponents.update(sigFluxes);

filename_I = pg_settings.datadir_settings['workspace_data']+\
    '/ALEsKOs01_impFeats/ALEsKOs01_0_11_correlationPatterns.csv'
    
iobase = base_importData();
iobase.read_csv(filename_I);
analysis_table_I = iobase.data;

analysis_table_I = [row for row in analysis_table_I if 'Metabolomics' in row['analysis_id']]

#ref vs KO and KO vs EP for each lineage
#pvalue_I = 0.05;
pvalue_I = None;
correlation_coefficient_I = 0.88;

data1 = execute_sigPairWiseAgreementCorrelationPatterns(
    session,
    analysis_table_I,
    pvalue_I=pvalue_I,
    correlation_coefficient_I=correlation_coefficient_I,
    sigComponents_I=sigComponents,
    redundancy_I=True)



#iobase = base_importData();
#iobase.read_json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/BioCyc2COBRA_regulationAndInteractionCorrelationPattern_data_O.json');
#data_O = iobase.data;

#dataSummary_O = count_regulationAgreementCorrelation(
#    data_O,
#    pvalue_threshold = None,
#    correlation_coefficient_threshold = None)



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

