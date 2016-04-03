[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> Using the data from NSFG with the help of the thinkplot.Scatter it was fairley straightforward to get the following scatter plot of birth weight vs mother's age.
![scatter plot](https://raw.githubusercontent.com/ekruskal/dsp/master/figure_7.png)
What was little more difficult was in plotting percentiles in birth weight vs. mother's age as it required me to first bin the ages. Luckily NumPy provides functions that make this easier:

```
bins = np.arange(10, 46, 3)
indices = np.digitize(age, bins)
groups = data.groupby(indices)
```

Once I successfully binned the ages, I represented each bin by the mean of all ages contained in that bin. Then I made a cdf for each bin using the corresponding weights. Then, using cdf.Percentile, I took from each cdf the weights that corresponded to the 75th, 50th, and 25th percentiles and plotted them versus age. This resulted in the following plot:
![percentile plot](https://github.com/ekruskal/dsp/blob/master/figure_6.png?raw=true)
