[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> Here are the pmf and cdf plots for 1000 numbers generated randomly from random.random:

![pmf](https://raw.githubusercontent.com/ekruskal/dsp/master/figure_2.png)
![cdf](https://raw.githubusercontent.com/ekruskal/dsp/master/figure_3.png)

As you can see, the pmf does a pretty poor job of describing the data since every number that doesn't get outputed from random will have a zero probability and every number that does will have a nonzero probability. So you get the jagged pattern seen in the first image. But if you look at the cdf plot as shown in the second image, you can see that the distribution is uniform, since it is approximately linear.
