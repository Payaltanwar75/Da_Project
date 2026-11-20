# Project 5: Intelligent Inventory Management Using Knapsack Optimization

## Problem statement
Select products to maximize total profit without exceeding storage capacity. Each product has a weight and profit.

## Algorithms
- **Greedy Fractional Knapsack:** sort by profit/weight ratio; products may be split. Time: `O(n log n)`.
- **Dynamic Programming 0/1 Knapsack:** each product is either fully selected or not selected. Time: `O(n × W)` where W is integer capacity.

## Features
Add/delete products, store inventory in SQLite, optimize against a capacity, compare both algorithm results, and benchmark execution time.

## Run in VS Code on Windows
1. Extract this ZIP and open the extracted project folder in VS Code.
2. Open Terminal → New Terminal.
3. Run `python -m pip install -r requirements.txt`
4. Run `python app.py`
5. Open `http://127.0.0.1:5000` in your browser.

Sample products are inserted automatically the first time: Laptop (weight 3, profit ₹60000), Monitor (5, ₹25000), Keyboard (1, ₹3000), Printer (4, ₹18000), Tablet (2, ₹22000).

**Note:** 0/1 DP rounds product weights to the nearest whole unit and capacity down to an integer. Fractional Knapsack uses decimal weights/capacity directly. Use whole-number weights for a straightforward classroom comparison. Benchmark times vary by computer.

## Structure
- `app.py` — Flask routes and API
- `algorithms.py` — Fractional and 0/1 Knapsack plus benchmark
- `database.py` — SQLite database operations
- `templates/index.html` — dashboard structure
- `static/style.css` — dashboard styling
- `static/script.js` — frontend interactions
- `requirements.txt` — dependency list
