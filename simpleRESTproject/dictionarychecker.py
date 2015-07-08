__author__ = 'vivekl'

class DictionaryChecker:
    scopes = {
        'SCM_scope': ['PLMN-PLMN/RNC-148/WBTS-1/WCEL-1', 'PLMN-PLMN/RNC-148/WBTS-1/WCEL-2'],
        'CAC_scope': ['PLMN-PLMN/RNC-150/LNBTS-1/LNCEL-1', 'PLMN-PLMN/RNC-150/LNBTS-2/LNCEL-5'],
        'PCI_scope': ['PLMN-PLMN/RNC-150/LNBTS-2/LNCEL-3', 'PLMN-PLMN/RNC-150/LNBTS-2/LNCEL-1']
    }

    print(scopes['SCM_scope'])