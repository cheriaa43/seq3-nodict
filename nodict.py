#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Cheria Artis'


class Node:
    """Define a class named `Node` that can be initialized with a key (mandatory) and a value (optional).
    """
    def __init__(self, key, value=None):
        """Similar to a constructor in other languages"""
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        """
        The Node class should print a human-readable representation of its key/value contents when asked. The `__repr__` method can do this.
        """
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """The Node class object should be able to compare itself to other Node objects using the Python built-in `==` operator.
        """
        # Your code here
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """Similar to a constructor in other languages. Class initializer to create the buckets according to a size parameter. Save the size parameter as an instance variable in the class. Create another instance variable to hold the bucket list. Your instance variable should be named `self.buckets`.
        """
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        """Return a string representing the NoDict contents."""
         # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        """
        This class method should accept a new key and value, and store it into the `NoDict` instance. However, this method should not allow duplicate keys.  First, make a `Node` class using the key and value, e.g. `new_node = Node(key, value)`.
        """
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for kv in bucket:
            if kv == new_node:
                bucket.remove(kv)
                break
        bucket.append(new_node)

    def get(self, key):
        """
        This class method should perform a key-lookup in the `NoDict` class. It should accept just one parameter: The key to look up. If the key is found in the `NoDict` class, return its associated value. If the key is not found, raise a `KeyError` exceptiondatetime A combination of a date and a time. Attributes: ()
        """
        key_val = Node(key)
        bucket = self.buckets[key_val.hash % self.size]
        for kv in bucket:
            if kv == key_val:
                return kv.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """"
        Implement this magic "dunder" method within the `NoDict` class to enable square-bracket _reading_ behavior. 
        """
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        """
        Implement this magic "dunder" method within the `NoDict` class to enable square-bracket _assignment_ behavior. Think of it like a setter method.
        """
        self.add(key, value)
