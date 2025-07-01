from .general_elements import *
from .homepage_elements import *
from .category_page_elements import *

from ..db_handler import get_page_data
import asyncio
import time

def get_homepage():
    async def get_homepage_async():
        start_time = time.time()
        data = get_page_data("homepage")
        homepage_data = data.get("page_data", {})

        loop = asyncio.get_event_loop()
        
        # Execute all functions in parallel using thread pool
        tasks = [
            loop.run_in_executor(None, get_header),
            loop.run_in_executor(None, get_homepage_hero_section_html, homepage_data["hero_section"]),
            loop.run_in_executor(None, get_1_by_3_html, homepage_data["1_by_3_section"]),
            loop.run_in_executor(None, get_top_stories, homepage_data["top_stories_section"]),
            loop.run_in_executor(None, get_horizontal_ad_banner, homepage_data["horizontal_ad_banner"]),
            loop.run_in_executor(None, get_1_by_3_html, homepage_data["1_by_3_section_2"]),
            loop.run_in_executor(None, get_split_section, homepage_data["split_section"]),
            loop.run_in_executor(None, get_fuel_your_ambitions_html),
            loop.run_in_executor(None, get_1_by_2_by_6_html, homepage_data["one_by_two_by_six_section"]),
            loop.run_in_executor(None, get_1_by_2_by_6_html, homepage_data["one_by_two_by_six_section_2"]),
            loop.run_in_executor(None, get_ninety_percent_of_business_owners_html),
            loop.run_in_executor(None, get_footer)
        ]
        
        # Execute all tasks in parallel
        results = await asyncio.gather(*tasks)
        
        # Insert moving_banner at index 3 (after 1_by_3_section)
        total_body = results[:3] + [moving_banner] + results[3:]
        
        total_body = "\n".join(total_body)
        end_time = time.time()
        print(f"Homepage generated in {end_time - start_time:.2f} seconds")
        return EMPTY_HOMEPAGE_TEMPLATE.replace("[[total_body]]", total_body)
    return asyncio.run(get_homepage_async())


def get_category_page(category):
    async def get_category_page_async():
        start_time = time.time()
        try:
            data = get_page_data(category)
            category_data = data.get("page_data", {})

            loop = asyncio.get_event_loop()
            
            # Execute all functions in parallel using thread pool
            tasks = [
                loop.run_in_executor(None, get_header),
                loop.run_in_executor(None, get_category_header_html, category),
                loop.run_in_executor(None, get_1_by_3_html, category_data["1_by_3_section"]),
                loop.run_in_executor(None, get_horizontal_ad_banner, category_data["horizontal_ad_banner_1"]),
                loop.run_in_executor(None, get_editor_picks, category_data["editor_picks"]),
                loop.run_in_executor(None, get_top_stories_category, category_data["top_stories_section"]),
                loop.run_in_executor(None, get_1_by_2_by_6_html, category_data["one_by_two_by_six_section"]),
                loop.run_in_executor(None, get_horizontal_ad_banner, category_data["horizontal_ad_banner_2"]),
                loop.run_in_executor(None, get_fuel_your_ambitions_html),
                loop.run_in_executor(None, get_footer)
            ]
            
            # Execute all tasks in parallel
            results = await asyncio.gather(*tasks)
            
            total_body = "\n".join(results)
            end_time = time.time()
            print(f"Category page '{category}' generated in {end_time - start_time:.2f} seconds")
            return CATEGORY_PAGE_TEMPLATE.replace("[[total_body]]", total_body)

        except Exception as e:
            print(f"Error fetching data for category '{category}': {e}")
            return "error"
    
    return asyncio.run(get_category_page_async())
