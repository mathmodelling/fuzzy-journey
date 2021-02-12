# Statistical Analysis of Hydrometeorological Variables

***Work in Progress!***

This repository contains support scripts for statistical analysis of hydrometeorological variables. Initially intended for teaching in the courses of Applied stochastic processes, Hydroclimatolgy,  Hydroclimatology and Climate Variability at Javeriana University.

Here you will find scripts for:

  ## Randomness analysis
  * My own script version of the Runs Test
  
  This version is based on the descriptions presented in [@Rozhdenstvenskiy:Revelation:1974] Th data to be read is located in an Excel file using the following template:
  
  Año  Col1 Col2  ... ColN
  XXXX XXXX XXXX  ... XXXX
  XXXX XXXX XXXX  ... XXXX 
  ...  ...  ...   ... ...
  XXXX XXXX XXXX  ... XXXX
  
  Column titles should start at the firts row and first column. It will be usual for Col1, Col2, ..., ColN to be Months but, could be anything else. 
  
  * Using the RandomSuite
 ## Gap filling
 ## Fitting theoretical probability density curves
 ## Calculation of statistical moments
 ## Hydrometeorological Teleconnections
 ## Secular cycles
 ## Spatial interpolation
 ## Water balance

All scripts were developed to work in a chain starting from raw data and finishing with a gauged territory's water balance. All scripts are provided as is; use them under your own responsibility.


@book{Rozhdenstvenskiy1974,
address = {Leningrad},
author = {Rozhdenstvenskiy, Anatoly Vadimovich and Chevotariov, Alexander Ivanovich},
editor = {Kozhina, Z M},
pages = {424},
publisher = {Guidrometeoizdat},
title = {{Statistical methods in hydrology}},
year = {1974}
}
