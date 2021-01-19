import matplotlib.pyplot as plt
import numpy as np
import netCDF4 as nc




# load data

fN = '/home/ssilje/PYTHON_course/pyvis/data/cmip5_tas_rcp85_ts.nc'

ncf = nc.Dataset(fN)

# the with construct automatically closes the dataset once we are done
with nc.Dataset(fN) as ncf:
    
    year = ncf.variables['year'][:]
    tas = ncf.variables['tas'][:]




# calculate the anomaly with respect to 1971..2000

# select all years in this range
sel = (year >= 1971) & (year <= 2000)

# calculate the climatology for each model
clim = tas[:, sel].mean(axis=1)

# calculate the anomaly

# we need to add an axis such that the broadcasting works
tas_anom = tas - clim[:, np.newaxis]



#mmm = tas_anom.mean(axis=0)

#np.shape(tas_anom) --> returns the dimension of a matrix

#shape of tas_anom: (40, 231)
#mmm = tas_anom.mean(axis=0) --> mmm--> dim (231,)
#mmm = tas_anom.mean(axis=1) --> mmm--> dim (40,)



mmm = tas_anom.mean(axis=0) 




f, ax = plt.subplots(1, 1)

ax.plot(year, mmm, color='0.1',linestyle='solid',label='tas mmm',linewidth=4)
ax.set_xlabel('time [year]')
ax.set_ylabel('tas [C$^\circ$]')
# add legend
ax.legend()
ax.set_title('Multi model mean temperature', fontsize=15);

#ax.set_xlim(year[0], year[len(year)-1])
#ax.set_ylim(min(co2), max(co2))

#xtick=np.arange(year[0],year[len(year)-1],1) 
#xtick=np.array([year[0], year[(len(year)-1)/2], year[len(year)-1]])
a = (len(year)-1)/2
print(a)
xtick=np.array([year[0], year[int(a)], year[len(year)-1]])
xticklabels=[xtick[0], xtick[1], xtick[2]]


ax.set_xticks(xtick);
ax.set_xticklabels(xticklabels);
#ytick=np.arange(,380,20)
#ytick=np.array([mm[0], year[int(a)], year[len(year)-1]])
#yticklabels = [ytick[0], ytick[1], ytick[2]]
#ax.set_yticks(ytick);
#ax.set_yticklabels(yticklabels);




f, ax = plt.subplots(1, 1)

ax.plot(year, mmm, color='0.1',linestyle='solid',label='tas mmm',linewidth=4)
ax.set_xlabel('time [year]')
ax.set_ylabel('tas [C$^\circ$]')
# add legend                                                                                                                                                                     
ax.legend()
ax.set_title('Multi model mean temperature', fontsize=15);


ax.axhline(0, color='0.1', lw=0.5)

ax.axvspan(1971, 2000, color='0.75')


plt.show()    



