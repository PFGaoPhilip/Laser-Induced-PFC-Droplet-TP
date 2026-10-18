from figs_c1a import FIGS as A
from figs_c1b import FIGS as B
from figs_c1c import FIGS as C
# Legacy drawing functions retain their original physical cases. Select them
# through this explicit final-ID map after deleting the old dissipation case.
FIGS = {old if old < 12 else old - 1: fn
        for old, fn in {**A, **B, **C}.items() if old != 12}
