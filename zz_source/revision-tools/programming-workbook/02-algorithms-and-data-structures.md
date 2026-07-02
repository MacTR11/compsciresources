# Programming Workbook 2 — Algorithms & Data Structures

*OCR A Level Computer Science (H446), Component 02 — targeting Section 2.3 (Algorithms) and Section 1.4.2 (Data structures).*

This workbook gives you **practical coding challenges** with full, runnable solutions. Solutions are in **Python 3**, but you may answer in your own chosen language (Java, C#, VB.NET, etc.) — the *logic* and the **Big O complexity** are what matter for the exam. Where it clarifies the algorithm, **OCR exam-reference pseudocode** is shown alongside.

**How to use it**

1. Read the task and the example input/output.
2. Attempt it on paper or in an IDE **before** opening the solution.
3. Open `<details>Solution</details>`, compare, and read the explanation — especially the **Big O** line.
4. Re-type the solution from memory; that is how the algorithms stick.

**Difficulty key:** ★ = warm-up · ★★ = core exam standard · ★★★ = stretch / A* territory.

**Quick Big O reminder** — drop constants and lower-order terms; Big O describes the **worst-case** growth of operations (time) or memory (space) as input size *n* grows. `3n² + 5n + 17` → **O(n²)**.

---

## Section A — Searching algorithms

### Challenge 1 — Linear search ★

**Task.** Write a function `linear_search(data, target)` that returns the **index** of `target` in the list `data`, or `-1` if it is not present. The list need **not** be sorted.

**Example I/O**

```
linear_search([4, 2, 7, 1, 9, 3], 7)  ->  2
linear_search([4, 2, 7, 1, 9, 3], 5)  -> -1
```

<details><summary>Solution</summary>

```python
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i          # found — return position immediately
    return -1                 # whole list checked, not found

# Tests
print(linear_search([4, 2, 7, 1, 9, 3], 7))   # 2
print(linear_search([4, 2, 7, 1, 9, 3], 5))   # -1
```

OCR pseudocode equivalent:

```
function linearSearch(data, target)
    for i = 0 to data.length - 1
        if data[i] == target then
            return i
        endif
    next i
    return -1
endfunction
```

**Explanation.** We inspect each element once until we find the target (or run out of elements). It works on **unsorted** data, which is its main advantage over binary search.

**Big O:** worst/average case **O(n)** time (the target may be last or absent, so all *n* items are checked); best case **O(1)** (first item). Space **O(1)** — no extra structure used. ✅

</details>

---

### Challenge 2 — Binary search, iterative **and** recursive ★★

**Task.** The list is **already sorted ascending**. Write **two** versions of binary search that return the index of `target` or `-1`:

- `binary_search_iter(data, target)` using a loop.
- `binary_search_rec(data, target)` using recursion.

**Example I/O**

```
binary_search_iter([1, 3, 5, 7, 9, 11], 7)  ->  3
binary_search_iter([1, 3, 5, 7, 9, 11], 8)  -> -1
binary_search_rec ([1, 3, 5, 7, 9, 11], 11) ->  5
```

<details><summary>Solution</summary>

```python
# --- Iterative version ---
def binary_search_iter(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2     # integer division
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1           # discard left half
        else:
            high = mid - 1          # discard right half
    return -1

# --- Recursive version ---
def binary_search_rec(data, target, low=0, high=None):
    if high is None:                # first call: set the upper bound
        high = len(data) - 1
    if low > high:                  # base case: empty range -> not found
        return -1
    mid = (low + high) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search_rec(data, target, mid + 1, high)
    else:
        return binary_search_rec(data, target, low, mid - 1)

print(binary_search_iter([1, 3, 5, 7, 9, 11], 7))    # 3
print(binary_search_iter([1, 3, 5, 7, 9, 11], 8))    # -1
print(binary_search_rec ([1, 3, 5, 7, 9, 11], 11))   # 5
```

OCR pseudocode (iterative):

```
function binarySearch(data, target)
    low = 0
    high = data.length - 1
    while low <= high
        mid = (low + high) DIV 2
        if data[mid] == target then
            return mid
        elseif data[mid] < target then
            low = mid + 1
        else
            high = mid - 1
        endif
    endwhile
    return -1
endfunction
```

**Explanation.** Each comparison halves the remaining search space by examining the middle element and discarding the half that cannot contain the target. **The list must be sorted** for this to work. Doubling the list size adds just **one** extra step — that is logarithmic growth.

**Big O:** **O(log n)** time for both versions (worst and average); best case **O(1)** (target is the first midpoint). Space: the iterative version is **O(1)**; the recursive version is **O(log n)** because of the call stack (one frame per level of recursion). ✅

</details>

---

## Section B — Sorting algorithms

### Challenge 3 — Bubble sort ★★

**Task.** Write `bubble_sort(data)` that returns a **new sorted (ascending)** list. Include the optimisation that stops early if a pass makes no swaps.

**Example I/O**

```
bubble_sort([5, 1, 4, 2, 8])  ->  [1, 2, 4, 5, 8]
```

<details><summary>Solution</summary>

```python
def bubble_sort(data):
    a = data[:]                       # copy so the original is untouched
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):    # last i items are already in place
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]   # swap
                swapped = True
        if not swapped:               # no swaps -> already sorted, stop
            break
    return a

print(bubble_sort([5, 1, 4, 2, 8]))   # [1, 2, 4, 5, 8]
```

**Explanation.** On each pass, adjacent out-of-order pairs are swapped, so the largest remaining value "bubbles" to its correct end position. After pass *i*, the last *i* items are final — that is why the inner loop shrinks. The `swapped` flag lets a list that becomes sorted early finish in one clean pass.

**Big O:** worst and average **O(n²)** time (two nested loops over *n*); best case **O(n)** thanks to the early-exit flag (one pass over an already-sorted list). Space **O(1)** — sorting is in place. Bubble sort is **stable**. ✅

</details>

---

### Challenge 4 — Insertion sort ★★

**Task.** Write `insertion_sort(data)` returning a new ascending-sorted list, building the sorted portion one element at a time.

**Example I/O**

```
insertion_sort([9, 5, 1, 4, 3])  ->  [1, 3, 4, 5, 9]
```

<details><summary>Solution</summary>

```python
def insertion_sort(data):
    a = data[:]
    for i in range(1, len(a)):
        key = a[i]                    # the value to insert
        j = i - 1
        # shift larger elements one place to the right
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key                # drop key into the gap
    return a

print(insertion_sort([9, 5, 1, 4, 3]))   # [1, 3, 4, 5, 9]
```

**Explanation.** The list is split into a sorted left part and an unsorted right part. Each new `key` is shifted leftwards into its correct slot within the sorted part (like sorting a hand of playing cards). It is efficient on **small or nearly-sorted** lists.

**Big O:** worst and average **O(n²)** time (each insertion may shift up to *i* elements); best case **O(n)** when the input is already sorted (the inner `while` never runs). Space **O(1)** — in place. Insertion sort is **stable**. ✅

</details>

---

### Challenge 5 — Merge sort ★★★

**Task.** Write `merge_sort(data)` using the **divide-and-conquer** approach: split the list, sort each half recursively, then merge.

**Example I/O**

```
merge_sort([38, 27, 43, 3, 9, 82, 10])  ->  [3, 9, 10, 27, 38, 43, 82]
```

<details><summary>Solution</summary>

```python
def merge_sort(data):
    if len(data) <= 1:                # base case: 0 or 1 item is sorted
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])     # divide and sort left half
    right = merge_sort(data[mid:])    # divide and sort right half
    return merge(left, right)         # conquer: combine

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:       # <= keeps the sort stable
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])           # one side is exhausted; add the rest
    result.extend(right[j:])
    return result

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))   # [3, 9, 10, 27, 38, 43, 82]
```

**Explanation.** **Divide:** repeatedly split the list in half until each piece has one element (trivially sorted). **Conquer/merge:** repeatedly merge two sorted lists by comparing their front elements. There are **log n** levels of splitting, and merging at each level touches all **n** elements.

**Big O:** **O(n log n)** time in **all** cases (best, average and worst) — the consistent performance is merge sort's headline strength. Space **O(n)** because the merge step needs extra lists (more memory-hungry than the in-place sorts). Merge sort is **stable**. ✅

</details>

---

### Challenge 6 — Quick sort ★★★

**Task.** Write `quick_sort(data)` using divide-and-conquer around a **pivot**. (A clear, readable partition is fine for the exam — you do not need the classic in-place Lomuto/Hoare scheme.)

**Example I/O**

```
quick_sort([3, 6, 1, 8, 2, 9, 4])  ->  [1, 2, 3, 4, 6, 8, 9]
```

<details><summary>Solution</summary>

```python
def quick_sort(data):
    if len(data) <= 1:                       # base case
        return data
    pivot = data[len(data) // 2]             # choose a pivot (middle element)
    less    = [x for x in data if x < pivot]
    equal   = [x for x in data if x == pivot]
    greater = [x for x in data if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort([3, 6, 1, 8, 2, 9, 4]))     # [1, 2, 3, 4, 6, 8, 9]
```

**Explanation.** Pick a **pivot**, then **partition** the rest into items smaller than it and items larger than it. The pivot is now in its final sorted position. Recursively sort the two partitions and concatenate. Choosing a good pivot keeps the partitions balanced.

**Big O:** average **O(n log n)** time (balanced partitions, ~log n levels each costing O(n)); **worst case O(n²)** when the pivot is consistently the smallest or largest value (e.g. an already-sorted list with a poor pivot choice), giving very unbalanced partitions. The classic in-place version uses **O(log n)** space for the recursion stack; this readable version builds new lists, so it uses **O(n)** space. The simple version above is **not** stable. ✅

</details>

---

## Section C — Data structures (Section 1.4.2)

### Challenge 7 — Implement a Stack class ★★

**Task.** Implement a **Stack** (LIFO — Last In, First Out) class supporting `push`, `pop`, `peek` and `is_empty`. Popping or peeking an empty stack should raise a clear error.

**Example I/O**

```
s = Stack(); s.push(1); s.push(2); s.push(3)
s.peek()   -> 3
s.pop()    -> 3
s.is_empty() -> False
```

<details><summary>Solution</summary>

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)            # add to the top

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")   # underflow
        return self._items.pop()            # remove & return the top

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]              # look at top without removing

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

s = Stack()
s.push(1); s.push(2); s.push(3)
print(s.peek())       # 3
print(s.pop())        # 3
print(s.is_empty())   # False
```

**Explanation.** A stack is **LIFO**: the last item pushed is the first popped. Both ends of the operation happen at the **top**. Real uses include the call/return stack for procedures, undo functionality, and reversing a sequence. Trying to pop an empty stack is **stack underflow**; a fixed-size stack that is full would be **stack overflow**.

**Big O:** `push`, `pop`, `peek` and `is_empty` are all **O(1)** — they only ever touch the top. Space **O(n)** for *n* stored items. ✅

</details>

---

### Challenge 8 — Implement a Queue (with circular-queue note) ★★

**Task.** Implement a **Queue** (FIFO — First In, First Out) class with `enqueue`, `dequeue`, `peek` and `is_empty`. Then read the note and implement a fixed-size **circular queue**.

**Example I/O**

```
q = Queue(); q.enqueue('a'); q.enqueue('b'); q.enqueue('c')
q.dequeue() -> 'a'
q.peek()    -> 'b'
```

<details><summary>Solution</summary>

```python
class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)            # add to the rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)           # remove from the front

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

q = Queue()
q.enqueue('a'); q.enqueue('b'); q.enqueue('c')
print(q.dequeue())   # 'a'
print(q.peek())      # 'b'
```

**Note — linear vs circular queue.** In the simple list version above, `pop(0)` shifts every remaining element down one place, which is **O(n)** per dequeue. A naive *linear* queue using fixed front/rear pointers also wastes space: once the rear pointer reaches the end of the array, the slots freed at the front cannot be reused. A **circular queue** solves this by wrapping the rear pointer back to index 0 using **modulo arithmetic** (`(front + count) % capacity`), reusing freed slots so all operations are **O(1)**.

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0          # index of the front item
        self.count = 0          # number of items currently stored

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("queue full")
        rear = (self.front + self.count) % self.capacity   # wrap around
        self.data[rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue empty")
        item = self.data[self.front]
        self.front = (self.front + 1) % self.capacity      # wrap around
        self.count -= 1
        return item

cq = CircularQueue(3)
cq.enqueue(1); cq.enqueue(2); cq.enqueue(3)
print(cq.dequeue())   # 1
cq.enqueue(4)         # reuses the slot freed by dequeuing 1
print(cq.dequeue())   # 2
print(cq.dequeue())   # 3
print(cq.dequeue())   # 4
```

**Explanation.** A queue is **FIFO**: items leave in the order they arrived (printer spoolers, keyboard buffers, breadth-first traversal). The circular version stores `front` and a `count` (or a `rear` pointer) and uses **modulo** to wrap, keeping every operation constant time within a fixed-size array.

**Big O:** `enqueue`/`dequeue`/`peek` are **O(1)** for the circular queue. For the simple list queue, `dequeue` via `pop(0)` is **O(n)** (elements shift down). Space **O(n)** for both. ✅

</details>

---

### Challenge 9 — Singly linked list (add + traverse) ★★

**Task.** Implement a **singly linked list**: a `Node` (data + pointer to the next node) and a `LinkedList` with `add(data)` (append to the end) and `traverse()` (return all values in order as a list).

**Example I/O**

```
ll = LinkedList(); ll.add(10); ll.add(20); ll.add(30)
ll.traverse()  ->  [10, 20, 30]
```

<details><summary>Solution</summary>

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None          # pointer to the next node (None = end)

class LinkedList:
    def __init__(self):
        self.head = None          # pointer to the first node

    def add(self, data):
        new_node = Node(data)
        if self.head is None:     # empty list -> new node becomes head
            self.head = new_node
            return
        current = self.head
        while current.next is not None:   # walk to the last node
            current = current.next
        current.next = new_node           # link it on the end

    def traverse(self):
        result = []
        current = self.head
        while current is not None:        # follow next pointers to the end
            result.append(current.data)
            current = current.next
        return result

ll = LinkedList()
for x in [10, 20, 30]:
    ll.add(x)
print(ll.traverse())   # [10, 20, 30]
```

**Explanation.** A linked list stores each value in a **node** that also holds a **pointer** to the next node. The `head` points to the first node; the final node's pointer is `None` (a *null pointer*) to mark the end. Unlike an array, a linked list is **dynamic** — it grows as needed — and inserting/removing in the middle only re-points pointers rather than shifting elements. The trade-off is no direct indexing: you must traverse from the head.

**Big O:** `traverse` is **O(n)**. `add` (append) is **O(n)** here because we walk to the tail; keeping a `tail` pointer would make appends **O(1)**. Inserting at the **head** is **O(1)**. Space **O(n)**. ✅

</details>

---

### Challenge 10 — Binary search tree: insert + in-order traversal ★★★

**Task.** Implement a **binary search tree (BST)** with `insert(key)` and an `in_order()` traversal that returns the keys. (BST property: every key in a node's **left** subtree is smaller, every key in its **right** subtree is larger.)

**Example I/O**

```
bst = BST()
for k in [50, 30, 70, 20, 40, 60, 80]: bst.insert(k)
bst.in_order()  ->  [20, 30, 40, 50, 60, 70, 80]   # sorted!
```

<details><summary>Solution</summary>

```python
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:                  # found the empty spot -> place here
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)    # go left
        elif key > node.key:
            node.right = self._insert(node.right, key)  # go right
        # equal keys ignored (no duplicates)
        return node

    def in_order(self):                   # left, root, right -> ascending order
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.key)
            self._in_order(node.right, result)

bst = BST()
for k in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(k)
print(bst.in_order())   # [20, 30, 40, 50, 60, 70, 80]
```

**Explanation.** To **insert**, compare the new key with the current node and move left (smaller) or right (larger) until you reach an empty position. An **in-order traversal** (left → root → right) of a BST visits the keys in **ascending sorted order** — a neat and examinable property.

**Big O:** for a reasonably **balanced** tree, `insert` and search are **O(log n)** (one comparison per level, ~log n levels). In the **worst case** — keys inserted already sorted — the tree degenerates into a linked list and both become **O(n)**. `in_order` visits every node, so it is **O(n)**. Space **O(n)** for storage plus **O(h)** recursion stack, where *h* is the tree height. ✅

</details>

---

### Challenge 11 — Tree traversals: pre-, in- and post-order ★★★

**Task.** Add `pre_order()` and `post_order()` traversals to the BST from Challenge 10, alongside `in_order()`. Confirm each returns the keys in the expected order.

**Example I/O** (same tree as Challenge 10: 50, 30, 70, 20, 40, 60, 80)

```
pre_order()   ->  [50, 30, 20, 40, 70, 60, 80]   # root, left, right
in_order()    ->  [20, 30, 40, 50, 60, 70, 80]   # left, root, right
post_order()  ->  [20, 40, 30, 60, 80, 70, 50]   # left, right, root
```

<details><summary>Solution</summary>

```python
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    # pre-order: ROOT, left, right
    def pre_order(self):
        result = []
        self._pre_order(self.root, result)
        return result

    def _pre_order(self, node, result):
        if node is not None:
            result.append(node.key)
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)

    # in-order: left, ROOT, right
    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.key)
            self._in_order(node.right, result)

    # post-order: left, right, ROOT
    def post_order(self):
        result = []
        self._post_order(self.root, result)
        return result

    def _post_order(self, node, result):
        if node is not None:
            self._post_order(node.left, result)
            self._post_order(node.right, result)
            result.append(node.key)

bst = BST()
for k in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(k)
print(bst.pre_order())    # [50, 30, 20, 40, 70, 60, 80]
print(bst.in_order())     # [20, 30, 40, 50, 60, 70, 80]
print(bst.post_order())   # [20, 40, 30, 60, 80, 70, 50]
```

**Explanation.** The three depth-first traversals differ only in **when the root is visited** relative to its subtrees:

- **Pre-order** (root → left → right): used to **copy/serialise** a tree, or to output prefix (Polish) notation from an expression tree.
- **In-order** (left → root → right): outputs a BST in **ascending order**, or infix notation.
- **Post-order** (left → right → root): used to **delete/free** a tree safely (children before parent), or to output postfix (Reverse Polish) notation.

*Memory aid:* the prefix (pre / in / post) tells you where the **root** sits relative to its children.

**Big O:** every traversal is **O(n)** time — each of the *n* nodes is visited exactly once. Space **O(h)** for the recursion stack, where *h* is the tree height (O(log n) if balanced, O(n) if degenerate). ✅

</details>

---

## Section D — Stretch challenge

### Challenge 12 — Dijkstra's shortest path ★★★

**Task.** Given a small **weighted graph** stored as an **adjacency dictionary** `{node: {neighbour: weight, ...}}`, write `dijkstra(graph, start)` that returns the **shortest distance** from `start` to **every** node. Assume all edge weights are non-negative.

**Example I/O**

```
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}
dijkstra(graph, 'A')  ->  {'A': 0, 'B': 3, 'C': 1, 'D': 8}
```

(Check: A→C costs 1; A→C→B costs 1+2 = 3, beating the direct A→B = 4; A→C→B→D costs 1+2+5 = 8, beating A→C→D = 9.)

<details><summary>Solution</summary>

```python
import heapq   # binary min-heap, used as the priority queue

def dijkstra(graph, start):
    # Step 1: every node starts at "infinity" distance, except the start (0)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # priority queue of (distance_so_far, node); always pops the smallest
    pq = [(0, start)]

    while pq:
        current_dist, current = heapq.heappop(pq)

        # skip stale entries (we already found a shorter route to this node)
        if current_dist > distances[current]:
            continue

        # relax each neighbour: can we reach it faster via `current`?
        for neighbour, weight in graph[current].items():
            distance = current_dist + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))

    return distances

graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}
print(dijkstra(graph, 'A'))   # {'A': 0, 'B': 3, 'C': 1, 'D': 8}
```

**Explanation.** Dijkstra's algorithm finds shortest paths from one source by **always expanding the closest not-yet-finalised node first** (a greedy strategy). We keep a tentative `distances` table initialised to infinity, and a **priority queue** (min-heap) ordered by distance. We repeatedly pop the nearest node and **relax** its edges — if going through that node gives a neighbour a shorter distance, we update it and push the new distance. Because all weights are non-negative, once a node is popped with its minimum distance, that distance is final. (It does **not** work with negative edge weights.)

**Big O:** with a binary-heap priority queue, **O((V + E) log V)**, where V = number of vertices and E = number of edges — each edge can trigger a heap push (O(log V)) and each vertex is popped once. Space **O(V)** for the distances table and the queue. A simpler array-scan version (no heap) is **O(V²)**, which can be faster on small dense graphs. ✅

</details>

---

## Where next

- **Building a real project?** Move on to the **NEA programming project guide** — `../../nea-guide/` (analysis → design → development → testing → evaluation). The stacks, queues, linked lists and search/sort algorithms in this workbook are exactly the kind of "complex techniques" that earn marks in the Development section, so reuse them where they genuinely fit your solution.
- **Exam practice on these topics:** sit **Mock Paper 2 — Algorithms & Programming** (`../mock-papers/mock-paper-2-algorithms-and-programming.md`) and the broader **Mock Paper 1 — Computer Systems** (`../mock-papers/mock-paper-1-computer-systems.md`).
- **Recap the theory:** the **2.3 Algorithms** and **1.4 Data types/structures** knowledge organisers (`../knowledge-organisers/`) and the **2.3 algorithms flashcards** (`../flashcards/2.3-algorithms.csv`) reinforce the Big O complexities you have just coded.

*Tip: for the exam, memorise the Big O table (best/average/worst) for every algorithm in this workbook, and be ready to trace any of them by hand on a small dataset.*
