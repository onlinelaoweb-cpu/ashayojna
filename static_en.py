# -*- coding: utf-8 -*-
def get(SITE_NAME, UPD, CONTACT_EMAIL, e):
    return {
"about": ("About us", f'''<h1>About us</h1><div class="note" style="font-size:16px">🪔 <b>Dedication</b><br>This website is dedicated to my mother, <b>Asha ji</b>. "Asha" means hope, and that is our effort: that the right scheme information reaches every needy person and nobody's hope is lost to wrong information or fraud.</div><p><b>{e(SITE_NAME)}</b> is an independent website built to give ordinary people simple, trustworthy information on Central and State (all states of India; a few main schemes per state, with more being added) government schemes. Hindi is the main language and English is available as a second language.</p>
<h2>Our aim</h2><p>People often miss out on benefits because of incomplete or wrong information, or fall into the hands of fraudsters. We explain eligibility, documents and how to apply in simple language, with links to the official portals.</p>
<h2>What we are not</h2><p>We are not a government department, agency or authorised representative. We do not charge money for filling applications. The application and the final decision rest with the concerned government department or bank.</p>
<h2>Quality of information</h2><p>We write information after checking official portals and reliable sources, and show the date of last check on each page. If you spot a mistake, <a href="contact.html">tell us</a> and we will fix it soon.</p>'''),
"contact": ("Contact us", f'''<h1>Contact us</h1>{("<p>For a mistake in any information, a suggestion, or an advertising-related question, email us:</p><p class='hl'>✉️ "+e(CONTACT_EMAIL)+"</p>") if CONTACT_EMAIL else "<p>If you find a mistake or have a suggestion, please write to us. The contact email will be added on this page soon.</p>"}<p>We normally reply within a few working days. Please note that we cannot fill applications for you or push your case in a government department. For that, contact the concerned department's helpline or your nearest CSC.</p>'''),
"privacy-policy": ("Privacy Policy", f'''<h1>Privacy Policy</h1><p>Last updated: {UPD}</p>
<p>{e(SITE_NAME)} respects your privacy. This policy explains what information may be collected when you use the website.</p>
<h2>What information we collect</h2><p>We do not directly ask you for any personal information (name, Aadhaar, bank details etc.). If you email us, your email address is used only to reply.</p>
<h2>Log files and analytics</h2><p>Like most websites, server logs may record your IP address, browser type and time of visit. This is used to improve the site and for security.</p>
<h2>Cookies and advertising (Google AdSense)</h2><p>We may use third-party advertising services such as Google AdSense. Third-party vendors, including Google, may use cookies to serve ads based on your previous visits. Google's advertising cookies let the website and its partners show ads based on your visits across the internet. You can turn off personalised ads in <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a>.</p>
<h2>External links</h2><p>Our pages contain links to government and other websites. We have no control over those sites' privacy policies.</p>
<h2>Children's privacy</h2><p>We do not knowingly collect information from children under 13.</p>
<h2>Changes to this policy</h2><p>This policy may change from time to time. Changes will be published on this page.</p>
<h2>Contact</h2><p>If you have questions, see the <a href="contact.html">contact page</a>.</p>'''),
"disclaimer": ("Disclaimer", f'''<h1>Disclaimer</h1><p>Last updated: {UPD}</p>
<p><b>{e(SITE_NAME)}</b> is a private information website. It does not represent, and is not affiliated with, any government department, ministry or agency.</p>
<h2>Accuracy of information</h2><p>We try our best to keep information correct and up to date, but scheme rules, amounts and dates can be changed by the government at any time. So before applying to any scheme or putting in money, always confirm the information with the concerned <b>official website or department</b>.</p>
<h2>No advice</h2><p>The information here is for general awareness only. Do not treat it as legal, financial or medical advice.</p>
<h2>Beware of fraud</h2><p>Many fraudsters run fake calls, messages and websites in the name of government schemes. Official applications generally carry no fee. Do not share OTP, PIN, passwords or bank details with anyone.</p>
<h2>External links</h2><p>We are not responsible for the content of external websites.</p>
<h2>Advertising</h2><p>Third-party ads such as Google AdSense may appear on the website. We are not responsible for the advertised products or services.</p>'''),
    }
