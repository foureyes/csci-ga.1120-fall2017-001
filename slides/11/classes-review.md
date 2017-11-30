---
layout: slides
title: "Classes Review"
---
<section markdown="block">
## Classes Review

Creating a class lets you create a new type:

* there are types, like `int`, `range`, etc.
* but sometimes, these types aren't adequate for what you're doing
* you create your own type
    * what data that type holds
    * what actions / behaviors that type has

</section>

<section markdown="block">
## Class Analogy

Definitions:

* __class__ - a blueprint for making objects
    * it'll define the data that those objects will have
    * and the possible methods you can call on that object
* __instance__ - that is the result of creating an object with a class
    * _insantiation_ creating an instance from a class that was defined
    * can have "properties" - the data (sometimes these are called: fields, member variables, or attributes)
    * can have "methods" - actions, behavior

</section>

<section markdown="block">
## Syntax for Creating a Class

<pre><code data-trim contenteditable>
class ClassName:
    # define some stuff here
    # methods / a constructor
    def __init__(self):
        pass

    def method_name(self):
        pass
</code></pre>

1. keyword `class`
2. followed by a class name (_should be camel case_), and a colon
3. indented block of code follows
    * define methods
    * a constructor
</section>


<section markdown="block">
## Creating an Object

Use the name of the class to create a new object.  &rarr; 

<pre><code data-trim contenteditable>
class Widget:
    def __init__(self):
        print("doing what init does") 
w = Widget()
</code></pre>

The method, `__init__`, is the function that's automatically called when an entirely new object is created from your class. In other languages, this is called a __constructor__.

1. To create an object from your class, call your class by name; use it as if it were a function
2. The code in `__init__` is executed when a new _instance_ is created

</section>

<section markdown="block">
## \_\_init\_\_

The code in `__init__` is __usually used to create / initialize properties on the new instance__. &rarr;

1. The first parameter for `__init__` should be `self` which represents the newly created instance
2. The remaining number of parameters declared in `__init__` determine the number of arguments passed in when creating a new object

<pre><code data-trim contenteditable>
class SomeFancyClass:
    # first param is self
    def __init__(self, arg1, arg2):  
        self.foo = 'foo'
# 2 arguments passed
SomeFancyClass('one', 'two') 
</code></pre>


</section>

<section markdown="block">
## Setting Properties on Instances

__Instance variables (properties) can be added to an instance__ &rarr;

First note that the property, `bar` does not exist on the instance, `f`

<pre><code data-trim contenteditable>
>>> class Foo:
...   pass
...
>>> f = Foo()
>>> f.baz
Traceback (most recent call last):
File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'Foo' object has no attribute 'bar'
</code></pre>

</section>

<section markdown="block">
## Setting Properties Continued

__To set a property...__ &rarr;

1. use the instance
2. followed by a dot
3. and the new property name 
4. ... along with assignment

(Assuming that `f = Foo()`)

<pre><code data-trim contenteditable>
>>> # f is an instance of Foo
>>> f.baz = 'baz'
>>> f.baz
'baz'
</code></pre>
</section>

<section markdown="block">
## Setting Properties Continued


__Setting a property on an instance does not affect other instances created from the same class__ &rarr;


If we look for `baz` in a new instance, it will not be present (it only exists in the instance `f` from the previous slide).

<pre><code data-trim contenteditable>
>>> f2 = Foo()
>>> f2.baz
Traceback (most recent call last):
File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'Foo' object has no attribute 'baz'
</code></pre>


</section>

<section markdown="block">
## Back to __init__

If you want to have a property initialized to a value for every instance, __it can be done within the constructor (init) method__ &rarr;

<pre><code data-trim contenteditable>
>>> class Foo:
...   def __init__(self):
  ...     self.baz = "baz"
...
>>> f = Foo()
>>> f.baz
'baz'
</code></pre>

Now that you can still override an instance variable set by `__init__`:

<pre><code data-trim contenteditable>
>>> f.baz = 'what'
>>> f.baz
'what'
</code></pre>

</section>

<section markdown="block">
## __str__

This is a special method. By default, it will give back the type of the object... and _probably_ its memory address.

If you define your own __str__, then that will be called instead.

The __str__ should have one argument, self, and it should give back a string

</section>

<section markdown="block">
## Creating a new Object With Your Class 

Your class name is essentially going to be a function... so class name and function call to create new object from class must match:

<pre><code data-trim contenteditable>
class Thingamajig:
    def __init__(self):
        print('making a thing')

t = Thingamajig()
</code></pre>

<pre><code data-trim contenteditable>
# when function is called, the thing
# that's actually called is 
# __init__
</code></pre>
</section>

<section markdown="block">
## We've Seen This in Turtle

<pre><code data-trim contenteditable>
import turtle
t = turtle.Turtle() # Turtle is a constructor
</code></pre>

</section>

<section markdown="block">
## 

<pre><code data-trim contenteditable>
class Dog:
    # self will be the new instance created
    # from here, we can augment self
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        self.toys = []

    # if you want to reference a property from within your class
    # method, always prefix with self... that will refer to
    # the current instance
    def __str__(self):
        toys_string = ','.join(self.toys)
        return "A dog named " + self.name + " that has " + toys_string

    def make_noise(self):
        return self.sound.upper()

d1 = Dog('Bark Twain', 'woof')
print(d1.name)
d1.toys.extend(['chew toy', 'pig\'s ear'])
print(d1)
print(d1.make_noise())
d2 = Dog('Jane Clawsten', 'arf')
print(d2.name)
print(d2)
print(d2.make_noise())

"""
print will cause the __str__ method of an object to be called??????
"""

</code></pre>
</section>

<section markdown="block">
## An Exercise

</section>
{% comment %}
<section markdown="block">
## File Formats

* csv - comma separated values
* txt - no format (like a novel downloaded from project gutenberg)
    * space delimited
    * tab delimited
    * fixed width (every field is x number of characters)
* json - a text format for a file
    * looks like a python dictionary
    * where you have keys and their values
    * {"key": "value"}
* use built in module called json to turn a string into a python object (a dictionary)

</section>
{% endcomment %}



































































