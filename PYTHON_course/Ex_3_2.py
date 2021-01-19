import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

import mplotutils as mpu


fN = 'pyvis/data/cmip5_delta_pr_rcp85_map.nc'

# load data, omitting some unecessary variables
pr = xr.open_dataset(fN, drop_variables=['pr_rel', 'proj', 'agree_sign', 'pval'])

lon, lat, hist = pr.lon, pr.lat, pr.hist

print(pr.lon.values[:5])
print('Delta lon:', np.unique(np.diff(pr.lon.values)))

print()
print(pr.lat.values[:5])
print('Delta lat:', np.unique(np.diff(pr.lat.values)))

####### Method 1 to  create coordinates of edges ######

## lon goes from 1.25-358.75, with 2.5 distance
## lat goes from -88.75 - 88.75 with 2.5 distance
## LON goes from 0.  - 360.  with 2.5 distance
##LAT goes from -90. - 90.  with 2.5 distance
#LON = np.arange(0, 361, 2.5)
#LAT = np.arange(-90, 91, 2.5)

#ax = plt.axes(projection=ccrs.Robinson())
#ax.coastlines()

#h=ax.pcolormesh(LON, LAT, hist,transform=ccrs.PlateCarree())

#ax.set_global()
#ax.set_title('CMIP5 precipitation (pr)', fontsize=10);
#plt.colorbar(h, label='pr [mm]')          

####### End method 1 to  create coordinates of edges ######

####### Method 2 to  create coordinates of edges ######

ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines()
LON, LAT = mpu.infer_interval_breaks(lon, lat)
h=ax.pcolormesh(LON, LAT, hist,transform=ccrs.PlateCarree())

ax.set_global()
ax.set_title('CMIP5 precipitation (pr)', fontsize=10);
plt.colorbar(h, label='pr [mm]')          







plt.show()
