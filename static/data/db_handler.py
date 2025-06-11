from supabase import create_client, Client

from dotenv import load_dotenv
import os
load_dotenv()

from supabase import create_client, Client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

from .html_templates import *
import time


def format_file_size(size_bytes):
    """Convert bytes to human readable format (B, KB, MB, GB, TB)"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"



#--------------------------------------------------------------------------------#
#                               BLOGS FUNCTIONS                                  #
#--------------------------------------------------------------------------------#

def get_blog(blog_id, render=False):
    response = (
        supabase.table("blogs")
        .select("*")
        .eq("id", blog_id)
        .execute()
    )
    data = response.data[0] if len(response.data) > 0 else None
    if render:
        NEWSPAGE_BLANK_TEMPLATE = NEWSPAGE_BLANK_TEMPLATE.replace("[[meta tags]]", data['meta_tags'])
        return NEWSPAGE_BLANK_TEMPLATE
    return data


def handle_blog(blog_id:str = None, insert_data:dict =None, update_data:dict= None, operation:str = None):
    if operation == "insert":
        if insert_data is None:
            raise ValueError("insert_data must be provided for insert operation")
        # Insert a new blog
        response = (
            supabase.table("blogs")
            .insert(insert_data)
            .execute()
        )
        return response.data
    
    if operation == "update":
        if blog_id is None or update_data is None:
            raise ValueError("blog_id and update_data must be provided for update operation")
        # Update an existing blog
        response = (
            supabase.table("blogs")
            .update(update_data)
            .eq("id", blog_id)
            .execute()
        )
        return response.data
    
    if operation == "delete":
        if blog_id is None:
            raise ValueError("blog_id must be provided for delete operation")
        # Delete a blog
        response = (
            supabase.table("blogs")
            .delete()
            .eq("id", blog_id)
            .execute()
        )
        return response.data


def get_leadership_details():
    response = (
        supabase.table("leadership_table")
        .select("*")
        .execute()
    )
    return response.data[0] if response.data else None

def save_blogs_to_db(blog_data):
    modified_data = {}
    modified_data['id'] = blog_data.get('blogTitle', '').replace(" ", "_").lower()
    modified_data['created_by'] = blog_data.get('admin_name', '')
    modified_data['status'] = blog_data.get('status', 'draft')

    del blog_data['admin_name']
    del blog_data['status']
    del blog_data['enc_email']
    del blog_data['enc_pwd']

    modified_data['json_data'] = blog_data
    modified_data['history'] = [
        {
            "admin_name": modified_data['created_by'],
            "date": blog_data.get('blogDate', '')
        }
    ]
    try:
        response = (
            supabase.table("blogs")
            .insert(modified_data)
            .execute()
        )
    except Exception as e:
        print(f"Error saving blog to database: {e}")
        error_str = str(e)
        print(f"Error string: {error_str}")
        if '23505' in error_str and 'duplicate key value violates unique constraint' in error_str:
            return {"status": "error", "message": "Blog with this title already exists."}
        return False
    response.data[0]['url'] = f"{blog_data['base_url']}/blog/{modified_data['id']}"
    return response.data[0]

def update_blogs_to_db(blog_data):
    delete_blog_from_db(blog_data['blog_id'])
    res = save_blogs_to_db(blog_data)

    if res:
        return {"status": "success", "message": "Blog updated successfully.", "data": res}
    return {"status": "error", "message": "Failed to update blog."}



def get_blogs_list_db(search_keyword):
    print(f"Searching blogs with keyword: {search_keyword}")
    response = (
        supabase.table("blogs")
        .select("*")
        .ilike("id", f'%{search_keyword.replace(" ", "_").lower()}%')
        .execute()
    )
    if response.data:
        return response.data
    return []

def delete_blog_from_db(blog_id):
    print(f"Deleting blog with ID: {blog_id}")
    response = (
        supabase.table("blogs")
        .delete()
        .eq("id", blog_id)
        .execute()
    )
    if response.data:
        return {"status": "success", "message": "Blog deleted successfully."}
    return {"status": "error", "message": "Blog not found or could not be deleted."}

#--------------------------------------------------------------------------------#
#                             UPLOAD PAGE FUNCTIONS                               #
#--------------------------------------------------------------------------------#

def upload_file_to_storage(file, file_path):
    try:
        # Generate a unique filename to avoid conflicts
        timestamp = str(int(time.time()))
        
        # Read file content
        file_content = file.read()
        
        # Upload to Supabase storage
        response = supabase.storage.from_(file_path).upload(
            path=file.filename,
            file=file_content,
            file_options={"content-type": file.content_type}
        )
        if not response:
            raise Exception(f"Error uploading file: {response.error.message}")        
        return {
            "status": "success",
            "filename": file.filename
        }
        
    except Exception as e:
        print(f"Error uploading to storage: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }


def get_file_details_db(bucket_name):
    try:
        # List all files in the specified bucket
        response = supabase.storage.from_(bucket_name).list()
        
        if not response:
            return {
                "status": "error",
                "message": "Failed to retrieve files",
                "data": []
            }
        
        file_details = []
        public_url = supabase.storage.from_(bucket_name).get_public_url(response[0]['name'])
        for file in response:
            # Get public URL for each file
            temp = public_url.split('storage')[0] + 'storage/v1/object/public/' + bucket_name + '/' + file['name']
            
            file_info = {
                "name": file['name'],
                "size": format_file_size(file['metadata']['size']),
                "id": file['id'],
                "public_url": temp ,
            }
            file_details.append(file_info)
        
        return {
            "status": "success",
            "data": file_details,
            "public_url": public_url
        }
        
    except Exception as e:
        print(f"Error getting file details: {str(e)}")
        return {
            "status": "error",
            "message": str(e),
            "data": []
        }

def delete_file_from_storage(file_name):
    try:
        # Determine bucket based on file extension
        file_extension = file_name.lower().split('.')[-1]
        
        if file_extension in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'svg']:
            bucket_name = "blog-images"
        elif file_extension == 'pdf':
            bucket_name = "magazine-pdfs"
        elif file_name == '.emptyFolderPlaceholder':
            bucket_name = 'blog-images'
        else:
            return {
                "status": "error",
                "message": "Unsupported file type. Only images and PDFs are allowed."
            }
        
        # Delete file from Supabase storage
        response = supabase.storage.from_(bucket_name).remove([file_name])
        
        if not response:
            return {
                "status": "error",
                "message": "Failed to delete file"
            }
        
        return {
            "status": "success",
            "message": f"File '{file_name}' deleted successfully from {bucket_name}"
        }
        
    except Exception as e:
        print(f"Error deleting file from storage: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }
    




#--------------------------------------------------------------------------------#
#                             ADMIN PAGE FUNCTIONS                               #
#--------------------------------------------------------------------------------#

def admin_login_db_check(email, password):
    print(f"Attempting admin login with email: {email} and \n password: {password}")
    response = (
        supabase.table("admin users")
        .select("*")
        .eq("email", email)
        .eq("password", password)
        .execute()
    )
    if response.data:
        return {
            "success": True,
            "email": email,
            "name": response.data[0]['username'],
            "enc_email": response.data[0]['email'],
            "enc_pwd": response.data[0]['password']
        }
    return {
        "success": False,
        "email": email
    }
