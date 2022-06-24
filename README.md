# Surfs Up

## Overview

I'll have to convince the board of directors to invest 

### Temperature & Precipitation Plots

Period|Temperature|Precipitation
---|---|---
June|![](./analysis/temp_june_plt.png)|![](./analysis/prcp_june_plt.png)
December|![](./analysis/temp_dec_plt.png)|![](./analysis/prcp_dec_plt.png)
Whole Period|![](./analysis/temp_whp_plt.png)|![](./analysis/prcp_whp_plt.png)

### Temperature & Precipitation Statistics

temp/prcp|June|December|Whole Period
---|---|---|---
Temperature|![](./analysis/temp_june_st.png)|![](./analysis/temp_dec_st.png)|![](./analysis/temp_whp_st.png)
Precipitation|![](./analysis/prcp_june_st.png)|![](./analysis/prcp_dec_st.png)|![](./analysis/prcp_whp_st.png)

### Box Plots

![](./analysis/temp_box_plot.png)

![](./analysis/prcp_box_plot.png)

## already

### log scales

### box plots

## to do

### why are there gaps in the histogram with the whole dataset?
Seems like stations round up temps and prcps or "prefer"/"avoid" some values
it's obvious form hist (gaps)
use value_counts to test

### distributions (seem to be)
prcp - gamma (https://journals.ametsoc.org/view/journals/atsc/76/11/jas-d-18-0343.1.xml)
temp - normal
Why these distributions?

### different day scales:
do the same scale limits and take 200 days. How many days out of 200 for every scale for every month. Eliminate whole period.

### other months

### station coordinates - other stations
