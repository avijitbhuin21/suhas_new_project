from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/news_waiting_page')
def news_waiting_page():
    return render_template('news_waiting_page.html')

@app.route('/news_page')
def news_page():
    return render_template('news_page.html')

@app.route('/magazine_page')
def magazine_page():
    return render_template('magazine_page.html')

@app.route('/magazine_page_read_only')
def magazine_page_read_only():
    return render_template('magazine_page_read_only.html')

@app.route('/category_homepage')
def category_homepage():
    return render_template('category_homepage.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)