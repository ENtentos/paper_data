from plant_uml_renderer import PlantUMLGenerator

from iac_models.S1 import *
from iac_models.S1V1 import *
from iac_models.S1V2 import *

from iac_models.S2 import *
from iac_models.S2V1 import *
from iac_models.S2V2 import *

from iac_models.S3 import *
from iac_models.S3V1 import *
from iac_models.S3V2 import *

from metamodels.deployment_metamodel import *
from metamodels.component_metamodel import *
from metamodels.microservice_components_metamodel import *



generator = PlantUMLGenerator()
generator.directory = "../_generated"


generator.generate_class_models("deplyment_metamodel",deployment_metamodel_views)
generator.generate_class_models("component_metamodel",componentMetamodelViews)
generator.generate_class_models("system_metamodel",microservice_metamodel_views)

generator.generate_object_models("S1", shocks_shop)
generator.generate_object_models("S2", robotShopViews)
generator.generate_object_models("S3", S3Views)
generator.generate_object_models("CS1_V1", S1V1Views)
generator.generate_object_models("CS1_V2", S1V2Views)
generator.generate_object_models("CS2_V1", shocks_shopV1)
generator.generate_object_models("CS2_V2", shocks_shopV2)
generator.generate_object_models("CS3_V1", robotShopViewsV1)
generator.generate_object_models("CS3_V2", robotShopViewsV2)
