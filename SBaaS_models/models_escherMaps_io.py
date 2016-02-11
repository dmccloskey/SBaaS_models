
from .models_escherMaps_query import models_escherMaps_query
from SBaaS_base.sbaas_template_io import sbaas_template_io

class models_escherMaps_io(models_escherMaps_query,
                    sbaas_template_io):
    

    def import_modelsEschermaps_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_modelsEschermaps(data.data);
        data.clear_data();
        
    def import_modelsEschermaps_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_modelsEschermaps(data.data);
        data.clear_data();