import re

file_path = r'c:\my folder\Pictures\Desktop\downsocial\frontend\shared\script.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update changeLanguage to try locales/${lang}.json, then ../shared/locales/${lang}.json
old_fetch = """        if (!this.cache[lang]) {
            try {
                const response = await fetch(`locales/${lang}.json`);
                if (!response.ok) throw new Error('Translation file not found');
                this.cache[lang] = await response.json();
            } catch (error) {
                console.error('Error loading language:', error);
                if (lang !== 'en') this.changeLanguage('en'); // Fallback
                return;
            }
        }"""

new_fetch = """        if (!this.cache[lang]) {
            try {
                let response = await fetch(`locales/${lang}.json`);
                if (!response.ok) {
                    response = await fetch(`../shared/locales/${lang}.json`);
                }
                if (!response.ok) throw new Error('Translation file not found');
                this.cache[lang] = await response.json();
            } catch (error) {
                console.error('Error loading language:', error);
                if (lang !== 'en') this.changeLanguage('en'); // Fallback
                return;
            }
        }"""

if old_fetch in content:
    content = content.replace(old_fetch, new_fetch)
    print("Replaced translation fetch logic")
else:
    print("Old fetch logic not found exactly, checking regex...")

# 2. Add bindContactForm() to UIManager
if "this.bindContactForm();" not in content:
    content = content.replace("this.bindHomeNavigation();", "this.bindHomeNavigation();\n        this.bindContactForm();")
    
contact_form_code = """
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
"""

if "bindContactForm() {" not in content:
    # Insert right before closeAllMenus()
    content = content.replace("    closeAllMenus() {", contact_form_code + "\n    closeAllMenus() {")
    print("Added bindContactForm()")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated frontend/shared/script.js successfully!")
