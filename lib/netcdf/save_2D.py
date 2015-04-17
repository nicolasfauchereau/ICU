def save_2D(filenameout,var,lat,lon,miss_val):
    import numpy as np
    from scipy.io.netcdf import netcdf_file as NetCDFFile

    n = NetCDFFile(filenameout, 'w',) # open it for writing 
    n.title = 'saved netcdf variable'

    n.createDimension('lat',len(lat))
    n.createDimension('lon',len(lon))

    latitude = n.createVariable('lat','f',('lat',))
    latitude.longname = 'latitude'
    latitude.units = 'degrees_north'
    latitude[:] = lat.astype(np.float32)

    longitude = n.createVariable('lon','f',('lon',))
    longitude.longname = 'longitude'
    longitude.units = 'degrees_east'
    longitude[:] = lon[:].astype(np.float32)

    varnc = n.createVariable('varnc','f',('lat','lon',))
    varnc.missing_value = np.array(miss_val,np.float32)
    varnc.FillValue = np.array(miss_val,np.float32)

    varnc[:,:]=var[:,:].astype(np.float32)

    n.close()
