import re
from html_templates import BLOGS_TEMPLATE, more_in_business_single_post_template

def parse_html_to_json(html_content):
    """
    Parse HTML-like content into a structured JSON format.
    """
    data = []
    pos = 0
    content_length = len(html_content)
    def process_text(text):
        text = text.strip()
        if not text:
            return
        paragraphs = re.split(r'\n\s*\n', text)
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if paragraph:
                paragraph = re.sub(r'\s+', ' ', paragraph)
                data.append({"text": paragraph})
    while pos < content_length:
        while pos < content_length and html_content[pos].isspace():
            pos += 1
        if pos >= content_length:
            break
        next_h2 = html_content.find('<h2>', pos)
        next_h3 = html_content.find('<h3>', pos)
        next_img = html_content.find('<img>', pos)
        next_tags = [(idx, tag_type) for idx, tag_type in 
                     [(next_h2, 'h2'), (next_h3, 'h3'), (next_img, 'img')] 
                     if idx != -1]
        if not next_tags:
            process_text(html_content[pos:])
            break
        next_tag, tag_type = min(next_tags, key=lambda x: x[0])
        if next_tag > pos:
            process_text(html_content[pos:next_tag])
        if tag_type == 'h2':
            end_h2 = html_content.find('</h2>', next_tag)
            if end_h2 != -1:
                header_text = html_content[next_tag+4:end_h2]
                data.append({"header": header_text})
                pos = end_h2 + 5  
            else:
                pos = next_tag + 4
        elif tag_type == 'h3':
            end_h3 = html_content.find('</h3>', next_tag)
            if end_h3 != -1:
                subheader_text = html_content[next_tag+4:end_h3]
                data.append({"subheader": subheader_text})
                pos = end_h3 + 5  
            else:
                pos = next_tag + 4
        elif tag_type == 'img':
            alt_start = html_content.find('<alt>', next_tag)
            alt_end = html_content.find('<alt/>', alt_start) if alt_start != -1 else -1
            img_end = html_content.find('<img/>', alt_end) if alt_end != -1 else -1
            if alt_start != -1 and alt_end != -1 and img_end != -1:
                img_url = html_content[next_tag+5:alt_start]
                alt_text = html_content[alt_start+5:alt_end]
                data.append({"image": {"url": img_url, "alt_text": alt_text}})
                pos = img_end + 6  
            else:
                pos = next_tag + 5
    result = {"data": data}
    return result


