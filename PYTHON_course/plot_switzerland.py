# load outline of switzerland
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import netCDF4 as nc

fN = 'pyvis/data/outline_switzerland.nc'
ch = xr.open_dataset(fN)

# =====================================
    
# load climatological station data

fN = 'pyvis/data/MCH_clim.nc'
clim = xr.open_dataset(fN)



mn = clim.prec.min()
mx = clim.prec.max()

p_scaled = ((clim.prec - mn) / (mx - mn)) * 200 + 50

#####PLOT 1 #############################################


#ax = plt.axes(projection=ccrs.PlateCarree())

#ax.plot(ch.lon, ch.lat, transform=ccrs.PlateCarree())
#h = ax.scatter(clim.lon, clim.lat, c=clim.temp, cmap='RdBu_r', vmax=8, vmin=-8, s=p_scaled, edgecolor='0.5',
#               transform=ccrs.PlateCarree(), zorder=3)

#ax.set_title('MeteoCH monthly station data, climatology"', fontsize=15);

#plt.colorbar(h)

##### END PLOT 1 #############################################


#####PLOT 2 #############################################



#f, axes = plt.subplots(2,1)
plt.figure(1)
ax0=plt.subplot(2,1,1, projection=ccrs.EuroPP())
ax0.plot(ch.lon, ch.lat, transform=ccrs.PlateCarree())
h = ax0.scatter(clim.lon, clim.lat, c=clim.temp, cmap='RdBu_r', vmax=8, vmin=-8, s=p_scaled, edgecolor='0.5',transform=ccrs.PlateCarree(), zorder=3)
ax0.set_title('MeteoCH monthly station data [proj=EuroPP]', fontsize=10);
plt.colorbar(h, label='Temperature [°C]')

ax1=plt.subplot(2,1,2,projection=ccrs.PlateCarree())
ax1.plot(ch.lon, ch.lat, transform=ccrs.PlateCarree())

h = ax1.scatter(clim.lon, clim.lat, c=clim.temp, cmap='RdBu_r', vmax=8, vmin=-8, s=p_scaled, edgecolor='0.5',transform=ccrs.PlateCarree(), zorder=3)
ax1.set_title('MeteoCH monthly station data [proj=PlateCarree]', fontsize=10);
plt.colorbar(h, label='Temperature [°C]')                                                                                  

"""
### Subfigure 1 --> Europpean projection

ax=axes[0]
projection = ccrs.EuroPP()
ax = plt.axes(projection=projection)


ax.plot(ch.lon, ch.lat, transform=ccrs.PlateCarree())


### Subfigure 2 --> PlateCarree projection
ax=axes[1]
plt.axes(projection=ccrs.PlateCarree())                                                                                                                                                     


"""
plt.show()

