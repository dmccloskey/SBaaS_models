from .models_MFA_postgresql_models import *
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class models_MFA_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage02_isotopomer_modelMetabolites':data_stage02_isotopomer_modelMetabolites,
            'data_stage02_isotopomer_modelReactions':data_stage02_isotopomer_modelReactions,
            'data_stage02_isotopomer_models':data_stage02_isotopomer_models,
            'data_stage02_isotopomer_atomMappingMetabolites':data_stage02_isotopomer_atomMappingMetabolites,
            'data_stage02_isotopomer_atomMappingReactions':data_stage02_isotopomer_atomMappingReactions,
                        };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage02_isotopomer_modelReactions
    # query rows from data_stage02_isotopomer_modelReactions
    def get_rows_modelID_dataStage02IsotopomerModelReactions(self,model_id_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_modelReactions).filter(
                    data_stage02_isotopomer_modelReactions.model_id.like(model_id_I),
                    data_stage02_isotopomer_modelReactions.used_.is_(True)).order_by(
                    data_stage02_isotopomer_modelReactions.model_id.asc(),
                    data_stage02_isotopomer_modelReactions.rxn_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'model_id':d.model_id,
                            'rxn_id':d.rxn_id,
                            'equation':d.equation,
                            'subsystem':d.subsystem,
                            'gpr':d.gpr,
                            'genes':d.genes,
                            'reactants_stoichiometry':d.reactants_stoichiometry,
                            'products_stoichiometry':d.products_stoichiometry,
                            'reactants_ids':d.reactants_ids,
                            'products_ids':d.products_ids,
                            'lower_bound':d.lower_bound,
                            'upper_bound':d.upper_bound,
                            'objective_coefficient':d.objective_coefficient,
                            'flux_units':d.flux_units,
                            'fixed':d.fixed,
                            'free':d.free,
                            'reversibility':d.reversibility,
                            'weight':d.weight,
                            'used_':d.used_,
                            'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    # query metabolites from data_stage02_isotopomer_modelReactions
    def get_metIDs_modelID_dataStage02IsotopomerModelReactions(self,model_id_I):
        '''Querry metabolites by model_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_modelReactions.reactants_ids,
                    data_stage02_isotopomer_modelReactions.products_ids).filter(
                    data_stage02_isotopomer_modelReactions.model_id.like(model_id_I),
                    data_stage02_isotopomer_modelReactions.used_.is_(True)).all();
            mets_all = [];
            mets_unique_O = [];
            if data: 
                for d in data:
                    mets_all.extend(d.reactants_ids);
                    mets_all.extend(d.products_ids);
                mets_unique_O = list(set(mets_all));
            return mets_unique_O;
        except SQLAlchemyError as e:
            print(e);
    ## Query from data_stage02_isotopomer_atomMappingReactions
    # query rxn_ids from data_stage02_isotopomer_atomMappingReactions
    def get_rxnIDs_mappingID_dataStage02IsotopomerAtomMappingReactions(self,mapping_id_I):
        '''Querry rows by mapping_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_atomMappingReactions.rxn_id).filter(
                    data_stage02_isotopomer_atomMappingReactions.mapping_id.like(mapping_id_I),
                    data_stage02_isotopomer_atomMappingReactions.used_.is_(True)).order_by(
                    data_stage02_isotopomer_atomMappingReactions.rxn_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    rows_O.append(d.rxn_id);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    # query rows from data_stage02_isotopomer_atomMappingReactions
    def get_rows_mappingID_dataStage02IsotopomerAtomMappingReactions(self,mapping_id_I):
        '''Querry rows by mapping_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_atomMappingReactions).filter(
                    data_stage02_isotopomer_atomMappingReactions.mapping_id.like(mapping_id_I),
                    data_stage02_isotopomer_atomMappingReactions.used_.is_(True)).order_by(
                    data_stage02_isotopomer_atomMappingReactions.mapping_id.asc(),
                    data_stage02_isotopomer_atomMappingReactions.rxn_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'mapping_id':d.mapping_id,
                            'rxn_id':d.rxn_id,
                            'rxn_description':d.rxn_description,
                            'reactants_stoichiometry_tracked':d.reactants_stoichiometry_tracked,
                            'products_stoichiometry_tracked':d.products_stoichiometry_tracked,
                            'reactants_ids_tracked':d.reactants_ids_tracked,
                            'products_ids_tracked':d.products_ids_tracked,
                            'reactants_elements_tracked':d.reactants_elements_tracked,
                            'products_elements_tracked':d.products_elements_tracked,
                            'reactants_positions_tracked':d.reactants_positions_tracked,
                            'products_positions_tracked':d.products_positions_tracked,
                            'reactants_mapping':d.reactants_mapping,
                            'products_mapping':d.products_mapping,
                            'rxn_equation':d.rxn_equation,
                            'used_':d.used_,
                            'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_mappingIDAndRxnID_dataStage02IsotopomerAtomMappingReactions(self,mapping_id_I,rxn_id_I):
        '''Querry rows by mapping_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_atomMappingReactions).filter(
                    data_stage02_isotopomer_atomMappingReactions.rxn_id.like(rxn_id_I),
                    data_stage02_isotopomer_atomMappingReactions.mapping_id.like(mapping_id_I),
                    data_stage02_isotopomer_atomMappingReactions.used_.is_(True)).order_by(
                    data_stage02_isotopomer_atomMappingReactions.mapping_id.asc(),
                    data_stage02_isotopomer_atomMappingReactions.rxn_id.asc()).all();
            row_O = {};
            if data: 
                for d in data:
                    row_tmp = {'mapping_id':d.mapping_id,
                            'rxn_id':d.rxn_id,
                            'rxn_description':d.rxn_description,
                            'reactants_stoichiometry_tracked':d.reactants_stoichiometry_tracked,
                            'products_stoichiometry_tracked':d.products_stoichiometry_tracked,
                            'reactants_ids_tracked':d.reactants_ids_tracked,
                            'products_ids_tracked':d.products_ids_tracked,
                            'reactants_elements_tracked':d.reactants_elements_tracked,
                            'products_elements_tracked':d.products_elements_tracked,
                            'reactants_positions_tracked':d.reactants_positions_tracked,
                            'products_positions_tracked':d.products_positions_tracked,
                            'reactants_mapping':d.reactants_mapping,
                            'products_mapping':d.products_mapping,
                            'rxn_equation':d.rxn_equation,
                            'used_':d.used_,
                            'comment_':d.comment_};
                    row_O.update(row_tmp);
            return row_O;
        except SQLAlchemyError as e:
            print(e);
    def get_atomMappingMetabolites_mappingID_dataStage02IsotopomerAtomMappingReactions(self,mapping_id_I):
        '''Querry rows by mapping_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_atomMappingReactions).filter(
                data_stage02_isotopomer_atomMappingReactions.mapping_id.like(mapping_id_I),
                data_stage02_isotopomer_atomMappingReactions.used_.is_(True)).all();
            data_O = []
            if data:
                for i,d in enumerate(data):
                    if d.reactants_ids_tracked:
                        for reactant_cnt,reactant in enumerate(d.reactants_ids_tracked):
                            print(d.mapping_id,d.rxn_id,reactant)
                            if len(d.reactants_elements_tracked)!=len(d.reactants_ids_tracked):
                                print('reactants tracked do not match the elements tracked')
                                input("Press enter to continue")
                            if len(d.reactants_positions_tracked)!=len(d.reactants_ids_tracked):
                                print('reactants tracked do not match the positions tracked')
                                input("Press enter to continue")
                            if len(d.reactants_stoichiometry_tracked)!=len(d.reactants_ids_tracked):
                                print('reactants tracked do not match the stoichiometry tracked')
                                input("Press enter to continue")
                            data_O.append({
                                    'mapping_id':d.mapping_id,
                                    #'met_name':self.met_name,
                                    'met_id':reactant,
                                    #'formula':self.formula,
                                    'met_elements':d.reactants_elements_tracked[reactant_cnt],
                                    'met_atompositions':d.reactants_positions_tracked[reactant_cnt],
                                    'met_symmetry_elements':None,
                                    'met_symmetry_atompositions':None,
                                    'used_':True,
                                    'comment_':None,
                                    'met_mapping':None,
                                    'base_met_ids':None,
                                    'base_met_elements':None,
                                    'base_met_atompositions':None,
                                    'base_met_symmetry_elements':None,
                                    'base_met_symmetry_atompositions':None,
                                    'base_met_indices':None})
                    if d.products_ids_tracked:
                        for product_cnt,product in enumerate(d.products_ids_tracked):
                            print(d.mapping_id,d.rxn_id,product)
                            if len(d.products_elements_tracked)!=len(d.products_ids_tracked):
                                print('products tracked do not match the elements tracked')
                                input("Press enter to continue")
                            if len(d.products_positions_tracked)!=len(d.products_ids_tracked):
                                print('products tracked do not match the positions tracked')
                                input("Press enter to continue")
                            if len(d.products_stoichiometry_tracked)!=len(d.products_ids_tracked):
                                print('products tracked do not match the stoichiometry tracked')
                                input("Press enter to continue")
                            data_O.append({
                                    'mapping_id':d.mapping_id,
                                    #'met_name':self.met_name,
                                    'met_id':product,
                                    #'formula':self.formula,
                                    'met_elements':d.products_elements_tracked[product_cnt],
                                    'met_atompositions':d.products_positions_tracked[product_cnt],
                                    'met_symmetry_elements':None,
                                    'met_symmetry_atompositions':None,
                                    'used_':True,
                                    'comment_':None,
                                    'met_mapping':None,
                                    'base_met_ids':None,
                                    'base_met_elements':None,
                                    'base_met_atompositions':None,
                                    'base_met_symmetry_elements':None,
                                    'base_met_symmetry_atompositions':None,
                                    'base_met_indices':None})
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_atomMappingMetabolites_mappingID_dataStage02IsotopomerAtomMappingReactionsAndAtomMappingMetabolites(self,mapping_id_rxns_I,mapping_id_mets_I):
        '''Querry rows by mapping_id that are used;
        NOTE: the mapping id matches the reaction mapping id'''
        try:
            data_O = [];
            #1. get the atom mapping metabolites already in the database
            data=None;
            data = self.session.query(data_stage02_isotopomer_atomMappingMetabolites).filter(
                data_stage02_isotopomer_atomMappingMetabolites.mapping_id.like(mapping_id_mets_I),
                data_stage02_isotopomer_atomMappingMetabolites.used_.is_(True)).all();
            if data:
                for d in data:
                    data_O.append({
                            'mapping_id':mapping_id_rxns_I, #d.mapping_id,
                            #'met_name':self.met_name,
                            'met_id':d.met_id,
                            #'formula':self.formula,
                            'met_elements':d.met_elements,
                            'met_atompositions':d.met_atompositions,
                            'met_symmetry_elements':d.met_symmetry_elements,
                            'met_symmetry_atompositions':d.met_symmetry_atompositions,
                            'used_':True,
                            'comment_':None,
                            'met_mapping':d.met_mapping,
                            'base_met_ids':d.base_met_ids,
                            'base_met_elements':d.base_met_elements,
                            'base_met_atompositions':d.base_met_atompositions,
                            'base_met_symmetry_elements':d.base_met_symmetry_elements,
                            'base_met_symmetry_atompositions':d.base_met_symmetry_atompositions,
                            'base_met_indices':d.base_met_indices})

            #2. get the atom mapping metabolites from the reactions
            data=None;
            data = self.session.query(data_stage02_isotopomer_atomMappingReactions).filter(
                data_stage02_isotopomer_atomMappingReactions.mapping_id.like(mapping_id_rxns_I),
                data_stage02_isotopomer_atomMappingReactions.used_.is_(True)).all();
            if data:
                for i,d in enumerate(data):
                    if d.reactants_ids_tracked:
                        for reactant_cnt,reactant in enumerate(d.reactants_ids_tracked):
                            print(d.mapping_id,d.rxn_id,reactant)
                            if len(d.reactants_elements_tracked)!=len(d.reactants_ids_tracked):
                                print('reactants tracked do not match the elements tracked')
                                input("Press enter to continue")
                            if len(d.reactants_positions_tracked)!=len(d.reactants_ids_tracked):
                                print('reactants tracked do not match the positions tracked')
                                input("Press enter to continue")
                            if len(d.reactants_stoichiometry_tracked)!=len(d.reactants_ids_tracked):
                                print('reactants tracked do not match the stoichiometry tracked')
                                input("Press enter to continue")
                            data_O.append({
                                    'mapping_id':d.mapping_id,
                                    #'met_name':self.met_name,
                                    'met_id':reactant,
                                    #'formula':self.formula,
                                    'met_elements':d.reactants_elements_tracked[reactant_cnt],
                                    'met_atompositions':d.reactants_positions_tracked[reactant_cnt],
                                    'met_symmetry_elements':None,
                                    'met_symmetry_atompositions':None,
                                    'used_':True,
                                    'comment_':None,
                                    'met_mapping':None,
                                    'base_met_ids':None,
                                    'base_met_elements':None,
                                    'base_met_atompositions':None,
                                    'base_met_symmetry_elements':None,
                                    'base_met_symmetry_atompositions':None,
                                    'base_met_indices':None})
                    if d.products_ids_tracked:
                        for product_cnt,product in enumerate(d.products_ids_tracked):
                            print(d.mapping_id,d.rxn_id,product)
                            if len(d.products_elements_tracked)!=len(d.products_ids_tracked):
                                print('products tracked do not match the elements tracked')
                                input("Press enter to continue")
                            if len(d.products_positions_tracked)!=len(d.products_ids_tracked):
                                print('products tracked do not match the positions tracked')
                                input("Press enter to continue")
                            if len(d.products_stoichiometry_tracked)!=len(d.products_ids_tracked):
                                print('products tracked do not match the stoichiometry tracked')
                                input("Press enter to continue")
                            data_O.append({
                                    'mapping_id':d.mapping_id,
                                    #'met_name':self.met_name,
                                    'met_id':product,
                                    #'formula':self.formula,
                                    'met_elements':d.products_elements_tracked[product_cnt],
                                    'met_atompositions':d.products_positions_tracked[product_cnt],
                                    'met_symmetry_elements':None,
                                    'met_symmetry_atompositions':None,
                                    'used_':True,
                                    'comment_':None,
                                    'met_mapping':None,
                                    'base_met_ids':None,
                                    'base_met_elements':None,
                                    'base_met_atompositions':None,
                                    'base_met_symmetry_elements':None,
                                    'base_met_symmetry_atompositions':None,
                                    'base_met_indices':None})
            return data_O; #may contain duplicates
        except SQLAlchemyError as e:
            print(e);
    # update rows from data_stage02_isotopomer_modelReactions and data_stage02_isotopomer_atomMappingReactions
    def update_rows_dataStage02IsotopomerAtomMappingReactions(self,data_I):
        '''update rows of data_stage02_isotopomer_atomMappingReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_atomMappingReactions).filter(
                            data_stage02_isotopomer_atomMappingReactions.mapping_id.like(d['mapping_id']),
                            data_stage02_isotopomer_atomMappingReactions.rxn_id.like(d['rxn_id'])
                            ).update(
                            {
                            'rxn_description':d['rxn_description'],
                            'reactants_stoichiometry_tracked':d['reactants_stoichiometry_tracked'],
                            'products_stoichiometry_tracked':d['products_stoichiometry_tracked'],
                            'reactants_ids_tracked':d['reactants_ids_tracked'],
                            'products_ids_tracked':d['products_ids_tracked'],
                            'reactants_elements_tracked':d['reactants_elements_tracked'],
                            'products_elements_tracked':d['products_elements_tracked'],
                            'reactants_positions_tracked':d['reactants_positions_tracked'],
                            'products_positions_tracked':d['products_positions_tracked'],
                            'reactants_mapping':d['reactants_mapping'],
                            'products_mapping':d['products_mapping'],
                            'rxn_equation':d['rxn_equation'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # delete rows from data_stage02_isotopomer_atomMappingReactions
    def delete_rows_mappingID_dataStage02IsotopomerAtomMappingReactions(self,mapping_id_I):
        '''Delete rows by mapping_id that are not used'''
        try:
            data = self.session.query(data_stage02_isotopomer_atomMappingReactions).filter(
                    data_stage02_isotopomer_atomMappingReactions.mapping_id.like(mapping_id_I),
                    data_stage02_isotopomer_atomMappingReactions.used_.is_(False)).delete(synchronize_session=False);
            if data:
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    # add rows to data_stage02_isotopomer_atomMappingReactions
    def add_data_dataStage02IsotopomerAtomMappingReactions(self, data_I):
        '''add rows of data_stage02_isotopomer_atomMappingReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_atomMappingReactions(
                                d['mapping_id'],
                                d['rxn_id'],
                                d['rxn_description'],
                                d['reactants_stoichiometry_tracked'],
                                d['products_stoichiometry_tracked'],
                                d['reactants_ids_tracked'],
                                d['products_ids_tracked'],
                                d['reactants_elements_tracked'],
                                d['products_elements_tracked'],
                                d['reactants_positions_tracked'],
                                d['products_positions_tracked'],
                                d['reactants_mapping'],
                                d['products_mapping'],
                                d['rxn_equation'],
                                d['used_'],
                                d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    ## Query from data_stage02_isotopomer_modelReactions and data_stage02_isotopomer_atomMappingReactions
    # query rows from data_stage02_isotopomer_modelReactions and data_stage02_isotopomer_atomMappingReactions
    def get_join_modelIDAndMappingID_dataStage02IsotopomerModelReactionsAndAtomMapping(self,model_id_I,mapping_id_I):
        '''Querry join by model_id and mapping_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_modelReactions.model_id,
                    data_stage02_isotopomer_modelReactions.rxn_id,
                    data_stage02_isotopomer_modelReactions.equation,
                    data_stage02_isotopomer_modelReactions.subsystem,
                    data_stage02_isotopomer_modelReactions.gpr,
                    data_stage02_isotopomer_modelReactions.genes,
                    data_stage02_isotopomer_modelReactions.reactants_stoichiometry,
                    data_stage02_isotopomer_modelReactions.products_stoichiometry,
                    data_stage02_isotopomer_modelReactions.reactants_ids,
                    data_stage02_isotopomer_modelReactions.products_ids,
                    data_stage02_isotopomer_modelReactions.lower_bound,
                    data_stage02_isotopomer_modelReactions.upper_bound,
                    data_stage02_isotopomer_modelReactions.objective_coefficient,
                    data_stage02_isotopomer_modelReactions.flux_units,
                    data_stage02_isotopomer_modelReactions.fixed,
                    data_stage02_isotopomer_modelReactions.free,
                    data_stage02_isotopomer_modelReactions.reversibility,
                    data_stage02_isotopomer_modelReactions.weight,
                    data_stage02_isotopomer_atomMappingReactions.mapping_id,
                    data_stage02_isotopomer_atomMappingReactions.rxn_description,
                    data_stage02_isotopomer_atomMappingReactions.reactants_stoichiometry_tracked,
                    data_stage02_isotopomer_atomMappingReactions.products_stoichiometry_tracked,
                    data_stage02_isotopomer_atomMappingReactions.reactants_ids_tracked,
                    data_stage02_isotopomer_atomMappingReactions.products_ids_tracked,
                    data_stage02_isotopomer_atomMappingReactions.reactants_elements_tracked,
                    data_stage02_isotopomer_atomMappingReactions.products_elements_tracked,
                    data_stage02_isotopomer_atomMappingReactions.reactants_positions_tracked,
                    data_stage02_isotopomer_atomMappingReactions.products_positions_tracked,
                    data_stage02_isotopomer_atomMappingReactions.reactants_mapping,
                    data_stage02_isotopomer_atomMappingReactions.products_mapping,
                    data_stage02_isotopomer_atomMappingReactions.rxn_equation).filter(
                    data_stage02_isotopomer_modelReactions.model_id.like(model_id_I),
                    data_stage02_isotopomer_modelReactions.used_.is_(True),
                    data_stage02_isotopomer_atomMappingReactions.mapping_id.like(mapping_id_I),
                    data_stage02_isotopomer_atomMappingReactions.used_.is_(True),
                    data_stage02_isotopomer_modelReactions.rxn_id.like(data_stage02_isotopomer_atomMappingReactions.rxn_id)).group_by(
                    data_stage02_isotopomer_modelReactions.model_id,
                    data_stage02_isotopomer_modelReactions.rxn_id,
                    data_stage02_isotopomer_modelReactions.equation,
                    data_stage02_isotopomer_modelReactions.subsystem,
                    data_stage02_isotopomer_modelReactions.gpr,
                    data_stage02_isotopomer_modelReactions.genes,
                    data_stage02_isotopomer_modelReactions.reactants_stoichiometry,
                    data_stage02_isotopomer_modelReactions.products_stoichiometry,
                    data_stage02_isotopomer_modelReactions.reactants_ids,
                    data_stage02_isotopomer_modelReactions.products_ids,
                    data_stage02_isotopomer_modelReactions.lower_bound,
                    data_stage02_isotopomer_modelReactions.upper_bound,
                    data_stage02_isotopomer_modelReactions.objective_coefficient,
                    data_stage02_isotopomer_modelReactions.flux_units,
                    data_stage02_isotopomer_modelReactions.fixed,
                    data_stage02_isotopomer_modelReactions.free,
                    data_stage02_isotopomer_modelReactions.reversibility,
                    data_stage02_isotopomer_modelReactions.weight,
                    data_stage02_isotopomer_atomMappingReactions.mapping_id,
                    data_stage02_isotopomer_atomMappingReactions.rxn_description,
                    data_stage02_isotopomer_atomMappingReactions.reactants_stoichiometry_tracked,
                    data_stage02_isotopomer_atomMappingReactions.products_stoichiometry_tracked,
                    data_stage02_isotopomer_atomMappingReactions.reactants_ids_tracked,
                    data_stage02_isotopomer_atomMappingReactions.products_ids_tracked,
                    data_stage02_isotopomer_atomMappingReactions.reactants_elements_tracked,
                    data_stage02_isotopomer_atomMappingReactions.products_elements_tracked,
                    data_stage02_isotopomer_atomMappingReactions.reactants_mapping,
                    data_stage02_isotopomer_atomMappingReactions.products_mapping,
                    data_stage02_isotopomer_atomMappingReactions.rxn_equation).order_by(
                    data_stage02_isotopomer_modelReactions.rxn_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'model_id':d.model_id,
                            'rxn_id':d.rxn_id,
                            'equation':d.equation,
                            'subsystem':d.subsystem,
                            'gpr':d.gpr,
                            'genes':d.genes,
                            'reactants_stoichiometry':d.reactants_stoichiometry,
                            'products_stoichiometry':d.products_stoichiometry,
                            'reactants_ids':d.reactants_ids,
                            'products_ids':d.products_ids,
                            'lower_bound':d.lower_bound,
                            'upper_bound':d.upper_bound,
                            'objective_coefficient':d.objective_coefficient,
                            'flux_units':d.flux_units,
                            'fixed':d.fixed,
                            'free':d.free,
                            'reversibility':d.reversibility,
                            'weight':d.weight,
                            'mapping_id':d.mapping_id,
                            'rxn_description':d.rxn_description,
                            'reactants_stoichiometry_tracked':d.reactants_stoichiometry_tracked,
                            'products_stoichiometry_tracked':d.products_stoichiometry_tracked,
                            'reactants_ids_tracked':d.reactants_ids_tracked,
                            'products_ids_tracked':d.products_ids_tracked,
                            'reactants_elements_tracked':d.reactants_elements_tracked,
                            'products_elements_tracked':d.products_elements_tracked,
                            'reactants_positions_tracked':d.reactants_positions_tracked,
                            'products_positions_tracked':d.products_positions_tracked,
                            'reactants_mapping':d.reactants_mapping,
                            'products_mapping':d.products_mapping,
                            'rxn_equation':d.rxn_equation};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
            
    ## Query from data_stage02_isotopomer_atomMappingMetabolites
    # query rows from data_stage02_isotopomer_atomMappingMetabolites
    def get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(self,mapping_id_I,met_id_I):
        '''Querry rows by mapping_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_atomMappingMetabolites).filter(
                    data_stage02_isotopomer_atomMappingMetabolites.met_id.like(met_id_I),
                    data_stage02_isotopomer_atomMappingMetabolites.mapping_id.like(mapping_id_I),
                    data_stage02_isotopomer_atomMappingMetabolites.used_.is_(True)).order_by(
                    data_stage02_isotopomer_atomMappingMetabolites.mapping_id.asc(),
                    data_stage02_isotopomer_atomMappingMetabolites.met_id.asc()).all();
            row_O = {};
            if data: 
                for d in data:
                    row_tmp = {'mapping_id':d.mapping_id,
                            'met_id':d.met_id,
                            'met_elements':d.met_elements,
                            'met_atompositions':d.met_atompositions,
                            'met_symmetry_elements':d.met_symmetry_elements,
                            'met_symmetry_atompositions':d.met_symmetry_atompositions,
                            'used_':d.used_,
                            'comment_':d.comment_,
                            'met_mapping':d.met_mapping,
                            'base_met_ids':d.base_met_ids,
                            'base_met_elements':d.base_met_elements,
                            'base_met_atompositions':d.base_met_atompositions,
                            'base_met_symmetry_elements':d.base_met_symmetry_elements,
                            'base_met_symmetry_atompositions':d.base_met_symmetry_atompositions,
                            'base_met_indices':d.base_met_indices};
                    row_O.update(row_tmp);
            return row_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_mappingID_dataStage02IsotopomerAtomMappingMetabolites(self,mapping_id_I):
        '''Querry rows by mapping_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_atomMappingMetabolites).filter(
                    data_stage02_isotopomer_atomMappingMetabolites.mapping_id.like(mapping_id_I),
                    data_stage02_isotopomer_atomMappingMetabolites.used_.is_(True)).order_by(
                    data_stage02_isotopomer_atomMappingMetabolites.mapping_id.asc(),
                    data_stage02_isotopomer_atomMappingMetabolites.met_id.asc()).all();
            row_O = [];
            if data: 
                for d in data:
                    row_tmp = {'mapping_id':d.mapping_id,
                            'met_id':d.met_id,
                            'met_elements':d.met_elements,
                            'met_atompositions':d.met_atompositions,
                            'met_symmetry_elements':d.met_symmetry_elements,
                            'met_symmetry_atompositions':d.met_symmetry_atompositions,
                            'used_':d.used_,
                            'comment_':d.comment_,
                            'met_mapping':d.met_mapping,
                            'base_met_ids':d.base_met_ids,
                            'base_met_elements':d.base_met_elements,
                            'base_met_atompositions':d.base_met_atompositions,
                            'base_met_symmetry_elements':d.base_met_symmetry_elements,
                            'base_met_symmetry_atompositions':d.base_met_symmetry_atompositions,
                            'base_met_indices':d.base_met_indices};
                    row_O.append(row_tmp);
            return row_O;
        except SQLAlchemyError as e:
            print(e);
    # update rows from data_stage02_isotopomer_atomMappingMetabolites
    def update_rows_dataStage02IsotopomerAtomMappingMetabolites(self,data_I):
        '''update rows of data_stage02_isotopomer_atomMappingMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_atomMappingMetabolites).filter(
                            data_stage02_isotopomer_atomMappingMetabolites.mapping_id.like(d['mapping_id']),
                            data_stage02_isotopomer_atomMappingMetabolites.met_id.like(d['met_id'])
                            ).update(
                            {'met_elements':d['met_elements'],
                            'met_atompositions':d['met_atompositions'],
                            'met_symmetry_elements':d['met_symmetry_elements'],
                            'met_symmetry_atompositions':d['met_symmetry_atompositions'],
                            'used_':d['used_'],
                            'comment_':d['comment_'],
                            'met_mapping':d['met_mapping'],
                            'base_met_ids':d['base_met_ids'],
                            'base_met_elements':d['base_met_elements'],
                            'base_met_atompositions':d['base_met_atompositions'],
                            'base_met_symmetry_elements':d['base_met_symmetry_elements'],
                            'base_met_symmetry_atompositions':d['base_met_symmetry_atompositions'],
                            'base_met_indices':d['base_met_indices']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # add rows to data_stage02_isotopomer_atomMappingMetabolites
    def add_data_dataStage02IsotopomerAtomMappingMetabolites(self, data_I):
        '''add rows of data_stage02_isotopomer_atomMappingMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_atomMappingMetabolites(
                                d['mapping_id'],
                                d['met_id'],
                                d['met_elements'],
                                d['met_atompositions'],
                                d['met_symmetry_elements'],
                                d['met_symmetry_atompositions'],
                                d['used_'],
                                d['comment_'],
                                d['met_mapping'],
                                d['base_met_ids'],
                                d['base_met_elements'],
                                d['base_met_atompositions'],
                                d['base_met_symmetry_elements'],
                                d['base_met_symmetry_atompositions'],
                                d['base_met_indices']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
            
    ## Query from data_stage02_isotopomer_modelMetabolites
    # query formula from data_stage02_isotopomer_modelMetabolites
    def get_formula_modelIDAndMetID_dataStage02IsotopomerModelMetabolites(self,model_id_I, met_id_I):
        '''Query formula by model_id and met_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_modelMetabolites.formula).filter(
                    data_stage02_isotopomer_modelMetabolites.model_id.like(model_id_I),
                    data_stage02_isotopomer_modelMetabolites.met_id.like(met_id_I),
                    data_stage02_isotopomer_modelMetabolites.used_.is_(True)).order_by(
                    data_stage02_isotopomer_modelMetabolites.model_id.asc(),
                    data_stage02_isotopomer_modelMetabolites.met_id.asc()).all();
            formula_O = None;
            if data: 
                for d in data:
                    formula_O=d.formula
            else:
                print("formula not found")
            return formula_O;
        except SQLAlchemyError as e:
            print(e);
    # query rows from data_stage02_isotopomer_modelMetabolites
    def get_rows_modelID_dataStage02IsotopomerModelMetabolites(self,model_id_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_modelMetabolites).filter(
                    data_stage02_isotopomer_modelMetabolites.model_id.like(model_id_I),
                    data_stage02_isotopomer_modelMetabolites.used_.is_(True)).order_by(
                    data_stage02_isotopomer_modelMetabolites.model_id.asc(),
                    data_stage02_isotopomer_modelMetabolites.met_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'model_id':d.model_id,
                            'met_name':d.met_name,
                            'met_id':d.met_id,
                            'formula':d.formula,
                            'charge':d.charge,
                            'bound':d.bound,
                            'constraint_sense':d.constraint_sense,
                            'compartment':d.compartment,
                            'lower_bound':d.lower_bound,
                            'upper_bound':d.upper_bound,
                            'balanced':d.balanced,
                            'fixed':d.fixed,
                            'used_':d.used_,
                            'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_modelIDAndMetID_dataStage02IsotopomerModelMetabolites(self,model_id_I,met_id_I):
        '''Query row by model_id and met_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_modelMetabolites).filter(
                    data_stage02_isotopomer_modelMetabolites.model_id.like(model_id_I),
                    data_stage02_isotopomer_modelMetabolites.met_id.like(met_id_I),
                    data_stage02_isotopomer_modelMetabolites.used_.is_(True)).order_by(
                    data_stage02_isotopomer_modelMetabolites.model_id.asc(),
                    data_stage02_isotopomer_modelMetabolites.met_id.asc()).all();
            rows_O = {};
            if len(data)>1:
                print('more than 1 model_id/met_id found!')
            if data: 
                for d in data:
                    rows_O = {'model_id':d.model_id,
                            'met_name':d.met_name,
                            'met_id':d.met_id,
                            'formula':d.formula,
                            'charge':d.charge,
                            'bound':d.bound,
                            'constraint_sense':d.constraint_sense,
                            'compartment':d.compartment,
                            'lower_bound':d.lower_bound,
                            'upper_bound':d.upper_bound,
                            'balanced':d.balanced,
                            'fixed':d.fixed,
                            'used_':d.used_,
                            'comment_':d.comment_};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    # query metabolites from data_stage02_isotopomer_modelMetabolites
    def get_metIDs_modelID_dataStage02IsotopomerModelMetabolites(self,model_id_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_modelMetabolites.met_id).filter(
                    data_stage02_isotopomer_modelMetabolites.model_id.like(model_id_I),
                    data_stage02_isotopomer_modelMetabolites.used_.is_(True)).order_by(
                    data_stage02_isotopomer_modelMetabolites.met_id.asc()).all();
            mets_O = [];
            if data: 
                for d in data:
                    mets_O.append(d.met_id);
            return mets_O;
        except SQLAlchemyError as e:
            print(e);

    ## Query from data_stage02_physiology_modelMetabolites
    # query rows from data_stage02_physiology_modelMetabolites
    def get_row_modelIDAndMetID_dataStage02PhysiologyModelMetabolites(self,model_id_I,met_id_I):
        '''Query row by model_id and met_id that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelMetabolites).filter(
                    data_stage02_physiology_modelMetabolites.model_id.like(model_id_I),
                    data_stage02_physiology_modelMetabolites.met_id.like(met_id_I),
                    data_stage02_physiology_modelMetabolites.used_.is_(True)).order_by(
                    data_stage02_physiology_modelMetabolites.model_id.asc(),
                    data_stage02_physiology_modelMetabolites.met_id.asc()).all();
            rows_O = {};
            if len(data)>1:
                print('more than 1 model_id/met_id found!')
            if data: 
                for d in data:
                    rows_O = {'model_id':d.model_id,
                            'met_name':d.met_name,
                            'met_id':d.met_id,
                            'formula':d.formula,
                            'charge':d.charge,
                            'bound':d.bound,
                            'constraint_sense':d.constraint_sense,
                            'compartment':d.compartment};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);      

    ## Query from data_stage02_isotopomer_models
    # query row from data_stage02_isotopomer_models
    def get_row_modelID_dataStage02IsotopomerModels(self,model_id_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_models).filter(
                    data_stage02_isotopomer_models.model_id.like(model_id_I)).order_by(
                    data_stage02_isotopomer_models.model_id.asc()).all();
            rows_O = {};
            if data: 
                for d in data:
                    row_tmp = {'model_id':d.model_id,
                                'model_name':d.model_name,
                                'model_description':d.model_description,
                                'model_file':d.model_file,
                                'file_type':d.file_type,
                                'date':d.date};
                    rows_O.update(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
            
    def add_data_stage02_isotopomer_models(self, data_I):
        '''add rows of data_stage02_isotopomer_models'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_models(d['model_id'],
                            d['model_name'],
                            d['model_description'],
                            d['model_file'],
                            d['file_type'],
                            d['date']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_modelReactions(self, data_I):
        '''add rows of data_stage02_isotopomer_modelReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_modelReactions(d['model_id'],
                                d['rxn_id'],
                                d['equation'],
                                d['subsystem'],
                                d['gpr'],
                                d['genes'],
                                d['reactants_stoichiometry'],
                                d['products_stoichiometry'],
                                d['reactants_ids'],
                                d['products_ids'],
                                d['lower_bound'],
                                d['upper_bound'],
                                d['objective_coefficient'],
                                d['flux_units'],
                                d['fixed'],
                                d['free'],
                                d['reversibility'],
                                d['weight'],
                                d['used_'],
                                d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_modelMetabolites(self, data_I):
        '''add rows of data_stage02_isotopomer_modelMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_modelMetabolites(d['model_id'],
                            d['met_name'],
                            d['met_id'],
                            d['formula'],
                            d['charge'],
                            d['compartment'],
                            d['bound'],
                            d['constraint_sense'],
                            d['lower_bound'],
                            d['upper_bound'],
                            d['balanced'],
                            d['fixed'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_atomMappingReactions(self, data_I):
        '''add rows of data_stage02_isotopomer_atomMappingReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_atomMappingReactions(
                                #d['id'],
                                d['mapping_id'],
                                d['rxn_id'],
                                d['rxn_description'],
                                d['reactants_stoichiometry_tracked'],
                                d['products_stoichiometry_tracked'],
                                d['reactants_ids_tracked'],
                                d['products_ids_tracked'],
                                d['reactants_elements_tracked'],
                                d['products_elements_tracked'],
                                d['reactants_positions_tracked'],
                                d['products_positions_tracked'],
                                d['reactants_mapping'],
                                d['products_mapping'],
                                d['rxn_equation'],
                                d['used_'],
                                d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_atomMappingMetabolites(self, data_I):
        '''add rows of data_stage02_isotopomer_atomMappingMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_atomMappingMetabolites(
                                #d['id'],
                                d['mapping_id'],
                                d['met_id'],
                                d['met_elements'],
                                d['met_atompositions'],
                                d['met_symmetry_elements'],
                                d['met_symmetry_atompositions'],
                                d['used_'],
                                d['comment_'],
                                d['met_mapping'],
                                d['base_met_ids'],
                                d['base_met_elements'],
                                d['base_met_atompositions'],
                                d['base_met_symmetry_elements'],
                                d['base_met_symmetry_atompositions'],
                                d['base_met_indices']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_models(self,data_I):
        '''update rows of data_stage02_isotopomer_models'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_models).filter(
                            data_stage02_isotopomer_models.model_id.like(d['model_id'])
                            ).update(
                            {
                                #'model_id':d['model_id'],
                            'model_name':d['model_name'],
                            'model_description':d['model_description'],
                            'model_file':d['model_file'],
                            'file_type':d['file_type'],
                            'date':d['date']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_modelReactions(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_modelReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_modelReactions).filter(
                            #sample.sample_name.like(d['sample_name'])
                            ).update(
                            {'model_id':d['model_id'],
                            'rxn_id':d['rxn_id'],
                            'equation':d['equation'],
                            'subsystem':d['subsystem'],
                            'gpr':d['gpr'],
                            'genes':d['genes'],
                            'reactants_stoichiometry':d['reactants_stoichiometry'],
                            'products_stoichiometry':d['products_stoichiometry'],
                            'reactants_ids':d['reactants_ids'],
                            'products_ids':d['products_ids'],
                            'lower_bound':d['lower_bound'],
                            'upper_bound':d['upper_bound'],
                            'objective_coefficient':d['objective_coefficient'],
                            'flux_units':d['flux_units'],
                            'fixed':d['fixed'],
                            'free':d['free'],
                            'reversibility':d['reversibility'],
                            'weight':d['weight'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_modelMetabolites(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_modelMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_modelMetabolites).filter(
                            #sample.sample_name.like(d['sample_name'])
                            ).update(
                            {'model_id':d['model_id'],
                            'met_name':d['met_name'],
                            'met_id':d['met_id'],
                            'formula':d['formula'],
                            'charge':d['charge'],
                            'compartment':d['compartment'],
                            'bound':d['bound'],
                            'constraint_sense':d['constraint_sense'],
                            'lower_bound':d['lower_bound'],
                            'upper_bound':d['upper_bound'],
                            'balanced':d['balanced'],
                            'fixed':d['fixed'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_atomMappingReactions(self,data_I):
        '''update rows of data_stage02_isotopomer_atomMappingReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_atomMappingReactions).filter(
                            data_stage02_isotopomer_atomMappingReactions.id == d['id']
                            ).update(
                            {'mapping_id':d['mapping_id'],
                            'rxn_id':d['rxn_id'],
                            'rxn_description':d['rxn_description'],
                            'reactants_stoichiometry_tracked':d['reactants_stoichiometry_tracked'],
                            'products_stoichiometry_tracked':d['products_stoichiometry_tracked'],
                            'reactants_ids_tracked':d['reactants_ids_tracked'],
                            'products_ids_tracked':d['products_ids_tracked'],
                            'reactants_elements_tracked':d['reactants_elements_tracked'],
                            'products_elements_tracked':d['products_elements_tracked'],
                            'reactants_positions_tracked':d['reactants_positions_tracked'],
                            'products_positions_tracked':d['products_positions_tracked'],
                            'reactants_mapping':d['reactants_mapping'],
                            'products_mapping':d['products_mapping'],
                            'rxn_equation':d['rxn_equation'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_atomMappingMetabolites(self,data_I):
        '''update rows of data_stage02_isotopomer_atomMappingMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_atomMappingMetabolites).filter(
                            data_stage02_isotopomer_atomMappingMetabolites.id == d['id']
                            ).update(
                            {'mapping_id':d['mapping_id'],
                            'met_id':d['met_id'],
                            'met_elements':d['met_elements'],
                            'met_atompositions':d['met_atompositions'],
                            'met_symmetry_elements':d['met_symmetry_elements'],
                            'met_symmetry_atompositions':d['met_symmetry_atompositions'],
                            'used_':d['used_'],
                            'comment_':d['comment_'],
                            'met_mapping':d['met_mapping'],
                            'base_met_ids':d['base_met_ids'],
                            'base_met_elements':d['base_met_elements'],
                            'base_met_atompositions':d['base_met_atompositions'],
                            'base_met_symmetry_elements':d['base_met_symmetry_elements'],
                            'base_met_symmetry_atompositions':d['base_met_symmetry_atompositions'],
                            'base_met_indices':d['base_met_indices']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def initialize_MFA_models(self):
        try:
            data_stage02_isotopomer_models.__table__.create(self.engine,True);
            data_stage02_isotopomer_modelMetabolites.__table__.create(self.engine,True);
            data_stage02_isotopomer_modelReactions.__table__.create(self.engine,True);
            data_stage02_isotopomer_atomMappingReactions.__table__.create(self.engine,True);
            data_stage02_isotopomer_atomMappingMetabolites.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_MFA_models(self):
        try:
            data_stage02_isotopomer_models.__table__.drop(self.engine,True);
            data_stage02_isotopomer_modelReactions.__table__.drop(self.engine,True);
            data_stage02_isotopomer_modelMetabolites.__table__.drop(self.engine,True);
            data_stage02_isotopomer_atomMappingReactions.__table__.drop(self.engine,True);
            data_stage02_isotopomer_atomMappingMetabolites.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage02_isotopomer_models(self,model_id_I = None):
        try:
            if model_id_I:
                reset = self.session.query(data_stage02_isotopomer_models).filter(data_stage02_isotopomer_models.model_id.like(model_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_modelMetabolites).filter(data_stage02_isotopomer_modelMetabolites.model_id.like(model_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_modelReactions).filter(data_stage02_isotopomer_modelReactions.model_id.like(model_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_models).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_modelMetabolites).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_modelReactions).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage02_isotopomer_modelReactions(self,model_id_I = None,rxn_ids_I=[]):
        try:
            if model_id_I and rxn_ids_I:
                for rxn_id in rxn_ids_I:
                    reset = self.session.query(data_stage02_isotopomer_modelReactions).filter(
                        data_stage02_isotopomer_modelReactions.model_id.like(model_id_I),
                        data_stage02_isotopomer_modelReactions.rxn_id.like(rxn_id)).delete(synchronize_session=False);
                    reset = self.session.query(data_stage02_isotopomer_atomMappingReactions).filter(
                        data_stage02_isotopomer_atomMappingReactions.model_id.like(model_id_I),
                        data_stage02_isotopomer_atomMappingReactions.rxn_id.like(rxn_id)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_modelReactions).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_atomMappingReactions).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage02_isotopomer_modelMetabolites(self,model_id_I = None,met_ids_I=[]):
        try:
            if model_id_I and met_ids_I:
                for met_id in met_ids_I:
                    reset = self.session.query(data_stage02_isotopomer_modelMetabolites).filter(
                        data_stage02_isotopomer_modelMetabolites.model_id.like(model_id_I),
                        data_stage02_isotopomer_modelMetabolites.met_id.like(met_id)).delete(synchronize_session=False);
                    reset = self.session.query(data_stage02_isotopomer_atomMappingMetabolites).filter(
                        data_stage02_isotopomer_atomMappingMetabolites.model_id.like(model_id_I),
                        data_stage02_isotopomer_atomMappingMetabolites.met_id.like(met_id)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_modelMetabolites).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_atomMappingMetabolites).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage02_isotopomer_mappings(self,mapping_id_I = None):
        try:
            if mapping_id_I:
                reset = self.session.query(data_stage02_isotopomer_atomMappingReactions).filter(data_stage02_isotopomer_atomMappingReactions.mapping_id.like(mapping_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_atomMappingMetabolites).filter(data_stage02_isotopomer_atomMappingMetabolites.mapping_id.like(mapping_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_atomMappingReactions).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_atomMappingMetabolites).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);