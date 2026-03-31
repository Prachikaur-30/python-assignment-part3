# Part 3: File I/O, APIs, and Exception Handling
# This script covers all 4 tasks as specified in the assignment.

import requests
from datetime import datetime

# ==========================================
# Helper: Error Logger
# ==========================================
def log_error(function_name, error_type, message):
    """
    Writes a timestamped error entry to error_log.txt.
    Format: [YYYY-MM-DD HH:MM:SS] ERROR in <function>: <ErrorType> — <message>
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n"
    with open("error_log.txt", "a", encoding="utf-8") as f:
        f.write(entry)


# ==========================================
# Task 1 — File Read & Write Basics (6 marks)
# ==========================================
print("=" * 50)
print("  Task 1 — File Read & Write Basics")
print("=" * 50)

# --- Part A: Write ---
print("\n--- Part A: Writing to file ---")

# The 5 lines specified in the assignment
notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes.",
]

# Write the 5 lines using write mode ('w') with encoding="utf-8"
with open("python_notes.txt", "w", encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")
print("File written successfully.")

# Append 2 more lines using append mode ('a')
extra_lines = [
    "Topic 6: Functions help organize reusable blocks of code.",
    "Topic 7: File I/O allows reading and writing data to disk.",
]

with open("python_notes.txt", "a", encoding="utf-8") as f:
    for line in extra_lines:
        f.write(line + "\n")
print("Lines appended.")

# --- Part B: Read ---
print("\n--- Part B: Reading from file ---")

# Read and print each line numbered, stripping trailing newline
with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    print(f"{i}. {line.strip()}")

# Count and print total number of lines
print(f"\nTotal number of lines: {len(lines)}")

# Ask user for a keyword and search (case-insensitive)
keyword = input("\nEnter a keyword to search for in the notes: ").strip()
matches = [line.strip() for line in lines if keyword.lower() in line.lower()]

if matches:
    print(f"\nLines containing '{keyword}':")
    for m in matches:
        print(f"  → {m}")
else:
    print(f"No lines found containing '{keyword}'.")


# ==========================================
# Task 2 — API Integration (8 marks)
# ==========================================
print("\n" + "=" * 50)
print("  Task 2 — API Integration")
print("=" * 50)

# --- Step 1: Fetch and Display 20 Products ---
print("\n--- Step 1: Fetch 20 Products ---")

try:
    response = requests.get("https://dummyjson.com/products?limit=20", timeout=5)
    response.raise_for_status()
    data = response.json()
    products = data.get("products", [])

    # Print formatted table
    print(f"{'ID':<4}| {'Title':<32}| {'Category':<15}| {'Price':<9}| {'Rating'}")
    print("-" * 4 + "|" + "-" * 32 + "|" + "-" * 15 + "|" + "-" * 9 + "|" + "-" * 7)

    for p in products:
        pid = p.get("id", "")
        title = p.get("title", "Unknown")[:30]
        category = p.get("category", "N/A")[:13]
        price = p.get("price", 0)
        rating = p.get("rating", 0)
        print(f"{pid:<4}| {title:<32}| {category:<15}| ${price:<8.2f}| {rating}")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    log_error("fetch_products", "ConnectionError", "No internet connection")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
    log_error("fetch_products", "Timeout", "Server took too long to respond")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    log_error("fetch_products", type(e).__name__, str(e))


# --- Step 2: Filter (rating >= 4.5) and Sort by price descending ---
print("\n--- Step 2: Filtered Products (Rating ≥ 4.5, sorted by price desc) ---")

try:
    # Reuse previously fetched products if available
    filtered = [p for p in products if p.get("rating", 0) >= 4.5]
    filtered.sort(key=lambda p: p.get("price", 0), reverse=True)

    if filtered:
        print(f"{'ID':<4}| {'Title':<32}| {'Price':<9}| {'Rating'}")
        print("-" * 4 + "|" + "-" * 32 + "|" + "-" * 9 + "|" + "-" * 7)
        for p in filtered:
            title = p.get("title", "Unknown")[:30]
            print(f"{p['id']:<4}| {title:<32}| ${p['price']:<8.2f}| {p['rating']}")
    else:
        print("No products found with rating ≥ 4.5.")

except NameError:
    print("Could not filter — products were not fetched in Step 1.")
except Exception as e:
    print(f"Error during filtering: {e}")
    log_error("filter_products", type(e).__name__, str(e))


# --- Step 3: Search by Category (laptops) ---
print("\n--- Step 3: Laptops Category ---")

try:
    response = requests.get("https://dummyjson.com/products/category/laptops", timeout=5)
    response.raise_for_status()
    laptops_data = response.json()
    laptop_products = laptops_data.get("products", [])

    if laptop_products:
        for lp in laptop_products:
            print(f"  - {lp.get('title', 'Unknown')} — ${lp.get('price', 0):.2f}")
    else:
        print("No laptops found.")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    log_error("search_laptops", "ConnectionError", "No internet connection")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
    log_error("search_laptops", "Timeout", "Server took too long to respond")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    log_error("search_laptops", type(e).__name__, str(e))


# --- Step 4: POST Request (Simulated) ---
print("\n--- Step 4: POST Request (Add Custom Product) ---")

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

try:
    response = requests.post("https://dummyjson.com/products/add", json=new_product, timeout=5)
    response.raise_for_status()
    result = response.json()
    print("Server response:")
    for key, value in result.items():
        print(f"  {key}: {value}")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    log_error("post_product", "ConnectionError", "No internet connection")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
    log_error("post_product", "Timeout", "Server took too long to respond")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    log_error("post_product", type(e).__name__, str(e))


# ==========================================
# Task 3 — Exception Handling (7 marks)
# ==========================================
print("\n" + "=" * 50)
print("  Task 3 — Exception Handling")
print("=" * 50)

# --- Part A: Guarded Calculator ---
print("\n--- Part A: Guarded Calculator ---")

def safe_divide(a, b):
    """
    Returns a / b, handling ZeroDivisionError and TypeError.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

# Test cases
print(f"safe_divide(10, 2)      = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0)      = {safe_divide(10, 0)}")
print(f'safe_divide("ten", 2)   = {safe_divide("ten", 2)}')


# --- Part B: Guarded File Reader ---
print("\n--- Part B: Guarded File Reader ---")

def read_file_safe(filename):
    """
    Tries to read the given file. Handles FileNotFoundError.
    Uses a finally block to print completion message.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"Successfully read '{filename}' ({len(content)} characters).")
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    finally:
        print("File operation attempt complete.")

# Test with existing file
print("Test 1: python_notes.txt")
read_file_safe("python_notes.txt")
print()

# Test with non-existent file
print("Test 2: ghost_file.txt")
read_file_safe("ghost_file.txt")


# --- Part C: Robust API Calls ---
# (Already implemented in Task 2 — every API call is wrapped in try-except
#  handling ConnectionError, Timeout, and general Exception.)
print("\n--- Part C: Robust API Calls ---")
print("All API calls in Task 2 already use try-except blocks handling:")
print("  - requests.exceptions.ConnectionError")
print("  - requests.exceptions.Timeout")
print("  - General Exception as a catch-all")


# --- Part D: Input Validation Loop ---
print("\n--- Part D: Input Validation Loop ---")

while True:
    user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ").strip()
    
    if user_input.lower() == "quit":
        print("Exiting product lookup.")
        break
    
    # Validate that input is an integer in range 1-100
    try:
        product_id = int(user_input)
    except ValueError:
        print("Warning: Please enter a valid integer.")
        continue
    
    if product_id < 1 or product_id > 100:
        print("Warning: ID must be between 1 and 100.")
        continue
    
    # Make the API request
    try:
        response = requests.get(f"https://dummyjson.com/products/{product_id}", timeout=5)
        
        if response.status_code == 404:
            print("Product not found.")
            log_error("lookup_product", "HTTPError", f"404 Not Found for product ID {product_id}")
        elif response.status_code == 200:
            product = response.json()
            print(f"  Title: {product.get('title', 'Unknown')}")
            print(f"  Price: ${product.get('price', 0):.2f}")
        else:
            print(f"Unexpected status code: {response.status_code}")
            log_error("lookup_product", "HTTPError", f"{response.status_code} for product ID {product_id}")
            
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
        log_error("lookup_product", "ConnectionError", "No internet connection")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
        log_error("lookup_product", "Timeout", "Server took too long to respond")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        log_error("lookup_product", type(e).__name__, str(e))


# ==========================================
# Task 4 — Logging to File (4 marks)
# ==========================================
print("\n" + "=" * 50)
print("  Task 4 — Logging to File")
print("=" * 50)

# --- Intentionally trigger a ConnectionError ---
print("\n--- Triggering ConnectionError (unreachable URL) ---")
try:
    response = requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError as e:
    print("Caught ConnectionError as expected.")
    log_error("test_connection", "ConnectionError", "No connection could be made to unreachable host")
except requests.exceptions.Timeout as e:
    print("Caught Timeout as expected.")
    log_error("test_connection", "Timeout", "Request timed out for unreachable host")
except Exception as e:
    print(f"Caught unexpected error: {e}")
    log_error("test_connection", type(e).__name__, str(e))

# --- Intentionally trigger an HTTP 404 (not a Python exception) ---
print("\n--- Triggering HTTP 404 (product ID 999) ---")
try:
    response = requests.get("https://dummyjson.com/products/999", timeout=5)
    if response.status_code != 200:
        print(f"HTTP {response.status_code} received as expected.")
        log_error("test_http_error", "HTTPError", f"{response.status_code} Not Found for product ID 999")
    else:
        print(f"Unexpectedly got 200 OK.")
except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    log_error("test_http_error", "ConnectionError", "No internet connection")
except requests.exceptions.Timeout:
    print("Request timed out.")
    log_error("test_http_error", "Timeout", "Server took too long to respond")
except Exception as e:
    print(f"Unexpected error: {e}")
    log_error("test_http_error", type(e).__name__, str(e))

# --- Read and print the full error log ---
print("\n--- Full Contents of error_log.txt ---")
try:
    with open("error_log.txt", "r", encoding="utf-8") as f:
        log_contents = f.read()
    if log_contents.strip():
        print(log_contents)
    else:
        print("(Log file is empty — no errors were logged.)")
except FileNotFoundError:
    print("error_log.txt not found — no errors were logged.")

print("\nAll tasks completed.")