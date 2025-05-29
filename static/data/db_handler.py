from supabase import create_client, Client

from dotenv import load_dotenv
import os
load_dotenv()

from supabase import create_client, Client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

from .html_templates import *


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
    data = response.data[0]
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












#--------------------------------------------------------------------------------#
#                             ADMIN PAGE FUNCTIONS                               #
#--------------------------------------------------------------------------------#

# def get_cards():
