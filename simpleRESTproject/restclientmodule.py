
__author__ = 'vivekl'

import logging
import logging.config
import json
import requests

class ScopesRESTClient:

    def __init__(self):
        self.__scope_rest_service_base_url = 'http://127.0.0.1:7711/api/scopes/get_scope?scope_name='
        self.__scope_reg_base_url = 'http://10.91.47.243:9080/ScopeRegistryService/v1/scopes'
        logging.config.fileConfig('logging.conf')
        self.__LOG = logging.getLogger('root')

    def fetch_scopes_from_rest_client(self, scope_name):
        target_link = self.__scope_rest_service_base_url + scope_name
        result = requests.get(target_link)
        logging.info('scope elements are ', result.text)

    def fetch_scope_id_from_scope_registry(self, scope_name='SCM'):
        result = requests.get(self.__scope_reg_base_url)
        scopes_details = json.loads(result.text)
        print(scopes_details)
        for scope_detail in scopes_details:
            dictionary_value = dict(scope_detail)
            if (dictionary_value.get('displayName')) == scope_name:
                return dictionary_value.get('itemsetId')

    def fetch_scope_elements_from_scope_registry(self, scope_id=4):
        url = self.__scope_reg_base_url + '/' + str(scope_id) + '/elements/resolve/unchecked'
        result = requests.get(url)
        scope_elements_json = json.loads(result.text)
        dict_of_scope_elements = dict(scope_elements_json)
        for scope_element in dict_of_scope_elements.get('resolvedScopeElements'):
            print(scope_element.get('elementId'))


class SoftVIMRESTClient:
    def __init__(self):
        self.__softvim_base_url = 'http://10.91.47.243:9080/softvimapp/v1/SoftVIM/1'
        logging.config.fileConfig('logging.conf')
        self.__LOG = logging.getLogger('restModulesLogger')

    def fetch_data(self):
        try:
            elements = requests.get(self.__softvim_base_url)
        except:
            self.__LOG.error('Error occurred while accessing SoftVIM')
            return

        elements_json = json.loads(elements.text)
        self.__LOG.info('Elements are: %s', elements_json)
        softvim_url_for_individual_elements = self.__softvim_base_url + '/' + elements_json[0] + '/children'

        individual_elements = requests.get(softvim_url_for_individual_elements)
        individual_elements_json = json.loads(individual_elements.text)
        self.__LOG.info('Individual elements are: %s', individual_elements_json)
