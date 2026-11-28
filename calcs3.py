# -*- coding: utf-8 -*-
# Savings-scheme calculators (rates: Oct-Dec 2026 quarter). Rates are editable inputs because the government resets them every quarter.
from calcs2 import F
_N = "यह सिर्फ़ अंदाज़ा है। दर हर तिमाही बदल सकती है और असली रकम डाकघर/बैंक के हिसाब से थोड़ी अलग हो सकती है। टैक्स शामिल नहीं है।"
_NE = "This is only an estimate. The rate can change every quarter and the actual amount can differ slightly at the post office/bank. Tax is not included."
CALCS = [
 dict(slug="ppf-calculator", icon="🏦", scheme="ppf-public-provident-fund",
  fields=[F("am","num",150000,mn=0),F("rt","num",7.1,step=0.1,mn=0),F("yr","num",15,mn=1)],
  js='''if(v.am<500)return "<p class=note>"+L.min+"</p>";if(v.am>150000)return "<p class=note>"+L.max+"</p>";
var b=0,y=Math.max(1,Math.round(v.yr));for(var i=0;i<y;i++){b=(b+v.am)*(1+v.rt/100)}
var d=v.am*y;
return "<div class=facts><div><span>"+L.r1+"</span><b>"+fm(b)+"</b></div><div><span>"+L.r2+"</span><b>"+fm(d)+"</b></div><div><span>"+L.r3+"</span><b>"+fm(b-d)+"</b></div></div>";''',
  hi=dict(h1="PPF कैलकुलेटर", desc="PPF में हर साल जमा करने पर 15 साल (या ज़्यादा) बाद अंदाज़न रकम देखें।",
   lead="सालाना जमा, ब्याज दर और साल डालिए। मैच्योरिटी पर अंदाज़न रकम और कुल ब्याज दिख जाएगा।",
   labels=["सालाना जमा (₹500 से ₹1,50,000)","ब्याज दर (% सालाना)","कितने साल"],
   hint=[None,"अभी 7.1% है (अक्टूबर–दिसंबर 2026)। हर तिमाही बदल सकती है।","न्यूनतम अवधि 15 साल है; बढ़ाने पर ज़्यादा साल डाल सकते हैं।"],
   btn="हिसाब लगाएँ", note=_N+" हिसाब में साल की शुरुआत में पूरी रकम जमा मानी गई है।",
   rh="PPF की मुख्य बातें", rules=["साल में ₹500 से ₹1,50,000 तक जमा।","ब्याज साल में एक बार जुड़ता है।","5 पूरे वित्त वर्ष बाद आंशिक निकासी।","15 साल बाद 5-5 साल के ब्लॉक में बढ़ा सकते हैं।"],
   see="PPF की पूरी जानकारी पढ़ें →",
   js=dict(min="सालाना जमा कम से कम ₹500 होनी चाहिए।",max="सालाना जमा ₹1,50,000 से ज़्यादा नहीं हो सकती।",r1="अंदाज़न कुल रकम",r2="कुल जमा",r3="अनुमानित ब्याज")),
  en=dict(h1="PPF Calculator", desc="Estimate the PPF amount after 15 years (or more) for a yearly deposit.",
   lead="Enter the yearly deposit, the interest rate and the number of years. You will see the approximate maturity amount and total interest.",
   labels=["Yearly deposit (₹500 to ₹1,50,000)","Interest rate (% per year)","Number of years"],
   hint=[None,"It is 7.1% now (Oct–Dec 2026). It can change every quarter.","The minimum term is 15 years; enter more years if you extend."],
   btn="Calculate", note=_NE+" The calculation assumes the full amount is deposited at the start of each year.",
   rh="Key points of PPF", rules=["Deposit ₹500 to ₹1,50,000 a year.","Interest is compounded once a year.","Partial withdrawal after 5 complete financial years.","Extendable in 5-year blocks after 15 years."],
   see="Read the full PPF details →",
   js=dict(min="The yearly deposit must be at least ₹500.",max="The yearly deposit cannot exceed ₹1,50,000.",r1="Approx. total amount",r2="Total deposited",r3="Estimated interest"))),

 dict(slug="scss-interest-calculator", icon="👴", scheme="scss-senior-citizen-savings-scheme",
  fields=[F("am","num",1000000,step=1000,mn=0),F("rt","num",8.2,step=0.1,mn=0)],
  js='''if(v.am<1000)return "<p class=note>"+L.min+"</p>";if(v.am>3000000)return "<p class=note>"+L.max+"</p>";
var q=v.am*v.rt/400;
return "<div class=facts><div><span>"+L.r1+"</span><b>"+fm(q)+"</b></div><div><span>"+L.r2+"</span><b>"+fm(q*4)+"</b></div><div><span>"+L.r3+"</span><b>"+fm(q*20)+"</b></div></div>";''',
  hi=dict(h1="SCSS ब्याज कैलकुलेटर (वरिष्ठ नागरिक बचत योजना)", desc="वरिष्ठ नागरिक बचत योजना में जमा रकम पर हर तिमाही, साल भर और 5 साल में मिलने वाला ब्याज देखें।",
   lead="जमा रकम और ब्याज दर डालिए। हर तिमाही का ब्याज, सालाना ब्याज और 5 साल का कुल ब्याज दिखेगा।",
   labels=["जमा रकम (₹, अधिकतम ₹30 लाख)","ब्याज दर (% सालाना)"],
   hint=[None,"अभी 8.2% है (अक्टूबर–दिसंबर 2026)। हर तिमाही बदल सकती है।"],
   btn="हिसाब लगाएँ", note=_N+" यहाँ साधारण ब्याज माना गया है, क्योंकि SCSS का ब्याज हर तिमाही निकल जाता है।",
   rh="SCSS की मुख्य बातें", rules=["₹1,000 के गुणक में अधिकतम ₹30 लाख।","5 साल की अवधि, 3 साल बढ़ाने का विकल्प।","ब्याज हर तिमाही मिलता है।","उम्र 60+ (कुछ रिटायर्ड लोगों के लिए 55+ या 50+)।"],
   see="SCSS की पूरी जानकारी पढ़ें →",
   js=dict(min="जमा कम से कम ₹1,000 होनी चाहिए।",max="अधिकतम जमा ₹30 लाख है।",r1="हर तिमाही का ब्याज",r2="एक साल का ब्याज",r3="5 साल का कुल ब्याज")),
  en=dict(h1="SCSS Interest Calculator (Senior Citizens Savings Scheme)", desc="See the quarterly, yearly and 5-year interest on a Senior Citizens Savings Scheme deposit.",
   lead="Enter the deposit and the interest rate. You will see the quarterly interest, the yearly interest and the 5-year total.",
   labels=["Deposit (₹, maximum ₹30 lakh)","Interest rate (% per year)"],
   hint=[None,"It is 8.2% now (Oct–Dec 2026). It can change every quarter."],
   btn="Calculate", note=_NE+" Simple interest is assumed because SCSS interest is paid out every quarter.",
   rh="Key points of SCSS", rules=["Maximum ₹30 lakh in multiples of ₹1,000.","5-year term, option to extend by 3 years.","Interest is paid every quarter.","Age 60+ (55+ or 50+ for some retirees)."],
   see="Read the full SCSS details →",
   js=dict(min="The deposit must be at least ₹1,000.",max="The maximum deposit is ₹30 lakh.",r1="Interest every quarter",r2="Interest for one year",r3="Total interest over 5 years"))),

 dict(slug="pomis-monthly-income-calculator", icon="📮", scheme="post-office-monthly-income-scheme",
  fields=[F("am","num",900000,step=1000,mn=0),F("rt","num",7.4,step=0.1,mn=0)],
  js='''if(v.am<1000)return "<p class=note>"+L.min+"</p>";if(v.am>1500000)return "<p class=note>"+L.max+"</p>";
var m=v.am*v.rt/1200;
return "<div class=facts><div><span>"+L.r1+"</span><b>"+fm(m)+"</b></div><div><span>"+L.r2+"</span><b>"+fm(m*12)+"</b></div><div><span>"+L.r3+"</span><b>"+fm(m*60)+"</b></div></div>"+(v.am>900000?"<p class=note>"+L.warn+"</p>":"");''',
  hi=dict(h1="डाकघर मासिक आय योजना (POMIS) कैलकुलेटर", desc="POMIS में जमा रकम पर हर महीने मिलने वाली अंदाज़न आय और 5 साल का कुल ब्याज देखें।",
   lead="जमा रकम और ब्याज दर डालिए। हर महीने की आय, साल भर की आय और 5 साल का कुल ब्याज दिखेगा।",
   labels=["जमा रकम (₹)","ब्याज दर (% सालाना)"],
   hint=["अकेले खाते में अधिकतम ₹9 लाख, जॉइंट में ₹15 लाख।","अभी 7.4% है (अक्टूबर–दिसंबर 2026)। हर तिमाही बदल सकती है।"],
   btn="हिसाब लगाएँ", note=_N,
   rh="POMIS की मुख्य बातें", rules=["अकेले ₹9 लाख, जॉइंट ₹15 लाख तक।","5 साल की अवधि।","ब्याज हर महीने मिलता है।","ब्याज पर टैक्स लगता है, 80C की छूट नहीं।"],
   see="POMIS की पूरी जानकारी पढ़ें →",
   js=dict(min="जमा कम से कम ₹1,000 होनी चाहिए।",max="जॉइंट खाते की अधिकतम सीमा ₹15 लाख है।",warn="₹9 लाख से ऊपर की रकम सिर्फ़ जॉइंट खाते में जमा हो सकती है।",r1="हर महीने की आय",r2="एक साल की आय",r3="5 साल का कुल ब्याज")),
  en=dict(h1="Post Office Monthly Income Scheme (POMIS) Calculator", desc="See the approximate monthly income and the 5-year total interest on a POMIS deposit.",
   lead="Enter the deposit and the interest rate. You will see the monthly income, the yearly income and the 5-year total interest.",
   labels=["Deposit (₹)","Interest rate (% per year)"],
   hint=["Maximum ₹9 lakh in a single account, ₹15 lakh in a joint one.","It is 7.4% now (Oct–Dec 2026). It can change every quarter."],
   btn="Calculate", note=_NE,
   rh="Key points of POMIS", rules=["Up to ₹9 lakh single, ₹15 lakh joint.","5-year term.","Interest is paid every month.","Interest is taxable, no 80C deduction."],
   see="Read the full POMIS details →",
   js=dict(min="The deposit must be at least ₹1,000.",max="The maximum for a joint account is ₹15 lakh.",warn="An amount above ₹9 lakh can only be deposited in a joint account.",r1="Monthly income",r2="Income for one year",r3="Total interest over 5 years"))),

 dict(slug="nsc-calculator", icon="📜", scheme="nsc-national-savings-certificate",
  fields=[F("am","num",100000,step=1000,mn=0),F("rt","num",7.7,step=0.1,mn=0)],
  js='''if(v.am<1000)return "<p class=note>"+L.min+"</p>";
var t=v.am*Math.pow(1+v.rt/100,5);
return "<div class=facts><div><span>"+L.r1+"</span><b>"+fm(t)+"</b></div><div><span>"+L.r2+"</span><b>"+fm(v.am)+"</b></div><div><span>"+L.r3+"</span><b>"+fm(t-v.am)+"</b></div></div>";''',
  hi=dict(h1="NSC कैलकुलेटर (राष्ट्रीय बचत पत्र)", desc="NSC में निवेश करने पर 5 साल बाद मैच्योरिटी पर मिलने वाली अंदाज़न रकम देखें।",
   lead="निवेश की रकम और ब्याज दर डालिए। 5 साल बाद अंदाज़न रकम और कुल ब्याज दिख जाएगा।",
   labels=["निवेश (₹, न्यूनतम ₹1,000)","ब्याज दर (% सालाना)"],
   hint=[None,"अभी 7.7% है (अक्टूबर–दिसंबर 2026)। जिस तिमाही में खरीदेंगे, उसी की दर लागू होती है।"],
   btn="हिसाब लगाएँ", note=_N+" ब्याज सालाना कंपाउंड मानकर 5 साल का हिसाब है।",
   rh="NSC की मुख्य बातें", rules=["न्यूनतम ₹1,000, कोई ऊपरी सीमा नहीं।","5 साल की अवधि।","ब्याज सालाना जुड़ता है, मैच्योरिटी पर मिलता है।","धारा 80C की छूट (₹1.5 लाख तक)।"],
   see="NSC की पूरी जानकारी पढ़ें →",
   js=dict(min="निवेश कम से कम ₹1,000 होना चाहिए।",r1="5 साल बाद अंदाज़न रकम",r2="निवेश",r3="अनुमानित ब्याज")),
  en=dict(h1="NSC Calculator (National Savings Certificate)", desc="Estimate the amount you get at maturity after 5 years on an NSC investment.",
   lead="Enter the investment and the interest rate. You will see the approximate amount after 5 years and the total interest.",
   labels=["Investment (₹, minimum ₹1,000)","Interest rate (% per year)"],
   hint=[None,"It is 7.7% now (Oct–Dec 2026). The rate of the quarter in which you buy applies."],
   btn="Calculate", note=_NE+" The calculation assumes annual compounding over 5 years.",
   rh="Key points of NSC", rules=["Minimum ₹1,000, no upper limit.","5-year term.","Interest compounds yearly and is paid at maturity.","Section 80C deduction (up to ₹1.5 lakh)."],
   see="Read the full NSC details →",
   js=dict(min="The investment must be at least ₹1,000.",r1="Approx. amount after 5 years",r2="Investment",r3="Estimated interest"))),
]
