import xarray as xr

import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import numpy as np
import mplotutils as mpu
ds = xr.open_dataset('pyvis/data/wah_LH.nc')

f = plt.figure()
#####subplot PLOT 1
ax0=plt.subplot(3,1,1, projection=ccrs.PlateCarree())
ax0.coastlines()
ax0.pcolormesh(ds.lon, ds.lat, ds.LH, transform=ccrs.PlateCarree(), cmap='Reds')
ax0.set_extent([-30, 60, 10, 90], ccrs.PlateCarree())

#####subplot PLOT 2

ax1 = plt.subplot(3,1,2, projection=ccrs.PlateCarree())
ax1.coastlines()
ax1.pcolormesh(ds.global_lon, ds.global_lat, ds.LH, transform=ccrs.PlateCarree(), cmap='Reds')
ax1.set_extent([-30, 60, 10, 90], ccrs.PlateCarree())

#####subplot PLOT 3
ax2 = plt.subplot(3,1,3, projection=ccrs.PlateCarree())
# this is the EURO CORDEX POLE
pole_lon = ds.attrs['pole_lon'] # -162.0
pole_lat = ds.attrs['pole_lat'] # 39.25
transform = ccrs.RotatedPole(pole_longitude=pole_lon, pole_latitude=pole_lat)
ax2.coastlines()
LON, LAT = mpu.infer_interval_breaks(ds.lon, ds.lat)
ax2.pcolormesh(LON ,LAT, ds.LH, cmap='Reds', transform=transform)
ax2.set_extent([-30, 60, 10, 90], ccrs.PlateCarree())

plt.show()
