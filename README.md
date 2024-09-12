# VIIRsDownload
Automated VIIRS download from NOAA Chl-A site

This python script runs to download chlorophyll .nc files from https://coralreefwatch.noaa.gov/product/oc/puerto_rico.php

Coralreefwatch from NOAA uses VIIRS satellite to obtain Chl-A at a 750m resolution

Operation of python script is easy

1) Open command prompt

2) change directory to this folder 
	
	cd path_to_folder

3) python NOAAVIIRSdownload.py "link to https directory with year" "path for folder to download to"

         example NOAA link "https://www.star.nesdis.noaa.gov/pub/socd/mecb/crw/data/ocean_color/viirs_coastwatch/msl12_v1.21/750m/puerto_rico/l3_composite/2019/"
	 
	 This sill specifically get all of the .nc files for the year 2019
