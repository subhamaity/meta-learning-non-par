# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:48:46 2019

@author: Subha Maity
"""

import numpy as np

class Meta_learning_non_par():
    
    def __init__(self, kernel = "gaussian"):
        self.kernel = kernel
        self.x = np.array([])
        
        