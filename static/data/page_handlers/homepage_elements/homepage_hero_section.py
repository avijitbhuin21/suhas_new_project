
def get_homepage_hero_section_html(data: dict):
    HERO_SECTION_TEMPLATE = f"""<section class="w-full py-6 px-4 md:px-8">
        
        <div class="flex flex-col md:flex-row gap-6 md:gap-8 max-w-7xl mx-auto">
            
            <article class="flex flex-col w-full md:w-3/5">
                
                <div class="w-full aspect-video bg-cover bg-center relative  overflow-hidden">
                      <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                      <div class="w-full h-full bg-cover bg-center  bg-[url({data['main_image_url']})] ">
                      </div>
                      
                 </div>
                 
                 <div class="mt-3">
                    <div class="font-jakarta font-normal text-xs text-gray-600 mb-1">{data['main_post_author']} - {data['main_post_date']}</div>
                    <h2 class="font-jakarta font-medium text-2xl md:text-[36px] leading-tight capitalize text-gray-900">{data['main_post_title']}</h2>
                </div>
            </article>

            
             <div class="grid grid-cols-2 gap-4 md:gap-x-4 md:gap-y-6 w-full md:w-2/5 mt-6 md:mt-0">
                 
                 <article class="flex flex-col">
                     <div class="w-full aspect-video bg-cover bg-center relative  overflow-hidden">
                          <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
                          <div class="w-full h-full bg-cover bg-center  bg-[url({data['right_panel_post_1_image_url']})] "></div>
                      </div>
                     <div class="mt-2">
                        <div class="font-jakarta font-normal text-[10px] text-gray-500 mb-0.5">{data['right_panel_post_1_author']} - {data['right_panel_post_1_date']}</div>
                        <h3 class="font-jakarta font-medium text-sm leading-snug capitalize text-gray-800">{data['right_panel_post_1_title']}</h3>
                    </div>
                 </article>
                 
                 <article class="flex flex-col">
                      <div class="w-full aspect-video bg-cover bg-center relative  overflow-hidden">
                           <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
                           <div class="w-full h-full bg-cover bg-center  bg-[url({data['right_panel_post_2_image_url']})] "></div>
                       </div>
                      <div class="mt-2">
                        <div class="font-jakarta font-normal text-[10px] text-gray-500 mb-0.5">{data['right_panel_post_2_author']} - {data['right_panel_post_2_date']}</div>
                        <h3 class="font-jakarta font-medium text-sm leading-snug capitalize text-gray-800">{data['right_panel_post_2_title']}</h3>
                    </div>
                 </article>
                 
                 <article class="flex flex-col col-span-2 mt-2 md:mt-0">
                      <div class="w-full h-40 bg-cover bg-center relative overflow-hidden"> 
                           <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
                           <div class="w-full h-full bg-cover bg-center  bg-[url({data['right_panel_post_3_image_url']})] "></div>
                       </div>
                     <div class="mt-2">
                        <div class="font-jakarta font-normal text-xs text-gray-600 mb-1">{data['right_panel_post_3_author']} - {data['right_panel_post_3_date']}</div>
                        <h2 class="font-jakarta font-medium text-xl md:text-[24px] leading-tight capitalize text-gray-900">{data['right_panel_post_3_title']}</h2>
                    </div>
                 </article>
             </div>
        </div>
    </section>"""
    
    return HERO_SECTION_TEMPLATE