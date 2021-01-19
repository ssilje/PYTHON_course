#need to load:
# module load conda/2018 
# source activate iacpy3_2018

import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs

fN = 'pyvis/data/ARGO_ATL_20171230.nc'
ATL = xr.open_dataset(fN)

fN = 'pyvis/data/ARGO_IND_20171230.nc'
IND = xr.open_dataset(fN)

fN = 'pyvis/data/ARGO_PAC_20171230.nc'
PAC = xr.open_dataset(fN)

ATL


######## PLOT 1 ############


#projection = ccrs.PlateCarree()

#ax = plt.axes(projection=projection)

#ax.coastlines()

######## END PLOT 1 ############





######## PLOT 2 ############

#ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))

#ax.coastlines()

######## END PLOT 2 ############



######## PLOT 3 ############
#f, axes = plt.subplots(1, 2, subplot_kw=dict(projection=ccrs.PlateCarree()))

#for ax in axes:
#    ax.coastlines()

######## END PLOT 3 ############


######## PLOT 4 ############
f, axes = plt.subplots(3,1, subplot_kw=dict(projection=ccrs.PlateCarree()))

#ax = plt.axes(projection=ccrs.PlateCarree()) --> work

#ax.coastlines()

axes[0].coastlines()
axes[0].scatter(ATL.lon, ATL.lat)
axes[0].scatter(IND.lon, IND.lat)
axes[0].scatter(PAC.lon, PAC.lat)
axes[0].set_global()

opt = dict(color='green',s=10)
axes[1].coastlines()  
axes[1].scatter(ATL.lon, ATL.lat, **opt)
axes[1].scatter(IND.lon, IND.lat, **opt)
axes[1].scatter(PAC.lon, PAC.lat, **opt)
axes[1].set_global()

# when vmin,vmak is set, the range of plotting color used in colorbar
#opt = dict(s=10,vmin=0, vmax=25,)
opt = dict(s=10) 
axes[2].coastlines()
h=axes[2].scatter(ATL.lon, ATL.lat,c=ATL.TEMP, **opt)
h=axes[2].scatter(IND.lon, IND.lat,c=IND.TEMP, **opt)
h=axes[2].scatter(PAC.lon, PAC.lat,c=PAC.TEMP, **opt)
axes[2].set_global()
plt.colorbar(h)
plt.show()
######## END PLOT 4 ############



######## PLOT 5 ############


ax = plt.axes(projection=ccrs.Mollweide()) 
opt = dict(s=10,transform=ccrs.PlateCarree())
ax.coastlines()
h=ax.scatter(ATL.lon, ATL.lat,c=ATL.TEMP, **opt)
h=ax.scatter(IND.lon, IND.lat,c=IND.TEMP, **opt)
h=ax.scatter(PAC.lon, PAC.lat,c=PAC.TEMP, **opt)
ax.set_global()
plt.colorbar(h)
plt.show()

#ax = plt.axes(projection=ccrs.PlateCarree())











