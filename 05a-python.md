# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> The most obvious similarly between tuples and lists is that they are both ordered collections of data. As a result they have very similar operations. Using a[0] will give you the first element of the collection if a is a tuple or a list, and writing a loop such as 

	For x in list1: 
	
		print(x) 
		
>>> will work for both tuples and lists. And as opposed to sets they both allow for duplicates. The biggest difference 	between the two is that tuples are immutable, while lists mutable. Meaning that tuples are best used when looking at data you don't want to change, for example the (x,y) coordinate list of a graph. While you would use lists for data that you are constantly appending, so your path history while walking around the said graph. While this may lead you to believe that we should always use lists, there are some advantages to using tuples. For example since tuples are mutable, they can be used as dictionary keys. If you tried to use an immutable object like a list for a dictionary key, you wouldn't be able to find the dictionary entry after changing the list. But mainly you should use tuples over lists whenever you can simply because they are lighter weight computationally speaking. So your program will run faster if you are using tuples over lists.


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Again the obvious similarity between sets and lists are in their very nature, that of being collections of data. So as above looping through a set or a list has the same syntax. Also both sets and lists are mutable, so they are often used for collections of data that you are constantly appending throughout your program. Of the differences between the two, the most glaring two are that lists are ordered while sets are unordered, and that lists can contain duplicates while sets cannot. Also sets are much more effective when it comes to searching for an element because sets uses a hash table which results in an O(1) average runtime, at the cost of higher memory storage. So if I wanted to store a collection of all items being sold in a grocery store as a reference, I would use a set, since this collection would be unordered, contain no duplicates, and the searching of an item would run faster as opposed to a list. Now if I wanted to store my bank account statements from the past year, I would use a list because of the significance of the ordering (furthest to latest) and for the possibility of duplicates.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is a keyword used to create an anonymous function. So (lambda x: x-1)(2) will return 1. So if you want to use a function once without the bother of formally defining it, lambda can be useful. So if I want to sort a list A = [[1,2], [3,1], [0,3]] based off of the second entry of each element, lambda can be used in the sorted function as follows 

	sorted(A, key = lambda x: x[1])

>> which will run the anonymous lamda function that takes the second entry of each element, then sorts based off of them.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





