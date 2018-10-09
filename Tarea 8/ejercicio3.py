import urllib2
from astropy.io import fits 
import numpy as np 
import matplotlib.pyplot as plt  
from matplotlib.colors import LogNorm 
import os 


#link hacia el archivo
link = ('https://fits.gsfc.nasa.gov/nrao_data/samples/hst/w0ck0101t_c0h.fit.gz')
#lo renombramos
name = ('archivo.gz')
#lo descargamos
desc = urllib2.urlopen(link)

save = file(name,'w')
#escribimos mientras se descarga el archivo
save.write(desc.read())
save.close()
#verificamos el archivo descargado 
print os.listdir('.')

hdu = fits.open('archivo.gz')



