#SBaaS
from .models_COBRA_query import models_COBRA_query
from .models_COBRA_dependencies import models_COBRA_dependencies
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
# Dependencies from cobra
from cobra.io.sbml import create_cobra_model_from_sbml_file, write_cobra_model_to_sbml_file
from cobra.io.json import load_json_model, save_json_model

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

    def export_modelFromTable(self,model_id_I,filename_I):
        '''export a cobra model
        INPUT:
        model_id_I = model id
        filename_I = filename
        '''
        
        # get the model
        cobra_model_sbml = {};
        cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id_I);
        if not cobra_model_sbml:
            print('model not found');
            return;
        if cobra_model_sbml['file_type'] == 'sbml':
            with open(filename_I,'w') as file:
                file.write(cobra_model_sbml['model_file']);
                file.close();
        elif cobra_model_sbml['file_type'] == 'json':
            with open(filename_I,'w') as file:
                file.write(cobra_model_sbml['model_file']);
                file.close();
        else:
            print('file_type not supported')

    def export_model(self,model_id_I,filename_I,filetype_I = 'sbml',ko_list=[],flux_dict={}):
        '''export a cobra model
        INPUT:
        model_id_I = model id
        filename_I = filename
        filetype_I = if specified, the model will be written to the desired filetype
                    default: model file in the database
        '''
        
        # get the model
        cobra_model_sbml = {};
        cobra_model_sbml = self.get_row_modelID_dataStage02IsotopomerModels(model_id_I);
        if not cobra_model_sbml:
            print('model not found');
            return;
        # load the model
        cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
        # Constrain the model
        self.constrain_modelModelVariables(cobra_model=cobra_model,ko_list=ko_list,flux_dict=flux_dict);
        # export the model
        if filetype_I == 'sbml':
            cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
            #export the model to sbml
            write_cobra_model_to_sbml_file(cobra_model,filename_I);
        elif filetype_I == 'json':
            cobra_model = self.writeAndLoad_modelTable(cobra_model_sbml);
            #export the model to json
            save_json_model(cobra_model,filename_I);
        else:
            print('file_type not supported')