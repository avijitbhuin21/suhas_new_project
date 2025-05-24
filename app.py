from flask import Flask, render_template, request, jsonify
from static.data.page_handler import *

from pyngrok import ngrok
import psutil
import os
import time
from dotenv import load_dotenv

from static.data.page_handler import *
from static.data.page_editor import *
from static.data.db_handler import *

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

@app.route('/magazine_page')
def magazine_page():
    return render_template('magazine_page.html')

@app.route('/magazine_page_read_only')
def magazine_page_read_only():
    return render_template('magazine_page_read_only.html')

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

@app.route('/get_blog')
def get_blog():
    blog_id = request.args.get('blog_id')
    # Add logic to fetch and return blog data based on blog_id
    return jsonify({"blog_id": blog_id, "message": "Blog data will be here"})








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




