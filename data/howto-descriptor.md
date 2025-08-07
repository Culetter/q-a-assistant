> **Descriptor** **Guide** ***Release*** ***3.13.3***
>
> **Guido** **van** **Rossum** **and** **the** **Python**
> **development** **team**
>
> **April** **27,** **2025**
>
> **Python** **Software** **Foundation** **Email:** **docs@python.org**

**Contents**

**1** **Primer** **3** 1.1 Simple example: A descriptor that returns a
constant . . . . . . . . . . . . . . . . . . . . . . . . . 3 1.2 Dynamic
lookups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . 3 1.3 Managed attributes . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 1.4
Customized names . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . 5 1.5 Closing thoughts . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

**2** **Complete** **Practical** **Example** **6** 2.1 Validator class .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . 7 2.2 Custom validators . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . 7 2.3 Practical
application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . 8

**3** **Technical** **Tutorial** **9** 3.1 Abstract . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . 9 3.2 Definition and introduction . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . 9 3.3 Descriptor protocol . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . 9 3.4 Overview of descriptor invocation . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . 10 3.5 Invocation from an
instance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . 10 3.6 Invocation from a class . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . 11 3.7 Invocation from
super . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . 11 3.8 Summary of invocation logic . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . 11 3.9 Automatic
name notification . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . 11 3.10 ORM example . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

**4** **Pure** **Python** **Equivalents** **13** 4.1 Properties . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . 13 4.2 Functions and methods . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . 14 4.3 Kinds of
methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . 16 4.4 Static methods . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 4.5
Class methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . 17 4.6 Member objects and \_\_slots\_\_
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18

> **Author**
>
> Raymond Hettinger
>
> **Contact**
>
> \<python at rcn dot com\>
>
> **1**
>
> **Contents**
>
> • *Descriptor* *Guide* **–** *Primer*
>
> ∗ *Simple* *example:* *A* *descriptor* *that* *returns* *a* *constant*
> ∗ *Dynamic* *lookups*
>
> ∗ *Managed* *attributes* ∗ *Customized* *names* ∗ *Closing* *thoughts*
>
> **–** *Complete* *Practical* *Example* ∗ *Validator* *class*
>
> ∗ *Custom* *validators*
>
> ∗ *Practical* *application* **–** *Technical* *Tutorial*
>
> ∗ *Abstract*
>
> ∗ *Definition* *and* *introduction* ∗ *Descriptor* *protocol*
>
> ∗ *Overview* *of* *descriptor* *invocation* ∗ *Invocation* *from* *an*
> *instance*
>
> ∗ *Invocation* *from* *a* *class* ∗ *Invocation* *from* *super*
>
> ∗ *Summary* *of* *invocation* *logic* ∗ *Automatic* *name*
> *notification* ∗ *ORM* *example*
>
> **–** *Pure* *Python* *Equivalents* ∗ *Properties*
>
> ∗ *Functions* *and* *methods* ∗ *Kinds* *of* *methods*
>
> ∗ *Static* *methods* ∗ *Class* *methods*
>
> ∗ *Member* *objects* *and* *\_\_slots\_\_*

Descriptors let objects customize attribute lookup, storage, and
deletion. This guide has four major sections:

> 1\) The “primer” gives a basic overview, moving gently from simple
> examples, adding one feature at a time. Start here if you’re new to
> descriptors.
>
> 2\) The second section shows a complete, practical descriptor example.
> If you already know the basics, start there.
>
> 3\) The third section provides a more technical tutorial that goes
> into the detailed mechanics of how descriptors work. Most people don’t
> need this level of detail.
>
> **2**
>
> 4\) The last section has pure Python equivalents for built-in
> descriptors that are written in C. Read this if you’re curious about
> how functions turn into bound methods or about the implementation of
> common tools like classmethod(), staticmethod(), property(), and
> \_\_slots\_\_.

**1** **Primer**

In this primer, we start with the most basic possible example and then
we’ll add new capabilities one by one.

**1.1** **Simple** **example:** **A** **descriptor** **that**
**returns** **a** **constant**

The Ten class is a descriptor whose \_\_get\_\_() method always returns
the constant 10:

**class** **Ten**:

> **def** \_\_get\_\_(self, obj, objtype=**None**): **return** 10

To use the descriptor, it must be stored as a class variable in another
class:

**class** **A**: x = 5

> y = Ten()

*\#* *Regular* *class* *attribute* *\#* *Descriptor* *instance*

An interactive session shows the difference between normal attribute
lookup and descriptor lookup:

**\>\>\>** a = A() **\>\>\>** a.x

5

**\>\>\>** a.y 10

*\#* *Make* *an* *instance* *of* *class* *A* *\#* *Normal* *attribute*
*lookup*

*\#* *Descriptor* *lookup*

In the a.x attribute lookup, the dot operator finds 'x': 5 in the class
dictionary. In the a.y lookup, the dot operator finds a descriptor
instance, recognized by its \_\_get\_\_ method. Calling that method
returns 10.

Note that the value 10 is not stored in either the class dictionary or
the instance dictionary. Instead, the value 10 is computed on demand.

This example shows how a simple descriptor works, but it isn’t very
useful. For retrieving constants, normal attribute lookup would be
better.

In the next section, we’ll create something more useful, a dynamic
lookup.

**1.2** **Dynamic** **lookups**

Interesting descriptors typically run computations instead of returning
constants:

**import** **os**

**class** **DirectorySize**:

> **def** \_\_get\_\_(self, obj, objtype=**None**): **return**
> len(os.listdir(obj.dirname))

**class** **Directory**:

> size = DirectorySize()
>
> **def** \_\_init\_\_(self, dirname): self.dirname = dirname

*\#* *Descriptor* *instance*

*\#* *Regular* *instance* *attribute*

An interactive session shows that the lookup is dynamic — it computes
different, updated answers each time:

> **3**

**\>\>\>** s = Directory('songs') **\>\>\>** g = Directory('games')
**\>\>\>** s.size

20

**\>\>\>** g.size 3

**\>\>\>** os.remove('games/chess') **\>\>\>** g.size

2

*\#* *The* *songs* *directory* *has* *twenty* *files*

*\#* *The* *games* *directory* *has* *three* *files*

*\#* *Delete* *a* *game*

*\#* *File* *count* *is* *automatically* *updated*

Besides showing how descriptors can run computations, this example also
reveals the purpose of the parameters to \_\_get\_\_(). The *self*
parameter is *size*, an instance of *DirectorySize*. The *obj* parameter
is either *g* or *s*, an instance of *Directory*. It is the *obj*
parameter that lets the \_\_get\_\_() method learn the target directory.
The *objtype* parameter is the class *Directory*.

**1.3** **Managed** **attributes**

A popular use for descriptors is managing access to instance data. The
descriptor is assigned to a public attribute in the class dictionary
while the actual data is stored as a private attribute in the instance
dictionary. The descriptor’s \_\_get\_\_() and \_\_set\_\_() methods are
triggered when the public attribute is accessed.

In the following example, *age* is the public attribute and *\_age* is
the private attribute. When the public attribute is accessed, the
descriptor logs the lookup or update:

**import** **logging**

logging.basicConfig(level=logging.INFO)

**class** **LoggedAgeAccess**:

> **def** \_\_get\_\_(self, obj, objtype=**None**): value = obj.\_age
>
> logging.info('Accessing *%r* giving *%r*', 'age', value) **return**
> value
>
> **def** \_\_set\_\_(self, obj, value): logging.info('Updating *%r* to
> *%r*', 'age', value) obj.\_age = value

**class** **Person**:

> age = LoggedAgeAccess()
>
> **def** \_\_init\_\_(self, name, age): self.name = name
>
> self.age = age
>
> **def** birthday(self): self.age += 1

*\#* *Descriptor* *instance*

*\#* *Regular* *instance* *attribute* *\#* *Calls* *\_\_set\_\_()*

*\#* *Calls* *both* *\_\_get\_\_()* *and* *\_\_set\_\_()*

An interactive session shows that all access to the managed attribute
*age* is logged, but that the regular attribute *name* is not logged:

**\>\>\>** mary = Person('Mary M', 30) *\#* *The* *initial* *age*
*update* *is* *logged* INFO:root:Updating 'age' to 30

**\>\>\>** dave = Person('David D', 40) INFO:root:Updating 'age' to 40

> (continues on next page)
>
> **4**

**\>\>\>** vars(mary)

{'name': 'Mary M', '\_age': 30} **\>\>\>** vars(dave)

{'name': 'David D', '\_age': 40}

**\>\>\>** mary.age

INFO:root:Accessing 'age' giving 30 30

**\>\>\>** mary.birthday() INFO:root:Accessing 'age' giving 30
INFO:root:Updating 'age' to 31

**\>\>\>** dave.name 'David D'

**\>\>\>** dave.age

INFO:root:Accessing 'age' giving 40 40

(continued from previous page) *\#* *The* *actual* *data* *is* *in* *a*
*private* *attribute*

*\#* *Access* *the* *data* *and* *log* *the* *lookup*

*\#* *Updates* *are* *logged* *as* *well*

*\#* *Regular* *attribute* *lookup* *isn't* *logged*

*\#* *Only* *the* *managed* *attribute* *is* *logged*

One major issue with this example is that the private name *\_age* is
hardwired in the *LoggedAgeAccess* class. That means that each instance
can only have one logged attribute and that its name is unchangeable. In
the next example, we’ll fix that problem.

**1.4** **Customized** **names**

When a class uses descriptors, it can inform each descriptor about which
variable name was used.

In this example, the Person class has two descriptor instances, *name*
and *age*. When the Person class is defined, it makes a callback to
\_\_set_name\_\_() in *LoggedAccess* so that the field names can be
recorded, giving each descriptor its own *public_name* and
*private_name*:

**import** **logging**

logging.basicConfig(level=logging.INFO)

**class** **LoggedAccess**:

> **def** \_\_set_name\_\_(self, owner, name): self.public_name = name
> self.private_name = '\_' + name
>
> **def** \_\_get\_\_(self, obj, objtype=**None**):
>
> value = getattr(obj, self.private_name)
>
> logging.info('Accessing *%r* giving *%r*', self.public_name, value)
> **return** value
>
> **def** \_\_set\_\_(self, obj, value):
>
> logging.info('Updating *%r* to *%r*', self.public_name, value)
> setattr(obj, self.private_name, value)

**class** **Person**:

> name = LoggedAccess() age = LoggedAccess()
>
> **def** \_\_init\_\_(self, name, age): self.name = name
>
> self.age = age

*\#* *First* *descriptor* *instance* *\#* *Second* *descriptor*
*instance*

*\#* *Calls* *the* *first* *descriptor* *\#* *Calls* *the* *second*
*descriptor*

> (continues on next page)
>
> **5**
>
> (continued from previous page)
>
> **def** birthday(self): self.age += 1

An interactive session shows that the Person class has called
\_\_set_name\_\_() so that the field names would be recorded. Here we
call vars() to look up the descriptor without triggering it:

**\>\>\>** vars(vars(Person)\['name'\])

{'public_name': 'name', 'private_name': '\_name'} **\>\>\>**
vars(vars(Person)\['age'\])

{'public_name': 'age', 'private_name': '\_age'}

The new class now logs access to both *name* and *age*:

**\>\>\>** pete = Person('Peter P', 10) INFO:root:Updating 'name' to
'Peter P' INFO:root:Updating 'age' to 10

**\>\>\>** kate = Person('Catherine C', 20) INFO:root:Updating 'name' to
'Catherine C' INFO:root:Updating 'age' to 20

The two *Person* instances contain only the private names:

**\>\>\>** vars(pete)

{'\_name': 'Peter P', '\_age': 10} **\>\>\>** vars(kate)

{'\_name': 'Catherine C', '\_age': 20}

**1.5** **Closing** **thoughts**

A descriptor is what we call any object that defines \_\_get\_\_(),
\_\_set\_\_(), or \_\_delete\_\_().

Optionally, descriptors can have a \_\_set_name\_\_() method. This is
only used in cases where a descriptor needs to know either the class
where it was created or the name of class variable it was assigned to.
(This method, if present, is called even if the class is not a
descriptor.)

Descriptors get invoked by the dot operator during attribute lookup. If
a descriptor is accessed indirectly with
vars(some_class)\[descriptor_name\], the descriptor instance is returned
without invoking it.

Descriptors only work when used as class variables. When put in
instances, they have no effect.

The main motivation for descriptors is to provide a hook allowing
objects stored in class variables to control what happens during
attribute lookup.

Traditionally, the calling class controls what happens during lookup.
Descriptors invert that relationship and allow the data being looked-up
to have a say in the matter.

Descriptors are used throughout the language. It is how functions turn
into bound methods. Common tools like classmethod(), staticmethod(),
property(), andfunctools.cached_property() areallimplemented as
descriptors.

**2** **Complete** **Practical** **Example**

In this example, we create a practical and powerful tool for locating
notoriously hard to find data corruption bugs.

> **6**

**2.1** **Validator** **class**

A validator is a descriptor for managed attribute access. Prior to
storing any data, it verifies that the new value meets various type and
range restrictions. If those restrictions aren’t met, it raises an
exception to prevent data corruption at its source.

This Validator class is both an abstract base class and a managed
attribute descriptor:

**from** **abc** **import** ABC, abstractmethod

**class** **Validator**(ABC):

> **def** \_\_set_name\_\_(self, owner, name): self.private_name =
> '\_' + name
>
> **def** \_\_get\_\_(self, obj, objtype=**None**): **return**
> getattr(obj, self.private_name)
>
> **def** \_\_set\_\_(self, obj, value): self.validate(value)
>
> setattr(obj, self.private_name, value)
>
> **@abstractmethod**
>
> **def** validate(self, value): **pass**

Custom validators need to inherit from Validator and must supply a
validate() method to test various restric-tions as needed.

**2.2** **Custom** **validators**

Here are three practical data validation utilities:

> 1\) OneOf verifies that a value is one of a restricted set of options.
>
> 2\) Number verifies that a value is either an int or float.
> Optionally, it verifies that a value is between a given minimum or
> maximum.
>
> 3\) String verifies that a value is a str. Optionally, it validates a
> given minimum or maximum length. It can validate a user-defined
> [predicate](https://en.wikipedia.org/wiki/Predicate_(mathematical_logic))
> as well.

**class** **OneOf**(Validator):

> **def** \_\_init\_\_(self, \*options): self.options = set(options)
>
> **def** validate(self, value):
>
> **if** value **not** **in** self.options: **raise** ValueError(
>
> f'Expected *{*value*!r}* to be one of *{*self.options*!r}*' )

**class** **Number**(Validator):

> **def** \_\_init\_\_(self, minvalue=**None**, maxvalue=**None**):
> self.minvalue = minvalue
>
> self.maxvalue = maxvalue
>
> **def** validate(self, value):
>
> **if** **not** isinstance(value, (int, float)):
>
> (continues on next page)
>
> **7**
>
> (continued from previous page)
>
> **raise** TypeError(f'Expected *{*value*!r}* to be an int or float')
> **if** self.minvalue **is** **not** **None** **and** value \<
> self.minvalue:
>
> **raise** ValueError(
>
> f'Expected *{*value*!r}* to be at least *{*self.minvalue*!r}*' )
>
> **if** self.maxvalue **is** **not** **None** **and** value \>
> self.maxvalue: **raise** ValueError(
>
> f'Expected *{*value*!r}* to be no more than *{*self.maxvalue*!r}*' )

**class** **String**(Validator):

> **def** \_\_init\_\_(self, minsize=**None**, maxsize=**None**,
> predicate=**None**): self.minsize = minsize
>
> self.maxsize = maxsize self.predicate = predicate
>
> **def** validate(self, value):
>
> **if** **not** isinstance(value, str):
>
> **raise** TypeError(f'Expected *{*value*!r}* to be an str')
>
> **if** self.minsize **is** **not** **None** **and** len(value) \<
> self.minsize: **raise** ValueError(
>
> f'Expected *{*value*!r}* to be no smaller than *{*self.minsize*!r}*' )
>
> **if** self.maxsize **is** **not** **None** **and** len(value) \>
> self.maxsize: **raise** ValueError(
>
> f'Expected *{*value*!r}* to be no bigger than *{*self.maxsize*!r}*' )
>
> **if** self.predicate **is** **not** **None** **and** **not**
> self.predicate(value): **raise** ValueError(
>
> f'Expected *{*self.predicate*}* to be true for *{*value*!r}*' )

**2.3** **Practical** **application**

Here’s how the data validators can be used in a real class:

**class** **Component**:

> name = String(minsize=3, maxsize=10, predicate=str.isupper) kind =
> OneOf('wood', 'metal', 'plastic')
>
> quantity = Number(minvalue=0)
>
> **def** \_\_init\_\_(self, name, kind, quantity): self.name = name
>
> self.kind = kind self.quantity = quantity

The descriptors prevent invalid instances from being created:

**\>\>\>** Component('Widget', 'metal', 5) *\#* *Blocked:* *'Widget'*
*is* *not* *all* *uppercase* Traceback (most recent call last):

> ...

ValueError: Expected \<method 'isupper' of 'str' objects\> to be true
for 'Widget'

**\>\>\>** Component('WIDGET', 'metle', 5) *\#* *Blocked:* *'metle'*
*is* *misspelled*

> (continues on next page)
>
> **8**
>
> (continued from previous page)

Traceback (most recent call last): ...

ValueError: Expected 'metle' to be one of {'metal', 'plastic', 'wood'}

**\>\>\>** Component('WIDGET', 'metal', -5) *\#* *Blocked:* *-5* *is*
*negative* Traceback (most recent call last):

> ...

ValueError: Expected -5 to be at least 0

**\>\>\>** Component('WIDGET', 'metal', 'V') *\#* *Blocked:* *'V'*
*isn't* *a* *number* Traceback (most recent call last):

> ...

TypeError: Expected 'V' to be an int or float

**\>\>\>** c = Component('WIDGET', 'metal', 5) *\#* *Allowed:* *The*
*inputs* *are* *valid*

**3** **Technical** **Tutorial**

What follows is a more technical tutorial for the mechanics and details
of how descriptors work.

**3.1** **Abstract**

Defines descriptors, summarizes the protocol, and shows how descriptors
are called. Provides an example showing how object relational mappings
work.

Learning about descriptors not only provides access to a larger toolset,
it creates a deeper understanding of how Python works.

**3.2** **Definition** **and** **introduction**

In general, a descriptor is an attribute value that has one of the
methods in the descriptor protocol. Those methods are \_\_get\_\_(),
\_\_set\_\_(), and \_\_delete\_\_(). If any of those methods are defined
for an attribute, it is said to be a descriptor.

The default behavior for attribute access is to get, set, or delete the
attribute from an object’s dictionary. For instance, a.x has a lookup
chain starting with a.\_\_dict\_\_\['x'\], then
type(a).\_\_dict\_\_\['x'\], and continuing through the method
resolution order of type(a). If the looked-up value is an object
defining one of the descriptor methods, then Python may override the
default behavior and invoke the descriptor method instead. Where this
occurs in the precedence chain depends on which descriptor methods were
defined.

Descriptors are a powerful, general purpose protocol. They are the
mechanism behind properties, methods, static methods, class methods, and
super(). They are used throughout Python itself. Descriptors simplify
the underlying C code and offer a flexible set of new tools for everyday
Python programs.

**3.3** **Descriptor** **protocol** descr.\_\_get\_\_(self, obj,
type=None)

descr.\_\_set\_\_(self, obj, value)

descr.\_\_delete\_\_(self, obj)

That is all there is to it. Define any of these methods and an object is
considered a descriptor and can override default behavior upon being
looked up as an attribute.

If an object defines \_\_set\_\_() or \_\_delete\_\_(), it is considered
a data descriptor. Descriptors that only define \_\_get\_\_() are called
non-data descriptors (they are often used for methods but other uses are
possible).

Data and non-data descriptors differ in how overrides are calculated
with respect to entries in an instance’s dictionary. If an instance’s
dictionary has an entry with the same name as a data descriptor, the
data descriptor takes precedence.

> **9**

If an instance’s dictionary has an entry with the same name as a
non-data descriptor, the dictionary entry takes precedence.

To make a read-only data descriptor, define both \_\_get\_\_() and
\_\_set\_\_() with the \_\_set\_\_() raising an AttributeError when
called. Defining the \_\_set\_\_() method with an exception raising
placeholder is enough to make it a data descriptor.

**3.4** **Overview** **of** **descriptor** **invocation**

A descriptor can be called directly with desc.\_\_get\_\_(obj) or
desc.\_\_get\_\_(None, cls). But it is more common for a descriptor to
be invoked automatically from attribute access.

The expression obj.x looks up the attribute x in the chain of namespaces
for obj. If the search finds a descriptor outside of the instance
\_\_dict\_\_, its \_\_get\_\_() method is invoked according to the
precedence rules listed below.

The details of invocation depend on whether obj is an object, class, or
instance of super.

**3.5** **Invocation** **from** **an** **instance**

Instance lookup scans through a chain of namespaces giving data
descriptors the highest priority, followed by instance variables, then
non-data descriptors, then class variables, and lastly \_\_getattr\_\_()
if it is provided.

If a descriptor is found for a.x, then it is invoked with:
desc.\_\_get\_\_(a, type(a)).

The logic for a dotted lookup is in object.\_\_getattribute\_\_(). Here
is a pure Python equivalent:

**def** find_name_in_mro(cls, name, default):

> "Emulate \_PyType_Lookup() in Objects/typeobject.c" **for** base
> **in** cls.\_\_mro\_\_:
>
> **if** name **in** vars(base): **return** vars(base)\[name\]
>
> **return** default

**def** object_getattribute(obj, name):

> "Emulate PyObject_GenericGetAttr() in Objects/object.c" null =
> object()
>
> objtype = type(obj)
>
> cls_var = find_name_in_mro(objtype, name, null) descr_get =
> getattr(type(cls_var), '\_\_get\_\_', null) **if** descr_get **is**
> **not** null:
>
> **if** (hasattr(type(cls_var), '\_\_set\_\_')
>
> **or** hasattr(type(cls_var), '\_\_delete\_\_')):
>
> **return** descr_get(cls_var, obj, objtype) *\#* *data* *descriptor*
> **if** hasattr(obj, '\_\_dict\_\_') **and** name **in** vars(obj):
>
> **return** vars(obj)\[name\] *\#* *instance* *variable* **if**
> descr_get **is** **not** null:
>
> **return** descr_get(cls_var, obj, objtype) *\#* *non-data*
> *descriptor* **if** cls_var **is** **not** null:
>
> **return** cls_var *\#* *class* *variable* **raise**
> AttributeError(name)

Note, there is no \_\_getattr\_\_() hook in the \_\_getattribute\_\_()
code. That is why calling \_\_getattribute\_\_() directly or with
super().\_\_getattribute\_\_ will bypass \_\_getattr\_\_() entirely.

Instead, it is the dot operator and the getattr() function that are
responsible for invoking \_\_getattr\_\_() when-ever
\_\_getattribute\_\_() raises an AttributeError. Their logic is
encapsulated in a helper function:

**def** getattr_hook(obj, name):

> "Emulate slot_tp_getattr_hook() in Objects/typeobject.c" **try**:
>
> (continues on next page)
>
> **10**
>
> **return** obj.\_\_getattribute\_\_(name) **except** AttributeError:
>
> **if** **not** hasattr(type(obj), '\_\_getattr\_\_'): **raise**
>
> **return** type(obj).\_\_getattr\_\_(obj, name)
>
> (continued from previous page)

*\#* *\_\_getattr\_\_*

**3.6** **Invocation** **from** **a** **class**

The logic for a dotted lookup such as A.x is in
type.\_\_getattribute\_\_(). The steps are similar to those for
object.\_\_getattribute\_\_() but the instance dictionary lookup is
replaced by a search through the class’s method resolution order.

If a descriptor is found, it is invoked with desc.\_\_get\_\_(None, A).

The full C implementation can be found in type_getattro() and
\_PyType_Lookup() in
[Objects/typeobject.c](https://github.com/python/cpython/tree/3.13/Objects/typeobject.c).

**3.7** **Invocation** **from** **super**

The logic for super’s dotted lookup is in the \_\_getattribute\_\_()
method for object returned by super().

A dotted lookup such as super(A, obj).m searches
obj.\_\_class\_\_.\_\_mro\_\_ for the base class B immediately following
A and then returns B.\_\_dict\_\_\['m'\].\_\_get\_\_(obj, A). If not a
descriptor, m is returned unchanged.

The full C implementation can be found in super_getattro() in
[Objects/typeobject.c](https://github.com/python/cpython/tree/3.13/Objects/typeobject.c).
A pure Python equivalent can be found in [Guido’s
Tutorial.](https://www.python.org/download/releases/2.2.3/descrintro/#cooperation)

**3.8** **Summary** **of** **invocation** **logic**

The mechanism for descriptors is embedded in the \_\_getattribute\_\_()
methods for object, type, and super().

The important points to remember are:

> • Descriptors are invoked by the \_\_getattribute\_\_() method. •
> Classes inherit this machinery from object, type, or super().
>
> • Overriding \_\_getattribute\_\_() prevents automatic descriptor
> calls because all the descriptor logic is in that method.
>
> • object.\_\_getattribute\_\_() and type.\_\_getattribute\_\_() make
> different calls to \_\_get\_\_(). The first includes the instance and
> may include the class. The second puts in None for the instance and
> always includes the class.
>
> • Data descriptors always override instance dictionaries.
>
> • Non-data descriptors may be overridden by instance dictionaries.

**3.9** **Automatic** **name** **notification**

Sometimes it is desirable for a descriptor to know what class variable
name it was assigned to. When a new class is created, the type metaclass
scans the dictionary of the new class. If any of the entries are
descriptors and if they define \_\_set_name\_\_(), that method is called
with two arguments. The *owner* is the class where the descriptor is
used, and the *name* is the class variable the descriptor was assigned
to.

The implementation details are in type_new() and set_names() in
[Objects/typeobject.c](https://github.com/python/cpython/tree/3.13/Objects/typeobject.c).

Sincetheupdatelogicisintype.\_\_new\_\_(),
notificationsonlytakeplaceatthetimeofclasscreation. Ifdescriptors are
added to the class afterwards, \_\_set_name\_\_() will need to be called
manually.

> **11**

**3.10** **ORM** **example**

The following code is a simplified skeleton showing how data descriptors
could be used to implement an
[object](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
[relational
mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping).

The essential idea is that the data is stored in an external database.
The Python instances only hold keys to the database’s tables.
Descriptors take care of lookups or updates:

**class** **Field**:

> **def** \_\_set_name\_\_(self, owner, name):
>
> self.fetch = f'SELECT *{*name*}* FROM *{*owner.table*}* WHERE
> *{*owner.key*}*=?;' self.store = f'UPDATE *{*owner.table*}* SET
> *{*name*}*=? WHERE *{*owner.key*}*=?;'
>
> **def** \_\_get\_\_(self, obj, objtype=**None**):
>
> **return** conn.execute(self.fetch, \[obj.key\]).fetchone()\[0\]
>
> **def** \_\_set\_\_(self, obj, value): conn.execute(self.store,
> \[value, obj.key\]) conn.commit()

We can use the Field class to define
[models](https://en.wikipedia.org/wiki/Database_model) that describe the
schema for each table in a database:

**class** **Movie**:

> table = 'Movies' key = 'title' director = Field() year = Field()

*\#* *Table* *name* *\#* *Primary* *key*

> **def** \_\_init\_\_(self, key): self.key = key

**class** **Song**:

> table = 'Music' key = 'title' artist = Field() year = Field() genre =
> Field()
>
> **def** \_\_init\_\_(self, key): self.key = key

To use the models, first connect to the database:

**\>\>\>** **import** **sqlite3**

**\>\>\>** conn = sqlite3.connect('entertainment.db')

An interactive session shows how data is retrieved from the database and
how it can be updated:

**\>\>\>** Movie('Star Wars').director 'George Lucas'

**\>\>\>** jaws = Movie('Jaws')

**\>\>\>** f'Released in *{*jaws.year*}* by *{*jaws.director*}*'
'Released in 1975 by Steven Spielberg'

**\>\>\>** Song('Country Roads').artist 'John Denver'

**\>\>\>** Movie('Star Wars').director = 'J.J. Abrams'

> (continues on next page)
>
> **12**
>
> (continued from previous page)

**\>\>\>** Movie('Star Wars').director 'J.J. Abrams'

**4** **Pure** **Python** **Equivalents**

The descriptor protocol is simple and offers exciting possibilities.
Several use cases are so common that they have been prepackaged into
built-in tools. Properties, bound methods, static methods, class
methods, and \_\_slots\_\_ are all based on the descriptor protocol.

**4.1** **Properties**

Calling property() is a succinct way of building a data descriptor that
triggers a function call upon access to an attribute. Its signature is:

property(fget=**None**, fset=**None**, fdel=**None**, doc=**None**) -\>
property

The documentation shows a typical use to define a managed attribute x:

**class** **C**:

> **def** getx(self): **return** self.\_\_x
>
> **def** setx(self, value): self.\_\_x = value **def** delx(self):
> **del** self.\_\_x
>
> x = property(getx, setx, delx, "I'm the 'x' property.")

To see how property() is implemented in terms of the descriptor
protocol, here is a pure Python equivalent that implements most of the
core functionality:

**class** **Property**:

> "Emulate PyProperty_Type() in Objects/descrobject.c"
>
> **def** \_\_init\_\_(self, fget=**None**, fset=**None**,
> fdel=**None**, doc=**None**): self.fget = fget
>
> self.fset = fset self.fdel = fdel
>
> **if** doc **is** **None** **and** fget **is** **not** **None**: doc =
> fget.\_\_doc\_\_
>
> self.\_\_doc\_\_ = doc
>
> **def** \_\_set_name\_\_(self, owner, name): self.\_\_name\_\_ = name
>
> **def** \_\_get\_\_(self, obj, objtype=**None**): **if** obj **is**
> **None**:
>
> **return** self
>
> **if** self.fget **is** **None**: **raise** AttributeError
>
> **return** self.fget(obj)
>
> **def** \_\_set\_\_(self, obj, value): **if** self.fset **is**
> **None**:
>
> **raise** AttributeError self.fset(obj, value)
>
> **def** \_\_delete\_\_(self, obj): **if** self.fdel **is** **None**:
>
> **raise** AttributeError
>
> (continues on next page)
>
> **13**
>
> (continued from previous page) self.fdel(obj)
>
> **def** getter(self, fget):
>
> **return** type(self)(fget, self.fset, self.fdel, self.\_\_doc\_\_)
>
> **def** setter(self, fset):
>
> **return** type(self)(self.fget, fset, self.fdel, self.\_\_doc\_\_)
>
> **def** deleter(self, fdel):
>
> **return** type(self)(self.fget, self.fset, fdel, self.\_\_doc\_\_)

The property() builtin helps whenever a user interface has granted
attribute access and then subsequent changes require the intervention of
a method.

For instance, a spreadsheet class may grant access to a cell value
through Cell('b10').value. Subsequent im-provements to the program
require the cell to be recalculated on every access; however, the
programmer does not want to affect existing client code accessing the
attribute directly. The solution is to wrap access to the value
attribute in a property data descriptor:

**class** **Cell**: ...

> **@property**
>
> **def** value(self):
>
> "Recalculate the cell before returning value" self.recalc()
>
> **return** self.\_value

Either the built-in property() or our Property() equivalent would work
in this example.

**4.2** **Functions** **and** **methods**

Python’s object oriented features are built upon a function based
environment. Using non-data descriptors, the two are merged seamlessly.

Functions stored in class dictionaries get turned into methods when
invoked. Methods only differ from regular func-tions in that the object
instance is prepended to the other arguments. By convention, the
instance is called *self* but could be called *this* or any other
variable name.

Methods can be created manually with types.MethodType which is roughly
equivalent to:

**class** **MethodType**:

> "Emulate PyMethod_Type in Objects/classobject.c"
>
> **def** \_\_init\_\_(self, func, obj): self.\_\_func\_\_ = func
> self.\_\_self\_\_ = obj
>
> **def** \_\_call\_\_(self, \*args, \*\*kwargs): func =
> self.\_\_func\_\_
>
> obj = self.\_\_self\_\_
>
> **return** func(obj, \*args, \*\*kwargs)
>
> **def** \_\_getattribute\_\_(self, name):
>
> "Emulate method_getset() in Objects/classobject.c" **if** name ==
> '\_\_doc\_\_':
>
> **return** self.\_\_func\_\_.\_\_doc\_\_
>
> **return** object.\_\_getattribute\_\_(self, name)
>
> (continues on next page)
>
> **14**
>
> (continued from previous page)
>
> **def** \_\_getattr\_\_(self, name):
>
> "Emulate method_getattro() in Objects/classobject.c" **return**
> getattr(self.\_\_func\_\_, name)
>
> **def** \_\_get\_\_(self, obj, objtype=**None**):
>
> "Emulate method_descr_get() in Objects/classobject.c" **return** self

To support automatic creation of methods, functions include the
\_\_get\_\_() method for binding methods during attribute access. This
means that functions are non-data descriptors that return bound methods
during dotted lookup from an instance. Here’s how it works:

**class** **Function**: ...

> **def** \_\_get\_\_(self, obj, objtype=**None**):
>
> "Simulate func_descr_get() in Objects/funcobject.c" **if** obj **is**
> **None**:
>
> **return** self
>
> **return** MethodType(self, obj)

Running the following class in the interpreter shows how the function
descriptor works in practice:

**class** **D**:

> **def** f(self): **return** self

**class** **D2**: **pass**

The function has a qualified name attribute to support introspection:

**\>\>\>** D.f.\_\_qualname\_\_ 'D.f'

Accessingthefunctionthroughtheclassdictionarydoesnotinvoke\_\_get\_\_().
Instead, itjustreturnstheunderlying function object:

**\>\>\>** D.\_\_dict\_\_\['f'\] \<function D.f at 0x00C45070\>

Dotted access from a class calls \_\_get\_\_() which just returns the
underlying function unchanged:

**\>\>\>** D.f

\<function D.f at 0x00C45070\>

The interesting behavior occurs during dotted access from an instance.
The dotted lookup calls \_\_get\_\_() which returns a bound method
object:

**\>\>\>** d = D() **\>\>\>** d.f

\<bound method D.f of \<\_\_main\_\_.D object at 0x00B18C90\>\>

Internally, the bound method stores the underlying function and the
bound instance:

**\>\>\>** d.f.\_\_func\_\_

\<function D.f at 0x00C45070\>

> (continues on next page)
>
> **15**
>
> (continued from previous page)

**\>\>\>** d.f.\_\_self\_\_

\<\_\_main\_\_.D object at 0x00B18C90\>

If you have ever wondered where *self* comes from in regular methods or
where *cls* comes from in class methods, this is it!

**4.3** **Kinds** **of** **methods**

Non-data descriptors provide a simple mechanism for variations on the
usual patterns of binding functions into meth-ods.

To recap, functions have a \_\_get\_\_() method so that they can be
converted to a method when accessed as attributes. The non-data
descriptor transforms an obj.f(\*args) call into f(obj, \*args). Calling
cls.f(\*args) be-comes f(\*args).

This chart summarizes the binding and its two most useful variants:

||
||
||
||
||
||
||
||

**4.4** **Static** **methods**

Static methods return the underlying function without changes. Calling
either c.f or C.f is the equivalent of a direct lookup into
object.\_\_getattribute\_\_(c, "f") or object.\_\_getattribute\_\_(C,
"f"). As a result, the function becomes identically accessible from
either an object or a class.

Good candidates for static methods are methods that do not reference the
self variable.

For instance, a statistics package may include a container class for
experimental data. The class provides normal methods for computing the
average, mean, median, and other descriptive statistics that depend on
the data. However, there may be useful functions which are conceptually
related but do not depend on the data. For instance, erf(x) is handy
conversion routine that comes up in statistical work but does not
directly depend on a particular dataset. It can be called either from an
object or the class: s.erf(1.5) --\> 0.9332 or Sample.erf(1.5) --\>
0.9332.

Since static methods return the underlying function with no changes, the
example calls are unexciting:

**class** **E**: **@staticmethod** **def** f(x):

> **return** x \* 10

**\>\>\>** E.f(3) 30

**\>\>\>** E().f(3) 30

Using the non-data descriptor protocol, a pure Python version of
staticmethod() would look like this:

**import** **functools**

**class** **StaticMethod**:

> "Emulate PyStaticMethod_Type() in Objects/funcobject.c"
>
> **def** \_\_init\_\_(self, f):
>
> (continues on next page)
>
> **16**
>
> (continued from previous page)
>
> self.f = f functools.update_wrapper(self, f)
>
> **def** \_\_get\_\_(self, obj, objtype=**None**): **return** self.f
>
> **def** \_\_call\_\_(self, \*args, \*\*kwds): **return**
> self.f(\*args, \*\*kwds)

The functools.update_wrapper() call adds a \_\_wrapped\_\_ attribute
that refers to the underlying function. Also it carries forward the
attributes necessary to make the wrapper look like the wrapped function:
\_\_name\_\_, \_\_qualname\_\_, \_\_doc\_\_, and \_\_annotations\_\_.

**4.5** **Class** **methods**

Unlike static methods, class methods prepend the class reference to the
argument list before calling the function. This format is the same for
whether the caller is an object or a class:

**class** **F**: **@classmethod** **def** f(cls, x):

> **return** cls.\_\_name\_\_, x

**\>\>\>** F.f(3) ('F', 3)

**\>\>\>** F().f(3) ('F', 3)

This behavior is useful whenever the method only needs to have a class
reference and does not rely on data stored in a specific instance. One
use for class methods is to create alternate class constructors. For
example, the classmethod dict.fromkeys() creates a new dictionary from a
list of keys. The pure Python equivalent is:

**class** **Dict**(dict): **@classmethod**

> **def** fromkeys(cls, iterable, value=**None**):
>
> "Emulate dict_fromkeys() in Objects/dictobject.c" d = cls()
>
> **for** key **in** iterable: d\[key\] = value
>
> **return** d

Now a new dictionary of unique keys can be constructed like this:

**\>\>\>** d = Dict.fromkeys('abracadabra') **\>\>\>** type(d) **is**
Dict

True **\>\>\>** d

{'a': None, 'b': None, 'r': None, 'c': None, 'd': None}

Using the non-data descriptor protocol, a pure Python version of
classmethod() would look like this:

**import** **functools**

**class** **ClassMethod**:

> "Emulate PyClassMethod_Type() in Objects/funcobject.c"
>
> **def** \_\_init\_\_(self, f):
>
> (continues on next page)
>
> **17**
>
> (continued from previous page)
>
> self.f = f functools.update_wrapper(self, f)
>
> **def** \_\_get\_\_(self, obj, cls=**None**): **if** cls **is**
> **None**:
>
> cls = type(obj)
>
> **return** MethodType(self.f, cls)

The functools.update_wrapper() call in ClassMethod adds a
\_\_wrapped\_\_ attribute that refers to the underlying function. Also
it carries forward the attributes necessary to make the wrapper look
like the wrapped function: \_\_name\_\_, \_\_qualname\_\_, \_\_doc\_\_,
and \_\_annotations\_\_.

**4.6** **Member** **objects** **and** **\_\_slots\_\_**

When a class defines \_\_slots\_\_, it replaces instance dictionaries
with a fixed-length array of slot values. From a user point of view that
has several effects:

1\. Provides immediate detection of bugs due to misspelled attribute
assignments. Only attribute names specified in \_\_slots\_\_ are
allowed:

**class** **Vehicle**:

> \_\_slots\_\_ = ('id_number', 'make', 'model')

**\>\>\>** auto = Vehicle()

**\>\>\>** auto.id_nubmer = 'VYE483814LQEX' Traceback (most recent call
last):

> ...

AttributeError: 'Vehicle' object has no attribute 'id_nubmer'

2\. Helps create immutable objects where descriptors manage access to
private attributes stored in \_\_slots\_\_:

**class** **Immutable**:

> \_\_slots\_\_ = ('\_dept', '\_name')
>
> **def** \_\_init\_\_(self, dept, name): self.\_dept = dept self.\_name
> = name
>
> **@property**
>
> **def** dept(self): **return** self.\_dept
>
> **@property**
>
> **def** name(self): **return** self.\_name

*\#* *Replace* *the* *instance* *dictionary*

*\#* *Store* *to* *private* *attribute* *\#* *Store* *to* *private*
*attribute*

*\#* *Read-only* *descriptor*

*\#* *Read-only* *descriptor*

**\>\>\>** mark = Immutable('Botany', 'Mark Watney') **\>\>\>**
mark.dept

'Botany'

**\>\>\>** mark.dept = 'Space Pirate' Traceback (most recent call last):

> ...

AttributeError: property 'dept' of 'Immutable' object has no setter
**\>\>\>** mark.location = 'Mars'

Traceback (most recent call last):

> (continues on next page)
>
> **18**
>
> (continued from previous page)
>
> ...

AttributeError: 'Immutable' object has no attribute 'location'

3\. Saves memory. On a 64-bit Linux build, an instance with two
attributes takes 48 bytes with \_\_slots\_\_ and 152 bytes without. This
[flyweight design
pattern](https://en.wikipedia.org/wiki/Flyweight_pattern) likely only
matters when a large number of instances are going to be created.

4\. Improves speed. Reading instance variables is 35% faster with
\_\_slots\_\_ (as measured with Python 3.10 on an Apple M1 processor).

5\. Blocks tools like functools.cached_property() which require an
instance dictionary to function correctly:

**from** **functools** **import** cached_property

**class** **CP**:

> \_\_slots\_\_ = () *\#* *Eliminates* *the* *instance* *dict*
>
> **@cached_property** *\#* *Requires* *an* *instance* *dict* **def**
> pi(self):
>
> **return** 4 \* sum((-1.0)\*\*n / (2.0\*n + 1.0)
>
> **for** n **in** reversed(range(100_000)))

**\>\>\>** CP().pi

Traceback (most recent call last): *...*

TypeError: No '\_\_dict\_\_' attribute on 'CP' instance to cache 'pi'
property.

It is not possible to create an exact drop-in pure Python version of
\_\_slots\_\_ because it requires direct access to C structures and
control over object memory allocation. However, we can build a mostly
faithful simulation where the actual C structure for slots is emulated
by a private \_slotvalues list. Reads and writes to that private
structure are managed by member descriptors:

null = object()

**class** **Member**:

> **def** \_\_init\_\_(self, name, clsname, offset):
>
> 'Emulate PyMemberDef in Include/structmember.h' *\#* *Also* *see*
> *descr_new()* *in* *Objects/descrobject.c* self.name = name
>
> self.clsname = clsname self.offset = offset
>
> **def** \_\_get\_\_(self, obj, objtype=**None**):
>
> 'Emulate member_get() in Objects/descrobject.c'
>
> *\#* *Also* *see* *PyMember_GetOne()* *in* *Python/structmember.c*
> **if** obj **is** **None**:
>
> **return** self
>
> value = obj.\_slotvalues\[self.offset\] **if** value **is** null:
>
> **raise** AttributeError(self.name) **return** value
>
> **def** \_\_set\_\_(self, obj, value):
>
> 'Emulate member_set() in Objects/descrobject.c'
> obj.\_slotvalues\[self.offset\] = value
>
> (continues on next page)
>
> **19**
>
> (continued from previous page)
>
> **def** \_\_delete\_\_(self, obj):
>
> 'Emulate member_delete() in Objects/descrobject.c' value =
> obj.\_slotvalues\[self.offset\]
>
> **if** value **is** null:
>
> **raise** AttributeError(self.name) obj.\_slotvalues\[self.offset\] =
> null
>
> **def** \_\_repr\_\_(self):
>
> 'Emulate member_repr() in Objects/descrobject.c' **return** f'\<Member
> *{*self.name*!r}* of *{*self.clsname*!r}*\>'

The type.\_\_new\_\_() method takes care of adding member objects to
class variables:

**class** **Type**(type):

> 'Simulate how the type metaclass adds member objects for slots'
>
> **def** \_\_new\_\_(mcls, clsname, bases, mapping, \*\*kwargs):
> 'Emulate type_new() in Objects/typeobject.c'
>
> *\#* *type_new()* *calls* *PyTypeReady()* *which* *calls*
> *add_methods()* slot_names = mapping.get('slot_names', \[\])
>
> **for** offset, name **in** enumerate(slot_names): mapping\[name\] =
> Member(name, clsname, offset)
>
> **return** type.\_\_new\_\_(mcls, clsname, bases, mapping, \*\*kwargs)

The object.\_\_new\_\_() method takes care of creating instances that
have slots instead of an instance dictionary. Here is a rough simulation
in pure Python:

**class** **Object**:

> 'Simulate how object.\_\_new\_\_() allocates memory for \_\_slots\_\_'
>
> **def** \_\_new\_\_(cls, \*args, \*\*kwargs):
>
> 'Emulate object_new() in Objects/typeobject.c' inst =
> super().\_\_new\_\_(cls)
>
> **if** hasattr(cls, 'slot_names'):
>
> empty_slots = \[null\] \* len(cls.slot_names)
> object.\_\_setattr\_\_(inst, '\_slotvalues', empty_slots)
>
> **return** inst
>
> **def** \_\_setattr\_\_(self, name, value):
>
> 'Emulate \_PyObject_GenericSetAttrWithDict() Objects/object.c' cls =
> type(self)
>
> **if** hasattr(cls, 'slot_names') **and** name **not** **in**
> cls.slot_names: **raise** AttributeError(
>
> f'*{*cls.\_\_name\_\_*!r}* object has no attribute *{*name*!r}*' )
>
> super().\_\_setattr\_\_(name, value)
>
> **def** \_\_delattr\_\_(self, name):
>
> 'Emulate \_PyObject_GenericSetAttrWithDict() Objects/object.c' cls =
> type(self)
>
> **if** hasattr(cls, 'slot_names') **and** name **not** **in**
> cls.slot_names: **raise** AttributeError(
>
> f'*{*cls.\_\_name\_\_*!r}* object has no attribute *{*name*!r}*' )
>
> super().\_\_delattr\_\_(name)

To use the simulation in a real class, just inherit from Object and set
the metaclass to Type:

> **20**

**class** **H**(Object, metaclass=Type): 'Instance variables stored in
slots'

> slot_names = \['x', 'y'\]
>
> **def** \_\_init\_\_(self, x, y): self.x = x
>
> self.y = y

At this point, the metaclass has loaded member objects for *x* and *y*:

**\>\>\>** **from** **pprint** **import** pp **\>\>\>**
pp(dict(vars(H))) {'\_\_module\_\_': '\_\_main\_\_',

> '\_\_doc\_\_': 'Instance variables stored in slots', 'slot_names':
> \['x', 'y'\],
>
> '\_\_init\_\_': \<function H.\_\_init\_\_ at 0x7fb5d302f9d0\>, 'x':
> \<Member 'x' of 'H'\>,
>
> 'y': \<Member 'y' of 'H'\>}

When instances are created, they have a slot_values list where the
attributes are stored:

**\>\>\>** h = H(10, 20) **\>\>\>** vars(h)

{'\_slotvalues': \[10, 20\]} **\>\>\>** h.x = 55

**\>\>\>** vars(h) {'\_slotvalues': \[55, 20\]}

Misspelled or unassigned attributes will raise an exception:

**\>\>\>** h.xz

Traceback (most recent call last): ...

AttributeError: 'H' object has no attribute 'xz'

> **21**
