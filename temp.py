demo_json_data = {'mainImageUrl': 'https://fastly.picsum.photos/id/879/1920/1080',
 'mainImageAlt': 'main alt',
 'blogTitle': "Innovative Approaches to Talent Acquisition & Retention in Today's Professional Landscape",
 'blogAuthor': 'Craig Bator',
 'blogDate': '2025-05-26',
 'blogSummary': 'The quest for top talent in the professional landscape has never been more competitive. Companies are redefining their approaches to attract and retain exceptional minds and this evolution calls for innovative strategies in talent acquisition and retention. Reports suggest 75% of HR professionals ring the bell on a talent shortage as their biggest challenge. The figure throws into relief the critical need for creative solutions.',
 'adBannerBesideUrl': 'https://picsum.photos/1200/236?random=52',
 'adBannerBesideHref': 'ad banner',
 'adBannerBelowUrl': 'https://picsum.photos/1200/236?random=50',
 'adBannerBelowHref': 'ad banner',
 'dynamicSections': [{'type': 'text',
   'id': 'section_1',
   'content': 'The quest for top talent in the professional landscape has never been more competitive. Companies are redefining their approaches to attract and retain exceptional minds and this evolution calls for innovative strategies in talent acquisition and retention. Reports suggest 75% of HR professionals ring the bell on a talent shortage as their biggest challenge. The figure throws into relief the critical need for creative solutions.'},
  {'type': 'header',
   'id': 'section_2',
   'content': 'Crafting Customised Recruitment Campaigns'},
  {'type': 'text',
   'id': 'section_3',
   'content': "These days, job advertisements don't carry a traditional approach as they used to do a decade back. Today, attracting top-tier talent requires bespoke recruitment initiatives that highlight what makes your company stand out. It's about digging deeper to understand what potential employees seek and ensuring these desires mesh with your company's ethics and goals.\n\n"},
  {'type': 'subheader',
   'id': 'section_4',
   'content': 'Building an Attractive Employer Identity'},
  {'type': 'subheader-text',
   'id': 'section_5',
   'content': 'Develop a strong employer brand that echoes your core values, workplace culture, and paths for advancement. Such branding should connect with prospective employees and set you apart in the crowd.'},
  {'type': 'subheader', 'id': 'section_6', 'content': 'Strategic Outreach'},
  {'type': 'subheader-text',
   'id': 'section_7',
   'content': 'Consider embracing a variety of platforms. They may include social media, industry gatherings, and professional circles. This will help you pinpoint and engage individuals with the necessary competencies and character.'},
  {'type': 'subheader',
   'id': 'section_8',
   'content': 'Encouraging Diversity Through Inclusive Hiring'},
  {'type': 'subheader-text',
   'id': 'section_9',
   'content': "Championing diversity and inclusivity in recruitment processes is critical. You should always aim for neutrality in job descriptions and interview setups. Furthermore, it's crucial to proactively approach candidates from diverse backgrounds."},
  {'type': 'image',
   'id': 'section_10',
   'content': {'url': 'https://picsum.photos/1200/236?random=51',
    'alt': 'image'}},
  {'type': 'header',
   'id': 'section_11',
   'content': 'Integrating Tech Innovations in Hiring'},
  {'type': 'text',
   'id': 'section_12',
   'content': "The integration of technology has transformed recruitment into a more strategic and fair process. The application of artificial intelligence (AI) for candidate evaluation streamlines hiring, ensuring decisions are free from bias. Furthermore, as mentioned earlier, social media has emerged as a crucial platform for engagement. It offers a window into an organisation's culture and values, which eventually draws in candidates aligned with these principles."},
  {'type': 'subheader',
   'id': 'section_13',
   'content': 'Innovating with AI for Fairer Hiring'},
  {'type': 'subheader-text',
   'id': 'section_14',
   'content': 'Organisations should adopt AI-driven tools to refine the screening process. This approach speeds up recruitment and simultaneously guarantees fairness. Consequently, talents from various backgrounds are considered on equal footing.'},
  {'type': 'subheader',
   'id': 'section_15',
   'content': 'Social Media as a Recruitment Catalyst'},
  {'type': 'subheader-text',
   'id': 'section_16',
   'content': "Harness the power of social platforms to broadcast your company's culture and vision. This transparency attracts professionals who resonate with your organisational values, facilitating a better match between the company and potential employees."},
  {'type': 'subheader',
   'id': 'section_17',
   'content': 'Digital Showcasing of Company Culture'},
  {'type': 'subheader-text',
   'id': 'section_18',
   'content': "Use online platforms to vividly present what it's like to work at your company. Through engaging content and interactive sessions, you can captivate the interest of prospective talents who are seeking inclusive and innovative workplaces."},
  {'type': 'header',
   'id': 'section_20',
   'content': 'Tailoring the Employee Experience'},
  {'type': 'text',
   'id': 'section_24',
   'content': "The integration of technology has transformed recruitment into a more strategic and fair process. The application of artificial intelligence (AI) for candidate evaluation streamlines hiring, ensuring decisions are free from bias. Furthermore, as mentioned earlier, social media has emerged as a crucial platform for engagement. It offers a window into an organisation's culture and values, which eventually draws in candidates aligned with these principles."},
  {'type': 'subheader',
   'id': 'section_25',
   'content': 'Moreover, tailored development initiatives'},
  {'type': 'subheader-text',
   'id': 'section_26',
   'content': "are now standard enabling employees to forge their unique trajectories in the organisation. The integration of technology has transformed recruitment into a more strategic and fair process. The application of artificial intelligence (AI) for candidate evaluation streamlines hiring, ensuring decisions are free from bias. Furthermore, as mentioned earlier, social media has emerged as a crucial platform for engagement. It offers a window into an organisation's culture and values, which eventually draws in candidates aligned with these principles."},
  {'type': 'subheader-text',
   'id': 'section_27',
   'content': "The integration of technology has transformed recruitment into a more strategic and fair process. The application of artificial intelligence (AI) for candidate evaluation streamlines hiring, ensuring decisions are free from bias. Furthermore, as mentioned earlier, social media has emerged as a crucial platform for engagement. It offers a window into an organisation's culture and values, which eventually draws in candidates aligned with these principles."}]}

import json
import re

def slugify(text):
    s = str(text).lower().strip()
    s = re.sub(r'[\s.&]+', '-', s)  # Replace whitespace, ampersands, common separators with a single hyphen
    s = re.sub(r'[^\w-]', '', s)    # Remove any character that is not a word character or a hyphen
    s = re.sub(r'--+', '-', s)      # Replace multiple hyphens with a single one
    if s.endswith("..."): # Specific case from your data
        s = s[:-3]
    s = s.strip('-')
    return s

def get_toc(json_data_full): # Pass the full JSON data
    header_template = f"""<div class="mb-4 toc-section" data-section-id="[[section_id]]">
            <a href="#[[section_id]]" data-toggle-target="[[sub_header_pointer]]" class="toc-h2-link flex items-center justify-between mt-1 mb-3 no-underline text-gray-800 hover:text-[#3533CD] transition-colors duration-200 toc-link">
                <div class="text-lg font-medium"> [[header]] </div>
                <i class="ph ph-caret-down text-xs ml-1 toc-arrow transition-transform duration-300" ></i>
            </a>
            <div id="[[sub_header_pointer]]" class="toc-subcategories hidden pl-4 mb-3 space-y-3">
                [[subcategories]]
            </div>
        </div>"""
    subheader_template = """<a href="#[[sub_section_slug]]" class="flex items-center mt-1 no-underline text-gray-600 hover:text-[#3533CD] transition-colors duration-200 toc-link border-l-2 border-gray-200 pl-3 hover:border-[#3533CD]">
                    <div class="text-sm">[[subheader]]</div>
                </a>"""
    
    dynamic_sections = json_data_full.get('dynamicSections', [])
    
    # Use a list to maintain order and structure
    processed_headers = []
    current_header_details = None

    for section in dynamic_sections:
        if section['type'] == 'header':
            header_content = section['content']
            header_slug = slugify(header_content)
            current_header_details = {
                'content': header_content,
                'slug': header_slug,
                'subheaders': []
            }
            processed_headers.append(current_header_details)
        elif section['type'] == 'subheader':
            if current_header_details: # Make sure it's under a header
                subheader_content = section['content']
                subheader_slug = slugify(subheader_content)
                current_header_details['subheaders'].append({
                    'content': subheader_content,
                    'slug': subheader_slug
                })

    toc_html_parts = []
    for header_detail in processed_headers:
        header_content = header_detail['content']
        header_slug = header_detail['slug']
        
        subcategories_html_list = []
        for sub_detail in header_detail['subheaders']:
            sub_html = subheader_template.replace('[[subheader]]', sub_detail['content'])
            sub_html = sub_html.replace("[[sub_section_slug]]", sub_detail['slug']) # Link to subheader's slug
            subcategories_html_list.append(sub_html)
        
        subcategories_str = '\n'.join(subcategories_html_list)

        # Populate header template
        header_html_part = header_template.replace('[[header]]', header_content)
        header_html_part = header_html_part.replace('[[subcategories]]', subcategories_str)
        header_html_part = header_html_part.replace('[[section_id]]', header_slug) # For href and data-section-id
        header_html_part = header_html_part.replace('[[sub_header_pointer]]', f'sub-{header_slug}') # For the collapsible div ID
        toc_html_parts.append(header_html_part)

    return '\n'.join(toc_html_parts)
def get_blog_content(json_data_full): # Pass the full JSON data
    # Templates from your original code
    text_template = """<p class="font-jakarta font-medium text-[15px] md:text-[16px] leading-[26px] md:leading-[30px] text-black" >
                [[textcontent]]
            </p>"""
    # For text that needs indentation, like section_3 or standalone subheader-text like section_27
    text_indented_template = """<p class="font-jakarta font-medium text-[15px] md:text-[16px] leading-[26px] md:leading-[30px] text-black md:ml-[2rem]" >
                [[textcontent]]
            </p>"""
    h2_template = """<h2 id="[[section_id]]" class="font-jakarta font-medium text-[22px] md:text-[28px] leading-[28px] md:leading-[30px] text-black scroll-mt-20" >
                [[h2content]]
            </h2>"""
    image_template = """<div class="w-full h-[120px] sm:h-[160px] md:h-[236px] my-8 md:my-12">
            <img src="[[imageurl]]" alt="[[imagealt]]" class="w-full h-full object-cover" />
          </div>"""
    
    # New template for subheaders, matching the expected <p><span>...</span></p> structure
    subheader_paragraph_template = """<p id="[[section_id]]" class="font-jakarta font-medium text-[15px] md:text-[16px] leading-[26px] md:leading-[30px] text-black mb-3 md:mb-4 scroll-mt-20 md:ml-[2rem]">
                <span class="font-semibold font-high text-[20px]">[[subheader_title]]<br/></span>
                [[subheader_body]]
            </p>"""

    output_html_parts = []
    sections = json_data_full.get('dynamicSections', [])
    idx = 0

    # Skip the first section if it's the summary (already handled elsewhere)
    if sections and sections[0]['id'] == 'section_1' and sections[0]['content'] == json_data_full.get('blogSummary', ''):
        idx = 1
    
    in_subheader_group_div = False

    while idx < len(sections):
        section = sections[idx]
        section_type = section['type']

        # If the current section is not a subheader type and we were in a subheader div, close it.
        if section_type not in ['subheader', 'subheader-text'] and in_subheader_group_div:
            output_html_parts.append("</div>")
            in_subheader_group_div = False

        if section_type == 'text':
            # Special styling for section_3 as per expected output
            if section['id'] == 'section_3':
                output_html_parts.append(text_indented_template.replace('[[textcontent]]', section['content']))
            else:
                output_html_parts.append(text_template.replace('[[textcontent]]', section['content']))
            idx += 1
        elif section_type == 'header':
            slug = slugify(section['content'])
            output_html_parts.append(h2_template.replace('[[h2content]]', section['content']).replace('[[section_id]]', slug))
            idx += 1
        elif section_type == 'image':
            img_content = section.get('content', {})
            output_html_parts.append(image_template.replace('[[imageurl]]', img_content.get('url', '')).replace('[[imagealt]]', img_content.get('alt', '')))
            idx += 1
        elif section_type == 'subheader':
            if not in_subheader_group_div:
                output_html_parts.append("<div>") # Start the grouping div
                in_subheader_group_div = True
            
            subheader_title = section['content']
            subheader_slug = slugify(subheader_title)
            subheader_body_content = ""
            
            # Check if next section is a paired 'subheader-text'
            if (idx + 1 < len(sections) and 
                sections[idx+1]['type'] == 'subheader-text' and
                # Basic pairing logic: e.g., section_4 (subheader) is tied to section_5 (subheader-text)
                sections[idx+1]['id'] == f"section_{int(section['id'].split('_')[1]) + 1}"):
                subheader_body_content = sections[idx+1]['content']
                idx_increment = 2 # Consumed subheader and its text
            else:
                idx_increment = 1 # Consumed only subheader

            # Populate the subheader paragraph template
            p_html = subheader_paragraph_template.replace('[[section_id]]', subheader_slug)
            p_html = p_html.replace('[[subheader_title]]', subheader_title)
            p_html = p_html.replace('[[subheader_body]]', subheader_body_content)
            output_html_parts.append(p_html)
            idx += idx_increment
            
        elif section_type == 'subheader-text':
            # This handles 'subheader-text' that was NOT consumed by a preceding 'subheader'
            # (e.g., section_27 in your data)
            if in_subheader_group_div: # This text is outside the subheader P-SPAN pattern, so close div.
                output_html_parts.append("</div>")
                in_subheader_group_div = False
            
            # Render it using the indented text template
            output_html_parts.append(text_indented_template.replace('[[textcontent]]', section['content']))
            idx += 1
        else:
            # Unknown section type, skip
            idx += 1

    # If loop finishes and we are still in a subheader div, close it
    if in_subheader_group_div:
        output_html_parts.append("</div>")

    return '\n'.join(output_html_parts)

def get_business_cards():
    return """<div class="mt-8 md:mt-16">
        <h2 class="font-jakarta font-bold text-[28px] md:text-[40px] leading-[30px] text-black mb-6 md:mb-8"> More in Business </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-8" >

          <div class="bg-white p-3 flex gap-4 h-auto min-h-[120px] md:h-[151px] transition-shadow hover:shadow-md">
            <img src="https://picsum.photos/127/121?random=1" alt="Article image" class="w-[90px] md:w-[127px] h-auto md:h-[121px] object-cover flex-none"/>
            <div class="flex flex-col">
              <span class="font-jakarta font-bold text-[10px] md:text-[12px] leading-[24px] md:leading-[30px] text-black uppercase">BUSINESS</span>
              <a
                href="#"
                class="font-jakarta font-medium text-[14px] md:text-[16px] leading-[22px] md:leading-[25px] underline text-black grow hover:text-[#3533CD]"
                >The best time to eat breakfast, according to a nutritional
                expert</a
              >
              <span
                class="font-jakarta italic font-bold text-[10px] md:text-[12px] text-black mt-auto"
                >Author -- Date</span
              >
            </div>
          </div>
          <div
            class="bg-white p-3 flex gap-4 h-auto min-h-[120px] md:h-[151px] transition-shadow hover:shadow-md"
          >
            <img
              src="https://picsum.photos/127/121?random=2"
              alt="Article image"
              class="w-[90px] md:w-[127px] h-auto md:h-[121px] object-cover flex-none"
            />
            <div class="flex flex-col">
              <span
                class="font-jakarta font-bold text-[10px] md:text-[12px] leading-[24px] md:leading-[30px] text-black uppercase"
                >BUSINESS</span
              >
              <a
                href="#"
                class="font-jakarta font-medium text-[14px] md:text-[16px] leading-[22px] md:leading-[25px] underline text-black grow hover:text-[#3533CD]"
                >Effective leadership practices for managing remote teams</a
              >
              <span
                class="font-jakarta italic font-bold text-[10px] md:text-[12px] text-black mt-auto"
                >Author</span
              >
            </div>
          </div>
          <div
            class="bg-white p-3 flex gap-4 h-auto min-h-[120px] md:h-[151px] transition-shadow hover:shadow-md"
          >
            <img
              src="https://picsum.photos/127/121?random=3"
              alt="Article image"
              class="w-[90px] md:w-[127px] h-auto md:h-[121px] object-cover flex-none"
            />
            <div class="flex flex-col">
              <span
                class="font-jakarta font-bold text-[10px] md:text-[12px] leading-[24px] md:leading-[30px] text-black uppercase"
                >BUSINESS</span
              >
              <a
                href="#"
                class="font-jakarta font-medium text-[14px] md:text-[16px] leading-[22px] md:leading-[25px] underline text-black grow hover:text-[#3533CD]"
                >How AI is transforming modern recruitment processes</a
              >
              <span
                class="font-jakarta italic font-bold text-[10px] md:text-[12px] text-black mt-auto"
                >Author</span
              >
            </div>
          </div>
          <div
            class="bg-white p-3 flex gap-4 h-auto min-h-[120px] md:h-[151px] transition-shadow hover:shadow-md"
          >
            <img
              src="https://picsum.photos/127/121?random=4"
              alt="Article image"
              class="w-[90px] md:w-[127px] h-auto md:h-[121px] object-cover flex-none"
            />
            <div class="flex flex-col">
              <span
                class="font-jakarta font-bold text-[10px] md:text-[12px] leading-[24px] md:leading-[30px] text-black uppercase"
                >BUSINESS</span
              >
              <a
                href="#"
                class="font-jakarta font-medium text-[14px] md:text-[16px] leading-[22px] md:leading-[25px] underline text-black grow hover:text-[#3533CD]"
                >The ROI of employee development programs</a
              >
              <span
                class="font-jakarta italic font-bold text-[10px] md:text-[12px] text-black mt-auto"
                >Author</span
              >
            </div>
          </div>
          <div
            class="bg-white p-3 flex gap-4 h-auto min-h-[120px] md:h-[151px] transition-shadow hover:shadow-md"
          >
            <img
              src="https://picsum.photos/127/121?random=5"
              alt="Article image"
              class="w-[90px] md:w-[127px] h-auto md:h-[121px] object-cover flex-none"
            />
            <div class="flex flex-col">
              <span
                class="font-jakarta font-bold text-[10px] md:text-[12px] leading-[24px] md:leading-[30px] text-black uppercase"
                >BUSINESS</span
              >
              <a
                href="#"
                class="font-jakarta font-medium text-[14px] md:text-[16px] leading-[22px] md:leading-[25px] underline text-black grow hover:text-[#3533CD]"
                >Building inclusive workplaces: strategies that work</a
              >
              <span
                class="font-jakarta italic font-bold text-[10px] md:text-[12px] text-black mt-auto"
                >Author</span
              >
            </div>
          </div>
          <div
            class="bg-white p-3 flex gap-4 h-auto min-h-[120px] md:h-[151px] transition-shadow hover:shadow-md"
          >
            <img
              src="https://picsum.photos/127/121?random=6"
              alt="Article image"
              class="w-[90px] md:w-[127px] h-auto md:h-[121px] object-cover flex-none"
            />
            <div class="flex flex-col">
              <span
                class="font-jakarta font-bold text-[10px] md:text-[12px] leading-[24px] md:leading-[30px] text-black uppercase"
                >BUSINESS</span
              >
              <a
                href="#"
                class="font-jakarta font-medium text-[14px] md:text-[16px] leading-[22px] md:leading-[25px] underline text-black grow hover:text-[#3533CD]"
                >The impact of corporate culture on retention rates</a
              >
              <span
                class="font-jakarta italic font-bold text-[10px] md:text-[12px] text-black mt-auto"
                >Author</span
              >
            </div>
          </div>
        </div>
      </div>"""



from static.data.html_templates import *
from static.data.db_handler import *

base_blog = BLOGS_TEMPLATE.replace('[[main_page_image]]', demo_json_data['mainImageUrl'])
base_blog = base_blog.replace('[[main_page_image_alt]]', demo_json_data['mainImageAlt'])
base_blog = base_blog.replace('[[main_page_title]]', demo_json_data['blogTitle'])
base_blog = base_blog.replace('[[author_name]]', demo_json_data['blogAuthor'])
base_blog = base_blog.replace('[[publish_date]]', demo_json_data['blogDate'])
base_blog = base_blog.replace('[[blog_summary]]', demo_json_data['blogSummary'])

toc = get_toc(demo_json_data)
base_blog = base_blog.replace('[[table_of_contents_mobile_menu]]', toc)
base_blog = base_blog.replace('[[table_of_contents_desktop_menu]]', toc)

actual_blog_content = get_blog_content(demo_json_data)
base_blog = base_blog.replace('[[actual_blog_content]]', actual_blog_content)

leader_details = get_leadership_details()
base_blog = base_blog.replace('[[leadership_spotlight_image]]', leader_details['leader_image_url'])
base_blog = base_blog.replace('[[leader_name]]', leader_details['leader_name'])
base_blog = base_blog.replace('[[leader_designation]]', leader_details['leader_designation'])
base_blog = base_blog.replace('[[leader_brief_description]]', leader_details['leader_desc'])
base_blog = base_blog.replace('[[link_to_leadership_webstories]]', leader_details['web_stories_url'])

base_blog = base_blog.replace('[[ad_banner_beside_leaderhip_spotlight]]', demo_json_data['adBannerBesideUrl'])
base_blog = base_blog.replace('[[ad_banner_under_leadership_section]]', demo_json_data['adBannerBelowUrl'])

business_cards = get_business_cards()
base_blog = base_blog.replace('[[more_in_business_posts]]', business_cards)

with open('temp.html', 'w') as f:
    f.write(base_blog)