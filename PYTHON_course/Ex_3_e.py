import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import mplotutils as mpu
import cartopy.util as cutil

fN = 'pyvis/data/cmip5_delta_pr_rcp85_map.nc'

# load data, omitting some unecessary variables
#pr = xr.open_dataset(fN, drop_variables=['proj', 'agree_sign', 'pval'])

pr = xr.open_dataset(fN)
lon, lat, hist, change= pr.lon.values, pr.lat.values, pr.hist.values, pr.pr_rel.values 
f = plt.figure()


ax0=plt.subplot(3,1,1, projection=ccrs.Robinson())
ax0.coastlines()
HIST, LON = cutil.add_cyclic_point(hist, lon)

h=ax0.contourf(LON, lat,HIST ,transform=ccrs.PlateCarree(), levels=np.arange(0,3100,1000), extend='both')

ax0.set_title('CMIP5 historical precipitation (pr)', fontsize=10);
#plt.colorbar(h, label='pr [mm]')          
ax0.set_global()

ax1=plt.subplot(3,1,2, projection=ccrs.Robinson())

ax1.coastlines()
CHANGE, LON = cutil.add_cyclic_point(change, lon)
colors = ['#8c510a', '#7fbc41']
h=ax1.contour(LON, lat,CHANGE ,transform=ccrs.PlateCarree(),levels=[-25,25],colors=colors)
cl = ax1.clabel(h,inline=False)
ax1.set_title('CMIP5 rel change precipitation (pr)', fontsize=10);
#plt.colorbar(h, label='pr [%]')          
ax1.set_global()

ax2=plt.subplot(3,1,3, projection=ccrs.Robinson())

ax2.coastlines()
CHANGE, LON = cutil.add_cyclic_point(change, lon)
colors = ['#8c510a', '#7fbc41']
h=ax2.contour(LON, lat,CHANGE ,transform=ccrs.PlateCarree(),levels=[-25,25],colors=colors)
cl = ax2.clabel(h,fmt='%1.0f %%')
ax2.set_title('CMIP5 rel change precipitation (pr)', fontsize=10);
#plt.colorbar(h, label='pr [%]')          
ax2.set_global()








plt.show()
