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
## Constructor

This is the function that's called when an entirely object is created from your class.

To create an object from your class, call it as if it were a function:

<pre><code data-trim contenteditable>
class Widget:
    pass

w = Widget()
</code></pre>

<pre><code data-trim contenteditable>
__init__ # contains the code that will be run when you create a new obj
</code></pre>


</section>

<section markdown="block">
## __init__

Typically within init... what we'll do is create / set some properties on our new instance.

We do this by using the 1st parameter passed in, which always the instance

<pre><code data-trim contenteditable>
__init__(self, arg1) #<-- first thing is always self

# self is passed in implicitly

ClassName(arg1)
</code></pre>

</section>

<section markdown="block">
## Blank Instances, Setting Properties

<pre><code data-trim contenteditable>
>>> class Foo:
...   pass
...
>>> f = Foo()
>>> f
<__main__.Foo object at 0x10c5e2d68>
>>> f.bar
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'Foo' object has no attribute 'bar'
>>> f
<__main__.Foo object at 0x10c5e2d68>
>>> f
<__main__.Foo object at 0x10c5e2d68>
>>> f.baz = 'baz'
>>> f.baz
'baz'
>>> f2 = Foo()
>>> f2.baz
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'Foo' object has no attribute 'baz'
>>> class Foo:
...   def __init__(self):
  ...     self.bar = "bar"
...
>>> f = Foo()
>>> f.bar
     'bar'
          >>> f.bar = 'what'
          >>> f.bar
          'what'
          >>>
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
t = turtle.Turtle() # Turtle is a contructor
</code></pre>

</section>


<section markdown="block">
## More Class Stuff

* composition... you can have a class where instances of another class are part of it
* static methods
* "static" / class variables ... properties that you can access without an instance (and that is the same for all instances)
* __method_name__ - magic methods... dunderscore - methods have have special meaning in python
    * __init__ - constructor (initializing your object)
    * __str__ - nicely formatted string representation
    * __repr__ - actual string representation .... doesn't have to be formatted nicely
    * __add__ - lets you use + operator
    * __eq__, __gt__
* __name__ ... built in variable that contains the name of the module
* '__main__' # a string that names the currently running module

</section>

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







































































