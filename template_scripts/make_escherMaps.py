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

#make the escherMaps table
from SBaaS_models.models_escherMaps_execute import models_escherMaps_execute
exescherMaps01 = models_escherMaps_execute(session,engine,pg_settings.datadir_settings);
exescherMaps01.drop_models_escherMaps();
exescherMaps01.initialize_models_escherMaps();
exescherMaps01.reset_models_escherMaps();
exescherMaps01.import_escherMaps_add('data/tests/analysis_models/150917_models_escherMaps.csv');
