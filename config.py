TOKEN_API = '6608642507:AAF2qL_Pn3y_Gz_ZjbRfxAVVVSnUNAwL3u0'

START_TEXT = '''
👋Привіт!
⚠️Це бот-автошкола.
❗️-Тут можна зареєструватися на навчання в нашій автошколі та в майбутньому отримати права.
✅-Щоб отримати більше інформації про цього бота натисніть  /description
✅-Щоб почати реєстрацію натисніть /start_signing
✅-Щоб отримати локацію школи натисніть /location
✅-Щоб отримати фото школи натисніть /photo_of_school
✅-Щоб отримати інформацію про робітників /colleagues

'''

DESCRIPTION_TEXT = '''
В цьому боті можна заповнити анкету для реєстрації 
на навчання та обрати на які саме права ви хочете отримати. 
Ви отримаєте геолокацію та фото нашої автоколи , а також інформацію про робітників.
'''

HELP_TEXT = '''
/start - почати роботу бота
/help - команди цього бота
/description - опис бота
/start_signing - почати реєстрацію
/location - отримати локацію
/photo_of_school - отримати фото школи
/colleagues - отримати інофрмацію про робітників
'''

license_type = """
на які права ви хочете здати? 
У нашій автошколі ви можете здати на 
A: мотоцикли; B: легкові автомобілі; 
C: грузові автомобілі; D пассажирскі автобусы;
BE: легкові авто з прицепом; CE: грузові авто з прицепом; 
DE: пассажирські автобусы з прицепом.
"""
collegi = {
    1:{'імʼя':'Ігор Миколайович Пєтров',"вік":32,'професія':'вчитель водіння'},
    2:{'імʼя':'Марина Сергіївна Вороніна','вік':27,'професія':'вчителька теорії'},
    3:{'імʼя':'Калінов Самвел Андрійович','вік':39,'професія':'директор школи'},
    4:{'імʼя':'Качур Галина Едуардівна','вік':55,'професія':'прибиральниця'}}

PHOTO_LIST = [
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fautoshkola-navihator.com.ua%2Fwp-content%2Fuploads%2F2021%2F11%2Fofis-na-oboloni-400x300.jpg&imgrefurl=https%3A%2F%2Fautoshkola-navihator.com.ua%2Fru%2Fmedia-gallery%2Fdetail%2F94%2F210&docid=0EPCHEz4AclebM&tbnid=szSK-5KtOd6TvM&vet=12ahUKEwif4Z3brZmEAxXWcvEDHcTNBHsQM3oECCcQAA..i&w=400&h=300&itg=1&ved=2ahUKEwif4Z3brZmEAxXWcvEDHcTNBHsQM3oECCcQAA'
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fagat.ua%2Fwp-content%2Fthemes%2Fagat%2Fimg%2Fschool%2F2%2F1.png&imgrefurl=https%3A%2F%2Fagat.ua%2Favtoshkola-obolon%2F&docid=lkqTNPMnRmGxOM&tbnid=c16qL2LUAP-6WM&vet=12ahUKEwif4Z3brZmEAxXWcvEDHcTNBHsQM3oECBwQAA..i&w=460&h=350&ved=2ahUKEwif4Z3brZmEAxXWcvEDHcTNBHsQM3oECBwQAA'
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Ftaurus-school.kiev.ua%2Fwp-content%2Fuploads%2F2021%2F03%2Fphoto_2021-03-03_10-56-36-1-1.webp&imgrefurl=https%3A%2F%2Ftaurus-school.kiev.ua%2Fbranches%2Fobolon-geroev-dnepra&docid=ptojC_uKACB_eM&tbnid=vb5wqvbERmp8uM&vet=12ahUKEwif4Z3brZmEAxXWcvEDHcTNBHsQM3oECDsQAA..i&w=780&h=596&ved=2ahUKEwif4Z3brZmEAxXWcvEDHcTNBHsQM3oECDsQAA'
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Ftaurus-school.kiev.ua%2Fwp-content%2Fuploads%2F2021%2F04%2Flogotip-1-1024x522.jpg&imgrefurl=https%3A%2F%2Ftaurus-school.kiev.ua%2Fteachers%2Furoki-vozhdeniya-s-instruktorom-obolon&docid=1_4yrCmeMjr_9M&tbnid=HnzBlr7gpbzFtM&vet=12ahUKEwif4Z3brZmEAxXWcvEDHcTNBHsQM3oECCUQAA..i&w=1024&h=522&ved=2ahUKEwif4Z3brZmEAxXWcvEDHcTNBHsQM3oECCUQAA'
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.kakfirma.com%2Fwp-content%2Fuploads%2F2013%2F07%2F10095.jpg&imgrefurl=https%3A%2F%2Fwww.kakfirma.com%2Flistings%2FAvtoshkola-Karat%2F&docid=nVPcFwm-WbIQSM&tbnid=mQXNG_K5hhYhsM&vet=12ahUKEwjH2N6trpmEAxXaXvEDHf3wDmI4ChAzegQIHhAA..i&w=604&h=403&ved=2ahUKEwjH2N6trpmEAxXaXvEDHf3wDmI4ChAzegQIHhAA'
]

