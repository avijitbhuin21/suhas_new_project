import hashlib
from static.data.db_handler import *
import math

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
                            <a href="/{category}"><span class="text-[#3533CD] text-xs font-medium mr-1">Know More</span></a>
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
                        <a href="/{category}" class="sub-menu-item know-more-item-mobile justify-center bg-gray-700/50 hover:bg-gray-600/50">
                            <span class="text-bol-purple-light text-xs font-medium mr-1">Know More</span>
                            <i class="ph ph-arrow-right text-bol-purple-light text-xs"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        '''
    return accordion_html


def get_blogs_for_header(limit):
    """Helper function to fetch blog data for header dropdowns."""
    categories = ["Business", "Technology", "GCC", "Sustainability", "Semiconductor"]
    blogs_by_category = {}
    for category in categories:
        blogs, _ = get_blogs_list_db(search_keyword=category, page=1, per_page=limit)
        blogs_by_category[category.lower()] = [
            {
                "id": blog.get("id"),
                "title": blog.get("json_data", {}).get("blogTitle"),
                "image": blog.get("json_data", {}).get("mainImageUrl"),
            }
            for blog in blogs
        ]
    return blogs_by_category

def _generate_business_card_items_html(blogs):
    """Helper to generate just the HTML for the blog cards."""
    if not blogs:
        return '<p class="col-span-full text-center py-8">No more blogs to display.</p>'

    cards_html = []
    for blog in blogs:
        blog_data = blog.get('json_data', {})
        
        blog_title = blog_data.get('blogTitle', 'Untitled')
        blog_author = blog_data.get('blogAuthor', 'N/A')
        blog_date = blog_data.get('blogDate', '')
        author_date_string = f"{blog_author} -- {blog_date}"

        card = f"""
          <div class="bg-white p-3 flex gap-4 h-auto min-h-[120px] md:h-[151px] transition-shadow hover:shadow-md">
            <img src="{blog_data.get('mainImageUrl', 'https://picsum.photos/127/121')}" alt="{blog_data.get('mainImageAlt', 'Business article')}" class="w-[90px] md:w-[127px] h-auto md:h-[121px] object-cover flex-none"/>
            <div class="flex flex-col flex-1 overflow-hidden">
              <span class="font-jakarta font-bold text-[10px] md:text-[12px] leading-[24px] md:leading-[30px] text-black uppercase">
              <a href="/{blog.get('category').lower()}">{blog.get('category')}</a></span>
              <a href="/blog/{blog.get('id')}" title="{blog_title}" class="font-jakarta font-medium text-[14px] md:text-[16px] leading-[22px] md:leading-[25px] text-black grow hover:text-black line-clamp-3">{blog_title}</a>
              <span title="{author_date_string}" class="font-jakarta italic font-bold text-[10px] md:text-[12px] text-black mt-auto block truncate">{author_date_string}</span>
            </div>
          </div>
        """
        cards_html.append(card)
    return ''.join(cards_html)

def _generate_pagination_controls_html(current_page, total_pages):
    """Helper to generate HTML for the pagination buttons."""
    if total_pages <= 1:
        return ""

    prev_disabled = 'disabled' if current_page == 1 else ''
    prev_onclick = f"onclick=\"loadBusinessPage({current_page - 1})\"" if current_page > 1 else ""
    
    next_disabled = 'disabled' if current_page == total_pages else ''
    next_onclick = f"onclick=\"loadBusinessPage({current_page + 1})\"" if current_page < total_pages else ""

    pagination_html = f"""
        <button class="pagination-btn" {prev_onclick} {prev_disabled}>Previous</button>
        <span class="page-info">Page {current_page} of {total_pages}</span>
        <button class="pagination-btn" {next_onclick} {next_disabled}>Next</button>
    """
    return f'<div class="flex justify-center items-center mt-8 space-x-2 md:space-x-4">{pagination_html}</div>'

def get_paginated_business_cards_data(page=1):
    """
    Fetches the data for a specific page of business cards.
    Returns a dictionary with HTML strings for cards and pagination controls.
    This function is intended to be called by an API endpoint.
    """
    per_page = 6
    business_blogs, total_count = get_blogs_list_db(search_keyword=None, page=page, per_page=per_page)
    total_pages = math.ceil(total_count / per_page)

    cards_html = _generate_business_card_items_html(business_blogs)
    pagination_html = _generate_pagination_controls_html(page, total_pages)

    return {
        "cards_html": cards_html,
        "pagination_html": pagination_html
    }

def get_business_cards(page=1):
    """Generates the 'More in Business' section with pagination and JS."""
    per_page = 6
    business_blogs, total_count = get_blogs_list_db(search_keyword=None, page=page, per_page=per_page)
    
    total_pages = math.ceil(total_count / per_page)
    
    cards_html = _generate_business_card_items_html(business_blogs)
    pagination_html = _generate_pagination_controls_html(page, total_pages)

    script_html = """
    <script>
      async function loadBusinessPage(page) {
        const grid = document.getElementById('business-cards-grid');
        const paginationControls = document.getElementById('business-pagination-controls');
        const section = document.getElementById('more-in-business-section');
        
        if (!grid || !paginationControls || !section) return;

        grid.style.opacity = '0.5';
        paginationControls.style.opacity = '0.5';

        try {
          const response = await fetch(`/get_paginated_business_cards?page=${page}`);
          if (!response.ok) throw new Error(`Network response was not ok, status: ${response.status}`);
          
          const data = await response.json();
          grid.innerHTML = data.cards_html;
          paginationControls.innerHTML = data.pagination_html;

        } catch (error) {
          console.error('Failed to load business page:', error);
          grid.innerHTML = '<p class="col-span-full text-center py-8">Error loading content. Please try again later.</p>';
        } finally {
          grid.style.opacity = '1';
          paginationControls.style.opacity = '1';
          section.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    </script>
    <style>
      .pagination-btn { padding: 8px 12px; border: 1px solid #ccc; border-radius: 4px; cursor: pointer; background-color: white; transition: background-color 0.2s, opacity 0.2s; font-size: 14px; }
      .pagination-btn:hover:not(:disabled) { background-color: #f0f0f0; }
      .pagination-btn:disabled { cursor: not-allowed; opacity: 0.5; }
      .page-info { margin: 0 1rem; font-size: 14px; color: #333; }
      #business-pagination-controls .flex { flex-wrap: wrap; }
    </style>
    """

    section_html = f'''<div id="more-in-business-section" class="mt-8 md:mt-16">
        <h2 class="font-jakarta font-bold text-[28px] md:text-[40px] leading-[30px] text-black mb-6 md:mb-8"> More in Business </h2>
        <div id="business-cards-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-8 min-h-[300px]">
          {cards_html}
        </div>
        <div id="business-pagination-controls">
          {pagination_html}
        </div>
      </div>
      {script_html}
    '''
    
    return section_html

def breadcrumbs(category):
    return f'''
        <article>
            <nav class="mb-4 text-left" aria-label="Breadcrumb">
                <div class="text-sm text-gray-600">
                    <span  class="font-jakarta font-medium">
                        <a href="/{category.lower()}">{category}
                        </a>
                    </span>
                </div>
            </nav>
        </article>'''