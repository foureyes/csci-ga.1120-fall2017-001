---
layout: slides
title: "More About Classes"
---

<section markdown="block">
## More Class Stuff

* composition... you can have a class where instances of another class are part of it
* static methods
* "static" / class variables ... properties that you can access without an instance (and that is the same for all instances)
* __method_name__ - magic methods... dunderscore - methods have have special meaning in python
    * `__init__` - constructor (initializing your object)
    * `__str__` - nicely formatted string representation
    * `__repr__` - actual string representation .... doesn't have to be formatted nicely
    * `__add__` - lets you use + operator
    * `__eq__`, `__gt__`
* `__name__` ... built in variable that contains the name of the module
* `'__main__' # a string that names the currently running module`

</section>

<section markdown="block">
## 
* Aaaand... More With Classes
    * instances as arguments
    * composition
    * calling methods from methods
    * static methods
    * class variables
    * \_\_eq\_\_, \_\_gt\_\_, \_\_lt\_\_
    * \_\_add\_\_
    * \_\_repr\_\_
    * demo: fraction class
    * exercise: rectangle class
        * equal if dimensions are same
        * compare with area
    * using with turtle
* Inheritance
    * super 
    * person &rarr; student
    * other shapes 

</section>
