# Island Climate Update

This repository gathers scripts and notebooks used to generate various products
related to the [Island Climate Update (ICU)](http://www.niwa.co.nz/climare/icu).

The Island Climate Update is a monthly Regional Climate Outlook Forum and outlook
bulletin for the southwest Pacific.

go to:

[https://speakerdeck.com/nicolasf/icu-175](https://speakerdeck.com/nicolasf/icu-175)

To view examples of these products incorportated in the presentation material uploaded
on [speakerdeck](https://speakerdeck.com/) before the ICU teleconference.

<hr size=5>

The scripts and [notebooks]() are written in the language [Python](). They make
heavy use of the **Python scientific stack**: i.e. in particular the following libraries:

+ Numpy
+ Scipy
+ Pandas
+ Matplotlib
+ Basemap

To get all these working on your platform (windows, linux, mac), I strongly recommend installing the [Anaconda Python distribution](https://store.continuum.io/cshop/anaconda/), developed and made available for free by [Continuum Analytics](http://continuum.io/).  

The repo is organised in different sections:

**1. [mailing]()**

  generates the monthly mail sent to the ICU mailing list, with time of the teleconference
  translated in the different time-zones in the region.

  usage example:

  ```
  $ ./make_mail_ICU.py 175 2015 04 02 12 30
  ```

**2. [maps]()**

  + TRMM Rainfall [(Tropical Rainfall Measurement Mission)](https://climatedataguide.ucar.edu/climate-data/trmm-tropical-rainfall-measuring-mission)

    there are two versions:

    + one makes use of the images directly available from the [Nasa TRMM website](http://trmm.gsfc.nasa.gov), updated daily for the last 30 days averages and anomalies: the script downloads the image, crops it and
    overlay the image on a high resolution basemap of the southwest Pacific.

      + see [plot_sp_30days_im_averages.ipynb](http://nbviewer.ipython.org/github/nicolasfauchereau/ICU/blob/master/maps/TRMM/plot_sp_30days_im_averages.ipynb) for the last 30 days averages map
      + see [plot_sp_30days_im_anoms.ipynb](http://nbviewer.ipython.org/github/nicolasfauchereau/ICU/blob/master/maps/TRMM/plot_sp_30days_im_anoms.ipynb) for the last 30 days anomalies map


    + The other is based on the actual data available from [](), the whole process is
    constructed around a few scripts and notebooks:

      + [get_daily_TRMM.py]() downloads the TRMM data daily in binary and converts the files
      to NetCDF
      + []()

  + Sea Surface Temperature anomalies from the OI-SST dataset


**3. ENSO indices**

  + this [notebook]() downloads the Southern Oscillation Index and NINO indices data from the Australian Bureau of Meteorology

  + [NIWA SOI](): calculates the *NIWA* SOI according to the Troup method using the Tahiti and Darwin MSLP data made available at the [LongPaddock website]()

**4. TRMM Regional Rainfall Estimates**
