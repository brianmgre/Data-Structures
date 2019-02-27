For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

<!-- 1. What is the runtime complexity of `add_to_tail`?

   a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?

2. What is the runtime complexity of `remove_head`?

3. What is the runtime complexity of `contains`?

4. What is the runtime complexity of `get_max`? -->

## Queue

1. What is the runtime complexity of `enqueue`?

The run time complexity of a Queue's enqueue feature is O(1). As the queue is large, it will take the same amount of time.

2. What is the runtime complexity of `dequeue`?

O(1) same as enqueue, there is no change in runtime with an increase in size.


3. What is the runtime complexity of `len`?

O(1) same as above.   

## Binary Search Tree

1. What is the runtime complexity of `insert`?

o(log(n)) the way a bst is setup is conducive to searching and finding the correct spot to insert. Meaning the entire bst does not have to be search. it is also why questions 2 and 3 are the same. 

2. What is the runtime complexity of `contains`?

o(Log n) 

3. What is the runtime complexity of `get_max`?

O(log n) 

## Heap

1. What is the runtime complexity of `_bubble_up`?

O(log n)

2. What is the runtime complexity of `_sift_down`?

O(log n ) depends on the number of levels

3. What is the runtime complexity of `insert`?

O(log n) The number of operations depends on the number of levels the new element must rise

4. What is the runtime complexity of `delete`?

O(log n) because you replace the top element with the last level and then sift down so the heap is back with the largest value on top. 

5. What is the runtime complexity of `get_max`?

O(1) if it is a max-heap, then the max value will be ready avaiable to us at the top of the heap. 

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

O(n) as you have to traverse the entire list



2. What is the runtime complexity of `ListNode.insert_before`?

O(1) as you have to traverse the entire list

3. What is the runtime complexity of `ListNode.delete`?

O(1) depending on where the node is located

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

O(1) head is easily accessible

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

O(1) head is easily accessible

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

O(1) same as the head

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

0(1) same as head, as long as tail is known

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

0(1) depending on where the node is located

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

0(1) depending on where the node is located

10. What is the runtime complexity of `DoublyLinkedList.delete`?

0(1) this depends on where the node is located and if the entire list is searched to find the node to delete

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better? 

    a doubly linked list is O(1) in worst case and array.slice is O(n). So doubly linked list method generally performs better. 


