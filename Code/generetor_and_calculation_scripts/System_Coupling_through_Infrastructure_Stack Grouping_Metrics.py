import os
import shutil
from itertools import product
from collections import defaultdict
from plant_uml_renderer import PlantUMLGenerator
from metamodels.component_metamodel import componentMetamodelViews
from metamodels.microservice_components_metamodel import *
from codeable_models import *
from metamodels.component_metamodel import *
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
        numberInfrStack = 0
        numberEnvironments = 0
        numberStorageresources = 0
        stackContainersConnectors = 0
        numberServicesStack = 0
        stackElementsConnectors= 0
        stackWebServerConnectors = 0
        stackStorageConnectors = 0
        databasetoContainerConnectors = 0
        pubsubtoContainerConnectors = 0

        containerList = []
        serviceList = []
        containerHostList = []
        hostList = []
        visitedLinks = []
        containerStackList =[]
        stackList = []
        stackElemetsList = []
        stackStorageList = []
        stackWebServerList = []
        stackConteinerList = []
        storageIDlist = []
        storagetostacklist = []
        stacktostoragelist = []
        webservertostacklist = []
        stacktowebserverlist = []
        web_server_list = []
        conteiner_web_server_list = []
        name = None

        violation_MSD = False
        violation_SES = False
        violation_AGS = False
        violation_MICS = False
        micro_stack = False

        MSD = 0
        AGS = 0
        SES = 0
        CRE = 0
        SRE = 0
        MST = 0
        SPS = 0
        CPS = 0
        MICS_3 = 0

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
                if container_env_type in elementClass.stereotype_instances:
                    numberContainers +=1
                if service in elementClass.stereotype_instances and not external_component in elementClass.stereotype_instances and not facade in elementClass.stereotype_instances:
                    numberServices +=1
                if storage_resources_infrastructure_type in elementClass.stereotype_instances:
                    numberStorageResources +=1
                if web_server_infrastructure_type in elementClass.stereotype_instances:
                    numberWebServers +=1
                if infrastructure_stack_type in elementClass.stereotype_instances:
                    numberInfrStack +=1
                if staging_env_type in elementClass.stereotype_instances or production_env_type in elementClass.stereotype_instances or test_env_type in elementClass.stereotype_instances:
                    numberEnvironments +=1
                if storage_resources_infrastructure_type in elementClass.stereotype_instances:
                    numberStorageresources +=1
             

                for link in element.link_objects:   
                    if not link in visitedLinks:
                        visitedLinks.append(link)  
                        
                        if service in link.source.stereotype_instances and container_env_type in link.target.stereotype_instances:
                              servicesContainersConnectors +=1
                              containerID = link.target
                              serviceID = link.source
                              containerList.append(containerID)
                              serviceList.append(serviceID)
                        
                        if infrastructure_stack_type in link.source.stereotype_instances and container_env_type in link.target.stereotype_instances:
                              stackContainersConnectors +=1
                              containerID = link.target
                              stackID = link.source
                              containerStackList.append(containerID)
                              stackConteinerList.append(stackID)
                        
                        if defines_deployment_of_deployment_node_relation_type in link.stereotype_instances:
                              stackElementsConnectors +=1
                              stackElementsID = link.target
                              stackStID = link.source
                              stackElemetsList.append(stackElementsID)
                              stackList.append(stackStID)
                        
                        if storage_resources_infrastructure_type in link.source.stereotype_instances and container_env_type in link.target.stereotype_instances:
                              stackStorageConnectors +=1
                              stackStorageID = link.source
                              storageContainerID = link.target
                              stackStorageList.append(stackStorageID)
                              storageIDlist.append(storageContainerID)

                        if web_server_infrastructure_type in link.source.stereotype_instances and container_env_type in link.target.stereotype_instances:
                            containersHostsConnectors +=1
                            containerHostID = link.source
                            hostID = link.target
                            web_server_list.append(containerHostID)
                            conteiner_web_server_list.append(hostID)
                        
                        if database in link.source.stereotype_instances and container_env_type in link.target.stereotype_instances:
                            databasetoContainerConnectors += 1

                        if pub_sub_component in link.source.stereotype_instances and container_env_type in link.target.stereotype_instances:
                            pubsubtoContainerConnectors += 1
        
        #Services
        commonContainers =[]
        servicetostacklist = []
        stacktoservicelist = []
        for container_1 in containerList:
            if container_1 in containerStackList:
                commonContainers.append(container_1)
        stacktocontainerlist = list(zip(stackConteinerList, containerStackList))
        stack_unique_to_container_link  = []
        for elem in set(stackConteinerList):
            if stackConteinerList.count(elem) == 1:
                stack_unique_to_container_link.append(elem)
        number_stack_unique_to_container_link = len(stack_unique_to_container_link)
        stack_to_container_links = len(stackConteinerList)
        servicetocontainerlist = list(zip(serviceList, containerList))
    
        for i,j in stacktocontainerlist:
            for x,y in servicetocontainerlist:
                if j == y:
                    servicetostacklist.append(x)
                    stacktoservicelist.append(i)
        unifiedstacktoservicelist= list(zip(stacktoservicelist, servicetostacklist))
        number_of_services = len(list(list(set(servicetostacklist))))
        number_of_stack_connected_to_services = len(list(list(set(stacktoservicelist))))
        stack_to_services_links = len(servicetostacklist)
        stack_unique_to_service_links = []

        for elem in set(stacktoservicelist):
            if stacktoservicelist.count(elem) == 1:
                stack_unique_to_service_links.append(elem)
        number_stack_unique_to_service_links = len(stack_unique_to_service_links)
        #storage resources
        storage_to_container = list(zip(stackStorageList, storageIDlist))
        for i,j in stacktocontainerlist:
            for x,y in storage_to_container:
                if j == y:
                    storagetostacklist.append(x)
                    stacktostoragelist.append(i)
        stack_to_storage_resources = list(zip(stacktostoragelist, storagetostacklist))
        number_of_storage = len(list(list(set(storagetostacklist))))
        number_of_stack_connected_to_storage = len(list(list(set(stacktostoragelist))))
        stack_to_storage_links = len(list(list(set(storagetostacklist))))
       
        stack_unique_to_storage_links = []
        for elem in set(stacktostoragelist):
            if stacktostoragelist.count(elem) == 1:
                stack_unique_to_storage_links.append(elem)
        number_stack_unique_to_storage_links = len(list(list(set(stack_unique_to_storage_links))))
        
        #web servers 
        web_server_to_container = list(zip(web_server_list, conteiner_web_server_list))
        for i,j in stacktocontainerlist:
            for x,y in web_server_to_container:
                if j == y:
                    webservertostacklist.append(x)
                    stacktowebserverlist.append(i)
        stack_to_web_server_resources = list(zip(stacktowebserverlist, webservertostacklist))
        number_of_web_servers = len(list(list(set(stacktowebserverlist))))
        number_of_stack_connected_to_web_servers = len(list(list(set(stacktowebserverlist))))
        
        
        number_of_stack_elements = number_of_services + number_of_storage + number_of_web_servers
        number_of_services_related_stack_elements = number_of_storage

        #Number of unique client links   
        numberUniqueLinks = max(number_of_services, number_of_stack_connected_to_services) + stack_to_services_links
         #Monolith Stack
        if numberInfrStack == 1:
            MSD = 1.00
        else:
            MSD = 0.00

        #Application Group Stack  
        if MSD == 1.00:
            AGS = 0.00
        else:
            if number_of_stack_connected_to_services == 1:
                AGS = 1.00

        #AGS = (((number_of_services/number_of_stack_elements)/number_of_stack_connected_to_services) + ((number_of_storage/number_of_stack_elements)/number_of_stack_connected_to_storage))
       
        #Service Stack
        if MSD == 1.00:
            SES = 0.00
        else:
            if number_stack_unique_to_service_links == stack_to_services_links:
                SES = 1
            else:
                SES = 0

        #Micro Stack
        if MSD == 1.00:
            MST = 0.00
        else:
            if number_stack_unique_to_container_link == stack_to_container_links and number_stack_unique_to_storage_links == stack_to_storage_links:
                MST = 1.00
            else:
                MST = 0
            #MICS = (((number_of_services/number_of_stack_elements)/number_of_stack_connected_to_services) + ((number_of_starage/number_of_stack_elements)/number_of_stack_connected_to_storage) + ((number_of_web_servers/number_of_stack_elements)/number_of_stack_connected_to_web_servers))
        print(number_stack_unique_to_storage_links, stack_to_storage_links)
        SPS = number_stack_unique_to_service_links/stack_to_services_links
        CPS = number_stack_unique_to_storage_links/stack_to_storage_links


        print(f"{name!s}: \nMSD = {MSD!s}\nSES = {SES!s}\nAGS = {AGS!s}\nMST = {MST!s}\nSPS = {SPS!s}\nCPS = {CPS!s}\n")

    def countViewLists(self, viewLists):
        self.ans = []
        for viewList in viewLists:
            self.ans.append(self.deployment_strategy_decision(viewList))
        
deployment_strategy_violation_detection = deployment_strategy_violation()
deployment_strategy_violation_detection.countViewLists([S3Views, S1V1Views, S1V2Views,shocks_shop, shocks_shopV1,shocks_shopV2, robotShopViews, robotShopViewsV1,robotShopViewsV2 ]) 
