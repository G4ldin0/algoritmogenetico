import matplotlib.pyplot as plt
import numpy as np

plotPoints = []

def gerarGrafico():
   fig, ax = plt.subplots(layout='constrained')
   ax.plot(plotPoints)
   ax.set_title("Melhor resultado por geração")
   ax.set_label("grafico")
   ax.set_xlabel("geração")
   ax.set_ylabel("melhor resultado")
   ax.grid(True)
   plt.show()