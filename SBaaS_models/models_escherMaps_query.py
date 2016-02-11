from .models_escherMaps_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class models_escherMaps_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'models_eschermaps':models_eschermaps,
                        };
        self.set_supportedTables(tables_supported);
    #table initializations:
    def drop_models_eschermaps(self):
        try:
            models_eschermaps.__table__.drop(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_models_eschermaps(self,eschermap_id_I = None):
        try:
            if eschermaps_id_I:
                reset = self.session.query(models_eschermaps).filter(models_eschermaps.eschermap_id.like(eschermap_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(models_eschermaps).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_models_eschermaps(self):
        try:
            models_eschermaps.__table__.create(engine,True);
        except SQLAlchemyError as e:
            print(e);
    def add_modelsEschermaps(self, data_I):
        '''add rows of models_eschermaps'''
        if data_I:
            for d in data_I:
                try:
                    data_add = models_eschermaps(
                                    d['used_'],
                                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_modelsEschermaps(self,data_I):
        '''update rows of models_eschermaps'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(models_eschermaps).filter(
                            models_eschermaps.id == d['id']).update(
                            {
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # query data from models_eschermaps
    def get_rows_eschermapID_modelsEschermaps(self,eschermap_id_I):
        '''Query rows that are used from the eschermaps'''
        try:
            data = self.session.query(models_eschermaps).filter(
                    models_eschermaps.eschermaps_id.like(eschermap_id_I),
                    models_eschermaps.used_.is_(True)).order_by(
                    models_eschermaps.eschermap_id.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append({
                        'model_id':d.model_id,
                        'eschermap_id':d.eschermap_id,
                        'eschermap_json':d.eschermap_json,
                        'used_':d.used_,
                        'comment_':d.comment_
                    });
            return  data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_modelID_modelsEschermaps(self,model_id_I):
        '''Query rows that are used from the eschermaps'''
        try:
            data = self.session.query(models_eschermaps).filter(
                    models_eschermaps.model_id.like(model_id_I),
                    models_eschermaps.used_.is_(True)).order_by(
                    models_eschermaps.eschermap_id.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append({
                        'model_id':d.model_id,
                        'eschermap_id':d.eschermap_id,
                        'eschermap_json':d.eschermap_json,
                        'used_':d.used_,
                        'comment_':d.comment_
                    });
            return  data_O;
        except SQLAlchemyError as e:
            print(e);