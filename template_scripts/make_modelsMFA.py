import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_1.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_base')
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_models')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/calculate_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')

#make the MFA table
from SBaaS_models.models_MFA_execute import models_MFA_execute
exMFA01 = models_MFA_execute(session,engine,pg_settings.datadir_settings);
exMFA01.drop_models_MFA();
exMFA01.initialize_models_MFA();
exMFA01.reset_datastage02_isotopomer_models(model_id_I='150526_iDM2015');
exMFA01.reset_datastage02_isotopomer_mappings(mapping_id_I='full05');
#import model tables
exMFA01.import_data_stage02_isotopomer_models_add('data/tests/analysis_models/150917_models_MFA_models.csv');
exMFA01.import_data_stage02_isotopomer_modelReactions_add('data/tests/analysis_models/150917_models_MFA_modelReactions.csv');
exMFA01.import_data_stage02_isotopomer_modelMetabolites_add('data/tests/analysis_models/150917_models_MFA_modelMetabolites.csv');
exMFA01.import_data_stage02_isotopomer_atomMappingReactions_add('data/tests/analysis_models/150917_models_MFA_atomMappingReactions.csv');
exMFA01.import_data_stage02_isotopomer_atomMappingMetabolites_add('data/tests/analysis_models/150917_models_MFA_atomMappingMetabolites.csv');
#build the model from the rxns and mets table
exMFA01.make_modelFromRxnsAndMetsTables(
    model_id_I='150526_iDM2015',
    model_id_O='150526_iDM2015',
    date_O='150526',
    ko_list=[],
    flux_dict={},
    description=None);

#TODO: example of making MFA model using genomeScale_MFA_model