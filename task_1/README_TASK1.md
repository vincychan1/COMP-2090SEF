# OOP Supermarket Checkout System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-CLI%20Project-orange)

An object-oriented supermarket checkout simulation built with Python.  
This project supports product management, shopping cart operations, tiered discount checkout, console receipt printing, and JSON-based data persistence.

---

## Table of Contents

- [1. Highlights](#1-highlights)
- [2. Features](#2-features)
- [3. Discount Rules](#3-discount-rules)
- [4. Project Structure](#4-project-structure)
- [5. Requirements](#5-requirements)
- [6. Quick Start](#6-quick-start)
- [7. Data File Format](#7-data-file-format)
- [8. Typical User Flow](#8-typical-user-flow)
- [9. Current Scope & Improvement Ideas](#9-current-scope--improvement-ideas)
- [10. Use Cases](#10-use-cases)
- [11. Demo Output](#11-demo-output)

---

## 1. Highlights

- Clear OOP design with `Goods`, `ShoppingCart`, `Cashier`, and `SupermarketSystem`
- Interactive command-line menu (good for coursework demos)
- Persistent product data stored in JSON
- Full cart operations: add, update, remove, clear
- Tiered discount calculation with before/after totals
- Admin mode for product add/edit/delete

---

## 2. Features

### Customer Features

1. Browse products
2. Add products to cart by product ID
3. View cart (with discounted total)
4. Edit cart (remove item / change quantity)
5. View discount rules
6. Checkout and print receipt

### Admin Features

- Product management is protected by admin password (default: `admin123`)
- For a selected product ID, admin can:
  - Edit name and price
  - Delete product
  - Add a new product if ID does not exist

---

## 3. Discount Rules

- Spend 100+, save 20
- Spend 300+, save 50
- Spend 500+, save 100
- Spend 1000+, save 300

Only the highest matched tier is applied once (not cumulative).

---

## 4. Project Structure

Core files:

- `main.py`: Entry point, menu flow, product loading/saving
- `goods.py`: Product model (`id`, `name`, `price`)
- `cart.py`: Cart logic (add, update quantity, remove, total)
- `Cashier.py`: Checkout calculation and receipt printing
- `goods.json`: Product data source (default read/write target)

Other scripts (e.g., binary tree/heap sort practice files) are independent and do not affect checkout flow.

---

## 5. Requirements

- Python 3.8+
- No third-party dependencies (standard library only)

---

## 6. Quick Start

Run from the project root:

```bash
python main.py
```

Then follow the menu prompts in the terminal.

---

## 7. Data File Format

### Product data (`goods.json`)

```json
[
  {"id": "001", "name": "Apple", "price": 6.5},
  {"id": "002", "name": "Milk", "price": 12.0}
]
```

Fields:

- `id`: Product ID (string)
- `name`: Product name (string)
- `price`: Product price (number, > 0)

If loading fails or the file is empty, built-in default products are used.

---

## 8. Typical User Flow

1. Browse products
2. Enter product ID and quantity to add items
3. Review cart and discounted total
4. Edit cart if needed
5. Checkout and review receipt in console
6. Confirm payment (cart is cleared)
7. Exit and save product data

---

## 9. Current Scope & Improvement Ideas

### Already Implemented

- Console receipt output
- Product data persistence

### Suggested Improvements

- Save receipts to the `receipts/` folder (txt/json)
- Add stock/inventory fields and stock deduction logic
- Add membership features (member discounts, points)
- Add unit tests (`unittest` / `pytest`)
- Upgrade from CLI to Web or GUI interface

---

## 10. Use Cases

- Python OOP coursework project
- Practice for business logic modeling + persistence
- Command-line application training project

---

## 11. Demo Output

Example terminal interaction:

```text
=============================================
         Supermarket Main Menu
=============================================
 1. Browse Products    2. View Cart
 3. Edit Cart          4. Clear Cart
 5. View Discounts     6. Checkout
 7. Product Admin      8. Save and Exit
=============================================

Choose (1-8): 1

=============================================
ID      Name                Price
---------------------------------------------
001     Apple               $    6.50
002     Milk                $   12.00
003     Chocolate           $    8.00
004     Biscuit             $    7.50
005     Bread               $   10.00
=============================================

Add product to cart? (y/n): y
Product ID: 002
Quantity (integer): 3
Added to cart: Milk x 3

Choose (1-8): 6
---RECEIPT---
Milk      3         $12.00  $36.00
-----------------------------------
Subtotal: $36.00
Total: $36.00
```

---

If you want, I can also add:

- A Chinese-English bilingual README
- A short architecture section with class relationships
- An MIT `LICENSE` file + contribution guide
