import os
import dicttoxml
import shutil
from itertools import product
from collections import defaultdict
from plant_uml_renderer import PlantUMLGenerator
from metamodels.component_metamodel import componentMetamodelViews
from metamodels.microservice_components_metamodel import *
from codeable_models import *
from metamodels.component_metamodel import *
from metamodels.deployment_metamodel import *
from codeable_models.internal.commons import is_cobject

from iac_models.S1 import *
from iac_models.S1V1 import *
from iac_models.S1V2 import *
from iac_models.S2 import *
from iac_models.S2V1 import *
from iac_models.S2V2 import *
from iac_models.S3 import *
from iac_models.S3V1 import *
from iac_models.S3V2 import *

class deployment_strategy_violation(object):
    
    def deployment_strategy_decision(self, viewList):

        numberServices = 0
        numberContainers = 0
        numberStorageResources = 0
        numberWebServers = 0
        numberContainersLinkedClients = 0
        servicesContainersConnectors = 0
        containersHostsConnectors = 0
        shared_container_links = 0
        number_shared_containers = 0
        number_services_connected_containers = 0
        numberConnectors = 0
        numberComponents = 0
        numberDeploymentNodes = 0
        numberDeploymentsRelations = 0
        numberdeployment_node_relation = 0

        containerList = []
        serviceList = []
        HostContainerList = []
        hostList = []
        visitedLinks = []
        name = None

        violation = False
        host_dependency = False
        containerSharedLinks = False

        SEEC = 0
        SEE = 0

        for bundle, kwargs in zip(viewList[::2],viewList[1::2]):
            if name == None:
                name = bundle.name
                underscorePos = name.find("_")
                if underscorePos != -1:
                    name = name[:underscorePos]
           
            for element in bundle.elements:
                elementClass = element
                if is_cobject(element):
                    elementClass = element.class_object_class_
                if element.instance_of(component):
                    numberComponents = numberComponents + 1
                if element.instance_of(deployment_node):
                    numberDeploymentNodes = numberDeploymentNodes + 1
                if container_env_type in elementClass.stereotype_instances:
                    numberContainers = numberContainers + 1
                if service in elementClass.stereotype_instances and not external_component in elementClass.stereotype_instances and not facade in elementClass.stereotype_instances:
                    numberServices = numberServices + 1
                #if storage_resources_infrastructure_type in elementClass.stereotype_instances:
                  #  numberStorageResources= +1
                if web_server_infrastructure_type in elementClass.stereotype_instances:
                    numberWebServers = +1


                for link in element.link_objects:   
                    if not link in visitedLinks:
                        visitedLinks.append(link)  
                        if link.association == connectors_relation:                      
                             numberConnectors = numberConnectors + 1
                        if link.association == deployment_relation:                      
                             numberDeploymentsRelations = numberDeploymentsRelations + 1 
                        if link.association == deployment_node_relation:                      
                             numberdeployment_node_relation = numberdeployment_node_relation + 1 
                        if service in link.source.stereotype_instances and container_env_type in link.target.stereotype_instances:
                              servicesContainersConnectors +=1
                              containerID = link.target
                              serviceID = link.source
                              containerList.append(containerID)
                              serviceList.append(serviceID)

                        if web_server_infrastructure_type in link.source.stereotype_instances and container_env_type in link.target.stereotype_instances:
                            containersHostsConnectors +=1
                            containerHostID = link.source
                            hostID = link.target
                            HostContainerList.append(containerHostID)
                            hostList.append(hostID)

                        #Number of container/VMs components linked to Hosts(Web Servers)
                        if web_server_infrastructure_type in link.target.stereotype_instances:
                          if container_env_type in elementClass.stereotype_instances:
                             numberContainersLinkedClients += 1


        #Shared Containers Links
        shared_containers = []
        sum_shared_containers = 0
        number_services_connected_containers = len(set(containerList))
        for y in set(containerList):
            sum_shared_containers = containerList.count(y)
            if sum_shared_containers > 1:
                containerSharedLinks = True
                shared_containers.append(sum_shared_containers)
                number_shared_containers = len(shared_containers)
                shared_container_links = sum(shared_containers)

        print(shared_container_links, servicesContainersConnectors)

        if containerSharedLinks == True:
            SEEC = shared_container_links/servicesContainersConnectors
        if containerSharedLinks == False:
            SEEC = 0

        if containerSharedLinks == True:
            SEE = number_shared_containers/number_services_connected_containers
        if containerSharedLinks == False:
            SEE = 0


        print(f"{name!s}: \nNumber of Deployment Nodes = {numberDeploymentNodes!s} \nNumber of Deployments Connectors = {numberDeploymentsRelations!s} \nNumber of Deployments Nodes Connectors = {numberdeployment_node_relation!s} \nNumber of Components = {numberComponents!s} \nNumber of Connectors = {numberConnectors!s} \nSEEC = {SEEC!s}\nSEE = {SEE!s}\n")

    def countViewLists(self, viewLists):
        self.ans = []
        for viewList in viewLists:
            self.ans.append(self.deployment_strategy_decision(viewList))
        
deployment_strategy_violation_detection = deployment_strategy_violation()
deployment_strategy_violation_detection.countViewLists([S3Views, S1V1Views,S1V2Views, shocks_shop,shocks_shopV1,shocks_shopV2, robotShopViews, robotShopViewsV1, robotShopViewsV2])
