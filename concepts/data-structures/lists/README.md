# Lists

Various list implementations. Complexity always refers to

## Single Linked List

* **Prepend**
    * **Complexity**: `O(1)`
    * **Brief Explanation**: The linked list simply maintains which node is the head, so
    `insert` just replaces the head with our new node, and sets that node's `next` value
    to the previous head.

* **Append**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: Have to iterate through the entire list until we reach the last
    node, and then append the new value to the end.

* **Size**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: `size` visits every node in order to count the number of nodes.

* **Search**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: Worst-case scenario, `search` visits every node.

* **Delete**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: Worst-case scenario, `delete` visits every node.
