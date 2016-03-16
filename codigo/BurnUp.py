from matplotlib import pyplot as plt
import numpy as np

class Sprint:
    def __init__(self):
        self.meta = []
        self.trabalho=[]
        self.sprint=9 

    def add_meta(self, meta):        
        self.meta.append(meta)

    def add_trabalho(self, trabalho):        
    	self.trabalho.append(trabalho)

    def mudar_sprint(self, sprint):        
    	self.sprint=sprint

    def grafico(self,meta,trabalho,sprint):

		x = np.arange(sprint)
		y = np.arange(sprint)

		with plt.style.context('fivethirtyeight'):
		    plt.plot(x, np.array(meta))
		    plt.plot(y, np.array(trabalho))

		plt.show() 

