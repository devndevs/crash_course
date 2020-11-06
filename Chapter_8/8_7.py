import shirts

from shirts import make_shirt
print()
make_shirt("Imported goods", " Large")

from shirts import make_shirt as ms
print()
ms("Abriviated Import" , "extra small")

import shirts as sh

from shirts import *

