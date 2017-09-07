---
layout: slides
title: Functions 
---

<section markdown="block" class="title-slide">
#  A Quick Peek at Making Our Own Functions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Functions

__What's a function (again)?__ &rarr;

<div class="incremental" markdown="block">
A __function__ is a named sequence of statements that performs a specific task or useful operation
</div>
</section>

<section markdown="block">
###  Built-In Functions

__What are some built-in function that we just learned about?__ &rarr;

<div class="incremental" markdown="block">
* print
* type
* int
* str
* float
* input
</div>
</section>

<section markdown="block">
###  Our Very Own Functions!

* we can actually create our own functions
* that means:
	* we can group a bunch of statements together
	* name that group of statements
	* __execute that group of statements simply by calling its name!__
</section>

<section markdown="block">
###  Motivation for Creating Functions

__Why would the ability to create our own functions be useful?__ &rarr;

<div class="incremental" markdown="block">
* reduce repetitive code (instead of typing in the group of statements multiple times, just call function)
* break down programming problem into discrete tasks
	* complexity of each sub-task or function is more manageable than dealing with program in its entirity
	* easier to test each individual function or component 
* create your own tools for solving a problem
	* it's almost like defining your own __problem domain__ specific language
</div>
</section>


<section markdown="block">
###  Defining a Function

{% highlight python %}
def the_name_of_your_function(parameter_1, paramter_2):
	""" some code """
	print("I'm doing something useful!")
{% endhighlight %}
</section>

<section markdown="block">
###  Defining a Function Continued

1. a function definition always starts with the __reserved__ word, __def__ (__the function header__)
2. ... followed by the name of your function
	* (function names adhere to the same rules as variable names)
3. ... followed by parentheses
4. with an __optional__, comma separated list of inputs enclosed in parentheses (depends on function)
	* if the __parentheses are empty, then the function is being called without arguments__
		* no_inputs_needed()
5. lastly, an indented block of code (__the function body__)
	* this is just one level of indentation in &rarr;
</section>

<section markdown="block">
###  What's This About an Indented Block?

* remember - in Python, __whitespace characters__ (such as space, tabs, newlines, etc.) are __significant__
* __consecutive lines of code__ can be grouped together based on __indentation__
* you can tell the start and end of a function body by its level of indentation
* it is indented one level in from the function header

{% highlight python %}
def the_name_of_your_function(parameter_1, paramter_2):
	""" inside the function """
	print("something")
	print("another thing")

""" outside of the function """
print("and another thing")
{% endhighlight %}

</section>

<section markdown="block">
###  Let's Try Creating a Function!

__Write a function called say_multilingual_meow:__ &rarr;

* it'll [say meow in two different languages](http://www.eleceng.adelaide.edu.au/personal/dabbott/animal.html)
* it should print out two lines
* one line with "meow", the other line with "nyan"

<div class="incremental" markdown="block">
{% highlight python %}
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Calling Your Function

So... now that you have a shiny new function, __how would you call it?  How many arguments would it take?  0, 1, or 2?__ &rarr;

{% highlight python %}
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
"""
Once the function is defined in your file, you can call it!
"""

say_multilingual_meow()
{% endhighlight %}

It takes 0 arguments.
</div>
</section>


<section markdown="block">
###  Let's See How This All Works!

In one file, write the function definition and function call from the previous slides.  

* try running it!  
* print out "done" after your function call
* __what do you think the output will be?__ &rarr;

{% highlight python %}
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)

say_multilingual_meow()
print("done!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
nyan
meow
done!
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Calling Your Function Continued

So... [what actually happened there](http://www.pythontutor.com/visualize.html#code=def+say_multilingual_meow()%3A%0A%09japanese_meow+%3D+%22nyan%22%0A%09english_meow+%3D+%22meow%22%0A%09print(japanese_meow)%0A%09print(english_meow)%0A%0Asay_multilingual_meow()%0Aprint(%22done!%22)&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0)? &rarr;

{% highlight python %}
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)

say_multilingual_meow()
print("done!")
{% endhighlight %}

* when you call your function...
* imagine that you're jumping back to your function definition
* ...and then executing the body of your function
* once it's done, execution goes back to where you called your function (printed done for clarity)
</section>

<section markdown="block">
###  Just the Definitions, Please!

Let's look at the same program, but without the function __call__.  __What do you think the output of this program will be?__ &rarr;
{% highlight python %}
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
 
{% endhighlight %}

(That's supposed to be nothing!  A function definition alone won't execute the code in a function.)
</div>
</section>

<section markdown="block">
###  Just the Calls, Please!

What about this version of the program? __What do you think the output will be?__ &rarr;

{% highlight python %}
say_multilingual_meow()
{% endhighlight %}

<div class="incremental" markdown="block">
We get a NameError!

{% highlight python %}
Traceback (most recent call last):
  File "/tmp/foo.py", line 1, in <module>
    say_multilingual_meow()
NameError: name 'say_multilingual_meow' is not defined
{% endhighlight %}

This may be obvious, but __a function has to be defined before it can be used__.
</div>
</section>

<section markdown="block">
###  Multiple Function Definitions

You can define more than one function in your program!

{% highlight python %}
def my_first_function():
	print("first")

def my_second_function():
	print("second")
{% endhighlight %}
</section>

<section markdown="block">
###  Functions in Functions

In fact, you can use a function that you've already defined in another function that you're creating.  __What do you think the output of this program will be?__ &rarr;

{% highlight python %}
def say_moo():
	print("moo")

def main():
	say_moo()
	say_moo()

main()
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
moo
moo
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Functions in Functions Continued

Notice that in the previous code...

{% highlight python %}
def say_moo():
	print("moo")

def main():
	say_moo()
	say_moo()

main()
{% endhighlight %}

* we defined a function called __say_moo__
* we defined another function called main that uses __say_moo__
</section>

<section markdown="block">
###  "Local" Variables

* variables defined in your function are available only to that function
* the variables in your function are __local__ to that function
* they cannot be used in another function or outside of the current function definition

</section>

<section markdown="block">
###  "Local" Variables Continued


{% highlight python %}
def my_first_function():
	a = 1
	print(a)

def my_second_function():
	b = 2
	print(b)
{% endhighlight %}

The variables __a__ and __b__ are local to __my\_first\_function__ and __my\_second\_function__ respectively.

</section>

<section markdown="block">
###  "Local" Variables Continued Some More

Because variables defined within a function are __local__

* using the same variable name in two different functions doesn't cause any errors
* nothing gets overwritten

{% highlight python %}
def my_first_function():
	a = 1
	print(a)

def my_second_function():
	a = 200
	print(a)
{% endhighlight %}

(calling both functions consecutively prints out 1, then 200)
</section>

<section markdown="block">
###  Defining a Main Function

* it is common practice to have the entirity of your program in a single function called main
* main is usually defined at the end of the file
* with other additional functions defined outside as well
* the examples in {{ site.bookq }} use this pattern often
* here's a template:

{% highlight python %}
def main():
	print("in main function")

main()
{% endhighlight %}
</section>

<section markdown="block">
###  Main Function Continued

For example, these two programs are equivalent:

{% highlight python %}
print("About to do stuff")
print("Doing stuff")
print("Done")
{% endhighlight %}

{% highlight python %}
def main():
	print("About to do stuff")
	print("Doing stuff")
	print("Done")

main()
{% endhighlight %}
</section>

<!--
<section markdown="block">
###  

* Global Scope
* Main convention
* Passing in Parameters?

<div class="incremental" markdown="block">
{% highlight python %}
{% endhighlight %}
</div>
</section>
-->

<section markdown="block">
##  [(Totally Optional) A Whirlwind Tour of Conditionals](conditionals.html)
</section>

