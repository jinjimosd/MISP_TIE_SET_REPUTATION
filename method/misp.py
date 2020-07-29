#./bin/python3
# -*- coding: utf-8 -*-\
#
# Author: TruongBLX

import urllib3
import sys


from pymisp import ExpandedPyMISP, PyMISP, MISPEvent
from configparser import ConfigParser
from method.threat import Threat

urllib3.disable_warnings()


class Misp(Threat):
    def __init__(self):
        parser = ConfigParser()
        parser.read("config/misp_key.ini")
        misp_url = parser.get("MISP_KEY_INFO", "misp_url") 
        misp_key = parser.get("MISP_KEY_INFO", "misp_key") 
        misp_verifycert =False

        #connect to MISP
        self.misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)

    #set new event to MISP
    def set_event(self):
        pass

    #return list attributes with correct type hash
    def get_hash_attributes(self, type_hash):
        try:
            #search list events is published 
            events = self.misp.search(published = True)
            #create list to add new threat objects
            list_hash = []

            for event in events:              
                for attribute in event['Event']['Attribute']:
                    #check all attribute has type is equal with type hash
                    if attribute['type'] == type_hash:
                        #display info attribute
                        print('STATUS: Found {0} {1} in Event {2}.'
                            .format(type_hash, str(attribute['value']), str(event['Event']['id'])))
                        #add new threat object to list
                        list_hash.append(Threat(str(attribute['value']), str(event['Event']['id'])))
                
                for objects in event['Event']['Object']:
                    for attribute in objects['Attribute']:
                        #check all attribute has type is equal with type hash
                        if attribute['type'] == type_hash:
                            #display info attribute
                            print('STATUS: Found {0} {1} in Event {2}.'
                                  .format(type_hash, str(attribute['value']), str(event['Event']['id']))) 
                            #add new threat object to list
                            list_hash.append(Threat(str(attribute['value']), str(event['Event']['id'])))

            return list_hash

        except Exception as e:
            exc_tb = sys.exc_info()
            print('ERROR: Error in {location}.{funct_name}() - line {line_no} : {error}'
                  .format(location=__name__, funct_name=sys._getframe().f_code.co_name, line_no=exc_tb.tb_lineno,
                          error=str(e)))
            return None
