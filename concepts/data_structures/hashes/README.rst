###########
Hash Tables
###########

.. contents:: Hash Tables


********************
Direct-address table
********************

A direct address table is a hash table where the hash function is the identity function.
They are a good choice when:

* The number of possible keys is small
* The keys are unique

If the universe of keys is :math:`U = \{0,1,...,m-1\}`, then a direct address table
can be implemented as an array ``T[m-1]``, where each slot corresponds to a unique key:

.. code-block:: python

   class DirectAddressTable(object):
       def __init__(self, size):
           self.size = size
           self.table = [None]*size

Direct address tables support `insert`, `delete`, and `search` operations, all in ``O(1)`` time.
However, because you have to maintain an array equal in size to the universe of keys, as soon
as this universe grows beyond a certain size, direct-address tables quickly become inefficient.


**********
Hash Table
**********
