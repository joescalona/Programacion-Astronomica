import numpy as np 
import matplotlib.pyplot as plt 

date, temperature = np.loadtxt('py4sci_wed/data/munich_temperatures_average_with_bad_data.txt', unpack = True) 
keep = np.abs(temperature) < 90 
date = date[keep]
temperature = temperature[keep]

i = 0 

#---------------------------------------------
d2003 = []
while int(date[i])%2003. == 0.:
	d2003.append(date[i])
	i = i+1
keep10 = (np.abs(date)<2004)*(np.abs(date)>2003)
t2003 = temperature[keep10]
#---------------------------------------------
d2004 = []
while int(date[i])%2004. == 0.:
	d2004.append(date[i])
	i = i+1
keep11 = (np.abs(date)<2005)*(np.abs(date)>2004)
t2004 = temperature[keep11]
#---------------------------------------------
d2005 = []
while int(date[i])%2005. == 0.:
	d2005.append(date[i])
	i = i+1
keep12 = (np.abs(date)<2006)*(np.abs(date)>2005)
t2005 = temperature[keep12]
#---------------------------------------------
d2006 = []
while int(date[i])%2006. == 0.:
	d2006.append(date[i])
	i = i+1
keep13 = (np.abs(date)<2007)*(np.abs(date)>2006)
t2006 = temperature[keep13]
#---------------------------------------------
d2007 = []
while int(date[i])%2007. == 0.:
	d2007.append(date[i])
	i = i+1
keep14 = (np.abs(date)<2008)*(np.abs(date)>2007)
t2007 = temperature[keep14]
#---------------------------------------------
d2008 = []
while int(date[i])%2008. == 0.:
	d2008.append(date[i])
	i = i+1
keep15 = (np.abs(date)<2009)*(np.abs(date)>2008)
t2008 = temperature[keep15]
#---------------------------------------------
d2008 = []
while int(date[i])%2008. == 0.:
	d2008.append(date[i])
	i = i+1
keep15 = (np.abs(date)<2009)*(np.abs(date)>2008)
t2008 = temperature[keep15]
#---------------------------------------------
d2009 = []
while int(date[i])%2009. == 0.:
	d2009.append(date[i])
	i = i+1
keep16 = (np.abs(date)<2010)*(np.abs(date)>2009)
t2009 = temperature[keep16]
#---------------------------------------------
d2010 = []
while int(date[i])%2010. == 0.:
	d2010.append(date[i])
	i = i+1
keep17 = (np.abs(date)<2011)*(np.abs(date)>2010)
t2010 = temperature[keep17]
#---------------------------------------------
d2011 = []
while int(date[i])%2011. == 0.:
	d2011.append(date[i])
	i = i+1
keep18 = (np.abs(date)<2012)*(np.abs(date)>2011)
t2011 = temperature[keep18]
#---------------------------------------------
d2012 = []
while int(date[i])%2012. == 0.:
	d2012.append(date[i])
	i = i+1
keep19 = (np.abs(date)<2013)*(np.abs(date)>2012)
t2012 = temperature[keep19]






#ploteando funciones
plt.plot(range(len(t2003)),t2003,label = '2003')

plt.plot(range(len(t2004)),t2004,label = '2004')

plt.plot(range(len(t2005)),t2005,label = '2005')

plt.plot(range(len(t2006)),t2006,label = '2006')

plt.plot(range(len(t2007)),t2007,label = '2007')

plt.plot(range(len(t2008)),t2008,label = '2008')

plt.plot(range(len(t2009)),t2009,label = '2009')

plt.plot(range(len(t2010)),t2010,label = '2010')

plt.plot(range(len(t2011)),t2011,label = '2011')

plt.plot(range(len(t2012)),t2012,label = '2012')

plt.legend(loc=8)

#configurando plot
plt.xlabel('Dias')
plt.ylabel('Temperatura')
plt.savefig('1_part2.pdf') 
