# Programming Workbook 1 — Core Programming Skills

*OCR A Level Computer Science (H446) — Component 02 (2.2 Programming techniques) and NEA preparation*

## How to use this workbook

This workbook is a set of graded **practical coding challenges**. The single most effective way to prepare for **Paper 2 (Component 02)** and the **NEA (Component 03/04)** is to *write real code*. Reading solutions is not enough — your brain only builds the skill by struggling with the problem first.

For each challenge:

1. **Read the task and the example input/output.**
2. **Attempt it yourself** in a code editor (IDLE, VS Code, Thonny, repl.it — whatever you use). Run it. Test it with the example data *and* with your own awkward cases.
3. **Only then** expand the `Solution` box and compare. If your code differs but works, that is fine — there is rarely one correct answer.
4. If you got stuck, type the solution out yourself rather than copying-pasting. Then **change it** — extend it, break it, fix it.

Solutions are written in **Python 3**. You may use your own programming language (the OCR exam accepts any high-level language); the *techniques* are identical. Where it clarifies the logic, **OCR Reference Language (pseudocode)** is shown alongside.

**Difficulty tags:**
- ★ **Foundation** — core syntax you must be fluent in.
- ★★ **Developing** — combining techniques; typical exam-question level.
- ★★★ **Stretch** — harder logic, closer to NEA-style problem solving.

---

## Skill 1 — Sequence, Selection, Iteration

The three basic programming constructs. Everything else is built on these.

### Challenge 1.1 — Odd or Even ★

**Task:** Ask the user for a whole number and print whether it is `odd` or `even`.

**Example**

```
Enter a number: 7
7 is odd
```

<details><summary>Solution</summary>

```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
```

The modulo operator `%` gives the remainder after division; a remainder of 0 when dividing by 2 means the number is even.

</details>

### Challenge 1.2 — FizzBuzz ★★

**Task:** Print the numbers 1 to 20. For multiples of 3 print `Fizz`, for multiples of 5 print `Buzz`, and for multiples of both print `FizzBuzz`.

**Example (first lines)**

```
1
2
Fizz
4
Buzz
```

<details><summary>Solution</summary>

```python
for n in range(1, 21):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
```

Check the *combined* condition (`Fizz` **and** `Buzz`) first, otherwise multiples of 15 would only ever match the single conditions.

</details>

### Challenge 1.3 — Times Table Grid ★★★

**Task:** Print a 12 × 12 multiplication grid, neatly aligned in columns.

**Example (first rows)**

```
  1   2   3   4   5   6   7   8   9  10  11  12
  2   4   6   8  10  12  14  16  18  20  22  24
  3   6   9 ...
```

<details><summary>Solution</summary>

```python
for row in range(1, 13):
    line = ""
    for col in range(1, 13):
        product = row * col
        line = line + str(product).rjust(4)
    print(line)
```

A **nested loop**: the outer loop handles each row, the inner loop builds that row's columns. `rjust(4)` pads each number to 4 characters so the columns line up.

</details>

---

## Skill 2 — String Manipulation

Strings are sequences of characters. You should be fluent with indexing, slicing, length, case conversion and concatenation.

### Challenge 2.1 — Reverse a String ★

**Task:** Read a word and print it backwards.

**Example**

```
Enter a word: stressed
desserts
```

<details><summary>Solution</summary>

```python
word = input("Enter a word: ")
print(word[::-1])
```

The slice `[::-1]` steps through the string from end to start. A loop equivalent: build a new string by prepending each character.

</details>

### Challenge 2.2 — Count Vowels ★★

**Task:** Read a sentence and report how many vowels (a, e, i, o, u) it contains, ignoring case.

**Example**

```
Enter a sentence: Computer Science
6 vowels
```

<details><summary>Solution</summary>

```python
sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = 0
for char in sentence:
    if char in vowels:
        count = count + 1
print(count, "vowels")
```

Converting to lower case first means we only need to test five vowel characters, not ten.

</details>

### Challenge 2.3 — Caesar Cipher ★★★

**Task:** Encrypt a lower-case message by shifting each letter forward by a given key (wrapping z → a). Leave non-letters unchanged.

**Example**

```
Message: hello world
Shift: 3
khoor zruog
```

<details><summary>Solution</summary>

```python
message = input("Message: ")
shift = int(input("Shift: "))
result = ""
for char in message:
    if char.isalpha():
        # position 0-25 within the alphabet
        position = ord(char.lower()) - ord('a')
        new_position = (position + shift) % 26
        result = result + chr(new_position + ord('a'))
    else:
        result = result + char
print(result)
```

`ord()` gives a character's ASCII code and `chr()` reverses it. The `% 26` makes the shift wrap around the 26-letter alphabet.

</details>

---

## Skill 3 — Arrays / Lists and 2D Lists

In OCR pseudocode these are **arrays**; in Python they are **lists**. A 2D list is a list of lists — used for grids, tables and game boards.

### Challenge 3.1 — Sum and Average ★

**Task:** Given a list of numbers, print the total and the average.

**Example**

```
[4, 8, 15, 16, 23, 42]  ->  Total: 108  Average: 18.0
```

<details><summary>Solution</summary>

```python
numbers = [4, 8, 15, 16, 23, 42]
total = sum(numbers)
average = total / len(numbers)
print("Total:", total, " Average:", average)
```

`len()` gives the number of elements. Doing it by hand: a running `total` accumulated in a `for` loop, then divided by `len(numbers)`.

</details>

### Challenge 3.2 — Find the Maximum (without `max`) ★★

**Task:** Find the largest value in a list **without** using the built-in `max()` function.

**Example**

```
[3, 9, 1, 7, 9, 2]  ->  Largest: 9
```

<details><summary>Solution</summary>

```python
numbers = [3, 9, 1, 7, 9, 2]
largest = numbers[0]
for value in numbers:
    if value > largest:
        largest = value
print("Largest:", largest)
```

Assume the first element is the largest, then update whenever a bigger value is found. This linear-scan pattern is exactly how a max-finding algorithm works.

</details>

### Challenge 3.3 — 2D Grid Row Totals ★★★

**Task:** Given a 2D list (a table of numbers), print the total of each row.

**Example**

```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
Row 0 total: 6
Row 1 total: 15
Row 2 total: 24
```

<details><summary>Solution</summary>

```python
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

for index in range(len(grid)):
    row = grid[index]
    row_total = 0
    for value in row:
        row_total = row_total + value
    print("Row", index, "total:", row_total)
```

A 2D list is indexed `grid[row][column]`. The outer loop selects a row; the inner loop walks across that row's columns.

**OCR pseudocode**

```
for index = 0 to len(grid) - 1
    rowTotal = 0
    for col = 0 to len(grid[index]) - 1
        rowTotal = rowTotal + grid[index][col]
    next col
    print("Row " + str(index) + " total: " + str(rowTotal))
next index
```

</details>

---

## Skill 4 — Functions and Procedures

A **function** returns a value; a **procedure** performs an action but returns nothing. Both can take **parameters**. Using them well is essential for the NEA's *modular* design and decomposition marks.

### Challenge 4.1 — Area of a Rectangle ★

**Task:** Write a function `area(width, height)` that **returns** the area, then call it and print the result.

**Example**

```
area(5, 3)  ->  15
```

<details><summary>Solution</summary>

```python
def area(width, height):
    return width * height

print(area(5, 3))
```

`width` and `height` are **parameters**; `5` and `3` are the **arguments** passed in. `return` sends the result back to the caller.

</details>

### Challenge 4.2 — Procedure vs Function ★★

**Task:** Write a **procedure** `greet(name)` that *prints* a greeting (returns nothing), and a **function** `make_greeting(name)` that *returns* the greeting string. Show that only the function's result can be stored in a variable.

**Example**

```
greet("Sam")            prints: Hello, Sam!
make_greeting("Sam")    returns: "Hello, Sam!"
```

<details><summary>Solution</summary>

```python
def greet(name):           # procedure: side effect only
    print("Hello, " + name + "!")

def make_greeting(name):   # function: returns a value
    return "Hello, " + name + "!"

greet("Sam")                       # prints directly
message = make_greeting("Sam")     # value captured
print(message)
print(greet("Sam"))                # prints "None" — a procedure returns nothing
```

A procedure has no `return`, so in Python it implicitly returns `None`. Only a function's returned value is useful to store or reuse.

</details>

### Challenge 4.3 — Default and Multiple Return Values ★★★

**Task:** Write `divide(a, b)` that returns **both** the quotient and remainder. Give `b` a default value of 1. Handle the example below.

**Example**

```
divide(17, 5)  ->  quotient 3, remainder 2
divide(9)      ->  quotient 9, remainder 0   (b defaults to 1)
```

<details><summary>Solution</summary>

```python
def divide(a, b=1):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print("quotient", q, "remainder", r)

q, r = divide(9)
print("quotient", q, "remainder", r)
```

`b=1` is a **default parameter**, used when no second argument is given. Python returns the pair as a tuple, which we unpack into `q` and `r`.

</details>

---

## Skill 5 — Variable Scope

A **local** variable exists only inside the function where it is created. A **global** variable exists for the whole program. Scope is a favourite exam topic — read the next challenge carefully *before* running it.

### Challenge 5.1 — Predict the Output ★★

**Task:** *Without running it*, predict what this program prints. Then run it to check.

```python
total = 10

def add_five():
    total = 0          # this is a NEW local variable
    total = total + 5
    print("Inside:", total)

add_five()
print("Outside:", total)
```

<details><summary>Solution</summary>

```
Inside: 5
Outside: 10
```

The `total` inside `add_five` is a **separate local variable** that shadows the global one. Assigning to it does **not** change the global `total`, so `Outside` is still `10`. This is the trap: a function cannot accidentally overwrite a global just by sharing its name.

</details>

### Challenge 5.2 — Local Stays Local ★★

**Task:** Try to access a function's local variable from outside the function and observe what happens. Then fix the design by **returning** the value instead.

<details><summary>Solution</summary>

```python
def calculate():
    answer = 42        # local to calculate()
    return answer

# print(answer)        # would raise NameError: 'answer' is not defined

result = calculate()   # correct: capture the returned value
print(result)
```

A local variable is **destroyed when the function ends**. The right way to get data out of a function is to `return` it — never rely on reaching inside. (`global` exists but is poor practice; prefer parameters and return values for clean, testable NEA code.)

</details>

### Challenge 5.3 — Using `global` (and why to avoid it) ★★★

**Task:** Make a function that *does* modify a global counter using the `global` keyword, then rewrite it without `global` by passing and returning the value. Compare the two designs.

<details><summary>Solution</summary>

```python
# Version A — uses global (works, but harder to test/reuse)
counter = 0
def increment_global():
    global counter
    counter = counter + 1

increment_global()
print(counter)   # 1

# Version B — pure function, no global state
def increment(value):
    return value + 1

counter = increment(counter)   # 2
print(counter)
```

Version A reaches outside itself, which makes the function depend on hidden state and harder to test. Version B is **self-contained**: its output depends only on its input. Examiners and good NEA design favour Version B.

</details>

---

## Skill 6 — Pass by Value vs Pass by Reference

In Python, **immutable** objects (int, float, string, tuple, bool) behave like *pass by value* — the original is unaffected. **Mutable** objects (lists, dictionaries) behave like *pass by reference* — changes inside the function affect the original.

### Challenge 6.1 — Numbers Don't Change ★★

**Task:** Predict the output, then run it.

```python
def add_ten(x):
    x = x + 10
    print("Inside:", x)

number = 5
add_ten(number)
print("Outside:", number)
```

<details><summary>Solution</summary>

```
Inside: 15
Outside: 5
```

An `int` is **immutable**. Inside the function `x` is rebound to a new value, but the caller's `number` is untouched — this is *pass by value* behaviour.

</details>

### Challenge 6.2 — Lists Do Change ★★

**Task:** Predict the output, then run it.

```python
def append_item(my_list):
    my_list.append(99)
    print("Inside:", my_list)

data = [1, 2, 3]
append_item(data)
print("Outside:", data)
```

<details><summary>Solution</summary>

```
Inside: [1, 2, 3, 99]
Outside: [1, 2, 3, 99]
```

A list is **mutable**. The parameter `my_list` refers to the *same* list object as `data`, so `.append()` modifies the original — *pass by reference* behaviour.

</details>

### Challenge 6.3 — Protect the Original ★★★

**Task:** Write `doubled(values)` that returns a new list with every element doubled **without changing** the original list. Prove the original is unchanged.

**Example**

```
original [1, 2, 3]  ->  doubled returns [2, 4, 6], original still [1, 2, 3]
```

<details><summary>Solution</summary>

```python
def doubled(values):
    result = []                 # build a brand-new list
    for v in values:
        result.append(v * 2)
    return result

original = [1, 2, 3]
new_list = doubled(original)
print("Returned:", new_list)    # [2, 4, 6]
print("Original:", original)    # [1, 2, 3] — unchanged
```

Because we create a **new** list rather than mutating the parameter, the caller's list is safe. Making a copy (e.g. `values[:]`) before changing it is a common defensive technique.

</details>

---

## Skill 7 — Recursion

A **recursive** function calls itself, breaking a problem into a smaller version of itself. Every recursion needs a **base case** (when to stop) and a **general/recursive case**.

### Challenge 7.1 — Factorial ★★

**Task:** Write a recursive function `factorial(n)` where `factorial(n) = n × (n−1) × ... × 1`, and `factorial(0) = 1`.

**Example**

```
factorial(5)  ->  120
```

<details><summary>Solution</summary>

```python
def factorial(n):
    if n == 0:              # base case
        return 1
    else:                   # recursive case
        return n * factorial(n - 1)

print(factorial(5))   # 120
```

Each call multiplies `n` by the factorial of `n-1`, shrinking towards the base case `n == 0`, which stops the recursion.

</details>

### Challenge 7.2 — Sum of a List ★★

**Task:** Write a recursive function `list_sum(numbers)` that returns the total of a list.

**Example**

```
list_sum([2, 4, 6])  ->  12
```

<details><summary>Solution</summary>

```python
def list_sum(numbers):
    if len(numbers) == 0:           # base case: empty list sums to 0
        return 0
    else:
        return numbers[0] + list_sum(numbers[1:])

print(list_sum([2, 4, 6]))   # 12
```

The result is the first element plus the sum of *the rest* of the list. `numbers[1:]` is the list without its first element, getting shorter each call.

</details>

### Challenge 7.3 — Fibonacci ★★★

**Task:** Write a recursive `fibonacci(n)` where the sequence is 0, 1, 1, 2, 3, 5, 8, ... (`fib(0)=0`, `fib(1)=1`).

**Example**

```
fibonacci(7)  ->  13
```

<details><summary>Solution</summary>

```python
def fibonacci(n):
    if n == 0:               # base case
        return 0
    elif n == 1:             # base case
        return 1
    else:                    # recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))   # 13
```

Two base cases are needed because each term depends on the *two* before it. Note this naive version recalculates values many times — for large `n` an iterative loop is far more efficient, a useful point to discuss in exams.

</details>

---

## Skill 8 — Validation and Error Handling

Validation checks data is sensible *before* using it. Exception handling (`try`/`except`) catches errors at run time so the program does not crash — essential for robust NEA code.

### Challenge 8.1 — Range Check ★

**Task:** Keep asking for an exam mark until the user enters a whole number between 0 and 100 inclusive.

**Example**

```
Enter mark (0-100): 150
Out of range, try again.
Enter mark (0-100): 72
Accepted: 72
```

<details><summary>Solution</summary>

```python
mark = int(input("Enter mark (0-100): "))
while mark < 0 or mark > 100:
    print("Out of range, try again.")
    mark = int(input("Enter mark (0-100): "))
print("Accepted:", mark)
```

A **range check** with a `while` loop that repeats until the input falls inside the valid 0–100 boundary.

</details>

### Challenge 8.2 — Catch a Bad Number ★★

**Task:** Ask for a number. If the user types something that is not a number, catch the error and print a friendly message instead of crashing.

**Example**

```
Enter a number: hello
That was not a valid number.
```

<details><summary>Solution</summary>

```python
try:
    value = int(input("Enter a number: "))
    print("You entered", value)
except ValueError:
    print("That was not a valid number.")
```

`int("hello")` raises a `ValueError`. The `try` block attempts the conversion; if it fails, control jumps to the matching `except` block instead of stopping the program.

</details>

### Challenge 8.3 — Robust Integer Input ★★★

**Task:** Write a function `get_int(prompt)` that keeps asking until the user enters a valid whole number, handling non-numeric input gracefully, then returns it.

**Example**

```
Enter age: twelve
Please enter a whole number.
Enter age: 12
-> returns 12
```

<details><summary>Solution</summary>

```python
def get_int(prompt):
    while True:                      # loop until we return
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

age = get_int("Enter age: ")
print("Got:", age)
```

Combining a `while True` loop with `try`/`except` gives a reusable, crash-proof input routine — exactly the kind of helper function that earns robustness marks in the NEA.

</details>

---

## Skill 9 — File Handling

Reading from and writing to text files lets a program **persist** data between runs. Use `with open(...)` so the file is closed automatically.

### Challenge 9.1 — Write Then Read ★★

**Task:** Write three names to a text file `names.txt`, one per line, then read the file back and print each name.

**Example**

```
Wrote 3 names.
Alice
Bob
Carol
```

<details><summary>Solution</summary>

```python
names = ["Alice", "Bob", "Carol"]

# Writing ("w" overwrites any existing file)
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
print("Wrote", len(names), "names.")

# Reading back
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())   # strip() removes the trailing newline
```

Mode `"w"` opens for writing; `"r"` for reading. `with` guarantees the file is closed even if an error occurs. `strip()` removes the `\n` added on each line.

</details>

### Challenge 9.2 — Append and Count ★★★

**Task:** Add a new line to an existing log file using **append** mode (don't overwrite it), then report how many lines the file now contains.

**Example**

```
log.txt before: 2 lines
(adds "New entry")
log.txt now: 3 lines
```

<details><summary>Solution</summary>

```python
# Set up a starting file with two lines
with open("log.txt", "w") as file:
    file.write("First entry\n")
    file.write("Second entry\n")

# Append a new line (mode "a" keeps existing content)
with open("log.txt", "a") as file:
    file.write("New entry\n")

# Count the lines
with open("log.txt", "r") as file:
    lines = file.readlines()
print("log.txt now:", len(lines), "lines")
```

Mode `"a"` (append) writes to the **end** of the file without deleting what is already there. `readlines()` returns a list with one element per line, so its length is the line count.

</details>

---

## Skill 10 — Object-Oriented Programming

A **class** is a blueprint with **attributes** (data) and **methods** (behaviour). An **object** is one instance of a class. **Inheritance** lets a subclass reuse and extend a parent class.

### Challenge 10.1 — A Student Class ★★

**Task:** Define a class `Student` with attributes `name` and `mark`, and a method `has_passed()` that returns `True` if the mark is 40 or more. Create a student and test it.

**Example**

```
Student("Priya", 55).has_passed()  ->  True
Student("Tom", 30).has_passed()    ->  False
```

<details><summary>Solution</summary>

```python
class Student:
    def __init__(self, name, mark):
        self.name = name        # attributes set on the object
        self.mark = mark

    def has_passed(self):
        return self.mark >= 40

priya = Student("Priya", 55)
print(priya.name, priya.has_passed())   # Priya True

tom = Student("Tom", 30)
print(tom.name, tom.has_passed())       # Tom False
```

`__init__` is the **constructor**, run automatically when an object is created. `self` refers to the specific object, letting each one hold its own `name` and `mark`.

</details>

### Challenge 10.2 — Inheritance: A Subclass ★★★

**Task:** Create a subclass `ALevelStudent` that **inherits** from `Student` and adds a `subjects` attribute (a list) and a method `subject_count()`. Reuse the parent's `__init__` with `super()`.

**Example**

```
s = ALevelStudent("Maya", 68, ["CS", "Maths", "Physics"])
s.has_passed()     ->  True   (inherited from Student)
s.subject_count()  ->  3      (new method)
```

<details><summary>Solution</summary>

```python
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def has_passed(self):
        return self.mark >= 40

class ALevelStudent(Student):           # inherits from Student
    def __init__(self, name, mark, subjects):
        super().__init__(name, mark)    # reuse parent constructor
        self.subjects = subjects        # new attribute

    def subject_count(self):            # new method
        return len(self.subjects)

maya = ALevelStudent("Maya", 68, ["CS", "Maths", "Physics"])
print(maya.has_passed())      # True  — inherited
print(maya.subject_count())   # 3     — added by subclass
```

`ALevelStudent(Student)` declares inheritance. `super().__init__(...)` calls the parent's constructor so we don't repeat the `name`/`mark` setup, and `has_passed()` is inherited for free. This reuse is exactly what inheritance is for.

</details>

---

## Where next

You have now exercised the core programming techniques of OCR 2.2. To keep building toward Paper 2 and the NEA:

- **Algorithms Workbook** — searching, sorting, stacks/queues and computational thinking applied to problems. Practise turning a description into working, tested code.
- **NEA Guide** — analysis, design, iterative development and evaluation. Apply *all* of these skills (functions, validation, file handling, OOP) inside one substantial, well-decomposed project.

Keep coding regularly. Short, frequent practice — writing, running and *debugging* your own programs — is the best preparation for both the written exam and the NEA.
