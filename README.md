# Frequency Analysis of Earthquakes

## Abstract

This project aims to model the frequency of earthquakes. The data is sourced from Kaggle. The report is written in a Jupyter Notebook and analyzed using Pandas, Matplotlib, and Scipy.

For the full report text, download the compiled [pdf](../blob/master/Earthquake.pdf).

## Highlighted conclusions

### Statistical Analysis

Earthquakes are random, but the frequency can be modeled using common statistical distributions.

![Data Frequency](/Present/BarChart.png)

This data is fit to an exponential distribution using SciPy

![Exponential MDF](/Present/ExpMDF.png)

![Exponential CDF](/Present/ExpCDF.png)

The sum of many repeated exponential distributions is called a Poisson distribution. It is left as an exercise to the reader to prove this relationship.

![Poisson Distribution](/Present/Poisson.png)

### Comparing Local Areas

Earthquakes occur along fault lines where tectonic plates meet.

![Map of Locations](/Present/TectonicPlates.png)

After calculating distance by converting spherical coordinates (Latitude and Longitude) to cartesian, the frequency of earthquakes in different cities can be compared.

![City Comparison](/Present/CompareCity.png)
