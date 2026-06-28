# Reference & Formula Sheet — Numbers, Big O, Logic, SQL

The high-frequency facts you should be able to recall instantly. Print it, stick it up, quiz yourself on it.

---

## 🔢 Number & data representation (1.4.1)

### Place values
**Binary (8-bit, unsigned):** `128 64 32 16 8 4 2 1`
**Hex digits:** `0 1 2 3 4 5 6 7 8 9 A B C D E F` (A=10 … F=15)

### Conversions
- **Binary → Denary:** add the place values where there is a 1.
- **Denary → Binary:** subtract largest place values that fit, or repeatedly divide by 2 (remainders bottom-up).
- **Binary ↔ Hex:** group bits in **nibbles of 4**; each nibble = one hex digit. (e.g. `1101 0110` = `D6`).
- **Hex → Denary:** (first digit × 16) + second digit.

### Two's complement (signed)
- Leftmost bit = **negative** place value (8-bit: −128).
- **To negate:** invert all bits, then add 1.
- **Subtraction A − B:** compute A + (two's complement of B).
- Range of n bits (signed): **−2ⁿ⁻¹ to 2ⁿ⁻¹ − 1** (8-bit: −128 to +127).

### Shifts
- **Logical left shift by n:** ×2ⁿ (zeros in on the right) — may overflow.
- **Logical right shift by n:** ÷2ⁿ (zeros in on the left).
- **Arithmetic right shift:** preserves the sign bit (for signed numbers).

### Floating point
- Number = **mantissa × 2^exponent**; mantissa and exponent both in two's complement.
- **Normalised:** positive numbers start `0.1…`, negative numbers start `1.0…` (first two bits differ).
- **More mantissa bits →** greater **precision**; **more exponent bits →** greater **range** (trade-off).

### Character sets
- **ASCII:** 7-bit (128 chars), commonly stored in 8 bits.
- **Unicode:** supports far more characters (multiple languages/emoji); more bits per character.

### Storage units
`8 bits = 1 byte` · 1 KB = 1000 B · 1 MB = 1000 KB · 1 GB = 1000 MB · 1 TB = 1000 GB (decimal). (Binary: KiB/MiB = ×1024.)

---

## ⏱️ Big O complexity (2.3)

| Class | Name | Example |
|-------|------|---------|
| **O(1)** | Constant | Accessing an array element by index; stack push/pop |
| **O(log n)** | Logarithmic | Binary search |
| **O(n)** | Linear | Linear search; traversing a list |
| **O(n log n)** | Linearithmic | Merge sort; quick sort (average) |
| **O(n²)** | Polynomial (quadratic) | Bubble sort; insertion sort; nested loops |
| **O(2ⁿ)** | Exponential | Some brute-force/recursive combinatorial algorithms |

### Standard algorithm complexities

| Algorithm | Best | Average | Worst | Space | Needs sorted? |
|-----------|------|---------|-------|-------|---------------|
| Linear search | O(1) | O(n) | O(n) | O(1) | No |
| Binary search | O(1) | O(log n) | O(log n) | O(1) | **Yes** |
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | — |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | — |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | — |
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) | — |

> Rule of thumb: drop constants and lower-order terms — O(3n² + 5n) → **O(n²)**.

---

## 🔌 Boolean algebra (1.4.3)

### Gate symbols (truth, 2-input)
| A | B | AND | OR | NAND | NOR | XOR |
|---|---|-----|----|----|-----|-----|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

### Identities (· = AND, + = OR, ¬ = NOT)
- **AND:** A·0 = 0 · A·1 = A · A·A = A · A·¬A = 0
- **OR:** A+0 = A · A+1 = 1 · A+A = A · A+¬A = 1
- **Double negation:** ¬(¬A) = A
- **Commutation:** A·B = B·A ; A+B = B+A
- **Association:** (A·B)·C = A·(B·C)
- **Distribution:** A·(B+C) = A·B + A·C
- **De Morgan's:** ¬(A·B) = ¬A + ¬B ; ¬(A+B) = ¬A · ¬B
- **Absorption:** A + (A·B) = A ; A·(A+B) = A

### Adders
- **Half adder:** Sum = A XOR B; Carry = A AND B.
- **Full adder:** adds A, B and carry-in; outputs sum and carry-out (two half adders + OR).

---

## 🗄️ SQL quick reference (1.3.2)

```sql
SELECT column1, column2        -- choose fields ( * = all )
FROM   Table
WHERE  condition               -- filter rows
ORDER BY column ASC|DESC;       -- sort results

-- Joining tables
SELECT *
FROM   Orders
JOIN   Customers ON Orders.CustomerID = Customers.CustomerID;

INSERT INTO Table (col1, col2) VALUES (val1, val2);
UPDATE Table SET col1 = val WHERE condition;   -- WHERE is essential!
DELETE FROM Table WHERE condition;             -- WHERE is essential!
CREATE TABLE Table (ID INTEGER PRIMARY KEY, Name VARCHAR(30));
```
Common conditions: `=  <>  <  >  <=  >=  AND  OR  NOT  LIKE 'A%'  BETWEEN x AND y  IN (...)`

---

## 🌐 Networking quick reference (1.3.3)

**TCP/IP layers (top → bottom):** Application → Transport → Network/Internet → Link.

| Protocol | Use |
|----------|-----|
| HTTP / HTTPS | Web pages (HTTPS = encrypted) |
| FTP | File transfer |
| SMTP | Sending email |
| POP3 / IMAP | Retrieving email |
| TCP | Reliable, ordered delivery |
| IP | Addressing & routing packets |
| DNS | Domain name → IP address |

---

Recall these cold and you free up exam time and brainpower for the application marks that decide A vs A\*.
