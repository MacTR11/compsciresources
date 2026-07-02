# OCR Exam Reference Language — Complete Guide (H446/02)

A practical, exam-focused cheat sheet for writing pseudocode that **scores marks** in OCR A Level Computer Science.

> **What is OCR Exam Reference Language?**
> It is the pseudocode style OCR publishes and uses in **Paper 2 (H446/02 — Algorithms and Programming)**. When a question says "write an algorithm / a program", you may answer in **either** OCR Exam Reference Language **or a recognised high-level programming language** (e.g. Python, Java, C#, VB.NET).
>
> **Key rule: be consistent.** Pick one and stay in it for the whole answer. Examiners mark the *logic*, not which language you chose, but mixing Python syntax into OCR pseudocode (or vice versa) looks like an error. You do **not** lose marks for minor syntax slips in pseudocode as long as your intent is clear — but clean, consistent syntax is faster to read and less likely to be misread.
>
> **Version note:** OCR has published more than one version of its reference language over the years (small differences exist, e.g. `print`/`input` casing, `==` vs `=` in some early specimens, string method names). Always check the **reference language sheet provided with the paper / specimen** you are using, and copy its exact conventions. This guide follows OCR's current documented style.

---

## 1. Variables, constants and assignment

Assignment uses a single equals sign `=`. Variables do not need declaring before use.

```
name = "Macauley"
age = 17
pi = 3.14159
isLoggedIn = True
```

**Constants** use the `const` keyword and are conventionally written in UPPERCASE:

```
const VAT = 0.20
const PI = 3.14159
```

### Data types
OCR pseudocode is loosely typed (you rarely declare types), but you should know the underlying types:

| Type | Example values |
|------|----------------|
| `integer` | `7`, `-42`, `0` |
| `real` / `float` | `3.14`, `-0.5` |
| `string` | `"hello"` (double quotes) |
| `boolean` | `True`, `False` |
| `char` | `"A"` (a single character) |

### Casting (type conversion)
Convert between types with these functions:

```
str(12)        // → "12"        number to string
int("12")      // → 12          string/real to integer (truncates)
float("3.5")   // → 3.5         string to real
bool("True")   // → True        to boolean
ASC("A")       // → 65          character to ASCII code
CHR(65)        // → "A"         ASCII code to character
```

```
age = int(input("Enter your age: "))   // input is a string, so cast it
message = "You are " + str(age)        // cast number back to string to concatenate
```

---

## 2. Input and output

```
print("Hello world")
name = input("Enter your name: ")
```

- `print()` displays output to the screen.
- `input()` reads a value typed by the user. The prompt text in the brackets is optional but good practice. **`input()` always returns a string** — cast it if you need a number.

---

## 3. Operators

### Arithmetic
| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | add | `3 + 4` | `7` |
| `-` | subtract | `10 - 3` | `7` |
| `*` | multiply | `3 * 4` | `12` |
| `/` | divide (real result) | `7 / 2` | `3.5` |
| `MOD` | modulus (remainder) | `7 MOD 2` | `1` |
| `DIV` | integer (whole) division | `7 DIV 2` | `3` |
| `^` | exponent (to the power of) | `2 ^ 3` | `8` |

### Comparison
| Operator | Meaning |
|----------|---------|
| `==` | equal to |
| `!=` | not equal to |
| `<` | less than |
| `<=` | less than or equal to |
| `>` | greater than |
| `>=` | greater than or equal to |

> Note the **double** `==` for comparison vs the **single** `=` for assignment. (Some older OCR specimens used a single `=` for comparison — match the sheet on your paper, but `==` is the current style.)

### Boolean
| Operator | Example |
|----------|---------|
| `AND` | `if age > 12 AND age < 20 then` |
| `OR` | `if day == "Sat" OR day == "Sun" then` |
| `NOT` | `if NOT found then` |

---

## 4. Selection

### if / elseif / else / endif

```
if score >= 70 then
    print("Distinction")
elseif score >= 50 then
    print("Merit")
elseif score >= 40 then
    print("Pass")
else
    print("Fail")
endif
```

- The branch keyword is `then`.
- Use `elseif` (one word) for additional conditions.
- Every `if` block closes with `endif`.

### switch / case

```
switch grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Okay")
    default:
        print("Try harder")
endswitch
```

- Use `switch` when comparing **one variable** against several fixed values.
- `default:` is the catch-all (like `else`). Close with `endswitch`.

---

## 5. Iteration (loops)

### Count-controlled: for ... next

```
for i = 0 to 9
    print(i)
next i
```

This prints `0` to `9` (the range is **inclusive** of both ends).

With a **step** (count up or down by a fixed amount):

```
for i = 10 to 0 step -1
    print(i)
next i
```

```
for i = 0 to 20 step 2
    print(i)        // prints even numbers 0, 2, 4 ... 20
next i
```

### Condition-controlled (pre-check): while ... endwhile

Tests the condition **before** each iteration — may run zero times.

```
total = 0
number = 1
while number <= 10
    total = total + number
    number = number + 1
endwhile
print(total)        // 55
```

### Condition-controlled (post-check): do ... until

Tests the condition **after** each iteration — always runs **at least once**.

```
do
    answer = input("Enter password: ")
until answer == "letmein"
```

---

## 6. String handling

Strings support these properties and methods (note: methods use a **dot** after the variable; `.length` has no brackets):

```
text = "Computer"

text.length              // → 8          number of characters
text.upper               // → "COMPUTER"
text.lower               // → "computer"
text.substring(2, 3)     // → "mpu"       start index 2, take 3 characters
text.left(4)             // → "Comp"      leftmost 4 characters
text.right(3)            // → "ter"       rightmost 3 characters
```

> **Indexing starts at 0.** In `substring(start, number)`, `start` is the index of the first character and `number` is how many characters to take.

### Indexing a single character
```
text[0]                  // → "C"
```

### Concatenation
Join strings with `+`:

```
firstName = "Ada"
lastName = "Lovelace"
fullName = firstName + " " + lastName    // "Ada Lovelace"
```

> If string method names differ on your paper's reference sheet (e.g. `.subString` casing), use the sheet's version.

---

## 7. Arrays

Arrays are **zero-indexed** and declared with `array`.

### 1D array
```
array names[5]                       // 5 elements, indices 0–4
names[0] = "Sam"
names[1] = "Jo"
print(names[0])                      // "Sam"
```

You can also declare with values directly:

```
array scores = [10, 25, 30, 15]
print(scores[2])                     // 30
```

### Iterating a 1D array
```
array scores = [10, 25, 30, 15]
for i = 0 to scores.length - 1
    print(scores[i])
next i
```

### 2D array
Think of it as rows and columns: `board[row, column]`.

```
array board[3, 3]                    // 3 rows × 3 columns
board[0, 0] = "X"
board[1, 2] = "O"
print(board[1, 2])                   // "O"
```

### Iterating a 2D array (nested loops)
```
for row = 0 to 2
    for col = 0 to 2
        print(board[row, col])
    next col
next row
```

---

## 8. Subroutines

### Procedure (does something, returns nothing)

```
procedure greet(name)
    print("Hello " + name)
endprocedure
```

Call it with:
```
greet("Macauley")
```

### Function (returns a value)

```
function square(number)
    return number * number
endfunction
```

Call it and use the returned value:
```
result = square(5)       // result = 25
print(square(9))         // 81
```

- **Parameters** go in the brackets and are passed when calling.
- A `function` **must** use `return`; a `procedure` does not return a value.
- Choose a `function` when you need an answer back; a `procedure` for an action.

---

## 9. File handling

```
myFile = open("data.txt")           // open a file
myFile = openRead("data.txt")       // open for reading
myFile = openWrite("data.txt")      // open for writing
```

### Reading
```
myFile = openRead("data.txt")
while NOT myFile.endOfFile()
    line = myFile.readLine()
    print(line)
endwhile
myFile.close()
```

### Writing
```
myFile = openWrite("data.txt")
myFile.writeLine("First line")
myFile.writeLine("Second line")
myFile.close()
```

| Method | Purpose |
|--------|---------|
| `.readLine()` | read the next line from the file |
| `.writeLine(text)` | write a line to the file |
| `.endOfFile()` | returns `True` when the end is reached |
| `.close()` | close the file (**always do this**) |

---

## 10. Random numbers

```
diceRoll = random(1, 6)              // random integer between 1 and 6 inclusive
```

`random(a, b)` returns a random integer from `a` to `b` (both ends included).

---

## 11. Object-Oriented Programming (OCR reference style)

OCR's object-oriented pseudocode uses `class`, `public`/`private` access modifiers, a `new` constructor, attributes and methods.

### Defining a class
```
class Animal
    private name
    private sound

    public procedure new(givenName, givenSound)
        name = givenName
        sound = givenSound
    endprocedure

    public procedure speak()
        print(name + " says " + sound)
    endprocedure

    public function getName()
        return name
    endfunction
endclass
```

- `private` attributes are accessible only inside the class (encapsulation).
- `public` methods can be called from outside.
- The **constructor** is the method named `new`, called automatically when an object is created.

### Creating and using an object
```
myPet = new Animal("Rex", "Woof")
myPet.speak()                        // Rex says Woof
print(myPet.getName())               // Rex
```

> Note: an object is created with `new ClassName(arguments)`.

### Inheritance (`inherits`)
A subclass `inherits` from a superclass, gaining its attributes and methods. `super` calls the parent constructor.

```
class Dog inherits Animal
    private breed

    public procedure new(givenName, givenBreed)
        super.new(givenName, "Woof")
        breed = givenBreed
    endprocedure

    public procedure fetch()
        print(getName() + " fetches the ball")
    endprocedure
endclass
```

```
myDog = new Dog("Bella", "Labrador")
myDog.speak()                        // Bella says Woof   (inherited)
myDog.fetch()                        // Bella fetches the ball
```

---

## 12. Common syntax mistakes that lose (or cost) marks

- **Mixing languages.** Don't drop Python's `print(x)` colons and indentation rules into OCR pseudocode that uses `endif`/`next`. Pick one style and keep it.
- **Using `=` for comparison.** Use `==` to compare, `=` to assign. (`if x = 5` should be `if x == 5`.)
- **Forgetting the closing keyword.** Every block closes: `endif`, `endwhile`, `next`, `endprocedure`, `endfunction`, `endswitch`, `endclass`. Missing these makes logic ambiguous.
- **Forgetting `then` after an `if` condition.**
- **Off-by-one in arrays.** Arrays start at index **0**, so the last index is `length - 1`. Looping `for i = 0 to array.length` goes one too far.
- **Not casting `input()`.** `input()` returns a **string**. `age = input(...)` then `age + 1` will not work — use `age = int(input(...))`.
- **Confusing `/`, `DIV` and `MOD`.** `7 / 2 = 3.5`, `7 DIV 2 = 3` (whole part), `7 MOD 2 = 1` (remainder).
- **`function` without `return`** (or a `procedure` that tries to `return` a value). A function must return; a procedure should not.
- **`substring` arguments.** It is `substring(startIndex, numberOfChars)` — not start and end positions.
- **Single quotes for strings.** OCR uses **double quotes** `"like this"`.
- **Calling a method on a value without the dot**, e.g. `length(text)` instead of `text.length`.
- **Not closing files** with `.close()`.

---

## 13. Worked example programs (complete)

### A. Linear search
Searches an array for a target and returns its index (or -1 if not found).

```
function linearSearch(items, target)
    for i = 0 to items.length - 1
        if items[i] == target then
            return i
        endif
    next i
    return -1
endfunction

array numbers = [4, 8, 15, 16, 23, 42]
position = linearSearch(numbers, 16)
print(position)              // 3
```
*Explanation:* check each element in turn; return the index the moment a match is found, otherwise return -1 after the loop.

### B. Find the maximum value in an array

```
function findMax(items)
    max = items[0]
    for i = 1 to items.length - 1
        if items[i] > max then
            max = items[i]
        endif
    next i
    return max
endfunction

array scores = [12, 45, 7, 89, 33]
print(findMax(scores))      // 89
```
*Explanation:* assume the first element is the biggest, then compare every other element, updating `max` whenever a larger one is found.

### C. A class with a method (BankAccount)

```
class BankAccount
    private balance

    public procedure new(openingBalance)
        balance = openingBalance
    endprocedure

    public procedure deposit(amount)
        balance = balance + amount
    endprocedure

    public function getBalance()
        return balance
    endfunction
endclass

myAccount = new BankAccount(100)
myAccount.deposit(50)
print(myAccount.getBalance())   // 150
```
*Explanation:* `balance` is private (encapsulated); the only way to change or read it is through the public methods. The constructor `new` sets the opening balance.

### D. Recursive factorial

```
function factorial(n)
    if n == 0 then
        return 1
    else
        return n * factorial(n - 1)
    endif
endfunction

print(factorial(5))         // 120
```
*Explanation:* the **base case** `n == 0` returns 1 and stops the recursion; otherwise the function calls itself with a smaller value (`n - 1`), so `5! = 5 × 4 × 3 × 2 × 1 = 120`.

---

## 14. Quick "translate this concept" reference table

| Concept | OCR keyword / syntax |
|---------|----------------------|
| Assign a value | `x = 5` |
| Constant | `const NAME = value` |
| Output | `print(...)` |
| Input | `input(...)` |
| Number → string | `str(...)` |
| String → integer | `int(...)` |
| String → real | `float(...)` |
| Character ↔ ASCII | `ASC(...)` / `CHR(...)` |
| Equal / not equal | `==` / `!=` |
| Integer division / remainder | `DIV` / `MOD` |
| Power | `^` |
| Boolean operators | `AND` / `OR` / `NOT` |
| If statement | `if ... then ... elseif ... else ... endif` |
| Multi-way selection | `switch ... case ... default ... endswitch` |
| Count loop | `for i = a to b [step n] ... next i` |
| Pre-check loop | `while ... endwhile` |
| Post-check loop | `do ... until ...` |
| String length | `text.length` |
| Substring | `text.substring(start, number)` |
| Upper / lower case | `text.upper` / `text.lower` |
| Left / right of string | `text.left(n)` / `text.right(n)` |
| Concatenate | `+` |
| 1D array | `array a[n]` , `a[i]` |
| 2D array | `array a[r, c]` , `a[row, col]` |
| Procedure | `procedure name(params) ... endprocedure` |
| Function | `function name(params) ... return v ... endfunction` |
| Call subroutine | `name(args)` |
| Open file | `open / openRead / openWrite("file")` |
| Read / write line | `.readLine()` / `.writeLine(text)` |
| End of file | `.endOfFile()` |
| Close file | `.close()` |
| Random integer | `random(a, b)` |
| Class | `class Name ... endclass` |
| Access modifiers | `public` / `private` |
| Constructor | `procedure new(params)` |
| Create object | `obj = new Class(args)` |
| Call method | `obj.method(args)` |
| Inheritance | `class Child inherits Parent` |

---

*Final reminder: in the exam, write neatly, be consistent, close every block, and check the reference language sheet supplied with your paper for any small version differences.*
