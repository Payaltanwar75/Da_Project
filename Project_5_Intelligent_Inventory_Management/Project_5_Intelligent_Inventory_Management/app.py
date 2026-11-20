from flask import Flask, render_template, request, jsonify
from database import init_db, get_products, add_product, delete_product
from algorithms import fractional_knapsack, zero_one_knapsack, benchmark_algorithms
app = Flask(__name__)

@app.route('/')
def index(): return render_template('index.html')

@app.get('/api/products')
def products(): return jsonify(get_products())

@app.post('/api/products')
def create_product():
    d=request.get_json(silent=True) or {}; name=str(d.get('name','')).strip()
    try: weight=float(d.get('weight')); profit=float(d.get('profit'))
    except (TypeError,ValueError): return jsonify(error='Weight and profit must be valid numbers.'),400
    if not name: return jsonify(error='Product name is required.'),400
    if weight<=0 or profit<0: return jsonify(error='Weight must be > 0 and profit cannot be negative.'),400
    return jsonify(id=add_product(name,weight,profit),message='Product added.'),201

@app.delete('/api/products/<int:pid>')
def remove_product(pid):
    delete_product(pid); return jsonify(message='Product deleted.')

@app.post('/api/optimize')
def optimize():
    d=request.get_json(silent=True) or {}
    try: capacity=float(d.get('capacity'))
    except (TypeError,ValueError): return jsonify(error='Enter a valid capacity.'),400
    if capacity<=0: return jsonify(error='Capacity must be greater than zero.'),400
    p=get_products()
    return jsonify(capacity=capacity, fractional=fractional_knapsack(p,capacity), zero_one=zero_one_knapsack(p,capacity), note='Fractional Knapsack may take part of an item; 0/1 Knapsack must take each item fully or leave it.')

@app.get('/api/benchmark')
def benchmark(): return jsonify(benchmark_algorithms())

if __name__=='__main__':
    init_db(); app.run(debug=True)
