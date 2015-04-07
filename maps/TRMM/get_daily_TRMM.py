#!/Users/nicolasf/anaconda/bin/python                                                                                  
# -*- coding: utf-8 -*-
# ==================================================================================
# code get_daily_TRMM.py
# Description: download TRMM 3B42 RT binary files for
# TAGS:3B42:wget:datetime
# created on 2012-04-11
# Nicolas Fauchereau <Nicolas.Fauchereau@gmail.com>
# ==================================================================================

import sys, os, glob
import numpy as np
from numpy import ma
from string import rjust
import datetime
from netCDF4 import num2date, Dataset
import pandas as pd

sys.path.append(os.path.join(os.environ['HOME'],"pythonlibs"))

### ==============================================================================================================
### SOME DEFINITIONS 

### paths and all 

dpath = os.path.join(os.environ['HOME'],'data/TRMM/daily/')

### parameters for the domain to extract 
nlat = 400
nlon = 1440

### create lat and lon vectors
lon = np.arange(0.125, 0.125 + nlon * 0.25, 0.25) 
lat = np.arange(-59.875, -59.875 + nlat * 0.25, 0.25)

### set the domain we want [lonW, lonE, latS, latN]
domain = [135., 240., -50., 10.]

ilon = np.where( (lon >= domain[0]) & (lon <= domain[1]))[0]
ilat = np.where( (lat >= domain[2]) & (lat <= domain[3]))[0]

lon = lon[ilon]
lat = lat[ilat]

### ==============================================================================================================
### get the date of today, and subtract 1 days

today = datetime.datetime.utcnow()

### delay to real time in days 
### usually the day before at 10:05
delay = 1

date = today - datetime.timedelta(days=delay)

### ==============================================================================================================
### construct the files name

fname = "3B42RT_daily.%s.bin" % ( date.strftime('%Y.%m.%d') )

from netcdf import save_3D_stack

### ==============================================================================================================
### download the file
os.system("curl --silent ftp://disc2.nascom.nasa.gov/data/TRMM/Gridded/Derived_Products/3B42RT/Daily/" + str(fname.split(".")[1]) + "/"+ fname +" -o " + os.path.join(dpath,fname))

### ==============================================================================================================
### convert from binary to NetCDF
trmm_data = (np.fromfile(os.path.join(dpath,fname), dtype=np.float32, count=nlat*nlon).byteswap()).reshape((nlat,nlon))

print("converting " + dpath + "/" + fname + " from Binary to NetCDF")

### ==============================================================================================================
### select domain [lonW, lonE, latS, latN]
trmm_data = np.take(np.take(trmm_data,ilat,axis=0),ilon,axis=1)

origin = datetime.datetime(1979,1,1,0,0,0)
idays = (date - origin).days

### ==============================================================================================================
### save in NetCDF
trmm_data = trmm_data[np.newaxis,:,:]
save_3D_stack(dpath+"3B42RT_daily.%s.%s.%s.nc" \
        % ( date.strftime('%Y'),   date.strftime('%m'), date.strftime('%d')),\
        trmm_data,'trmm',lat,lon,-99999.0,np.array(idays))
os.remove(os.path.join(dpath,fname))
