import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_metabolomics_151001.ini';
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
sys.path.append(pg_settings.datadir_settings['drive']+'/genomeScale_MFA')
sys.path.append(pg_settings.datadir_settings['drive']+'/genomeScale_MFA_INCA')

#make the MFA table
from SBaaS_models.models_MFA_execute import models_MFA_execute
exMFA01 = models_MFA_execute(session,engine,pg_settings.datadir_settings);
#export the mode
ko_list = ['F6PA','F6PA_reverse','DHAPT','GLYCDx','DHAPT',
           'EX_acald_LPAREN_e_RPAREN_',
           'EX_etoh_LPAREN_e_RPAREN_',
           'EX_glyc_LPAREN_e_RPAREN_',
           'EX_glyclt_LPAREN_e_RPAREN_',
           'EX_lac_DASH_D_LPAREN_e_RPAREN_',
           'EX_pyr_LPAREN_e_RPAREN_',
          'EX_succ_LPAREN_e_RPAREN_']
exMFA01.export_model('150526_iDM2015',filename_I='150526_iDM2015.json',filetype_I='json',ko_list=ko_list)

#make the COBRA table
from SBaaS_models.models_COBRA_execute import models_COBRA_execute
exCOBRA01 = models_COBRA_execute(session,engine,pg_settings.datadir_settings);
#exCOBRA01.drop_models_COBRA();
exCOBRA01.initialize_models_COBRA();
exCOBRA01.make_modelFromRxnsAndMetsTables();
#exCOBRA01.reset_models_COBRA('ALEsKOs01_evo04tpiA_11');
#TODO: exCOBRA01.import_COBRA_add('data/tests/analysis_models/.csv');

##make the MASS table
#from SBaaS_models.models_MASS_execute import models_MASS_execute
#exMASS01 = models_MASS_execute(session,engine,pg_settings.datadir_settings);
#exMASS01.drop_models_MASS();
#exMASS01.initialize_models_MASS();
#exMASS01.reset_models_MASS('ALEsKOs01_evo04tpiA_11');
##TODO: exMASS01.import_MASS_add('data/tests/analysis_models/.csv');