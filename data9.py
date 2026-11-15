# -*- coding: utf-8 -*-
# Extra sections: "how to check status" + "payment not received? possible reasons". (hi, en) per scheme.
# Only generally true causes + what third-party/news sources reported; hedged where portals change.
G_HI = [
 "आधार बैंक खाते से लिंक (NPCI मैपिंग) नहीं है। बैंक शाखा में पूछें, या myaadhaar.uidai.gov.in पर 'Bank Seeding Status' जाँचें (मेन्यू का नाम बदल सकता है)।",
 "e-KYC / सत्यापन बाकी है। ऑनलाइन, CSC या संबंधित कार्यालय में पूरा करें।",
 "आवेदन और आधार/बैंक में नाम या जन्म तिथि अलग-अलग है।",
 "बैंक खाता बंद या निष्क्रिय है, या पोर्टल पर खाता संख्या/IFSC गलत है।",
 "सरकारी मंज़ूरी, फ़ंड या चुनाव आचार संहिता की वजह से किस्त देर से जारी हुई। इस हाल में सिर्फ़ आपका नहीं, पूरे राज्य का भुगतान रुका होता है।",
]
G_EN = [
 "Aadhaar is not linked to the bank account (NPCI mapping). Ask the bank branch, or check 'Bank Seeding Status' at myaadhaar.uidai.gov.in (the menu name may change).",
 "e-KYC / verification is pending. Complete it online, at a CSC or at the concerned office.",
 "Name or date of birth is different in the application and in Aadhaar/bank records.",
 "The bank account is closed or dormant, or the account number/IFSC on the portal is wrong.",
 "The instalment was released late because of government approval, funds or an election code of conduct. In that case payments are held for everyone in the state, not only for you.",
]
def mk(shi, sen, ihi=(), ien=(), tool=None):
    return {"hi":{"status":shi,"issues":list(ihi)+G_HI},"en":{"status":sen,"issues":list(ien)+G_EN},"tool":tool}

EXTRA = {
 "up-pension-yojana-sspy": mk(
  ["sspy-up.gov.in खोलें। अगर सर्टिफ़िकेट की चेतावनी आए तो वहाँ कुछ न भरें, CSC/जन सेवा केंद्र जाएँ।","पोर्टल पर आवेदन/पेंशन की स्थिति देखने का विकल्प चुनें और आधार या आवेदन संख्या (जो पोर्टल माँगे) डालें।","नाम, जन्म तिथि और श्रेणी (वृद्धा/विधवा/दिव्यांग) सही हैं या नहीं देखें।","कुछ बाकी हो तो CSC या ब्लॉक/ज़िला समाज कल्याण कार्यालय में पावती (acknowledgement) लेकर जमा करें।"],
  ["Open sspy-up.gov.in. If a certificate warning appears, do not enter anything there; go to a CSC/Jan Seva Kendra.","Choose the application/pension status option and enter Aadhaar or the application number (whatever the portal asks).","Check that name, date of birth and category (old age/widow/disabled) are correct.","If something is pending, submit it at a CSC or the block/district social welfare office and keep the acknowledgement."],
  ["प्रमाणपत्र (आयु/आय/दिव्यांग) छूटा, पुराना या रिकॉर्ड से अलग है।"],
  ["A certificate (age/income/disability) is missing, expired or does not match the records."]),
 "bihar-samajik-suraksha-pension-yojana": mk(
  ["elabharthi.bihar.gov.in खोलें (पुराना sspmis पता अक्सर नहीं खुलता)।","भुगतान/लाभार्थी की स्थिति वाला विकल्प चुनें और माँगी गई जानकारी (जैसे आधार या खाता संख्या) डालें।","e-KYC की स्थिति देखें। रिपोर्टों के अनुसार e-KYC के लिए पेंशनर का खुद मौजूद होना (फ़ेस/फ़िंगरप्रिंट) ज़रूरी हो सकता है।","e-KYC बाकी हो तो CSC, ब्लॉक सामाजिक सुरक्षा कोषांग या पोर्टल से कराएँ।"],
  ["Open elabharthi.bihar.gov.in (the old sspmis address often does not open).","Choose the payment/beneficiary status option and enter what it asks (for example Aadhaar or account number).","Check the e-KYC status. As per reports, the pensioner may need to be present for face/fingerprint e-KYC.","If e-KYC is pending, complete it at a CSC, the block social security cell or on the portal."],
  ["रिपोर्टों के अनुसार e-KYC न होने पर अगली किस्त रोक दी जाती है। e-KYC के बाद पेंशन अगले चक्र से फिर शुरू हो जाती है (नियम बदल सकते हैं)।"],
  ["As per reports, the next instalment is held if e-KYC is not done. After e-KYC the pension usually restarts from the next cycle (rules can change)."]),
 "jharkhand-sarvajan-pension": mk(
  ["sarvajanpension.jharkhand.gov.in खोलें।","आवेदन/लाभार्थी की स्थिति वाला विकल्प खोजें और आधार या आवेदन संख्या डालें।","स्थिति 'लंबित' हो तो पंचायत/प्रखंड कार्यालय में सत्यापन की स्थिति पूछें।"],
  ["Open sarvajanpension.jharkhand.gov.in.","Find the application/beneficiary status option and enter Aadhaar or the application number.","If the status is pending, ask the panchayat/block office about verification."],
  ["सत्यापन प्रखंड/पंचायत स्तर पर लंबित है।"],
  ["Verification is pending at block/panchayat level."]),
 "chhattisgarh-mahtari-vandan": mk(
  ["mahtarivandan.cgstate.gov.in खोलें।","तृतीय-पक्ष गाइडों के अनुसार 'आवेदन की स्थिति / भुगतान की स्थिति' वाले विकल्प में पंजीकृत मोबाइल या आधार और कैप्चा डालने पर भुगतान का इतिहास दिखता है (मेन्यू के नाम बदल सकते हैं)।","e-KYC बाकी हो तो आंगनबाड़ी केंद्र या CSC पर आधार और पंजीकृत मोबाइल लेकर जाएँ।","पोर्टल पर बैंक खाता संख्या और IFSC सही हैं या नहीं जाँचें।"],
  ["Open mahtarivandan.cgstate.gov.in.","As per third-party guides, the 'application status / payment status' option shows payment history when you enter the registered mobile or Aadhaar and the captcha (menu names may change).","If e-KYC is pending, go to an Anganwadi centre or CSC with Aadhaar and the registered mobile.","Check that the bank account number and IFSC on the portal are correct."],
  ["बैंक खाता NPCI से मैप न होने पर DBT असफल हो जाता है। बैंक से 'आधार सीडिंग' करवाएँ।"],
  ["If the bank account is not NPCI-mapped, the DBT fails. Ask the bank for 'Aadhaar seeding'."]),
 "jharkhand-maiyan-samman": mk(
  ["mmmsy.jharkhand.gov.in खोलें।","स्थिति देखने का विकल्प चुनें और आवेदन संख्या या आधार डालें (जो पोर्टल माँगे)।","स्थिति 'लंबित' हो तो पंचायत सेवक/प्रखंड कार्यालय या शिविर में पूछें।","बैंक खाता आधार से जुड़ा और चालू होना चाहिए।"],
  ["Open mmmsy.jharkhand.gov.in.","Choose the status option and enter the application number or Aadhaar (whatever the portal asks).","If the status is pending, ask the panchayat or block office or at a camp.","The bank account must be linked to Aadhaar and active."],
  ["समाचार रिपोर्टों में कई ज़िलों में भुगतान में देरी की बात आई है। यह अक्सर सत्यापन या बैंक सीडिंग की वजह से होती है।"],
  ["News reports mention payment delays in several districts. This is often due to verification or bank seeding."]),
 "odisha-subhadra": mk(
  ["subhadra.odisha.gov.in खोलें या नज़दीकी Mo Seva/जन सेवा केंद्र जाएँ।","स्थिति या भुगतान देखने का विकल्प चुनें और आवेदन संख्या/आधार डालें (जो पोर्टल माँगे)।","रिपोर्टों के अनुसार किस्तें चरणों में जारी होती हैं। आपकी बारी अभी न आई हो तो भुगतान में समय लग सकता है।"],
  ["Open subhadra.odisha.gov.in or go to the nearest Mo Seva/Jan Seva Kendra.","Choose the status or payment option and enter the application number/Aadhaar (whatever the portal asks).","As per reports, instalments are released in phases. If your turn has not come yet, the payment may take time."],
  ["रिपोर्टों के अनुसार भुगतान चरणों में जारी होता है, इसलिए कुछ लाभार्थियों को देर से मिलता है।"],
  ["As per reports, payments are released in phases, so some beneficiaries get them later."]),
 "mp-ladli-behna-yojana": mk(
  ["cmladlibahna.mp.gov.in खोलें।","भुगतान की स्थिति के लिए आवेदन संख्या या समग्र सदस्य ID, कैप्चा और OTP डालें।","दिक्कत हो तो हेल्पलाइन 0755-2700800 पर संपर्क करें।"],
  ["Open cmladlibahna.mp.gov.in.","To see the payment status, enter the application number or Samagra member ID, captcha and OTP.","If there is a problem, call helpline 0755-2700800."],
  ["समग्र ID में नाम/ई-केवाईसी अपडेट न होना।"],
  ["Name/e-KYC not updated in the Samagra ID."]),
 "maharashtra-ladki-bahin-yojana": mk(
  ["ladakibahin.maharashtra.gov.in खोलें।","आवेदन और e-KYC की स्थिति देखें।","e-KYC में दिक्कत हो तो आंगनवाड़ी या ज़िला कार्यालय से संपर्क करें।"],
  ["Open ladakibahin.maharashtra.gov.in.","Check the application and e-KYC status.","If you have e-KYC trouble, contact your Anganwadi or the district office."],
  ["जनवरी 2026 की एक रिपोर्ट (Free Press Journal) के अनुसार e-KYC अनिवार्य किया गया था, और बाद की किस्त वित्त विभाग की मंज़ूरी और चुनाव की वजह से देर से बताई गई थी। ताज़ा स्थिति पोर्टल पर देखें।"],
  ["A January 2026 report (Free Press Journal) said e-KYC had been made mandatory and a later instalment was reported delayed due to finance department approval and elections. Check the latest on the portal."]),
 "bihar-kanya-utthan-yojana": mk(
  ["medhasoft.bih.nic.in खोलें।","अपना आवेदन/योजना चुनकर स्थिति देखें।","कॉलेज/विभाग की ओर से सत्यापन बाकी हो तो अपने संस्थान के कार्यालय में पूछें।"],
  ["Open medhasoft.bih.nic.in.","Choose your application/scheme and view the status.","If verification from the college/department is pending, ask at your institution's office."],
  ["कॉलेज या विभाग का सत्यापन लंबित है।"],
  ["College or department verification is pending."]),
 "bihar-mahila-rozgar-yojana": mk(
  ["अपने जीविका समूह या प्रखंड जीविका कार्यालय से आवेदन की स्थिति पूछें।","brlps.in पर जानकारी देखें।"],
  ["Ask your JEEViKA group or the block JEEViKA office about the application status.","Check brlps.in for information."],
  ["समूह स्तर पर सत्यापन या दस्तावेज़ अधूरे हैं।"],
  ["Group-level verification or documents are incomplete."]),
 "bihar-student-credit-card-yojana": mk(
  ["7nishchay-yojana.bihar.gov.in खोलें।","लॉग इन करके आवेदन की स्थिति देखें।","स्थिति 'बैंक को भेजा गया' हो तो बैंक शाखा से स्वीकृति के बारे में पूछें।"],
  ["Open 7nishchay-yojana.bihar.gov.in.","Log in and view the application status.","If the status says 'sent to bank', ask the bank branch about sanction."],
  ["बैंक स्वीकृति या दस्तावेज़ों की जाँच बाकी है।"],
  ["Bank sanction or document checks are pending."]),
 "up-kanya-sumangala-yojana": mk(
  ["mksy.up.gov.in खोलें।","लॉग इन करके आवेदन की स्थिति देखें।","स्थिति लंबित हो तो ज़िला परिवीक्षा अधिकारी (DPO) कार्यालय से पूछें।"],
  ["Open mksy.up.gov.in.","Log in and view the application status.","If the status is pending, ask the District Probation Officer (DPO) office."],
  ["किस्त चरणों के हिसाब से मिलती है (जन्म, टीकाकरण, कक्षा आदि)। अगला चरण पूरा न होने पर अगली किस्त नहीं आती।"],
  ["The amount is paid in stages (birth, vaccination, class etc.). The next instalment does not come until the next stage is done."]),
 "sukanya-samriddhi-yojana": {"hi":None,"en":None,"tool":True},
}
