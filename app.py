from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data
items = ['Item 1', 'Item 2', 'Item 3']

@app.route('/')
def index():
    return '''
    <h1>Flask Demo App</h1>
    <p>Welcome to this simple Flask application!</p>
    <a href="/items">View Items</a>
    <a href="/api/items">API - Get Items</a>
    '''

@app.route('/items')
def show_items():
    items_html = '<h2>Items</h2><ul>'
    for item in items:
        items_html += f'<li>{item}</li>'
    items_html += '</ul><a href="/">Back to home</a>'
    return items_html

@app.route('/api/items')
def api_items():
    return jsonify(items=items)

if __name__ == '__main__':
    app.run(debug=True)