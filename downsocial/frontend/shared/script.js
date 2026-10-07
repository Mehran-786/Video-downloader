// ---------------------------------------------------------
// 1. Translation Manager (Handles JSON fetching & DOM updates)
// ---------------------------------------------------------
class TranslationManager {
    constructor() {
        this.currentLang = localStorage.getItem('selectedLang') || 'en';
        this.cache = {};
        this.flatTranslations = {};
    }

    getPageKey() {
        const p = window.location.pathname.toLowerCase();
        if (p.includes('about')) return 'about';
        if (p.includes('features')) return 'features';
        if (p.includes('contact')) return 'contact';
        if (p.includes('privacy')) return 'privacy';
        if (p.includes('terms')) return 'terms';
        if (p.includes('facebook')) return 'facebook';
        if (p.includes('instagram')) return 'instagram';
        if (p.includes('tiktok')) return 'tiktok';
        if (p.includes('youtube')) return 'youtube';
        if (p.includes('snapchat')) return 'snapchat';
        if (p.includes('threads')) return 'threads';
        if (p.includes('private')) return 'private';
        return 'index';
    }

    // Flattens nested JSON for easy key mapping
    flattenObject(ob) {
        let toReturn = {};
        for (let i in ob) {
            if (!ob.hasOwnProperty(i)) continue;
            if (typeof ob[i] === 'object' && ob[i] !== null && !Array.isArray(ob[i])) {
                let flatObject = this.flattenObject(ob[i]);
                for (let x in flatObject) {
                    if (!flatObject.hasOwnProperty(x)) continue;
                    toReturn[x] = flatObject[x];
                }
            } else {
                toReturn[i] = ob[i];
            }
        }
        return toReturn;
    }

    async changeLanguage(lang) {
        this.currentLang = lang;
        localStorage.setItem('selectedLang', lang);

        if (!this.cache[lang]) {
            try {
                let response = await fetch(`locales/${lang}.json`);
                if (!response.ok) response = await fetch(`../shared/locales/${lang}.json`);
                if (!response.ok) response = await fetch(`../locales/${lang}.json`);
                if (!response.ok) response = await fetch(`../../locales/${lang}.json`);
                if (!response.ok) throw new Error('Translation file not found');
                this.cache[lang] = await response.json();
            } catch (error) {
                console.error('Error loading language:', error);
                if (lang !== 'en') this.changeLanguage('en'); // Fallback
                return;
            }
        }

        this.flatTranslations = this.flattenObject(this.cache[lang]);
        this.applyTranslations(this.cache[lang]);

        // RTL Support (Arabic and Urdu)
        const isRtl = (lang === 'ar' || lang === 'ur');
        document.documentElement.lang = lang;
        document.documentElement.dir = isRtl ? 'rtl' : 'ltr';
        document.body.setAttribute('dir', isRtl ? 'rtl' : 'ltr');

        // Dynamic Active Flag Icon Update
        const flagMap = {'en': 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgNDgwIiB3aWR0aD0iNjQwIiBoZWlnaHQ9IjQ4MCI+DQogIDxwYXRoIGZpbGw9IiNiZDNkNDQiIGQ9Ik0wIDBoNjQwdjQ4MEgweiIvPg0KICA8cGF0aCBzdHJva2U9IiNmZmYiIHN0cm9rZS13aWR0aD0iMzciIGQ9Ik0wIDU1LjVoNjQwTTAgMTI5LjVoNjQwTTAgMjAzLjVoNjQwTTAgMjc3LjVoNjQwTTAgMzUxLjVoNjQwTTAgNDI1LjVoNjQwIi8+DQogIDxwYXRoIGZpbGw9IiMxOTJmNWQiIGQ9Ik0wIDBoMjYwdjI1OUgweiIvPg0KICA8IS0tIFN0YXJzIHBhdHRlcm4gLS0+DQogIDxnIGZpbGw9IiNmZmYiPg0KICAgIDxnIGlkPSJzMSI+DQogICAgICA8ZyBpZD0iczIiPg0KICAgICAgICA8cG9seWdvbiBpZD0ic3RhciIgcG9pbnRzPSIwLC0xMCAyLjksLTIuMiA5LjUsLTIuMiA0LjEsMS44IDYuMiw4LjEgMCw0IC02LjIsOC4xIC00LjEsMS44IC05LjUsLTIuMiAtMi45LC0yLjIiLz4NCiAgICAgICAgPHVzZSBocmVmPSIjc3RhciIgeD0iNDMuMyIvPg0KICAgICAgICA8dXNlIGhyZWY9IiNzdGFyIiB4PSI4Ni42Ii8+DQogICAgICAgIDx1c2UgaHJlZj0iI3N0YXIiIHg9IjEzMCIvPg0KICAgICAgICA8dXNlIGhyZWY9IiNzdGFyIiB4PSIxNzMuMyIvPg0KICAgICAgICA8dXNlIGhyZWY9IiNzdGFyIiB4PSIyMTYuNiIvPg0KICAgICAgPC9nPg0KICAgICAgPHVzZSBocmVmPSIjczIiIHk9IjU2Ii8+DQogICAgICA8dXNlIGhyZWY9IiNzMiIgeT0iMTEyIi8+DQogICAgICA8dXNlIGhyZWY9IiNzMiIgeT0iMTY4Ii8+DQogICAgICA8dXNlIGhyZWY9IiNzMiIgeT0iMjI0Ii8+DQogICAgPC9nPg0KICAgIDxnIGlkPSJzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjEuNiwgMjgpIj4NCiAgICAgIDxwb2x5Z29uIHBvaW50cz0iMCwtMTAgMi45LC0yLjIgOS41LC0yLjIgNC4xLDEuOCA2LjIsOC4xIDAsNCAtNi4yLDguMSAtNC4xLDEuOCAtOS41LC0yLjIgLTIuOSwtMi4yIi8+DQogICAgICA8dXNlIGhyZWY9IiNzdGFyIiB4PSI0My4zIi8+DQogICAgICA8dXNlIGhyZWY9IiNzdGFyIiB4PSI4Ni42Ii8+DQogICAgICA8dXNlIGhyZWY9IiNzdGFyIiB4PSIxMzAiLz4NCiAgICAgIDx1c2UgaHJlZj0iI3N0YXIiIHg9IjE3My4zIi8+DQogICAgICA8dXNlIGhyZWY9IiNzdGFyIiB4PSIyMTYuNiIgeT0iMCIvPg0KICAgIDwvZz4NCiAgICA8dXNlIGhyZWY9IiNzMyIgeT0iNTYiLz4NCiAgICA8dXNlIGhyZWY9IiNzMyIgeT0iMTEyIi8+DQogICAgPHVzZSBocmVmPSIjczMiIHk9IjE2OCIvPg0KICA8L2c+DQo8L3N2Zz4=', 'es': 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgNDgwIiB3aWR0aD0iNjQwIiBoZWlnaHQ9IjQ4MCI+DQogIDxwYXRoIGZpbGw9IiNhYTE1MWIiIGQ9Ik0wIDBoNjQwdjQ4MEgweiIvPg0KICA8cGF0aCBmaWxsPSIjZjFiZjAwIiBkPSJNMCAxMjBoNjQwdjI0MEgweiIvPg0KICA8IS0tIFNwYW5pc2ggQ29hdCBvZiBhcm1zIHNpbXBsaWZpZWQgcmVwcmVzZW50YXRpb24gZm9yIGZsYWcgaWNvbiAtLT4NCiAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTgwLCAyNDApIHNjYWxlKDAuNjUpIj4NCiAgICA8IS0tIENyb3duIC0tPg0KICAgIDxwYXRoIGZpbGw9IiNkNDliMDAiIGQ9Ik0tMzAsLTc1IEwtNDAsLTUwIEwtMTAsLTU1IEwwLC03OCBMMTAsLTU1IEw0MCwtNTAgTDMwLC03NSBaIi8+DQogICAgPGNpcmNsZSBjeD0iMCIgY3k9Ii04MiIgcj0iNiIgZmlsbD0iI2ZmMDAwMCIvPg0KICAgIDwhLS0gUGlsbGFycyBvZiBIZXJjdWxlcyAtLT4NCiAgICA8cmVjdCB4PSItNjUiIHk9Ii0zMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjcwIiBmaWxsPSIjYzBjMGMwIiByeD0iMyIvPg0KICAgIDxyZWN0IHg9IjUzIiB5PSItMzAiIHdpZHRoPSIxMiIgaGVpZ2h0PSI3MCIgZmlsbD0iI2MwYzBjMCIgcng9IjMiLz4NCiAgICA8cGF0aCBmaWxsPSIjYWExNTFiIiBkPSJNLTcyLCAtNSBoMjYgdjggaC0yNiB6IE00NiwgLTUgaDI2IHY4IGgtMjYgeiIvPg0KICAgIDwhLS0gU2hpZWxkIC0tPg0KICAgIDxwYXRoIGQ9Ik0tNDAsLTMwIGg4MCB2NTAgYzAsMzAgLTQwLDUwIC00MCw1MCBjMCwwIC00MCwtMjAgLTQwLC01MCB6IiBmaWxsPSIjYWExNTFiIiBzdHJva2U9IiNmMWJmMDAiIHN0cm9rZS13aWR0aD0iNCIvPg0KICAgIDwhLS0gU2hpZWxkIHF1YXJ0ZXJzIC0tPg0KICAgIDxwYXRoIGQ9Ik0tMzYsLTI2IGgzNiB2MzYgaC0zNiB6IiBmaWxsPSIjYWExNTFiIi8+DQogICAgPHBhdGggZD0iTTAsLTI2IGgzNiB2MzYgaC0zNiB6IiBmaWxsPSIjZmZmZmZmIi8+DQogICAgPHBhdGggZD0iTS0zNiwxMCBoMzYgdjMwIGMwLDEwIDEwLDIwIDIwLDI1IGgtMjAgdi0yNSB6IiBmaWxsPSIjZjFiZjAwIi8+DQogICAgPHBhdGggZD0iTTAsMTAgaDM2IHYyNSBjLTEwLDUgLTIwLDEwIC0yMCwyMCB2LTIwIGgtMTYgeiIgZmlsbD0iI2FhMTUxYiIvPg0KICAgIDwhLS0gQ2VudGVyIGluZXNjdXRjaGVvbiAtLT4NCiAgICA8ZWxsaXBzZSBjeD0iMCIgY3k9IjEwIiByeD0iMTAiIHJ5PSIxNCIgZmlsbD0iIzAwMzU4MCIgc3Ryb2tlPSIjYWExNTFiIiBzdHJva2Utd2lkdGg9IjIiLz4NCiAgICA8Y2lyY2xlIGN4PSIwIiBjeT0iMTAiIHI9IjQiIGZpbGw9IiNmMWJmMDAiLz4NCiAgPC9nPg0KPC9zdmc+', 'pt': 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgNDgwIiB3aWR0aD0iNjQwIiBoZWlnaHQ9IjQ4MCI+DQogIDxwYXRoIGZpbGw9IiNkYTI5MWMiIGQ9Ik0wIDBoNjQwdjQ4MEgweiIvPg0KICA8cGF0aCBmaWxsPSIjMDQ2YTM4IiBkPSJNMCAwaDI0MHY0ODBIMHoiLz4NCiAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjQwLCAyNDApIHNjYWxlKDAuOSkiPg0KICAgIDwhLS0gQXJtaWxsYXJ5IHNwaGVyZSAoeWVsbG93KSAtLT4NCiAgICA8Y2lyY2xlIHI9IjY1IiBmaWxsPSIjZjFiZjAwIiBzdHJva2U9IiMwMDAiIHN0cm9rZS13aWR0aD0iMiIvPg0KICAgIDxjaXJjbGUgcj0iNDgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzY4NTQwMCIgc3Ryb2tlLXdpZHRoPSI1Ii8+DQogICAgPGxpbmUgeDE9Ii02NSIgeTE9IjAiIHgyPSI2NSIgeTI9IjAiIHN0cm9rZT0iIzY4NTQwMCIgc3Ryb2tlLXdpZHRoPSI1Ii8+DQogICAgPGxpbmUgeDE9IjAiIHkxPSItNjUiIHgyPSIwIiB5Mj0iNjUiIHN0cm9rZT0iIzY4NTQwMCIgc3Ryb2tlLXdpZHRoPSI1Ii8+DQogICAgPGVsbGlwc2Ugcng9IjM1IiByeT0iNjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzY4NTQwMCIgc3Ryb2tlLXdpZHRoPSI1IiB0cmFuc2Zvcm09InJvdGF0ZSgzNSkiLz4NCiAgICA8IS0tIFBvcnR1Z3Vlc2UgU2hpZWxkIC0tPg0KICAgIDxwYXRoIGQ9Ik0tMjgsLTM2IGg1NiB2NDAgYzAsMjggLTI4LDQyIC0yOCw0MiBjMCwwIC0yOCwtMTQgLTI4LC00MiB6IiBmaWxsPSIjZmZmZmZmIiBzdHJva2U9IiNkYTI5MWMiIHN0cm9rZS13aWR0aD0iOSIvPg0KICAgIDwhLS0gNyBDYXN0bGVzIG9uIHJlZCBib3JkZXIgLS0+DQogICAgPGNpcmNsZSBjeD0iLTIwIiBjeT0iLTI4IiByPSIzIiBmaWxsPSIjZjFiZjAwIi8+DQogICAgPGNpcmNsZSBjeD0iMCIgY3k9Ii0zMiIgcj0iMyIgZmlsbD0iI2YxYmYwMCIvPg0KICAgIDxjaXJjbGUgY3g9IjIwIiBjeT0iLTI4IiByPSIzIiBmaWxsPSIjZjFiZjAwIi8+DQogICAgPGNpcmNsZSBjeD0iLTIzIiBjeT0iMiIgcj0iMyIgZmlsbD0iI2YxYmYwMCIvPg0KICAgIDxjaXJjbGUgY3g9IjIzIiBjeT0iMiIgcj0iMyIgZmlsbD0iI2YxYmYwMCIvPg0KICAgIDxjaXJjbGUgY3g9Ii0xNCIgY3k9IjI0IiByPSIzIiBmaWxsPSIjZjFiZjAwIi8+DQogICAgPGNpcmNsZSBjeD0iMTQiIGN5PSIyNCIgcj0iMyIgZmlsbD0iI2YxYmYwMCIvPg0KICAgIDwhLS0gSW5uZXIgYmx1ZSBxdWluYXMgLS0+DQogICAgPHBhdGggZD0iTS01LC0xMCBoMTAgdjE0IGMwLDUgLTUsOCAtNSw4IGMwLDAgLTUsLTMgLTUsLTggeiIgZmlsbD0iIzAwMzU4MCIvPg0KICAgIDxwYXRoIGQ9Ik0tNSwtMjIgaDEwIHYxMCBjMCw0IC01LDYgLTUsNiBjMCwwIC01LC0yIC01LC02IHoiIGZpbGw9IiMwMDM1ODAiLz4NCiAgICA8cGF0aCBkPSJNLTUsNCBoMTAgdjEwIGMwLDQgLTUsNiAtNSw2IGMwLDAgLTUsLTIgLTUsLTYgeiIgZmlsbD0iIzAwMzU4MCIvPg0KICAgIDxwYXRoIGQ9Ik0tMTUsLTEwIGg4IHYxMCBjMCw0IC00LDYgLTQsNiBjMCwwIC00LC0yIC00LC02IHoiIGZpbGw9IiMwMDM1ODAiLz4NCiAgICA8cGF0aCBkPSJNNywtMTAgaDggdjEwIGMwLDQgLTQsNiAtNCw2IGMwLDAgLTQsLTIgLTQsLTYgeiIgZmlsbD0iIzAwMzU4MCIvPg0KICA8L2c+DQo8L3N2Zz4=', 'de': 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgNDgwIiB3aWR0aD0iNjQwIiBoZWlnaHQ9IjQ4MCI+DQogIDxwYXRoIGZpbGw9IiMwMDAwMDAiIGQ9Ik0wIDBoNjQwdjE2MEgweiIvPg0KICA8cGF0aCBmaWxsPSIjZGQwMDAwIiBkPSJNMCAxNjBoNjQwdjE2MEgweiIvPg0KICA8cGF0aCBmaWxsPSIjZmZjZTAwIiBkPSJNMCAzMjBoNjQwdjE2MEgweiIvPg0KPC9zdmc+', 'fr': 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgNDgwIiB3aWR0aD0iNjQwIiBoZWlnaHQ9IjQ4MCI+DQogIDxwYXRoIGZpbGw9IiMwMDIzOTUiIGQ9Ik0wIDBoMjEzLjN2NDgwSDB6Ii8+DQogIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0yMTMuMyAwaDIxMy40djQ4MEgyMTMuM3oiLz4NCiAgPHBhdGggZmlsbD0iI2VkMjkzOSIgZD0iTTQyNi43IDBoMjEzLjN2NDgwSDQyNi43eiIvPg0KPC9zdmc+', 'it': 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAgNDgwIiB3aWR0aD0iNjQwIiBoZWlnaHQ9IjQ4MCI+DQogIDxwYXRoIGZpbGw9IiMwMDkyNDYiIGQ9Ik0wIDBoMjEzLjN2NDgwSDB6Ii8+DQogIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0yMTMuMyAwaDIxMy40djQ4MEgyMTMuM3oiLz4NCiAgPHBhdGggZmlsbD0iI2NlMmIzNyIgZD0iTTQyNi43IDBoMjEzLjN2NDgwSDQyNi43eiIvPg0KPC9zdmc+'};
        if (flagMap[lang]) {
            document.querySelectorAll('.active-lang-flag').forEach(img => {
                img.src = flagMap[lang];
                img.alt = lang;
            });
        }


        // Close menus after selection
        if (window.uiManager) window.uiManager.closeAllMenus();
    }

    applyTranslations(data) {
        const lang = this.currentLang;
        const pageKey = this.getPageKey();
        const pageData = data[pageKey] || data.index;

        // A. Standard data-key text replacement
        document.querySelectorAll("[data-key]").forEach(el => {
            const key = el.getAttribute("data-key");
            if (this.flatTranslations[key]) {
                if (el.tagName === "INPUT") el.placeholder = this.flatTranslations[key];
                else if (el.tagName === "SPAN") el.textContent = this.flatTranslations[key];
                else el.innerHTML = this.flatTranslations[key];
            }
        });

        // B. Navigation & Header
        document.querySelectorAll('.nav-brand-home span, a[data-key="homeBtn"]').forEach(el => {
            el.textContent = data.common?.homeBtn || 'Home';
        });
        document.querySelectorAll('a[href*="private-downloader"] span').forEach(el => {
            el.textContent = data.common?.privateBtn || 'Private Downloader';
        });
        document.querySelectorAll('#desktopLangToggle span, #mobileLangToggle span, [data-key="langBtn"]').forEach(el => {
            el.textContent = data.common?.langBtn || 'Language';
        });
        document.querySelectorAll('[data-key="extBtn"]').forEach(el => {
            el.textContent = data.common?.extBtn || 'Extension';
        });
        document.querySelectorAll('.soon-badge, [data-key="soonBadge"]').forEach(el => {
            el.textContent = data.common?.soonBadge || 'Soon';
        });
        document.querySelectorAll('.sidebar .menu-links a[href*="features.html"] span').forEach(el => {
            el.textContent = data.common?.featuresBtn || 'Features';
        });
        document.querySelectorAll('.sidebar .menu-links a[href*="about.html"] span').forEach(el => {
            el.textContent = data.common?.aboutBtn || 'About Us';
        });
        document.querySelectorAll('.sidebar .menu-links a[href*="contact.html"] span').forEach(el => {
            el.textContent = data.common?.contactBtn || 'Contact';
        });

        // C. Hero Section (H1, Tagline, Placeholder, Download Btn, Orbit)
        if (pageData) {
            const h1 = document.querySelector('.main-wrapper h1, h1');
            if (h1 && pageData.title) h1.textContent = pageData.title;

            const tagline = document.querySelector('.tagline');
            if (tagline && pageData.tagline) tagline.textContent = pageData.tagline;

            const input = document.getElementById('videoUrl') || document.querySelector('.url-input');
            if (input && pageData.placeholder) input.placeholder = pageData.placeholder;

            const dlBtn = document.getElementById('downloadBtn') || document.querySelector('.download-btn');
            if (dlBtn && pageData.downloadBtn) dlBtn.textContent = pageData.downloadBtn;

            const orbitBadge = document.querySelector('.orbit-more-badge');
            if (orbitBadge && data.common?.moreTools) {
                orbitBadge.innerHTML = `<i class="fas fa-th-large"></i> ${data.common.moreTools}`;
            }

            // Result Card UI elements
            const mediaTitle = document.getElementById('mediaTitle');
            if (mediaTitle && data.common?.readyTitle) mediaTitle.textContent = data.common.readyTitle;

            const infoP = document.querySelector('.details-container p');
            if (infoP && data.common?.infoText) infoP.innerHTML = `<i class="fas fa-info-circle"></i> ${data.common.infoText}`;

            const btnVidHigh = document.querySelector('#btnVidHigh span');
            if (btnVidHigh && data.common?.dlVidHigh) btnVidHigh.textContent = data.common.dlVidHigh;

            const btnVidNorm = document.querySelector('#btnVidNorm span');
            if (btnVidNorm && data.common?.dlVidNorm) btnVidNorm.textContent = data.common.dlVidNorm;

            const btnAudHigh = document.querySelector('#btnAudHigh span');
            if (btnAudHigh && data.common?.dlAudHigh) btnAudHigh.textContent = data.common.dlAudHigh;

            const btnAudNorm = document.querySelector('#btnAudNorm span');
            if (btnAudNorm && data.common?.dlAudNorm) btnAudNorm.textContent = data.common.dlAudNorm;
        }

        // D. Feature Cards (H3, P, and Blog Content)
        const featureBoxes = document.querySelectorAll('.features-container .feature-box');
        if (featureBoxes.length && pageData?.features) {
            featureBoxes.forEach((box, i) => {
                const f = pageData.features[i];
                if (f) {
                    const h3 = box.querySelector('h3');
                    if (h3) h3.textContent = f.title;
                    const p = box.querySelector(':scope > p');
                    if (p) p.textContent = f.desc;
                    const blog = box.querySelector('.blog-content');
                    if (blog) {
                        const iconHtml = f.blogIcon ? `<i class="${f.blogIcon}" style="font-size: 18px; margin-right: 5px;"></i> ` : '';
                        blog.innerHTML = `<h4>${iconHtml}${f.blogTitle}</h4><p>${f.blogP1}</p>${f.blogP2 ? `<p>${f.blogP2}</p>` : ''}`;
                    }
                }
            });
        }

        document.querySelectorAll('.expandable-box').forEach(box => {
            const btnText = box.querySelector('.more-details-text');
            if (btnText) {
                btnText.innerText = box.classList.contains('active')
                    ? (data.common?.showLess || "Show Less")
                    : (data.common?.moreDetails || "More Details");
            }
        });

        // E. How-To Guide Section
        const howToContainer = document.querySelector('.how-to-section');
        if (howToContainer && pageData?.howToTitle) {
            const isExpanded = document.getElementById('howToHiddenContent')?.classList.contains('expanded');
            let howToHTML = `<h2 class="section-title">${pageData.howToTitle}</h2><div class="how-to-content">`;
            if (pageData.howToSteps) {
                pageData.howToSteps.forEach(st => {
                    howToHTML += `<h3>${st.title}</h3><p>${st.desc}</p>`;
                    if (st.bullet) howToHTML += `<ul class="how-to-list"><li><i class="fas fa-check"></i> ${st.bullet}</li></ul>`;
                });
            }
            if (pageData.howToHidden) {
                howToHTML += `<div class="how-to-hidden-content ${isExpanded ? 'expanded' : ''}" id="howToHiddenContent">`;
                pageData.howToHidden.forEach(st => {
                    howToHTML += `<h3>${st.title}</h3><p>${st.desc}</p>`;
                    if (st.bullets) {
                        howToHTML += `<ul class="how-to-list">`;
                        st.bullets.forEach(b => howToHTML += `<li><i class="fas fa-check"></i> ${b}</li>`);
                        howToHTML += `</ul>`;
                    }
                    if (st.tip) howToHTML += `<p class="pro-tip">${st.tip}</p>`;
                });
                howToHTML += `</div>`;
            }
            const readMoreText = data.common?.readMore || 'Read More';
            const readLessText = data.common?.readLess || 'Read Less';
            howToHTML += `<button class="read-more-btn ${isExpanded ? 'expanded' : ''}" id="readMoreHowTo">${isExpanded ? readLessText + ' <i class="fas fa-chevron-up"></i>' : readMoreText + ' <i class="fas fa-chevron-down"></i>'}</button></div>`;
            howToContainer.innerHTML = howToHTML;
            if (window.uiManager) window.uiManager.bindHowToBtn(pageData);
        }

        // F. Quick Answer (AEO / GEO direct snippet)
        const qaBox = document.querySelector('.quick-answer');
        if (qaBox && pageData?.quickAnswerText) {
            const qaTitle = qaBox.querySelector('.quick-answer-title, strong, h3');
            if (qaTitle && pageData.quickAnswerTitle) qaTitle.innerHTML = pageData.quickAnswerTitle;
            const qaText = qaBox.querySelector('.quick-answer-text, p');
            if (qaText) qaText.innerHTML = pageData.quickAnswerText;
        }

        // G. FAQs Accordions
        const faqContainer = document.querySelector('.faq-section');
        if (faqContainer && pageData?.faqs) {
            let faqHTML = `<h2 class="section-title">${pageData.faqsTitle || data.common?.faqTitle || 'Frequently Asked Questions'}</h2><div class="accordion">`;
            pageData.faqs.forEach(faq => {
                faqHTML += `
                    <div class="accordion-item">
                        <div class="accordion-header">
                            <span>${faq.q}</span><i class="fas fa-plus"></i>
                        </div>
                        <div class="accordion-body"><p>${faq.a}</p></div>
                    </div>`;
            });
            faqContainer.innerHTML = faqHTML + `</div>`;
            if (window.uiManager) window.uiManager.bindAccordions();
        }

        // H. SEO Article
        const seoWrapper = document.querySelector('.seo-article-wrapper, article.seo-article');
        if (seoWrapper && pageData?.seoArticle) {
            if (seoWrapper.tagName === 'ARTICLE' && !seoWrapper.classList.contains('seo-article-wrapper')) {
                seoWrapper.outerHTML = pageData.seoArticle;
            } else {
                seoWrapper.innerHTML = pageData.seoArticle;
            }
        }

        // I. Standalone Pages (About, Features, Contact, Privacy, Terms)
        const staticWrapper = document.querySelector('.page-content-wrapper, main.page-container');
        if (staticWrapper && data[pageKey]?.pageHtml) {
            staticWrapper.outerHTML = data[pageKey].pageHtml;
            if (window.uiManager) window.uiManager.bindAccordions();
        } else {
            const articleContainer = document.querySelector('.article-container');
            if (articleContainer && data[pageKey]?.content) {
                articleContainer.innerHTML = data[pageKey].content;
            }
        }

        // J. Footer Elements
        const footerToolsTitle = document.querySelector('.footer-tools-title');
        if (footerToolsTitle && data.common?.footerToolsTitle) {
            footerToolsTitle.innerHTML = `<i class="fas fa-th"></i> ${data.common.footerToolsTitle}`;
        }

        const footerBrandP = document.querySelector('.footer-brand p, .footer-col-brand p');
        if (footerBrandP && data.common?.footerAboutDesc) {
            footerBrandP.textContent = data.common.footerAboutDesc;
        }

        document.querySelectorAll('.footer-col h4, .footer-column h4').forEach(h4 => {
            const text = h4.textContent.toLowerCase();
            if (text.includes('downloader') || text.includes('herramienta') || text.includes('outil') || text.includes('tool')) {
                h4.textContent = data.common?.footerToolsTitle || h4.textContent;
            } else if (text.includes('company') || text.includes('compañía') || text.includes('entreprise') || text.includes('legal')) {
                h4.textContent = data.common?.footerLegalTitle || h4.textContent;
            } else if (text.includes('support') || text.includes('soporte') || text.includes('hilfe') || text.includes('सहायता')) {
                h4.textContent = data.common?.footerSupportTitle || h4.textContent;
            }
        });

        document.querySelectorAll('.footer-links a, .footer-col a').forEach(a => {
            const href = (a.getAttribute('href') || '').toLowerCase();
            if (href.endsWith('index.html') || href === '/' || href === '../index.html') a.textContent = data.common?.homeBtn || 'Home';
            else if (href.includes('features')) a.textContent = data.common?.featuresBtn || 'Features';
            else if (href.includes('about')) a.textContent = data.common?.aboutBtn || 'About';
            else if (href.includes('contact')) a.textContent = data.common?.contactBtn || 'Contact';
            else if (href.includes('privacy')) a.textContent = data.common?.privacyBtn || 'Privacy';
            else if (href.includes('terms')) a.textContent = data.common?.termsBtn || 'Terms';
            else if (href.includes('private-downloader')) a.textContent = data.common?.privateBtn || 'Private Downloader';
        });

        const footerCopy = document.querySelector('.footer-bottom p, .footer-copyright, .footer-bottom-copy');
        if (footerCopy && data.common?.footerCopyright) {
            footerCopy.innerHTML = data.common.footerCopyright;
        }

        const footerDisc = document.querySelector('.footer-disclaimer p, .footer-disclaimer');
        if (footerDisc && data.common?.footerDisclaimer) {
            footerDisc.innerHTML = data.common.footerDisclaimer;
        }

        // K. Notifications
        if (data.notifications) {
            document.querySelectorAll('.notif-header h4').forEach(el => el.innerHTML = data.notifications.header);
            document.querySelectorAll('.notif-header .badge').forEach(el => el.innerHTML = data.notifications.newBadge);
            document.querySelectorAll('.notif-info').forEach(info => {
                const h5 = info.querySelector('h5'), p = info.querySelector('.notif-time');
                if (h5) h5.innerHTML = data.notifications.extTitle;
                if (p) p.innerHTML = data.notifications.time;
            });
            document.querySelectorAll('.notif-content').forEach(content => {
                content.innerHTML = `<p>${data.notifications.content1}</p><p>${data.notifications.content2}</p><p>${data.notifications.content3}</p>`;
            });
        }

        // L. SEO Meta Tags & 20-Point Technical Optimization
        if (data.seo) {
            const seo = data.seo;
            const pageTitle = seo[pageKey + 'Title'] || (pageData?.title ? `${pageData.title} — downsocial` : document.title);
            const pageDesc = seo[pageKey + 'Desc'] || pageData?.tagline || '';
            const pageKw = seo[pageKey + 'Keywords'] || '';
            const pageOgTitle = seo[pageKey + 'OgTitle'] || pageTitle;
            const pageOgDesc = seo[pageKey + 'OgDesc'] || pageDesc;

            document.title = pageTitle;
            document.querySelector('meta[name="description"]')?.setAttribute("content", pageDesc);
            document.querySelector('meta[name="keywords"]')?.setAttribute("content", pageKw);
            document.querySelector('meta[property="og:title"]')?.setAttribute("content", pageOgTitle);
            document.querySelector('meta[property="og:description"]')?.setAttribute("content", pageOgDesc);
            document.querySelector('meta[name="twitter:title"]')?.setAttribute("content", pageOgTitle);
            document.querySelector('meta[name="twitter:description"]')?.setAttribute("content", pageOgDesc);

            const jsonLdScript = document.querySelector('script[type="application/ld+json"]');
            if (jsonLdScript && pageData) {
                try {
                    let schema = JSON.parse(jsonLdScript.textContent);
                    if (schema['@graph']) {
                        schema['@graph'].forEach(node => {
                            if (node['@type'] === 'WebApplication' || node['@type'] === 'WebPage') {
                                node.name = pageTitle;
                                node.description = pageDesc;
                                node.inLanguage = lang;
                            }
                            if (node['@type'] === 'FAQPage' && pageData.faqs) {
                                node.mainEntity = pageData.faqs.map(f => ({
                                    '@type': 'Question',
                                    'name': f.q,
                                    'acceptedAnswer': {
                                        '@type': 'Answer',
                                        'text': f.a.replace(/<[^>]*>?/gm, '')
                                    }
                                }));
                            }
                        });
                        jsonLdScript.textContent = JSON.stringify(schema, null, 2);
                    }
                } catch (err) {}
            }
        }
    }

    getFlatTrans(key, fallback) {
        return this.flatTranslations[key] || fallback;
    }
}

// ---------------------------------------------------------
// 2. UI Manager (Handles interactions, menus, accordions)
// ---------------------------------------------------------
class UIManager {
    init() {
        this.bindMenus();
        this.bindNotifications();
        this.bindExpandableBoxes();
        this.enforceNewTabLinks();
        this.bindAccordions();
        this.bindBrandOrbit();
        this.bindSmartToolLinks();
        this.bindHomeNavigation();
        this.bindContactForm();
    }

    bindBrandOrbit() {
        const orbit = document.getElementById('brandOrbit');
        const centerBtn = document.getElementById('orbitCenterBtn');
        if (orbit && centerBtn) {
            centerBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                orbit.classList.toggle('active');
            });

            document.addEventListener('click', (e) => {
                if (!orbit.contains(e.target)) {
                    orbit.classList.remove('active');
                }
            });

            // When user switches back to this tab, ensure circle is closed
            window.addEventListener('focus', () => {
                orbit.classList.remove('active');
            });

            document.addEventListener('visibilitychange', () => {
                if (document.visibilityState === 'visible') {
                    orbit.classList.remove('active');
                }
            });
        }
    }

    bindSmartToolLinks() {
        const normalizePath = (urlStr) => {
            try {
                const u = new URL(urlStr, window.location.href);
                let p = u.pathname.toLowerCase().replace(/\/index\.html$/, '');
                if (!p.endsWith('/')) {
                    p += '/';
                }
                return u.origin + p;
            } catch (err) {
                return urlStr;
            }
        };

        const currentNormalized = normalizePath(window.location.href);

        document.querySelectorAll('.orbit-item, .tool-pill').forEach(link => {
            link.addEventListener('click', (e) => {
                const href = link.getAttribute('href');
                if (!href || href === '#' || href.startsWith('javascript:')) return;

                // Always close the orbit circle immediately on click
                const orbit = document.getElementById('brandOrbit');
                if (orbit) orbit.classList.remove('active');

                // Browser DOM property `link.href` automatically resolves relative href to full absolute URL
                const targetNormalized = normalizePath(link.href);

                // If user clicks the link of the page they are ALREADY on, do not open a new tab
                if (targetNormalized === currentNormalized) {
                    e.preventDefault();

                    const urlInput = document.getElementById('videoUrl');
                    if (urlInput) {
                        urlInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
                        urlInput.focus();

                        urlInput.style.transition = 'box-shadow 0.3s ease, border-color 0.3s ease';
                        urlInput.style.borderColor = 'var(--accent-blue)';
                        urlInput.style.boxShadow = '0 0 20px rgba(232, 41, 74, 0.5)';
                        setTimeout(() => {
                            urlInput.style.boxShadow = '';
                            urlInput.style.borderColor = '';
                        }, 1200);
                    }
                } else {
                    // Open different tool in new tab with window.opener preserved so Home can close it
                    e.preventDefault();
                    window.open(link.href, '_blank');
                }
            });
        });
    }

    bindHomeNavigation() {
        const cleanPath = window.location.pathname.toLowerCase().replace(/\/index\.html$/, '').replace(/^\//, '').replace(/\/$/, '');
        const isSubPage = cleanPath !== '';

        // On sub-pages (Facebook, Instagram, Snapchat, About, Privacy, Terms, Universal),
        // clicking Home/Logo returns to the already open main page tab and closes the current tab
        if (isSubPage) {
            document.querySelectorAll('.nav-brand-home, .nav-brand, .sidebar a[href*="index.html"]').forEach(link => {
                link.addEventListener('click', (e) => {
                    const href = link.getAttribute('href');
                    if (href && (href === 'index.html' || href.endsWith('/index.html') || href === '../index.html' || href.includes('downsocial.net'))) {
                        e.preventDefault();

                        // 1. If opened from parent main page tab, focus parent tab & close this tab
                        if (window.opener && !window.opener.closed) {
                            try {
                                window.opener.focus();
                                window.close();
                                return;
                            } catch (err) {
                                console.warn('Could not focus opener tab:', err);
                            }
                        }

                        // 2. Try closing window directly
                        try {
                            window.close();
                        } catch (err) {}

                        // 3. Fallback if browser blocked close (e.g. direct URL entry): navigate back or go to link.href / main index.html
                        setTimeout(() => {
                            if (!window.closed) {
                                if (window.history.length > 1) {
                                    window.history.back();
                                } else {
                                    window.location.href = link.href || (window.location.pathname.split('/').filter(Boolean).length > 1 ? '../index.html' : 'index.html');
                                }
                            }
                        }, 100);
                    }
                });
            });
        }
    }


    bindContactForm() {
        const form = document.getElementById('contactForm');
        if (form) {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                const alertBox = document.getElementById('contactAlert') || document.querySelector('.form-alert');
                const btn = form.querySelector('.submit-btn');
                const origText = btn ? btn.innerHTML : 'Send Message';
                
                if (btn) {
                    btn.disabled = true;
                    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
                }
                
                setTimeout(() => {
                    if (alertBox) {
                        alertBox.style.display = 'block';
                        alertBox.className = 'form-alert success';
                        alertBox.innerHTML = '<i class="fas fa-check-circle"></i> Thank you! Your message has been received. Our dedicated platform team will respond within 24 hours.';
                    }
                    if (btn) {
                        btn.disabled = false;
                        btn.innerHTML = origText;
                    }
                    form.reset();
                    alertBox?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 700);
            });
        }
    }

    closeAllMenus() {
        document.getElementById('desktopLangMenu')?.classList.remove('active');
        document.getElementById('mobileLangMenu')?.classList.remove('active');
        document.getElementById('sidebar')?.classList.remove('active');
        document.getElementById('desktopNotifPanel')?.classList.remove('active');
        document.getElementById('mobileNotifPanel')?.classList.remove('active');
    }

    bindMenus() {
        const toggleMenu = (btnId, menuId, excludePanelId) => {
            const btn = document.getElementById(btnId);
            const menu = document.getElementById(menuId);
            if (btn && menu) {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    menu.classList.toggle('active');
                    if (excludePanelId) document.getElementById(excludePanelId)?.classList.remove('active');
                });
            }
        };

        toggleMenu('desktopLangToggle', 'desktopLangMenu', 'desktopNotifPanel');
        toggleMenu('mobileLangToggle', 'mobileLangMenu');

        document.getElementById('menuIcon')?.addEventListener('click', () => document.getElementById('sidebar')?.classList.add('active'));
        document.getElementById('closeBtn')?.addEventListener('click', () => document.getElementById('sidebar')?.classList.remove('active'));

        document.addEventListener('click', (e) => {
            const closeIfOutside = (btnId, panelId) => {
                const btn = document.getElementById(btnId), panel = document.getElementById(panelId);
                if (btn && panel && !btn.contains(e.target) && !panel.contains(e.target)) {
                    panel.classList.remove('active');
                }
            };
            closeIfOutside('desktopLangToggle', 'desktopLangMenu');
            closeIfOutside('desktopNotifToggle', 'desktopNotifPanel');
            closeIfOutside('mobileNotifToggle', 'mobileNotifPanel');
        });
    }

    bindNotifications() {
        const setup = (toggleId, panelId) => {
            const toggle = document.getElementById(toggleId), panel = document.getElementById(panelId);
            if (toggle && panel) {
                toggle.addEventListener('click', (e) => {
                    e.preventDefault();
                    panel.classList.toggle('active');
                    const dot = toggle.querySelector('.notif-dot');
                    if (dot) dot.style.display = 'none';
                    if (toggleId === 'desktopNotifToggle') document.getElementById('desktopLangMenu')?.classList.remove('active');
                });
            }
        };

        setup('desktopNotifToggle', 'desktopNotifPanel');
        setup('mobileNotifToggle', 'mobileNotifPanel');

        document.querySelectorAll('.expandable-notif').forEach(notif => {
            notif.addEventListener('click', function () { this.classList.toggle('active'); });
            notif.querySelector('.notif-content')?.addEventListener('click', e => e.stopPropagation());
        });
    }

    bindExpandableBoxes() {
        document.querySelectorAll('.expandable-box').forEach(box => {
            box.addEventListener('click', function () {
                const isActive = this.classList.contains('active');
                const transMgr = window.translationManager;

                document.querySelectorAll('.expandable-box').forEach(b => {
                    b.classList.remove('active');
                    const btnText = b.querySelector('.more-details-text');
                    const icon = b.querySelector('.more-details-btn i');
                    if (btnText) btnText.innerText = transMgr.getFlatTrans('moreDetails', "More Details");
                    if (icon) { icon.classList.remove('fa-chevron-up'); icon.classList.add('fa-chevron-down'); }
                });

                const container = document.getElementById('featuresContainer');
                if (!isActive) {
                    this.classList.add('active');
                    if (container) container.classList.add('has-active-box');

                    const btnText = this.querySelector('.more-details-text');
                    const icon = this.querySelector('.more-details-btn i');
                    if (btnText) btnText.innerText = transMgr.getFlatTrans('showLess', "Show Less");
                    if (icon) { icon.classList.remove('fa-chevron-down'); icon.classList.add('fa-chevron-up'); }
                } else {
                    if (container) container.classList.remove('has-active-box');
                }
            });
            box.querySelector('.blog-content')?.addEventListener('click', e => e.stopPropagation());
        });
    }

    bindAccordions() {
        document.querySelectorAll('.accordion-header').forEach(header => {
            const newHeader = header.cloneNode(true);
            header.parentNode.replaceChild(newHeader, header);

            newHeader.addEventListener('click', () => {
                const item = newHeader.parentElement;
                document.querySelectorAll('.accordion-item').forEach(other => {
                    if (other !== item) other.classList.remove('active');
                });
                item.classList.toggle('active');
            });
        });
    }

    bindHowToBtn(indexData) {
        const btn = document.getElementById('readMoreHowTo');
        const content = document.getElementById('howToHiddenContent');
        if (btn && content) {
            btn.addEventListener('click', () => {
                content.classList.toggle('expanded');
                btn.classList.toggle('expanded');
                btn.innerHTML = content.classList.contains('expanded')
                    ? `${indexData.readLessBtn} <i class="fas fa-chevron-up"></i>`
                    : `${indexData.readMoreBtn} <i class="fas fa-chevron-down"></i>`;
            });
        }
    }

    enforceNewTabLinks() {
        document.querySelectorAll('.footer-btn').forEach(link => {
            const href = link.getAttribute('href');
            if (href && !href.includes('mailto:')) {
                link.removeAttribute('target');
                link.removeAttribute('rel');
            }
        });
    }
}

// ---------------------------------------------------------
// 3. Download Manager (Handles API Fetching & Results UI)
// ---------------------------------------------------------
class DownloadManager {
    constructor() {
        const isLocalHost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
        this.baseUrl = isLocalHost ? "http://127.0.0.1:5000" : "https://video-downloader-uvw1.onrender.com";
        this.btn = document.getElementById('downloadBtn');
        this.input = document.getElementById('videoUrl');
        this.status = document.getElementById('statusMessage');
        this.card = document.getElementById('resultCard');
        this.videoPreview = document.getElementById('videoPreview');
        this.imagePreview = document.getElementById('imagePreview');

        this.historyKey = 'fb_video_history';
        this.createSuggestionBox();
    }

    init() {
        if (this.btn && this.input) {
            this.btn.addEventListener('click', () => this.processDownload());
            this.bindHistoryEvents();
        }
    }

    createSuggestionBox() {
        this.suggestionBox = document.createElement('div');
        this.suggestionBox.className = 'suggestion-box';

        const inputGroup = document.querySelector('.input-group');
        if (inputGroup) {
            inputGroup.style.position = 'relative';
            inputGroup.appendChild(this.suggestionBox);
        }
    }

    bindHistoryEvents() {
        this.input.addEventListener('focus', () => this.showSuggestions());
        this.input.addEventListener('click', () => this.showSuggestions());

        document.addEventListener('click', (e) => {
            if (!this.input.contains(e.target) && !this.suggestionBox.contains(e.target)) {
                this.hideSuggestions();
            }
        });

        window.addEventListener('resize', () => {
            if (this.suggestionBox.classList.contains('active')) {
                this.positionSuggestionBox();
            }
        });
    }

    showSuggestions() {
        let history = JSON.parse(localStorage.getItem(this.historyKey) || '[]');
        if (history.length === 0) {
            this.hideSuggestions();
            return;
        }

        this.suggestionBox.innerHTML = '';
        history.forEach(url => {
            const item = document.createElement('div');
            item.className = 'suggestion-item';
            
            const icon = document.createElement('i');
            icon.className = 'fas fa-history';
            
            const textSpan = document.createElement('span');
            textSpan.textContent = url;
            
            item.appendChild(icon);
            item.appendChild(textSpan);
            
            item.addEventListener('click', () => {
                this.input.value = url;
                this.hideSuggestions();
            });
            this.suggestionBox.appendChild(item);
        });

        this.suggestionBox.classList.add('active');
        this.positionSuggestionBox();
    }

    positionSuggestionBox() {
        if (!this.input || !this.suggestionBox) return;
        this.suggestionBox.style.top = `${this.input.offsetTop + this.input.offsetHeight + 5}px`;
        this.suggestionBox.style.left = `${this.input.offsetLeft}px`;
        this.suggestionBox.style.width = `${this.input.offsetWidth}px`;
    }

    hideSuggestions() {
        if (this.suggestionBox) {
            this.suggestionBox.classList.remove('active');
        }
    }

    saveToHistory(url) {
        let history = JSON.parse(localStorage.getItem(this.historyKey) || '[]');
        history = history.filter(item => item !== url);
        history.unshift(url);
        if (history.length > 3) history = history.slice(0, 3);
        localStorage.setItem(this.historyKey, JSON.stringify(history));
    }

    async processDownload() {
        const url = this.input.value.trim();
        const transMgr = window.translationManager;

        if (!url) {
            alert(transMgr.getFlatTrans('emptyLinkAlert', "Please paste a link first!"));
            return;
        }

        this.saveToHistory(url);
        this.hideSuggestions();
        this.input.value = '';
        this.input.blur();

        const origText = this.btn.innerHTML;
        this.btn.innerHTML = `${transMgr.getFlatTrans('processing', "Processing...")} <i class='fas fa-spinner fa-spin'></i>`;
        this.btn.disabled = true;
        this.resetUI();

        try {
            const res = await fetch(`${this.baseUrl}/api/download?url=${encodeURIComponent(url)}`);

            // Checking if response is actually JSON and not an HTML error page
            const contentType = res.headers.get("content-type");
            if (!contentType || !contentType.includes("application/json")) {
                console.error("Backend crashed and returned HTML instead of JSON.");
                this.onError("Backend server crashed. Please check Render logs.");
                return;
            }

            const data = await res.json();

            if (res.ok && data.success) {
                this.onSuccess(data, transMgr);
            } else {
                this.onError(data.error || "Extraction failed.");
            }

        } catch (err) {
            console.error("Network/Fetch Error:", err);
            // This happens if CORS fails or server is completely down
            this.onError("Connection blocked or Server is down. Check CORS policy.");
        } finally {
            this.btn.innerHTML = origText;
            this.btn.disabled = false;
        }
    }

    resetUI() {
        if (this.card) this.card.style.display = "none";
        if (this.status) this.status.style.display = "none";
        if (this.videoPreview) {
            this.videoPreview.pause();
            this.videoPreview.removeAttribute('src');
        }
    }

    onSuccess(data, transMgr) {
        if (this.card) this.card.style.display = "block";

        const isImg = data.type === "image";
        // TikTok CDN URLs have CORS restrictions — they cannot be played
        // directly in an HTML5 <video> tag from a different origin.
        const inputUrl = (this.input && this.input._lastUrl) || '';
        const isTikTok = data.platform === 'tiktok' ||
            (data.video_high && data.video_high.includes('tiktok')) ||
            (data.video_high && data.video_high.includes('tiktokv'));

        if (this.videoPreview) this.videoPreview.style.display = "none";
        if (this.imagePreview) this.imagePreview.style.display = "none";

        // Remove any old TikTok notice
        const oldNotice = this.card && this.card.querySelector('.tiktok-preview-notice');
        if (oldNotice) oldNotice.remove();

        if (isImg && this.imagePreview) {
            this.imagePreview.style.display = "block";
            this.imagePreview.src = data.video_high;
        } else if (isTikTok) {
            // Show a clean notice instead of the broken black video player
            const notice = document.createElement('div');
            notice.className = 'tiktok-preview-notice';
            notice.style.cssText = `
                display:flex; flex-direction:column; align-items:center; justify-content:center;
                gap:10px; padding:24px 16px; border-radius:12px;
                background:linear-gradient(135deg,#010101 0%,#1a1a1a 100%);
                border:1px solid rgba(255,255,255,0.08);
                text-align:center; margin-bottom:12px;
            `;
            notice.innerHTML = `
                <img src="https://www.tiktok.com/favicon.ico" width="32" height="32"
                     style="border-radius:8px;" onerror="this.style.display='none'">
                <div style="font-size:1rem;font-weight:600;color:#fff;">
                    📲 TikTok Video Ready!
                </div>
                <div style="font-size:0.82rem;color:rgba(255,255,255,0.55);max-width:240px;line-height:1.5;">
                    Preview is not available for TikTok.<br>
                    Click <strong style="color:#fe2c55;">Video (HD)</strong> or <strong style="color:#fe2c55;">Video (Normal)</strong> below to download and watch.
                </div>
            `;
            // Insert before the download buttons row
            const btnsRow = this.card.querySelector('.download-btns') ||
                            this.card.querySelector('.btn-row') ||
                            this.card.querySelector('#btnVidHigh')?.parentElement;
            if (btnsRow) {
                this.card.insertBefore(notice, btnsRow);
            } else {
                this.card.prepend(notice);
            }
        } else {
            // Normal preview for YouTube, Facebook, Instagram, etc.
            if (this.videoPreview) {
                this.videoPreview.style.display = "block";
                this.videoPreview.src = data.video_normal || data.video_high;
            }
        }

        this.configureDownloadLinks(data, isImg, transMgr);
        this.showStatus(transMgr.getFlatTrans('successMsg', "✅ Ready!"), "#4ade80");
    }

    configureDownloadLinks(data, isImg, transMgr) {
        const setLink = (id, url, type, quality = '', label = 'Media') => {
            const el = document.getElementById(id);
            if (el && url) {
                const uniqueId = Math.floor(Date.now() / 1000);
                const prefix = type === 'mp3' ? 'DownSocial_Audio' : (isImg ? 'DownSocial_Image' : 'DownSocial_Video');
                const fileName = `${prefix}_${uniqueId}.${type}`;
                const qParam = quality ? `&q=${quality}` : '';
                el.href = `${this.baseUrl}/api/direct?url=${encodeURIComponent(url)}&type=${type}&t=${uniqueId}${qParam}`;
                el.setAttribute('download', fileName);

                // Bind interactive animated progress line and floating PIP download popup
                this.bindDownloadAnimation(el, label, type, fileName);
            }
        };

        const btnAudHigh = document.getElementById('btnAudHigh');
        const btnAudNorm = document.getElementById('btnAudNorm');
        const btnVidNorm = document.getElementById('btnVidNorm');
        const btnVidHigh = document.getElementById('btnVidHigh');

        if (isImg) {
            [btnAudHigh, btnAudNorm, btnVidNorm].forEach(b => { if (b) b.style.display = "none"; });
            if (btnVidHigh) {
                btnVidHigh.innerHTML = '<i class="fas fa-image"></i> Download Image';
                setLink('btnVidHigh', data.video_high, 'jpg', '', 'Image (Full HD)');
            }
        } else {
            [btnAudHigh, btnAudNorm, btnVidNorm].forEach(b => { if (b) b.style.display = "flex"; });
            if (btnVidHigh) {
                btnVidHigh.innerHTML = `<i class="fas fa-video"></i> <span data-key="dlVidHigh">${transMgr.getFlatTrans('dlVidHigh', 'Video (HD)')}</span>`;
            }

            setLink('btnVidHigh', data.video_high, 'mp4', 'hd', 'Video (HD 1080p)');
            setLink('btnVidNorm', data.video_normal, 'mp4', 'sd', 'Video (Normal 720p)');
            setLink('btnAudHigh', data.audio_high, 'mp3', 'hq', 'Audio (HQ 320kbps)');
            setLink('btnAudNorm', data.audio_normal, 'mp3', 'normal', 'Audio (Normal MP3)');
        }
    }

    bindDownloadAnimation(btn, label, type, fileName) {
        if (!btn || btn._hasDownloadHandler) return;
        btn._hasDownloadHandler = true;

        btn.addEventListener('click', (e) => {
            // 1. Ensure capsule progress line is inside the button (matches @codewith_muhilan reel)
            let progressLine = btn.querySelector('.btn-progress-line');
            if (!progressLine) {
                progressLine = document.createElement('div');
                progressLine.className = 'btn-progress-line';
                btn.appendChild(progressLine);
            }

            // Save original button contents
            const originalHTML = btn.innerHTML;
            btn.classList.add('is-downloading');

            // 2. Launch floating PIP progress toast
            this.showDownloadPipModal(label, type, fileName);

            // 3. Smooth animated progress (0% -> 95%)
            let progress = 10;
            if (progressLine) progressLine.style.width = '10%';
            this.updateDownloadPipProgress(10, false);

            const progressTimer = setInterval(() => {
                progress += Math.floor(Math.random() * 15) + 12;
                if (progress > 95) progress = 95;
                if (progressLine) progressLine.style.width = `${progress}%`;
                this.updateDownloadPipProgress(progress, false);
            }, 140);

            // 4. Complete state when browser receives direct stream
            setTimeout(() => {
                clearInterval(progressTimer);
                if (progressLine) progressLine.style.width = '100%';
                this.updateDownloadPipProgress(100, true);

                btn.classList.remove('is-downloading');
                btn.classList.add('is-downloaded');
                btn.innerHTML = `<i class="fas fa-check-circle" style="color:#ffffff;"></i> <span>Downloaded! ✓</span>`;

                // 5. Restore original button after 3.5 seconds
                setTimeout(() => {
                    btn.classList.remove('is-downloaded');
                    if (progressLine) progressLine.style.width = '0%';
                    btn.innerHTML = originalHTML;
                }, 3500);
            }, 1800);
        });
    }

    showDownloadPipModal(label, type, fileName) {
        let toast = document.getElementById('downloadPipToast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'downloadPipToast';
            toast.className = 'download-pip-toast';
            document.body.appendChild(toast);
        }

        const iconClass = type === 'mp3' ? 'fa-headphones' : 'fa-video';
        const typeBadge = type === 'mp3' ? 'Audio MP3' : (type === 'jpg' ? 'Image HD' : 'Video MP4');

        toast.className = 'download-pip-toast show';
        toast.innerHTML = `
            <div class="pip-header">
                <div class="pip-badge">
                    <span class="pip-spinner"></span>
                    <span id="pipStatusTitle">Downloading ${typeBadge}</span>
                </div>
                <button class="pip-close-btn" id="pipCloseBtn" aria-label="Close">&times;</button>
            </div>
            <div class="pip-body">
                <div class="pip-content-meta">
                    <span class="pip-filename"><i class="fas ${iconClass}"></i> ${label || 'Media File'}</span>
                    <span class="pip-percent-text" id="pipPercentText">15%</span>
                </div>
                <div class="pip-track">
                    <div class="pip-fill" id="pipFillBar" style="width: 15%;"></div>
                </div>
                <div class="pip-status-hint" id="pipStatusHint">
                    <i class="fas fa-bolt"></i> Preparing direct high-speed download...
                </div>
            </div>
        `;

        const closeBtn = toast.querySelector('#pipCloseBtn');
        if (closeBtn) {
            closeBtn.onclick = () => {
                toast.classList.remove('show');
            };
        }

        if (this._pipDismissTimer) clearTimeout(this._pipDismissTimer);
    }

    updateDownloadPipProgress(percent, isComplete = false) {
        const toast = document.getElementById('downloadPipToast');
        if (!toast || !toast.classList.contains('show')) return;

        const fill = toast.querySelector('#pipFillBar');
        const text = toast.querySelector('#pipPercentText');
        const title = toast.querySelector('#pipStatusTitle');
        const hint = toast.querySelector('#pipStatusHint');

        if (fill) fill.style.width = `${percent}%`;
        if (text) text.textContent = `${percent}%`;

        if (isComplete) {
            toast.classList.add('is-success');
            if (title) title.innerHTML = `<i class="fas fa-check-circle" style="color:#38bdf8;"></i> Download Started!`;
            if (hint) hint.innerHTML = `<i class="fas fa-folder-open" style="color:#38bdf8;"></i> File saved to your Downloads folder!`;

            this._pipDismissTimer = setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => {
                    toast.classList.remove('is-success');
                }, 400);
            }, 4000);
        } else if (percent > 65) {
            if (hint) hint.innerHTML = `<i class="fas fa-cloud-arrow-down" style="color:#38bdf8;"></i> Finalizing media download...`;
        }
    }

    onError(msg) {
        this.showStatus(`❌ ${msg}`, "#ff4757");
    }

    showStatus(msg, color) {
        if (this.status) {
            this.status.style.display = "block";
            this.status.style.color = color;
            this.status.innerHTML = msg;
        }
    }
}

// ---------------------------------------------------------
// Theme Manager (Handles 3-Mode Sliding Segmented Themes)
// ---------------------------------------------------------
class ThemeManager {
    constructor() {
        this.currentTheme = localStorage.getItem('siteTheme') || 'dark';
    }

    init() {
        this.applyTheme(this.currentTheme, false);
        this.bindEvents();

        window.addEventListener('resize', () => this.updatePillPositions());
        if (document.fonts && document.fonts.ready) {
            document.fonts.ready.then(() => this.updatePillPositions());
        }
        setTimeout(() => this.updatePillPositions(), 30);
        setTimeout(() => this.updatePillPositions(), 150);
        setTimeout(() => this.updatePillPositions(), 500);
    }

    applyTheme(theme, animate = true) {
        if (!['premium', 'dark', 'light'].includes(theme)) {
            theme = 'dark';
        }
        this.currentTheme = theme;
        localStorage.setItem('siteTheme', theme);
        document.documentElement.setAttribute('data-theme', theme);
        document.body.setAttribute('data-theme', theme);

        this.updatePillPositions();
    }

    updatePillPositions() {
        document.querySelectorAll('[data-theme-switcher]').forEach(switcher => {
            const pill = switcher.querySelector('.theme-pill');
            const btns = switcher.querySelectorAll('.theme-btn');
            let activeBtn = null;

            btns.forEach((btn) => {
                const btnTheme = btn.getAttribute('data-theme-val');
                if (btnTheme === this.currentTheme) {
                    btn.classList.add('active');
                    activeBtn = btn;
                } else {
                    btn.classList.remove('active');
                }
            });

            if (pill && activeBtn) {
                const left = activeBtn.offsetLeft;
                const top = activeBtn.offsetTop;
                const width = activeBtn.offsetWidth;
                const height = activeBtn.offsetHeight;

                pill.style.width = `${width}px`;
                pill.style.height = `${height}px`;
                pill.style.transform = `translate(${left}px, ${top}px)`;
                pill.style.opacity = '1';
            }
        });
    }

    bindEvents() {
        document.querySelectorAll('[data-theme-switcher] .theme-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const targetTheme = btn.getAttribute('data-theme-val');
                this.applyTheme(targetTheme, true);
            });
        });
    }
}

// ---------------------------------------------------------
// 4. Initialization & Global Expose
// ---------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    window.themeManager = new ThemeManager();
    window.translationManager = new TranslationManager();
    window.uiManager = new UIManager();
    window.downloadManager = new DownloadManager();

    window.themeManager.init();
    window.uiManager.init();
    window.downloadManager.init();

    window.translationManager.changeLanguage(window.translationManager.currentLang);

    window.changeLanguage = (lang) => {
        window.translationManager.changeLanguage(lang);
    };

    window.changeTheme = (theme) => {
        window.themeManager.applyTheme(theme, true);
    };
});