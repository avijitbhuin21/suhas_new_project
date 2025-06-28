from flask import Flask, render_template, request, jsonify
from static.data.page_handler import *

from pyngrok import ngrok
import psutil
import os
import time
from dotenv import load_dotenv
import json
import re

from static.data.page_handler import *
from static.data.page_editor import *
from static.data.db_handler import *
from static.data.blogs import *
from static.data.global_functions import *

from flask_ngrok import run_with_ngrok
load_dotenv()

app = Flask(__name__)

blogs_by_category=get_blogs_for_header(limit=3)

#--------------------------------------------------------------------------------#
#                              RENDERING ROUTES                                  #
#--------------------------------------------------------------------------------#

@app.route('/')
def index():
    
    return render_template('homepage.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/news_waiting_page')
def news_waiting_page():
    return render_template('news_waiting_page.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/news_page')
def news_page():
    return render_template('news_page.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/category_homepage')
def category_homepage():
    return render_template('category_homepage.html' ,blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/advertise_with_us')
def advertise_with_us():
    return render_template('advertise_with_us.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/career_page')
def career_page():
    return render_template('career_page.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/JD')
def JD():
    return render_template('JD.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')


#--------------------------------------------------------------------------------#
#                              CATAGORIES ROUTES                                 #
#--------------------------------------------------------------------------------#

@app.route('/business')
def business():
    return render_template('business.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/technology')
def technology():
    return render_template('technology.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/gcc')
def gcc():
    return render_template('gcc.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/sustainability')
def sustainability():
    return render_template('sustainability.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')

@app.route('/semiconductor')
def semiconductor():
    return render_template('semiconductor.html', blogs_by_category=get_blogs_for_header(limit=3),desktop_nav_links = f'''{generate_header_dropdowns_html(blogs_by_category)}''',mobile_nav_links = f'''{generate_mobile_accordion_html(blogs_by_category)}''')


#--------------------------------------------------------------------------------#
#                              ADMIN PAGE ROUTES                                 #
#--------------------------------------------------------------------------------#
@app.route('/admin_login')
def admin_login():
    return render_template('admin.html')

@app.route('/admin_auth', methods=['POST'])
def admin_auth():
    data = request.json
    email = sha256_hash(data.get('email')) if "@" in data.get('email',"a") else data.get('enc_email')
    password = sha256_hash(data.get('password')) if "@" in data.get('email','a') else data.get('enc_pwd')
    return admin_login_db_check(email, password)

#------------------------------ ADMIN PAGE BLOG ------------------------------#

@app.route('/admin_blogs')
def admin_blogs():
    return render_template('admin_blogs.html')

@app.route('/admin_blog_preview', methods=['POST'])
def admin_blog_preview():
    data = request.json
    blogs_by_category = get_blogs_for_header(limit=3)
    html_output = get_blog_html(demo_json_data=data)
    return jsonify({
        "status": "success",
        "message": "Blog preview generated successfully",
        "data": html_output
    })

@app.route('/admin_save_blog', methods=['POST'])
def admin_save_blog():
    data = request.json
    minimum_required_keys = ["mainImageUrl", "mainImageAlt", "blogTitle", "blogAuthor", "blogDate", "blogSummary", "dynamicSections", "blogCategory"]
    for key in minimum_required_keys:
        if not data.get(key):
            return jsonify({"status": "error", "message": f"{key} cannot be empty"}), 400
    
    verification_status = admin_login_db_check(email=data.get('enc_email', ''), password=data.get('enc_pwd', ''))
    if not verification_status['success']:
        return jsonify({"status": "error", "message": "Admin authentication failed"}), 403
    
    data['admin_name'] = verification_status['name']
    
    if data.get('reason','insert') == 'insert':
        result = save_blogs_to_db(data)
    else:
        result = update_blogs_to_db(data)

    if result.get('status') == 'error':
        return jsonify({"status": "error", "message": result.get('message')}), 400
    
    return jsonify({"status": "success", "message": "Blog saved successfully", "url": result.get('url', '')}), 200

@app.route('/blog/<blog_id>')
def display_blog(blog_id):
    blog_data = get_blog(blog_id=blog_id)
    if not blog_data:
        return render_template('404.html'), 404
    
    json_data = blog_data.get('json_data', {})
    html_template = get_blog_html(demo_json_data=json_data)
    
    if not html_template:
        return render_template('404.html'), 404
    
    return html_template

# ... (rest of app.py remains the same) ...
@app.route('/get_blog_list')
def get_blog_list():
    search_keyword = request.args.get('search_keyword')
    list_of_blogs = get_blogs_list_db(search_keyword=search_keyword)
    return jsonify({
        "status": "success",
        "blogs": list_of_blogs
    })

# ... (etc.)

if __name__ == "__main__":
    app.run(port=5000, debug=True)