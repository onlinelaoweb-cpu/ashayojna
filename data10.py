# -*- coding: utf-8 -*-
from data9 import mk, EXTRA
def own(shi,sen,ihi,ien):  # without the generic payment reasons
    return {"hi":{"status":shi,"issues":ihi},"en":{"status":sen,"issues":ien},"tool":None}
EXTRA.update({
 "pm-kisan-samman-nidhi": mk(
  ["pmkisan.gov.in खोलें और 'Farmers Corner' में 'Know Your Status' चुनें।","रजिस्ट्रेशन नंबर और कैप्चा डालें। रजिस्ट्रेशन नंबर भूल गए हों तो वहीं 'Know your registration no.' से मोबाइल नंबर डालकर पता करें।","हर किस्त का हाल और 'e-KYC', 'Land Seeding', 'Aadhaar Bank Account Seeding' की स्थिति देखें (मेन्यू के नाम बदल सकते हैं)।","समझ न आए तो हेल्पलाइन 155261 या 011-24300606 पर पूछें।"],
  ["Open pmkisan.gov.in and choose 'Know Your Status' under 'Farmers Corner'.","Enter the registration number and captcha. If you have forgotten the number, use 'Know your registration no.' there with your mobile number.","See each instalment and the status of 'e-KYC', 'Land Seeding' and 'Aadhaar Bank Account Seeding' (menu names may change).","If it is unclear, ask on helpline 155261 or 011-24300606."],
  ["रिपोर्टों के अनुसार e-KYC (OTP/बायोमेट्रिक/फ़ेस) बाकी हो तो किस्त रुक सकती है।","ज़मीन का रिकॉर्ड पोर्टल से 'सीड' या सत्यापित नहीं है। पटवारी/कृषि विभाग से पूछें।","बैंक खाते में आधार-आधारित DBT (NPCI) चालू नहीं है।"],
  ["As per reports, the instalment can be held if e-KYC (OTP/biometric/face) is pending.","Land records are not seeded or verified on the portal. Ask the patwari/agriculture office.","Aadhaar-based DBT (NPCI) is not active on the bank account."]),
 "ayushman-bharat-pmjay": own(
  ["mera.pmjay.gov.in खोलें और मोबाइल नंबर व OTP से लॉगिन करें, फिर राज्य व अपना विवरण डालकर पात्रता देखें।","कार्ड बनवाने के लिए नज़दीकी आयुष्मान मित्र, CSC या सूचीबद्ध अस्पताल में आधार और राशन कार्ड लेकर जाएँ।","हेल्पलाइन 14555 पर भी पात्रता और कार्ड के बारे में पूछ सकते हैं।"],
  ["Open mera.pmjay.gov.in, log in with your mobile number and OTP, then choose your state and enter your details to check eligibility.","To get the card, go to the nearest Ayushman Mitra, CSC or listed hospital with Aadhaar and ration card.","You can also ask about eligibility and the card on helpline 14555."],
  ["नाम पात्रता सूची (SECC/राज्य सूची) में नहीं है, तो कार्ड नहीं बनता। पात्रता की श्रेणी राज्य के अनुसार अलग हो सकती है।","e-KYC (आधार सत्यापन) पूरी नहीं हुई या आधार में नाम/उम्र अलग है।","इलाज के समय अस्पताल योजना में सूचीबद्ध नहीं है, या इलाज पैकेज में शामिल नहीं है। अस्पताल के आयुष्मान मित्र से पहले पूछें।"],
  ["The name is not on the eligibility list (SECC/state list), so no card is made. Eligibility categories can differ by state.","e-KYC (Aadhaar verification) is not done or the name/age in Aadhaar is different.","At the time of treatment the hospital is not listed under the scheme, or the treatment is not in a package. Ask the hospital's Ayushman Mitra first."]),
 "pm-ujjwala-yojana": mk(
  ["अपने गैस वितरक (एजेंसी) से पूछें कि सब्सिडी का भुगतान हुआ या नहीं।","mylpg.in पर LPG आईडी/मोबाइल से लॉगिन करके सिलेंडर और सब्सिडी का इतिहास देखें (साइट का मेन्यू बदल सकता है)।","बैंक पासबुक में 'DBT/LPG' की एंट्री देखें।"],
  ["Ask your gas distributor (agency) whether the subsidy was paid.","Log in at mylpg.in with the LPG ID/mobile to see the cylinder and subsidy history (the site menu may change).","Look for a 'DBT/LPG' entry in the bank passbook."],
  ["रिपोर्टों के अनुसार वितरक के यहाँ बायोमेट्रिक e-KYC बाकी हो तो सब्सिडी या कनेक्शन पर असर पड़ सकता है। वितरक से पूछें।","LPG कनेक्शन में दर्ज बैंक खाता गलत है या आधार से लिंक नहीं है।"],
  ["As per reports, if biometric e-KYC is pending at the distributor, subsidy or the connection can be affected. Ask the distributor.","The bank account on the LPG connection is wrong or not linked with Aadhaar."]),
 "pm-surya-ghar-muft-bijli-yojana": mk(
  ["pmsuryaghar.gov.in खोलें और बिजली उपभोक्ता नंबर व मोबाइल से लॉगिन करें।","आवेदन की स्थिति के चरण देखें: रजिस्ट्रेशन, डिस्कॉम की मंज़ूरी, इंस्टॉलेशन, निरीक्षण, कमीशनिंग और सब्सिडी (चरणों के नाम बदल सकते हैं)।","अटका हो तो पोर्टल पर दी शिकायत/हेल्पलाइन का इस्तेमाल करें।"],
  ["Open pmsuryaghar.gov.in and log in with your electricity consumer number and mobile.","See the application stages: registration, discom approval, installation, inspection, commissioning and subsidy (stage names may change).","If it is stuck, use the complaint/helpline given on the portal."],
  ["नेट मीटर लगना, डिस्कॉम का निरीक्षण या कमीशनिंग रिपोर्ट बाकी है। सब्सिडी इसके बाद ही जारी होती है।","इंस्टॉलर/वेंडर ने पोर्टल पर दस्तावेज़ या फ़ोटो अपलोड नहीं किए।"],
  ["The net meter, discom inspection or commissioning report is pending. The subsidy is released only after this.","The installer/vendor has not uploaded the documents or photos on the portal."]),
 "pm-awas-yojana-gramin": mk(
  ["आधिकारिक PMAY-G पोर्टल पर लाभार्थी खोज वाला विकल्प खोलें और रजिस्ट्रेशन नंबर या आधार/नाम से अपना विवरण देखें (साइट का मेन्यू बदल सकता है)।","किस्त की स्थिति, जियो-टैगिंग और निरीक्षण की स्थिति देखें।","ग्राम पंचायत या ब्लॉक कार्यालय (BDO) से भी पूछ सकते हैं।"],
  ["Open the beneficiary search option on the official PMAY-G portal and look up your details by registration number or Aadhaar/name (the site menu may change).","See the instalment, geo-tagging and inspection status.","You can also ask at the gram panchayat or block office (BDO)."],
  ["रिपोर्टों के अनुसार निर्माण के चरण की जियो-टैग फ़ोटो अपलोड न हो तो अगली किस्त रुक सकती है। पंचायत सचिव या आवास सहायक से पूछें।","नाम आवास प्लस/पात्र सूची में नहीं है।"],
  ["As per reports, the next instalment can be held if the geo-tagged photo of a construction stage is not uploaded. Ask the panchayat secretary or housing assistant.","The name is not on the Awaas Plus/eligible list."]),
 "pm-svanidhi-yojana": mk(
  ["pmsvanidhi.mohua.gov.in खोलें और आवेदन की स्थिति ('Know your application status' जैसा विकल्प) में आवेदन संख्या या मोबाइल डालें।","नगर निकाय (ULB) और बैंक, दोनों में स्थिति देखें।","अटका हो तो नगर निगम/पालिका के स्ट्रीट वेंडर सेल से पूछें।"],
  ["Open pmsvanidhi.mohua.gov.in and enter the application number or mobile under application status (an option like 'Know your application status').","Check the status at both the urban local body (ULB) and the bank.","If it is stuck, ask the municipality's street vendor cell."],
  ["नगर निकाय का सत्यापन या सिफ़ारिश पत्र (LoR) बाकी है।","दूसरी किस्त के लिए पहली किस्त का समय पर चुकाया जाना ज़रूरी होता है (रिपोर्टों के अनुसार)।"],
  ["The urban local body verification or recommendation letter (LoR) is pending.","The first loan generally needs to be repaid on time for the next tranche (as per reports)."]),
 "pm-fasal-bima-yojana": own(
  ["pmfby.gov.in खोलें और आवेदन की स्थिति ('Application Status') में रसीद संख्या डालें।","क्लेम की स्थिति के लिए उसी पोर्टल पर या फ़सल बीमा ऐप में अपना विवरण डालें।","हेल्पलाइन 14447 पर कॉल करके भी पूछ सकते हैं।"],
  ["Open pmfby.gov.in and enter the receipt number under 'Application Status'.","For the claim status, enter your details on the same portal or in the crop insurance app.","You can also call helpline 14447."],
  ["स्थानीय आपदा (जैसे ओला, बाढ़) के नुकसान की सूचना तय समय में नहीं दी, जो रिपोर्टों के अनुसार लगभग 72 घंटे बताया जाता है। समय सीमा बीमा कंपनी से पक्की करें।","प्रीमियम समय पर नहीं कटा, या बोई गई फ़सल/ज़मीन का विवरण बीमा रिकॉर्ड से अलग है।","क्लेम की रकम बैंक खाते (आधार-लिंक) में नहीं आ पा रही। खाता और IFSC जाँचें।"],
  ["Loss from a local calamity (like hailstorm or flood) was not reported in time, which is said to be about 72 hours as per reports. Confirm the time limit with the insurer.","The premium was not deducted on time, or the crop/land details differ from the insurance record.","The claim amount cannot reach the bank account (Aadhaar-linked). Check the account and IFSC."]),
 "pm-vishwakarma-yojana": own(
  ["pmvishwakarma.gov.in खोलें और आवेदक लॉगिन में मोबाइल/आवेदन आईडी से लॉगिन करें।","आवेदन के चरण देखें: आधार e-KYC, ग्राम पंचायत/नगर निकाय का सत्यापन, ज़िला समिति की मंज़ूरी, प्रशिक्षण, पहचान पत्र (चरणों के नाम बदल सकते हैं)।","टूलकिट और लोन के चरण में अटके हों तो CSC या ज़िला उद्योग केंद्र से पूछें।"],
  ["Open pmvishwakarma.gov.in and log in under applicant login with the mobile number/application ID.","See the application stages: Aadhaar e-KYC, verification by the gram panchayat/urban body, district committee approval, training, ID card (stage names may change).","If you are stuck at the toolkit or loan stage, ask a CSC or the District Industries Centre."],
  ["ग्राम पंचायत/नगर निकाय या ज़िला समिति के स्तर पर सत्यापन लंबित है।","आधार e-KYC या फ़ोटो/दस्तावेज़ अधूरे हैं।","प्रशिक्षण पूरा न होने तक टूलकिट वाउचर जारी नहीं होता (रिपोर्टों के अनुसार)।"],
  ["Verification is pending at the gram panchayat/urban body or district committee.","Aadhaar e-KYC or the photo/documents are incomplete.","The toolkit voucher is not issued until training is complete (as per reports)."]),
 "pm-matru-vandana-yojana": mk(
  ["आंगनवाड़ी कार्यकर्ता या ASHA से आवेदन की स्थिति पूछें, क्योंकि पंजीकरण वहीं से होता है।","आधिकारिक पोर्टल पर आवेदन की स्थिति का विकल्प खोजें और अपना विवरण डालें (साइट का मेन्यू बदल सकता है)।","बैंक/डाकघर खाते की पासबुक में DBT की एंट्री देखें।"],
  ["Ask the Anganwadi worker or ASHA for the application status, as registration is done there.","Look for the application status option on the official portal and enter your details (the site menu may change).","Look for the DBT entry in the bank/post office passbook."],
  ["किस्त के लिए ज़रूरी चरण (जैसे गर्भावस्था पंजीकरण, जाँच, टीकाकरण) रिकॉर्ड में दर्ज नहीं हुए। आंगनवाड़ी से पूछें।"],
  ["The required stages for the instalment (such as pregnancy registration, check-ups, immunisation) are not recorded. Ask the Anganwadi."]),
})
