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

#--------------------------------------------------------------------------------#
#                              RENDERING ROUTES                                  #
#--------------------------------------------------------------------------------#

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/news_waiting_page')
def news_waiting_page():
    return render_template('news_waiting_page.html')

@app.route('/news_page')
def news_page():
    return render_template('news_page.html')

@app.route('/category_homepage')
def category_homepage():
    return render_template('category_homepage.html')

@app.route('/advertise_with_us')
def advertise_with_us():
    return render_template('advertise_with_us.html')

@app.route('/career_page')
def career_page():
    return render_template('career_page.html')

@app.route('/JD')
def JD():
    return render_template('JD.html')

#--------------------------------------------------------------------------------#
#                              ADMIN PAGE ROUTES                                 #
#--------------------------------------------------------------------------------#
@app.route('/admin_login')
def admin_login():
    return render_template('admin.html')

@app.route('/admin_auth', methods=['POST'])
def admin_auth():
    data = request.json
    print(f"Received data for admin_auth: {json.dumps(data, indent=2, ensure_ascii=False)}")

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
    print(f"Received data for admin_blog_preview: {json.dumps(data, indent=2, ensure_ascii=False)}")

    data = get_blog_html(data)
               
    return jsonify({
        "status": "success",
        "message": "Blog added/edited successfully",
        "data": data
    })

@app.route('/admin_save_blog', methods=['POST'])
def admin_save_blog():
    data = request.json
    print(f"Received data for admin_save_blog: {json.dumps(data, indent=2, ensure_ascii=False)}")

    minimum_required_keys = [
        "mainImageUrl", "mainImageAlt", "blogTitle", "blogAuthor",
        "blogDate", "blogSummary", "dynamicSections", "blogCategory"  # "blogSubCategory" commented out
    ]

    error_identifiers = {
        "mainImageUrl": "Main Image URL",
        "mainImageAlt": "Main Image Alt Text",
        "blogTitle": "Blog Title",
        "blogAuthor": "Blog Author",
        "blogDate": "Blog Date",
        "blogSummary": "Blog Summary",
        "dynamicSections": "Dynamic Sections",
        "blogCategory": "Category"
        # "blogSubCategory": "Sub-Category"  # commented out
    }

    # Optional fields that will be stored if provided
    optional_fields = [
        "seoTitle", "seoMetaDescription", "seoCanonicalUrl"  # "blogSubCategory" moved here if needed
    ]

    for i in minimum_required_keys:
        if isinstance(data.get(i), str):
            if data[i].strip() == "":
                return jsonify({"status": "error", "message": f"{error_identifiers[i]} cannot be empty"}), 400
        elif isinstance(data.get(i), list):
            if data[i] == []:
                return jsonify({"status": "error", "message": f"{error_identifiers[i]} cannot be empty"}), 400
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

    print(f"Result from save_blogs_to_db: {result}")
    
    if result:
        return jsonify({"status": "success", "message": "Blog saved successfully", "url": result.get('url', '')}), 200
    else:
        return jsonify({"status": "error", "message": "Failed to save blog"}), 500

@app.route('/blog/<blog_id>')
def display_blog(blog_id):
    blog_data = get_blog(blog_id=blog_id)
    
    if not blog_data:
        return render_template('404.html'), 404
    json_data = blog_data.get('json_data', {})
    html_template = get_blog_html(json_data)
    if not html_template:
        return render_template('404.html'), 404
        
    
    html_template = re.sub(
        r'(src|href)="static/',
        r'\1="/static/',
        html_template
    )
    
    return html_template













@app.route('/admin_get_card_structure')
def admin_get_card_structure():
    return get_homepage_data()

@app.route('/admin_update_homepage', methods=['POST'])
def admin_update_homepage():
    try:
        # Get JSON data from request
        data = request.json
        print(f"Received homepage update data: {data}")
        
        if not data:
            return jsonify({"status": "error", "message": "No data received"}), 400
        
        # Log to help debug any parameter matching issues
        print(f"Passing {len(data)} parameters to update_homepage function")
        
        # Call update_homepage function with the data
        result = update_homepage(**data)
        print(f"Update homepage result: {result}")
        
        return jsonify({"status": "success", "message": result})
    
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        print(f"Error updating homepage: {str(e)}")
        print(f"Traceback: {error_traceback}")
        return jsonify({
            "status": "error",
            "message": str(e),
            "traceback": error_traceback
        }), 500


#--------------------------------------------------------------------------------#
#                                 BLOGS ROUTE                                    #
#--------------------------------------------------------------------------------#

@app.route('/get_blog_list')
def get_blog_list():
    search_keyword = request.args.get('search_keyword')
    print(f"Received search keyword: {search_keyword}")
    list_of_blogs = get_blogs_list_db(search_keyword=search_keyword)
    print(f"Blogs list retrieved: {list_of_blogs}")
    return jsonify({
        "status": "success",
        "blogs": list_of_blogs
    })

@app.route('/delete_blog', methods=['POST'])
def delete_blog():
    data = request.json
    print(f"Received data for delete_blog: {json.dumps(data, indent=2, ensure_ascii=False)}")

    if 'blog_id' not in data:
        return jsonify({"status": "error", "message": "Blog ID is required"}), 400

    blog_id = data['blog_id']
    result = delete_blog_from_db(blog_id)

    if result['status'] == 'success':
        return jsonify({"status": "success", "message": "Blog deleted successfully"}), 200
    else:
        return jsonify({"status": "error", "message": "Failed to delete blog"}), 500


#--------------------------------------------------------------------------------#
#                             UPLOAD FILES ROUTE                                 #
#--------------------------------------------------------------------------------#

@app.route('/manage_files')
def manage_files():
    return render_template('manage_files.html')

@app.route('/upload_file', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"status": "error", "message": "No file part"}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"status": "error", "message": "No selected file"}), 400
        
        # Get file extension
        file_extension = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
        
        # Define allowed extensions
        image_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp', 'svg'}
        pdf_extensions = {'pdf'}
        
        # Check file type and determine bucket path
        if file_extension in image_extensions:
            bucket_path = 'blog-images'
        elif file_extension in pdf_extensions:
            bucket_path = 'magazine-pdfs'
        else:
            return jsonify({
                "status": "error", 
                "message": "File not supported. Only images (PNG, JPG, JPEG, GIF, WEBP, BMP, SVG) and PDF files are allowed."
            }), 400
        
        # Upload file to Supabase storage
        result = upload_file_to_storage(file, bucket_path)
        
        if result.get('status') == 'success':
            return jsonify({
                "status": "success",
                "message": "File uploaded successfully",
                "url": result.get('url', ''),
                "filename": file.filename
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": result.get('message', 'Failed to upload file')
            }), 500
            
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Upload failed: {str(e)}"
        }), 500

@app.route('/get_file_details', methods=['GET'])
def get_file_details():
    data = request.args
    print(f"Received data for get_file_details: {json.dumps(data, indent=2, ensure_ascii=False)}")

    bucket_name = data.get('bucket_name', None)
    if not bucket_name:
        return jsonify({"status": "error", "message": "Bucket name is required"}), 400
    file_details = get_file_details_db(bucket_name)
    if file_details['status'] == 'error':
        return jsonify({"status": "error", "message": file_details.get('message', 'Failed to retrieve file details')}), 500
    return jsonify({
        "status": "success",
        "data": file_details.get('data', [])
    }), 200

@app.route('/delete_file', methods=['POST'])
def delete_file():
    data = request.json
    print(f"Received data for delete_file: {json.dumps(data, indent=2, ensure_ascii=False)}")

    if 'file_name' not in data:
        return jsonify({"status": "error", "message": "File name is required"}), 400

    file_name = data['file_name']
    result = delete_file_from_storage(file_name)

    if result['status'] == 'success':
        return jsonify({"status": "success", "message": result.get('message', 'File deleted successfully')}), 200
    else:
        return jsonify({"status": "error", "message": result.get('message', 'Failed to delete file')}), 500
    



#--------------------------------------------------------------------------------#
#                            MAGAZINE PAGE FUNCTIONS                             #
#--------------------------------------------------------------------------------#

@app.route('/magazine_page')
def magazine_page():
    return render_template('magazine_page.html')

@app.route('/magazine/<magazine_id>')
def magazine_page_read_only(magazine_id):
    data = get_magazine_details_db(magazine_id)
    magazine_html = open('templates/magazine_page_read_only.html').read()

    updated_html = magazine_html.replace('[[pdf_url]]', data.get('pdf_url', ''))
    updated_html = updated_html.replace('[[magazine_id]]', magazine_id)

    if not data:
        return render_template('404.html'), 404
    
    return updated_html


@app.route('/flipbook/<magazine_id>')
@app.route('/flipbook')
def magazine_page_flipbook_view(magazine_id=None):
    if magazine_id is None:
        magazine_id = request.args.get('magazine_id')
        
    if not magazine_id:
        return render_template('404.html'), 404
        
    print(f"Received request for magazine_id: {magazine_id}")
    page_number = request.args.get('page_number', '1')
    data = get_magazine_details_db(magazine_id)
    
    if not data:
        return render_template('404.html'), 404
    
    magazine_html = open('templates/magazine_page_flipbook.html').read()
    updated_html = magazine_html.replace('[[pdf_url]]', data.get('pdf_url', ''))
    updated_html = updated_html.replace('[[page_number]]', page_number)
    
    return updated_html








#--------------------------------------------------------------------------------#
#                                 TRIAL ROUTE                                    #
#--------------------------------------------------------------------------------#

@app.route('/trial')
def trial():
    return render_template('trial.html')

@app.route('/dynamic_render_trial')
def dynamic_render_trial():
    return get_homepage()

@app.route('/news_page_dev')
def news_page_dev():
    return render_template('news_page_dev.html')










#--------------------------------------------------------------------------------#
#                               MAIN RUNNING SCRIPT                              #
#--------------------------------------------------------------------------------#


def kill_ngrok_processes():
    ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN"))
    # Kill using pyngrok
    try:
        ngrok.kill()
        print("Killed ngrok processes via pyngrok")
    except Exception as e:
        print(f"pyngrok kill error: {e}")
    
    # Find and kill by process name
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'ngrok' in proc.info['name'].lower():
                print(f"Killing ngrok process with PID {proc.info['pid']}")
                psutil.Process(proc.info['pid']).terminate()
                time.sleep(0.5)
                if psutil.pid_exists(proc.info['pid']):
                    psutil.Process(proc.info['pid']).kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Additional OS-specific commands
    try:
        if os.name == 'nt':  # Windows
            os.system('taskkill /F /IM ngrok.exe')
        else:  # Linux/Mac
            os.system('pkill -f ngrok')
    except Exception as e:
        print(f"OS command error: {e}")
        
    # Wait to ensure processes are terminated
    time.sleep(2)

def main(t = 'ngrok'):
    if t == 'ngrok':
        kill_ngrok_processes()
        run_with_ngrok(app)
        ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN"))
        ngrok_tunnel = ngrok.connect(addr='5000', proto="http", hostname="noble-raven-entirely.ngrok-free.app")
        print("Public URL:", ngrok_tunnel.public_url)
        app.run()
    else:
        app.run(port=5000, debug=True, use_reloader=True)

if __name__ == "__main__":
    main(t='local')






# 1. in ai lifestyle we need to add another bottom panel with 3 posts each. --done
# 2. move the view all articles button to the bottom of the section.  --done
# 5. editorial changes to podcast in header. --done
# 8. remove the Entrepreneurship from header.   -- done
# 9. news_page restructure  --done

# 3. magazine_page_read_only page add a leadership section on the right of the magazine and a banner ad space on the left of the magazine.
# 4. add a bar and full screen button and a download button for the flipbook magazine.

# 6. newsletter page to be implemented.
# 7. the startup and Business in the header will lead to category_homepage, and will changes based on which option is selected.



# 9. only categories we will write content manually: 
#     1. startup
#     2. gcc
#     3. technology

# 10. need a feature to add new category pages and edit that category page in future as well. **
# 11. admin should be able to change meta description and canonical tag of the page.




