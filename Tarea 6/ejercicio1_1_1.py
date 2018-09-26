import numpy as np 
import matplotlib.pyplot as plt 

date, temperature = np.loadtxt('py4sci_wed/data/munich_temperatures_average_with_bad_data.txt', unpack = True) 
keep = np.abs(temperature) < 90 
date = date[keep]
temperature = temperature[keep]

i = 0 

#-----------------------------------------------
d1995 = []

while int(date[i])%1995.==0.:
	d1995.append(date[i])
	i = i + 1 

keep2 = np.abs(date)<=1996 

t1995 = temperature[keep2]
#-------------------------------------------------

i = 0
d1996 = []
while int(date[i])%1996.==0:
	d1996.append(date[i])
	i = i+1
keep3 = (np.abs(date)<1997)*(np.abs(date)>1996)
t1996 = temperature[keep3]

#------------------------------------------------
d1997 = []
while int(date[i])%1997. == 0.:
	d1997.append(date[i])
	i = i+1 
keep4 = (np.abs(date)<1998)*(np.abs(date)>1997)
t1997 = temperature[keep4]

#----------------------------------------------
d1998 = []
while int(date[i])%1998. == 0.:
	d1998.append(date[i])
	i = i+1
keep5 = (np.abs(date)<1999)*(np.abs(date)>1998)
t1998 = temperature[keep5]

#---------------------------------------------
d1999 = []
while int(date[i])%1999. == 0.:
	d1999.append(date[i])
	i = i+1
keep6 = (np.abs(date)<2000)*(np.abs(date)>1999)
t1999 = temperature[keep6]

#---------------------------------------------
d2000 = []
while int(date[i])%2000. == 0.:
	d2000.append(date[i])
	i = i+1
keep7 = (np.abs(date)<2001)*(np.abs(date)>2000)
t2000 = temperature[keep7]
#---------------------------------------------
d2001 = []
while int(date[i])%2001. == 0.:
	d2001.append(date[i])
	i = i+1
keep8 = (np.abs(date)<2002)*(np.abs(date)>2001)
t2001 = temperature[keep8]
#---------------------------------------------
d2002 = []
while int(date[i])%2002. == 0.:
	d2002.append(date[i])
	i = i+1
keep9 = (np.abs(date)<2003)*(np.abs(date)>2002)
t2002 = temperature[keep9]







#ploteando funciones
plt.plot(range(len(t1996)),t1996,label = '1996')

plt.plot(range(len(t1995)),t1995,label='1995')

plt.plot(range(len(t1997)),t1997,label='1997')

plt.plot(range(len(t1998)),t1998,label='1998')

plt.plot(range(len(t1999)),t1999,label='1999')

plt.plot(range(len(t2000)),t2000,label='2000')

plt.plot(range(len(t2001)),t2001,label='2001')

plt.plot(range(len(t2002)),t2002,label='2002')


plt.legend(loc=8)

#configurando plot
plt.xlabel('Dias')
plt.ylabel('Temperatura')
plt.savefig('1_part1.pdf')


