#SBaaS
from .models_BioCyc_query import models_BioCyc_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class models_BioCyc_io(models_BioCyc_query,
                    sbaas_template_io):
    pass;