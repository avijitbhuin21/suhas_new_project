import hashlib
from static.data.db_handler import *

def sha256_hash(input_string):
    encoded_string = input_string.encode('utf-8')
    sha256_hash = hashlib.sha256(encoded_string)
    return sha256_hash.hexdigest()

def generate_header_dropdowns_html(blogs_by_category):
    """Generates the HTML for the header navigation dropdowns."""
    nav_links_html = []
    
    category_map = {
        "business": "Latest Business Stories",
        "technology": "Tech Innovations",
        "gcc": "GCC Regional News",
        "sustainability": "Green Initiatives",
        "semiconductor": "Chip Industry Updates"
    }

    for category, blogs in blogs_by_category.items():
        category_title = category_map.get(category, f"Latest in {category.capitalize()}")
        
        items_html = ""
        for blog in blogs:
            items_html += f'''
            <a href="/blog/{blog.get('id')}" class="dropdown-item" data-category="{category}" data-id="{blog.get('id')}">
            <div class="dropdown-item flex items-center space-x-3 p-2 rounded-lg cursor-pointer" data-category="{category}" data-id="{blog.get('id')}">
                <img src="{blog.get('image')}" alt="{blog.get('title')}" class="w-12 h-12 object-cover rounded">
                <div class="flex-1">
                    <h4 class="text-gray-800 text-xs font-medium line-clamp-2">{blog.get('title')}</h4>
                </div>
            </div>
            </a>
            '''

        dropdown_html = f'''
        <div class="dropdown-container" data-category="{category}">
            <a href="/{category}" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">{category.capitalize()}</a>
            <div class="dropdown-content">
                <h3 class="text-gray-800 font-semibold text-sm mb-3">{category_title}</h3>
                <div class="space-y-3">
                    {items_html}
                    <div class="border-t border-gray-200 pt-3 mt-3">
                        <div class="dropdown-item know-more-item flex items-center justify-center p-2 rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100">
                            <span class="text-[#3533CD] text-xs font-medium mr-1">Know More</span>
                            <i class="ph ph-arrow-right text-[#3533CD] text-xs transition-all duration-200"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        '''
        nav_links_html.append(dropdown_html)
        
    return "\n".join(nav_links_html)

def generate_mobile_accordion_html(blogs_by_category):
    """Generates the HTML for the mobile accordion menu."""
    
    icon_map = {
        "business": "ph-buildings",
        "technology": "ph-gear",
        "gcc": "ph-globe",
        "sustainability": "ph-leaf",
        "semiconductor": "ph-cpu"
    }
    accordion_html = ""
    for category, blogs in blogs_by_category.items():
        icon_class = icon_map.get(category, "ph-article")
        blog_items_html = ""
        for blog in blogs:
            blog_items_html += f'''
            <a href="/blog/{blog.get('id')}" class="sub-menu-item" data-category="{category}" data-id="{blog.get('id')}">
                <img src="{blog.get('image')}" alt="{blog.get('title')}" class="w-10 h-10 object-cover rounded-md flex-shrink-0">
                <div class="flex-1 ml-3"><h4 class="text-white text-xs font-medium line-clamp-2">{blog.get('title')}</h4></div>
            </a>
            '''
        accordion_html += f'''
        <div>
            <a href="#" class="accordion-toggle mobile-menu-item" aria-expanded="false">
                <div class="flex items-center">
                    <i class="ph {icon_class} text-white text-lg"></i>
                    <span class="item-title">{category.capitalize()}</span>
                </div>
                <i class="ph ph-caret-down accordion-icon text-lg text-gray-400"></i>
            </a>
            <div class="accordion-content">
                <div class="p-3 space-y-2">
                    {blog_items_html}
                    <div class="pt-2 mt-2 border-t border-gray-700/50">
                        <a href="#" class="sub-menu-item know-more-item-mobile justify-center bg-gray-700/50 hover:bg-gray-600/50">
                            <span class="text-bol-purple-light text-xs font-medium mr-1">Know More</span>
                            <i class="ph ph-arrow-right text-bol-purple-light text-xs"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        '''
    return accordion_html


def get_blogs_list_db(search_keyword,limit):
    print(f"Searching blogs with keyword: {search_keyword}")
    if not search_keyword or search_keyword.strip() == "":
        # Return all blogs if no search keyword
        response = (
            supabase.table("blogs")
            .select("*")
            .order("created_at", desc=True)
            .limit(limit)
            .execute()
        )
    else:
        # Search in multiple fields: id, category, and blog title within json_data
        search_term = f'%{search_keyword.replace(" ", "_").lower()}%'
        response = (
            supabase.table("blogs")
            .select("*")
            .or_(f"id.ilike.{search_term},category.ilike.{search_term}")  # sub_category.ilike.{search_term} commented out
            .order("created_at", desc=True).limit(limit)
            .execute()
        )
    
    if response.data:
        return response.data
    return []


def get_blogs_for_header(limit):
    """Helper function to fetch blog data for header dropdowns."""
    categories = ["Business", "Technology", "GCC", "Sustainability", "Semiconductor"]
    blogs_by_category = {}
    for category in categories:
        blogs = get_blogs_list_db(search_keyword=category,limit=limit)
        blogs_by_category[category.lower()] = [
            {
                "id": blog.get("id"),
                "title": blog.get("json_data", {}).get("blogTitle"),
                "image": blog.get("json_data", {}).get("mainImageUrl"),
            }
            for blog in blogs[:3]
        ]
    return blogs_by_category



def get_business_cards():
    """Generates the 'More in Business' section with dynamic blog data."""
    business_blogs = get_blogs_list_db(limit=6,search_keyword=None)  # Ensure the function is available in this scope
    cards_html = []
    for blog in business_blogs:
        blog_data = blog.get('json_data', {})
        
        # Prepare text for display and for the hover tooltip
        blog_title = blog_data.get('blogTitle', 'Untitled')
        blog_author = blog_data.get('blogAuthor', 'N/A')
        blog_date = blog_data.get('blogDate', '')
        author_date_string = f"{blog_author} -- {blog_date}"

        card = f"""
          <div href="/{blog.get('id')}" class="bg-white p-3 flex gap-4 h-auto min-h-[120px] md:h-[151px] transition-shadow hover:shadow-md">
            <img src="{blog_data.get('mainImageUrl', 'https://picsum.photos/127/121')}" alt="{blog_data.get('mainImageAlt', 'Business article')}" class="w-[90px] md:w-[127px] h-auto md:h-[121px] object-cover flex-none"/>
            <div class="flex flex-col flex-1 overflow-hidden">
              <span class="font-jakarta font-bold text-[10px] md:text-[12px] leading-[24px] md:leading-[30px] text-black uppercase">{blog.get('category')}</span>
              <a href="/blog/{blog.get('id')}" title="{blog_title}" class="font-jakarta font-medium text-[14px] md:text-[16px] leading-[22px] md:leading-[25px] text-black grow hover:text-black line-clamp-3">{blog_title}</a>
              <span title="{author_date_string}" class="font-jakarta italic font-bold text-[10px] md:text-[12px] text-black mt-auto block truncate">{author_date_string}</span>
            </div>
          </div>
        """
        cards_html.append(card)

    return f'''<div class="mt-8 md:mt-16">
        <h2 class="font-jakarta font-bold text-[28px] md:text-[40px] leading-[30px] text-black mb-6 md:mb-8"> More in Business </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-8" >
          {''.join(cards_html)}
        </div>
      </div>'''

def breadcrumbs(category):
    return f'''
<article>
        <nav class="mb-4 text-left" aria-label="Breadcrumb">
        
        <div class="text-sm text-gray-600">
                    <span href="/{category}" class="font-jakarta font-medium">{category}</span>
                </div>
            </nav>
        </article>'''
