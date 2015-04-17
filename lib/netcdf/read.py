def read(filename):
    import numpy as np
    from numpy import ma
    # from Scientific.IO.NetCDF import NetCDFFile
    from scipy.io.netcdf import netcdf_file as NetCDFFile
    """
    read a netcdf file and return a dictionnary with 
    key: name of the variables: value (array)
    array is masked is missing_values defined 
    in the netcdf 
    """

    nc = NetCDFFile(filename, 'r') # open it for writing 

    #     number of dimensions 
    #     ndim = nc.dimensions.__len__()
    #     dim_dict = nc.dimensions

    var_dict = {}

    for i in nc.variables.iterkeys():
        exec("cdf_var = nc.variables['" + i + "']")
        #exec(i + " = nc.variables['" + i + "'].getValue()")
        exec(i + " = nc.variables['" + i + "'][...]")
        exec(i + " = np.squeeze(" + i + ")")
        if '_FillValue' in dir(cdf_var):
            miss_val = np.float(cdf_var._FillValue)
            exec(i + " = ma.masked_values(" + i + ",miss_val)")
        if 'FillValue' in dir(cdf_var):
            miss_val = np.float(cdf_var.FillValue)
            exec(i + " = ma.masked_values(" + i + ",miss_val)")
        if '_missing_value' in dir(cdf_var):
            miss_val = np.float(cdf_var._missing_value)
            exec(i + " = ma.masked_values(" + i + ",miss_val)")
        if 'missing_value' in dir(cdf_var):
            miss_val = np.float(cdf_var.missing_value)
            exec(i + " = ma.masked_values(" + i + ",miss_val)")
        exec("var_dict['"+ i + "'] = " + i + ".astype(np.float32)")
    nc.close()
    return var_dict
