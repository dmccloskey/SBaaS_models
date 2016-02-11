#sbaas
from SBaaS_base.postgresql_orm_base import *

class data_stage02_isotopomer_models(Base):
    __tablename__ = 'data_stage02_isotopomer_models'
    id = Column(Integer, Sequence('data_stage02_isotopomer_models_id_seq'), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    model_name = Column(String(100))
    model_description = Column(String(100))
    model_file = Column(Text)
    file_type = Column(String(50))
    date = Column(DateTime)

    def __init__(self,model_id_I,
            model_name_I,
            model_description_I,
            model_file_I,
            file_type_I,
            date_I):
        self.model_id=model_id_I
        self.model_name=model_name_I
        self.model_description=model_description_I
        self.model_file=model_file_I
        self.file_type=file_type_I
        self.date=date_I

    def __repr__dict__(self):
        return {'id':self.id,
                'model_id':self.model_id,
                'model_name':self.model_name,
                'model_description':self.model_description,
                'file':self.file,
                'file_type':self.file_type,
                'date':self.date}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_modelReactions(Base):
    __tablename__ = 'data_stage02_isotopomer_modelReactions'
    id = Column(Integer, Sequence('data_stage02_isotopomer_modelReactions_id_seq'), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    rxn_id = Column(String(50), primary_key=True)
    rxn_name = Column(String(100))
    equation = Column(String(4000));
    subsystem = Column(String(255));
    gpr = Column(Text);
    genes = Column(postgresql.ARRAY(String(50)));
    reactants_stoichiometry = Column(postgresql.ARRAY(Float)) # stoichiometry of metabolites
    products_stoichiometry = Column(postgresql.ARRAY(Float)) 
    reactants_ids = Column(postgresql.ARRAY(String(100))) # list of met_ids that are in the reaction
    products_ids = Column(postgresql.ARRAY(String(100))) 
    lower_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    upper_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    objective_coefficient = Column(Float)
    flux_units = Column(String(50))
    fixed = Column(Boolean)
    free = Column(Boolean)
    reversibility = Column(Boolean)
    weight = Column(Float) #weighting given in the optimization problem
    used_ = Column(Boolean)
    comment_ = Column(Text);

    def __init__(self,model_id_I,
            rxn_id_I,
            equation_I,
            subsystem_I,
            gpr_I,
            genes_I,
            reactants_stoichiometry_I,
            products_stoichiometry_I,
            reactants_ids_I,
            products_ids_I,
            lower_bound_I,
            upper_bound_I,
            objective_coefficient_I,
            flux_units_I,
            fixed_I,
            free_I,
            reversibility_I,
            weight_I,
            used__I,
            comment__I):
        self.model_id=model_id_I
        self.rxn_id=rxn_id_I
        self.equation=equation_I
        self.subsystem=subsystem_I
        self.gpr=gpr_I
        self.genes=genes_I
        self.reactants_stoichiometry=reactants_stoichiometry_I
        self.products_stoichiometry=products_stoichiometry_I
        self.reactants_ids=reactants_ids_I
        self.products_ids=products_ids_I
        self.lower_bound=lower_bound_I
        self.upper_bound=upper_bound_I
        self.objective_coefficient=objective_coefficient_I
        self.flux_units=flux_units_I
        self.fixed=fixed_I
        self.free=free_I
        self.reversibility=reversibility_I
        self.weight=weight_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'model_id':self.model_id,
            'rxn_id':self.rxn_id,
            'equation':self.equation,
            'subsystem':self.subsystem,
            'gpr':self.gpr,
            'genes':self.genes,
            'reactants_stoichiometry':self.reactants_stoichiometry,
            'products_stoichiometry':self.products_stoichiometry,
            'reactants_ids':self.reactants_ids,
            'products_ids':self.products_ids,
            'lower_bound':self.lower_bound,
            'upper_bound':self.upper_bound,
            'objective_coefficient':self.objective_coefficient,
            'flux_units':self.flux_units,
            'fixed':self.fixed,
            'free':self.free,
            'reversibility':self.reversibility,
            'weight':self.weight,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage02_isotopomer_modelMetabolites(Base):
    __tablename__ = 'data_stage02_isotopomer_modelMetabolites'
    id = Column(Integer, Sequence('data_stage02_isotopomer_modelMetabolites_id_seq'), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    met_name = Column(String(500))
    met_id = Column(String(100), primary_key=True)
    formula = Column(String(100))
    charge = Column(Integer)
    compartment = Column(String(50))
    bound = Column(Float)
    constraint_sense = Column(String(5))
    used_ = Column(Boolean)
    comment_ = Column(Text);
    lower_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    upper_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    balanced = Column(Boolean)
    fixed = Column(Boolean)

    def __init__(self,model_id_I,
            met_name_I,
            met_id_I,
            formula_I,
            charge_I,
            compartment_I,
            bound_I,
            constraint_sense_I,
            lower_bound_I,
            upper_bound_I,
            balanced_I,
            fixed_I,
            used__I,
            comment__I):
        self.model_id=model_id_I
        self.met_name=met_name_I
        self.met_id=met_id_I
        self.formula=formula_I
        self.charge=charge_I
        self.compartment=compartment_I
        self.bound=bound_I
        self.constraint_sense=constraint_sense_I
        self.lower_bound=lower_bound_I
        self.upper_bound=upper_bound_I
        self.balanced=balanced_I
        self.fixed=fixed_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'model_id':self.model_id,
                'met_name':self.met_name,
                'met_id':self.met_id,
                'formula':self.formula,
                'charge':self.charge,
                'bound':self.bound,
                'constraint_sense':self.constraint_sense,
                'compartment':self.compartment,
                'lower_bound':self.lower_bound,
                'upper_bound':self.upper_bound,
                'balanced':self.balanced,
                'fixed':self.fixed,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_atomMappingReactions(Base):
    __tablename__ = 'data_stage02_isotopomer_atomMappingReactions'
    id = Column(Integer, Sequence('data_stage02_isotopomer_atomMappingReactions_id_seq'), primary_key=True)
    mapping_id = Column(String(100), primary_key=True)
    rxn_id = Column(String(50), primary_key=True)
    rxn_description = Column(String(500))
    reactants_stoichiometry_tracked = Column(postgresql.ARRAY(Float)) # stoichiometry of metabolites (e.g. ['-1','-1'])
    products_stoichiometry_tracked = Column(postgresql.ARRAY(Float))  
    reactants_ids_tracked = Column(postgresql.ARRAY(String(100))) # list of met_ids that are tracked (e.g. ['pyr_c','accoa_c'])
    products_ids_tracked = Column(postgresql.ARRAY(String(100)))
    reactants_elements_tracked = Column(postgresql.JSON) # list of elements that are tracked (e.g. ['C','C'])
    products_elements_tracked = Column(postgresql.JSON)
    reactants_positions_tracked = Column(postgresql.JSON) # list of elements that are tracked (e.g. ['C','C'])
    products_positions_tracked = Column(postgresql.JSON)
    reactants_mapping = Column(postgresql.ARRAY(String(20000))) # mappings of each atom for each met_id that are tracked (e.g. ['abc','de'])
    products_mapping = Column(postgresql.ARRAY(String(20000)))
    rxn_equation = Column(String(5000)) #formatted version of rxn_formula and rxn_mapping depending on the fluxomics software
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self,
            #id_I,
            mapping_id_I,
            rxn_id_I,
            rxn_description_I,
            reactants_stoichiometry_tracked_I,
            products_stoichiometry_tracked_I,
            reactants_ids_tracked_I,
            products_ids_tracked_I,
            reactants_elements_tracked_I,
            products_elements_tracked_I,
            reactants_positions_tracked_I,
            products_positions_tracked_I,
            reactants_mapping_I,
            products_mapping_I,
            rxn_equation_I,
            used__I,
            comment__I):
        #self.id=id_I
        self.mapping_id=mapping_id_I
        self.rxn_id=rxn_id_I
        self.rxn_description=rxn_description_I
        self.reactants_stoichiometry_tracked=reactants_stoichiometry_tracked_I
        self.products_stoichiometry_tracked=products_stoichiometry_tracked_I
        self.reactants_ids_tracked=reactants_ids_tracked_I
        self.products_ids_tracked=products_ids_tracked_I
        self.reactants_elements_tracked=reactants_elements_tracked_I
        self.products_elements_tracked=products_elements_tracked_I
        self.reactants_positions_tracked=reactants_positions_tracked_I
        self.products_positions_tracked=products_positions_tracked_I
        self.reactants_mapping=reactants_mapping_I
        self.products_mapping=products_mapping_I
        self.rxn_equation=rxn_equation_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'mapping_id':self.mapping_id,
                'rxn_id':self.rxn_id,
                'rxn_description':self.rxn_description,
                'reactants_stoichiometry_tracked':self.reactants_stoichiometry_tracked,
                'products_stoichiometry_tracked':self.products_stoichiometry_tracked,
                'reactants_ids_tracked':self.reactants_ids_tracked,
                'products_ids_tracked':self.products_ids_tracked,
                'reactants_elements_tracked':self.reactants_elements_tracked,
                'products_elements_tracked':self.products_elements_tracked,
                'reactants_positions_tracked':self.reactants_positions_tracked,
                'products_positions_tracked':self.products_positions_tracked,
                'reactants_mapping':self.reactants_mapping,
                'products_mapping':self.products_mapping,
                'rxn_equation':self.rxn_equation,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__());

class data_stage02_isotopomer_atomMappingMetabolites(Base):
    __tablename__ = 'data_stage02_isotopomer_atomMappingMetabolites'
    id = Column(Integer, Sequence('data_stage02_isotopomer_atomMappingMetabolites_id_seq'), primary_key=True)
    mapping_id = Column(String(100), primary_key=True)
    #met_name = Column(String(500))
    met_id = Column(String(100), primary_key=True)
    #formula = Column(String(100))
    met_elements = Column(postgresql.ARRAY(String(3))) # the elements that are tracked (e.g. C,C,C)
    met_atompositions = Column(postgresql.ARRAY(Integer)) #the atoms positions that are tracked (e.g. 1,2,3) 
    met_symmetry_elements = Column(postgresql.ARRAY(String(3))) #symmetric molecules can alternatively be indicated in the reaction mapping
    met_symmetry_atompositions = Column(postgresql.ARRAY(Integer)) #maps the symmetric atom positions
    used_ = Column(Boolean)
    comment_ = Column(Text);
    met_mapping=Column(postgresql.JSON())
    #met_mapping=Column(postgresql.ARRAY(String(5000)))
    base_met_ids=Column(postgresql.ARRAY(String(100)))
    base_met_elements=Column(postgresql.JSON())
    #base_met_elements=Column(postgresql.ARRAY(String(3)))
    base_met_atompositions=Column(postgresql.JSON())
    #base_met_atompositions=Column(postgresql.ARRAY(Integer))
    base_met_symmetry_elements=Column(postgresql.JSON())
    #base_met_symmetry_elements=Column(postgresql.ARRAY(String(3)))
    base_met_symmetry_atompositions=Column(postgresql.JSON())
    #base_met_symmetry_atompositions=Column(postgresql.ARRAY(Integer))
    base_met_indices=Column(postgresql.ARRAY(Integer))

    def __init__(self,
            mapping_id_I,
            #met_name_I,
            met_id_I,
            #formula_I,
            met_elements_I,
            met_atompositions_I,
            met_symmetry_elements_I,
            met_symmetry_atompositions_I,
            used__I,
            comment__I,
            met_mapping_I=None,
            base_met_ids_I=None,
            base_met_elements_I=None,
            base_met_atompositions_I=None,
            base_met_symmetry_elements_I=None,
            base_met_symmetry_atompositions_I=None,
            base_met_indices_I=None):
        self.mapping_id=mapping_id_I
        #self.met_name=met_name_I
        self.met_id=met_id_I
        #self.formula=formula_I
        self.met_elements=met_elements_I
        self.met_atompositions=met_atompositions_I
        self.met_symmetry_elements=met_symmetry_elements_I
        self.met_symmetry_atompositions=met_symmetry_atompositions_I
        self.used_=used__I
        self.comment_=comment__I
        self.met_mapping=met_mapping_I;
        self.base_met_ids=base_met_ids_I;
        self.base_met_elements=base_met_elements_I;
        self.base_met_atompositions=base_met_atompositions_I;
        self.base_met_symmetry_elements=base_met_symmetry_elements_I;
        self.base_met_symmetry_atompositions=base_met_symmetry_atompositions_I;
        self.base_met_indices = base_met_indices_I;

    def __repr__dict__(self):
        return {'id':self.id,
                'mapping_id':self.mapping_id,
                #'met_name':self.met_name,
                'met_id':self.met_id,
                #'formula':self.formula,
                'met_elements':self.met_elements,
                'met_atompositions':self.met_atompositions,
                'met_symmetry_elements':self.met_symmetry_elements,
                'met_symmetry_atompositions':self.met_symmetry_atompositions,
                'used_':self.used_,
                'comment_':self.comment_,
                'met_mapping':self.met_mapping,
                'base_met_ids':self.base_met_ids,
                'base_met_elements':self.base_met_elements,
                'base_met_atompositions':self.base_met_atompositions,
                'base_met_symmetry_elements':self.base_met_symmetry_elements,
                'base_met_symmetry_atompositions':self.base_met_symmetry_atompositions,
                'base_met_indices':self.base_met_indices}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())