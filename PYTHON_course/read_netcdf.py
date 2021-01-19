import netCDF4 as nc
import numpy as np

fN = '/home/ssilje/PYTHON_course/pyvis/data/HadEX2_GSL.nc'


ncf = nc.Dataset(fN)

print(ncf)

# get all variables
print(ncf.variables.keys())

# get a variable from the file
ncf.variables['lon']



ncf.variables['time'].units


# get data of lon from the file
lon = ncf.variables['lon'][:]
# this is a numpy array
lon


# get data of lat from the file                                                                                                                                                  
lat = ncf.variables['lat'][:]
# this is a numpy array                                                                                                                                                          
lat


# load the trend
trend_masked = ncf.variables['trend'][:]

trend_masked


# example

ma = np.ma.array([0., 1, 2], mask=[True, False, False], fill_value=np.NaN)
ma



import xarray as xr

import numpy as np




ds = xr.open_dataset(fN)

ds


lat = ds['lat']
lat[:10]


lon = ds.lon
lon[:10]


lat = ds.lat
lat[:10]


lat.values[:10]

print(np.asarray(lat)[:10])

