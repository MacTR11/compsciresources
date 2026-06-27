# Master Glossary — Exam-Ready Definitions (OCR H446)

Precise definitions win AO1 marks and underpin everything else. Use this for **daily quick-fire retrieval**: cover the right column, read the term, say the definition aloud, then check. Definitions are written to match the language OCR mark schemes reward.

> Tip: don't just read it — test yourself. Recall, then check.

---

## Component 01 — Computer Systems

### 1.1 Processors, input/output, storage
| Term | Definition |
|------|-----------|
| **ALU** (Arithmetic Logic Unit) | Part of the CPU that performs arithmetic and logical operations. |
| **Control Unit (CU)** | Directs the operation of the processor; decodes instructions and coordinates components using control signals. |
| **Register** | A small, very fast storage location inside the CPU. |
| **PC** (Program Counter) | Holds the address of the next instruction to be fetched. |
| **MAR** (Memory Address Register) | Holds the address of the memory location to be read from or written to. |
| **MDR** (Memory Data Register) | Holds the data or instruction that has been fetched from / is to be written to memory. |
| **CIR** (Current Instruction Register) | Holds the instruction currently being decoded/executed. |
| **ACC** (Accumulator) | Stores the intermediate results of calculations in the ALU. |
| **Fetch–Decode–Execute cycle** | The continuous cycle by which the CPU retrieves, interprets and carries out instructions. |
| **Cache** | Small, fast memory close to the CPU that stores frequently/recently used data and instructions to reduce access time. |
| **Clock speed** | The number of FDE cycles a processor can perform per second (measured in Hz). |
| **Core** | An independent processing unit within a CPU capable of executing instructions. |
| **Pipelining** | Overlapping the fetch, decode and execute of multiple instructions to increase throughput. |
| **Von Neumann architecture** | An architecture where data and instructions share the same memory and bus. |
| **Harvard architecture** | An architecture with separate memory and buses for data and instructions. |
| **CISC** | Complex Instruction Set Computer — many, complex instructions. |
| **RISC** | Reduced Instruction Set Computer — fewer, simple instructions executed quickly. |
| **GPU** | Graphics Processing Unit — many cores optimised for parallel tasks (e.g. graphics, ML). |

### 1.2 Software & software development
| Term | Definition |
|------|-----------|
| **Operating system** | Software that manages hardware and software resources and provides services for programs. |
| **Virtual memory** | Using secondary storage as an extension of RAM when RAM is full. |
| **Paging** | Dividing memory into fixed-size blocks (pages) for memory management. |
| **Interrupt** | A signal to the processor requesting attention, causing the current task to pause. |
| **Scheduling** | The OS deciding which process gets CPU time and when. |
| **Compiler** | Translates the whole source program into machine code/object code in one go before execution. |
| **Interpreter** | Translates and executes source code one line/statement at a time. |
| **Assembler** | Translates assembly language into machine code. |
| **Lexical analysis** | First stage of compilation: source code is turned into tokens; whitespace/comments removed. |
| **Syntax analysis** | Tokens are checked against grammar rules; a parse/syntax tree is built; syntax errors detected. |
| **Linker** | Combines compiled modules and library code into one executable. |
| **Class** | A template/blueprint defining the attributes and methods of objects. |
| **Object** | An instance of a class. |
| **Encapsulation** | Bundling data and methods together and restricting direct access to an object's data. |
| **Inheritance** | A subclass acquiring the attributes and methods of a parent (super) class. |
| **Polymorphism** | The ability of objects of different classes to respond to the same method call in their own way. |

### 1.3 Exchanging data
| Term | Definition |
|------|-----------|
| **Lossless compression** | Reducing file size with no loss of data; the original can be perfectly reconstructed. |
| **Lossy compression** | Reducing file size by permanently removing some (less important) data. |
| **Run length encoding (RLE)** | Lossless compression that stores runs of repeated values as a value + count. |
| **Symmetric encryption** | The same key is used to encrypt and decrypt. |
| **Asymmetric encryption** | A public key encrypts and a separate private key decrypts (or vice versa). |
| **Hashing** | Applying a function to data to produce a fixed-size value; one-way and not reversible. |
| **Primary key** | An attribute (or set) that uniquely identifies each record in a table. |
| **Foreign key** | An attribute in one table that is the primary key in another, linking the tables. |
| **Normalisation** | Organising data in tables to reduce redundancy and avoid anomalies. |
| **Referential integrity** | Ensuring relationships between tables remain consistent (no orphaned foreign keys). |
| **ACID** | Atomicity, Consistency, Isolation, Durability — properties guaranteeing reliable transactions. |
| **Protocol** | A set of rules governing communication between devices. |
| **TCP/IP stack** | A layered model (application, transport, network/internet, link) for network communication. |
| **DNS** | Domain Name System — translates domain names into IP addresses. |
| **Packet switching** | Splitting data into packets routed independently across a network. |

### 1.4 Data, structures, Boolean
| Term | Definition |
|------|-----------|
| **Two's complement** | A method of representing signed integers where the most significant bit has a negative place value. |
| **Floating point** | Representing real numbers as a mantissa and an exponent. |
| **Normalisation (floating point)** | Adjusting mantissa/exponent to maximise precision (mantissa starts 0.1 or 1.0 in sign-magnitude form). |
| **Array** | An ordered, finite set of elements of the same data type accessed by index. |
| **Record** | A data structure grouping related fields of possibly different types. |
| **Tuple** | An ordered, immutable set of values. |
| **Linked list** | A dynamic structure of nodes where each node holds data and a pointer to the next node. |
| **Stack** | A LIFO (last-in, first-out) structure; push/pop at the top. |
| **Queue** | A FIFO (first-in, first-out) structure; enqueue at the rear, dequeue at the front. |
| **Binary search tree** | A tree where each left child < parent < each right child, enabling fast search. |
| **Hash table** | A structure mapping keys to values via a hash function for fast lookup. |
| **Logic gate** | A circuit implementing a Boolean operation (AND, OR, NOT, XOR, NAND, NOR). |
| **De Morgan's laws** | NOT(A AND B) = NOT A OR NOT B; NOT(A OR B) = NOT A AND NOT B. |
| **Half adder** | A logic circuit adding two bits, outputting sum and carry. |
| **Full adder** | Adds two bits plus a carry-in, outputting sum and carry-out. |
| **D-type flip-flop** | An edge-triggered circuit that stores one bit. |

### 1.5 Legal/moral/ethical
| Term | Definition |
|------|-----------|
| **Data Protection Act** | Legislation governing how organisations collect, store and use personal data. |
| **Computer Misuse Act 1990** | Legislation criminalising unauthorised access to and modification of computer material. |
| **Copyright, Designs and Patents Act 1988** | Protects creators' intellectual property from being copied/used without permission. |
| **RIPA 2000** | Regulates how public bodies carry out surveillance and interception of communications. |

---

## Component 02 — Algorithms & Programming

| Term | Definition |
|------|-----------|
| **Abstraction** | Removing/hiding unnecessary detail to focus on the essential features of a problem. |
| **Decomposition** | Breaking a problem into smaller, more manageable sub-problems. |
| **Caching** | Storing results/data likely to be needed again to save recomputation/retrieval time. |
| **Iteration** | Repeating a block of code (count-controlled or condition-controlled). |
| **Recursion** | A subroutine that calls itself, with a base case to stop and a general case. |
| **Base case** | The condition that stops recursion. |
| **Local variable** | A variable accessible only within the subroutine where it is declared. |
| **Global variable** | A variable accessible throughout the whole program. |
| **Procedure** | A subroutine that performs a task but does not return a value. |
| **Function** | A subroutine that returns a value. |
| **Pass by value** | A copy of the argument is passed; the original is unchanged. |
| **Pass by reference** | A reference to the argument is passed; the original can be changed. |
| **Divide and conquer** | Repeatedly breaking a problem into halves/sub-problems to solve it efficiently. |
| **Backtracking** | Building a solution incrementally and undoing steps that fail to satisfy constraints. |
| **Heuristic** | A "rule of thumb" approach giving a good-enough solution where an exact one is impractical. |
| **Big O notation** | A measure of how an algorithm's time/space requirement grows with input size n. |
| **Linear search** | Checking each element in turn; O(n). |
| **Binary search** | Repeatedly halving a *sorted* list; O(log n). |
| **Bubble sort** | Repeatedly swapping adjacent out-of-order elements; worst/average O(n²). |
| **Insertion sort** | Building a sorted section by inserting each element into place; worst/average O(n²). |
| **Merge sort** | Divide-and-conquer sort that splits, sorts and merges; O(n log n). |
| **Quick sort** | Divide-and-conquer sort using a pivot and partitioning; average O(n log n), worst O(n²). |
| **Dijkstra's algorithm** | Finds the shortest path from a start node to all others in a weighted graph. |
| **A\* algorithm** | Shortest-path search using actual cost + a heuristic estimate to the goal. |
| **Breadth-first traversal** | Visiting all neighbours level by level (uses a queue). |
| **Depth-first traversal** | Exploring as far as possible along each branch before backtracking (uses a stack). |

---

Drill these until they're automatic. Fast, accurate definitions free up thinking time for the AO2/AO3 marks that decide your grade.
