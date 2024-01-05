# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:14:07 2024

@author: gawe
"""

import pyqtgraph as pg

# ========================= #

if hasattr(pg, 'GraphicsWindow'):
    # GraphicsWindow = pg.GraphicsWindow

    class GraphicsWindow(pg.GraphicsWindow):
        def show(self):
            pass

elif hasattr(pg, 'GraphicsLayoutWidget'):
    # GraphicsWindow = pg.GraphicsLayoutWidget

    class GraphicsWindow(pg.GraphicsLayoutWidget):
        def __init__(self, *args, **kwargs):
            super(GraphicsWindow, self).__init__(*args, show=True, **kwargs)

# ========================= #