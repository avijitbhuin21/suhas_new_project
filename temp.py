<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page Recreation (Tailwind)</title>
    <!-- Include Tailwind CSS (Use CDN for development, replace with build process for production) -->
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <!-- Consider reducing font weights/families if not all are used for optimization -->
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=IBM+Plex+Sans:wght@600&family=Inter:wght@500&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,800&family=Roboto:wght@500&display=swap" rel="stylesheet">
     <!-- Load Helvetica Now Display font if available (add font-face or ensure user has it) -->
     <!-- For demonstration, we rely on the fallback defined in Tailwind config -->
<!-- Minimal Custom CSS for things Tailwind doesn't handle easily -->
<style>
    @media screen and (min-width: 1024px) {
        body {
            transform: scale(1.3248);
            transform-origin: 0 0;
            width: 75.5%;
        }
    }

    .gradient-text {
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-fill-color: transparent;
        display: inline-block; 
    }

    .strip-startups { background-image: linear-gradient(93.43deg, #000000 6.93%, #3533CD 94.41%); }
    .strip-ai { background-image: linear-gradient(211.98deg, #000000 19.22%, #3533CD 94.53%); }
    .strip-business { background-image: linear-gradient(105.57deg, #000000 2.6%, #3533CD 60.9%); }
    .strip-entrepreneur { background-image: linear-gradient(90.82deg, #000000 3.28%, #3533CD 140.89%); }
    .strip-events { background-image: linear-gradient(260.78deg, #000000 43.02%, #3533CD 106.67%); }
    .strip-brands { background-image: linear-gradient(104.28deg, #000000 3.4%, #3533CD 101.3%); }
    .strip-trends { background-image: linear-gradient(264.46deg, #000000 -20.15%, #3533CD 54.42%); }
    .podcast-title-gradient { background: linear-gradient(269.15deg, #000000 47.22%, #3533CD 97.69%); }
    .hero-title-gradient { background: linear-gradient(90deg, #FFFFFF 0%, #3533CD 100%); }
    .footer-italic-gradient { background: linear-gradient(90deg, #C4C3FF 0%, #10E2FF 100%); }

    .button-icon-plus-shape::before,
    .button-icon-plus-shape::after {
        content: '';
        position: absolute;
        background-color: currentColor; 
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }
    .button-icon-plus-shape::before { width: 12px; height: 2px; }
    .button-icon-plus-shape::after { width: 2px; height: 12px; }

    .button-icon-union-shape {
         background: currentColor; 

    }

     .location-input-wrapper::after {
        content: '';
        position: absolute;
        width: 0; height: 0;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 6px solid #414141; 
        right: 15px; 
        top: 50%;
        transform: translateY(-50%);
        pointer-events: none; 
    }

    input[type="checkbox"]:checked {
        background-color: #3533CD;
        border-color: #3533CD;
        background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e");
        background-size: 100% 100%;
        background-position: center;
        background-repeat: no-repeat;
    }
</style>

<script>
  tailwind.config = {
    theme: {
      extend: {
        fontFamily: {

          'jakarta': ['"Plus Jakarta Sans"', 'sans-serif'],
          'helvetica': ['"Helvetica Now Display"', 'Arial', 'sans-serif'], 
          'dm': ['"DM Sans"', 'sans-serif'],
          'ibm-plex': ['"IBM Plex Sans"', 'sans-serif'],
          'inter': ['"Inter"', 'sans-serif'],
          'roboto': ['"Roboto"', 'sans-serif'],
          'sans': ['"Plus Jakarta Sans"', 'sans-serif'], 
        },
        colors: {
          'bol-purple': '#3533CD',
          'bol-purple-light': '#C4C3FF',
          'bol-black': '#0D0D0D',
          'bol-gray': '#B8C2CE',

        },
        spacing: { 
          '1.5px': '1.5px',
          '13px': '13px',
        },
        fontSize: { 
           '10px': '10px',
        },
         lineHeight: { 
           '13px': '13px',
        },
        animation: {
          marquee: 'marquee 30s linear infinite',
        },
        keyframes: {
          marquee: {
            '0%': { transform: 'translateX(0%)' },
            '100%': { transform: 'translateX(-50%)' }, 
          }
        }
      }
    }
  }
</script>
</head>
<body class="font-jakarta bg-white text-bol-black"> <!-- Set default font and text color -->
<div class="flex flex-col items-center w-full max-w-[1440px] mx-auto bg-white overflow-x-hidden relative">

    <!-- Order 0: Header Banner -->
    <!-- <section class="flex flex-col justify-center items-center px-[30px] sm:px-[100px] lg:px-[200px] py-[10px] gap-[13px] w-full h-[157px] bg-cover bg-center bg-[url(static/images/header.png)]">
    </section> -->

    <!-- Order 1: Main Header (Combined Desktop/Mobile) -->
    <header class="w-full bg-black relative">
        <!-- Desktop Header -->
        <div class="hidden lg:flex flex-row justify-center items-center px-20 py-[10px] gap-[70px] h-[113px]">
        <!-- Logo -->
        <img src="static/images/header_logo.png" alt="Brands Out Loud Logo" class="w-20 h-20 flex-shrink-0">

        <!-- Navigation Area -->
        <nav class="flex flex-col items-stretch w-[700px] h-[93px] py-[14px] px-[18px] gap-[10px]">
        <!-- Top Nav Row -->
        <div class="flex flex-row justify-end items-center w-full gap-[60px] px-[30px]">
        <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0">Careers</a>
        <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0">Editorial</a>
        <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0">Register</a>
        <a href="#" class="bg-[#CDA7FF] rounded-[2px] px-2.5 py-0.5 text-[#0D0D0D] font-bold text-[10px] text-center flex-shrink-0">Login</a>
        </div>
        <!-- Separator Line -->
        <div class="w-full h-[1px] bg-gradient-to-r from-black to-[#9747FF]"></div>
        <!-- Bottom Nav Row -->
        <div class="flex flex-row justify-end items-center w-full gap-[60px] px-2">
        <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0">Newsletters</a>
        <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0">Magazine</a>
        <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0">Entrepreneurship</a>
        <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0">Startups</a>
        <a href="#" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0">Business</a>
        </div>
        </nav>
        </div>

        <!-- Mobile Header -->
        <div class="flex lg:hidden justify-between items-center h-full h-[60px]">
        <!-- Logo Section -->
        <div class="flex items-center w-full"> <!-- Added w-full to allow span to take full width -->
        <span class="flex-grow h-[60px] text-white text-[2rem] font-bold whitespace-nowrap text-center bg-gradient-to-r from-black to-bol-purple flex items-center justify-center">Brands Out Loud</span>

        </div>

        <!-- Hamburger Button -->
        <button id="mobile-menu-button" aria-label="Toggle Menu" class="h-full px-4 flex flex-col justify-center items-center space-y-[6px] bg-black hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500 flex-shrink-0"> <!-- Added flex-shrink-0 -->
        <span class="block w-8 h-[3px] bg-white rounded-sm"></span>
        <span class="block w-8 h-[3px] bg-white rounded-sm"></span>
        <span class="block w-8 h-[3px] bg-white rounded-sm"></span>
        </button>
        </div>

        <!-- Mobile Menu (Hidden by default) -->
        <div id="mobile-menu" class="hidden lg:hidden absolute top-[58px] left-0 w-full bg-black z-50 py-4 shadow-lg">
        <div class="grid grid-cols-2 gap-x-4 gap-y-2 px-6">
        <!-- First Column -->
        <div class="flex flex-col">
        <h3 class="text-white font-bold text-sm mb-2 border-b border-gray-700 pb-1">Main Menu</h3>
        <a href="#" class="text-white font-bold text-sm py-2">Careers</a>
        <a href="#" class="text-white font-bold text-sm py-2">Editorial</a>
        <a href="#" class="text-white font-bold text-sm py-2">Register</a>
        <a href="#" class="bg-[#CDA7FF] rounded-[2px] px-2.5 py-2 text-[#0D0D0D] font-bold text-sm mb-4 inline-block w-max">Login</a>
        </div>

        <!-- Second Column -->
        <div class="flex flex-col">
        <h3 class="text-white font-bold text-sm mb-2 border-b border-gray-700 pb-1">Categories</h3>
        <a href="#" class="text-[#C4C3FF] font-bold text-sm py-2">Newsletters</a>
        <a href="#" class="text-[#C4C3FF] font-bold text-sm py-2">Magazine</a>
        <a href="#" class="text-[#C4C3FF] font-bold text-sm py-2">Entrepreneurship</a>
        <a href="#" class="text-[#C4C3FF] font-bold text-sm py-2">Startups</a>
        <a href="#" class="text-[#C4C3FF] font-bold text-sm py-2">Business</a>
        </div>
        </div>
        </div>
    </header>

    <!-- Script for mobile menu toggle functionality -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');
        
        mobileMenuButton.addEventListener('click', function() {
            // Toggle the mobile menu visibility
            if (mobileMenu.classList.contains('hidden')) {
            mobileMenu.classList.remove('hidden');
            mobileMenu.classList.add('block');
            } else {
            mobileMenu.classList.add('hidden');
            mobileMenu.classList.remove('block');
            }
        });
        });
    </script>

    <!-- Order 2: News Section -->
    <section class="w-full h-auto md:h-[609px] relative py-5 md:py-0 px-4 md:px-0">
        <!-- Desktop-only Lines absolutely positioned relative to this section -->
        <div class="absolute w-[279px] h-0 left-[358px] top-[244px] border-t border-[#B8C2CE] hidden md:block"></div>
        <div class="absolute w-[279px] h-0 left-[358px] top-[413px] border-t border-[#B8C2CE] hidden md:block"></div>
        <!-- Container for posts -->
        <!-- Using Grid for mobile, explicit positioning for desktop -->
        <div class="grid grid-cols-1 md:grid-cols-[minmax(0,_782px)_1fr] gap-4 md:gap-[15px] w-full md:w-[1365px] md:h-[533px] md:relative md:left-[38px] md:top-[19px]">
            <!-- Post 1 (Large) -->
            <article class="relative w-full md:h-[529px]">
                <!-- Image with Gradient Overlay -->
                <div class="w-full h-[300px] md:h-[394px] bg-cover bg-center relative">
                     <div class="absolute inset-0 bg-[linear-gradient(0deg,rgba(0,0,0,0.6),rgba(0,0,0,0.6))]"></div>
                     <div class="w-full h-full bg-cover bg-center bg-[url(https://picsum.photos/seed/post1large/782/394)]"></div>
                 </div>
                 <div class="p-4 md:p-0 md:absolute md:w-[168px] md:h-[12px] md:left-[29.17px] md:top-[421px] mt-2 md:mt-0 font-jakarta font-normal text-[12px] leading-[1.1] text-[#171717]">Craig Bator - 27 Dec 2020</div>
                <h2 class="p-4 md:p-0 md:absolute md:w-[570px] md:h-auto md:left-[29px] md:top-[439px] font-jakarta font-medium text-2xl md:text-[36px] leading-tight md:leading-[45px] capitalize text-[#171717]">After all is said and done, more is done</h2>
            </article>

            <!-- Right side posts container -->
             <div class="grid grid-cols-2 md:grid-cols-2 gap-4 md:gap-y-[24px] md:gap-x-[15px] md:h-full">
                 <!-- Post 2 (Small Top Left on desktop grid) -->
                 <article class="relative w-full md:h-[247px]">
                     <div class="w-full h-[175px] bg-cover bg-center relative">
                          <div class="absolute inset-0 bg-[linear-gradient(0deg,rgba(0,0,0,0.4),rgba(0,0,0,0.4))]"></div>
                          <div class="w-full h-full bg-cover bg-center bg-[url(https://picsum.photos/seed/post2small/274/175)]"></div>
                      </div>
                     <div class="p-2 md:p-0 md:absolute md:w-[140px] md:h-[10px] md:left-[29.33px] md:top-[195px] mt-1 md:mt-0 font-jakarta font-normal text-[10px] leading-[1] text-[#313131]">Craig Bator - 27 Dec 2020</div>
                     <h3 class="p-2 md:p-0 md:absolute md:w-[215px] md:h-auto md:left-[29px] md:top-[211px] font-jakarta font-medium text-sm md:text-[14px] leading-[18px] capitalize text-[#313131]">They’re back! Kennedy Darling named to return to</h3>
                 </article>
                 <!-- Post 3 (Small Top Right on desktop grid) -->
                 <article class="relative w-full md:h-[247px]">
                      <div class="w-full h-[175px] bg-cover bg-center relative">
                           <div class="absolute inset-0 bg-[linear-gradient(0deg,rgba(0,0,0,0.4),rgba(0,0,0,0.4))]"></div>
                           <div class="w-full h-full bg-cover bg-center bg-[url(https://picsum.photos/seed/post3small/274/175)]"></div>
                       </div>
                      <div class="p-2 md:p-0 md:absolute md:w-[140px] md:h-[10px] md:left-[29px] md:top-[195px] mt-1 md:mt-0 font-jakarta font-normal text-[10px] leading-[1] text-[#000000]">Craig Bator - 27 Dec 2020</div>
                      <h3 class="p-2 md:p-0 md:absolute md:w-[192px] md:h-auto md:left-[29px] md:top-[211px] font-jakarta font-medium text-sm md:text-[14px] leading-[18px] capitalize text-[#000000]">Swiss authorities say Uber drivers should</h3>
                 </article>
                 <!-- Post 4 (Medium Bottom Right on desktop grid) - Spans 2 cols on mobile & desktop -->
                 <article class="relative w-full md:h-[262px] col-span-2">
                      <div class="w-full h-[161px] bg-cover bg-center relative">
                           <div class="absolute inset-0 bg-[linear-gradient(0deg,rgba(0,0,0,0.4),rgba(0,0,0,0.4))]"></div>
                           <div class="w-full h-full bg-cover bg-center bg-[url(https://picsum.photos/seed/post4medium/566/161)]"></div>
                       </div>
                     <div class="p-2 md:p-0 md:absolute md:w-[168px] md:h-[12px] md:left-[29.33px] md:top-[184px] mt-1 md:mt-0 font-jakarta font-normal text-[12px] leading-[1.1] text-[#000000]">Craig Bator - 27 Dec 2020</div>
                     <h2 class="p-2 md:p-0 md:absolute md:w-[363px] md:h-auto md:left-[29px] md:top-[202px] font-jakarta font-medium text-lg md:text-[24px] leading-[30px] capitalize text-[#000000]">Tourism in Dubai is booming by international tourist</h2>
                 </article>
             </div>
        </div>
    </section>

    <!-- Order 3: Trending News Section -->
    <section class="w-full h-auto md:h-[609px] relative overflow-hidden my-5 md:my-0">
        <div class="absolute inset-0 w-full h-full bg-gradient-to-br from-[#3533CD] via-black to-black md:bg-[linear-gradient(125.25deg,_#3533CD_0.4%,_#000000_47.94%)] rounded-none md:rounded-[6px]"></div>
        <div class="relative w-full h-full z-10 p-4 md:p-0 md:pl-[44.49px] md:pt-[29px] grid grid-cols-1 md:grid-cols-2 gap-6">
             <!-- Left Column: Title + 3 Small Posts -->
             <!-- Added divide-y for separator lines -->
             <div class="flex flex-col gap-4">
                 <h2 class="w-auto md:w-[232.35px] h-auto md:h-[38px] font-jakarta font-bold text-2xl md:text-[28px] leading-[38px] text-white pb-4">Trending News</h2>
                 <!-- Post 1 -->
                 <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5">
                     <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/racehorse/289/150)] flex-shrink-0"></div>
                     <div class="flex flex-col justify-center">
                          <div class="w-auto md:w-[137.18px] h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">Race98 - 03 June 2023</div>
                          <h3 class="w-auto md:w-[302.79px] h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white mb-2">6-Year-Old Horse Dies at Belmont Park After Race Injury</h3>
                          <p class="w-auto md:w-[295.38px] h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">NEW YORK—A 6-year-old horse died after being injured in a race at Belmont Park ahead of next week’s</p>
                     </div>
                 </article>
                 <!-- Post 2 -->
                <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5">
                     <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/cyclist/289/150)] flex-shrink-0"></div>
                     <div class="flex flex-col justify-center">
                         <div class="w-auto md:w-[135.95px] h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">Jony.Ls - 03 June 2023</div>
                         <h3 class="w-auto md:w-[302.79px] h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white capitalize mb-2">Savilia Blunk Embraces Longer Season with World Cup</h3>
                         <p class="w-auto md:w-[295.38px] h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">Last year, Savilia Blunk took a more conservative approach to her first season as an Elite Class athlete, skipping some</p>
                     </div>
                 </article>
                <!-- Post 3 -->
                <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5">
                     <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/boxing/289/150)] flex-shrink-0"></div>
                     <div class="flex flex-col justify-center">
                         <div class="w-auto md:w-[127.3px] h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">King.F - 03 June 2023</div>
                         <h3 class="w-auto md:w-[302.79px] h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white mb-2">Ryan Garcia is fighting again, this time on social media</h3>
                         <p class="w-auto md:w-[295.38px] h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">Boxing star Ryan Garcia and his promoter, Hall of Fame fighter Oscar De La Hoya, reignited their war of words via Twitter on</p>
                     </div>
                 </article>
             </div>

            <!-- Right Column: Large Post -->
            <div class="relative w-full h-auto md:w-[640.07px] md:h-[531.62px] md:absolute md:left-[742px] md:top-[41px]">
                <div class="relative w-full h-[250px] md:absolute md:inset-0 md:w-[640px] md:h-[395px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/trendinglarge/640/395)]"></div>
                 <div class="absolute left-[18px] top-[25px] border border-[#EBEEF3] rounded-[3px] bg-black/30 px-3 py-1 inline-block z-10">
                     <span class="font-dm font-medium text-[14px] md:text-[20px] leading-[26px] capitalize text-[#EBEEF3]">Business</span>
                 </div>
                 <div class="relative mt-4 px-4 font-dm font-normal text-sm leading-[1.1] text-white md:absolute md:w-[336.67px] md:h-auto md:left-[11px] md:top-[421px] md:text-[18px] md:z-10 md:mt-0 md:px-0">Debits - 03 June 2023</div> <!-- Matched meta styling/position -->
                 <h2 class="relative mt-1 px-4 pb-4 font-jakarta font-bold text-xl leading-tight capitalize text-white md:absolute md:w-[629.07px] md:h-auto md:left-[11px] md:top-[451.5px] md:text-[32px] md:leading-[40px] md:text-white md:z-10 md:mt-0 md:px-0 md:pb-0">DISCOVER THE MEMBER BENEFITS OF BOL BUSINESS</h2>
                 
                 
            </div>
        </div>
    </section>

    <!-- Order 4: Strip Section -->
    <section class="box-border w-full h-[90px] border-y border-black flex items-center overflow-hidden relative my-5 strip-section">
        <div class="flex gap-[100px] md:gap-[180px] items-center h-[45px] whitespace-nowrap absolute animate-marquee">
            
            <span class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-startups shrink-0">STARTUPS</span>
            <span class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-ai shrink-0">AI</span>
            <span class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-business shrink-0">BUSINESS</span>
            <span class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-entrepreneur shrink-0">ENTREPRENEUR</span>
            <span class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-events shrink-0">EVENTS</span>
            <span class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-brands shrink-0">BRANDS</span>
            <span class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-trends shrink-0">TRENDS</span>
        </div>
    </section>

    <!-- Order 5: Top Stories Section -->
     <section class="w-full md:max-w-[1434px] h-auto md:h-[535px] relative px-4 md:px-0 my-5">
         <!-- Grid layout for better responsiveness -->
         <div class="grid grid-cols-1 md:grid-cols-[minmax(0,_656px)_1fr] gap-8 md:gap-[42.5px] md:absolute md:left-[36.5px] md:top-[41px] w-full">
             <!-- Left Side: Main Story -->
             <div class="relative w-full">
                 <div class="w-full h-[250px] md:h-[371px] bg-cover bg-center bg-[url(https://picsum.photos/seed/topstorymain/656/371)] relative">
                      <!-- Tag positioning -->
                      <div class="absolute left-[17px] bottom-[-16px] md:left-[16.5px] md:top-[301px] z-20">
                           <div class="absolute w-[96px] h-[32px] bg-[#3533CD] z-20"></div>
                           <div class="absolute left-[9px] top-[10px] w-auto h-[14px] font-roboto font-medium text-[12px] leading-[14px] flex items-end text-white z-30 whitespace-nowrap">TOP STORIES</div>
                      </div>
                 </div>
                 <!-- Text content below image - adjusted for dynamic height -->
                 <div class="relative bg-white p-4 mt-8 md:mt-0 md:p-4 md:absolute md:left-[16px] md:top-[317px] md:w-[566px] md:h-auto z-10">
                      <h2 class="font-jakarta font-semibold text-lg md:text-[20px] leading-[25px] text-[#222222] mb-2">What One Photo Tells Us About North Korea’s Nuclear Program</h2>
                      <p class="font-jakarta font-normal text-[12px] leading-[15px] text-[#222222]">Clues from a propaganda photo reveal details about North Korea’s expanding weapons programs and internal politics.</p>
                 </div>
             </div>

            <!-- Right Side: Spotlight Boxes -->
             <div class="w-full flex flex-col gap-5 max-w-[44rem]">
                 <!-- Leadership Spotlight -->
                 <div class="relative w-full h-[196px] rounded-t-[20px] overflow-hidden">
                     <div class="absolute inset-0 bg-cover bg-center bg-[url(https://picsum.photos/seed/leadership/643/196)] rounded-t-[20px]"></div>
                     <div class="absolute inset-0 bg-[linear-gradient(354.1deg,_#3533CD_-75.73%,_#000000_95.32%)] opacity-50 rounded-t-[20px]"></div>
                     <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-[#111042]/80 z-10 rounded-t-[20px]"></div>
                     <div class="relative z-20 p-6 flex flex-col items-end text-right h-full justify-end">
                         <h3 class="w-auto md:w-[302px] h-auto font-helvetica font-bold text-2xl md:text-[30px] leading-[105%] text-white mb-2">Leadership Spotlight</h3>
                         <p class="w-auto md:w-[304px] h-auto font-helvetica font-normal text-sm md:text-[16px] leading-[128%] text-white">Discover powerful business insights and trendsetting ideas, one story at a time – fast, focused, and right at your fingertips.</p>
                     </div>
                 </div>

                 <!-- Stay Updated -->
                 <div class="relative w-full h-[196px] rounded-b-[20px] overflow-hidden">
                     <div class="absolute inset-0 bg-[linear-gradient(354.1deg,_#3533CD_-75.73%,_#000000_95.32%)] rounded-b-[20px]"></div>

                     <div class="absolute right-[-10px] w-[243px] h-[216px] bg-contain bg-no-repeat bg-[url(static/images/stay_updated.png)] z-10 opacity-80"></div>
                     <div class="relative z-20 p-6 md:p-[33px_0_0_33px] flex flex-col justify-between h-[10rem]">
                         <h3 class="w-auto md:w-[201px] h-auto font-helvetica font-bold text-2xl md:text-[30px] leading-[105%] text-white mb-5 md:mb-0 pt-4">Stay Updated</h3>
                         <a href="#" class="inline-flex flex-row justify-start items-center p-[12px_16px_12px_12px] gap-[12px] bg-white w-[341px] max-w-full h-[56px] no-underline border-none cursor-pointer rounded-md text-[#3533CD] hover:bg-gray-200">
                             <span class="w-[32px] h-[32px] bg-[#3533CD] relative button-icon-plus-shape text-white flex-shrink-0"></span>
                             <span class="font-ibm-plex font-semibold text-[14px] leading-[90%] tracking-[1.2px] uppercase">Checkout the latest magazine</span>
                         </a>
                     </div>
                 </div>
            </div>
        </div>

     </section>

    <!-- Order 6: Ad Banner -->
    <section class="w-full md:w-[1372px] h-[225px] bg-[#FF9D9D] flex justify-center items-center text-white text-2xl font-bold mx-auto ">
        AD BANNER PLACEHOLDER
    </section>

    <!-- Order 7: Funding News Section -->
    <section class="w-full h-auto md:h-[609px] relative overflow-hidden my-5 md:my-0"> <!-- Adjusted height -->
        <div class="absolute inset-0 w-full h-full bg-gradient-to-br from-[#3533CD] via-black to-black md:bg-[linear-gradient(125.25deg,_#3533CD_0.4%,_#000000_47.94%)] rounded-none md:rounded-[6px]"></div> <!-- Matched gradient -->
         <div class="relative w-full h-full z-10 p-4 md:p-0 md:pl-[44.49px] md:pt-[29px] grid grid-cols-1 md:grid-cols-2 gap-6"> <!-- Matched padding/grid -->
            <!-- Left Column: Title + 3 Small Posts -->
            <!-- Added divide-y for separator lines -->
            <div class="flex flex-col gap-4"> <!-- Matched gap -->
                <h2 class="w-auto md:w-[232.35px] h-auto md:h-[38px] font-jakarta font-bold text-2xl md:text-[28px] leading-[38px] text-white pb-4">FUNDING</h2> <!-- Matched title height -->
                <!-- Post 1 -->
                 <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5"> <!-- Added border/padding -->
                     <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/fundinghorse/289/150)] flex-shrink-0"></div> <!-- Matched image height -->
                     <div class="flex flex-col justify-center">
                          <div class="w-auto md:w-[137.18px] h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">Race98 - 03 June 2023</div> <!-- Matched meta height -->
                          <h3 class="w-auto md:w-[302.79px] h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white mb-2">6-Year-Old Horse Dies at Belmont Park After Race Injury</h3> <!-- Matched margin -->
                          <p class="w-auto md:w-[295.38px] h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">NEW YORK—A 6-year-old horse died after being injured in a race at Belmont Park ahead of next week’s</p>
                     </div>
                 </article>
                <!-- Post 2 -->
                <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5"> <!-- Added border/padding -->
                     <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/fundingcyclist/289/150)] flex-shrink-0"></div> <!-- Matched image height -->
                     <div class="flex flex-col justify-center">
                         <div class="w-auto md:w-[135.95px] h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">Jony.Ls - 03 June 2023</div> <!-- Matched meta height -->
                         <h3 class="w-auto md:w-[302.79px] h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white capitalize mb-2">Savilia Blunk Embraces Longer Season with World Cup</h3> <!-- Matched margin -->
                         <p class="w-auto md:w-[295.38px] h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">Last year, Savilia Blunk took a more conservative approach to her first season as an Elite Class athlete, skipping some</p>
                     </div>
                 </article>
                 <!-- Post 3 -->
                <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5"> <!-- Added border/padding -->
                     <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/fundingboxing/289/150)] flex-shrink-0"></div> <!-- Matched image height -->
                     <div class="flex flex-col justify-center">
                         <div class="w-auto md:w-[127.3px] h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">King.F - 03 June 2023</div> <!-- Matched meta height -->
                         <h3 class="w-auto md:w-[302.79px] h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white mb-2">Ryan Garcia is fighting again, this time on social media</h3> <!-- Matched margin -->
                         <p class="w-auto md:w-[295.38px] h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">Boxing star Ryan Garcia and his promoter, Hall of Fame fighter Oscar De La Hoya, reignited their war of words via Twitter on</p>
                     </div>
                 </article>
            </div>

             <!-- Right Column: Large Post -->
             <div class="relative w-full h-auto md:w-[640.07px] md:h-[531.62px] md:absolute md:left-[742px] md:top-[41px]"> <!-- Matched dimensions/position -->
                 <div class="relative w-full h-[250px] md:absolute md:inset-0 md:w-[640px] md:h-[395px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/fundinglarge/640/395)]"></div> <!-- Matched image dimensions -->
                 <!-- Removed overlay div -->
                 <div class="absolute left-[18px] top-[25px] border border-[#EBEEF3] rounded-[3px] bg-black/30 px-3 py-1 inline-block z-10"> <!-- Matched tag styling/position -->
                     <span class="font-dm font-medium text-[14px] md:text-[20px] leading-[26px] capitalize text-[#EBEEF3]">Business</span>
                 </div>
                 <div class="relative mt-4 px-4 font-dm font-normal text-sm leading-[1.1] text-white md:absolute md:w-[336.67px] md:h-auto md:left-[11px] md:top-[421px] md:text-[18px] md:z-10 md:mt-0 md:px-0">Debits - 03 June 2023</div> <!-- Matched meta styling/position -->
                 <h2 class="relative mt-1 px-4 pb-4 font-jakarta font-bold text-xl leading-tight capitalize text-white md:absolute md:w-[629.07px] md:h-auto md:left-[11px] md:top-[451.5px] md:text-[32px] md:leading-[40px] md:text-white md:z-10 md:mt-0 md:px-0 md:pb-0">DISCOVER THE MEMBER BENEFITS OF BOL BUSINESS</h2> <!-- Matched title styling/position -->
             </div>
        </div>
    </section>

    <!-- Order 8: Podcast Section -->
    <section class=" w-full h-auto md:h-[564px] relative flex items-center justify-center bg-cover bg-center bg-[url(static/images/9_out_of_10.png)] py-14 md:py-0 ">
            <div class="relative z-10 flex justify-center items-center w-full h-full px-4 text-center">
                <a href="#" class=" inline-block relative scale-[.4] -left-[9rem] top-12 md:hidden ">
                    <img src="static/images/checkot_button.png" alt="Checkout Podcast Button - Mobile" class=" h-auto w-full max-w-[160px] sm:max-w-[200px] hover:opacity-90 transition-opacity">
                </a>
                <a href="#" class="hidden md:inline-block" style="transform: scale(0.5); left: -32rem; position: relative; top: 11rem;">
                    <img src="static/images/checkot_button.png" alt="Checkout Podcast Button - Desktop" class=" block w-full h-auto hover:opacity-90 transition-opacity">
                </a>
            </div>
        </section>
        <!-- End Order 8 -->

    <!-- Order 9: Dual Column Section (Sustainability/Semiconductors) -->
    <section class="w-full grid grid-cols-1 md:grid-cols-2 justify-center items-start gap-5 px-4 md:px-0 my-5">
        <!-- Left Column (Sustainability) -->
        <div class="w-full h-auto relative overflow-hidden rounded-[6px] bg-gradient-to-tl from-[#3533CD] via-black to-black md:bg-[linear-gradient(93.25deg,_#3533CD_0.4%,_#000000_47.94%)] p-4 md:p-[32px_20px_32px_43px]">
             <h2 class="w-auto md:w-[359.22px] h-auto font-jakarta font-bold text-2xl md:text-[28px] leading-[38px] text-white mb-6">Sustainability</h2>
             <!-- Added divide-y -->
             <div class="flex flex-col gap-2">
                 
                 <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5">
                     <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/sushorse/293/184)] flex-shrink-0"></div>
                     <div class="flex flex-col justify-center">
                         <div class="w-auto h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">Race98 - 03 June 2023</div>
                         <h3 class="w-auto h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white mb-2">6-Year-Old Horse Dies at Belmont Park After Race Injury</h3>
                         <p class="w-auto h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">NEW YORK—A 6-year-old horse died after being injured in a race at Belmont Park ahead of next week’s</p>
                     </div>
                 </article>
                 <!-- Post 2 -->
                 <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5">
                     <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/suscyclist/293/184)] flex-shrink-0"></div>
                     <div class="flex flex-col justify-center">
                         <div class="w-auto h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">Jony.Ls - 03 June 2023</div>
                         <h3 class="w-auto h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white capitalize mb-2">Savilia Blunk Embraces Longer Season with World Cup</h3>
                         <p class="w-auto h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">Last year, Savilia Blunk took a more conservative approach to her first season as an Elite Class athlete, skipping some</p>
                     </div>
                 </article>
                 <!-- Post 3 -->
                <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5">
                     <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/susboxing/293/184)] flex-shrink-0"></div>
                     <div class="flex flex-col justify-center">
                         <div class="w-auto h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">King.F - 03 June 2023</div>
                         <h3 class="w-auto h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white mb-2">Ryan Garcia is fighting again, this time on social media</h3>
                         <p class="w-auto h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">Boxing star Ryan Garcia and his promoter, Hall of Fame fighter Oscar De La Hoya, reignited their war of words via Twitter on</p>
                     </div>
                 </article>
             </div>
        </div>
        <!-- Right Column (Semiconductors) -->
         <div class="w-full h-auto relative overflow-hidden rounded-[6px] bg-gradient-to-tl from-black via-[#3533CD] to-[#3533CD] md:bg-[linear-gradient(93.25deg,_#000000_0.4%,_#3533CD_47.94%)] p-4 md:p-[36px_20px_36px_46px]">
             <h2 class="w-auto md:w-[238px] h-auto font-jakarta font-bold text-2xl md:text-[28px] leading-[38px] text-white mb-6">Semiconductors</h2>
             <!-- Added divide-y -->
             <div class="flex flex-col gap-2">
                 
                <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5">
                    <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/sushorse/293/184)] flex-shrink-0"></div>
                    <div class="flex flex-col justify-center">
                        <div class="w-auto h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">Race98 - 03 June 2023</div>
                        <h3 class="w-auto h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white mb-2">6-Year-Old Horse Dies at Belmont Park After Race Injury</h3>
                        <p class="w-auto h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">NEW YORK—A 6-year-old horse died after being injured in a race at Belmont Park ahead of next week’s</p>
                    </div>
                </article>
                <!-- Post 2 -->
                <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5">
                    <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/suscyclist/293/184)] flex-shrink-0"></div>
                    <div class="flex flex-col justify-center">
                        <div class="w-auto h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">Jony.Ls - 03 June 2023</div>
                        <h3 class="w-auto h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white capitalize mb-2">Savilia Blunk Embraces Longer Season with World Cup</h3>
                        <p class="w-auto h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">Last year, Savilia Blunk took a more conservative approach to her first season as an Elite Class athlete, skipping some</p>
                    </div>
                </article>
                <!-- Post 3 -->
               <article class="flex flex-col md:flex-row gap-4 md:w-[616.71px] border-b border-white/30 pb-3.5">
                    <div class="w-full md:w-[289.2px] h-[150px] bg-cover bg-center rounded-[6px] bg-[url(https://picsum.photos/seed/susboxing/293/184)] flex-shrink-0"></div>
                    <div class="flex flex-col justify-center">
                        <div class="w-auto h-[10px] font-jakarta font-medium text-[10px] leading-[1] text-white/60 mb-2">King.F - 03 June 2023</div>
                        <h3 class="w-auto h-auto font-jakarta font-normal text-lg leading-[136.9%] text-white mb-2">Ryan Garcia is fighting again, this time on social media</h3>
                        <p class="w-auto h-auto font-jakarta font-normal text-xs leading-[123.9%] text-white ">Boxing star Ryan Garcia and his promoter, Hall of Fame fighter Oscar De La Hoya, reignited their war of words via Twitter on</p>
                    </div>
                </article>
            </div>
        </div>
    </section>

    <!-- Order 10: Hero Section Bottom -->
    <section class="w-full h-[200px] md:h-[564px] relative flex items-center justify-center bg-cover bg-center bg-[url(static/images/fuel_ambition.png)] py-14 md:py-0">
        <div class="relative z-10 flex justify-center items-center w-full h-full px-4 text-center">
            <a href="#" class="inline-block relative md:hidden">
                <img src="static/images/checkout_magazine_button.png" alt="Checkout Podcast Button - Mobile" class="h-auto w-full max-w-[160px] sm:max-w-[200px] hover:opacity-90 transition-opacity" style="scale: 0.7; top: 3.6rem; position: relative;">
            </a>
            <a href="#" class="hidden md:inline-block" style="transform: scale(0.5); position: relative; top: 10rem;">
                <img src="static/images/checkout_magazine_button.png" alt="Checkout Podcast Button - Desktop" class="block w-full h-auto hover:opacity-90 transition-opacity">
            </a>
        </div>
    </section>



    <!-- Order 11: AI / Lifestyle Section -->
    <section class="w-full h-auto relative px-4 md:px-[34px] py-9 my-5">
         <div class="relative w-full h-auto flex flex-col">
             <!-- Section Header -->
             <div class="relative w-full h-[42px] mb-[25px]">
                 <h2 class="absolute left-0 top-0 font-jakarta font-extrabold text-2xl leading-[30px] text-[#3533CD]">AI</h2>
                 <div class="absolute left-0 top-[42px] w-full border-t border-[#393939]"></div>
                 <div class="absolute left-0 top-[42px] w-[60px] border-t-2 border-[#3533CD] z-10"></div> 
             </div>
             <!-- Posts Grid -->
             <div class="grid grid-cols-1 md:grid-cols-2 gap-x-[47px] gap-y-[35px] w-full mt-8">
                 <!-- Large Post 1 -->
                 <article class="flex flex-col">
                     <div class="w-full h-[250px] bg-cover bg-center mb-[15px] bg-[url(https://picsum.photos/seed/ailarge1/662/250)]"></div>
                     <div class="font-jakarta text-[12px] leading-[1.1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                     <h3 class="font-jakarta font-medium text-2xl leading-[30px] capitalize text-[#393939] mb-[10px] h-auto">‘Institutional delivery vital for reducing maternal and neonatal deaths’</h3>
                     <p class="font-jakarta text-sm leading-[1.3] text-[#393939]/60 h-auto overflow-hidden">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus lobortis augue condimentum maecenas. Metus at in fames vitae posuere ut vel vulputate ...</p>
                 </article>
                  <!-- Large Post 2 -->
                 <article class="flex flex-col">
                      <div class="w-full h-[250px] bg-cover bg-center mb-[15px] bg-[url(https://picsum.photos/seed/ailarge2/662/250)]"></div>
                      <div class="font-jakarta text-[12px] leading-[1.1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                      <h3 class="font-jakarta font-medium text-2xl leading-[30px] capitalize text-[#393939] mb-[10px] h-auto">Being self-controlled child may lead to healthier middle-age</h3>
                      <p class="font-jakarta text-sm leading-[1.3] text-[#393939]/60 h-auto overflow-hidden">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus lobortis augue condimentum maecenas. Metus at in fames vitae posuere ut vel vulputate...</p>
                 </article>
                  <!-- Small Post 3 -->
                  <article class="flex flex-row gap-[19px] items-start h-auto mt-4 md:mt-0">
                      <div class="w-[100px] md:w-[189.24px] h-[90px] bg-cover bg-center flex-shrink-0 bg-[url(https://picsum.photos/seed/aismall3/189/90)]"></div>
                      <div class="flex flex-col flex-grow pt-1">
                          <div class="font-jakarta text-[10px] leading-[1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                          <h4 class="font-jakarta font-normal text-lg md:text-xl leading-[1.2] text-[#393939]">Best things you can do on a solo mountain climb</h4>
                      </div>
                  </article>
                  <!-- Small Post 4 -->
                   <article class="flex flex-row gap-[19px] items-start h-auto mt-4 md:mt-0">
                      <div class="w-[100px] md:w-[189.24px] h-[90px] bg-cover bg-center flex-shrink-0 bg-[url(https://picsum.photos/seed/aismall4/189/90)]"></div>
                      <div class="flex flex-col flex-grow pt-1">
                          <div class="font-jakarta text-[10px] leading-[1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                          <h4 class="font-jakarta font-normal text-lg md:text-xl leading-[1.2] text-[#393939]">How to use basic design principles your home</h4>
                      </div>
                  </article>
                 <!-- Small Post 5 -->
                 <article class="flex flex-row gap-[19px] items-start h-auto mt-4 md:mt-0">
                      <div class="w-[100px] md:w-[189.24px] h-[90px] bg-cover bg-center flex-shrink-0 bg-[url(https://picsum.photos/seed/aismall5/189/90)]"></div>
                      <div class="flex flex-col flex-grow pt-1">
                          <div class="font-jakarta text-[10px] leading-[1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                          <h4 class="font-jakarta font-normal text-lg md:text-xl leading-[1.2] text-[#393939]">Creative decorating with houseplants</h4>
                      </div>
                  </article>
                  <!-- Small Post 6 -->
                  <article class="flex flex-row gap-[19px] items-start h-auto mt-4 md:mt-0">
                      <div class="w-[100px] md:w-[189.24px] h-[90px] bg-cover bg-center flex-shrink-0 bg-[url(https://picsum.photos/seed/aismall6/189/90)]"></div>
                      <div class="flex flex-col flex-grow pt-1">
                          <div class="font-jakarta text-[10px] leading-[1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                          <h4 class="font-jakarta font-normal text-lg md:text-xl leading-[1.2] text-[#393939]">How to burn calories with pleasant activities</h4>
                      </div>
                  </article>
             </div>
         </div>
     </section>

    <!-- Order 12: WhatsApp Newsletter Section -->
    <section class="flex flex-col md:flex-row justify-center items-stretch px-4 md:px-[30px] py-9 gap-[15px] w-full h-auto my-5">
        <!-- Left Side (Form) -->
         <div class="w-full md:w-[625px] min-h-[625px] bg-gradient-to-r from-[#3533CD] to-[#0A0A24] rounded-[15px] relative p-8 md:p-[43px_57px] flex flex-col text-white">
             <h2 class="w-full md:w-[475px] font-jakarta font-bold text-3xl md:text-[40px] leading-[1.4] mb-[16px]">Get Weekly WhatsApp Newsletters</h2>
             <p class="w-full md:w-[504px] font-jakarta font-semibold text-lg md:text-[20px] leading-[1.6] mb-[21px]">on Latest Funding, Tech News and Business News?</p>
             <form class="relative w-full flex flex-col gap-[18px]">
                 <div class="flex flex-col md:flex-row gap-[15px]">
                     <input type="text" placeholder="First Name" required class="flex-grow h-[36px] rounded-[4px] border-none bg-white px-[15px] py-[5px] font-jakarta text-base text-gray-900 placeholder:text-gray-400 placeholder:font-normal focus:ring-2 focus:ring-bol-purple">
                     <input type="text" placeholder="Last Name" required class="flex-grow h-[36px] rounded-[4px] border-none bg-white px-[15px] py-[5px] font-jakarta text-base text-gray-900 placeholder:text-gray-400 placeholder:font-normal focus:ring-2 focus:ring-bol-purple">
                 </div>
                 <div>
                     <input type="text" placeholder="Company Name" required class="w-full h-[36px] rounded-[4px] border-none bg-white px-[15px] py-[5px] font-jakarta text-base text-gray-900 placeholder:text-gray-400 placeholder:font-normal focus:ring-2 focus:ring-bol-purple">
                 </div>
                 <div class="flex flex-col md:flex-row gap-[15px]">
                     <input type="text" placeholder="Your Designation" required class="flex-grow h-[36px] rounded-[4px] border-none bg-white px-[15px] py-[5px] font-jakarta text-base text-gray-900 placeholder:text-gray-400 placeholder:font-normal focus:ring-2 focus:ring-bol-purple">
                     <div class="flex-grow relative location-input-wrapper">
                         <input type="text" placeholder="Location" id="location" required class="w-full h-[36px] rounded-[4px] border-none bg-white px-[15px] py-[5px] font-jakarta text-base text-gray-900 placeholder:text-gray-400 placeholder:font-normal focus:ring-2 focus:ring-bol-purple appearance-none"> 
                         <!-- Arrow added via CSS -->
                     </div>
                 </div>
                 <div class="flex flex-col gap-[11px]">
                     <div class="font-jakarta font-normal text-base">Choose Categories</div>
                     <div class="flex flex-wrap gap-x-5 gap-y-3 items-center">
                         <div class="flex items-center gap-[7px]">
                             <input type="checkbox" id="cat-ai" class="appearance-none w-[18px] h-[18px] bg-white border border-[#B1B1B3] rounded-[2px] cursor-pointer relative checked:bg-bol-purple checked:border-bol-purple focus:ring-bol-purple">
                             <label for="cat-ai" class="font-jakarta font-bold text-base cursor-pointer select-none">AI</label>
                         </div>
                         <div class="flex items-center gap-[7px]">
                             <input type="checkbox" id="cat-business" class="appearance-none w-[18px] h-[18px] bg-white border border-[#B1B1B3] rounded-[2px] cursor-pointer relative checked:bg-bol-purple checked:border-bol-purple focus:ring-bol-purple">
                             <label for="cat-business" class="font-jakarta font-bold text-base cursor-pointer select-none">Business</label>
                         </div>
                          <div class="flex items-center gap-[7px]">
                             <input type="checkbox" id="cat-startups" class="appearance-none w-[18px] h-[18px] bg-white border border-[#B1B1B3] rounded-[2px] cursor-pointer relative checked:bg-bol-purple checked:border-bol-purple focus:ring-bol-purple">
                             <label for="cat-startups" class="font-jakarta font-bold text-base cursor-pointer select-none">Startups</label>
                         </div>
                         <div class="flex items-center gap-[7px]">
                             <input type="checkbox" id="cat-entrep" class="appearance-none w-[18px] h-[18px] bg-white border border-[#B1B1B3] rounded-[2px] cursor-pointer relative checked:bg-bol-purple checked:border-bol-purple focus:ring-bol-purple">
                             <label for="cat-entrep" class="font-jakarta font-bold text-base cursor-pointer select-none">Entrepreneurship</label>
                         </div>
                     </div>
                 </div>
                 <div class="relative flex items-center w-full md:w-[224px]">
                     <span class="absolute left-[10px] top-1/2 -translate-y-1/2 w-[26px] h-[26px] flex items-center justify-center pointer-events-none">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" fill="#25D366" width="20" height="20">
                            <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>
                        </svg>
                     </span></svg>
                     <input type="tel" placeholder="Whatsapp No." required class="w-full h-[36px] rounded-[4px] border-none bg-white pl-[45px] pr-[15px] py-[5px] font-jakarta text-base text-gray-900 placeholder:text-gray-400 placeholder:font-normal focus:ring-2 focus:ring-bol-purple">
                 </div>
                 <div class="mt-[17px]">
                     <button type="submit" class="w-[132px] h-[39px] bg-gradient-to-r from-black to-[#3533CD] rounded-full border-none font-jakarta font-semibold text-base text-center text-white cursor-pointer hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-black focus:ring-white transition duration-150 ease-in-out">Subscribe</button>
                 </div>
             </form>
        </div>
        <!-- Right Side (Image) -->
        <div class="w-full md:w-[716px] h-[300px] md:h-[625px] bg-cover bg-center rounded-[15px] mt-4 md:mt-0 bg-[url(https://picsum.photos/seed/whatsappvisual/716/625)] flex-shrink-0"></div>
    </section>

    <!-- Order 13: AI / Lifestyle Section 2 (Duplicate Structure) -->
    <section class="w-full h-auto relative px-4 md:px-[34px] py-9 my-5">
         <div class="relative w-full h-auto flex flex-col">
             <!-- Section Header -->
             <div class="relative w-full h-[42px] mb-[25px]">
                 <h2 class="absolute left-0 top-0 font-jakarta font-extrabold text-2xl leading-[30px] text-[#3533CD]">Lifestyle</h2>
                 <div class="absolute left-0 top-[42px] w-full border-t border-[#393939]"></div>
                 <div class="absolute left-0 top-[42px] w-[150px] border-t-2 border-[#3533CD] z-10"></div> 
             </div>
              <!-- Posts Grid -->
             <div class="grid grid-cols-1 md:grid-cols-2 gap-x-[47px] gap-y-[35px] w-full mt-8">
                 
                 <!-- Large Post 1 -->
                 <article class="flex flex-col">
                     <div class="w-full h-[250px] bg-cover bg-center mb-[15px] bg-[url(https://picsum.photos/seed/ailifestyle1/662/250)]"></div>
                     <div class="font-jakarta text-[12px] leading-[1.1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                     <h3 class="font-jakarta font-medium text-2xl leading-[30px] capitalize text-[#393939] mb-[10px] h-auto">‘Institutional delivery vital for reducing maternal and neonatal deaths’</h3>
                     <p class="font-jakarta text-sm leading-[1.3] text-[#393939]/60 h-auto overflow-hidden">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus lobortis augue condimentum maecenas. Metus at in fames vitae posuere ut vel vulputate ...</p>
                 </article>
                  <!-- Large Post 2 -->
                 <article class="flex flex-col">
                      <div class="w-full h-[250px] bg-cover bg-center mb-[15px] bg-[url(https://picsum.photos/seed/ailifestyle2/662/250)]"></div>
                      <div class="font-jakarta text-[12px] leading-[1.1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                      <h3 class="font-jakarta font-medium text-2xl leading-[30px] capitalize text-[#393939] mb-[10px] h-auto">Being self-controlled child may lead to healthier middle-age</h3>
                      <p class="font-jakarta text-sm leading-[1.3] text-[#393939]/60 h-auto overflow-hidden">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus lobortis augue condimentum maecenas. Metus at in fames vitae posuere ut vel vulputate...</p>
                 </article>
                  <!-- Small Post 3 -->
                  <article class="flex flex-row gap-[19px] items-start h-auto mt-4 md:mt-0">
                      <div class="w-[100px] md:w-[189.24px] h-[90px] bg-cover bg-center flex-shrink-0 bg-[url(https://picsum.photos/seed/ailifestyle3/189/90)]"></div>
                      <div class="flex flex-col flex-grow pt-1">
                          <div class="font-jakarta text-[10px] leading-[1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                          <h4 class="font-jakarta font-normal text-lg md:text-xl leading-[1.2] text-[#393939]">Best things you can do on a solo mountain climb</h4>
                      </div>
                  </article>
                  <!-- Small Post 4 -->
                   <article class="flex flex-row gap-[19px] items-start h-auto mt-4 md:mt-0">
                      <div class="w-[100px] md:w-[189.24px] h-[90px] bg-cover bg-center flex-shrink-0 bg-[url(https://picsum.photos/seed/ailifestyle4/189/90)]"></div>
                      <div class="flex flex-col flex-grow pt-1">
                          <div class="font-jakarta text-[10px] leading-[1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                          <h4 class="font-jakarta font-normal text-lg md:text-xl leading-[1.2] text-[#393939]">How to use basic design principles your home</h4>
                      </div>
                  </article>
                 <!-- Small Post 5 -->
                 <article class="flex flex-row gap-[19px] items-start h-auto mt-4 md:mt-0">
                      <div class="w-[100px] md:w-[189.24px] h-[90px] bg-cover bg-center flex-shrink-0 bg-[url(https://picsum.photos/seed/ailifestyle5/189/90)]"></div>
                      <div class="flex flex-col flex-grow pt-1">
                          <div class="font-jakarta text-[10px] leading-[1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                          <h4 class="font-jakarta font-normal text-lg md:text-xl leading-[1.2] text-[#393939]">Creative decorating with houseplants</h4>
                      </div>
                  </article>
                  <!-- Small Post 6 -->
                  <article class="flex flex-row gap-[19px] items-start h-auto mt-4 md:mt-0">
                      <div class="w-[100px] md:w-[189.24px] h-[90px] bg-cover bg-center flex-shrink-0 bg-[url(https://picsum.photos/seed/ailifestyle6/189/90)]"></div>
                      <div class="flex flex-col flex-grow pt-1">
                          <div class="font-jakarta text-[10px] leading-[1] text-[#393939] mb-[6px]">Craig Bator - 27 Dec 2020</div>
                          <h4 class="font-jakarta font-normal text-lg md:text-xl leading-[1.2] text-[#393939]">How to burn calories with pleasant activities</h4>
                      </div>
                  </article>
             </div>
         </div>
    </section>

    <!-- Order 14: Footer Section 1 -->
    <footer class=" w-full h-auto md:h-[750px] relative flex items-center justify-center bg-cover bg-center bg-[url(static/images/footer1.png)] py-24 md:py-0 ">
        <div class="relative z-10 flex justify-center items-center w-full h-full px-4 text-center">
        <!-- Mobile Button -->
        <a href="#" class=" inline-block relative scale-[.6] top-[3.3rem] left-[-8rem] md:hidden ">
            <img src="static/images/checkout_magazine_button.png" alt="Footer Action Button - Mobile" class=" h-auto max-h-[250px] w-full max-w-[160px] sm:max-w-[200px] hover:opacity-90 transition-opacity">
        </a>
        <!-- Desktop Button -->
        <a href="#" class="hidden md:inline-block" style="transform: scale(0.5); position: relative; top: 11rem; left: -26.7rem;">
            <img src="static/images/checkout_magazine_button.png" alt="Footer Action Button - Desktop" class=" block w-full h-auto hover:opacity-90 transition-opacity">
        </a>
        </div>
    </footer>

    <!-- Order 15: Footer Section 2 -->
    <footer class="w-full bg-black px-4 sm:px-6 md:px-[111px] pt-[40px] md:pt-[70px] pb-[20px] md:pb-[30px] relative text-white">
                
        <!-- Footer Links Container - Restructured for mobile -->
        <div class="flex flex-row flex-wrap justify-around items-start gap-6 md:gap-16 mb-8 md:mb-[100px] pt-6 md:pt-0 text-center sm:text-left">

            <!-- Logo Area: Adjusted for row layout on mobile -->
            <div class="w-auto flex flex-col items-center sm:items-start order-1 mb-6 sm:mb-0 flex-shrink-0">
                <div class="w-[80px] h-[80px] sm:w-[100px] sm:h-[100px] md:w-[161px] md:h-[161px] bg-contain bg-no-repeat bg-center sm:bg-left bg-[url(static/images/header_logo.png)] mb-2 flex-shrink-0" loading="lazy"></div>
            </div>

            <!-- Quick Links -->
            <div class="w-auto order-2 flex-shrink-0">
                <div class="font-helvetica font-bold text-sm md:text-base leading-[90%] text-[#8B8B8B] mb-3 md:mb-[19px] uppercase">Quick Links</div>
                <ul class="list-none p-0 m-0 space-y-2 md:space-y-[17px]">
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Home</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">About Us</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Careers</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Web Stories</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Magazine</a></li>
                </ul>
            </div>

            <!-- News Links -->
            <div class="w-auto order-3 flex-shrink-0">
                <div class="font-helvetica font-bold text-sm md:text-base leading-[90%] text-[#8B8B8B] mb-3 md:mb-[20px] uppercase">News</div>
                <ul class="list-none p-0 m-0 space-y-2 md:space-y-[17px]">
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Business</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Startup</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">AI</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Entrepreneur</a></li>
                    <li><a href="#" class="font-helvetica font-bold text-xs sm:text-sm md:text-base leading-[90%] text-white no-underline hover:text-[#C4C3FF] uppercase">Events</a></li>
                </ul>
            </div>
        </div>

        <div class="border-t border-white/30 w-full my-[30px] md:my-[40px]"></div>

        <!-- Social links and Subscribe section - Made responsive -->
        <div class="flex flex-col md:flex-row justify-between items-center">
           
            <!-- Social Links -->
            <div class="block mb-6 md:mb-4 w-full md:w-auto text-center md:text-left">
                <div class="font-helvetica font-bold text-sm md:text-base leading-[90%] text-[#8B8B8B] mb-[12px] md:mb-[15px] uppercase">Social Links</div>
                <div class="flex justify-center md:justify-start space-x-4">
                    <a href="#" aria-label="Instagram" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>
                        </svg>
                    </a>
                    <a href="#" aria-label="Facebook" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                        </svg>
                    </a>
                    <a href="#" aria-label="X (Twitter)" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
                        </svg>
                    </a>
                    <a href="#" aria-label="YouTube" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                        </svg>
                    </a>
                    <a href="#" aria-label="LinkedIn" class="text-white hover:text-[#C4C3FF] transition-colors duration-200">
                        <svg class="w-5 h-5 md:w-6 md:h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                        </svg>
                    </a>
                </div>
            </div>

            <!-- Advertise With Us - Made responsive -->
            <div class="flex flex-col md:flex-row justify-between items-center gap-4 md:gap-[20px] flex-wrap mb-6 md:mb-[40px]">
                <a href="#" class="font-jakarta font-bold text-sm md:text-base leading-[20px] text-white no-underline hover:text-[#C4C3FF] uppercase">Advertise With Us</a>
            </div>

            <!-- Newsletter Subscription - Made responsive -->
            <div class="text-center md:text-left col-span-1 lg:col-span-1 flex flex-col items-center md:items-start">
                <div class="font-helvetica font-bold text-base leading-[90%] text-[#8B8B8B] mb-[20px] uppercase">Subscribe to Newsletter</div>
                <!-- Mobile form (hidden on sm and up) -->
                <form class="flex flex-row items-stretch gap-2 w-full max-w-md sm:hidden">
                     <input type="email" placeholder="Enter your email" required class="flex-grow h-[40px] bg-white border-none rounded-[4px] px-[15px] text-black placeholder:text-gray-500 focus:ring-2 focus:ring-bol-purple" style="left: 1rem; position: relative;">
                     <input type="image" src="static/images/subscribe_button.png" alt="Subscribe" class="h-[40px] w-auto cursor-pointer hover:opacity-90 transition duration-150 ease-in-out shrink-0" style="left: -1rem; position: relative;">
                 </form>
                 <!-- Desktop form (hidden below sm) -->
                 <form class="hidden sm:flex sm:flex-row items-stretch gap-2 w-full max-w-md">
                     <input type="email" placeholder="Enter your email" required class="flex-grow h-[40px] bg-white border-none rounded-[4px] px-[15px] text-black placeholder:text-gray-500 focus:ring-2 focus:ring-bol-purple">
                     <input type="image" src="static/images/subscribe_button.png" alt="Subscribe" class="h-[40px] w-auto cursor-pointer hover:opacity-90 transition duration-150 ease-in-out shrink-0" style="left: -2rem; position: relative;">
                 </form>
            </div>
        </div>

        <!-- Copyright section -->
        <div class="block">
            <div class="border-t border-white/30 w-full my-[30px] md:my-[40px]"></div>
            <div class="w-full text-center font-helvetica font-bold text-xs md:text-base leading-[90%] text-white/70 mt-[20px]">
                © 2025 BRANDSOUTLOUD All Rights Reserved
            </div>
        </div>
    </footer>

</div> 

<script defer>

    const stripSection = document.querySelector('.strip-section');
    if (stripSection) {
        const stripContent = stripSection.querySelector('.animate-marquee');
        if (stripContent && stripContent.children.length > 0) { 

            const contentWidth = stripContent.scrollWidth / 2; 
            const containerWidth = stripSection.offsetWidth;

            stripContent.innerHTML += stripContent.innerHTML;
        }
    }

    const highFiveEmojis = document.querySelectorAll('.high-five-emoji');
    const countNumbers = document.querySelectorAll('.count-number');

    let highFiveCount = parseInt(localStorage.getItem('highFiveCount') || '521');

    function updateHighFiveDisplay() {
         countNumbers.forEach(numDisplay => {
            numDisplay.textContent = highFiveCount;
        });
    }

    updateHighFiveDisplay();

    highFiveEmojis.forEach(emoji => {
        emoji.addEventListener('click', () => {
            highFiveCount++;
            updateHighFiveDisplay();

            localStorage.setItem('highFiveCount', highFiveCount);

            emoji.style.transform = 'scale(1.2)';
            setTimeout(() => {
                 emoji.style.transform = 'scale(1)';
            }, 150);
        });
    })

</script>
</body>
</html>