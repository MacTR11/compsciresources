# Diagnostic — Week 1 (GCSE Bridging)

Name: ______________________   Date: __________   Mark: ______ / 40

*OCR H446 · Week 1 · 45 minutes · Closed book. This paper checks the GCSE foundations the A Level builds on — nothing beyond GCSE Computer Science is assumed. Show your working on every calculation.*

## Section A — Number bases and data (12 marks)

**1.** Convert the 8-bit binary number 10110101 to denary. **[1]**

**2.** Convert the denary number 156 to 8-bit binary. **[1]**

**3.** Convert the denary number 202 to hexadecimal. Show your working. **[2]**

**4.** Convert the hexadecimal number 4F to denary. **[1]**

**5.** Add the 8-bit binary numbers 11010110 and 01001011. Give your answer in binary, and state whether an overflow error occurs in an 8-bit register, giving a reason. **[3]**

**6.** The binary number 00011011 is shifted **two places to the left**. Write the result and state the effect the shift has on the value. **[2]**

**7.** An image is 100 pixels wide and 50 pixels high, with a colour depth of 8 bits. Calculate the file size of the image in **bytes**. Show your working. **[2]**

## Section B — Computational thinking and reading pseudocode (14 marks)

**8.** State what is meant by **decomposition** and what is meant by **abstraction**. **[2]**

**9.** The following program is run. **[4]**

```
total = 0
for i = 1 to 4
    total = total + i * i
next i
print(total)
```

Complete the trace table, adding one row for each time round the loop, and state the output.

| i | total | Output |
|---|-------|--------|
|   |       |        |
|   |       |        |
|   |       |        |
|   |       |        |

@@SPACE:0@@

**10.** The following program is run three times. **[3]**

```
mark = int(input("Enter the mark"))
if mark >= 70 then
    print("Distinction")
elseif mark >= 40 then
    print("Pass")
else
    print("Fail")
endif
```

Complete the table to show the output for each value entered.

| Value entered | Output |
|---------------|--------|
| 70 |  |
| 39 |  |
| 55 |  |

@@SPACE:0@@

**11.** The following program is meant to count down from 10 to 1, but it does not work. Identify the error and write the line of code that fixes it, stating where it goes. **[2]**

```
count = 10
while count > 0
    print(count)
endwhile
```

**12.** The following program is run.

```
values = [12, 5, 19, 8]
biggest = values[0]
for i = 1 to values.length - 1
    if values[i] > biggest then
        biggest = values[i]
    endif
next i
print(biggest)
```

(a) State the output of the program. **[1]**

(b) State the purpose of the algorithm. **[1]**

(c) State the change needed so that the program finds the **smallest** value instead. **[1]**

## Section C — Computer systems basics (14 marks)

**13.** State the purpose of the **CPU** and name **two** components found inside it. **[3]**

**14.** Give **two** differences between **RAM** and **ROM**. **[2]**

**15.** A student needs to carry their coursework files between school and home. State why a computer needs **secondary storage**, recommend a suitable storage device for the student, and justify your choice. **[3]**

**16.** State **two** functions of an **operating system**. **[2]**

**17.** The computers in a school are connected in a network. State **one** advantage and **one** disadvantage of connecting computers in a network. **[2]**

**18.** State what is meant by an **embedded system** and give **one** example. **[2]**

---

## Mark scheme

**Section A — Number bases and data (12 marks)**

**1. [1]** 181. (128 + 32 + 16 + 4 + 1.)

**2. [1]** 10011100. (128 + 16 + 8 + 4 = 156.)

**3. [2]** CA. 1 mark for a valid method (202 ÷ 16 = 12 remainder 10, or via binary 11001010 split as 1100 / 1010); 1 mark for the answer CA. Correct answer with no working: 2 marks.

**4. [1]** 79. (4 × 16 + 15.)

**5. [3]**
- Correct 8-bit sum with working: 11010110 + 01001011 = **00100001** with a carry out of the register (full result 100100001). **[2]** — award 1 mark if at most one bit is wrong but carries are shown.
- Overflow: **yes** — the true result (289) needs 9 bits, so the carry out of the most significant bit is lost in an 8-bit register. **[1]**

**6. [2]**
- Result: **01101100**. **[1]**
- Effect: the value is **multiplied by 4** (each place shifted left doubles it; 27 becomes 108). **[1]**

**7. [2]**
- 100 × 50 × 8 = 40,000 bits. **[1]**
- 40,000 ÷ 8 = **5,000 bytes**. **[1]** (Allow follow-through from an incorrect bit total divided correctly by 8.)

**Section A total: 12**

**Section B — Computational thinking and reading pseudocode (14 marks)**

**8. [2]**
- Decomposition: breaking a problem down into smaller sub-problems, each of which is easier to solve. **[1]**
- Abstraction: removing/hiding unnecessary detail so only the information relevant to the problem remains. **[1]**

**9. [4]** Completed trace table (1 mark per correct row, max 3) and the output (1 mark):

| i | total | Output |
|---|-------|--------|
| 1 | 1 |  |
| 2 | 5 |  |
| 3 | 14 |  |
| 4 | 30 | 30 |

- Output printed: **30**. Allow the output shown on the last row or stated separately.

**10. [3]** 1 mark per correct row:

| Value entered | Output |
|---------------|--------|
| 70 | Distinction |
| 39 | Fail |
| 55 | Pass |

**11. [2]**
- Error identified: `count` is never changed inside the loop, so the condition stays true and the loop never ends (infinite loop). **[1]**
- Fix: add `count = count - 1` inside the loop body (after the `print(count)` line, before `endwhile`). **[1]**

**12. [3]**
- (a) **19**. **[1]**
- (b) It finds (and outputs) the **largest value** in the array. **[1]**
- (c) Change the comparison `>` to `<` (i.e. `if values[i] < biggest then`); also accept renaming with the same logic change. **[1]**

**Section B total: 14**

**Section C — Computer systems basics (14 marks)**

**13. [3]**
- Purpose: the CPU fetches, decodes and executes instructions / carries out the processing of data. **[1]**
- Any two components, 1 mark each: ALU, control unit, cache, registers (accept a named register such as the program counter or accumulator), (internal) buses. **[2]**

**14. [2]** Any two differences, 1 mark each:
- RAM is volatile (loses contents when power is off); ROM is non-volatile.
- RAM can be read and written; ROM is read-only (in normal use).
- RAM holds the currently running programs/data; ROM holds the boot/start-up instructions (firmware).
- RAM is usually much larger than ROM.

**15. [3]**
- Need for secondary storage: main memory (RAM) is volatile, so programs and data must be stored somewhere non-volatile / permanently when the power is off. **[1]**
- Suitable device: USB flash drive (accept portable SSD, or cloud storage as an alternative means). **[1]**
- Justification matched to the choice: e.g. small and portable, no moving parts so robust in a school bag, large enough capacity for coursework, works on both computers. **[1]**

**16. [2]** Any two functions, 1 mark each: provides a user interface; manages memory; manages the CPU/processes (scheduling/multitasking); manages files; manages input/output devices (via drivers); manages security (user accounts/access rights); manages utilities/housekeeping.

**17. [2]**
- Advantage (1): e.g. share files/peripherals (printers), central backup, log on anywhere, shared internet connection, easier to update software centrally.
- Disadvantage (1): e.g. malware can spread across the network, dependence on the server (if it fails, work stops), cost of cabling/hardware/technicians, security risk of a single point of attack.

**18. [2]**
- Embedded system: a computer system built into a larger device to perform a **dedicated function**, with the software usually fixed in firmware. **[1]**
- Example (1): washing machine controller, microwave, traffic lights, engine management unit, smart thermostat, etc.

**Section C total: 14**

**Total: 12 + 14 + 14 = 40 marks.**
