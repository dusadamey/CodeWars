# https://www.codewars.com/kata/5121303128ef4b495f000001/train/python

'''
Instructions:

The following code could use a bit of object oriented artistry. While its a simple method and works just fine as it is, in a larger system its best to organize methods into classes/objects. Refactor the following code so that it belongs to a Person class/object. Each Person instance will have a greet method. The Person instance should be instantiated with a name so that it no longer has to be passed into each greet method call.

Here is how the final refactored code would be used:

joe = Person('Joe')
joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
joe.name          # should == 'Joe'
'''


class Person:
    def __init__(self, name):
        self.name = name
    def greet(self, name):
        return "Hello %s, my name is %s" % (name, self.name)
