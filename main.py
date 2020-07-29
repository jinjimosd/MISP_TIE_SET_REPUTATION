#./bin/python3
# -*- coding: utf-8 -*-\
#
# Author: TruongBLX

from method.misp import Misp
from method.tie import Tie

if __name__ == '__main__':
    misp = Misp()
    tie = Tie()
    list_hash = misp.get_hash_attributes("md5")
    tie.set_reputation(list_hash, "md5")

        