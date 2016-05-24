
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete
from SBaaS_base.sbaas_template_query import sbaas_template_query
from .models_BioCyc_postgresql_models import *
class models_BioCyc_query(sbaas_template_query):
    def initialize_supportedTables(self):
        tables_supported = {
        'models_biocyc_regulation':models_biocyc_regulation,
        'models_biocyc_publications':models_biocyc_publications,
        'models_biocyc_enzymaticReactions':models_biocyc_enzymaticReactions,
        'models_biocyc_proteinFeatures':models_biocyc_proteinFeatures,
        'models_biocyc_pathways':models_biocyc_pathways,
        'models_biocyc_proteins':models_biocyc_proteins,
        'models_biocyc_reactions':models_biocyc_reactions,
        'models_biocyc_polymerSegments':models_biocyc_polymerSegments,
        'models_biocyc_compounds':models_biocyc_compounds,
        'models_biocyc_RNAs':models_biocyc_RNAs,
        }
        self.set_supportedTables(tables_supported)