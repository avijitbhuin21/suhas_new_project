BLOGS_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>News Page Dev</title>
    <link rel="icon" type="image/png" href="static/icon/website_icon.png" />
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/@phosphor-icons/web@2.0.3"></script>
    
    <link
    href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
    rel="stylesheet"
    />
    <link
    href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@600&family=Inter:wght@500&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,700&display=swap"
    rel="stylesheet"
    />
    
    <script>
    /* Define custom fonts in Tailwind (optional, better in tailwind.config.js) */
    tailwind.config = {
        theme: {
        extend: {
            fontFamily: {
            jakarta: ['"Plus Jakarta Sans"', "sans-serif"],
            "helvetica-now": ['"Helvetica Now Display"', "sans-serif"],
            helvetica: ['"Helvetica"', "sans-serif"],
            "ibm-plex": ['"IBM Plex Sans"', "sans-serif"],
            inter: ['"Inter"', "sans-serif"],
            },
            backgroundImage: {
            "header-banner":
                "url('digital-marketing-agency-website-banner-ad-template-lzytv.png')",
            "hero-gradient":
                "linear-gradient(0deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('https://picsum.photos/1920/1080')", // Placeholder image used for gradient bg
            "podcast-bg":
                "linear-gradient(360deg, rgba(255, 255, 255, 0) 74.02%, #FFFFFF 100%), linear-gradient(180deg, rgba(255, 255, 255, 0) 61.61%, #FFFFFF 100%), url('Your paragraph text (8).png')",
            "cta-bg":
                "linear-gradient(0deg, rgba(0, 0, 0, 0.69), rgba(0, 0, 0, 0.69)), url('Screenshot 2024-09-18 at 9.57.41\u202FPM.png')",
            "gradient-line":
                "linear-gradient(90deg, #000000 0%, #9747FF 100%)",
            },
        },
        },
    };
    </script>
    <script>
    document.addEventListener("DOMContentLoaded", function () {
        const mobileMenuButton = document.getElementById("mobile-menu-button");
        const mobileMenu = document.getElementById("mobile-menu");

        mobileMenuButton.addEventListener("click", function () {
        mobileMenu.classList.toggle("hidden");
        mobileMenuButton.classList.toggle("hamburger-active");

        if (!mobileMenu.classList.contains("hidden")) {
            mobileMenu.classList.add("slide-down");
        } else {
            mobileMenu.classList.remove("slide-down");
        }
        });
    });
    </script>
    <style>
    @media screen and (max-width: 768px) {
        .hero-text {
        font-size: 28px !important; 
        line-height: 36px !important;
        }

        .article-container {
        padding-left: 20px !important;
        padding-right: 20px !important;
        }

        .toc-container {
        padding: 10px !important;
        }
    }

    @import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@600&family=Inter:wght@500&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,700&display=swap");
    @font-face {
        font-family: "Helvetica Now Display";
        src: local("Helvetica Neue"), local("Helvetica"), local("Arial"),
        sans-serif; /* Basic fallback */
        font-weight: 700;
    }
    @font-face {
        font-family: "Helvetica";
        src: local("Helvetica Neue"), local("Helvetica"), local("Arial"),
        sans-serif; /* Basic fallback */
        font-weight: 400;
    }
    ::-webkit-scrollbar {
        display: none;
    }

    body {
        -ms-overflow-style: none;
        scrollbar-width: none;
    }
    @keyframes slideDown {
        from {
        transform: translateY(-10px);
        opacity: 0;
        }
        to {
        transform: translateY(0);
        opacity: 1;
        }
    }

    .slide-down {
        animation: slideDown 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    :root {
        --clr-dark-black: #121212;
        --clr-bdr-gray: #2a2a2a;
        --clr-white: #fff;
        --clr-primary: #9747ff;
        --clr-primary-light: #cda7ff;
        --clr-gray-800: #1e1e1e;
    }

    .mobile-menu-item {
        padding: 0.875rem 1rem;
        background: var(--clr-dark-black);
        border-bottom: solid 1px var(--clr-bdr-gray);
        color: var(--clr-white);
        cursor: pointer;
        display: flex;
        align-items: center;
        transition: background-color 0.2s ease;
    }

    .mobile-menu-item:hover {
        background-color: #1a1a1a;
    }

    .mobile-menu-item:active {
        background-color: #252525;
    }

    .item-title {
        flex-grow: 1;
        margin-left: 0.75rem;
        font-weight: 500;
    }

    .hamburger-line {
        transition: all 0.3s ease;
    }

    .hamburger-active .hamburger-line:nth-child(1) {
        transform: translateY(7px) rotate(45deg);
    }

    .hamburger-active .hamburger-line:nth-child(2) {
        opacity: 0;
    }

    .hamburger-active .hamburger-line:nth-child(3) {
        transform: translateY(-7px) rotate(-45deg);
    }

    .search-input {
        transition: all 0.2s ease;
    }

    .search-input:focus {
        box-shadow: 0 0 0 2px rgba(151, 71, 255, 0.5);
    }

    @keyframes shine {
        from {
        transform: translateX(-100%);
        }
        to {
        transform: translateX(100%);
        }
    }

    .login-btn {
        transition: all 0.2s ease;
    }

    .login-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(205, 167, 255, 0.4);
    }
    /* TOC container enhancements */
    aside .p-6 {
        scrollbar-width: thin;
        scrollbar-color: #3533cd #f5f5f5;
        scroll-behavior: smooth;
        transition: all 0.3s ease;
    }

    .toc-container {
        scrollbar-width: thin;
        scrollbar-color: #3533cd #f5f5f5;
        scroll-behavior: smooth;
        transition: all 0.3s ease;
    }

    /* Custom scrollbar for webkit browsers */
    aside .p-6::-webkit-scrollbar,
    .toc-container::-webkit-scrollbar {
        width: 6px;
    }

    aside .p-6::-webkit-scrollbar-track,
    .toc-container::-webkit-scrollbar-track {
        background: #f5f5f5;
        border-radius: 10px;
    }

    aside .p-6::-webkit-scrollbar-thumb,
    .toc-container::-webkit-scrollbar-thumb {
        background: rgba(53, 51, 205, 0.5);
        border-radius: 10px;
    }

    /* Smooth transitions for TOC links */
    .toc-link {
        transition: color 0.3s ease, font-weight 0.2s ease,
        border-color 0.3s ease;
    }

    /* Active indicator animation */
    .toc-link.text-\[\#3533CD\] {
        position: relative;
    }

    .toc-link.text-\[\#3533CD\]::after {
        content: "";
        position: absolute;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 70%;
        background-color: #3533cd;
        border-radius: 2px;
        animation: fadeIn 0.3s ease;
    }      @keyframes fadeIn {
        from {
        opacity: 0;
        }
        to {
        opacity: 1;
        }
    }      /* Mobile TOC arrow styling for better touch targets */
    @media screen and (max-width: 1023px) {
        .toc-arrow {
        padding: 8px;
        margin: -8px;
        cursor: pointer;
        border-radius: 4px;
        transition: background-color 0.2s ease;
        position: relative;
        z-index: 10;
        }
        
        .toc-arrow:hover {
        background-color: rgba(53, 51, 205, 0.1);
        }
    }
    </style>
</head>
<body class="font-poppins bg-white text-gray-800">
    <header class="w-full bg-black relative">
    
        <div class="hidden lg:flex flex-row justify-center items-center px-20 py-[10px] gap-[70px] h-[113px]">
            <img src="static/images/header_logo.png" alt="Brands Out Loud Logo" class="w-20 h-20 flex-shrink-0">
            <nav class="flex flex-col items-stretch w-[700px] h-[93px] py-[14px] px-[18px] gap-[10px]">
                <div class="flex flex-row justify-end items-center w-full gap-[60px] px-[30px]">
                    <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Careers </a>
                    <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Podcast </a>
                    <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Register </a>
                    <a href="#" class="bg-[#CDA7FF] rounded-[2px] px-2.5 py-0.5 text-[#0D0D0D] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Login </a>
                </div>
                <div class="w-full h-[1px] bg-gradient-to-r from-black to-[#9747FF]"></div>
                <div class="flex flex-row justify-end items-center w-full gap-[60px] px-2">
                    <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Newsletters </a>
                    <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Magazine </a>
                    
                    <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Startups </a>
                    <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Business </a>
                </div>
            </nav>
        </div>

    
    <div class="flex lg:hidden items-center h-[68px] w-full bg-[#0D0D0D]">

        <button id="mobile-menu-button" aria-label="Toggle Menu" class="h-full px-4 flex flex-col justify-center items-center space-y-[5px] bg-transparent focus:outline-none transition-colors duration-200 ease-in-out">
        <span class="hamburger-line block w-6 h-[2px] bg-white rounded-full"></span>
        <span class="hamburger-line block w-6 h-[2px] bg-white rounded-full"></span>
        <span class="hamburger-line block w-6 h-[2px] bg-white rounded-full"></span>
        </button>

        <div class="h-full flex items-center px-3 flex-shrink-0">
        <img src="static/icon/website_icon.png" alt="Brands Out Loud Logo" class="h-10 w-auto"/>
        </div>

        <div class="flex-grow px-3">
        <div class="relative">
            <input type="text" placeholder="Search..." class="search-input w-full bg-[#1e1e1e] text-white text-sm rounded-full pl-10 pr-4 py-2.5 border border-[#2a2a2a] focus:outline-none focus:border-[#9747FF] transition-all"/>
            <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
            <i class="ph ph-magnifying-glass text-gray-400 text-lg"></i>
            </div>
        </div>
        </div>
    </div>

    
    <div id="mobile-menu" class="hidden lg:hidden absolute top-[68px] left-0 w-full bg-[#121212] z-50 shadow-lg border-t border-[#2a2a2a] overflow-hidden">
        <div class="">
        <div class="px-4 py-3">
            <a href="#" class="login-btn block w-full text-center bg-gradient-to-r from-[#9747FF] to-[#CDA7FF] rounded-full px-4 py-2.5 text-white font-medium text-sm shadow-lg hover:-translate-y-0.5 transition-all duration-300 relative overflow-hidden">
            <span class="relative z-10 flex items-center justify-center gap-2">
                <i class="ph ph-sign-in text-lg"></i>
                <span>Login</span>
            </span>
            <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent -translate-x-full animate-[shine_2s_infinite]"></div>
            </a>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-book-open text-white text-lg"></i>
            <span class="item-title">Magazine</span>
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-lightning text-white text-lg"></i>
            <span class="item-title">Startups</span>
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-envelope-open text-white text-lg"></i>
            <span class="item-title">Newsletters</span>
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-newspaper text-white text-lg"></i>
            <span class="item-title">Podcast</span>
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-buildings text-white text-lg"></i>
            <span class="item-title">Business</span>
            <i class="ph ph-caret-right"></i>
        </div>

        <div class="mobile-menu-item">
            <i class="ph ph-briefcase text-white text-lg"></i>
            <span class="item-title">Careers</span>
            <i class="ph ph-caret-right"></i>
        </div>
        </div>
    </div>
    </header>
    
    <main class="w-full px-4 sm:px-8 md:px-[65px] py-[21px] relative article-container">
        <article class="mb-8 md:mb-12 relative">
            <div class="relative w-full h-[300px] md:h-[478px]">
                <div class="absolute inset-0 bg-hero-gradient bg-cover bg-center"></div>
                <img src="[[main_page_image]]" alt="[[main_page_image_alt]]" class="w-full h-full object-cover opacity-40 mix-blend-multiply"/>
            </div>

            <div class="relative bg-white md:w-full w-[420px] md:ml-[6.85rem] ml-[-1.5rem] max-w-[1175px] h-auto mx-auto -mt-[40px] sm:-mt-[60px] md:-mt-[76px] p-4 sm:p-6 md:p-8 z-10">
                <h1 class="font-jakarta font-medium text-[28px] sm:text-[34px] md:text-[42px] lg:text-[50px] leading-[1.2] md:leading-[1.25] capitalize text-black mb-3 md:mb-4 text-center hero-text">
                    [[main_page_title]]
                </h1>
                <div class="flex justify-center items-center gap-2 text-center mb-4">
                    <p class="font-jakarta font-semibold text-[11px] sm:text-[12px] md:text-[14px] leading-[100.9%] text-black"> [[author_name]] </p>
                    <span class="text-black">- -</span>
                    <p class="font-jakarta font-normal text-[11px] sm:text-[12px] md:text-[14px] leading-[100.9%] text-black"> [[publish_date]] </p>
                </div>
            </div>

            <p class="font-jakarta font-medium text-[18px] md:text-[22px] leading-[26px] md:leading-[30px] text-[#636363] text-center mt-6 md:mt-8 max-w-[1175px] mx-auto px-2 md:px-0">
            [[page_summary]]
            </p>

            <hr class="border-t border-black my-8 md:my-12 w-full md:w-[90%] lg:w-[87rem] mx-auto"/>
        </article>
    
        <div class="block lg:hidden px-4 mt-8">
            <div class="relative toc-container p-5 bg-white rounded-xl border-gray-100">
                <h2 class="text-xl font-bold text-[#3533CD] mb-4 border-b pb-3">Table of Contents</h2>
                
                <div class="mb-3 toc-section" data-section-id="crafting-customised-recruitment-campaigns">
                    <a href="#crafting-customised-recruitment-campaigns" data-toggle-target="#sub-crafting-customised-recruitment-campaigns" class="toc-h2-link flex items-center justify-between mt-1 mb-3 no-underline text-gray-800 hover:text-[#3533CD] transition-colors duration-200 toc-link">
                        <div class="text-base font-medium">Crafting Customised Recruitment Campaigns</div>
                        <i class="ph ph-caret-down text-xs ml-1 toc-arrow transition-transform duration-300"></i>
                    </a>
                    
                    <div id="sub-crafting-customised-recruitment-campaigns" class="toc-subcategories hidden pl-4 mb-3 space-y-2">
                        <a href="#building-attractive-employer-identity" class="flex items-center mt-1 no-underline text-gray-600 hover:text-[#3533CD] transition-colors duration-200 toc-link border-l-2 border-gray-200 pl-3 hover:border-[#3533CD]">
                            <div class="text-sm">Building an Attractive Employer Identity</div>
                        </a>
                        <a href="#strategic-outreach" class="flex items-center mt-1 no-underline text-gray-600 hover:text-[#3533CD] transition-colors duration-200 toc-link border-l-2 border-gray-200 pl-3 hover:border-[#3533CD]">
                            <div class="text-sm">Strategic Outreach</div>
                        </a>
                        <a href="#encouraging-diversity" class="flex items-center mt-1 no-underline text-gray-600 hover:text-[#3533CD] transition-colors duration-200 toc-link border-l-2 border-gray-200 pl-3 hover:border-[#3533CD]">
                            <div class="text-sm">Encouraging Diversity Through Inclusive Hiring</div>
                        </a>
                    </div>
                </div>
                
                <div class="mb-3 toc-section" data-section-id="integrating-tech-innovations-in-hiring">
                    <a href="#integrating-tech-innovations-in-hiring" data-toggle-target="#sub-integrating-tech-innovations-in-hiring" class="toc-h2-link flex items-center justify-between mt-1 mb-3 no-underline text-gray-800 hover:text-[#3533CD] transition-colors duration-200 toc-link">
                        <div class="text-base font-medium">Integrating Tech Innovations in Hiring</div>
                        <i class="ph ph-caret-down text-xs ml-1 toc-arrow transition-transform duration-300"></i>
                    </a>
                    
                    <div id="sub-integrating-tech-innovations-in-hiring" class="toc-subcategories hidden pl-4 mb-3 space-y-2">
                        <a href="#innovating-with-ai" class="flex items-center mt-1 no-underline text-gray-600 hover:text-[#3533CD] transition-colors duration-200 toc-link border-l-2 border-gray-200 pl-3 hover:border-[#3533CD]">
                            <div class="text-sm">Innovating with AI for Fairer Hiring</div>
                        </a>
                        <a href="#social-media-catalyst" class="flex items-center mt-1 no-underline text-gray-600 hover:text-[#3533CD] transition-colors duration-200 toc-link border-l-2 border-gray-200 pl-3 hover:border-[#3533CD]">
                            <div class="text-sm">Social Media as a Recruitment Catalyst</div>
                        </a>
                        <a href="#digital-showcasing" class="flex items-center mt-1 no-underline text-gray-600 hover:text-[#3533CD] transition-colors duration-200 toc-link border-l-2 border-gray-200 pl-3 hover:border-[#3533CD]">
                            <div class="text-sm">Digital Showcasing of Company Culture</div>
                        </a>
                    </div>
                </div>
                
                <div class="mb-3 toc-section" data-section-id="tailoring-the-employee-experience">
                    <a href="#tailoring-the-employee-experience" data-toggle-target="#sub-tailoring-the-employee-experience" class="toc-h2-link flex items-center justify-between mt-1 mb-3 no-underline text-gray-800 hover:text-[#3533CD] transition-colors duration-200 toc-link">
                        <div class="text-base font-medium">Tailoring the Employee Experience</div>
                        <i class="ph ph-caret-down text-xs ml-1 toc-arrow transition-transform duration-300"></i>
                    </a>
                    
                    <div id="sub-tailoring-the-employee-experience" class="toc-subcategories hidden pl-4 mb-3 space-y-2">
                        <a href="#tailored-development-initiatives" class="flex items-center mt-1 no-underline text-gray-600 hover:text-[#3533CD] transition-colors duration-200 toc-link border-l-2 border-gray-200 pl-3 hover:border-[#3533CD]">
                            <div class="text-sm">Moreover, tailored development initiatives...</div>
                        </a>
                    </div>
                </div>
                
                <div class="mt-6 space-y-4 border-t pt-5">
                    <button class="w-full h-[45px] bg-[#3533CD] rounded-xl flex items-center justify-center text-white font-jakarta font-medium text-[16px] leading-[120%] hover:bg-opacity-90 transition-colors shadow-md">
                        <i class="ph ph-download mr-2"></i>Download Article as PDF
                    </button>
                    <div class="flex items-center flex-wrap">
                        <div class="relative inline-flex items-center justify-center gap-2 bg-[#3533CD] rounded-xl h-[45px] px-4 cursor-pointer hover:bg-opacity-90 transition-colors shadow-md">
                            <span class="text-white font-jakarta font-medium text-[16px] leading-[120%] text-center" style="width: 7rem">
                                <i class="ph ph-share-network mr-2"></i>Share
                            </span>
                        </div>
                        <div class="flex space-x-3 ml-3">
                            <img src="static/images/whatsapp_logo.png" alt="WhatsApp" class="w-[35px] h-[35px] object-contain hover:opacity-80 transition-opacity"/>
                            <img src="static/images/insta_logo.png" alt="Instagram" class="w-[35px] h-[35px] object-contain hover:opacity-80 transition-opacity"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    
    
    
    """