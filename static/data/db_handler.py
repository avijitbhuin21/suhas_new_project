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

# --------------------------------------------------------------------------------#
#                           HOMEPAGE HELPER FUNCTIONS                            #
# --------------------------------------------------------------------------------#


def get_blogs_list_db(search_keyword, page=1, per_page=100, include_deleted=False):
    print(
        f"Searching blogs with keyword: {search_keyword}, page: {page}, per_page: {per_page}"
    )

    offset = (page - 1) * per_page

    # Use count='exact' to get the total number of rows matching the query
    query = supabase.table("blogs").select("*", count="exact")
    
    # Exclude deleted blogs unless specifically requested
    if not include_deleted:
        query = query.neq("status", "deleted")

    if not search_keyword or search_keyword.strip() == "":
        response = (
            query.order("created_at", desc=True)
            .range(offset, offset + per_page - 1)
            .execute()
        )
    else:
        search_term = f'%{search_keyword.replace(" ", "_").lower()}%'
        response = (
            query.or_(f"id.ilike.{search_term},category.ilike.{search_term}")
            .order("created_at", desc=True)
            .range(offset, offset + per_page - 1)
            .execute()
        )

    # The response object now contains 'data' and 'count'
    if response.data:
        return response.data, response.count
    return [], 0


def get_page_data(page_name: str):
    response = (
        supabase.table("main_pages").select("*").eq("page_name", page_name).execute()
    )
    return response.data[0] if response.data else None


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


# --------------------------------------------------------------------------------#
#                               BLOGS FUNCTIONS                                  #
# --------------------------------------------------------------------------------#


def get_blog(blog_id, render=False):
    response = supabase.table("blogs").select("*").eq("id", blog_id).execute()
    data = response.data[0] if len(response.data) > 0 else None
    if render:
        NEWSPAGE_BLANK_TEMPLATE = NEWSPAGE_BLANK_TEMPLATE.replace(
            "[[meta tags]]", data["meta_tags"]
        )
        return NEWSPAGE_BLANK_TEMPLATE
    return data


def handle_blog(
    blog_id: str = None,
    insert_data: dict = None,
    update_data: dict = None,
    operation: str = None,
):
    if operation == "insert":
        if insert_data is None:
            raise ValueError("insert_data must be provided for insert operation")
        # Insert a new blog
        response = supabase.table("blogs").insert(insert_data).execute()
        return response.data

    if operation == "update":
        if blog_id is None or update_data is None:
            raise ValueError(
                "blog_id and update_data must be provided for update operation"
            )
        # Update an existing blog
        response = (
            supabase.table("blogs").update(update_data).eq("id", blog_id).execute()
        )
        return response.data

    if operation == "delete":
        if blog_id is None:
            raise ValueError("blog_id must be provided for delete operation")
        # Delete a blog
        response = supabase.table("blogs").delete().eq("id", blog_id).execute()
        return response.data


def get_leadership_details():
    response = supabase.table("leadership_table").select("*").execute()
    return response.data[0] if response.data else None


def save_blogs_to_db(blog_data):
    modified_data = {}
    blog_id = blog_data.get("blogTitle", "").replace(" ", "_").lower()
    modified_data["id"] = blog_id
    modified_data["created_by"] = blog_data.get("admin_name", "")
    modified_data["status"] = blog_data.get("status", "draft")

    # Extract category and SEO information for separate storage if needed
    modified_data["category"] = blog_data.get("blogCategory", "")
    # Sub-category commented out as requested
    # modified_data['sub_category'] = blog_data.get('blogSubCategory', '')
    
    # Extract and store labels in JSON format
    labels_data = blog_data.get("labels", {})
    modified_data["labels"] = labels_data if isinstance(labels_data, dict) else {}

    # Generate meta tags from SEO data
    seo_title = blog_data.get("seoTitle", "") or blog_data.get("blogTitle", "")
    seo_description = blog_data.get("seoMetaDescription", "") or blog_data.get(
        "blogSummary", ""
    )
    seo_canonical = (
        blog_data.get("seoCanonicalUrl", "")
        or f"{blog_data.get('base_url', '')}/blog/{modified_data['id']}"
    )

    # Create meta tags HTML
    meta_tags = f"""<title>{seo_title}</title>
    <meta name="description" content="{seo_description}">
    <meta property="og:title" content="{seo_title}">
    <meta property="og:description" content="{seo_description}">
    <meta property="og:image" content="{blog_data.get('mainImageUrl', '')}">
    <meta property="og:url" content="{seo_canonical}">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{seo_title}">
    <meta name="twitter:description" content="{seo_description}">
    <meta name="twitter:image" content="{blog_data.get('mainImageUrl', '')}">
    <link rel="canonical" href="{seo_canonical}">"""

    modified_data["meta_tags"] = meta_tags

    # Store the base_url before cleaning up for the return URL
    base_url = blog_data.get("base_url", "")

    # Clean up fields before storing in json_data
    fields_to_remove = ["admin_name", "status", "enc_email", "enc_pwd", "base_url", "labels"]
    for field in fields_to_remove:
        if field in blog_data:
            del blog_data[field]

    # Store the complete blog data including category and SEO information
    modified_data["json_data"] = blog_data
    
    # Check if a blog with the same ID exists and is in deleted state
    try:
        existing_blog_response = supabase.table("blogs").select("*").eq("id", blog_id).execute()
        existing_blog = existing_blog_response.data[0] if existing_blog_response.data else None
        
        if existing_blog and existing_blog.get("status") == "deleted":
            # Update the existing deleted blog instead of inserting
            print(f"Found existing deleted blog with ID: {blog_id}. Updating instead of inserting.")
            
            # Clear redirect URL when updating from deleted state
            modified_data["redirect_url"] = None
            
            # Get existing blog history and append to it
            if existing_blog and "history" in existing_blog:
                modified_data["history"] = existing_blog["history"]
                modified_data["history"].append(
                    {
                        "admin_name": modified_data["created_by"],
                        "date": blog_data.get("blogDate", ""),
                        "action": "restored_from_deleted",
                    }
                )
            else:
                modified_data["history"] = [
                    {
                        "admin_name": modified_data["created_by"],
                        "date": blog_data.get("blogDate", ""),
                        "action": "restored_from_deleted",
                    }
                ]
            
            # Update the existing blog
            response = supabase.table("blogs").update(modified_data).eq("id", blog_id).execute()
            
            if response.data:
                response.data[0]["url"] = f"{base_url}/blog/{modified_data['id']}"
                return response.data[0]
            else:
                return {
                    "status": "error",
                    "message": "Failed to update existing deleted blog.",
                }
        else:
            # Insert new blog (original logic)
            modified_data["history"] = [
                {
                    "admin_name": modified_data["created_by"],
                    "date": blog_data.get("blogDate", ""),
                }
            ]
            
            # Debug: Print what data is being stored
            print(f"Inserting new blog with data: {modified_data}")
            
            response = supabase.table("blogs").insert(modified_data).execute()
            
            # Use the stored base_url for the return URL
            response.data[0]["url"] = f"{base_url}/blog/{modified_data['id']}"
            return response.data[0]
            
    except Exception as e:
        print(f"Error saving blog to database: {e}")
        error_str = str(e)
        print(f"Error string: {error_str}")
        if (
            "23505" in error_str
            and "duplicate key value violates unique constraint" in error_str
        ):
            return {
                "status": "error",
                "message": "Blog with this title already exists.",
            }
        return {
            "status": "error",
            "message": f"Failed to save blog: {str(e)}",
        }


def update_blogs_to_db(blog_data):
    blog_id = blog_data.get("blog_id")
    if not blog_id:
        return {"status": "error", "message": "Blog ID is required for update."}

    # Prepare update data similar to save_blogs_to_db
    modified_data = {}
    modified_data["id"] = blog_data.get("blogTitle", "").replace(" ", "_").lower()
    modified_data["created_by"] = blog_data.get("admin_name", "")
    modified_data["status"] = blog_data.get("status", "draft")

    # Extract category and SEO information
    modified_data["category"] = blog_data.get("blogCategory", "")
    # Sub-category commented out as requested
    # modified_data['sub_category'] = blog_data.get('blogSubCategory', '')
    
    # Extract and store labels in JSON format
    labels_data = blog_data.get("labels", {})
    modified_data["labels"] = labels_data if isinstance(labels_data, dict) else {}

    # Generate meta tags from SEO data
    seo_title = blog_data.get("seoTitle", "") or blog_data.get("blogTitle", "")
    seo_description = blog_data.get("seoMetaDescription", "") or blog_data.get(
        "blogSummary", ""
    )
    seo_canonical = (
        blog_data.get("seoCanonicalUrl", "")
        or f"{blog_data.get('base_url', '')}/blog/{modified_data['id']}"
    )

    # Create meta tags HTML
    meta_tags = f"""<title>{seo_title}</title>
    <meta name="description" content="{seo_description}">
    <meta property="og:title" content="{seo_title}">
    <meta property="og:description" content="{seo_description}">
    <meta property="og:image" content="{blog_data.get('mainImageUrl', '')}">
    <meta property="og:url" content="{seo_canonical}">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{seo_title}">
    <meta name="twitter:description" content="{seo_description}">
    <meta name="twitter:image" content="{blog_data.get('mainImageUrl', '')}">
    <link rel="canonical" href="{seo_canonical}">"""

    modified_data["meta_tags"] = meta_tags

    # Store the base_url before cleaning up
    base_url = blog_data.get("base_url", "")

    # Clean up fields before storing in json_data
    fields_to_remove = [
        "admin_name",
        "status",
        "enc_email",
        "enc_pwd",
        "base_url",
        "blog_id",
        "reason",
        "labels",
    ]
    for field in fields_to_remove:
        if field in blog_data:
            del blog_data[field]

    # Store the complete blog data
    modified_data["json_data"] = blog_data

    # Get existing blog history and append to it
    existing_blog = get_blog(blog_id)
    if existing_blog and "history" in existing_blog:
        modified_data["history"] = existing_blog["history"]
        modified_data["history"].append(
            {
                "admin_name": modified_data["created_by"],
                "date": blog_data.get("blogDate", ""),
                "action": "updated",
            }
        )
    else:
        modified_data["history"] = [
            {
                "admin_name": modified_data["created_by"],
                "date": blog_data.get("blogDate", ""),
                "action": "updated",
            }
        ]

    try:
        # Update the existing blog
        response = (
            supabase.table("blogs").update(modified_data).eq("id", blog_id).execute()
        )

        if response.data:
            response.data[0]["url"] = f"{base_url}/blog/{modified_data['id']}"
            return {
                "status": "success",
                "message": "Blog updated successfully.",
                "data": response.data[0],
            }
        else:
            return {
                "status": "error",
                "message": "Blog not found or could not be updated.",
            }

    except Exception as e:
        print(f"Error updating blog: {e}")
        return {"status": "error", "message": str(e)}


def delete_blog_from_db(blog_id, redirect_url=None):
    print(f"Marking blog as deleted with ID: {blog_id}")
    
    # Prepare update data
    update_data = {
        "status": "deleted"
    }
    
    # Add redirect URL if provided
    if redirect_url:
        update_data["redirect_url"] = redirect_url
    
    # Update the blog status instead of deleting
    response = supabase.table("blogs").update(update_data).eq("id", blog_id).execute()
    
    if response.data:
        return {"status": "success", "message": "Blog marked as deleted successfully."}
    return {"status": "error", "message": "Blog not found or could not be updated."}


# --------------------------------------------------------------------------------#
#                             UPLOAD PAGE FUNCTIONS                               #
# --------------------------------------------------------------------------------#


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
            file_options={"content-type": file.content_type},
        )
        if not response:
            raise Exception(f"Error uploading file: {response.error.message}")
        return {"status": "success", "filename": file.filename}

    except Exception as e:
        print(f"Error uploading to storage: {str(e)}")
        return {"status": "error", "message": str(e)}


def get_file_details_db(bucket_name):
    try:
        # List all files in the specified bucket
        response = supabase.storage.from_(bucket_name).list()

        if not response:
            return {
                "status": "error",
                "message": "Failed to retrieve files",
                "data": [],
            }

        file_details = []
        public_url = supabase.storage.from_(bucket_name).get_public_url(
            response[0]["name"]
        )
        for file in response:
            # Get public URL for each file
            temp = (
                public_url.split("storage")[0]
                + "storage/v1/object/public/"
                + bucket_name
                + "/"
                + file["name"]
            )

            file_info = {
                "name": file["name"],
                "size": format_file_size(file["metadata"]["size"]),
                "id": file["id"],
                "public_url": temp,
            }
            file_details.append(file_info)

        return {"status": "success", "data": file_details, "public_url": public_url}

    except Exception as e:
        print(f"Error getting file details: {str(e)}")
        return {"status": "error", "message": str(e), "data": []}


def delete_file_from_storage(file_name):
    try:
        # Determine bucket based on file extension
        file_extension = file_name.lower().split(".")[-1]

        if file_extension in ["jpg", "jpeg", "png", "gif", "bmp", "webp", "svg"]:
            bucket_name = "blog-images"
        elif file_extension == "pdf":
            bucket_name = "magazine-pdfs"
        elif file_name == ".emptyFolderPlaceholder":
            bucket_name = "blog-images"
        else:
            return {
                "status": "error",
                "message": "Unsupported file type. Only images and PDFs are allowed.",
            }

        # Delete file from Supabase storage
        response = supabase.storage.from_(bucket_name).remove([file_name])

        if not response:
            return {"status": "error", "message": "Failed to delete file"}

        return {
            "status": "success",
            "message": f"File '{file_name}' deleted successfully from {bucket_name}",
        }

    except Exception as e:
        print(f"Error deleting file from storage: {str(e)}")
        return {"status": "error", "message": str(e)}


# --------------------------------------------------------------------------------#
#                             ADMIN PAGE FUNCTIONS                               #
# --------------------------------------------------------------------------------#


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
            "name": response.data[0]["username"],
            "enc_email": response.data[0]["email"],
            "enc_pwd": response.data[0]["password"],
        }
    return {"success": False, "email": email}


# --------------------------------------------------------------------------------#
#                            MAGAZINE PAGE FUNCTIONS                             #
# --------------------------------------------------------------------------------#


def get_magazine_details_db(magazine_id):
    print(f"Fetching magazine details for ID: {magazine_id}")
    response = (
        supabase.table("magazine_details").select("*").eq("id", magazine_id).execute()
    )
    if response.data:
        return response.data[0]
    return None
