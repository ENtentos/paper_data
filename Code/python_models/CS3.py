from codeable_models import *
from metamodels.deployment_metamodel import *

from metamodels.microservice_components_metamodel import *

#deployment components
awsServer = CClass(device, 'AWS Server 0.0.0.0/0', stereotype_instances=[cloud_server_device_type])
webserver0_0_0_0= CClass(infrastructure_resources, 'Webserver 0.0.0.0', stereotype_instances=[web_server_infrastructure_type])
logstash = CClass(component, 'Logstash', stereotype_instances=[logging_component])
fluentd = CClass(component, 'Fluentd', stereotype_instances=[monitoring_dashboard])

mongo= CClass(infrastructure_resources, 'Mongo DB', stereotype_instances=[storage_resources_infrastructure_type])
mysql= CClass(infrastructure_resources, 'MySQL DB', stereotype_instances=[storage_resources_infrastructure_type])


#environments
production_env = CClass(execution_environment, "INSTANA_AGENT_HOST", stereotype_instances = [production_env_type])
test_env = CClass(execution_environment, "Production Environment", stereotype_instances = [test_env_type])

#stacks
app_stack = CClass(infrastructure_resources, 'Application Stack', stereotype_instances=[infrastructure_stack_type])
tool_stack = CClass(infrastructure_resources, 'Tool Stack', stereotype_instances=[infrastructure_stack_type])



dockerContainer_web = CClass(execution_environment, 'Docker Container Web', stereotype_instances=[container_env_type])
dockerContainer_ratings = CClass(execution_environment, 'Docker Container Web', stereotype_instances=[container_env_type])
dockerContainer_catalog = CClass(execution_environment, 'Docker Container Catalog', stereotype_instances=[container_env_type])
dockerContainer_dispatch = CClass(execution_environment, 'Docker Container Dispatch', stereotype_instances=[container_env_type])
dockerContainer_shipping = CClass(execution_environment, 'Docker Container Shipping', stereotype_instances=[container_env_type])
dockerContainer_payment = CClass(execution_environment, 'Docker Container Payment', stereotype_instances=[container_env_type])
dockerContainer_cart = CClass(execution_environment, 'Docker Container Cart', stereotype_instances=[container_env_type])
dockerContainer_user = CClass(execution_environment, 'Docker Container User', stereotype_instances=[container_env_type])
dockerContainer_api = CClass(execution_environment, 'Docker Container API', stereotype_instances=[container_env_type])
dockerContainer_rabbitmq = CClass(execution_environment, 'Docker Container RabbitMQ', stereotype_instances=[container_env_type])
dockerContainer_mongoDB = CClass(execution_environment, 'Docker Container Mongo DB', stereotype_instances=[container_env_type])
dockerContainer_mysqlDB = CClass(execution_environment, 'Docker Container MySQL DB', stereotype_instances=[container_env_type])
dockerContainer_userDB = CClass(execution_environment, 'Docker Container User DB', stereotype_instances=[container_env_type])
dockerContainer_catalogDB = CClass(execution_environment, 'Docker Container Catalog DB', stereotype_instances=[container_env_type])
dockerContainer_shippingDB = CClass(execution_environment, 'Docker Container Shipping DB', stereotype_instances=[container_env_type])
dockerContainer_payment_fix = CClass(execution_environment, 'Docker Container Paypal', stereotype_instances=[container_env_type])

add_links({mongo: dockerContainer_mongoDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({mysql: dockerContainer_mysqlDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])

dockerContainer_load = CClass(execution_environment, 'Docker Container Load', stereotype_instances=[container_env_type])
dockerContainer_fluentd = CClass(execution_environment, 'Docker Container Fluentd', stereotype_instances=[container_env_type])

add_links({logstash: dockerContainer_mongoDB}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({fluentd: dockerContainer_mysqlDB}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

add_links({app_stack : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : [test_env,production_env]}, role_name="to", stereotype_instances=[includes_deployment_node_relation_type])
add_links({tool_stack : webserver0_0_0_0}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])


add_links({dockerContainer_shipping: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_web: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_catalog: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_shippingDB: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_payment: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_user: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_cart: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_api: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_rabbitmq: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_mysqlDB: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_mongoDB: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_userDB: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_catalogDB: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_dispatch: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_ratings: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_load: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_fluentd: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({dockerContainer_payment_fix: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])

add_links({webserver0_0_0_0: dockerContainer_shipping}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_web}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_catalog}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_shippingDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_payment}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_cart}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_api}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_rabbitmq}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_mysqlDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_mongoDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_userDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_catalogDB}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_dispatch}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_ratings}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_load}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_fluentd}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])
add_links({webserver0_0_0_0: dockerContainer_payment_fix}, role_name="to", stereotype_instances=[deployed_on_deployment_node_relation_type])

add_links({test_env: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({production_env: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])

add_links({app_stack : dockerContainer_web}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : dockerContainer_cart}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : dockerContainer_dispatch}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : [dockerContainer_payment, dockerContainer_payment_fix]}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : dockerContainer_rabbitmq}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : dockerContainer_ratings}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : dockerContainer_shipping}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : dockerContainer_user}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : dockerContainer_catalog}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : [dockerContainer_catalogDB, dockerContainer_mongoDB, dockerContainer_userDB]}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({app_stack : dockerContainer_mysqlDB}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({tool_stack : dockerContainer_fluentd}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])
add_links({tool_stack : dockerContainer_load}, role_name="to", stereotype_instances=[defines_deployment_of_deployment_node_relation_type])


#microservices
cart = CClass(component, 'Cart', stereotype_instances = [service])
catalogue = CClass(component, 'Catalogue', stereotype_instances = [service])
dispatch = CClass(component, 'Dispatch', stereotype_instances = [service])
payment = CClass(component, 'Payment', stereotype_instances = [service])
ratings = CClass(component, 'Ratings', stereotype_instances = [service])
shipping = CClass(component, 'Shipping', stereotype_instances = [service])
user = CClass(component, 'User', stereotype_instances = [service])
NGINXAPIGateway = CClass(component, 'NGINX API Gateway', stereotype_instances = [facade])

add_links({NGINXAPIGateway: catalogue}, role_name = "target", stereotype_instances = [restful_http])
add_links({NGINXAPIGateway: user}, role_name = "target", stereotype_instances = [restful_http])
add_links({NGINXAPIGateway: cart}, role_name = "target", stereotype_instances = [restful_http])
add_links({NGINXAPIGateway: shipping}, role_name = "target", stereotype_instances = [restful_http])
add_links({NGINXAPIGateway: payment}, role_name = "target", stereotype_instances = [restful_http])
add_links({NGINXAPIGateway: ratings}, role_name = "target", stereotype_instances = [restful_http])
RESTAPIClient = CClass(component, 'REST API Client', stereotype_instances = [client])
add_links({RESTAPIClient: NGINXAPIGateway}, role_name = "target", stereotype_instances = [restful_http])
webUIClient = CClass(component, 'Web UI Client', stereotype_instances = [web_ui])
add_links({webUIClient: NGINXAPIGateway}, role_name = "target", stereotype_instances = [http])
add_links({cart: catalogue}, role_name = "target", stereotype_instances = [restful_http, asynchronous_connector])
cartandAnonymousUserCountDB = CClass(component, 'Cart and Anonymous User Count DB', stereotype_instances = [database])
add_links({cart: cartandAnonymousUserCountDB}, role_name = "target", stereotype_instances = [database_connector],
          tagged_values = {"read": ["cart"], "write": ["cart"]})
add_links({user: cartandAnonymousUserCountDB}, role_name = "target", stereotype_instances = [database_connector],
          tagged_values = {"read": ["anonymous-counter"], "write": ["anonymous-counter"]})
cartPrometheusMonitor = CClass(component, 'Cart Prometheus Monitor', stereotype_instances = [service])
add_links({cart: cartPrometheusMonitor}, role_name = "target", stereotype_instances = [in_memory_connector])
catalogueUsersOrdersDB = CClass(component, 'Catalogue Users Orders DB', stereotype_instances = [database])
add_links({catalogue: catalogueUsersOrdersDB}, role_name = "target", stereotype_instances = [database_connector],
          tagged_values = {"read": ["products"], "write": ["products"]})
add_links({user: catalogueUsersOrdersDB}, role_name = "target", stereotype_instances = [database_connector],
          tagged_values = {"read": ["users", "orders"], "write": ["users", "orders"]})
paypalPaymentGateway = CClass(component, 'Paypal Payment Gateway', stereotype_instances = [service, external_component])
add_links({payment: paypalPaymentGateway}, role_name = "target", stereotype_instances = [restful_http, synchronous_connector])
add_links({payment: user}, role_name = "target", stereotype_instances = [restful_http, synchronous_connector])
add_links({payment: cart}, role_name = "target", stereotype_instances = [restful_http, synchronous_connector])
paymentPrometheusMonitor = CClass(component, 'Payment Prometheus Monitor', stereotype_instances = [service])
add_links({payment: paymentPrometheusMonitor}, role_name = "target", stereotype_instances = [in_memory_connector])
instanaAgent = CClass(component, 'Instana Agent', stereotype_instances = [tracing_component, external_component])
add_links({cart: instanaAgent}, role_name = "target", stereotype_instances = [http2])
add_links({catalogue: instanaAgent}, role_name = "target", stereotype_instances = [http2])
add_links({dispatch: instanaAgent}, role_name = "target", stereotype_instances = [http2])
add_links({payment: instanaAgent}, role_name = "target", stereotype_instances = [http2])
add_links({user: instanaAgent}, role_name = "target", stereotype_instances = [http2])
rabbitMQ = CClass(component, 'Rabbit MQ', stereotype_instances = [message_broker])
add_links({payment: rabbitMQ}, role_name = "target", stereotype_instances = [message_producer],
          tagged_values = {'outChannels' : ['orders']})
add_links({dispatch: rabbitMQ}, role_name = "target", stereotype_instances = [message_consumer],
          tagged_values = {'inChannels' : ['orders']})
ratingsandShippingCitiesDB = CClass(component, 'Ratings and Shipping Cities DB', stereotype_instances = [database])
add_links({ratings: ratingsandShippingCitiesDB}, role_name = "target", stereotype_instances = [database_connector],
          tagged_values = {"read": ["ratings"],"write": ["ratings"]})
add_links({ratings: catalogue}, role_name = "target", stereotype_instances = [restful_http])
add_links({shipping: cart}, role_name = "target", stereotype_instances = [restful_http])
add_links({shipping: ratingsandShippingCitiesDB}, role_name = "target", stereotype_instances = [database_connector],
          tagged_values = {"read": ["cities", "codes"], "write":[]})


#deployemnts
add_links({catalogue: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({cart: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({dispatch: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({payment: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({shipping: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({NGINXAPIGateway: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({ratings: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({user: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({cartandAnonymousUserCountDB: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({rabbitMQ: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({ratingsandShippingCitiesDB: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({paypalPaymentGateway: webserver0_0_0_0}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

add_links({user: dockerContainer_user}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalogue: dockerContainer_catalog}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({dispatch: dockerContainer_dispatch}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({cart: dockerContainer_cart}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({payment: dockerContainer_payment}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({shipping: dockerContainer_shipping}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({ratings: dockerContainer_ratings}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({cartandAnonymousUserCountDB: dockerContainer_userDB}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({ratingsandShippingCitiesDB: dockerContainer_shippingDB}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalogueUsersOrdersDB: dockerContainer_catalogDB}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({rabbitMQ: dockerContainer_rabbitmq}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({NGINXAPIGateway: dockerContainer_api}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({paypalPaymentGateway: dockerContainer_payment_fix}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

add_links({cartandAnonymousUserCountDB: mongo}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({ratingsandShippingCitiesDB: mysql}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])
add_links({catalogueUsersOrdersDB: mongo}, role_name="deployment_nodes", stereotype_instances=[deployed_on_type])

add_links({mongo: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])
add_links({mysql: awsServer}, role_name="to", stereotype_instances=[runs_on_deployment_node_relation_type])

#Views
_all = CBundle("S3", elements=[awsServer, webserver0_0_0_0, user, catalogue,shipping,payment, cart, cartandAnonymousUserCountDB, ratingsandShippingCitiesDB, catalogueUsersOrdersDB, NGINXAPIGateway, rabbitMQ, test_env, production_env,dockerContainer_shipping, dockerContainer_payment_fix, app_stack, tool_stack,
dockerContainer_catalog,
dockerContainer_dispatch,
dockerContainer_payment,
dockerContainer_user,
dockerContainer_cart,
dockerContainer_api,
dockerContainer_rabbitmq,
dockerContainer_mongoDB,
dockerContainer_userDB,
dockerContainer_catalogDB,
dockerContainer_shippingDB,
dockerContainer_ratings, mongo,mysql
 ])

terraform = CBundle("IaC Deployment", elements=[awsServer, webserver0_0_0_0, test_env, production_env,dockerContainer_shipping, dockerContainer_payment_fix,
dockerContainer_catalog,
dockerContainer_dispatch,
dockerContainer_payment,
dockerContainer_user,
dockerContainer_cart,
dockerContainer_api,
dockerContainer_rabbitmq,
dockerContainer_mongoDB,
dockerContainer_userDB,
dockerContainer_catalogDB,
dockerContainer_shippingDB,
dockerContainer_ratings, mongo,mysql, app_stack, tool_stack ])

#robotShop = CBundle("RS",  elements = RESTAPIClient.class_object.get_connected_elements())
robotShopViews = [_all,{}, 
            #terraform, {}
            ]