from SBaaS_base.postgresql_orm_base import *
class models_biocyc_enzymaticReactions(Base):
    __tablename__ = 'models_biocyc_enzymaticReactions'
    id = Column(Integer, Sequence('models_biocyc_enzymaticReactions_id_seq'), primary_key=True)
    name = Column(Text)
    alternative_cofactors = Column(Text)
    alternative_substrates = Column(Text)
    basis_for_assignment = Column(Text)
    citations = Column(Text)
    cofactors = Column(Text)
    common_name = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    enzyme = Column(Text)
    frame_id = Column(Text)
    kcat = Column(Text)
    km = Column(Text)
    names = Column(Text)
    parent_classes = Column(Text)
    ph_opt = Column(Text)
    physiologically_relevant = Column(Text)
    reaction = Column(Text)
    reaction_direction = Column(Text)
    regulated_by = Column(Text)
    required_protein_complex = Column(Text)
    specific_activity = Column(Text)
    synonyms = Column(Text)
    temperature_opt = Column(Text)
    vmax = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.alternative_cofactors = row_dict_I['alternative_cofactors']
        self.alternative_substrates = row_dict_I['alternative_substrates']
        self.basis_for_assignment = row_dict_I['basis_for_assignment']
        self.citations = row_dict_I['citations']
        self.cofactors = row_dict_I['cofactors']
        self.common_name = row_dict_I['common_name']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.enzyme = row_dict_I['enzyme']
        self.frame_id = row_dict_I['frame_id']
        self.kcat = row_dict_I['kcat']
        self.km = row_dict_I['km']
        self.names = row_dict_I['names']
        self.parent_classes = row_dict_I['parent_classes']
        self.ph_opt = row_dict_I['ph_opt']
        self.physiologically_relevant = row_dict_I['physiologically_relevant']
        self.reaction = row_dict_I['reaction']
        self.reaction_direction = row_dict_I['reaction_direction']
        self.regulated_by = row_dict_I['regulated_by']
        self.required_protein_complex = row_dict_I['required_protein_complex']
        self.specific_activity = row_dict_I['specific_activity']
        self.synonyms = row_dict_I['synonyms']
        self.temperature_opt = row_dict_I['temperature_opt']
        self.vmax = row_dict_I['vmax']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,alternative_cofactors_I,alternative_substrates_I,basis_for_assignment_I,citations_I,cofactors_I,common_name_I,credits_I,data_source_I,enzyme_I,frame_id_I,kcat_I,km_I,names_I,parent_classes_I,ph_opt_I,physiologically_relevant_I,reaction_I,reaction_direction_I,regulated_by_I,required_protein_complex_I,specific_activity_I,synonyms_I,temperature_opt_I,vmax_I,database_I,used__I,comment__I):
        self.name = name_I
        self.alternative_cofactors = alternative_cofactors_I
        self.alternative_substrates = alternative_substrates_I
        self.basis_for_assignment = basis_for_assignment_I
        self.citations = citations_I
        self.cofactors = cofactors_I
        self.common_name = common_name_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.enzyme = enzyme_I
        self.frame_id = frame_id_I
        self.kcat = kcat_I
        self.km = km_I
        self.names = names_I
        self.parent_classes = parent_classes_I
        self.ph_opt = ph_opt_I
        self.physiologically_relevant = physiologically_relevant_I
        self.reaction = reaction_I
        self.reaction_direction = reaction_direction_I
        self.regulated_by = regulated_by_I
        self.required_protein_complex = required_protein_complex_I
        self.specific_activity = specific_activity_I
        self.synonyms = synonyms_I
        self.temperature_opt = temperature_opt_I
        self.vmax = vmax_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'alternative_cofactors':self.alternative_cofactors,
        'alternative_substrates':self.alternative_substrates,
        'basis_for_assignment':self.basis_for_assignment,
        'citations':self.citations,
        'cofactors':self.cofactors,
        'common_name':self.common_name,
        'credits':self.credits,
        'data_source':self.data_source,
        'enzyme':self.enzyme,
        'frame_id':self.frame_id,
        'kcat':self.kcat,
        'km':self.km,
        'names':self.names,
        'parent_classes':self.parent_classes,
        'ph_opt':self.ph_opt,
        'physiologically_relevant':self.physiologically_relevant,
        'reaction':self.reaction,
        'reaction_direction':self.reaction_direction,
        'regulated_by':self.regulated_by,
        'required_protein_complex':self.required_protein_complex,
        'specific_activity':self.specific_activity,
        'synonyms':self.synonyms,
        'temperature_opt':self.temperature_opt,
        'vmax':self.vmax,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class models_biocyc_polymerSegments(Base):
    __tablename__ = 'models_biocyc_polymerSegments'
    id = Column(Integer, Sequence('models_biocyc_polymerSegments_id_seq'), primary_key=True)
    name = Column(Text)
    abs_center_pos = Column(Text)
    absolute_plus_1_pos = Column(Text)
    accession_1 = Column(Text)
    accession_2 = Column(Text)
    alternate_sequence = Column(Text)
    bucket_of = Column(Text)
    centisome_position = Column(Text)
    citations = Column(Text)
    common_name = Column(Text)
    component_of = Column(Text)
    components = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    extent_unknown = Column(Text)
    frame_id = Column(Text)
    in_group = Column(Text)
    interrupted = Column(Text)
    involved_in_regulation = Column(Text)
    knockout_growth_observations = Column(Text)
    last_update = Column(Text)
    left_end_position = Column(Text)
    names = Column(Text)
    parent_classes = Column(Text)
    product = Column(Text)
    promoter_boxes = Column(Text)
    pseudo_gene_product = Column(Text)
    regulated_by = Column(Text)
    right_end_position = Column(Text)
    site_length = Column(Text)
    synonyms = Column(Text)
    transcription_direction = Column(Text)
    unmapped_component_of = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.abs_center_pos = row_dict_I['abs_center_pos']
        self.absolute_plus_1_pos = row_dict_I['absolute_plus_1_pos']
        self.accession_1 = row_dict_I['accession_1']
        self.accession_2 = row_dict_I['accession_2']
        self.alternate_sequence = row_dict_I['alternate_sequence']
        self.bucket_of = row_dict_I['bucket_of']
        self.centisome_position = row_dict_I['centisome_position']
        self.citations = row_dict_I['citations']
        self.common_name = row_dict_I['common_name']
        self.component_of = row_dict_I['component_of']
        self.components = row_dict_I['components']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.extent_unknown = row_dict_I['extent_unknown']
        self.frame_id = row_dict_I['frame_id']
        self.in_group = row_dict_I['in_group']
        self.interrupted = row_dict_I['interrupted']
        self.involved_in_regulation = row_dict_I['involved_in_regulation']
        self.knockout_growth_observations = row_dict_I['knockout_growth_observations']
        self.last_update = row_dict_I['last_update']
        self.left_end_position = row_dict_I['left_end_position']
        self.names = row_dict_I['names']
        self.parent_classes = row_dict_I['parent_classes']
        self.product = row_dict_I['product']
        self.promoter_boxes = row_dict_I['promoter_boxes']
        self.pseudo_gene_product = row_dict_I['pseudo_gene_product']
        self.regulated_by = row_dict_I['regulated_by']
        self.right_end_position = row_dict_I['right_end_position']
        self.site_length = row_dict_I['site_length']
        self.synonyms = row_dict_I['synonyms']
        self.transcription_direction = row_dict_I['transcription_direction']
        self.unmapped_component_of = row_dict_I['unmapped_component_of']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,abs_center_pos_I,absolute_plus_1_pos_I,accession_1_I,accession_2_I,alternate_sequence_I,bucket_of_I,centisome_position_I,citations_I,common_name_I,component_of_I,components_I,credits_I,data_source_I,extent_unknown_I,frame_id_I,in_group_I,interrupted_I,involved_in_regulation_I,knockout_growth_observations_I,last_update_I,left_end_position_I,names_I,parent_classes_I,product_I,promoter_boxes_I,pseudo_gene_product_I,regulated_by_I,right_end_position_I,site_length_I,synonyms_I,transcription_direction_I,unmapped_component_of_I,database_I,used__I,comment__I):
        self.name = name_I
        self.abs_center_pos = abs_center_pos_I
        self.absolute_plus_1_pos = absolute_plus_1_pos_I
        self.accession_1 = accession_1_I
        self.accession_2 = accession_2_I
        self.alternate_sequence = alternate_sequence_I
        self.bucket_of = bucket_of_I
        self.centisome_position = centisome_position_I
        self.citations = citations_I
        self.common_name = common_name_I
        self.component_of = component_of_I
        self.components = components_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.extent_unknown = extent_unknown_I
        self.frame_id = frame_id_I
        self.in_group = in_group_I
        self.interrupted = interrupted_I
        self.involved_in_regulation = involved_in_regulation_I
        self.knockout_growth_observations = knockout_growth_observations_I
        self.last_update = last_update_I
        self.left_end_position = left_end_position_I
        self.names = names_I
        self.parent_classes = parent_classes_I
        self.product = product_I
        self.promoter_boxes = promoter_boxes_I
        self.pseudo_gene_product = pseudo_gene_product_I
        self.regulated_by = regulated_by_I
        self.right_end_position = right_end_position_I
        self.site_length = site_length_I
        self.synonyms = synonyms_I
        self.transcription_direction = transcription_direction_I
        self.unmapped_component_of = unmapped_component_of_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'abs_center_pos':self.abs_center_pos,
        'absolute_plus_1_pos':self.absolute_plus_1_pos,
        'accession_1':self.accession_1,
        'accession_2':self.accession_2,
        'alternate_sequence':self.alternate_sequence,
        'bucket_of':self.bucket_of,
        'centisome_position':self.centisome_position,
        'citations':self.citations,
        'common_name':self.common_name,
        'component_of':self.component_of,
        'components':self.components,
        'credits':self.credits,
        'data_source':self.data_source,
        'extent_unknown':self.extent_unknown,
        'frame_id':self.frame_id,
        'in_group':self.in_group,
        'interrupted':self.interrupted,
        'involved_in_regulation':self.involved_in_regulation,
        'knockout_growth_observations':self.knockout_growth_observations,
        'last_update':self.last_update,
        'left_end_position':self.left_end_position,
        'names':self.names,
        'parent_classes':self.parent_classes,
        'product':self.product,
        'promoter_boxes':self.promoter_boxes,
        'pseudo_gene_product':self.pseudo_gene_product,
        'regulated_by':self.regulated_by,
        'right_end_position':self.right_end_position,
        'site_length':self.site_length,
        'synonyms':self.synonyms,
        'transcription_direction':self.transcription_direction,
        'unmapped_component_of':self.unmapped_component_of,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class models_biocyc_proteinFeatures(Base):
    __tablename__ = 'models_biocyc_proteinFeatures'
    id = Column(Integer, Sequence('models_biocyc_proteinFeatures_id_seq'), primary_key=True)
    name = Column(Text)
    alternate_sequence = Column(Text)
    attached_group = Column(Text)
    common_name = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    feature_of = Column(Text)
    frame_id = Column(Text)
    homology_motif = Column(Text)
    parent_classes = Column(Text)
    possible_feature_states = Column(Text)
    residue_number = Column(Text)
    residue_type = Column(Text)
    synonyms = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.alternate_sequence = row_dict_I['alternate_sequence']
        self.attached_group = row_dict_I['attached_group']
        self.common_name = row_dict_I['common_name']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.feature_of = row_dict_I['feature_of']
        self.frame_id = row_dict_I['frame_id']
        self.homology_motif = row_dict_I['homology_motif']
        self.parent_classes = row_dict_I['parent_classes']
        self.possible_feature_states = row_dict_I['possible_feature_states']
        self.residue_number = row_dict_I['residue_number']
        self.residue_type = row_dict_I['residue_type']
        self.synonyms = row_dict_I['synonyms']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,alternate_sequence_I,attached_group_I,common_name_I,credits_I,data_source_I,feature_of_I,frame_id_I,homology_motif_I,parent_classes_I,possible_feature_states_I,residue_number_I,residue_type_I,synonyms_I,database_I,used__I,comment__I):
        self.name = name_I
        self.alternate_sequence = alternate_sequence_I
        self.attached_group = attached_group_I
        self.common_name = common_name_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.feature_of = feature_of_I
        self.frame_id = frame_id_I
        self.homology_motif = homology_motif_I
        self.parent_classes = parent_classes_I
        self.possible_feature_states = possible_feature_states_I
        self.residue_number = residue_number_I
        self.residue_type = residue_type_I
        self.synonyms = synonyms_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'alternate_sequence':self.alternate_sequence,
        'attached_group':self.attached_group,
        'common_name':self.common_name,
        'credits':self.credits,
        'data_source':self.data_source,
        'feature_of':self.feature_of,
        'frame_id':self.frame_id,
        'homology_motif':self.homology_motif,
        'parent_classes':self.parent_classes,
        'possible_feature_states':self.possible_feature_states,
        'residue_number':self.residue_number,
        'residue_type':self.residue_type,
        'synonyms':self.synonyms,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class models_biocyc_pathways(Base):
    __tablename__ = 'models_biocyc_pathways'
    id = Column(Integer, Sequence('models_biocyc_pathways_id_seq'), primary_key=True)
    name = Column(Text)
    reaction_list = Column(Text)
    chimeric = Column(Text)
    citations = Column(Text)
    common_name = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    engineered = Column(Text)
    enzyme_use = Column(Text)
    enzymes_not_used = Column(Text)
    frame_id = Column(Text)
    genes_of_pathway = Column(Text)
    hypothetical_reactions = Column(Text)
    in_pathway = Column(Text)
    key_reactions = Column(Text)
    names = Column(Text)
    parent_classes = Column(Text)
    pathway_links = Column(Text)
    primaries = Column(Text)
    rate_limiting_step = Column(Text)
    reaction_layout = Column(Text)
    regulated_by = Column(Text)
    score = Column(Text)
    species = Column(Text)
    sub_pathways = Column(Text)
    super_pathways = Column(Text)
    synonyms = Column(Text)
    taxonomic_range = Column(Text)
    variants = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.reaction_list = row_dict_I['reaction_list']
        self.chimeric = row_dict_I['chimeric']
        self.citations = row_dict_I['citations']
        self.common_name = row_dict_I['common_name']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.engineered = row_dict_I['engineered']
        self.enzyme_use = row_dict_I['enzyme_use']
        self.enzymes_not_used = row_dict_I['enzymes_not_used']
        self.frame_id = row_dict_I['frame_id']
        self.genes_of_pathway = row_dict_I['genes_of_pathway']
        self.hypothetical_reactions = row_dict_I['hypothetical_reactions']
        self.in_pathway = row_dict_I['in_pathway']
        self.key_reactions = row_dict_I['key_reactions']
        self.names = row_dict_I['names']
        self.parent_classes = row_dict_I['parent_classes']
        self.pathway_links = row_dict_I['pathway_links']
        self.primaries = row_dict_I['primaries']
        self.rate_limiting_step = row_dict_I['rate_limiting_step']
        self.reaction_layout = row_dict_I['reaction_layout']
        self.regulated_by = row_dict_I['regulated_by']
        self.score = row_dict_I['score']
        self.species = row_dict_I['species']
        self.sub_pathways = row_dict_I['sub_pathways']
        self.super_pathways = row_dict_I['super_pathways']
        self.synonyms = row_dict_I['synonyms']
        self.taxonomic_range = row_dict_I['taxonomic_range']
        self.variants = row_dict_I['variants']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,reaction_list_I,chimeric_I,citations_I,common_name_I,credits_I,data_source_I,engineered_I,enzyme_use_I,enzymes_not_used_I,frame_id_I,genes_of_pathway_I,hypothetical_reactions_I,in_pathway_I,key_reactions_I,names_I,parent_classes_I,pathway_links_I,primaries_I,rate_limiting_step_I,reaction_layout_I,regulated_by_I,score_I,species_I,sub_pathways_I,super_pathways_I,synonyms_I,taxonomic_range_I,variants_I,database_I,used__I,comment__I):
        self.name = name_I
        self.reaction_list = reaction_list_I
        self.chimeric = chimeric_I
        self.citations = citations_I
        self.common_name = common_name_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.engineered = engineered_I
        self.enzyme_use = enzyme_use_I
        self.enzymes_not_used = enzymes_not_used_I
        self.frame_id = frame_id_I
        self.genes_of_pathway = genes_of_pathway_I
        self.hypothetical_reactions = hypothetical_reactions_I
        self.in_pathway = in_pathway_I
        self.key_reactions = key_reactions_I
        self.names = names_I
        self.parent_classes = parent_classes_I
        self.pathway_links = pathway_links_I
        self.primaries = primaries_I
        self.rate_limiting_step = rate_limiting_step_I
        self.reaction_layout = reaction_layout_I
        self.regulated_by = regulated_by_I
        self.score = score_I
        self.species = species_I
        self.sub_pathways = sub_pathways_I
        self.super_pathways = super_pathways_I
        self.synonyms = synonyms_I
        self.taxonomic_range = taxonomic_range_I
        self.variants = variants_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'reaction_list':self.reaction_list,
        'chimeric':self.chimeric,
        'citations':self.citations,
        'common_name':self.common_name,
        'credits':self.credits,
        'data_source':self.data_source,
        'engineered':self.engineered,
        'enzyme_use':self.enzyme_use,
        'enzymes_not_used':self.enzymes_not_used,
        'frame_id':self.frame_id,
        'genes_of_pathway':self.genes_of_pathway,
        'hypothetical_reactions':self.hypothetical_reactions,
        'in_pathway':self.in_pathway,
        'key_reactions':self.key_reactions,
        'names':self.names,
        'parent_classes':self.parent_classes,
        'pathway_links':self.pathway_links,
        'primaries':self.primaries,
        'rate_limiting_step':self.rate_limiting_step,
        'reaction_layout':self.reaction_layout,
        'regulated_by':self.regulated_by,
        'score':self.score,
        'species':self.species,
        'sub_pathways':self.sub_pathways,
        'super_pathways':self.super_pathways,
        'synonyms':self.synonyms,
        'taxonomic_range':self.taxonomic_range,
        'variants':self.variants,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class models_biocyc_compounds(Base):
    __tablename__ = 'models_biocyc_compounds'
    id = Column(Integer, Sequence('models_biocyc_compounds_id_seq'), primary_key=True)
    name = Column(Text)
    chemical_formula = Column(Text)
    appears_in_left_side_of = Column(Text)
    appears_in_right_side_of = Column(Text)
    citations = Column(Text)
    cofactors_of = Column(Text)
    common_name = Column(Text)
    component_of = Column(Text)
    components = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    frame_id = Column(Text)
    gibbs_0 = Column(Text)
    has_no_structure = Column(Text)
    in_mixture = Column(Text)
    inchi = Column(Text)
    inchi_key = Column(Text)
    molecular_weight = Column(Text)
    monoisotopic_mw = Column(Text)
    names = Column(Text)
    parent_classes = Column(Text)
    pka1 = Column(Text)
    pka2 = Column(Text)
    pka3 = Column(Text)
    regulates = Column(Text)
    smiles = Column(Text)
    species = Column(Text)
    synonyms = Column(Text)
    systematic_name = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.chemical_formula = row_dict_I['chemical_formula']
        self.appears_in_left_side_of = row_dict_I['appears_in_left_side_of']
        self.appears_in_right_side_of = row_dict_I['appears_in_right_side_of']
        self.citations = row_dict_I['citations']
        self.cofactors_of = row_dict_I['cofactors_of']
        self.common_name = row_dict_I['common_name']
        self.component_of = row_dict_I['component_of']
        self.components = row_dict_I['components']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.frame_id = row_dict_I['frame_id']
        self.gibbs_0 = row_dict_I['gibbs_0']
        self.has_no_structure = row_dict_I['has_no_structure']
        self.in_mixture = row_dict_I['in_mixture']
        self.inchi = row_dict_I['inchi']
        self.inchi_key = row_dict_I['inchi_key']
        self.molecular_weight = row_dict_I['molecular_weight']
        self.monoisotopic_mw = row_dict_I['monoisotopic_mw']
        self.names = row_dict_I['names']
        self.parent_classes = row_dict_I['parent_classes']
        self.pka1 = row_dict_I['pka1']
        self.pka2 = row_dict_I['pka2']
        self.pka3 = row_dict_I['pka3']
        self.regulates = row_dict_I['regulates']
        self.smiles = row_dict_I['smiles']
        self.species = row_dict_I['species']
        self.synonyms = row_dict_I['synonyms']
        self.systematic_name = row_dict_I['systematic_name']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,chemical_formula_I,appears_in_left_side_of_I,appears_in_right_side_of_I,citations_I,cofactors_of_I,common_name_I,component_of_I,components_I,credits_I,data_source_I,frame_id_I,gibbs_0_I,has_no_structure_I,in_mixture_I,inchi_I,inchi_key_I,molecular_weight_I,monoisotopic_mw_I,names_I,parent_classes_I,pka1_I,pka2_I,pka3_I,regulates_I,smiles_I,species_I,synonyms_I,systematic_name_I,database_I,used__I,comment__I):
        self.name = name_I
        self.chemical_formula = chemical_formula_I
        self.appears_in_left_side_of = appears_in_left_side_of_I
        self.appears_in_right_side_of = appears_in_right_side_of_I
        self.citations = citations_I
        self.cofactors_of = cofactors_of_I
        self.common_name = common_name_I
        self.component_of = component_of_I
        self.components = components_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.frame_id = frame_id_I
        self.gibbs_0 = gibbs_0_I
        self.has_no_structure = has_no_structure_I
        self.in_mixture = in_mixture_I
        self.inchi = inchi_I
        self.inchi_key = inchi_key_I
        self.molecular_weight = molecular_weight_I
        self.monoisotopic_mw = monoisotopic_mw_I
        self.names = names_I
        self.parent_classes = parent_classes_I
        self.pka1 = pka1_I
        self.pka2 = pka2_I
        self.pka3 = pka3_I
        self.regulates = regulates_I
        self.smiles = smiles_I
        self.species = species_I
        self.synonyms = synonyms_I
        self.systematic_name = systematic_name_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'chemical_formula':self.chemical_formula,
        'appears_in_left_side_of':self.appears_in_left_side_of,
        'appears_in_right_side_of':self.appears_in_right_side_of,
        'citations':self.citations,
        'cofactors_of':self.cofactors_of,
        'common_name':self.common_name,
        'component_of':self.component_of,
        'components':self.components,
        'credits':self.credits,
        'data_source':self.data_source,
        'frame_id':self.frame_id,
        'gibbs_0':self.gibbs_0,
        'has_no_structure':self.has_no_structure,
        'in_mixture':self.in_mixture,
        'inchi':self.inchi,
        'inchi_key':self.inchi_key,
        'molecular_weight':self.molecular_weight,
        'monoisotopic_mw':self.monoisotopic_mw,
        'names':self.names,
        'parent_classes':self.parent_classes,
        'pka1':self.pka1,
        'pka2':self.pka2,
        'pka3':self.pka3,
        'regulates':self.regulates,
        'smiles':self.smiles,
        'species':self.species,
        'synonyms':self.synonyms,
        'systematic_name':self.systematic_name,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class models_biocyc_proteins(Base):
    __tablename__ = 'models_biocyc_proteins'
    id = Column(Integer, Sequence('models_biocyc_proteins_id_seq'), primary_key=True)
    name = Column(Text)
    appears_in_left_side_of = Column(Text)
    appears_in_right_side_of = Column(Text)
    catalyzes = Column(Text)
    chemical_formula = Column(Text)
    citations = Column(Text)
    cofactors_of = Column(Text)
    common_name = Column(Text)
    component_of = Column(Text)
    consensus_sequence = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    dna_footprint_size = Column(Text)
    enzyme_not_used_in = Column(Text)
    features = Column(Text)
    frame_id = Column(Text)
    gene = Column(Text)
    gibbs_0 = Column(Text)
    go_terms = Column(Text)
    has_no_structure = Column(Text)
    in_mixture = Column(Text)
    locations = Column(Text)
    modified_form = Column(Text)
    molecular_weight = Column(Text)
    molecular_weight_exp = Column(Text)
    molecular_weight_kd = Column(Text)
    molecular_weight_seq = Column(Text)
    names = Column(Text)
    neidhardt_spot_number = Column(Text)
    parent_classes = Column(Text)
    pi = Column(Text)
    recognized_promoters = Column(Text)
    regulated_by = Column(Text)
    regulates = Column(Text)
    species = Column(Text)
    splice_form_introns = Column(Text)
    symmetry = Column(Text)
    synonyms = Column(Text)
    unmodified_form = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.appears_in_left_side_of = row_dict_I['appears_in_left_side_of']
        self.appears_in_right_side_of = row_dict_I['appears_in_right_side_of']
        self.catalyzes = row_dict_I['catalyzes']
        self.chemical_formula = row_dict_I['chemical_formula']
        self.citations = row_dict_I['citations']
        self.cofactors_of = row_dict_I['cofactors_of']
        self.common_name = row_dict_I['common_name']
        self.component_of = row_dict_I['component_of']
        self.consensus_sequence = row_dict_I['consensus_sequence']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.dna_footprint_size = row_dict_I['dna_footprint_size']
        self.enzyme_not_used_in = row_dict_I['enzyme_not_used_in']
        self.features = row_dict_I['features']
        self.frame_id = row_dict_I['frame_id']
        self.gene = row_dict_I['gene']
        self.gibbs_0 = row_dict_I['gibbs_0']
        self.go_terms = row_dict_I['go_terms']
        self.has_no_structure = row_dict_I['has_no_structure']
        self.in_mixture = row_dict_I['in_mixture']
        self.locations = row_dict_I['locations']
        self.modified_form = row_dict_I['modified_form']
        self.molecular_weight = row_dict_I['molecular_weight']
        self.molecular_weight_exp = row_dict_I['molecular_weight_exp']
        self.molecular_weight_kd = row_dict_I['molecular_weight_kd']
        self.molecular_weight_seq = row_dict_I['molecular_weight_seq']
        self.names = row_dict_I['names']
        self.neidhardt_spot_number = row_dict_I['neidhardt_spot_number']
        self.parent_classes = row_dict_I['parent_classes']
        self.pi = row_dict_I['pi']
        self.recognized_promoters = row_dict_I['recognized_promoters']
        self.regulated_by = row_dict_I['regulated_by']
        self.regulates = row_dict_I['regulates']
        self.species = row_dict_I['species']
        self.splice_form_introns = row_dict_I['splice_form_introns']
        self.symmetry = row_dict_I['symmetry']
        self.synonyms = row_dict_I['synonyms']
        self.unmodified_form = row_dict_I['unmodified_form']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,appears_in_left_side_of_I,appears_in_right_side_of_I,catalyzes_I,chemical_formula_I,citations_I,cofactors_of_I,common_name_I,component_of_I,consensus_sequence_I,credits_I,data_source_I,dna_footprint_size_I,enzyme_not_used_in_I,features_I,frame_id_I,gene_I,gibbs_0_I,go_terms_I,has_no_structure_I,in_mixture_I,locations_I,modified_form_I,molecular_weight_I,molecular_weight_exp_I,molecular_weight_kd_I,molecular_weight_seq_I,names_I,neidhardt_spot_number_I,parent_classes_I,pi_I,recognized_promoters_I,regulated_by_I,regulates_I,species_I,splice_form_introns_I,symmetry_I,synonyms_I,unmodified_form_I,database_I,used__I,comment__I):
        self.name = name_I
        self.appears_in_left_side_of = appears_in_left_side_of_I
        self.appears_in_right_side_of = appears_in_right_side_of_I
        self.catalyzes = catalyzes_I
        self.chemical_formula = chemical_formula_I
        self.citations = citations_I
        self.cofactors_of = cofactors_of_I
        self.common_name = common_name_I
        self.component_of = component_of_I
        self.consensus_sequence = consensus_sequence_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.dna_footprint_size = dna_footprint_size_I
        self.enzyme_not_used_in = enzyme_not_used_in_I
        self.features = features_I
        self.frame_id = frame_id_I
        self.gene = gene_I
        self.gibbs_0 = gibbs_0_I
        self.go_terms = go_terms_I
        self.has_no_structure = has_no_structure_I
        self.in_mixture = in_mixture_I
        self.locations = locations_I
        self.modified_form = modified_form_I
        self.molecular_weight = molecular_weight_I
        self.molecular_weight_exp = molecular_weight_exp_I
        self.molecular_weight_kd = molecular_weight_kd_I
        self.molecular_weight_seq = molecular_weight_seq_I
        self.names = names_I
        self.neidhardt_spot_number = neidhardt_spot_number_I
        self.parent_classes = parent_classes_I
        self.pi = pi_I
        self.recognized_promoters = recognized_promoters_I
        self.regulated_by = regulated_by_I
        self.regulates = regulates_I
        self.species = species_I
        self.splice_form_introns = splice_form_introns_I
        self.symmetry = symmetry_I
        self.synonyms = synonyms_I
        self.unmodified_form = unmodified_form_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'appears_in_left_side_of':self.appears_in_left_side_of,
        'appears_in_right_side_of':self.appears_in_right_side_of,
        'catalyzes':self.catalyzes,
        'chemical_formula':self.chemical_formula,
        'citations':self.citations,
        'cofactors_of':self.cofactors_of,
        'common_name':self.common_name,
        'component_of':self.component_of,
        'consensus_sequence':self.consensus_sequence,
        'credits':self.credits,
        'data_source':self.data_source,
        'dna_footprint_size':self.dna_footprint_size,
        'enzyme_not_used_in':self.enzyme_not_used_in,
        'features':self.features,
        'frame_id':self.frame_id,
        'gene':self.gene,
        'gibbs_0':self.gibbs_0,
        'go_terms':self.go_terms,
        'has_no_structure':self.has_no_structure,
        'in_mixture':self.in_mixture,
        'locations':self.locations,
        'modified_form':self.modified_form,
        'molecular_weight':self.molecular_weight,
        'molecular_weight_exp':self.molecular_weight_exp,
        'molecular_weight_kd':self.molecular_weight_kd,
        'molecular_weight_seq':self.molecular_weight_seq,
        'names':self.names,
        'neidhardt_spot_number':self.neidhardt_spot_number,
        'parent_classes':self.parent_classes,
        'pi':self.pi,
        'recognized_promoters':self.recognized_promoters,
        'regulated_by':self.regulated_by,
        'regulates':self.regulates,
        'species':self.species,
        'splice_form_introns':self.splice_form_introns,
        'symmetry':self.symmetry,
        'synonyms':self.synonyms,
        'unmodified_form':self.unmodified_form,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class models_biocyc_publications(Base):
    __tablename__ = 'models_biocyc_publications'
    id = Column(Integer, Sequence('models_biocyc_publications_id_seq'), primary_key=True)
    name = Column(Text)
    abstract = Column(Text)
    authors = Column(Text)
    common_name = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    frame_id = Column(Text)
    medline_uid = Column(Text)
    parent_classes = Column(Text)
    pubmed_id = Column(Text)
    source = Column(Text)
    synonyms = Column(Text)
    title = Column(Text)
    year = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.abstract = row_dict_I['abstract']
        self.authors = row_dict_I['authors']
        self.common_name = row_dict_I['common_name']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.frame_id = row_dict_I['frame_id']
        self.medline_uid = row_dict_I['medline_uid']
        self.parent_classes = row_dict_I['parent_classes']
        self.pubmed_id = row_dict_I['pubmed_id']
        self.source = row_dict_I['source']
        self.synonyms = row_dict_I['synonyms']
        self.title = row_dict_I['title']
        self.year = row_dict_I['year']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,abstract_I,authors_I,common_name_I,credits_I,data_source_I,frame_id_I,medline_uid_I,parent_classes_I,pubmed_id_I,source_I,synonyms_I,title_I,year_I,database_I,used__I,comment__I):
        self.name = name_I
        self.abstract = abstract_I
        self.authors = authors_I
        self.common_name = common_name_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.frame_id = frame_id_I
        self.medline_uid = medline_uid_I
        self.parent_classes = parent_classes_I
        self.pubmed_id = pubmed_id_I
        self.source = source_I
        self.synonyms = synonyms_I
        self.title = title_I
        self.year = year_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'abstract':self.abstract,
        'authors':self.authors,
        'common_name':self.common_name,
        'credits':self.credits,
        'data_source':self.data_source,
        'frame_id':self.frame_id,
        'medline_uid':self.medline_uid,
        'parent_classes':self.parent_classes,
        'pubmed_id':self.pubmed_id,
        'source':self.source,
        'synonyms':self.synonyms,
        'title':self.title,
        'year':self.year,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class models_biocyc_reactions(Base):
    __tablename__ = 'models_biocyc_reactions'
    id = Column(Integer, Sequence('models_biocyc_reactions_id_seq'), primary_key=True)
    name = Column(Text)
    ec_number = Column(Text)
    cannot_balance = Column(Text)
    citations = Column(Text)
    common_name = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    enzymatic_reaction = Column(Text)
    enzymes_not_used = Column(Text)
    equilibrium_constant = Column(Text)
    frame_id = Column(Text)
    gibbs_0 = Column(Text)
    in_pathway = Column(Text)
    left = Column(Text)
    names = Column(Text)
    orphan = Column(Text)
    parent_classes = Column(Text)
    physiologically_relevant = Column(Text)
    primaries = Column(Text)
    reaction_direction = Column(Text)
    reaction_list = Column(Text)
    regulated_by = Column(Text)
    requirements = Column(Text)
    right = Column(Text)
    signal = Column(Text)
    species = Column(Text)
    spontaneous = Column(Text)
    std_reduction_potential = Column(Text)
    substrates = Column(Text)
    synonyms = Column(Text)
    systematic_name = Column(Text)
    taxonomic_range = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.ec_number = row_dict_I['ec_number']
        self.cannot_balance = row_dict_I['cannot_balance']
        self.citations = row_dict_I['citations']
        self.common_name = row_dict_I['common_name']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.enzymatic_reaction = row_dict_I['enzymatic_reaction']
        self.enzymes_not_used = row_dict_I['enzymes_not_used']
        self.equilibrium_constant = row_dict_I['equilibrium_constant']
        self.frame_id = row_dict_I['frame_id']
        self.gibbs_0 = row_dict_I['gibbs_0']
        self.in_pathway = row_dict_I['in_pathway']
        self.left = row_dict_I['left']
        self.names = row_dict_I['names']
        self.orphan = row_dict_I['orphan']
        self.parent_classes = row_dict_I['parent_classes']
        self.physiologically_relevant = row_dict_I['physiologically_relevant']
        self.primaries = row_dict_I['primaries']
        self.reaction_direction = row_dict_I['reaction_direction']
        self.reaction_list = row_dict_I['reaction_list']
        self.regulated_by = row_dict_I['regulated_by']
        self.requirements = row_dict_I['requirements']
        self.right = row_dict_I['right']
        self.signal = row_dict_I['signal']
        self.species = row_dict_I['species']
        self.spontaneous = row_dict_I['spontaneous']
        self.std_reduction_potential = row_dict_I['std_reduction_potential']
        self.substrates = row_dict_I['substrates']
        self.synonyms = row_dict_I['synonyms']
        self.systematic_name = row_dict_I['systematic_name']
        self.taxonomic_range = row_dict_I['taxonomic_range']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,ec_number_I,cannot_balance_I,citations_I,common_name_I,credits_I,data_source_I,enzymatic_reaction_I,enzymes_not_used_I,equilibrium_constant_I,frame_id_I,gibbs_0_I,in_pathway_I,left_I,names_I,orphan_I,parent_classes_I,physiologically_relevant_I,primaries_I,reaction_direction_I,reaction_list_I,regulated_by_I,requirements_I,right_I,signal_I,species_I,spontaneous_I,std_reduction_potential_I,substrates_I,synonyms_I,systematic_name_I,taxonomic_range_I,database_I,used__I,comment__I):
        self.name = name_I
        self.ec_number = ec_number_I
        self.cannot_balance = cannot_balance_I
        self.citations = citations_I
        self.common_name = common_name_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.enzymatic_reaction = enzymatic_reaction_I
        self.enzymes_not_used = enzymes_not_used_I
        self.equilibrium_constant = equilibrium_constant_I
        self.frame_id = frame_id_I
        self.gibbs_0 = gibbs_0_I
        self.in_pathway = in_pathway_I
        self.left = left_I
        self.names = names_I
        self.orphan = orphan_I
        self.parent_classes = parent_classes_I
        self.physiologically_relevant = physiologically_relevant_I
        self.primaries = primaries_I
        self.reaction_direction = reaction_direction_I
        self.reaction_list = reaction_list_I
        self.regulated_by = regulated_by_I
        self.requirements = requirements_I
        self.right = right_I
        self.signal = signal_I
        self.species = species_I
        self.spontaneous = spontaneous_I
        self.std_reduction_potential = std_reduction_potential_I
        self.substrates = substrates_I
        self.synonyms = synonyms_I
        self.systematic_name = systematic_name_I
        self.taxonomic_range = taxonomic_range_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'ec_number':self.ec_number,
        'cannot_balance':self.cannot_balance,
        'citations':self.citations,
        'common_name':self.common_name,
        'credits':self.credits,
        'data_source':self.data_source,
        'enzymatic_reaction':self.enzymatic_reaction,
        'enzymes_not_used':self.enzymes_not_used,
        'equilibrium_constant':self.equilibrium_constant,
        'frame_id':self.frame_id,
        'gibbs_0':self.gibbs_0,
        'in_pathway':self.in_pathway,
        'left':self.left,
        'names':self.names,
        'orphan':self.orphan,
        'parent_classes':self.parent_classes,
        'physiologically_relevant':self.physiologically_relevant,
        'primaries':self.primaries,
        'reaction_direction':self.reaction_direction,
        'reaction_list':self.reaction_list,
        'regulated_by':self.regulated_by,
        'requirements':self.requirements,
        'right':self.right,
        'signal':self.signal,
        'species':self.species,
        'spontaneous':self.spontaneous,
        'std_reduction_potential':self.std_reduction_potential,
        'substrates':self.substrates,
        'synonyms':self.synonyms,
        'systematic_name':self.systematic_name,
        'taxonomic_range':self.taxonomic_range,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class models_biocyc_RNAs(Base):
    __tablename__ = 'models_biocyc_RNAs'
    id = Column(Integer, Sequence('models_biocyc_RNAs_id_seq'), primary_key=True)
    name = Column(Text)
    anticodon = Column(Text)
    appears_in_left_side_of = Column(Text)
    appears_in_right_side_of = Column(Text)
    citations = Column(Text)
    codons = Column(Text)
    cofactors_of = Column(Text)
    common_name = Column(Text)
    component_of = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    frame_id = Column(Text)
    gene = Column(Text)
    gibbs_0 = Column(Text)
    go_terms = Column(Text)
    has_no_structure = Column(Text)
    in_mixture = Column(Text)
    locations = Column(Text)
    modified_form = Column(Text)
    names = Column(Text)
    parent_classes = Column(Text)
    regulated_by = Column(Text)
    regulates = Column(Text)
    species = Column(Text)
    splice_form_introns = Column(Text)
    synonyms = Column(Text)
    unmodified_form = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.anticodon = row_dict_I['anticodon']
        self.appears_in_left_side_of = row_dict_I['appears_in_left_side_of']
        self.appears_in_right_side_of = row_dict_I['appears_in_right_side_of']
        self.citations = row_dict_I['citations']
        self.codons = row_dict_I['codons']
        self.cofactors_of = row_dict_I['cofactors_of']
        self.common_name = row_dict_I['common_name']
        self.component_of = row_dict_I['component_of']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.frame_id = row_dict_I['frame_id']
        self.gene = row_dict_I['gene']
        self.gibbs_0 = row_dict_I['gibbs_0']
        self.go_terms = row_dict_I['go_terms']
        self.has_no_structure = row_dict_I['has_no_structure']
        self.in_mixture = row_dict_I['in_mixture']
        self.locations = row_dict_I['locations']
        self.modified_form = row_dict_I['modified_form']
        self.names = row_dict_I['names']
        self.parent_classes = row_dict_I['parent_classes']
        self.regulated_by = row_dict_I['regulated_by']
        self.regulates = row_dict_I['regulates']
        self.species = row_dict_I['species']
        self.splice_form_introns = row_dict_I['splice_form_introns']
        self.synonyms = row_dict_I['synonyms']
        self.unmodified_form = row_dict_I['unmodified_form']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,anticodon_I,appears_in_left_side_of_I,appears_in_right_side_of_I,citations_I,codons_I,cofactors_of_I,common_name_I,component_of_I,credits_I,data_source_I,frame_id_I,gene_I,gibbs_0_I,go_terms_I,has_no_structure_I,in_mixture_I,locations_I,modified_form_I,names_I,parent_classes_I,regulated_by_I,regulates_I,species_I,splice_form_introns_I,synonyms_I,unmodified_form_I,database_I,used__I,comment__I):
        self.name = name_I
        self.anticodon = anticodon_I
        self.appears_in_left_side_of = appears_in_left_side_of_I
        self.appears_in_right_side_of = appears_in_right_side_of_I
        self.citations = citations_I
        self.codons = codons_I
        self.cofactors_of = cofactors_of_I
        self.common_name = common_name_I
        self.component_of = component_of_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.frame_id = frame_id_I
        self.gene = gene_I
        self.gibbs_0 = gibbs_0_I
        self.go_terms = go_terms_I
        self.has_no_structure = has_no_structure_I
        self.in_mixture = in_mixture_I
        self.locations = locations_I
        self.modified_form = modified_form_I
        self.names = names_I
        self.parent_classes = parent_classes_I
        self.regulated_by = regulated_by_I
        self.regulates = regulates_I
        self.species = species_I
        self.splice_form_introns = splice_form_introns_I
        self.synonyms = synonyms_I
        self.unmodified_form = unmodified_form_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'anticodon':self.anticodon,
        'appears_in_left_side_of':self.appears_in_left_side_of,
        'appears_in_right_side_of':self.appears_in_right_side_of,
        'citations':self.citations,
        'codons':self.codons,
        'cofactors_of':self.cofactors_of,
        'common_name':self.common_name,
        'component_of':self.component_of,
        'credits':self.credits,
        'data_source':self.data_source,
        'frame_id':self.frame_id,
        'gene':self.gene,
        'gibbs_0':self.gibbs_0,
        'go_terms':self.go_terms,
        'has_no_structure':self.has_no_structure,
        'in_mixture':self.in_mixture,
        'locations':self.locations,
        'modified_form':self.modified_form,
        'names':self.names,
        'parent_classes':self.parent_classes,
        'regulated_by':self.regulated_by,
        'regulates':self.regulates,
        'species':self.species,
        'splice_form_introns':self.splice_form_introns,
        'synonyms':self.synonyms,
        'unmodified_form':self.unmodified_form,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class models_biocyc_regulation(Base):
    __tablename__ = 'models_biocyc_regulation'
    id = Column(Integer, Sequence('models_biocyc_regulation_id_seq'), primary_key=True)
    name = Column(Text)
    accessory_proteins = Column(Text)
    anti_antiterm_end_pos = Column(Text)
    anti_antiterm_start_pos = Column(Text)
    antiterminator_end_pos = Column(Text)
    antiterminator_start_pos = Column(Text)
    associated_binding_site = Column(Text)
    associated_rnase = Column(Text)
    common_name = Column(Text)
    credits = Column(Text)
    data_source = Column(Text)
    frame_id = Column(Text)
    ki = Column(Text)
    mechanism = Column(Text)
    mode = Column(Text)
    parent_classes = Column(Text)
    pause_end_pos = Column(Text)
    pause_start_pos = Column(Text)
    physiologically_relevant = Column(Text)
    regulated_entity = Column(Text)
    regulator = Column(Text)
    synonyms = Column(Text)
    database = Column(Text)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    #__table_args__ = (UniqueConstraint('',),)
    def __init__(self,row_dict_I,):
        self.name = row_dict_I['name']
        self.accessory_proteins = row_dict_I['accessory_proteins']
        self.anti_antiterm_end_pos = row_dict_I['anti_antiterm_end_pos']
        self.anti_antiterm_start_pos = row_dict_I['anti_antiterm_start_pos']
        self.antiterminator_end_pos = row_dict_I['antiterminator_end_pos']
        self.antiterminator_start_pos = row_dict_I['antiterminator_start_pos']
        self.associated_binding_site = row_dict_I['associated_binding_site']
        self.associated_rnase = row_dict_I['associated_rnase']
        self.common_name = row_dict_I['common_name']
        self.credits = row_dict_I['credits']
        self.data_source = row_dict_I['data_source']
        self.frame_id = row_dict_I['frame_id']
        self.ki = row_dict_I['ki']
        self.mechanism = row_dict_I['mechanism']
        self.mode = row_dict_I['mode']
        self.parent_classes = row_dict_I['parent_classes']
        self.pause_end_pos = row_dict_I['pause_end_pos']
        self.pause_start_pos = row_dict_I['pause_start_pos']
        self.physiologically_relevant = row_dict_I['physiologically_relevant']
        self.regulated_entity = row_dict_I['regulated_entity']
        self.regulator = row_dict_I['regulator']
        self.synonyms = row_dict_I['synonyms']
        self.database = row_dict_I['database']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self,name_I,accessory_proteins_I,anti_antiterm_end_pos_I,anti_antiterm_start_pos_I,antiterminator_end_pos_I,antiterminator_start_pos_I,associated_binding_site_I,associated_rnase_I,common_name_I,credits_I,data_source_I,frame_id_I,ki_I,mechanism_I,mode_I,parent_classes_I,pause_end_pos_I,pause_start_pos_I,physiologically_relevant_I,regulated_entity_I,regulator_I,synonyms_I,database_I,used__I,comment__I):
        self.name = name_I
        self.accessory_proteins = accessory_proteins_I
        self.anti_antiterm_end_pos = anti_antiterm_end_pos_I
        self.anti_antiterm_start_pos = anti_antiterm_start_pos_I
        self.antiterminator_end_pos = antiterminator_end_pos_I
        self.antiterminator_start_pos = antiterminator_start_pos_I
        self.associated_binding_site = associated_binding_site_I
        self.associated_rnase = associated_rnase_I
        self.common_name = common_name_I
        self.credits = credits_I
        self.data_source = data_source_I
        self.frame_id = frame_id_I
        self.ki = ki_I
        self.mechanism = mechanism_I
        self.mode = mode_I
        self.parent_classes = parent_classes_I
        self.pause_end_pos = pause_end_pos_I
        self.pause_start_pos = pause_start_pos_I
        self.physiologically_relevant = physiologically_relevant_I
        self.regulated_entity = regulated_entity_I
        self.regulator = regulator_I
        self.synonyms = synonyms_I
        self.database = database_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'name':self.name,
        'accessory_proteins':self.accessory_proteins,
        'anti_antiterm_end_pos':self.anti_antiterm_end_pos,
        'anti_antiterm_start_pos':self.anti_antiterm_start_pos,
        'antiterminator_end_pos':self.antiterminator_end_pos,
        'antiterminator_start_pos':self.antiterminator_start_pos,
        'associated_binding_site':self.associated_binding_site,
        'associated_rnase':self.associated_rnase,
        'common_name':self.common_name,
        'credits':self.credits,
        'data_source':self.data_source,
        'frame_id':self.frame_id,
        'ki':self.ki,
        'mechanism':self.mechanism,
        'mode':self.mode,
        'parent_classes':self.parent_classes,
        'pause_end_pos':self.pause_end_pos,
        'pause_start_pos':self.pause_start_pos,
        'physiologically_relevant':self.physiologically_relevant,
        'regulated_entity':self.regulated_entity,
        'regulator':self.regulator,
        'synonyms':self.synonyms,
        'database':self.database,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())