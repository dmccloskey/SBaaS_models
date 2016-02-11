from .models_COBRA_query import models_COBRA_query
from .models_COBRA_dependencies import models_COBRA_dependencies
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
class models_COBRA_io(models_COBRA_query,
                      models_COBRA_dependencies,
                    sbaas_template_io):
            
    def import_modelsLumpedRxns_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_modelsLumpedRxns(data.data);
        data.clear_data();

    def import_dataStage02PhysiologyModel_sbml(self, model_id_I, date_I, model_sbml):
        '''import physiology model from file'''
        dataStage02PhysiologyModelRxns_data = [];
        dataStage02PhysiologyModelMets_data = [];
        dataStage02PhysiologyModels_data,\
            dataStage02PhysiologyModelRxns_data,\
            dataStage02PhysiologyModelMets_data = self._parse_model_sbml(model_id_I, date_I, model_sbml)
        self.add_dataStage02PhysiologyModelMetabolites(dataStage02PhysiologyModelMets_data);
        self.add_dataStage02PhysiologyModelReactions(dataStage02PhysiologyModelRxns_data);
        self.add_dataStage02PhysiologyModels(dataStage02PhysiologyModels_data);

    def import_dataStage02PhysiologyModel_json(self, model_id_I, date_I, model_json):
        '''import physiology model from file'''
        dataStage02PhysiologyModelRxns_data = [];
        dataStage02PhysiologyModelMets_data = [];
        dataStage02PhysiologyModels_data,\
            dataStage02PhysiologyModelRxns_data,\
            dataStage02PhysiologyModelMets_data = self._parse_model_json(model_id_I, date_I, model_json)
        self.add_dataStage02PhysiologyModelMetabolites(dataStage02PhysiologyModelMets_data);
        self.add_dataStage02PhysiologyModelReactions(dataStage02PhysiologyModelRxns_data);
        self.add_dataStage02PhysiologyModels(dataStage02PhysiologyModels_data);

    def import_dataStage02PhysiologyModels_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage02PhysiologyModels(data.data);
        data.clear_data();

    def import_dataStage02PhysiologyModels_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage02PhysiologyModels(data.data);
        data.clear_data();

    def import_dataStage02PhysiologyModelReactions_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage02PhysiologyModelReactions(data.data);
        data.clear_data();

    def import_dataStage02PhysiologyModelReactions_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage02PhysiologyModelReactions(data.data);
        data.clear_data();

    def import_dataStage02PhysiologyModelMetabolites_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage02PhysiologyModelMetabolites(data.data);
        data.clear_data();

    def import_dataStage02PhysiologyModelMetabolites_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage02PhysiologyModelMetabolites(data.data);
        data.clear_data();
            
    def import_dataStage02PhysiologyModelPathways_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage02PhysiologyModelPathways(data.data);
        data.clear_data();

    def import_dataStage02PhysiologyModelPathways_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage02PhysiologyModelPathways(data.data);
        data.clear_data();