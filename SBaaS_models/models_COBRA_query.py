#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .models_COBRA_postgresql_models import *
#dependencies
from .models_COBRA_dependencies import models_COBRA_dependencies

class models_COBRA_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage02_physiology_modelMetabolites':data_stage02_physiology_modelMetabolites,
            'data_stage02_physiology_modelReactions':data_stage02_physiology_modelReactions,
            'data_stage02_physiology_models':data_stage02_physiology_models,
            'data_stage02_physiology_modelPathways':data_stage02_physiology_modelPathways,

                        };
        self.set_supportedTables(tables_supported);
    def add_modelsLumpedRxns(self, data_I):
        '''add rows of models_lumpedRxns'''
        if data_I:
            for d in data_I:
                try:
                    data_add = models_lumpedRxns(d['lumped_id'],
                                d['lumped_date'],
                                d['lumped_description'],
                                d['rxn_id'],
                                d['reactions'],
                                d['stoichiometry']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage02PhysiologyModels(self, data_I):
        '''add rows of data_stage02_physiology_models'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_physiology_models(d['model_id'],
                        d['model_name'],
                        d['model_description'],
                            d['model_file'],
                            d['file_type'],
                        d['date']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage02PhysiologyModels(self,data_I):
        #Not yet tested
        '''update rows of data_stage02_physiology_models'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_physiology_models).filter(
                            data_stage02_physiology_models.id.like(d['id'])).update(
                            {'model_id':d['model_id'],
                            'model_name':d['model_name'],
                            'model_description':d['model_description'],
                            'file':d['model_file'],
                            'file_type':d['file_type'],
                            'date':d['date']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage02PhysiologyModelReactions(self, data_I):
        '''add rows of data_stage02_physiology_modelReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_physiology_modelReactions(d['model_id'],
                            d['rxn_id'],
                            d['rxn_name'],
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
                            d['reversibility'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage02PhysiologyModelReactions(self,data_I):
        #Not yet tested
        '''update rows of data_stage02_physiology_modelReactions'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_physiology_modelReactions).filter(
                            data_stage02_physiology_modelReactions.id.like(d['id'])).update(
                            {'model_id':d['model_id'],
                                'rxn_id':d['rxn_id'],
                                'rxn_name':d['rxn_name'],
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
                                'reversibility':d['reversibility'],
                                'used_':d['used_'],
                                'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage02PhysiologyModelMetabolites(self, data_I):
        '''add rows of data_stage02_physiology_modelMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_physiology_modelMetabolites(d['model_id'],
                        d['met_name'],
                        d['met_id'],
                        d['formula'],
                        d['charge'],
                        d['compartment'],
                        d['bound'],
                        d['constraint_sense'],
                        d['used_'],
                        d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage02PhysiologyModelMetabolites(self,data_I):
        '''update rows of data_stage02_physiology_modelMetabolites'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_physiology_modelMetabolites).filter(
                            data_stage02_physiology_modelMetabolites.id.like(d['id'])).update(
                            {'model_id':d['model_id'],
                                'met_name':d['met_name'],
                                'met_id':d['met_id'],
                                'formula':d['formula'],
                                'charge':d['charge'],
                                'compartment':d['compartment'],
                                'bound':d['bound'],
                                'constraint_sense':d['constraint_sense'],
                                'used_':d['used_'],
                                'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    # query row from data_stage02_physiology_models
    def get_row_modelID_dataStage02PhysiologyModels(self,model_id_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_physiology_models).filter(
                    data_stage02_physiology_models.model_id.like(model_id_I)).order_by(
                    data_stage02_physiology_models.model_id.asc()).all();
            rows_O = {};
            if len(data)>1:
                print('multiple rows retrieved!');
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

    #TODO: add in reaction and metabolite queries from MFA
    
    ## Query from data_stage02_physiology_modelReactions
    # query rows from data_stage02_physiology_modelReactions
    def get_rows_modelID_dataStage02PhysiologyModelReactions(self,model_id_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelReactions).filter(
                    data_stage02_physiology_modelReactions.model_id.like(model_id_I),
                    data_stage02_physiology_modelReactions.used_.is_(True)).order_by(
                    data_stage02_physiology_modelReactions.model_id.asc(),
                    data_stage02_physiology_modelReactions.rxn_id.asc()).all();
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
                            'reversibility':d.reversibility,
                            'used_':d.used_,
                            'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_modelIDAndRxnID_dataStage02PhysiologyModelReactions(self,model_id_I,rxn_id_I):
        '''Querry row by model_id and rxn_id that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelReactions).filter(
                    data_stage02_physiology_modelReactions.model_id.like(model_id_I),
                    data_stage02_physiology_modelReactions.rxn_id.like(rxn_id_I),
                    data_stage02_physiology_modelReactions.used_.is_(True)).order_by(
                    data_stage02_physiology_modelReactions.model_id.asc(),
                    data_stage02_physiology_modelReactions.rxn_id.asc()).all();
            row_O = {};
            if len(data)>1:
                print('more than 1 reaction found!');
            if data: 
                for d in data:
                    row_O = {'model_id':d.model_id,
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
                            'reversibility':d.reversibility,
                            'used_':d.used_,
                            'comment_':d.comment_};
            return row_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_modelIDAndOrderedLocusName_dataStage02PhysiologyModelReactions(self,model_id_I,ordered_locus_name_I):
        '''Query rows by model_id and ordered locus name that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelReactions).filter(
                    data_stage02_physiology_modelReactions.model_id.like(model_id_I),
                    data_stage02_physiology_modelReactions.genes.any(ordered_locus_name_I),
                    data_stage02_physiology_modelReactions.used_.is_(True)).order_by(
                    data_stage02_physiology_modelReactions.model_id.asc(),
                    data_stage02_physiology_modelReactions.rxn_id.asc()).all();
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
                            'reversibility':d.reversibility,
                            'used_':d.used_,
                            'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    # query genes from data_stage02_physiology_modelReactions
    def get_geneIDs_modelIDAndRxnID_dataStage02PhysiologyModelReactions(
        self,model_id_I,rxn_id_I):
        '''Querry genes by model_id and rxn_id that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelReactions.genes).filter(
                    data_stage02_physiology_modelReactions.model_id.like(model_id_I),
                    data_stage02_physiology_modelReactions.rxn_id.like(rxn_id_I),
                    data_stage02_physiology_modelReactions.used_.is_(True)).all();
            genes_all = [];
            genes_unique_O = [];
            if data: 
                for d in data:
                    genes_all.extend(d.genes);
                genes_unique_O = list(set(genes_all));
            return genes_unique_O;
        except SQLAlchemyError as e:
            print(e);
    # query metabolites from data_stage02_physiology_modelReactions
    def get_metIDs_modelID_dataStage02PhysiologyModelReactions(self,model_id_I):
        '''Querry metabolites by model_id that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelReactions.reactants_ids,
                    data_stage02_physiology_modelReactions.products_ids).filter(
                    data_stage02_physiology_modelReactions.model_id.like(model_id_I),
                    data_stage02_physiology_modelReactions.used_.is_(True)).all();
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
    # query reactions from data_stage02_physiology_modelReactions
    def get_rxnIDs_modelIDAndOrderedLocusName_dataStage02PhysiologyModelReactions(self,model_id_I,ordered_locus_name_I):
        '''Query rxn_ids by model_id and ordered locus name that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelReactions).filter(
                    data_stage02_physiology_modelReactions.model_id.like(model_id_I),
                    data_stage02_physiology_modelReactions.genes.any(ordered_locus_name_I),
                    data_stage02_physiology_modelReactions.used_.is_(True)).order_by(
                    data_stage02_physiology_modelReactions.model_id.asc(),
                    data_stage02_physiology_modelReactions.rxn_id.asc()).all();
            rxnIDs_O = [];
            if data: 
                for d in data:
                    rxnIDs_O.append(d.rxn_id);
            return rxnIDs_O;
        except SQLAlchemyError as e:
            print(e);
    def getGroup_subsystemsAndGenesAndCount_modelID_dataStage02PhysiologyModelReactions(
        self,model_id_I):
        '''Query unique subsystems, genes, and counts of genes in that subsystem by model_id
        '''
        try:
            data = self.session.query(data_stage02_physiology_modelReactions.genes,
                    data_stage02_physiology_modelReactions.subsystem).filter(
                    data_stage02_physiology_modelReactions.model_id.like(model_id_I),
                    data_stage02_physiology_modelReactions.used_.is_(True)).all();
            # roll-up the subsystem and genes into counts
            d_tmp = {};
            for d_cnt,d in enumerate(data):
                if d_cnt==0: d_tmp={};
                if not d.subsystem in d_tmp.keys():
                    d_tmp[d.subsystem]={};
                for g_cnt,g in enumerate(d.genes):
                    if not g in d_tmp[d.subsystem].keys():
                        d_tmp[d.subsystem][g]=0;
                    else:
                        d_tmp[d.subsystem][g]+=1;
            # roll-out the subsystem and genes and counts into rows
            rows_O = [];
            for k1,v1 in d_tmp.items():
                for k2,v2 in v1.items():
                    rows_O.append(
                        {'subsystem':k1,
                         'gene':k2,
                         'count':v2,
                        });
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def getGroup_subsystemsAndRxnIDAndCount_modelID_dataStage02PhysiologyModelReactions(self,model_id_I):
        '''Query unique subsystems, rxn_ids, and counts of rxn_ids in that subsystem by model_id
        '''
        try:
            data = self.session.query(data_stage02_physiology_modelReactions.rxn_id,
                    data_stage02_physiology_modelReactions.subsystem).filter(
                    data_stage02_physiology_modelReactions.model_id.like(model_id_I),
                    data_stage02_physiology_modelReactions.used_.is_(True)).all();
            # reformat with a default count=1
            # as all rxn_ids are unique
            rows_O = [{'subsystem':d.subsystem,'rxn_id':d.rxn_id,'count':1} for d in data];
            return rows_O;
        except SQLAlchemyError as e:
            print(e);  
    def getGroup_subsystemsAndMetIDAndCount_modelID_dataStage02PhysiologyModelReactions(
        self,model_id_I,deformat_metID_I = True):
        '''Query unique subsystems, met_ids, and counts of met_ids in that subsystem by model_id
        INPUT:
        model_id_I = str, model_id
        deformat_metID_I = boolean, remove formatting and compartment id
        '''
        dep = models_COBRA_dependencies();
        try:
            data = self.session.query(data_stage02_physiology_modelReactions.reactants_ids,
                    data_stage02_physiology_modelReactions.products_ids,
                    data_stage02_physiology_modelReactions.reactants_stoichiometry,
                    data_stage02_physiology_modelReactions.products_stoichiometry,
                    data_stage02_physiology_modelReactions.subsystem).filter(
                    data_stage02_physiology_modelReactions.model_id.like(model_id_I),
                    data_stage02_physiology_modelReactions.used_.is_(True)).all();
            # roll-up the subsystem and genes into counts
            d_tmp = {};
            for d_cnt,d in enumerate(data):
                if d_cnt==0: d_tmp={};
                if not d.subsystem in d_tmp.keys():
                    d_tmp[d.subsystem]={};
                for r_cnt,r in enumerate(d.reactants_ids):
                    if deformat_metID_I: r = dep.deformat_metid(r);
                    if not r in d_tmp[d.subsystem].keys():
                        d_tmp[d.subsystem][r]=0;
                    else:
                        d_tmp[d.subsystem][r]+=abs(d.reactants_stoichiometry[r_cnt]);
                for r_cnt,r in enumerate(d.products_ids):
                    if deformat_metID_I: r = dep.deformat_metid(r);
                    if not r in d_tmp[d.subsystem].keys():
                        d_tmp[d.subsystem][r]=0;
                    else:
                        d_tmp[d.subsystem][r]+=abs(d.products_stoichiometry[r_cnt]);
            # roll-out the subsystem and genes and counts into rows
            rows_O = [];
            for k1,v1 in d_tmp.items():
                for k2,v2 in v1.items():
                    rows_O.append(
                        {'subsystem':k1,
                         'met_id':k2,
                         'count':v2,
                        });
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    ## Query from data_stage02_physiology_modelMetabolites
    # query formula from data_stage02_physiology_modelMetabolites
    def get_formula_modelIDAndMetID_dataStage02PhysiologyModelMetabolites(self,model_id_I, met_id_I):
        '''Query formula by model_id and met_id that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelMetabolites.formula).filter(
                    data_stage02_physiology_modelMetabolites.model_id.like(model_id_I),
                    data_stage02_physiology_modelMetabolites.met_id.like(met_id_I),
                    data_stage02_physiology_modelMetabolites.used_.is_(True)).order_by(
                    data_stage02_physiology_modelMetabolites.model_id.asc(),
                    data_stage02_physiology_modelMetabolites.met_id.asc()).all();
            formula_O = None;
            if data: 
                for d in data:
                    formula_O=d.formula
            else:
                print("formula not found")
            return formula_O;
        except SQLAlchemyError as e:
            print(e);
    # query rows from data_stage02_physiology_modelMetabolites
    def get_rows_modelID_dataStage02PhysiologyModelMetabolites(self,model_id_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelMetabolites).filter(
                    data_stage02_physiology_modelMetabolites.model_id.like(model_id_I),
                    data_stage02_physiology_modelMetabolites.used_.is_(True)).order_by(
                    data_stage02_physiology_modelMetabolites.model_id.asc(),
                    data_stage02_physiology_modelMetabolites.met_id.asc()).all();
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
                            'used_':d.used_,
                            'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
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
                            'compartment':d.compartment,
                            'used_':d.used_,
                            'comment_':d.comment_};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    # query metabolites from data_stage02_physiology_modelMetabolites
    def get_metIDs_modelID_dataStage02PhysiologyModelMetabolites(self,model_id_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_physiology_modelMetabolites.met_id).filter(
                    data_stage02_physiology_modelMetabolites.model_id.like(model_id_I),
                    data_stage02_physiology_modelMetabolites.used_.is_(True)).order_by(
                    data_stage02_physiology_modelMetabolites.met_id.asc()).all();
            mets_O = [];
            if data: 
                for d in data:
                    mets_O.append(d.met_id);
            return mets_O;
        except SQLAlchemyError as e:
            print(e);

    ## Query data from data_stage02_physiology_modelPathways
    # query rows from data_stage02_physiology_modelPathways
    def get_rowsDict_modelID_dataStage02PhysiologyModelPathways(self,model_id_I):
        '''Query rows that are used from model pathways'''
        try:
            data = self.session.query(data_stage02_physiology_modelPathways).filter(
                    data_stage02_physiology_modelPathways.model_id.like(model_id_I),
                    data_stage02_physiology_modelPathways.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.pathway_id in rows_O:
                        print('duplicate pathway_ids found!');
                    else:
                        rows_O[d.pathway_id]={'reactions':d.reactions,
                            'stoichiometry':d.stoichiometry};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage02PhysiologyModelPathways(self, data_I):
        '''add rows of data_stage02_physiology_modelPathways'''
        if data_I:
            for d in data_I:
                try:
                    d['reactions'] = d['reactions'].replace(' ','');
                    d['reactions'] = d['reactions'].split(',');
                    d['stoichiometry'] = d['stoichiometry'].replace(' ','');
                    #d['stoichiometry'] = numpy.array(d['stoichiometry'].split(','));
                    d['stoichiometry'] = d['stoichiometry'].split(',');
                    d['stoichiometry'] = [float(x) for x in d['stoichiometry']];
                    data_add = data_stage02_physiology_modelPathways(
                        d['model_id'],
                        d['pathway_id'],
                        d['reactions'],
                        d['stoichiometry'],
                        d['used_'],
                        d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage02PhysiologyModelPathways(self,data_I):
        #Not yet tested
        '''update rows of data_stage02_physiology_modelPathways'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_physiology_modelPathways).filter(
                            data_stage02_physiology_modelPathways.id.like(d['id'])).update(
                            {
                            'model_id':d['model_id'],
                            'pathway_id':d['pathway_id'],
                            'reactions':d['reactions'],
                            'stoichiometry':d['stoichiometry'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_COBRA_models(self):
        try:
            data_stage02_physiology_modelReactions.__table__.drop(self.engine,True);
            data_stage02_physiology_modelMetabolites.__table__.drop(self.engine,True);
            data_stage02_physiology_modelPathways.__table__.drop(self.engine,True);
            data_stage02_physiology_models.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_COBRA_models_all(self,model_id_I = None):
        try:
            if model_id_I:
                reset = self.session.query(data_stage02_physiology_modelReactions).filter(data_stage02_physiology_modelReactions.model_id.like(model_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_physiology_models).filter(data_stage02_physiology_models.model_id.like(model_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_physiology_modelMetabolites).filter(data_stage02_physiology_modelMetabolites.model_id.like(model_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_physiology_modelPathways).filter(data_stage02_physiology_modelPathways.model_id.like(model_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_COBRA_models(self,model_id_I = None):
        try:
            if model_id_I:
                reset = self.session.query(data_stage02_physiology_modelReactions).filter(data_stage02_physiology_modelReactions.model_id.like(model_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_physiology_models).filter(data_stage02_physiology_models.model_id.like(model_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_physiology_modelMetabolites).filter(data_stage02_physiology_modelMetabolites.model_id.like(model_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_COBRA_models(self):
        try:
            data_stage02_physiology_models.__table__.create(self.engine,True);
            data_stage02_physiology_modelReactions.__table__.create(self.engine,True);
            data_stage02_physiology_modelMetabolites.__table__.create(self.engine,True);
            data_stage02_physiology_modelPathways.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
