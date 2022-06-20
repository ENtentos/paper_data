from codeable_models import *
from metamodels.deployment_metamodel import *

from metamodels.microservice_components_metamodel import *


awsServer = CClass(device, 'ELK Server 0.0.0.0/0', stereotype_instances=[cloud_server_device_type])
webserver0_0_0_0= CClass(infrastructure_resources, 'Webserver 0.0.0.0', stereotype_instances=[web_server_infrastructure_type])


mongo= CClass(infrastructure_resources, 'Mongo DB', stereotype_instances=[storage_resources_infrastructure_type])
user_mongo= CClass(infrastructure_resources, 'User Mongo DB', stereotype_instances=[storage_resources_infrastructure_type])
catalog_mysql= CClass(infrastructure_resources, 'MySQL DB', stereotype_instances=[storage_resources_infrastructure_type])


kibana = CClass(component, 'Kibana', stereotype_instances=[monitoring_dashboard])
elasticsearch = CClass(component, 'Elasticsearch', stereotype_instances=[monitoring_component])


#environments
staging_env = CClass(execution_environment, "Staging Environment", stereotype_instances = [staging_env_type])
production_env = CClass(execution_environment, "Production Environment", stereotype_instances = [production_env_type])
test_env = CClass(execution_environment, "Production Environment", stereotype_instances = [test_env_type])

#stacks
stack_1 = CClass(infrastructure_resources, 'Stack 1', stereotype_instances=[infrastructure_stack_type])
stack_2 = CClass(infrastructure_resources, 'Stack 2', stereotype_instances=[infrastructure_stack_type])


#dockerContainer_shipping = CClass(execution_environment, 'Docker Container 0.0.4.8', stereotype_instances=[container_env_type])
#dockerContainer_catalog = CClass(execution_environment, 'Docker Container 0.0.3.5', stereotype_instances=[container_env_type])
dockerContainer_order = CClass(execution_environment, 'Docker Container 0.0.4.7', stereotype_instances=[container_env_type])
dockerContainer_payment = CClass(execution_environment, 'Docker Container 0.0.4.3', stereotype_instances=[container_env_type])
#dockerContainer_cart = CClass(execution_environment, 'Docker Container 0.0.4.8', stereotype_instances=[container_env_type])
dockerContainer_user = CClass(execution_environment, 'Docker Container 0.0.4.4', stereotype_instances=[container_env_type])
dockerContainer_api = CClass(execution_environment, 'Docker Container 0.0.3.12', stereotype_instances=[container_env_type])
dockerContainer_queue_master = CClass(execution_environment, 'Docker Container 0.0.3.1', stereotype_instances=[container_env_type])
dockerContainer_rabbitmq = CClass(execution_environment, 'Docker Container 0.3.6.8', stereotype_instances=[container_env_type])
dockerContainer_mongoDB = CClass(execution_environment, 'Docker Container 0.0.3.4', stereotype_instances=[container_env_type])
dockerContainer_userDB = CClass(execution_environment, 'Docker Container 0.0.4.0', stereotype_instances=[container_env_type])
dockerContainer_catalogDB = CClass(execution_environment, 'Docker Container 0.0.3.0', stereotype_instances=[container_env_type])
dockerContainer_edge_router = CClass(execution_environment, 'Docker Container 0.0.1.1', stereotype_instances=[container_env_type])

#dockerContainer_tool = CClass(execution_environment, 'Docker Container tools', stereotype_instances=[container_env_type])

add_links({kibana: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({elasticsearch: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
'''
add_links({stack : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack : mongo}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack : catalog_mysql}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({stack : user_mongo}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
'''
add_links({stack_1 : [test_env, production_env, staging_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({stack_2 : [test_env, production_env, staging_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])

#add_links({kibana: [test_env, production_env, staging_env]}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
#add_links({elasticsearch: [test_env, production_env, staging_env]}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

add_links({mongo: dockerContainer_mongoDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({user_mongo: dockerContainer_userDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({catalog_mysql: dockerContainer_catalogDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])

#add_links({dockerContainer_shipping: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
#add_links({dockerContainer_catalog: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_order: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_payment: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_user: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
#add_links({dockerContainer_cart: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_api: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_rabbitmq: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_queue_master: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_mongoDB: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_userDB: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_catalogDB: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_edge_router: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
#add_links({dockerContainer_tool: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])

#add_links({webserver0_0_0_0: dockerContainer_shipping}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
#add_links({webserver0_0_0_0: dockerContainer_catalog}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_order}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_payment}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_user}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
#add_links({webserver0_0_0_0: dockerContainer_cart}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_api}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_rabbitmq}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_queue_master}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_mongoDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_userDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_catalogDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_edge_router}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
#add_links({webserver0_0_0_0: dockerContainer_tool}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])

add_links({test_env: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({production_env: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({staging_env: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])


add_links({stack_1: [
dockerContainer_mongoDB,
dockerContainer_userDB,
dockerContainer_catalogDB,
dockerContainer_edge_router

]}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])

add_links({stack_2: [
dockerContainer_user,
dockerContainer_api,
dockerContainer_rabbitmq,
dockerContainer_queue_master,
dockerContainer_order,
dockerContainer_payment
]}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])


#Microservice
browser = CClass(component, "Browser", stereotype_instances = client)
apiGateway = CClass(component, "APIGateway", stereotype_instances = [service])
catalog = CClass(component, "Catalog Service", stereotype_instances = service)
shippingService = CClass(component, "Shipping Service", stereotype_instances = service)
user = CClass(component, "Login Service", stereotype_instances = service)
order = CClass(component, "Order Service", stereotype_instances = service)
payment = CClass(component, "Payment Service", stereotype_instances = service)
cart = CClass(component, "Cart Service", stereotype_instances = service)
qmaster = CClass(component, "Queue-Master Service", stereotype_instances = service)

#DBS
userDB = CClass(component, "Usert DB", stereotype_instances = database)
orderDB = CClass(component, "Order DB", stereotype_instances = database)
cartDB = CClass(component, "Cart DB", stereotype_instances = database)
catalogDB = CClass(component, "Catalog DB", stereotype_instances = database)
broker = CClass(component, "RabbitMQ", stereotype_instances = [pub_sub_component])

add_links({browser: apiGateway}, role_name = "target", stereotype_instances = [https])
add_links({apiGateway: [catalog, order, user, cart]}, role_name = "target", stereotype_instances = [restful_http])
add_links({order: [shippingService]}, role_name = "target", stereotype_instances = [restful_http])

add_links({user: userDB, cart: cartDB, order: orderDB, catalog: catalogDB},
          role_name = "target", stereotype_instances = database_connector)

add_links({shippingService: broker},
         role_name="target", stereotype_instances = [publisher, subscriber],
         tagged_values={'publishes': ["shipping"], 'subscribesTo': ["shipping"]})
add_links({qmaster: broker},
         role_name = "target", stereotype_instances = [publisher, subscriber],
         tagged_values = {'publishes': ["shipping"], 'subscribesTo': ["shipping"]})

#deployemnts

add_links({user: dockerContainer_user}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalog: dockerContainer_order}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({order: dockerContainer_order}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({cart: dockerContainer_order}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({payment: dockerContainer_payment}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({shippingService: dockerContainer_payment}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({qmaster: dockerContainer_queue_master}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({orderDB: dockerContainer_mongoDB}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({cartDB: dockerContainer_mongoDB}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalogDB: dockerContainer_catalogDB}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({userDB: dockerContainer_userDB}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({broker: dockerContainer_rabbitmq}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({apiGateway: dockerContainer_api}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

add_links({user: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalog: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({order: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({cart: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({payment: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({shippingService: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({qmaster: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({orderDB: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({cartDB: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalogDB: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({userDB: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({broker: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({apiGateway: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[runs_on_deployment_relation_type])


add_links({userDB: [user_mongo, mongo, catalog_mysql]}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

#add_links({orderDB: mongo}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
#add_links({cartDB: mongo}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
#add_links({catalogDB: catalog_mysql}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

add_links({user_mongo: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({mongo: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({catalog_mysql: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])

#Views
_all = CBundle("S2V2", elements = awsServer.class_object.get_connected_elements())


shocks_shopV2 = [
    
    _all, {},
    #terraform, {},
     
]


