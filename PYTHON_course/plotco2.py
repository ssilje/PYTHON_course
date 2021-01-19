import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np


#%matplotlib inline


x = np.arange(0, 3 * np.pi, 0.01)

y = np.sin(x)


# name of the data file
fN = '/home/ssilje/PYTHON_course/pyvis/data/co2.nc'

ncf = nc.Dataset(fN)

year = ncf.variables['year'][:]
co2 = ncf.variables['co2_annual'][:]

print(year[:3])
print(co2[:3])



#f, ax = plt.subplots()
#plt.plot(x, y)
#plt.show()
# adjusting the resolution 
#f.savefig('figure_300.png', dpi=300)



f, ax = plt.subplots()
plt.plot(year, co2)
#plt.show()
# adjusting the resolution                                                                                                                                                       
f.savefig('figure_co2.png', dpi=300)




f, ax = plt.subplots()

ax.plot(x, y + 0, color='green')            # specify color by name
ax.plot(x, y + 1, color='b')                # color code (rgbcmyk)
ax.plot(x, y + 2, color='0.75')             # Greyscale between 0 and 1
ax.plot(x, y + 3, color='#1c9099')          # Hex code (RRGGBB from 00 to FF)
ax.plot(x, y + 4, color=(1.0,0.2,0.3))      # RGB tuple, values 0 to 1
ax.plot(x, y + 5, color=(1.0,0.2,0.3, 0.5)) # RGB tuple including alpha channel (transparency)
ax.plot(x, y + 6, color='chartreuse');      # all HTML color names supported

ax.plot(x, y + 7, color='none');            # 'none' stands for no color








f, ax = plt.subplots()

ax.plot(year, co2 + 0, color='green')            # specify color by name
ax.plot(year, co2 + 2, color='b')                # color code (rgbcmyk)
ax.plot(year, co2 + 4, color='0.75')             # Greyscale between 0 and 1
ax.plot(year, co2 + 6, color='#1c9099')          # Hex code (RRGGBB from 00 to FF)
ax.plot(year, co2 + 8, color=(1.0, 0.2, 0.3))    # RGB tuple, values 0 to 1



f, ax = plt.subplots()

ax.plot(x, x + 0, linestyle='solid')
ax.plot(x, x + 1, linestyle='dotted')
# using ls also works
ax.plot(x, x + 2, ls='dashdot')


ax.plot(x, x + 5, linestyle='-') # solid
ax.plot(x, x + 6, linestyle=':') # dotted
# using ls also works
ax.plot(x, x + 7, ls='-.') # dashdot





f, ax = plt.subplots()

ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')

# no label keyword -> no legend entry
ax.plot(x, x / 10)

ax.set_ylim(-1.1, 1.1)

ax.legend()




f, ax = plt.subplots(1, 1)

ax.plot(year, co2, color='0.1',linestyle='dotted',label='CO$_2$ concentration')
ax.set_xlabel('time [year]')
ax.set_ylabel('CO$_2$ [ppm]')
# add legend
ax.legend()
ax.set_title('Mauna Loa Weekly Atmospheric CO2 Data', fontsize=15);

ax.set_xlim(year[0], year[len(year)-1])
ax.set_ylim(min(co2), max(co2))

xtick=np.arange(year[0],year[len(year)-1],20) 

#for element in ac:
#    print(element)


xticklabels = [xtick[0], xtick[1], xtick[2]]
ax.set_xticks(xtick);
ax.set_xticklabels(xticklabels);




ytick=np.arange(320,380,20)
yticklabels = [ytick[0], ytick[1], ytick[2]]
ax.set_yticks(ytick);
ax.set_yticklabels(yticklabels);

plt.show()    







