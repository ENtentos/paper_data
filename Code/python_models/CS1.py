from codeable_models import *
from metamodels.deployment_metamodel import *

from metamodels.microservice_components_metamodel import *

elkServer = CClass(device, 'Elk Server', stereotype_instances=[cloud_server_device_type])

elkServer = CClass(device, 'ELK Server 0.0.0.0/0', stereotype_instances=[cloud_server_device_type])
webserver0_0_0_0= CClass(infrastructure_resources, 'Webserver 127.0.0.1', stereotype_instances=[web_server_infrastructure_type])


baske_data= CClass(infrastructure_resources, 'MySQL DB', stereotype_instances=[storage_resources_infrastructure_type])
identity_data= CClass(infrastructure_resources, 'MySQL DB', stereotype_instances=[storage_resources_infrastructure_type])
marketing_data= CClass(infrastructure_resources, 'noSQL DB', stereotype_instances=[storage_resources_infrastructure_type])
payment_data= CClass(infrastructure_resources, 'MySQL DB', stereotype_instances=[storage_resources_infrastructure_type])
location_data= CClass(infrastructure_resources, 'MySQL DB', stereotype_instances=[storage_resources_infrastructure_type])
catalog_data= CClass(infrastructure_resources, 'MySQL DB', stereotype_instances=[storage_resources_infrastructure_type])

#environments
production_env = CClass(execution_environment, "INSTANA_AGENT_HOST", stereotype_instances = [production_env_type])
test_env = CClass(execution_environment, "Production Environment", stereotype_instances = [test_env_type])

#stacks
stack_web = CClass(infrastructure_resources, 'Web Stack', stereotype_instances=[infrastructure_stack_type])
stack_wmsapi = CClass(infrastructure_resources, 'Mobile API Stack', stereotype_instances=[infrastructure_stack_type])
stack_wwsapi = CClass(infrastructure_resources, 'Web API Stack', stereotype_instances=[infrastructure_stack_type])
stack_spa_web_app = CClass(infrastructure_resources, 'SPA Web App Stack', stereotype_instances=[infrastructure_stack_type])
stack_web_app_mvc = CClass(infrastructure_resources, 'Web App MVC Stack', stereotype_instances=[infrastructure_stack_type])
stack_basket_api = CClass(infrastructure_resources, 'Web Basket API Stack', stereotype_instances=[infrastructure_stack_type])
stack_basket_data = CClass(infrastructure_resources, 'Web Basket Data Stack', stereotype_instances=[infrastructure_stack_type])
stack_identity_api = CClass(infrastructure_resources, 'Identity API Stack', stereotype_instances=[infrastructure_stack_type])
stack_identity_data = CClass(infrastructure_resources, 'Identity Data Stack', stereotype_instances=[infrastructure_stack_type])
stack_marketing_api = CClass(infrastructure_resources, 'Marketing API Stack', stereotype_instances=[infrastructure_stack_type])
stack_marketing_data = CClass(infrastructure_resources, 'Marketing Data Stack', stereotype_instances=[infrastructure_stack_type])
stack_payment_api = CClass(infrastructure_resources, 'Payment API Stack', stereotype_instances=[infrastructure_stack_type])
stack_payment_data = CClass(infrastructure_resources, 'Payment Data Stack', stereotype_instances=[infrastructure_stack_type])
stack_rabbit = CClass(infrastructure_resources, 'RabbitMQ Stack', stereotype_instances=[infrastructure_stack_type])
stack_location_api = CClass(infrastructure_resources, 'Location API Stack', stereotype_instances=[infrastructure_stack_type])
stack_location_data = CClass(infrastructure_resources, 'Location Data Stack', stereotype_instances=[infrastructure_stack_type])
stack_catalog_api = CClass(infrastructure_resources, 'Catalog API Stack', stereotype_instances=[infrastructure_stack_type])
stack_catalog_data = CClass(infrastructure_resources, 'Catalog Data Stack', stereotype_instances=[infrastructure_stack_type])
stack_order_api = CClass(infrastructure_resources, 'Order Stack', stereotype_instances=[infrastructure_stack_type])

dockerContainer_web = CClass(execution_environment, 'Docker Container Web', stereotype_instances=[container_env_type])
dockerContainer_basket = CClass(execution_environment, 'Docker Container Basket', stereotype_instances=[container_env_type])
dockerContainer_catalog = CClass(execution_environment, 'Docker Container Catalog', stereotype_instances=[container_env_type])
dockerContainer_identity = CClass(execution_environment, 'Docker Container Identity', stereotype_instances=[container_env_type])
dockerContainer_ordering = CClass(execution_environment, 'Docker Container Ordering', stereotype_instances=[container_env_type])
dockerContainer_payment = CClass(execution_environment, 'Docker Container Payment', stereotype_instances=[container_env_type])
dockerContainer_mvc = CClass(execution_environment, 'Docker Container MVC', stereotype_instances=[container_env_type])
dockerContainer_spa = CClass(execution_environment, 'Docker Container SPA', stereotype_instances=[container_env_type])
dockerContainer_mapi = CClass(execution_environment, 'Docker Container Mobile API', stereotype_instances=[container_env_type])
dockerContainer_api = CClass(execution_environment, 'Docker Container API', stereotype_instances=[container_env_type])
dockerContainer_location = CClass(execution_environment, 'Docker Container Location', stereotype_instances=[container_env_type])
dockerContainer_marketing = CClass(execution_environment, 'Docker Container Marketing', stereotype_instances=[container_env_type])
dockerContainer_rabbit = CClass(execution_environment, 'Docker Container RabbitMQ', stereotype_instances=[container_env_type])

dockerContainer_catalog_data  = CClass(execution_environment, 'Docker Container Catalaog Data', stereotype_instances=[container_env_type])
dockerContainer_location_data = CClass(execution_environment, 'Docker Container Location Data', stereotype_instances=[container_env_type])
dockerContainer_payment_data = CClass(execution_environment, 'Docker Container Payment Data', stereotype_instances=[container_env_type])
dockerContainer_marketing_data = CClass(execution_environment, 'Docker Container Marketing Data', stereotype_instances=[container_env_type])
dockerContainer_identity_data = CClass(execution_environment, 'Docker Container Identity Data', stereotype_instances=[container_env_type])
dockerContainer_basket_data = CClass(execution_environment, 'Docker Container Basket Data', stereotype_instances=[container_env_type])

'''
add_links({baske_data: dockerContainer_basket}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({marketing_data: dockerContainer_marketing}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({identity_data: dockerContainer_identity}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({payment_data: dockerContainer_payment}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({location_data: dockerContainer_location}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({catalog_data: dockerContainer_catalog}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
'''

add_links({stack_order_api : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_order_api : [test_env,production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_wmsapi : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_wwsapi : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_wmsapi : [test_env,production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_wwsapi : [test_env,production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_spa_web_app : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_spa_web_app : [test_env,production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_web_app_mvc : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_web_app_mvc : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_basket_api : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_basket_api : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_rabbit : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_rabbit : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_marketing_api : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_marketing_api : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_marketing_data : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_marketing_data : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_payment_api : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_payment_api : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_payment_data : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_payment_data : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_location_api : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_location_api : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_location_data : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_location_data : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_catalog_api : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_catalog_api : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_catalog_data : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_catalog_data : [test_env, production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])


add_links({dockerContainer_web: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_basket: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_catalog: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_identity: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_payment: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_ordering: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_mvc: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_api: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_spa: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_mapi: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_location: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_marketing: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_rabbit: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])


add_links({webserver0_0_0_0: dockerContainer_basket}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_web}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_catalog}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_identity}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_payment}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_ordering}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_api}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_mvc}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_spa}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_mapi}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_location}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_marketing}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])

add_links({baske_data: dockerContainer_basket_data}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({location_data: dockerContainer_location_data}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({catalog_data: dockerContainer_catalog_data}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({identity_data: dockerContainer_identity_data}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({marketing_data: dockerContainer_marketing_data}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({payment_data: dockerContainer_payment_data}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])


add_links({test_env: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({production_env: elkServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])

add_links({stack_web : dockerContainer_web}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_wmsapi : dockerContainer_mapi}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_wwsapi : dockerContainer_api}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_spa_web_app : dockerContainer_mvc}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_web_app_mvc : dockerContainer_spa}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_order_api : [dockerContainer_ordering]}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_rabbit : dockerContainer_rabbit}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_basket_data : dockerContainer_basket_data}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_basket_api : dockerContainer_basket}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_identity_api : dockerContainer_identity}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_identity_data : dockerContainer_identity_data}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_marketing_api : dockerContainer_marketing}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_marketing_data : dockerContainer_marketing_data}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_payment_api : dockerContainer_payment}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_payment_data : dockerContainer_payment_data}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_location_api : dockerContainer_location}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_location_data : dockerContainer_location_data}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_catalog_api : dockerContainer_catalog}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack_catalog_data : dockerContainer_catalog_data}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])


#Microservice
#clients_facades
mobile_app = CClass(component, "Mobile App", stereotype_instances = web_ui)
traditional_web_app = CClass(component, "Traditional Web App", stereotype_instances = web_ui)
spa_web_app = CClass(component, "SPA Web App", stereotype_instances = web_ui)
web_app_mvc = CClass(component, "WebApp MVC", stereotype_instances = web_ui)

web_client_gateway = CClass(component, "Web Client Gateway", stereotype_instances = [facade])
mobile_gateway = CClass(component, "Mobile Gateway", stereotype_instances = [facade])

#system_services
marketing_service = CClass(component, "Marketing Service", stereotype_instances = service)
identity_service = CClass(component, "Identity Service", stereotype_instances = service)
basket_service = CClass(component, "Basket Service", stereotype_instances = service)
order_service = CClass(component, "Order Service", stereotype_instances = service)
locations_service = CClass(component, "Locations Service", stereotype_instances = service)
catalog_service = CClass(component, "Catalog Service", stereotype_instances = service)
payment_service = CClass(component, "Payment Service", stereotype_instances = service)

event_bus = CClass(component, "Event Bus", stereotype_instances = [pub_sub_component, event_sourcing])

#databases
marketing_db = CClass(component, "Marketing DB", stereotype_instances = sql_server)
identity_db = CClass(component, "identity DB", stereotype_instances = sql_server)
basket_db = CClass(component, "Basket DB", stereotype_instances = redis_db)
order_db = CClass(component, "Order DB", stereotype_instances = sql_server)
locations_db = CClass(component, "Locations DB", stereotype_instances = mongo_db)
catalog_db = CClass(component, "Catalog DB", stereotype_instances = sql_server)

#services_links
add_links({mobile_app: mobile_gateway}, role_name = "target", stereotype_instances = restful_http)
add_links({spa_web_app: web_client_gateway}, role_name = "target", stereotype_instances = restful_http)
add_links({traditional_web_app: web_app_mvc},role_name = "target", stereotype_instances = [http,https])
add_links({web_app_mvc: web_client_gateway}, role_name = "target", stereotype_instances = restful_http)


add_links({web_client_gateway: [marketing_service, identity_service, basket_service, order_service, locations_service, catalog_service, payment_service]},role_name = "target", stereotype_instances = [asynchronous_connector, restful_http])
add_links({mobile_gateway: [marketing_service, identity_service, basket_service, order_service, locations_service, catalog_service, payment_service]},role_name = "target", stereotype_instances = [asynchronous_connector, restful_http])

add_links({marketing_service: identity_service}, role_name = "target", stereotype_instances = [restful_http, linked_to_middleware_handler], tagged_values= {"handler": "ASP.NET Identity"})
add_links({basket_service: identity_service}, role_name = "target", stereotype_instances = [restful_http, linked_to_middleware_handler], tagged_values= {"handler": "ASP.NET Identity"})
add_links({order_service: identity_service}, role_name = "target", stereotype_instances = [restful_http, linked_to_middleware_handler], tagged_values= {"handler": "ASP.NET Identity"})
add_links({locations_service: identity_service}, role_name = "target", stereotype_instances = [restful_http, linked_to_middleware_handler], tagged_values= {"handler": "ASP.NET Identity"})
add_links({catalog_service: identity_service}, role_name = "target", stereotype_instances = [restful_http, linked_to_middleware_handler], tagged_values= {"handler": "ASP.NET Identity"})
add_links({payment_service: identity_service}, role_name = "target", stereotype_instances = [restful_http, linked_to_middleware_handler], tagged_values= {"handler": "ASP.NET Identity"})

add_links({marketing_service: event_bus}, role_name = "target", stereotype_instances = subscriber,tagged_values = {"subscribesTo": ["userLocationUpdated"]})
add_links({basket_service: event_bus}, role_name = "target", stereotype_instances = [publisher, subscriber],tagged_values = {"publishes": ["userCheckout"], "subscribesTo": ["product", "orderStarted"]})
add_links({order_service: event_bus}, role_name = "target", stereotype_instances = [publisher, subscriber],tagged_values = {"publishes": ["orderStatus", "orderStarted", "gracePeriod"],"subscribesTo": ["orderPayment", "orderStock", "userCheckout", "gracePeriod"]})
add_links({locations_service: event_bus}, role_name = "target", stereotype_instances = [publisher],tagged_values = {"publishes": ["userLocationUpdated"]})
add_links({catalog_service: event_bus}, role_name = "target", stereotype_instances = [publisher, subscriber],tagged_values = {"publishes": ["product", "orderStock"], "subscribesTo": ["orderStatus"]})
add_links({payment_service: event_bus}, role_name = "target", stereotype_instances = [publisher, subscriber],tagged_values = {"publishes": ["orderPayment"], "subscribesTo": ["orderStatus"]})


#database_links
add_links({marketing_service: marketing_db,identity_service: identity_db, basket_service: basket_db,locations_service: locations_db,catalog_service: catalog_db,order_service: order_db},role_name = "target", stereotype_instances = database_connector)



#deployemnts
add_links({mobile_app: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({traditional_web_app: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({spa_web_app: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({web_app_mvc: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({web_client_gateway: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({mobile_gateway: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({marketing_service: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({identity_service: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({basket_service: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({order_service: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({locations_service: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalog_service: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({payment_service: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({event_bus: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])


add_links({mobile_app: dockerContainer_mapi}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({traditional_web_app: dockerContainer_api}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({spa_web_app: dockerContainer_spa}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({web_app_mvc: dockerContainer_mvc}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({web_client_gateway: dockerContainer_web}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({mobile_gateway: dockerContainer_web}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({marketing_service: dockerContainer_marketing}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({identity_service: dockerContainer_identity}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({basket_service: dockerContainer_basket}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({order_service: dockerContainer_ordering}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({locations_service: dockerContainer_location}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalog_service: dockerContainer_catalog}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({payment_service: dockerContainer_payment}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({event_bus: dockerContainer_rabbit}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])


add_links({marketing_db: marketing_data}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({identity_db: identity_data}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalog_db: catalog_data}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

add_links({basket_db: baske_data}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({order_db: payment_data}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({locations_db: location_data}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

#Views

_all = CBundle("S1", elements = elkServer.class_object.get_connected_elements())
S3Views = [_all, {},]


