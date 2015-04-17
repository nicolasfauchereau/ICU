def save_3D(filenameout,var,varname,lat,lon,miss_val,time_it):
    import numpy as np
    from scipy.io.netcdf import netcdf_file as NetCDFFile
    """
    savenetcdf_3D(filenameout,var,varname,lat,lon,miss_val,time_it)
    save a 3D (time,lat,lon) numpy array into netcdf
    arguments:
    filenameout: string 
    var: np.array
    varname: string
    lat: np.array 
    lon: np.array
    miss_val: real
    time_it: np.array (dtype=int)
    """

    n = NetCDFFile(filenameout, 'w',) # open it for writing 
    n.title = 'saved netcdf variable'

    n.createDimension('time',None)
    n.createDimension('lat',len(lat))
    n.createDimension('lon',len(lon))

    latitude = n.createVariable('lat','f',('lat',))
    latitude.longname = 'latitude'
    latitude.units = 'degrees_north'
    latitude[:] = lat[:].astype(np.float32)

    longitude = n.createVariable('lon','f',('lon',))
    longitude.longname = 'longitude'
    longitude.units = 'degrees_east'
    longitude[:] = lon[:].astype(np.float32)

    time =  n.createVariable('time','i',('time',))
    time.units = 'days since 1979-1-1 00:00:0.0'
    time.delta_t = '0000-00-01 00:00:00'

    varnc = n.createVariable(varname,'f',('time','lat','lon',))
    varnc.missing_value = np.array(miss_val,np.float32)
    varnc._FillValue = np.array(miss_val,np.float32)

    for l in range(0,var.shape[0]):
        time[l]=time_it[l,]
        varnc[l,:,:]=var[l,:,:].astype(np.float32)

    n.close()
