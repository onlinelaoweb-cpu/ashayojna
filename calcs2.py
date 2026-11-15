# -*- coding: utf-8 -*-
# Generic calculators. Each: slug, icon, link(scheme slug), fields, js (body of function f(v,L,fm)->html string), and hi/en strings.
def F(id,kind,val=None,opts=None,step=None,mn=None):
    return dict(id=id,kind=kind,val=val,opts=opts,step=step,mn=mn)

CALCS = [
 dict(slug="nps-vatsalya-calculator", icon="👶", scheme="nps-vatsalya-yojana",
  fields=[F("am","num",1000,mn=0),F("age","num",0,mn=0),F("rt","num",10,step=0.5,mn=0)],
  js='''var n=Math.max(0,18-v.age)*12,r=v.rt/1200,b=0,d=0;for(var i=0;i<n;i++){b=(b+v.am)*(1+r);d+=v.am}
var b60=b*Math.pow(1+v.rt/100,42);
if(v.age>=18)return "<p class=note>"+L.err+"</p>";
if(v.am*12<1000)return "<p class=note>"+L.min+"</p>";
return "<div class=facts><div><span>"+L.r1+"</span><b>"+fm(b)+"</b></div><div><span>"+L.r2+"</span><b>"+fm(d)+"</b></div><div><span>"+L.r3+"</span><b>"+fm(b-d)+"</b></div><div><span>"+L.r4+"</span><b>"+fm(b60)+"</b></div></div>";''',
  hi=dict(h1="NPS वात्सल्य कैलकुलेटर", desc="बच्चे के नाम NPS वात्सल्य खाते में हर महीने जमा करने पर 18 साल और 60 साल की उम्र पर अंदाज़न रकम देखें।",
   lead="बच्चे की उम्र, हर महीने की जमा और अनुमानित रिटर्न डालिए। 18 साल पर और अगर आगे जमा न करें तो 60 साल पर अंदाज़न रकम दिखेगी।",
   labels=["हर महीने जमा (₹)","बच्चे की अभी उम्र (0–17 साल)","अनुमानित रिटर्न (% सालाना)"],
   hint=[None,None,"NPS बाज़ार से जुड़ी योजना है, रिटर्न पक्का नहीं होता। 10% सिर्फ़ उदाहरण के लिए है, इसे बदलकर देखें।"],
   btn="हिसाब लगाएँ", note="यह सिर्फ़ अंदाज़ा है। असली रिटर्न बाज़ार, फंड और खर्चों के हिसाब से ऊपर-नीचे होगा और कम भी हो सकता है। 18 के बाद निकासी और एन्युटी के नियम के लिए npstrust.org.in देखें।",
   rh="योजना की मुख्य बातें (रिपोर्टों के अनुसार)", rules=["18 साल से कम उम्र के बच्चे के नाम खाता खुलता है, माता-पिता या अभिभावक चलाते हैं।","साल में कम से कम ₹1,000 जमा करना होता है, ऊपरी सीमा नहीं बताई गई है।","18 साल पर खाता सामान्य NPS खाते में बदल सकता है।","निकासी और एन्युटी के नियम बदल सकते हैं। खाता खोलने से पहले आधिकारिक साइट पर पुष्टि करें।"],
   see="NPS वात्सल्य की पूरी जानकारी पढ़ें →",
   js=dict(err="बच्चे की उम्र 18 से कम डालिए।",min="साल में कम से कम ₹1,000 जमा करना होता है।",r1="18 साल पर अंदाज़न रकम",r2="कुल जमा",r3="अनुमानित रिटर्न",r4="60 साल पर (18 के बाद जमा बंद, महंगाई घटाए बिना)")),
  en=dict(h1="NPS Vatsalya Calculator", desc="Estimate the amount in an NPS Vatsalya account at age 18 and 60 for monthly deposits made in your child's name.",
   lead="Enter the child's age, the monthly deposit and the expected return. You will see the approximate amount at 18, and at 60 if no more is deposited.",
   labels=["Monthly deposit (₹)","Child's current age (0–17 years)","Expected return (% per year)"],
   hint=[None,None,"NPS is market-linked and returns are not guaranteed. 10% is only an example, try changing it."],
   btn="Calculate", note="This is only an estimate. Actual returns will go up and down with the market, the fund and charges, and can be lower. Check npstrust.org.in for withdrawal and annuity rules after 18.",
   rh="Key points of the scheme (as per reports)", rules=["An account can be opened for a child below 18, run by a parent or guardian.","A minimum of ₹1,000 per year must be deposited. No upper limit is stated.","At 18 the account can convert into a regular NPS account.","Withdrawal and annuity rules can change. Confirm on the official site before opening."],
   see="Read the full NPS Vatsalya details →",
   js=dict(err="Enter a child's age below 18.",min="At least ₹1,000 per year must be deposited.",r1="Approx. amount at 18",r2="Total deposited",r3="Estimated returns",r4="At age 60 (no deposits after 18, before inflation)"))),

 dict(slug="pm-surya-ghar-calculator", icon="☀️", scheme="pm-surya-ghar-muft-bijli-yojana",
  fields=[F("kw","num",3,step=0.5,mn=1),F("cp","num",60000,mn=0),F("tr","num",7,step=0.5,mn=0)],
  js='''if(!(v.kw>=1))return "<p class=note>"+L.min+"</p>";
var sub=v.kw<=2?v.kw*30000:Math.min(60000+Math.min(v.kw-2,1)*18000,78000);
var cost=v.kw*v.cp,net=Math.max(cost-sub,0),u=v.kw*120,sv=u*v.tr,pb=sv>0?net/(sv*12):0;
return "<div class=facts><div><span>"+L.r1+"</span><b>"+fm(sub)+"</b></div><div><span>"+L.r2+"</span><b>"+fm(cost)+"</b></div><div><span>"+L.r3+"</span><b>"+fm(net)+"</b></div><div><span>"+L.r4+"</span><b>"+Math.round(u)+" "+L.u+"</b></div><div><span>"+L.r5+"</span><b>"+fm(sv)+"</b></div><div><span>"+L.r6+"</span><b>"+pb.toFixed(1)+" "+L.y+"</b></div></div>";''',
  hi=dict(h1="पीएम सूर्य घर सब्सिडी और बचत कैलकुलेटर", desc="छत पर सोलर लगाने पर पीएम सूर्य घर में कितनी सब्सिडी मिल सकती है और बिजली बिल में कितनी बचत होगी, अंदाज़ा लगाएँ।",
   lead="सोलर सिस्टम का साइज़ (kW) डालिए। अंदाज़न सब्सिडी, आपकी जेब से लगने वाली रकम और बिजली बिल की बचत दिख जाएगी।",
   labels=["सिस्टम का साइज़ (kW)","एक kW की अनुमानित लागत (₹)","बिजली की दर (₹ प्रति यूनिट)"],
   hint=[None,"वेंडर के कोटेशन के हिसाब से बदलें। लागत जगह और कंपनी के अनुसार अलग होती है।","अपने बिजली बिल से दर देखकर डालिए।"],
   btn="हिसाब लगाएँ", note="यह सिर्फ़ अंदाज़ा है। माना गया है कि 1 kW सिस्टम से महीने में लगभग 120 यूनिट बिजली बनती है, जो मौसम और जगह के अनुसार बदलती है। सब्सिडी की रकम और शर्तें MNRE के आदेश से बदल सकती हैं। pmsuryaghar.gov.in पर पुष्टि करें।",
   rh="सब्सिडी का हिसाब (रिपोर्टों के अनुसार)", rules=["1 kW पर ₹30,000 और 2 kW पर ₹60,000 की सब्सिडी।","3 kW या उससे ज़्यादा पर अधिकतम ₹78,000।","कुछ राज्य अपनी तरफ़ से अलग सब्सिडी भी दे सकते हैं, यह यहाँ नहीं जोड़ी गई है।","सब्सिडी सत्यापन के बाद बैंक खाते में आती है, समय अलग-अलग हो सकता है।"],
   see="पीएम सूर्य घर की पूरी जानकारी पढ़ें →",
   js=dict(min="सिस्टम का साइज़ कम से कम 1 kW डालिए।",r1="अंदाज़न सब्सिडी",r2="सिस्टम की कुल लागत",r3="सब्सिडी के बाद आपकी लागत",r4="महीने में बिजली उत्पादन",u="यूनिट",r5="महीने की बचत",r6="लागत वसूल होने में अंदाज़न",y="साल")),
  en=dict(h1="PM Surya Ghar Subsidy and Savings Calculator", desc="Estimate the PM Surya Ghar subsidy for rooftop solar and how much you could save on your electricity bill.",
   lead="Enter the solar system size (kW). You will see the approximate subsidy, your own cost and the savings on your electricity bill.",
   labels=["System size (kW)","Approx. cost per kW (₹)","Electricity rate (₹ per unit)"],
   hint=[None,"Change it as per your vendor's quotation. Cost differs by place and company.","Take the rate from your electricity bill."],
   btn="Calculate", note="This is only an estimate. It assumes a 1 kW system makes about 120 units a month, which changes with season and location. Subsidy amounts and conditions can change by MNRE order. Confirm at pmsuryaghar.gov.in.",
   rh="Subsidy calculation (as per reports)", rules=["₹30,000 subsidy for 1 kW and ₹60,000 for 2 kW.","Maximum ₹78,000 for 3 kW or more.","Some states may give their own extra subsidy. It is not added here.","The subsidy reaches the bank account after verification. Timing can vary."],
   see="Read the full PM Surya Ghar details →",
   js=dict(min="Enter a system size of at least 1 kW.",r1="Approx. subsidy",r2="Total system cost",r3="Your cost after subsidy",r4="Monthly generation",u="units",r5="Monthly saving",r6="Approx. payback time",y="years"))),

 dict(slug="pmegp-subsidy-calculator", icon="🏭", scheme="pmegp-yojana",
  fields=[F("pc","num",1000000,mn=0),F("sec","sel",opts=[("m","m"),("s","s")]),F("cat","sel",opts=[("g","g"),("sp","sp")]),F("ar","sel",opts=[("r","r"),("u","u")])],
  js='''var cap=v.sec=="m"?5000000:2000000;if(!(v.pc>0))return "<p class=note>"+L.min+"</p>";if(v.pc>cap)return "<p class=note>"+L.max+" "+fm(cap)+"</p>";
var pct=v.cat=="g"?(v.ar=="r"?25:15):(v.ar=="r"?35:25),own=v.cat=="g"?10:5,sub=v.pc*pct/100,oc=v.pc*own/100,loan=v.pc-sub-oc;
return "<div class=facts><div><span>"+L.r1+"</span><b>"+pct+"%</b></div><div><span>"+L.r2+"</span><b>"+fm(sub)+"</b></div><div><span>"+L.r3+"</span><b>"+fm(oc)+" ("+own+"%)</b></div><div><span>"+L.r4+"</span><b>"+fm(loan)+"</b></div></div>";''',
  hi=dict(h1="PMEGP सब्सिडी कैलकुलेटर", desc="PMEGP में प्रोजेक्ट लागत पर कितनी सब्सिडी, अपनी हिस्सेदारी और बैंक लोन बनेगा, इसका अंदाज़ा लगाएँ।",
   lead="प्रोजेक्ट की लागत और अपनी श्रेणी चुनिए। अंदाज़न सब्सिडी, आपकी हिस्सेदारी और बैंक लोन दिख जाएगा।",
   labels=["प्रोजेक्ट की कुल लागत (₹)","काम का प्रकार","आवेदक की श्रेणी","इलाका"],
   opts=[[("m","विनिर्माण (मैन्युफैक्चरिंग)"),("s","सेवा / व्यापार")],[("g","सामान्य"),("sp","विशेष (SC, ST, OBC, अल्पसंख्यक, महिला, पूर्व सैनिक, दिव्यांग आदि)")],[("r","ग्रामीण"),("u","शहरी")]],
   btn="हिसाब लगाएँ", note="यह सिर्फ़ अंदाज़ा है। सब्सिडी की दर और सीमाएँ एक वित्तीय गाइड के आधार पर हैं और बदल सकती हैं। असली रकम बैंक की मंज़ूरी और आधिकारिक पोर्टल के अनुसार तय होगी। kviconline.gov.in/pmegpeportal पर पुष्टि करें।",
   rh="सब्सिडी की दरें (रिपोर्टों के अनुसार)", rules=["सामान्य श्रेणी: शहरी में 15%, ग्रामीण में 25%।","विशेष श्रेणी: शहरी में 25%, ग्रामीण में 35%।","अपनी हिस्सेदारी: सामान्य में 10%, विशेष में 5% (रिपोर्टों के अनुसार)।","अधिकतम प्रोजेक्ट लागत: विनिर्माण ₹50 लाख, सेवा/व्यापार ₹20 लाख।"],
   see="PMEGP की पूरी जानकारी पढ़ें →",
   js=dict(min="प्रोजेक्ट की लागत डालिए।",max="इस प्रकार के काम की सीमा",r1="सब्सिडी की दर",r2="अंदाज़न सब्सिडी",r3="आपकी हिस्सेदारी",r4="बैंक लोन (अंदाज़न)")),
  en=dict(h1="PMEGP Subsidy Calculator", desc="Estimate the PMEGP subsidy, your own contribution and the bank loan on your project cost.",
   lead="Enter the project cost and choose your category. You will see the approximate subsidy, your contribution and the bank loan.",
   labels=["Total project cost (₹)","Type of activity","Applicant category","Area"],
   opts=[[("m","Manufacturing"),("s","Service / trading")],[("g","General"),("sp","Special (SC, ST, OBC, minority, women, ex-servicemen, disabled etc.)")],[("r","Rural"),("u","Urban")]],
   btn="Calculate", note="This is only an estimate. Subsidy rates and limits are based on a financial guide and can change. The actual amount depends on the bank's approval and the official portal. Confirm at kviconline.gov.in/pmegpeportal.",
   rh="Subsidy rates (as per reports)", rules=["General category: 15% in urban and 25% in rural areas.","Special category: 25% in urban and 35% in rural areas.","Own contribution: 10% for general and 5% for special (as per reports).","Maximum project cost: ₹50 lakh for manufacturing and ₹20 lakh for service/trading."],
   see="Read the full PMEGP details →",
   js=dict(min="Enter the project cost.",max="The limit for this type of activity is",r1="Subsidy rate",r2="Approx. subsidy",r3="Your contribution",r4="Bank loan (approx.)"))),

 dict(slug="loan-emi-calculator", icon="💼", scheme="pm-mudra-yojana",
  fields=[F("la","num",100000,mn=0),F("lr","num",10,step=0.1,mn=0),F("ly","num",3,step=0.5,mn=0)],
  js='''if(!(v.la>0&&v.ly>0))return "<p class=note>"+L.min+"</p>";
var n=Math.round(v.ly*12),r=v.lr/1200,e=r==0?v.la/n:v.la*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1),t=e*n;
return "<div class=facts><div><span>"+L.r1+"</span><b>"+fm(e)+"</b></div><div><span>"+L.r2+"</span><b>"+fm(t-v.la)+"</b></div><div><span>"+L.r3+"</span><b>"+fm(t)+"</b></div></div>";''',
  hi=dict(h1="लोन EMI कैलकुलेटर (मुद्रा, PMEGP, स्वनिधि)", desc="कारोबार या मुद्रा लोन की मासिक किस्त (EMI), कुल ब्याज और कुल चुकाने वाली रकम का अंदाज़ा लगाएँ।",
   lead="लोन की रकम, ब्याज दर और अवधि डालिए। हर महीने की किस्त और कुल ब्याज दिख जाएगा।",
   labels=["लोन की रकम (₹)","ब्याज दर (% सालाना)","अवधि (साल)"],
   hint=[None,"मुद्रा लोन की ब्याज दर हर बैंक की अलग होती है। अपने बैंक से पूछकर सही दर डालिए।",None],
   btn="हिसाब लगाएँ", note="यह सिर्फ़ अंदाज़ा है। हिसाब में घटते बैलेंस पर EMI मानी गई है। बैंक की असली किस्त प्रोसेसिंग फीस, बीमा और अपनी गिनती के कारण थोड़ी अलग हो सकती है।",
   rh="मुद्रा लोन की श्रेणियाँ (रिपोर्टों के अनुसार)", rules=["शिशु: ₹50,000 तक।","किशोर: ₹50,001 से ₹5 लाख तक।","तरुण: ₹5 लाख से ₹10 लाख तक।","तरुण प्लस: ₹10 लाख से ₹20 लाख तक।","सीमाएँ और दरें बदल सकती हैं। बैंक से पुष्टि करें।"],
   see="मुद्रा योजना की पूरी जानकारी पढ़ें →",
   js=dict(min="लोन की रकम और अवधि डालिए।",r1="हर महीने की EMI",r2="कुल ब्याज",r3="कुल चुकाने वाली रकम")),
  en=dict(h1="Loan EMI Calculator (Mudra, PMEGP, SVANidhi)", desc="Estimate the monthly instalment (EMI), total interest and total repayment of a business or Mudra loan.",
   lead="Enter the loan amount, interest rate and tenure. You will see the monthly instalment and the total interest.",
   labels=["Loan amount (₹)","Interest rate (% per year)","Tenure (years)"],
   hint=[None,"Mudra loan interest rates differ by bank. Ask your bank and enter the right rate.",None],
   btn="Calculate", note="This is only an estimate. It assumes a reducing-balance EMI. The bank's actual instalment can differ slightly because of processing fees, insurance and its own calculation.",
   rh="Mudra loan categories (as per reports)", rules=["Shishu: up to ₹50,000.","Kishore: ₹50,001 to ₹5 lakh.","Tarun: ₹5 lakh to ₹10 lakh.","Tarun Plus: ₹10 lakh to ₹20 lakh.","Limits and rates can change. Confirm with the bank."],
   see="Read the full Mudra details →",
   js=dict(min="Enter the loan amount and tenure.",r1="Monthly EMI",r2="Total interest",r3="Total repayment"))),
]
HUB = {
 "hi": dict(h1="सरकारी योजनाओं के कैलकुलेटर", desc="सुकन्या समृद्धि, NPS वात्सल्य, पीएम सूर्य घर, PMEGP और लोन EMI के मुफ़्त कैलकुलेटर।", lead="योजनाओं का हिसाब लगाने के लिए मुफ़्त कैलकुलेटर। ये सिर्फ़ अंदाज़ा देते हैं, पक्की गिनती के लिए आधिकारिक साइट देखें।", ssy="बेटी की बचत योजना: 21 साल पर कितनी रकम बनेगी।", crumb="कैलकुलेटर"),
 "en": dict(h1="Government Scheme Calculators", desc="Free calculators for Sukanya Samriddhi, NPS Vatsalya, PM Surya Ghar, PMEGP and loan EMI.", lead="Free calculators to work out scheme amounts. They give only estimates, so check the official site for exact figures.", ssy="Girl-child savings scheme: how much you get at 21 years.", crumb="Calculators"),
}
