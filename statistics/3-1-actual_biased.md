[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Using the NSFG respondant variable NUMKDHH and the Thinkstats2 variable Pmf, it was pretty straighforward to construct the actual distribution for the number of children under 18 in the household to be:
```
Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})
```
>> Now to construct the biased data, we have to do two things. First we have to scale the probabilites in the above pmf by the corresponding number indicating the number of children in the household. This is due to the fact that in a biased questionnaire in which we ask the kids to indicate their household child count, we will get n responses per household, where n is the number of children in that household. Then once we do the appropiate scaling, we must re-normalized due to the increased sample size. This scaling and normalizing can be done using the following code:
```
def Biaspmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf
 ```   
>> The mean for the actual distribution is 1.02420515504. The mean for the biased distribution is 2.40367910066. The following is a plot of the two distributions side by side.
