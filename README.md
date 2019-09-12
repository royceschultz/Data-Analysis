# Frequency Analysis of Earthquakes

## Abstract

This project demonstrates how properties of common statistical distributions can be observed in nature.

For the full report text, download the compiled [pdf](Earthquake.pdf).

## About the data

The dataset can be found [here (geo.mtu.edu)](http://www.geo.mtu.edu/UPSeis/magnitude.html)

The filtered data contains 23,228 earthquakes with magnitude >5.5.

| Magnitude | Effects | Estimated Number Each Year |
|---|---|---|
| <2.5 | Usually not felt, only recorded by seismograph. | 900,000 |
| 2.5-5.4 | Often felt, but only minor damage | 30,000 |
|  5.5-6.0 | Slight damage to buildings | 500 |
|  6.1-6.9 | May cause lots of damage in populated areas | 100 |
|  7.0-7.9 | Serious Damage | 20 |
|  >8.0 | Can totally destroy communities | 1 every 5-10 years |

## Highlighted conclusions

### Statistical Analysis

Earthquakes are random, but the frequency can be modeled using common statistical distributions.

![Data Frequency](/Present/BarChart.png)

This data is fit to an exponential distribution using SciPy

#### Global Fit

![Exponential MDF](/Present/ExpMDF.png)

![Exponential CDF](/Present/ExpCDF.png)

The sum of many repeated exponential distributions is called a Poisson distribution. It is left as an exercise to the reader to prove this relationship.

![Poisson Distribution](/Present/Poisson.png)

### Comparing Local Areas

Earthquakes occur along fault lines where tectonic plates meet.

![Map of Locations](/Present/TectonicPlates.png)

After calculating distance by converting spherical coordinates (Latitude and Longitude) to a 3D space, the dataset can be filtered to local areas.

![City Comparison](/Present/CompareCity.png)

#### The probability of earthquakes in Tokyo

The same distribution fitting can be performed on the filtered, local dataset.

![Tokyo Exponential CDF](/Present/TokyoExpCDF.png)

![Tokyo Poisson Distribution](/Present/TokyoPoisson.png)
