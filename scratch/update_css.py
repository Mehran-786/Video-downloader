import os

css_additions = """

/* ============================================================
   MULTI-PLATFORM EXPANSION STYLES (SHARED)
   ============================================================ */

/* 1. Page Content Wrapper & Article Container */
.page-content-wrapper {
    max-width: 1040px;
    margin: 40px auto 80px;
    padding: 0 20px;
}

.article-container {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 16px;
    padding: 40px;
    box-shadow: var(--card-shadow);
    color: var(--text-main);
    line-height: 1.7;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

.article-container h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 12px;
    background: var(--h1-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.25;
}

.article-container h2 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 600;
    margin: 32px 0 14px;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 10px;
}

.article-container h3 {
    font-size: 18px;
    font-weight: 600;
    margin: 22px 0 10px;
    color: var(--text-main);
}

.article-container p {
    color: var(--text-sub);
    font-size: 15px;
    margin-bottom: 18px;
}

.article-container ul, .article-container ol {
    margin: 14px 0 24px 24px;
    color: var(--text-sub);
    font-size: 15px;
}

.article-container li {
    margin-bottom: 8px;
}

.article-intro {
    font-size: 16px !important;
    color: var(--text-main) !important;
    font-weight: 500;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--card-border);
    margin-bottom: 30px !important;
}

/* 2. Platform Branding Accents & Badges */
.platform-pill-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    border-radius: 50px;
    font-size: 12.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 16px;
}

.badge-facebook { background: rgba(24, 119, 242, 0.15); color: #1877F2; border: 1px solid rgba(24, 119, 242, 0.35); }
.badge-instagram { background: rgba(228, 64, 95, 0.15); color: #E4405F; border: 1px solid rgba(228, 64, 95, 0.35); }
.badge-tiktok { background: rgba(0, 242, 254, 0.15); color: #00f2fe; border: 1px solid rgba(0, 242, 254, 0.35); }
.badge-youtube { background: rgba(255, 0, 0, 0.15); color: #FF0000; border: 1px solid rgba(255, 0, 0, 0.35); }
.badge-snapchat { background: rgba(255, 252, 0, 0.15); color: #e6e300; border: 1px solid rgba(255, 252, 0, 0.35); }
.badge-threads { background: rgba(255, 255, 255, 0.15); color: #ffffff; border: 1px solid rgba(255, 255, 255, 0.35); }
.badge-universal { background: rgba(99, 102, 241, 0.15); color: #818cf8; border: 1px solid rgba(99, 102, 241, 0.35); }

/* 3. Platform Contact Desk Styles */
.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1.3fr;
    gap: 30px;
    margin-top: 30px;
}

@media (max-width: 820px) {
    .contact-grid {
        grid-template-columns: 1fr;
    }
}

.contact-info-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--card-border);
    border-radius: 12px;
    padding: 28px;
}

.contact-info-list {
    list-style: none !important;
    margin: 20px 0 !important;
    padding: 0 !important;
}

.contact-info-list li {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 18px;
    font-size: 14px;
    color: var(--text-sub);
}

.contact-info-list li i {
    font-size: 18px;
    color: var(--accent-blue);
    margin-top: 3px;
    flex-shrink: 0;
}

.contact-sla-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    border-radius: 8px;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #10b981;
    font-size: 13px;
    font-weight: 600;
    margin-top: 10px;
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 18px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 7px;
}

.form-label {
    font-size: 13.5px;
    font-weight: 600;
    color: var(--text-main);
}

.form-input, .form-select, .form-textarea {
    width: 100%;
    padding: 12px 16px;
    border-radius: 10px;
    background: var(--input-bg);
    border: 1px solid var(--input-border);
    color: var(--input-text);
    font-family: inherit;
    font-size: 14px;
    outline: none;
    transition: all 0.25s ease;
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
    border-color: var(--accent-blue);
    box-shadow: 0 0 15px rgba(232, 41, 74, 0.25);
}

.form-textarea {
    min-height: 120px;
    resize: vertical;
}

.submit-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 13px 26px;
    border-radius: 10px;
    background: var(--accent-blue);
    color: #fff;
    font-size: 15px;
    font-weight: 700;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    align-self: flex-start;
}

.submit-btn:hover {
    background: var(--accent-hover);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(232, 41, 74, 0.35);
}

.form-alert {
    padding: 14px 18px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
    display: none;
}
.form-alert.success {
    display: block;
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.35);
    color: #10b981;
}

/* 4. Features Showcase Grid */
.features-detail-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 22px;
    margin: 30px 0;
}

.feature-detail-card {
    background: rgba(255, 255, 255, 0.025);
    border: 1px solid var(--card-border);
    border-radius: 12px;
    padding: 24px;
    transition: all 0.3s ease;
}

.feature-detail-card:hover {
    border-color: var(--card-hover-border);
    transform: translateY(-3px);
    box-shadow: var(--card-shadow);
}

.feature-detail-icon {
    font-size: 28px;
    color: var(--accent-blue);
    margin-bottom: 14px;
}

.feature-detail-card h3 {
    margin: 0 0 10px 0;
    font-size: 17px;
    color: var(--text-main);
}

.feature-detail-card p {
    margin: 0;
    font-size: 14px;
    color: var(--text-sub);
    line-height: 1.6;
}

/* 5. How-It-Works Steps Grid */
.how-it-works-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 22px;
    margin: 30px 0;
}

.step-card {
    background: rgba(255, 255, 255, 0.025);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    padding: 28px 22px;
    position: relative;
    text-align: center;
}

.step-number {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: var(--accent-blue);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 800;
    margin: 0 auto 16px;
    box-shadow: 0 4px 14px rgba(232, 41, 74, 0.4);
}

.step-card h3 {
    font-size: 17px;
    margin-bottom: 10px;
    color: var(--text-main);
}

.step-card p {
    font-size: 14px;
    color: var(--text-sub);
    margin: 0;
}

/* RTL Global Adjustments */
body[dir="rtl"] .article-container ul,
body[dir="rtl"] .article-container ol {
    margin: 14px 24px 24px 0;
}

body[dir="rtl"] .contact-info-list li {
    text-align: right;
}

body[dir="rtl"] .seo-table {
    text-align: right;
}
"""

style_file = r'c:\my folder\Pictures\Desktop\downsocial\frontend\shared\style.css'
with open(style_file, 'a', encoding='utf-8') as f:
    f.write(css_additions)

print('Updated frontend/shared/style.css with multi-platform expansion styles!')
