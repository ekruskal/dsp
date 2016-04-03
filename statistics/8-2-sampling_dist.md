[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> Using np.random.exponential(mean, n) I drew a sample with size n=10 1000 times. Using these samples I obtained an estimate for lambda, denoted L. The sampling distribution of L is plotted below:
![sampling distribution](https://raw.githubusercontent.com/ekruskal/dsp/master/figure_4.png)
Using the RMSE function I found the standard error to be 0.8197838491635697, and putting 5 and 95 respectively into the Percentile variable gave me a 90% confidence interval of (1.2610265871121658, 3.7085738138620474). Repeating the process for different values of n, as you can see the higher n gets the smaller the standard error becomes.

![standerr vs n](https://raw.githubusercontent.com/ekruskal/dsp/master/figure_5.png)
