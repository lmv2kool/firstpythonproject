from simpleRESTproject.restclientmodule import ScopesRESTClient
from simpleRESTproject.restclientmodule import SoftVIMRESTClient

__author__ = 'vivekl'


class SCMAlgorithm:
    def __init__(self):
        print('init')

    def execute(self):
        scope_reg_rest_client = ScopesRESTClient()
        softvim_rest_client = SoftVIMRESTClient()
        scope_id = scope_reg_rest_client.fetch_scope_id_from_scope_registry('TC_08')
        scope_elements = scope_reg_rest_client.fetch_scope_elements_from_scope_registry(scope_id)


if __name__ == '__main__':
    algorithm = SCMAlgorithm()
    '''client.fetch_scopes('PCI_scope')'''
    algorithm.execute()
