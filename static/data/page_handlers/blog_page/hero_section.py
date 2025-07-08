

def get_blog_hero_section(data:dict):
    return f"""<article class="mb-8 md:mb-12 relative">
            <div class="relative w-full h-[300px] md:h-[478px]">
                <div class="absolute inset-0 bg-hero-gradient bg-cover bg-center"></div>
                <img src="{data['mainImageUrl']}" alt="{data['mainImageAlt']}" class="w-full h-full object-cover opacity-40 mix-blend-multiply"/>
            </div>
            <div class="relative bg-white md:w-full w-[420px] md:ml-[6.85rem] ml-[-1.5rem] max-w-[1175px] h-auto mx-auto -mt-[40px] sm:-mt-[60px] md:-mt-[76px] p-4 sm:p-6 md:p-8 z-10">
            <h1 class="font-jakarta font-medium text-[28px] sm:text-[34px] md:text-[42px] lg:text-[50px] leading-[1.2] md:leading-[1.25] capitalize text-black mb-3 md:mb-4 text-center hero-text">
                {data['blogTitle']}
            </h1>
            <div class="flex justify-center items-center gap-2 text-center mb-4">
                <p class="font-jakarta font-semibold text-[11px] sm:text-[12px] md:text-[14px] leading-[100.9%] text-black"> {data['blogAuthor']} </p>
                <span class="text-black">- -</span>
                <p class="font-jakarta font-normal text-[11px] sm:text-[12px] md:text-[14px] leading-[100.9%] text-black"> {data['blogDate']} </p>
            </div>
            </div>
            <p class="font-jakarta font-medium text-[18px] md:text-[22px] leading-[26px] md:leading-[30px] text-[#636363] text-center mt-6 md:mt-8 max-w-[1175px] mx-auto px-2 md:px-0">
            {data['blogSummary']}
            </p>
            <hr class="border-t border-black my-8 md:my-12 w-full md:w-[90%] lg:w-[87rem] mx-auto"/>
        </article>"""