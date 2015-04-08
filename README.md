# Island Climate Update

This repository gathers scripts and notebooks used to generate various products
related to the [Island Climate Update (ICU)](http://www.niwa.co.nz/climate/icu).

The Island Climate Update is a monthly Regional Climate Outlook Forum and outlook
bulletin for the southwest Pacific.

go to:

[https://speakerdeck.com/nicolasf/icu-175](https://speakerdeck.com/nicolasf/icu-175)

To view examples of some of these products incorportated in the presentation material uploaded
on [speakerdeck](https://speakerdeck.com/) before the monthly ICU teleconference.

<hr size=5>

The scripts and [notebooks]() are written in the language [Python](www.python.org). They make
heavy use of the [**Python scientific stack**](http://www.scipy.org/about.html): i.e. in particular the following libraries:

+ [Numpy](http://www.numpy.org/)
+ [Scipy](http://www.scipy.org/)
+ [Pandas](http://pandas.pydata.org/)
+ [Matplotlib](http://matplotlib.org/)
+ [Basemap](http://matplotlib.org/basemap/)

To get all these working on your platform (Windows, Linux, Mac), I strongly recommend installing the [Anaconda Python distribution](https://store.continuum.io/cshop/anaconda/), developed and made available for free by [Continuum Analytics](http://continuum.io/).  

This github repository is organised in different sections:

**1. [mailing](https://github.com/nicolasfauchereau/ICU/blob/master/mail/)**

  generates the monthly mail sent to the ICU mailing list, with time of the teleconference
  translated in the different time-zones in the region.

  usage example:

  ```
  $ ./make_mail_ICU.py 175 2015 04 02 12 30
  ```

  generates the mail for the issue 175 of the ICU, teleconference to be held on the 2nd of April 2015 at 12:30 PM (assumes NZ time)

**2. [Climate Maps](https://github.com/nicolasfauchereau/ICU/blob/master/maps/)**

  + TRMM Rainfall [(Tropical Rainfall Measurement Mission)](https://climatedataguide.ucar.edu/climate-data/trmm-tropical-rainfall-measuring-mission)

    there are two versions:

    + one makes use of the images directly available from the [Nasa TRMM website](http://trmm.gsfc.nasa.gov), updated daily for the last 30 days averages and anomalies: the script downloads the image, crops it and
    overlay the image on a high resolution basemap of the southwest Pacific.

      + see [plot_sp_30days_im_averages.ipynb](http://nbviewer.ipython.org/github/nicolasfauchereau/ICU/blob/master/maps/TRMM/plot_sp_30days_im_averages.ipynb) for the last **30 days averages** map

      + see [plot_sp_30days_im_anoms.ipynb](http://nbviewer.ipython.org/github/nicolasfauchereau/ICU/blob/master/maps/TRMM/plot_sp_30days_im_anoms.ipynb) for the last **30 days anomalies** map

    + The other is based on the actual data available from [ftp://disc2.nascom.nasa.gov/data/TRMM/Gridded/Derived_Products/3B42RT/Daily/](ftp://disc2.nascom.nasa.gov/data/TRMM/Gridded/Derived_Products/3B42RT/Daily/), the whole process is
    constructed around a couple of scripts and notebooks:

      + [get_daily_TRMM.py](https://github.com/nicolasfauchereau/ICU/blob/master/maps/TRMM/get_daily_TRMM.py) downloads the TRMM data daily in binary and converts the files
      to NetCDF
      + [make_ICU_TRMM_map.ipynb](http://nbviewer.ipython.org/github/nicolasfauchereau/ICU/blob/master/maps/TRMM/make_ICU_TRMM_map.ipynb) creates the map of averages or anomalies for the current month (if we are after the 25) or the previous month (before the 25th)

  + Sea Surface Temperature anomalies from the OI-SST dataset


**3. ENSO indices**

  + this [notebook]() downloads the Southern Oscillation Index and NINO indices data from the Australian Bureau of Meteorology

  + [NIWA SOI](): calculates the *NIWA* SOI according to the Troup method using the Tahiti and Darwin MSLP data made available at the [LongPaddock website]()

**4. TRMM Regional Rainfall Estimates**
