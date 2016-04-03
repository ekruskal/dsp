[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The first thing I did was to take the data set and split it up into two groups, Firsts and Others. Firsts is comprised of those babies whose birth order is marked as 1, while Others is comprised of babies whose birth order is greater than 1. Then simply using the totalwgt_lb variable along with the mean() function, I get that the average weight of first babies is 7.201094430437772 lbs while the average weight of other babies is 7.325855614973262 lbs. Therefore, the data shows that first babies are generally lighter than others. Now I wan't to find an effect size between these two groups, and then compare it to the difference in pregnancy lengths. In order to do this I wrote a function to calculate Choen's d between two groups, the code is as written below.

  def cohens_d(group1, group2):
    mean1 = group1.mean()
    mean2 = group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    length1 = len(group1)
    length2 = len(group2)
    s = math.sqrt((length1*var1 + length2*var2)/ (length1 + length2))
    d = (mean1 - mean2) / s
    return d
    
>> Using this function I got that the Cohen's d for the weight statistics to be -0.088672927072602 standard deviations, while that of pregnancy length is 0.028879044654449883 standard deviations. Therefore being a first baby has a higher effect on weight than it does pregnancy length.
