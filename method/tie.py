#./bin/python3
# -*- coding: utf-8 -*-\
#
# Author: TruongBLX

# TIE Reputation Level following options:
# TrustLevel.KNOWN_TRUSTED_INSTALLER
# TrustLevel.KNOWN_TRUSTED
# TrustLevel.MIGHT_BE_TRUSTED
# TrustLevel.MOST_LIKELY_TRUSTED
# TrustLevel.UNKNOWN
# TrustLevel.MIGHT_BE_MALICIOUS
# TrustLevel.MOST_LIKELY_MALICIOUS
# TrustLevel.KNOWN_MALICIOUS
# TrustLevel.NOT_SET

import sys

from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig
from dxltieclient import TieClient
from dxltieclient.constants import TrustLevel

from method.threat import Threat

class Tie(Threat):
    def __init__(self):
        dxl_config = 'config/dxlclient.config'
        self.config = DxlClientConfig.create_dxl_config_from_file(dxl_config)
        

    #set list new reputations with hash string and trustlevel is KNOWN_MALICIOUS
    def set_reputation(self, list_hash, type_hash):
        try:
            with DxlClient(self.config) as client:
                client.connect()
                tie_client = TieClient(client)
    
                for new_threat in list_hash:
                    #set new reputation with hash string and trustlevel is KNOWN_MALICIOUS
                    tie_client.set_external_file_reputation(
                        TrustLevel.KNOWN_MALICIOUS,
                        {type_hash: new_threat.hash_string},
                        filename='MISP Hash {0}'.format(str(new_threat.name)),
                        comment='External Reputation set via OpenDXL')

                    print('SUCCESS: Successfully pushed {0} {1} to TIE.'.format(type_hash, str(new_threat.hash_string)))

        except Exception as e:
            exc_tb = sys.exc_info()
            print('ERROR: Error in {location}.{funct_name}() - line {line_no} : {error}'
                  .format(location=__name__, funct_name=sys._getframe().f_code.co_name, line_no=exc_tb.tb_lineno,
                          error=str(e)))
    

