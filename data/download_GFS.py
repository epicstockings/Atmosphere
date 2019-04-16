# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:14:27 2019

@author: siwo1
"""

import urllib 
#import urllib2 
#import requests

def get_url(date,hour,foreHour,dis):
    defult_url = 'https://nomads.ncep.noaa.gov/cgi-bin/'
    factor1 = 'filter_gfs_0p%s.pl'%dis
    filename = 'file=gfs.t%sz.pgrb2full.0p%s.f%s'%(hour,dis,foreHour)
    factors = 'all_lev=on&var_CAPE=on&var_CIN=on&var_HGT=on&var_RH=on&var_TMP=on&var_UGRD=on&var_VGRD=on&subregion=&leftlon=80&rightlon=120&toplat=40&bottomlat=5'
    dirname = 'dir=%%2Fgfs.%s%s'%(date,hour)
    url = defult_url + factor1 + '?' + '&'.join([filename,factors,dirname])
    return url
print ("downloading with urllib" )
url = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p50.pl?file=gfs.t00z.pgrb2full.0p50.f000&all_lev=on&var_CAPE=on&var_CIN=on&var_HGT=on&var_RH=on&var_TMP=on&var_UGRD=on&var_VGRD=on&subregion=&leftlon=80&rightlon=120&toplat=40&bottomlat=5&dir=%2Fgfs.2019041600'  
print ("downloading with urllib")
#urllib.request.urlretrieve(url, "test.grib")
date = '20190416'
hour = '00'
foreHour = '000'
dis = '50'
url = get_url(date,hour,foreHour,dis)
print ("downloading with urllib")
urllib.request.urlretrieve(url, "%s%s.%s.%s.grib"%(date,hour,dis,foreHour))