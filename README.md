# Part 3: File I/O, APIs, and Exception Handling

## Assignment Overview
A **Product Explorer & Error-Resilient Logger** that fetches real product data from a public API, processes it, saves results to files, and handles all failure scenarios gracefully — just like a production-grade application.

## Concepts Covered
1. **File I/O** — Writing with `'w'` mode, appending with `'a'` mode, reading and searching file contents
2. **API Integration** — GET and POST requests using the `requests` library, formatted output, filtering and sorting
3. **Exception Handling** — `try-except-finally` blocks for division errors, file errors, and network errors; input validation loops
4. **Logging** — Timestamped error entries to `error_log.txt`, intentional error triggers for ConnectionError and HTTP 404

## File Structure
```
├── part3_api_files.py    # Main Python script with all 4 tasks
├── python_notes.txt      # Generated text file (Task 1)
├── error_log.txt         # Error log file (Task 4)
└── README.md             # This file
```

## How to Run
```bash
pip install requests
python part3_api_files.py
```

## Requirements
- Python 3.6+
- `requests` library (`pip install requests`)
- Internet connection (for API calls to https://dummyjson.com)

## Execution Output

```
==================================================
  Task 1 — File Read & Write Basics
==================================================

--- Part A: Writing to file ---
File written successfully.
Lines appended.

--- Part B: Reading from file ---
1. Topic 1: Variables store data. Python is dynamically typed.
2. Topic 2: Lists are ordered and mutable.
3. Topic 3: Dictionaries store key-value pairs.
4. Topic 4: Loops automate repetitive tasks.
5. Topic 5: Exception handling prevents crashes.
6. Topic 6: Functions help organize reusable blocks of code.
7. Topic 7: File I/O allows reading and writing data to disk.

Total number of lines: 7

Enter a keyword to search for in the notes: loop

Lines containing 'loop':
  → Topic 4: Loops automate repetitive tasks.

==================================================
  Task 2 — API Integration
==================================================

--- Step 1: Fetch 20 Products ---
ID  | Title                           | Category       | Price    | Rating
----|--------------------------------|---------------|---------|-------
1   | Essence Mascara Lash Princess   | beauty         | $9.99    | 2.56
2   | Eyeshadow Palette with Mirror   | beauty         | $19.99   | 2.86
3   | Powder Canister                 | beauty         | $14.99   | 4.64
4   | Red Lipstick                    | beauty         | $12.99   | 4.36
5   | Red Nail Polish                 | beauty         | $8.99    | 4.32
6   | Calvin Klein CK One             | fragrances     | $49.99   | 4.37
7   | Chanel Coco Noir Eau De         | fragrances     | $129.99  | 4.26
8   | Dior J'adore                    | fragrances     | $89.99   | 3.8
9   | Dolce Shine Eau de              | fragrances     | $69.99   | 3.96
10  | Gucci Bloom Eau de              | fragrances     | $79.99   | 2.74
11  | Annibale Colombo Bed            | furniture      | $1899.99 | 4.77
12  | Annibale Colombo Sofa           | furniture      | $2499.99 | 3.92
13  | Bedside Table African Cherry    | furniture      | $299.99  | 2.87
14  | Knoll Saarinen Executive Confe  | furniture      | $499.99  | 4.88
15  | Wooden Bathroom Sink With Mirr  | furniture      | $799.99  | 3.59
16  | Apple                           | groceries      | $1.99    | 4.19
17  | Beef Steak                      | groceries      | $12.99   | 4.47
18  | Cat Food                        | groceries      | $8.99    | 3.13
19  | Chicken Meat                    | groceries      | $9.99    | 3.19
20  | Cooking Oil                     | groceries      | $4.99    | 4.8

--- Step 2: Filtered Products (Rating ≥ 4.5, sorted by price desc) ---
ID  | Title                           | Price    | Rating
----|--------------------------------|---------|-------
11  | Annibale Colombo Bed            | $1899.99 | 4.77
14  | Knoll Saarinen Executive Confe  | $499.99  | 4.88
3   | Powder Canister                 | $14.99   | 4.64
20  | Cooking Oil                     | $4.99    | 4.8

--- Step 3: Laptops Category ---
  - Apple MacBook Pro 14 Inch Space Grey — $1999.99
  - Asus Zenbook Pro Dual Screen Laptop — $1799.99
  - Huawei Matebook X Pro — $1399.99
  - Lenovo Yoga 920 — $1099.99
  - New DELL XPS 13 9300 Laptop — $1499.99

--- Step 4: POST Request (Add Custom Product) ---
Server response:
  id: 195
  title: My Custom Product
  price: 999
  description: A product I created via API
  category: electronics

==================================================
  Task 3 — Exception Handling
==================================================

--- Part A: Guarded Calculator ---
safe_divide(10, 2)      = 5.0
safe_divide(10, 0)      = Error: Cannot divide by zero
safe_divide("ten", 2)   = Error: Invalid input types

--- Part B: Guarded File Reader ---
Test 1: python_notes.txt
Successfully read 'python_notes.txt' (350 characters).
File operation attempt complete.

Test 2: ghost_file.txt
Error: File 'ghost_file.txt' not found.
File operation attempt complete.

--- Part C: Robust API Calls ---
All API calls in Task 2 already use try-except blocks handling:
  - requests.exceptions.ConnectionError
  - requests.exceptions.Timeout
  - General Exception as a catch-all

--- Part D: Input Validation Loop ---
Enter a product ID to look up (1–100), or 'quit' to exit: 1
  Title: Essence Mascara Lash Princess
  Price: $9.99
Enter a product ID to look up (1–100), or 'quit' to exit: quit
Exiting product lookup.

==================================================
  Task 4 — Logging to File
==================================================

--- Triggering ConnectionError (unreachable URL) ---
Caught ConnectionError as expected.

--- Triggering HTTP 404 (product ID 999) ---
HTTP 404 received as expected.

--- Full Contents of error_log.txt ---
[2026-03-31 15:42:54] ERROR in test_connection: ConnectionError — No connection could be made to unreachable host
[2026-03-31 15:42:55] ERROR in test_http_error: HTTPError — 404 Not Found for product ID 999

All tasks completed.
```

## Error Log Format
Each entry in `error_log.txt` follows this format:
```
[YYYY-MM-DD HH:MM:SS] ERROR in <function_name>: <ErrorType> — <message>
```