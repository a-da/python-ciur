#!/usr/bin/env python
from ciur.common import DomParserFile


def test_rss(xml):
    dpf = DomParserFile(
        name="test",
        source="./originators/aa_com_tr/xjsons/rss.json"
    )

    xpath = dpf.get_version()

    dpf.validate_configs(xpath)

    html = open(xml).read()
    # e0
    html = html.replace("\xfd", "")
    # e3
    #if html == "no such rss type!...":
    #    print html
    #    return {}

    def string_to_time_set_default(date_string):
        return string_to_time(date_string)

    def string_to_time_no_set_default(date_string):
        return string_to_time(date_string, set_default_time = False)

    try:
        m = dpf.dive_xml_root_level(html, handlers=[string_to_time_set_default, string_to_time_no_set_default])
    except DomParserException, e:
        if e.value.get("suggestion") == "possible is plain/text not xml":
            print AdvancedDict(e.value).get_pretty()
        else:
            raise
    else:
        if do_retrun:
            return m.get_pretty()

        print m.get_pretty()


def test_rss1():
    """
    >>> test_rss1()
    constructor DOMParser
    {
        "item": [
            {
                "author": "ZAFER ÖZCAN",
                "category": "İŞ DÜNYASI",
                "content": "<IMG style=\\"border: navy 1px solid;\\" src=\\"http://medya.aksiyon.com.tr/aksiyon/2012/03/19/is-dunyasi-1_mainright.jpg\\" border=\\"0\\" align=\\"left\\" width=\\"80\\" height=\\"40\\"/>Altın fiyatlarının yükselmesi tekstil sektörünü yakından ilgilendiriyor. Eskiden doğumlara küçük altın götürenler artık bunun yerine kaliteli çocuk kıyafeti tercih ediyor.",
                "guid": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32108&link=32108",
                "link": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32108&link=32108",
                "pub_date": "Date(2012-03-18T22:00:00)",
                "title": "Altın alamayan kıyafete yöneliyor!"
            },
            {
                "category": "İŞ DÜNYASI",
                "content": "<IMG style=\\"border: navy 1px solid;\\" src=\\"http://medya.aksiyon.com.tr/aksiyon/2012/03/19/is-dunyasi-4_mainright.jpg\\" border=\\"0\\" align=\\"left\\" width=\\"80\\" height=\\"40\\"/>Türkiye’yi etkisi altına alan soğuk havaların uzaması tatlı sektörü için de umut kaynağı oldu. Özellikle kış aylarında yoğun tüketilen tahin, pekmez, helva, reçel, baklava gibi ürünlerin satışı firmaların yüzünü güldürüyor.",
                "guid": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32109&link=32109",
                "link": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32109&link=32109",
                "pub_date": "Date(2012-03-18T22:00:00)",
                "title": "Soğuklar tatlıcılara yaradı"
            },
            {
                "category": "İŞ DÜNYASI",
                "content": "<IMG style=\\"border: navy 1px solid;\\" src=\\"http://medya.aksiyon.com.tr/aksiyon/2012/03/19/is-dunyasi-5_mainright.jpg\\" border=\\"0\\" align=\\"left\\" width=\\"80\\" height=\\"40\\"/>Ar-Ge ve inovasyona verdiği önem sayesinde Türk halı sektöründe ilklere imza atan Royal Halı, sanatı halıya dokuyan Ebru desenli halıları ile çok beğeniliyor.",
                "guid": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32110&link=32110",
                "link": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32110&link=32110",
                "pub_date": "Date(2012-03-18T22:00:00)",
                "title": "Royal Halı’dan ebru sanatı"
            },
            {
                "category": "İŞ DÜNYASI",
                "content": "Ahşap Mutfak ve Banyo Mobilyası Sanayici ve İthalatçıları Derneği (MUDER) verilerine göre mutfak mobilya sektörü 2011 yılında yüzde 11 büyüdü.",
                "guid": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32111&link=32111",
                "link": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32111&link=32111",
                "pub_date": "Date(2012-03-18T22:00:00)",
                "title": "Mutfak değiştirme süresi kısalıyor"
            },
            {
                "category": "İŞ DÜNYASI",
                "content": "<IMG style=\\"border: navy 1px solid;\\" src=\\"http://medya.aksiyon.com.tr/aksiyon/2012/03/19/is-dunyasi-3_mainright.jpg\\" border=\\"0\\" align=\\"left\\" width=\\"80\\" height=\\"40\\"/>2011 yılında Cree işbirliğiyle LED aydınlatma sektörüne adım atan Vestel, tüm mekânları yüksek enerji tasarrufu sağlayan ve çevre dostu LED aydınlatma ürünleriyle aydınlatıyor.",
                "guid": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32112&link=32112",
                "link": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32112&link=32112",
                "pub_date": "Date(2012-03-18T22:00:00)",
                "title": "Vestel’den çok ışık, \\r az fatura"
            },
            {
                "category": "İŞ DÜNYASI",
                "content": "<IMG style=\\"border: navy 1px solid;\\" src=\\"http://medya.aksiyon.com.tr/aksiyon/2012/03/19/is-dunyasi-2_mainright.jpg\\" border=\\"0\\" align=\\"left\\" width=\\"80\\" height=\\"40\\"/>Yedi bölgeye yayılmış 124 mağazası ile Türkiye’nin en yaygın toptan satış zinciri olan Bizim Toptan, 2011 yılı net satışlarını 1 milyar 733 milyon TL olarak açıkladı. Satışlarını bir önceki yıla göre yüzde 19,4 oranında artıran Bizim Toptan’ın 2012 hedefi, yine çift haneli büyüyerek 2 milyar liranın üzerinde satış rakamına ulaşmak.",
                "guid": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32113&link=32113",
                "link": "http://www.aksiyon.com.tr/aksiyon/newsDetail_getNewsById.action?load=detay&newsId=32113&link=32113",
                "pub_date": "Date(2012-03-18T22:00:00)",
                "title": "Bizim Toptan’ın hedefi \\r 2 milyar TL"
            }
        ]
    }
    destructor DOMParser
    """
    test_rss("/oknetwiki/trunk/py_lib/vsft/test/feeds/rss.xml")


def test_rss2():
    """
    >>> test_rss2()
    constructor DOMParser
    {
        "item": [
            {
                "author": "stirpan@aa.com.tr (SİNEM ER)",
                "category": "frontpage",
                "content": "<p><img style=\\"margin-bottom: 3px; vertical-align: bottom;\\" alt=\\"suriye bombali_saldiri_2912\\" src=\\"http://aa.com.tr/images/stories/AA_HABERLER/DUNYA/suriye_bombali_saldiri_2912.jpg\\" width=\\"600\\" height=\\"300\\" /><br />Five Syrians, who were wounded during clashes in their country, crossed in Turkey and were taken to hospital on Monday.***<br /><br />HATAY <br /><br /> Ambulances and medical teams, waiting in Kavalcik, Kusakli and Bukulmez villages near Turkish-Syrian border, carried five Syrians, who were shot from their arms and legs, to hospital.<br />They were taken to Reyhanli State Hospital for treatment.</p>",
                "guid": "http://aa.com.tr/tr/component/content/article/111-alt-manset-haberleri-en/120228-wounded-syrians-enter-turkey-for-medical-treatment",
                "link": "http://aa.com.tr/tr/component/content/article/111-alt-manset-haberleri-en/120228-wounded-syrians-enter-turkey-for-medical-treatment",
                "pub_date": "Date(2012-03-26T13:13:35)",
                "title": "Wounded Syrians enter Turkey for medical treatment"
            },
            {
                "author": "gyildirim@aa.com.tr (GÖKSEL YILDIRIM)",
                "category": "frontpage",
                "content": "<p><img style=\\"margin-bottom: 3px; vertical-align: bottom;\\" alt=\\"hindistan kadin\\" src=\\"http://aa.com.tr/images/stories/AA_HABERLER/DUNYA/hindistan_kadin.jpg\\" width=\\"600\\" height=\\"300\\" /><br /><br />Hindistan'da, artan doğum oranıyla mücadele için ilginç bir yola başvuruldu. Kısırlaşmayı kabul edene otomobil bile var.***<br /><br />ANKARA <br /><br />Dünyanın ikinci kalabalık ülkesi Hindistan'ın Racestan eyaletinde kısırlaştırmayı kabul eden kadınlara ödül vaat edildi.<br />El Cezire'nin haberine göre 1,2 milyar nüfuslu ülkede 68 milyon kişinin yaşadığı eyalette yetkililer, kısırlaşmayı kabul eden kadınlara mutfak robotundan otomobile kadar çeşitli ödüller önerdi.<br />Eyalet yetkililerinin bu girişimi, hükümetin 1970'lerde sunduğu zoraki kısırlaştırma programının ardından şüpheyle bakılan bu yöntemle ilgili tartışmaları yeniden gündeme getirdi.<br /><br /></p>\\n<p><br /> </p>",
                "guid": "http://aa.com.tr/tr/kategoriler/yasam/105722-kisirlasana-odul",
                "link": "http://aa.com.tr/tr/kategoriler/yasam/105722-kisirlasana-odul",
                "pub_date": "Date(2011-12-06T13:04:36)",
                "title": "Kısırlaşana ödül"
            }
        ]
    }
    destructor DOMParser
    """
    test_rss("/oknetwiki/trunk/py_lib/vsft/test/feeds/e0.xml")


def test_rss3():
    """
    >>> test_rss3()
    constructor DOMParser
    {
        "msg": "Start tag expected, '<' not found, line 1, column 1",
        "suggestion": "possible is plain/text not xml",
        "xml": "no such rss type!..."
    }
    destructor DOMParser
    """
    test_rss("/oknetwiki/trunk/py_lib/vsft/test/feeds/e3.xml")


def test_rss4():
    """
    >>> test_rss4()
    constructor DOMParser
    {
        "item": [
            {
                "content": "Özgür Gündem'e özgürlük yeni yargı paketinde...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30072&catId=32",
                "pub_date": "Date(2012-03-27T12:15:36)",
                "title": "'Yayın durdurma önlenecek'"
            },
            {
                "content": "Kurtarıcı İsa katedraline baskın yapıp Putin'i protesto etmişlerdi...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30071&catId=33",
                "pub_date": "Date(2012-03-27T12:11:19)",
                "title": "'Bu kızlar şeytanın uşakları'"
            },
            {
                "content": "Merah'ın El Cezire'ye yolladığı paketin tarihi kafaları karıştırdı...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30070&catId=33",
                "pub_date": "Date(2012-03-27T12:08:33)",
                "title": "Katilin Çarşamba sırrı"
            },
            {
                "content": "Ferzan Özpetek, yeni filmi 'Şahane Misafir'i anlattı...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30069&catId=39",
                "pub_date": "Date(2012-03-27T12:03:48)",
                "title": "'Cem öyle namussuz ki'"
            },
            {
                "content": "Düzenli çikolata yiyenler daha zayıf oluyor...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30068&catId=35",
                "pub_date": "Date(2012-03-27T11:59:10)",
                "title": "Çikolata sevenlere müjde"
            },
            {
                "content": "Eskişehirspor-Fenerbahçe maçı iddiasına yanıt...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30067&catId=37",
                "pub_date": "Date(2012-03-27T11:54:44)",
                "title": "'Bir Galatasaraylı olarak...'"
            },
            {
                "content": "'Şehitliği ayağa düşürmek haddinize değil'",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30066&catId=32",
                "pub_date": "Date(2012-03-27T11:51:07)",
                "title": "Bahçeli'den 'şehit' çıkışı"
            },
            {
                "content": "Metro Holding'de arama yapılıyor...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30065&catId=32",
                "pub_date": "Date(2012-03-27T11:43:34)",
                "title": "İstanbul'da operasyon"
            },
            {
                "content": "Özge Özpirinçci'nin havaalanındaki polis memuru ile ilginç diyaloğu...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30064&catId=38",
                "pub_date": "Date(2012-03-27T11:38:57)",
                "title": "İngiliz polisi de şaşırdı"
            },
            {
                "content": "Anne ve karnındaki 4 aylık bebek iğne kurbanı oldu...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30063&catId=35",
                "pub_date": "Date(2012-03-27T11:36:30)",
                "title": "İğne skandalı"
            },
            {
                "content": "İlginç tarzıyla dikkat çeken ünlü şarkıcı bu kez makyajsız...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30062&catId=38",
                "pub_date": "Date(2012-03-27T11:34:15)",
                "title": "Lady Gaga şaşırttı"
            },
            {
                "content": "İşte Medvedev'le görüşen Obama'nın Putin'e gönderdiği mesaj...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30061&catId=33",
                "pub_date": "Date(2012-03-27T11:24:17)",
                "title": "Obama açık mikrofona yakalandı"
            },
            {
                "content": "Ünlü yönetmen, okyanusun en derin çukurundan döndü...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30060&catId=34",
                "pub_date": "Date(2012-03-27T11:15:51)",
                "title": "'Denizin dibi gezegen gibi'"
            },
            {
                "content": "Endonezya'da eşek arısının yeni bir türü keşfedildi...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30059&catId=34",
                "pub_date": "Date(2012-03-27T11:08:53)",
                "title": "'Şeytani' eşek arısı"
            },
            {
                "content": "Los Angeles'ta pilotluk yeteneklerini sergilerken görüntülendi...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30058&catId=38",
                "pub_date": "Date(2012-03-27T11:06:26)",
                "title": "Angelina Jolie göklerde"
            },
            {
                "content": "'Bu ülkede sıkıyönetim yok ama apoleti olmayan generaller, devlet başkanları var'",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30057&catId=32",
                "pub_date": "Date(2012-03-27T10:55:54)",
                "title": "Gazetecilere özgürlüğü anlattı"
            },
            {
                "content": "Gülen'den Şık ve Şener açıklaması...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30056&catId=32",
                "pub_date": "Date(2012-03-27T10:24:51)",
                "title": "'Benden bilseler de...'"
            },
            {
                "content": "Melek ile Mesut arasındaki yakınlaşma daha da artıyor",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30055&catId=42",
                "pub_date": "Date(2012-03-27T10:23:58)",
                "title": "Melek ve Mesut sinemada"
            },
            {
                "content": "Nursel Ergin'in sunuculuğunu üstlendiği Mutfağım, bugün Gaziantep'te.",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30054&catId=42",
                "pub_date": "Date(2012-03-27T10:06:44)",
                "title": "Mutfağım'dan Gaziantep lezzetleri"
            },
            {
                "content": "Vücut dili uzmanları bu işareti yorumladı...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30053&catId=32",
                "pub_date": "Date(2012-03-27T11:27:12)",
                "title": "Erdoğan'ın bu el hareketinin anlamı ne?"
            },
            {
                "content": "Gaziantep'in yöresel tatlarından Antep Fıstıklı Kurabiye'nin tarifi, Mutfağım\\n            programında...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30052&catId=31",
                "pub_date": "Date(2012-03-27T09:58:34)",
                "title": "Antep Fıstıklı Kurabiye tarifi"
            },
            {
                "content": "Gaziantep'in yöresel tatlarından Acılı Ekmek'in tarifi, Mutfağım programında...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30051&catId=31",
                "pub_date": "Date(2012-03-27T09:57:03)",
                "title": "Acılı Ekmek tarifi"
            },
            {
                "content": "Gaziantep'in yöresel tatlarından Ispanaklı Yoğurtlu Köfte'nin tarifi, Mutfağım\\n            programında...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30050&catId=31",
                "pub_date": "Date(2012-03-27T09:55:13)",
                "title": "Ispanaklı Yoğurtlu Köfte tarifi"
            },
            {
                "content": "Gaziantep'in yöresel tatlarından Şekerli Peynirli Börek'in tarifi, Mutfağım\\n            programında...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30049&catId=31",
                "pub_date": "Date(2012-03-27T09:53:27)",
                "title": "Şekerli Peynirli Börek tarifi"
            },
            {
                "content": "Başbuğ kısa bir savunma yaptı...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30048&catId=32",
                "pub_date": "Date(2012-03-27T11:17:57)",
                "title": "'Yetersizliğin komedisidir'"
            },
            {
                "content": "Gaziantep'in yöresel tatlarından Yeşil Zeytin Böreği'nin tarifi, Mutfağım programında...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30047&catId=31",
                "pub_date": "Date(2012-03-27T09:51:16)",
                "title": "Yeşil Zeytin Böreği tarifi"
            },
            {
                "content": "Eren’in ailesi Evren’le hesaplaşacak...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30046&catId=32",
                "pub_date": "Date(2012-03-27T09:46:54)",
                "title": "'Ölüm emrini siz verdiniz'"
            },
            {
                "content": "Erdoğan'ın emriyle nefes kesen tahliye...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30045&catId=32",
                "pub_date": "Date(2012-03-27T10:10:04)",
                "title": "Şam Büyükelçisi Türkiye'de"
            },
            {
                "content": "Elektriğe zam baskısı...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30044&catId=36",
                "pub_date": "Date(2012-03-27T09:35:29)",
                "title": "Nisan'da fatura kabarabilir!"
            },
            {
                "content": "Listedeki ilk üç ürün Türkiye'den...",
                "link": "http://www.kanaldhaber.com.tr/haber.aspx?haberid=30043&catId=35",
                "pub_date": "Date(2012-03-27T09:32:04)",
                "title": "Sebze-meyvede zehir alarmı"
            }
        ]
    }
    destructor DOMParser
    """
    test_rss("/oknetwiki/trunk/py_lib/vsft/test/feeds/e37.xml")

def test_rss5():
    """
    >>> test_rss5()
    constructor DOMParser
    {
        "item": [
            {
                "content": "Adalet Bakanlığı, Özgür Gündem gazetesinin yayınının durdurulması kararıyla ilgili açıklama\\n                yaptı<p> </p>\\n                Adalet Bakanlığı, yayın organlarının kapatılma riskiyle karşıya kalmamaları için hazırlanan ve 3. yargı\\n                paketi olarak bilinen düzenlemenin bu yılın Ocak ayında TBMMye sunulduğu hatırlatılarak, bu düzenleme\\n                Genel Kurulda görüşüldükten sonra, yayın organlarının kapatılmasının önüne geçileceği bildirildi.\\n\\n                Adalet Bakanlığından, Özgür Gündem gazetesinin yayınının durdurulması kararıyla ilgili açıklama yapıldı.\\n\\n                Yayın organlarının daha özgür bir ortamda yayın hayatını sürdürebilmeleri ve kapatılma riskiyle karşıya\\n                kalmamaları için Adalet Bakanlığınca hazırlanan düzenlemenin Ocak 2012 de...",
                "guid": "http://www.posta.com.tr/siyaset/HaberDetay/Bakanlik__Yayin_durdurmanin_onune_gecilecek.htm?ArticleID=114927",
                "link": "http://www.posta.com.tr/siyaset/HaberDetay/Bakanlik__Yayin_durdurmanin_onune_gecilecek.htm?ArticleID=114927",
                "pub_date": "Date(2012-03-27T09:17:00)",
                "title": "Bakanlık: Yayın durdurmanın önüne geçilecek"
            },
            {
                "content": "Türkiye'nin Şam Büyükelçisi Ömer Önhon feribotla Mersin Limanı'na geldi<p> </p>\\n                Beyrut Limanından dün saat 18.30 sularında hareket eden, Büyükelçi Önhon ve 26 kişiden oluşan\\n                büyükelçilik personelini taşıyan Fergün Denizcilik AŞye ait \\"Caroline\\" isimli feribot, 11.53te Mersin\\n                Limanına giriş yaptı.\\n\\n                Büyükelçi Önhon ve beraberindekileri taşıyan feribot, römorkörler eşliğinde limandaki 1 nolu rıhtıma\\n                yanaştı.\\n\\n                Kaptan Eryaşar: \\"Güvenli bir şekilde Türkiyeye geldik\\"\\n\\n                \\"Caroline\\" isimli feribotun kaptanı Eryaşar, Türkiyenin Şam Büyükelçisi Ömer Önhon ile elçilik\\n                personelini alarak dün Beyrut Limanından saat 18.30da hareket ettiklerini söyledi.\\n\\n                Feribotta Bü...",
                "guid": "http://www.posta.com.tr/siyaset/HaberDetay/Sam_buyukelcimiz_feribotla_geldi.htm?ArticleID=114926",
                "link": "http://www.posta.com.tr/siyaset/HaberDetay/Sam_buyukelcimiz_feribotla_geldi.htm?ArticleID=114926",
                "pub_date": "Date(2012-03-27T09:07:00)",
                "title": "Şam büyükelçimiz feribotla geldi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971201.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Hafta sonu sahasında Fenerbahçe'yi konuk edecek olan\\n                Trabzonspor'da, Galatasaray maçında başına darbe alan Giray'ın forma giyebileceği bildirildi<p>\\n                </p>\\n                Bordo-mavili kulübün internet sitesinden yayımlanan açıklamada, Girayın durumunun ciddi olmadığı\\n                belirtilerek, \\"Takımımızın Galatasaray ile oynadığı müsabakada rakibi ile girdiği pozisyonda başına\\n                darbe alan Giray Kaçarda cilt altı kanama meydana gelmiştir. Oyuncumuzun sağlığıyla ilgili herhangi bir\\n                endişe verici durumu söz konusu değildir\\"ifadelerine yer verildi.\\n\\n                Bordo-mavili takımda sakatlıkları süren Vittek ve Glowacki ile kart cezalısı Zokora, Fenerbahçe maçında\\n                forma giyemeyecek.",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Trabzonspor_a_Giray_mujdesi.htm?ArticleID=114925",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Trabzonspor_a_Giray_mujdesi.htm?ArticleID=114925",
                "pub_date": "Date(2012-03-27T09:06:00)",
                "title": "Trabzonspor'a Giray müjdesi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971214.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Tartışmalı Dukan diyetinin mimarı Dr. Pierre Dukan hakkında\\n                17 yaşındaki gençlerin tavsiye edilen kiloda olup olmadığının belirleneceği bir sınavdan geçmelerini\\n                önerdiği için disiplin soruşturması açı<p> </p>\\n                BBCnin haberine göre, Fransız Hekimler Birliği, 'doktorların yaptıkları yorumların halk üzerindeki\\n                etkilerini dikkate almak zorunda' olduğuna dair mesleki ilkeyi ihlal ettiği gerekçesiyle Dukan hakkında\\n                şikayette bulundu.\\n\\n                Altı ay içinde duruşmaya çıkması beklenen Dukanın haksız bulunması durumunda meslekten men edilebileceği\\n                bildirildi. Dukan, liseden mezun olmadan önce yapılan sınavlara obezite karşıtı bir seçeneğin\\n                eklenmesini ve kabul edilebilir vücut kitle endeksine sahip öğrencilere fazladan not verilmesini\\n                önermişti.\\n\\n                DOKTORDAN ÇOK TÜCCAR\\n\\n\\n                Fransız Hekimler Birliği, böyl...",
                "guid": "http://www.posta.com.tr/saglik/HaberDetay/Unlu_diyetisyen_Dukan_a_sok_sorusturma.htm?ArticleID=114924",
                "link": "http://www.posta.com.tr/saglik/HaberDetay/Unlu_diyetisyen_Dukan_a_sok_sorusturma.htm?ArticleID=114924",
                "pub_date": "Date(2012-03-27T08:57:00)",
                "title": "Ünlü diyetisyen Dukan'a şok soruşturma"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971186.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Antalya'nın Kemer ilçesinde bir ihbarı değerlendiren polis, 3\\n                bin şişe sahte parfüm ele geçirdi<p> </p>\\n                Kemer Emniyet Müdürlüğüne bağlı ekipler, ilçeye bir kamyonetle sahte parfüm getirildiği ihbarı üzerine\\n                yaptıkları operasyonda, 3 bin şişe sahte parfüm ele geçirdi.\\n\\n                Merkez Mahallesi Akdeniz Caddesinde dün saat 18.00 sıralarında 07 CUJ 21 plakalı kamyoneti durduran\\n                ekipler, dorsedeki kolileri kontrol etti.\\n\\n                Çeşitli markalardaki parfümlerin sahte olduğunu belirleyen ekipler, sürücü ve yanındaki 1 kişiyi\\n                gözaltına aldı.\\n\\n                Şüpheliler, kargo firmasında çalıştıklarını, parfümleri Kemerde bir depoya teslim etmek üzere firmadan\\n                aldıklarını, olayla bir ilgilerinin olmadığını öne sürdü....",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Sahte_parfum_operasyonu.htm?ArticleID=114922",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Sahte_parfum_operasyonu.htm?ArticleID=114922",
                "pub_date": "Date(2012-03-27T08:54:00)",
                "title": "Sahte parfüm operasyonu"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971194.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Yargıtay 9. Ceza Dairesi, Lefkoşa-İstanbul seferini yapan\\n                Atlasjet uçağını kaçıran 2 sanığa verilen 27 yıl 6'şar ay hapis cezasını az bularak bozdu<p> </p>\\n                Yargıtay 9. Ceza Dairesi, sanıkların terör örgütü El Kaide üyesi oldukları ve eylemlerinin, örgütün,\\n                Türkiye Cumhuriyeti Anayasasını zorla değiştirip yerine dini esaslara dayalı bir sistem getirmek\\n                şeklindeki amacına yönelik olduğu sonucuna vardı. Sanıklara ağırlaştırılmış müebbet hapis cezası\\n                verilmesi gerektiğine hükmedildi.\\n\\n                İzmir 10. Ağır Ceza Mahkemesi, Lefkoşa-İstanbul seferini yapan Atlasjet uçağını kaçıran Mehmet Reşat\\n                Özlü ve Filistin uyruklu Mümin Abdülaziz Cuma Telikh hakkında, \\"silahlı terör örgütüne üye olmamakla\\n                birlikte örgüt adına suç işleme, hava ulaşım aracını kaçırma ...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/Hava_korsanlarina_agirlastirilmis_muebbet_hapis.htm?ArticleID=114923",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/Hava_korsanlarina_agirlastirilmis_muebbet_hapis.htm?ArticleID=114923",
                "pub_date": "Date(2012-03-27T08:52:00)",
                "title": "Hava korsanlarına ağırlaştırılmış müebbet hapis"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971175.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Ünlü popçu Demet Akalın kameraların önünde küfür ederek\\n                herkesi şaşırttı, daha sonra gülerek olayı toparlamaya çalıştı<p> </p>\\n                Okan Kurt'la yaşadığı fırtınalı aşkla gündemden düşmeyen Demet Akalın, bu kez ettiği küfürle herkesi\\n                şoke etti.\\n\\n                Akalın, İstanbul Harbiye'de bir mekân çıkışında kameraların önünde \\"Para var, huzur yok a.... k...\\"\\n                dedi.\\n\\n                Ünlü popçu, daha sonra gülerek olayı toparlamaya çalıştı.",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Demet_Akalin_dan_kufur_soku_.htm?ArticleID=114921",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Demet_Akalin_dan_kufur_soku_.htm?ArticleID=114921",
                "pub_date": "Date(2012-03-27T08:34:00)",
                "title": "Demet Akalın'dan küfür şoku!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971168.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />ABD'de yapılan araştırmada düzenli olarak çikolata\\n                yiyenlerin, nadiren yiyenlerden daha zayıf olduğu ortaya çıktı<p> </p>\\n                ABDde yapılan araştırmada düzenli olarak çikolata yiyenlerin, nadiren yiyenlerden daha zayıf olduğu\\n                ortaya çıktı. Bilim insanları, sonuçları Archives of Internal Medicine dergisinde yayımlanan\\n                araştırmalarında, 1000'in üzerinde kadın ve erkeğin verilerini inceledi.\\n\\n                Araştırmaya katılanların şeker, kalp veya diğer önemli hastalıklarının bulunmamasına dikkat edildi.\\n                Araştırmada, düzenli olarak çikolata yiyenlerin vücut kitle endeksinin daha düşük olduğu tespit edildi.\\n\\n                Bilim insanları, vücut kitle endeksi ile düzenli çikolata tüketimi arasındaki bu bağlantının büyük\\n                ihtimalle çikolat...",
                "guid": "http://www.posta.com.tr/saglik/HaberDetay/Duzenli_cikolata_yiyenler_daha_zayif.htm?ArticleID=114920",
                "link": "http://www.posta.com.tr/saglik/HaberDetay/Duzenli_cikolata_yiyenler_daha_zayif.htm?ArticleID=114920",
                "pub_date": "Date(2012-03-27T08:31:00)",
                "title": "Düzenli çikolata yiyenler daha zayıf"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971160.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Basketbol FIBA Kadınlar Avrupa Ligi'nde yarın İstanbul'da\\n                başlayacak Sekizli Final organizasyonunda ilginç istatistikler dikkat çekiyor<p> </p>\\n                Avrupa kadın basketbolunda en iyi takımın belirleneceği Sekizli Finalde yer alacak 8 ekip arasında\\n                Fenerbahçe, 1.86 boy ortalamasıyla en uzun takım olarak dikkati çekerken, 1.82 ortalamasına sahip\\n                İspanyol ekibi Rivas Ecoplis de en kısa takım konumunda bulunuyor.\\n\\n                İspanyol temsilcisi Rivas Ecopolisin, 25,5 yaş ortalamasıyla en genç takım unvanını elinde bulundurduğu\\n                Sekizli Finalde, kupa mücadelesi verecek en tecrübeli ekip ise 28,9 ortalamasıyla İtalyadan Beretta\\n                Famila Schio olacak.\\n\\n                UMMC Ekaretinburgtan Maria Stepanova 2,03 metre boyuyla organizasyonun en uzun boylu oyuncusu...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Rakamlarla__Sekizli_Final_.htm?ArticleID=114919",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Rakamlarla__Sekizli_Final_.htm?ArticleID=114919",
                "pub_date": "Date(2012-03-27T08:25:00)",
                "title": "Rakamlarla 'Sekizli Final'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971153.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />İran, yaptırımların daha katı hale gelmesi veya askeri bir\\n                gerginlik yaşanma ihtimaline karşı stoklama yoluna gidiyor<p> </p>\\n                İran, buğday ithalatına hız verdi. Tahran, yaptırımların daha katı hale gelmesi veya askeri bir\\n                gerginlik yaşanma ihtimaline karşı stoklama yoluna gidiyor.\\n\\n                ABD'li Wall Street Journal Gazetesi'nin haberine göre İran, geride kalan birkaç ay boyunca ABD,\\n                Avustralya, Brezilya ve Kazakistan'dan buğday satın aldı. Aynı zamanda büyük ölçekte alım yapmak için\\n                Hindistan ile görüşüyor.\\n\\n                Georgetown Üniversitesi'nden Paul Sullivan, yağmurların az olması nedeniyle de buğday alımlarının İran\\n                için kritik önem taşıdığını ifade etti. İran'da hasat Mayıs'ta yapılacak.\\n\\n                İran'ın buğday alımları bu yı...",
                "guid": "http://www.posta.com.tr/dunya/HaberDetay/Iran_bugdaya_hucum_etti.htm?ArticleID=114918",
                "link": "http://www.posta.com.tr/dunya/HaberDetay/Iran_bugdaya_hucum_etti.htm?ArticleID=114918",
                "pub_date": "Date(2012-03-27T08:25:00)",
                "title": "İran buğdaya hücum etti"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971144.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Adana'da üvey kızı 14 yaşındaki S.K'ya yaklaşık 2 yıl önce\\n                tecavüz edip, sonra da \\"Anneni boşayıp seninle evleneceğim\\" diyen 40 yaşındaki Ali A'ya 18 yıl hapis\\n                isteniyor<p> </p>\\n                Merkez Seyhan ilçesine bağlı Şakirpaşa Mahallesinde seyyar satıcılık yapan Ali A., 9 yıl önce, bir çocuk\\n                annesi 38 yaşındaki H.A. ile ikinci evliliğini yaptı. Çiftin bu evlilikten iki çocukları oldu.\\n\\n                H.A., boşandığı ilk eşi bir yıl kadar önce başka kadınla evlenince, ondan olan kızı S.K.yı yanına aldı.\\n                Ali A. yanlarında kalmaya başlayan üvey kızı S.K.ya tecavüz etti. Ali A. ardından da, \\"Seni seviyorum.\\n                Annene bunları anlatma. Onu boşayıp seni alacağım\\" diye kandırdığı S.K. ile 2 yıl süreyle ilişkiyi\\n                sürdürdü.\\n\\n                Geçen 15 Martta Ali A., eşi H.A.nın gündüz komşuya gittiği sırada...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Uvey_kiza_tecavuze_18_yil_istemi.htm?ArticleID=114917",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Uvey_kiza_tecavuze_18_yil_istemi.htm?ArticleID=114917",
                "pub_date": "Date(2012-03-27T08:20:00)",
                "title": "Üvey kıza tecavüze 18 yıl istemi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971137.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />İzmir'de rüyasında aldatıldığını gören M.G. mesai bitimi\\n                döndüğü evinde eşi F.G.'yi 15 yerinden bıçakla yaralayıp kaçtı. Tedaviye alınan kadının hayati\\n                tehlikesinin sürdüğü belirtildi<p> </p>\\n                Güney Mahallesi'nde  oturan ve yaklaşık bir yıl önce dünya evine giren çiften öfkeli koca, eşine dehşet\\n                dolu dakikalar yaşattı. Trafik takip işiyle uğraşan ağabeyinin yanında çalışan 19 yaşındaki M.G., mesai\\n                bitimi dün saat 22.30 sıralarında evine döndü.\\n\\n                15 YERİNDEN BIÇAKLADI\\n\\n                M.G., eşine bir gün önce gördüğü rüyayı anlattı. M.G.nin rüyasında ev kadını olan eşi 18 yaşındaki\\n                F.G.nin, iddiaya göre, kendisini aynı mahallede oturan bir kişiyle aldattığını söylemesi üzerine\\n                tartışma çıktı. Büyüyen tartışma sonucu sinirlerine hakim olamayan M.G., mutfaktan aldığı bıçakla F.G.yi\\n                vücud...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Ruyasinda_aldatildi__karisini_bicakladi.htm?ArticleID=114913",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Ruyasinda_aldatildi__karisini_bicakladi.htm?ArticleID=114913",
                "pub_date": "Date(2012-03-27T08:09:00)",
                "title": "Rüyasında aldatıldı, karısını bıçakladı"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971127.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />CHP, milletvekili emekli aylığını düzenleyen kanunun bazı\\n                maddelerinin iptali için Anayasa Mahkemesi'ne başvurdu.<p> </p>\\n                CHP Grup Başkanvekili Muharrem İncenin mahkemeye sunduğu dava dilekçesinde, Türkiye Cumhuriyeti Emekli\\n                Sandığı Kanunu ile Bazı Kanunlarda\\n                Değişiklik Yapan Kanunun bazı maddelerinin iptali isteniyor.",
                "guid": "http://www.posta.com.tr/siyaset/HaberDetay/CHP__emekli_ayligi_duzenlemesine_itiraz_etti.htm?ArticleID=114912",
                "link": "http://www.posta.com.tr/siyaset/HaberDetay/CHP__emekli_ayligi_duzenlemesine_itiraz_etti.htm?ArticleID=114912",
                "pub_date": "Date(2012-03-27T08:09:00)",
                "title": "CHP, emekli aylığı düzenlemesine itiraz etti"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971120.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Şişli'de 11 yaşındaki çocuğunun kanserden hayatını kaybetmesi\\n                ve 2 bin 500 TL borcu intihara kalkışan İsmail Öztürk'ü Belediye Başkanı Mustafa Sarıgül ikna etti<p>\\n                </p>\\n                Büyükdere Caddesinde saat 08.00 sıralarında bir inşaatın 35 metrelik vincine çıkan İsmail Öztürkü fark\\n                eden çevredekiler, polisten yardım istedi.\\n\\n                İtfaiye ve sağlık ekipleri olay yerinde önlem aldı. İtfaiye merdiveni ile yaklaşan bir polis memuruna\\n                adının İsmail Öztürk olduğunu söyleyen şahıs, cep telefonunun numarasını verdi.\\n\\n                Aşağıdan numarayı arayan görevlilere, bir aydır işsiz olduğunu, kira ve esnafa olan borçlarından dolayı\\n                bunalıma girdiğini söyledi. Şişli Belediye Başkanı Mustafa Sarıgül de saat 09.00 sıralarında gelerek\\n                vincin üzerindeki İsmail Öztürk ile telefonla görüşt...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Sarigul_intihardan_vazgecirdi.htm?ArticleID=114914",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Sarigul_intihardan_vazgecirdi.htm?ArticleID=114914",
                "pub_date": "Date(2012-03-27T08:05:00)",
                "title": "Sarıgül intihardan vazgeçirdi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971113.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Fenerbahçe'nin Lille'den transfer ettiği Senegalli futbolcu\\n                Moussa Sow, Türkiye'de kendini iyi hissettiğini ve Lille'deki arkadaşlarını özlediğini söyledi<p>\\n                </p>\\n                Sow, Fransız RMC Radyosuna yaptığı açıklamada, Lilleden ayrılmasının üzerinden 2 ay geçtiğini\\n                belirterek, Türkiyede kendini iyi hissettiğini ifade etti.\\n\\n                Moussa Sow, \\"Yeni bir hayata yelken açtım, ancak Lillei takip etmeyi sürdürüyorum. Arkadaşlarımı, Rioyu,\\n                Aurelien Chedjouyu, Mathieu Debuchyyi ve Eden Hazardı özlüyorum. Orada çok iyi günler geçirdim, ancak bu\\n                futbol, diğerleri de sezon sonunda farklı takımlara gidebilir\\" dedi.",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Sow_arkadas_hasreti_cekiyor.htm?ArticleID=114911",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Sow_arkadas_hasreti_cekiyor.htm?ArticleID=114911",
                "pub_date": "Date(2012-03-27T08:01:00)",
                "title": "Sow arkadaş hasreti çekiyor"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971105.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Bartın'ın Amasra İlçesi'nde bir bankaya ait ATM'yi oksijen\\n                kaynağı ile keserek açmaya çalışan hırsızlar ateşin paralara sıçramaması için kola kullandı<p>\\n                </p>\\n                Amasra Kültür Parkta yan yana duran farklı bankalara ait oksijen kaynağı ile saat 02.30 sıralarında\\n                gelen 2 hırsız, otomatik para çekme makinesinin kasa bölümünü kesmeye başladı. Hırsızlar ateşin paralara\\n                sıçramaması için yanlarında bulunan 2.5 litrelik şişeden kola döktü. Alarm sisteminin devreye girmesi\\n                üzerine polis ekipleri sevk edildi. Polislerin geldiğini gören hırsızlardan biri kaçarken, Y.B.,\\n                gözaltına alındı.\\n\\n                Polis, soygunda kullanılan aletlere el koyarken, ATMdeki paralar çağrılan banka görevlileri nezaretinde\\n                sayılarak kayıt altına alındı. Polis kaçan kişinin yakalanması iç...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Bankamatikte_kolali_soygun.htm?ArticleID=114910",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Bankamatikte_kolali_soygun.htm?ArticleID=114910",
                "pub_date": "Date(2012-03-27T07:58:00)",
                "title": "Bankamatikte kolalı soygun"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971091.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Hükümeti halka şikayet etme kararı alan CHP, bugün grup\\n                toplantısını Ankara Tandoğan Meydanı'nda yapacak<p> </p>\\n                Hükümeti halka şikayet etme kararı alan CHP, bugün grup toplantısını Tandoğan Meydanında yapacak.\\n                Kılıçdaroğlu ise 4+4+4 görüşmeleri sırasında milletvekillerine Bu sefer kürsüyü işgal etmeyin talimatı\\n                verdi.\\n\\n                CHPnin, bugün Meclis Genel Kurulunda görüşmelerine başlanacak kesintili ve kademeli zorunlu eğitim\\n                sistemi öngören 4+4+4 teklifine ilişkin kritik bir karar verdiği öğrenildi. CHP, iç tüzük görüşmelerinde\\n                yaptığı gibi kürsüyü işgal etme yoluna gitmeme kararı aldı. \\n\\n                >> ANKARA TRAFİĞİNE MİTİNG AYARI\\n\\n                CHP lideri Kemal Kılıçdaroğlu, kurmayları yaptığı toplantıda kürsü işg...",
                "guid": "http://www.posta.com.tr/siyaset/HaberDetay/CHP_bugun_Tandogan_da.htm?ArticleID=114909",
                "link": "http://www.posta.com.tr/siyaset/HaberDetay/CHP_bugun_Tandogan_da.htm?ArticleID=114909",
                "pub_date": "Date(2012-03-27T07:55:00)",
                "title": "CHP bugün Tandoğan'da"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971099.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />İran, yaptırımların daha katı hale gelmesi veya askeri bir\\n                gerginlik yaşanma ihtimaline karşı stoklama yoluna gidiyor.<p> </p>\\n                İran, buğday ithalatına hız verdi. Tahran, yaptırımların daha katı hale gelmesi veya askeri bir\\n                gerginlik yaşanma ihtimaline karşı stoklama yoluna gidiyor.\\n\\n                ABD'li Wall Street Journal Gazetesi'nin haberine göre İran, geride kalan birkaç ay boyunca ABD,\\n                Avustralya, Brezilya ve Kazakistan'dan buğday satın aldı.\\n\\n                Aynı zamanda büyük ölçekte alım yapmak için Hindistan ile görüşüyor. Georgetown Üniversitesi'nden Paul\\n                Sullivan, yağmurların az olması nedeniyle de buğday alımlarının İran için kritik önem taşıdığını ifade\\n                etti. İran'da hasat Mayıs'ta yapılacak.\\n\\n                İran'ın buğday alımları bu ...",
                "guid": "http://www.posta.com.tr/dunya/HaberDetay/Iran__bugday_stokluyor.htm?ArticleID=114907",
                "link": "http://www.posta.com.tr/dunya/HaberDetay/Iran__bugday_stokluyor.htm?ArticleID=114907",
                "pub_date": "Date(2012-03-27T07:50:00)",
                "title": "İran, buğday stokluyor"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971074.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />(MEMEDER), Meme Kanseri Erken Tanı ve Tarama Projesi ile\\n                İstanbul Tabip Odası'nın her yıl düzenlediği \\"Prof. Dr. Nusret Fişek Halk Sağlığı Ödülleri\\" yarışmasına\\n                katıldı. Proje, Bilimsel Teşvik Ödülü'n<p> </p>\\n                2008 yılında İstanbulda başlatılan ve 5.329 kadının ücretsiz olarak meme kanseri taramasından\\n                geçirildiği Meme Kanseri Erken Tanı ve Tarama Projesi ile bugüne kadar 33 hastaya erken meme kanseri\\n                tanısı konuldu.\\n\\n                10 yıl süreyle devam edecek olan proje Bahçeşehir Belediyesi ve ilaç firması Rocheun ana sponsorluğunda\\n                gerçekleştiriliyor.\\n\\n                2007de kurulan MEMEDER; uzman kadro, kurum ve gönüllülerle birlikte meme sağlığı konusunda toplumu\\n                bilinçlendirmek, hastalara sosyal-psikolojik destek vermek, yaşam kalitesi ve süresini uzatmak, bilimsel\\n                proje ve sosyal etkinliklerle tıbba ve insanlar...",
                "guid": "http://www.posta.com.tr/saglik/HaberDetay/MEMEDER_e__Bilim_Tesvik_odulu.htm?ArticleID=114906",
                "link": "http://www.posta.com.tr/saglik/HaberDetay/MEMEDER_e__Bilim_Tesvik_odulu.htm?ArticleID=114906",
                "pub_date": "Date(2012-03-27T07:46:00)",
                "title": "MEMEDER'e 'Bilim Teşvik Ödülü"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm971083.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />\\"Futbolda şike\\" iddiaları üzerine aralarında Fenerbahçe\\n                Başkanı Aziz Yıldırım'ın da bulunduğu 16'sı tutuklu 93 sanık açılan davanın 10. duruşması görülmeye\\n                başlandı<p> </p>\\n                Özel yetkili İstanbul 16. Ağır Ceza Mahkemesince görülen duruşmaya aralarında Aziz Ylıdırım ve Olgun\\n                Pekerin bulunduğu 16 tutuklu sanık katıldı.\\n\\n                Tutuksuz sanıklardan ise bir önceki celse tahliye edilen Şekip Mosturoğlunun yanı sıra savunmalarını\\n                yapmak üzere Ümit Karanın da aralarında bulunduğu çok sayıda tutuksuz sanık duruşmada hazır bulundu.\\n\\n                \\"BİR GALATASARAYLI OLARAK...\\"\\n\\n                Mahkeme Başkanı Mehmet Ekinci tutuksuz sanıklardan Ümit Karanı sanık kürsüsüne çağırdı. Karan\\n                savunmasında, \\"Şu anda hayatım alt üst oldu. Böyle bir olayda adımın geçmesi beni çok üzdü\\" dedi.\\n\\n                Es...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Umit_Karan_dan_tartisilacak_aciklama.htm?ArticleID=114908",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Umit_Karan_dan_tartisilacak_aciklama.htm?ArticleID=114908",
                "pub_date": "Date(2012-03-27T07:45:00)",
                "title": "Ümit Karan'dan tartışılacak açıklama"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970997.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" /><p> </p>",
                "guid": "http://www.posta.com.tr/yasam/fotogaleri/FotoGaleri/En_ilginc_fotograflar.htm?ArticleID=114905",
                "link": "http://www.posta.com.tr/yasam/fotogaleri/FotoGaleri/En_ilginc_fotograflar.htm?ArticleID=114905",
                "pub_date": "Date(2012-03-27T07:44:00)",
                "title": "En ilginç fotoğraflar"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970989.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" /><p> </p>\\n                Türk Hava Yolları (THY), Suriyede yaşanan olaylar nedeniyle Şam ve Halepe olan bilet satışlarını 1 Nisan\\n                itibarıyla durdurdu.\\n\\n                THY Basın Müşavirliğinden alınan bilgiye göre, THYnin Şam ve Halepe olan seferleri için rezervasyon\\n                işlemleri, 1 Nisan itibarıyla durduruldu.\\n\\n                THY, İstanbul Atatürk Havalimanından Şama haftada 7, Halepe ise 5 sefer gerçekleştiriyor.",
                "guid": "http://www.posta.com.tr/ekonomi/HaberDetay/THY__Suriye_seferlerine_ara_veriyor.htm?ArticleID=114903",
                "link": "http://www.posta.com.tr/ekonomi/HaberDetay/THY__Suriye_seferlerine_ara_veriyor.htm?ArticleID=114903",
                "pub_date": "Date(2012-03-27T07:42:00)",
                "title": "THY, Suriye seferlerine ara veriyor"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970981.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Antalya Emniyet Müdürlüğü ekipleri, kapı göbek kilitlerini\\n                kırarak evlerden hırsızlık yapan çeteye yönelik 3 ilde düzenlediği eş zamanlı operasyonla 13 kişiyi\\n                gözaltına aldı<p> </p>\\n                Antalya Emniyeti Asayiş Şube Müdürlüğü Hırsızlık Büro Amirliği ekipleri, kentte faaliyet gösteren ve\\n                birlikte hareket eden iki hırsızlık çetesini takibe aldı.\\n\\n                2 ay süren teknik ve fiziki takibin ardından önceki gün Diyarbakırda, İzmirde ve Antalyada 100 polisin\\n                katıldığı eş zamanlı operasyon düzenlenirken, 13 kişi gözaltına alındı.\\n\\n                Liderliklerini Bayram A. ve Adem A.nın yaptığı iki hırsızlık çetesi üyeleri Müjdat A., İbrahim T., Evren\\n                A., Ozan C., Ramazan Y., Murat B. ve Sedat D. Antalyada, Kasım T. ve Ferhat T. Diyarbakırda, Çetin O. ve\\n                Veysi O. ise İzmirde yakalanarak ken...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Caldigi_LCD_yi_babasina_gonderdi.htm?ArticleID=114904",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Caldigi_LCD_yi_babasina_gonderdi.htm?ArticleID=114904",
                "pub_date": "Date(2012-03-27T07:41:00)",
                "title": "Çaldığı LCD'yi babasına gönderdi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970965.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Psikolojik desteğin onkolojideki önemi, hekimler, hemşireler\\n                ve diğer sağlık çalışanları tarafından iyi biliniyor ancak hasta ve hasta yakınlarına verilmesi gereken\\n                bu destek genellikle geri planda ka<p> </p>\\n                Onkoloji hastalarına ve yakınlarına verilmesi gereken psikolojik destek, Tıbbi Onkoloji Derneği'nin\\n                Antalyada yapılan 4. Tıbbi Onkoloji Kongresi'nde Kanserde bütüncül yaklaşım başlığı altında\\n                değerlendirildi.\\n\\n                İnsan vücudunun hastalandığı dönemlerde sadece fiziksel değişim göstermediğini, psikolojinin de\\n                etkilendiğini hatırlatan Dr. Aykan Özaslan, ruhsal durumun bazen hastalık sürecinin bertaraf edilmesine,\\n                bazen de tam tersine, ağırlaşmasına etki ettiğini söyledi.\\n\\n                Hastalığın türü ve şiddeti ağırlaştıkça, psikolojideki etkileşimin de artabildiğini ve tedavi sürecini\\n                önemli ölçüd...",
                "guid": "http://www.posta.com.tr/saglik/HaberDetay/Kanser_psikolojisi_onemsenmiyor.htm?ArticleID=114902",
                "link": "http://www.posta.com.tr/saglik/HaberDetay/Kanser_psikolojisi_onemsenmiyor.htm?ArticleID=114902",
                "pub_date": "Date(2012-03-27T07:38:00)",
                "title": "Kanser psikolojisi önemsenmiyor"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970972.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Lojmanı tahliye ederek boşaltmayanlardan, tahliye tarihine\\n                kadar geçecek süreler için ödenmesi gereken kira bedeli yerine işgaliye bedeli tahsil edilecek<p>\\n                </p>\\n                Bakanlar Kurulu kararıyla yürürlüğe konulan \\"Kamu Konutları Yönetmeliğinde Değişiklik Yapılmasına Dair\\n                Yönetmelik\\", Resmi Gazetenin bugünkü sayısında yayımlandı.\\n\\n                Değişikliğe göre, konutta oturma süresini doldurduğu veya konutta oturma hakkı sona erdiği halde konutu\\n                tahliye etmeyenlerden, konutu on beş gün içerisinde tahliye ederek boşaltması, aksi takdirde bu sürenin\\n                bitiminden itibaren işgaliye bedeli alınacağına ilişkin olarak İdarece yapılacak tebligata rağmen,\\n                konutu tahliye ederek boşaltmayanlardan, yeni bir tebligata gerek olmaksızın, konutun tahliye tarihine\\n                kadar geçecek sürele...",
                "guid": "http://www.posta.com.tr/ekonomi/HaberDetay/Lojmani_bosaltmayan_4_katini_odeyecek.htm?ArticleID=114901",
                "link": "http://www.posta.com.tr/ekonomi/HaberDetay/Lojmani_bosaltmayan_4_katini_odeyecek.htm?ArticleID=114901",
                "pub_date": "Date(2012-03-27T07:38:00)",
                "title": "Lojmanı boşaltmayan 4 katını ödeyecek"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970952.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Cumartesi günü Kıbrıs Rocks Otel'de sahne alan Ebru Gündeş,\\n                davetliler arasında bulunan Tuğba Ekinci'yi sahneye davet etti. Gündeş ve Ekinci bir parçayı birlikte\\n                seslendirdi<p> </p>\\n                Babakuş'un haberine göre; Kıbrıs'a ünlü isimlere özel spor hocalığı yapan genç sevgilisi Mesut Bey'le\\n                birlikte katılan Ekinci, sahnede Ebru Gündeş'le birlikte seslendirdiği şarkı nedeniyle izleyenlerden tam\\n                not aldı.",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Ebru_Gundes_ten_surpriz_duet_.htm?ArticleID=114899",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Ebru_Gundes_ten_surpriz_duet_.htm?ArticleID=114899",
                "pub_date": "Date(2012-03-27T07:35:00)",
                "title": "Ebru Gündeş'ten sürpriz düet!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970958.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Konya'da aynı gece hırsızlık amaçlı 7 işyerine giren ve\\n                kiraladığı otomobille kaçarken yakalanan 29 yaşındaki Erdal Adlar, çıkarıldığı nöbetçi mahkeme\\n                tarafından tutuklandı<p> </p>\\n                Konya Emniyet Müdürlüğü Asayiş Şubesi Hırsızlık Büro Amirliği ekipleri geçen pazartesi günü saat 02.00\\n                sıralarında merkez Selçuklu İlçesi Sancak Mahallesinde devriye gezerken şüphe üzerine bir otomobili\\n                durdurdu.\\n\\n                Otomobil sürücüsü Erdal Adların yapılan kimlik sorgulamasında hırsızlıktan 29 sabıka kaydı bulunduğu\\n                ortaya çıktı. Bunun üzerine otomobilde arama yapan polis, bagajda 1 LCD ekran televizyon, 2 dizüstü\\n                bilgisayar, 1 cep telefonu, 42 lira tutarında para ile 1 demir kesme makası buldu.\\n\\n                \\"ONLARI YOLDA BULDUM\\"\\n\\n                Polise \\"Ben onları yolda buldum\\" diyerek kendini savunan Erda...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Ayni_gece_7_isyeri_soydu.htm?ArticleID=114900",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Ayni_gece_7_isyeri_soydu.htm?ArticleID=114900",
                "pub_date": "Date(2012-03-27T07:32:00)",
                "title": "Aynı gece 7 işyeri soydu"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970945.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Eski Genelkurmay Başkanı Başbuğ, 5 dakika süren savunmasının\\n                sonunda, \\"Beni yargılayacak yer Yüce Divan'dır\\" dedi<p> </p>\\n                İnternet Andıcı Davası'nda yargılanan eski Genelkurmay Başkanı İlker Başbuğ, \\"Bu iddianameye hiçbir\\n                itibarım yoktur, yetersizliğin komedisidir. Bana terör örgütü yöneticisi diyene şaşarım\\" diye konuştu.\\n\\n                Başbuğ, savunmasında, \\"Bana terör örgütü yöneticisi diyenlere şaşarım. Bu suçlama hiçbir zaman, kişisel\\n                suçlama olarak kabul edilemez. Hayatımda hiçbir zaman hukuksuz davranmadım. İnternet andıcında herhangi\\n                bir suç unsuru görseydim, tereddütsüz soruşturma emri vereceğimiz bilmiyorlar mı? TSK personelinin\\n                masumiyet karinesi hiçe sayılarak medyaya haksız ithamlarla yıpratılmasına ve irti...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/Basbug_dan_5_dakikalik_savunma.htm?ArticleID=114898",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/Basbug_dan_5_dakikalik_savunma.htm?ArticleID=114898",
                "pub_date": "Date(2012-03-27T07:32:00)",
                "title": "Başbuğ'dan 5 dakikalık savunma"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970937.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Marsilya'nın Senegalli savunma oyuncusu Souleymane Diawara,\\n                sakatlığı nedeniyle sahalardan 6 ay uzak kalacak<p> </p>\\n                Marsilya kulübünün açıklamasında, hafta sonundaki Nice maçında sakatlanan Diawaranın sağ diz çapraz\\n                bağlarının koptuğu ve 33 yaşındaki futbolcunun gelecek hafta ameliyat edileceği belirtildi.\\n\\n                Açıklamada, Senegalli futbolcunun yaklaşık 6 ay futbol oynayamayacağı kaydedildi. Diawara, bu sezon\\n                Marsilyada sürekli olarak ilk 11de sahaya çıkıyordu.",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Diawara_6_ay_yok.htm?ArticleID=114897",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Diawara_6_ay_yok.htm?ArticleID=114897",
                "pub_date": "Date(2012-03-27T07:31:00)",
                "title": "Diawara 6 ay yok"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970912.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Uzun bir eğitimin ardından pilot ehliyeti alan Angelina\\n                Jolie, ABD'nin California Eyaleti'ndeki Van Nuys Havaalanı'ndan küçük bir uçakla havalandı<p> </p>\\n                Kendisine ait uçakla California semalarında dolaşan Jolie daha sonra sorunsuz bir şekilde yere inmeyi\\n                başardı. Jolieye uçuşta bir yardımcı pilot da eşlik etti. 6 çocuk annesi Jolie, uçarak stres attığını\\n                söylemişti.",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Angelina_ucagiyla_keyif_yapti.htm?ArticleID=114896",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Angelina_ucagiyla_keyif_yapti.htm?ArticleID=114896",
                "pub_date": "Date(2012-03-27T07:19:00)",
                "title": "Angelina uçağıyla keyif yaptı"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970905.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Her yıl Mart ayı sonlarında başlayan fok balığı avı için\\n                Kanada, bu yıl da kontenjanı artırdı<p> </p>\\n                Dünya genelinde yaşanan tüm protesto ve yasaklamalara rağmen, Kanadada bu yıl avlanmasına izin verilen\\n                fok sayısı 400 bin olarak açıklandı.\\n\\n                Kanada Federal Balıkçılık Bakanlığı, 2012 av sezonu için verilen avcı belgesine ilişkin sayıyı\\n                açıklamazken, avcıların St.Lawrence Körfezi'nden, Prince Edward İsland, New Brunswick ve\\n                Newfaoundland-Labrador'u içine alan bölgede avlanacakları kaydedildi.\\n\\n                Bakanlık yaptığı duyuruda, fokların sopalarla vurularak avlanmasına izin verilmeyeceğini, bu durumun\\n                bölgedeki ekiplerce denetleneceğini bildirdi.\\n\\n                \\"VAHŞETE İZİN VERİLİYOR\\"\\n\\n                Öte yanda...",
                "guid": "http://www.posta.com.tr/yasam/HaberDetay/Kanada_da_fok_katliami_basladi.htm?ArticleID=114895",
                "link": "http://www.posta.com.tr/yasam/HaberDetay/Kanada_da_fok_katliami_basladi.htm?ArticleID=114895",
                "pub_date": "Date(2012-03-27T07:08:00)",
                "title": "Kanada'da fok katliamı başladı"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970896.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />UEFA Avrupa Şampiyonlar Ligi'nde çeyrek final ilk maçları,\\n                yarın yapılacak iki karşılaşmayla tamamlanacak<p> </p>\\n                Marsilya, Stade Velodromeda kendi seyircisi önünde oynayacağı maçta Almanya temsilcisi Bayern Münihi\\n                ağırlayacak. Şampiyonlar Liginde çeyrek finale çıkarak 1993 yılından bu yana en iyi derecesini elde eden\\n                Marsilya, Bayern Münih ile daha önce karşılaşmadı.\\n\\n                Bayern Münih, Şampiyonlar Liginde bu sezon, kaleyi bulan şutlarda 8,38 gibi yüksek bir ortalama\\n                tutturdu. Buna karşılık Marsilya 3,62 ortalamayla oynadı.\\n\\n                Buna göre Bayern Münih, oynadığı maçlarda her 11 dakikada bir kaleyi bulan şut çekti. Bayern Münihin\\n                yıldız oyuncusu Franck Ribery, çeyrek finalde boy gösterecek futbolcu...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Sampiyonlar_Ligi_nde_dev_mac.htm?ArticleID=114894",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Sampiyonlar_Ligi_nde_dev_mac.htm?ArticleID=114894",
                "pub_date": "Date(2012-03-27T06:56:00)",
                "title": "Şampiyonlar Ligi'nde dev maç"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970872.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Jameson Empire Ödülleri törenine katılmak üzere İngiltere'ye\\n                giden Özge Özpirinçci, Londra havaalanındaki polis memurunu şaşkına çevirdi<p> </p>\\n                Popüler sinema dergisi Empireın geleneksel Jameson Empire Ödülleri, pazar gecesi Londrada yapılan\\n                törenle sahiplerini buldu. Tim Burton, Helena Bonham Carter, Gary Oldman gibi ünlülerin yer aldığı\\n                törenin davetlileri arasında Engin Altan Düzyatan ile Özge Özpirinççi çifti de vardı. Dizi çekimleri\\n                nedeniyle sevgilisinden bir gün sonra Londraya uçan Özpirinççi, havaalanında İngiliz polisiyle ilginç\\n                bir diyalog yaşadı.\\n\\n                \\"BEN SİZDEN AZ ÇALIŞIYORUM\\"  \\n\\n                Polisin, İngiltereye gelme sebebiniz nedir? sorusu üzerine Özpirinçci oyuncu olduğunu ve ödül törenini\\n                izlemek üzere ülkeye giriş y...",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Ingiliz_polisi_de_sasirdi.htm?ArticleID=114892",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Ingiliz_polisi_de_sasirdi.htm?ArticleID=114892",
                "pub_date": "Date(2012-03-27T06:56:00)",
                "title": "İngiliz polisi de şaşırdı"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970879.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Dünyaca ünlü çevre örgütü Greenpeace Avrupa'da satılan 76\\n                sebze-meyveyi test etti. Türkiye'de üretilen biber, armut ve üzüm en tehlikeli ürünler çıktı<p>\\n                </p>\\n\\n                Türk domatesi başta olmak üzere tarım ürünleri ihracı çeşitli kez İnsan sağlığına zararlı kalıntı\\n                tespitiyle sekteye uğramıştı. Türkiye buna rağmen 2011 yılında 2 milyar 339 milyon dolarlık sebze meyve\\n                ihracatı gerçekleştirmişti.\\n\\n                Vatan'ın haberine göre, çevre örgütü Greenpeace, yaptığı araştırmada en tehlikeli ürünler listesinde ilk\\n                3 sıraya yine Türkiyede yetişen tarım ürünlerini koydu.\\n\\n                Türk tarım ürünleri bir kez daha ağır darbe yedi. Bugüne kadar başta Rusya olmak üzere Ukrayna, Almanya,\\n                Hollanda gibi ülkelerden Yolladığınız tarım ürünlerinde insan sağlığına zararlı kalı...",
                "guid": "http://www.posta.com.tr/ekonomi/HaberDetay/Biber__armut_ve_uzumde_zehir_uyarisi.htm?ArticleID=114890",
                "link": "http://www.posta.com.tr/ekonomi/HaberDetay/Biber__armut_ve_uzumde_zehir_uyarisi.htm?ArticleID=114890",
                "pub_date": "Date(2012-03-27T06:54:00)",
                "title": "Biber, armut ve üzümde zehir uyarısı"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970864.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Boston Celtics, deplasmanda Charlotte Bobcats'i 102-95\\n                yenerek 49. maçında 27. galibiyetini aldı<p> </p>\\n                Celticsde Paul Pierce 36 sayı, 10 ribauntla \\"double-double\\" yaptı. Pierce, 36 sayıyla bu sezonki\\n                rekorunu kırdı. Boston ekibinde Kevin Garnett 24 sayı, 4 ribauntla, Brandon Bass, 15 sayı, 5 ribauntla\\n                oynadı. Rajon Rondo da 7 sayı, 13 asistle galibiyete katkıda bulundu.\\n\\n                Bobcatsde ise en skorer isim 21 sayı atan Gerald Henderson oldu. NBAde bu sezon şu ana kadar 10dan az\\n                galibiyet elde eden tek takım olan Bobcats, böylece 47. maçındaki 40. mağlubiyetini aldı.\\n\\n                HİDAYET İDARE ETTİ\\n\\n                Orlando Magicde forma giyen Hidayet Türkoğlu, takımının deplasmanda Toronto Raptorsu 117-101 ye...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Boston_da_Pierce_in_gecesi__102-95.htm?ArticleID=114891",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Boston_da_Pierce_in_gecesi__102-95.htm?ArticleID=114891",
                "pub_date": "Date(2012-03-27T06:53:00)",
                "title": "Boston'da Pierce'ın gecesi: 102-95"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970857.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Miss Turkey 2007 birincisi Selen Soyder, bir süredir,\\n                başrolünde oynadığı “Yer Gök Aşk” dizisinin eski yönetmeni Ulaş İnaç'la birlikte<p> </p>\\n                Soyderin Lale Devri dizisine transfer olup Ürgüpten İstanbula dönmesi, İnaçın da diziyi bırakmasıyla\\n                aşıklar sonunda rahat bir nefes aldı.\\n\\n                Artık rahat rahat görüşen sevgililer, geçtiğimiz gün Lale Devri için düzenlenen davetteydi. İkilinin\\n                romantizm dolu anları, objektiflere böyle yansıdı...",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Yer_gok_onlar_icin_ask.htm?ArticleID=114889",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Yer_gok_onlar_icin_ask.htm?ArticleID=114889",
                "pub_date": "Date(2012-03-27T06:53:00)",
                "title": "Yer gök onlar için aşk"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970889.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Güney Koreliler, komünist Kuzey Kore'de yaşayanlar için\\n                hazırladıkları kışlık çorap dolu kolileri balonlara bağlayarak gönderdi<p> </p>\\n                Kuzey Kore'den kaçarak Güney Kore'ye sığınanların oluşturduğu topluluk, iki ülke arasındaki askerden\\n                arındırılmış bölgede yardım kolilerini hazırladılar. Sıcak hava balonlarına sıkıca bağlanan koliler\\n                rüzgarın da yardımıyla sınırın karşı tarafına gönderildi.\\n\\n                Organizasyonun lideri Lee Ju Sung, Kuzey Kore'de kışlık çorapların bu aylarda en önemli giyecek olduğunu\\n                belirtti.",
                "guid": "http://www.posta.com.tr/dunya/HaberDetay/Kuzey_in_coraplari_Guney_den.htm?ArticleID=114893",
                "link": "http://www.posta.com.tr/dunya/HaberDetay/Kuzey_in_coraplari_Guney_den.htm?ArticleID=114893",
                "pub_date": "Date(2012-03-27T06:50:00)",
                "title": "Kuzey'in çorapları Güney'den"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970843.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Demi Moore'dan ayrılan Ashton Kutcher'ın kızları görünce\\n                “gözü döndü”<p> </p>\\n\\n\\n                Kısa sürede adı birçok kadınla anılan, en son Rihannayla birlikte olduğu iddia edilen seksi oyuncu\\n                Lakers maçında gözünü ponpon kızlardan alamadı!\\n\\n                Kutcher, maçtan çok kızlarla ilgilenince basın mensuplarının dikkatini üzerine çekmekten kurtulamadı.",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Kizlari_gorunce_gozu_dondu_.htm?ArticleID=114887",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Kizlari_gorunce_gozu_dondu_.htm?ArticleID=114887",
                "pub_date": "Date(2012-03-27T06:49:00)",
                "title": "Kızları görünce gözü döndü!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970836.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Elektrikte zam baskısı arttı. Nisan'da yüzde 7 ila 10\\n                arasında zamlı fatura ile karşı karşıya kalabilirsiniz<p> </p>\\n                Nisan ayında uygulamaya girecek yeni elektrik tarifeleri için kurumlar son çalışmalarını yaparken\\n                yetkililer yüzde 7 ila 10 arasında zam baskısı olduğunu belirtti. 1 Nisanda uygulamaya girecek yeni\\n                elektrik tarifelerinin belirlenmesi için ilgili kurumlar bu hafta son düzenlemelerini yapacak.\\n\\n                Hürriyet'in haberine göre yetkililer, yüzde 7 ila 10 arası zam baskısı doğduğunu belirtirken, Enerji\\n                Piyasası Düzenleme Kurumunda (EPDK) yarın yapılacak kurul toplantısında yeni tarifeler karara\\n                bağlanacak.\\n\\n                Elektrik, doğalgaz ve kömür KİTleri, uygulayacakları yeni tarifelerini döviz kuru, p...",
                "guid": "http://www.posta.com.tr/ekonomi/HaberDetay/Elektrik_faturaniz_Nisan_da_kabarabilir.htm?ArticleID=114886",
                "link": "http://www.posta.com.tr/ekonomi/HaberDetay/Elektrik_faturaniz_Nisan_da_kabarabilir.htm?ArticleID=114886",
                "pub_date": "Date(2012-03-27T06:47:00)",
                "title": "Elektrik faturanız Nisan'da kabarabilir"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970828.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Jüri üyesi ve sunucu Simon Cowell'in 11 milyon sterlinlik\\n                (31.3 milyon TL) evine bir kadın hayranı girdi<p> </p>\\n\\n\\n                \\"Yetenek Sizsiniz\\" ve \\"Pop Star\\" gibi yarışmaların yaratıcısı olan İngiliz yapımcı, jüri üyesi ve sunucu\\n                Simon Cowellin İngilterenin başkenti Londradaki 11 milyon sterlinlik (31.3 milyon TL) evine bir kadın\\n                hayranı girdi.\\n\\n                Cowellin yatağına yatan kadın, hizmetçinin ihbarı üzerine gözaltına alındı. Polisin evden yaka paça\\n                götürdüğü kadının psikolojik tedavi gördüğü açıklandı.\\n\\n                Cowellin olay sırasında evde olup olmadığı, kadınla karşılaşıp karşılaşmadığı bilinmiyor. Cowell, 200\\n                milyon sterlinlik (570 milyon TL) bir servete sahip.",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Hayrani_gizlice_yatagina_girdi_.htm?ArticleID=114885",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Hayrani_gizlice_yatagina_girdi_.htm?ArticleID=114885",
                "pub_date": "Date(2012-03-27T06:44:00)",
                "title": "Hayranı gizlice yatağına girdi!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970821.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />1 polisin şehit olmasına, 8'i polis 12 kişinin de\\n                yaralanmasına neden oldukları iddia edilen 1'i tutuklu 10 çocuk, bomba patladıktan sonra sevinç\\n                çığlıkları atmış<p> </p>\\n                Adana'da 16 Ekim 2011 tarihre, terör örgütü PKK yandaşlarının korsan gösterisinde, çöpe konulan bombanın\\n                patlatılması sonucu 1 polis memurunun şehit olmasına, 8i polis memuru 12 kişinin yaralanmasına neden\\n                oldukları iddia edilen 1i tutuklu 10 çocuğun yargılanmasına başlandı.\\n\\n                Sanık çocukların suçlamayı kabul etmediği duruşmada ;olaydan yaralı kurtulan polis memurlarından Ü.C.K.,\\n                eylemcilerin bombanın patlamasının ardından sevinç çığlığı attığını söyledi.\\n\\n                Merkez Seyhan İlçesi Gülbahçesi Mahallesi Obalar Caddesinde 16 Ekim 2011de meydana gelen olayda, terör\\n                örgütü PKK yandaşları...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/_Bomba_patlayinca_sevinc_cigliklari_attilar_.htm?ArticleID=114884",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/_Bomba_patlayinca_sevinc_cigliklari_attilar_.htm?ArticleID=114884",
                "pub_date": "Date(2012-03-27T06:43:00)",
                "title": "'Bomba patlayınca sevinç çığlıkları attılar'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970814.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" /><p> </p>\\n                İstanbul serbest piyasada dolar 1,7860, avro 2,3850 liradan güne başladı.\\n\\n                Kapalıçarşıda 1,7840 liradan alınan dolar 1,7860 liradan satılıyor. 2,3830 liradan alınan avronun satış\\n                fiyatı ise 2,3850 lira olarak belirlendi.\\n\\n                Önceki kapanışta doların satış fiyatı 1,7890 lira, avronun satış fiyatı ise 2,3820 lira olmuştu.\\n\\n                Bankalararası piyasada satışta dolar kotasyonları en düşük 1,7865 lira, en yüksek 1,7905 lira\\n                seviyesinde bulunuyor.\\n                Dolar kotasyonları saat 09.10 itibariyle alışta en düşük 1,7820 lira, en yüksek 1,7845 lira, satışta en\\n                düşük 1,7865 lira, en yüksek 1,7905 lira sev...",
                "guid": "http://www.posta.com.tr/ekonomi/HaberDetay/Dolar_dususte.htm?ArticleID=114883",
                "link": "http://www.posta.com.tr/ekonomi/HaberDetay/Dolar_dususte.htm?ArticleID=114883",
                "pub_date": "Date(2012-03-27T06:42:00)",
                "title": "Dolar düşüşte"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970806.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Sosyetik ikoncan Ivana Sert önceki gün Twitter'da günün\\n                konusuydu<p> </p>\\n                Twitter kullanıcıları, eşi Yurdal Sertle boşanma davası süren Sırp asıllı Sertin Bugün Ne Giysem?\\n                yarışmasında elenen yarışmacılara söylediği Bizimla değilsin! sözünü hashtag yaptı.\\n\\n                Gün boyu sanal âlemde sevmedikleri kişilere, Bizimla değilsin! diyen kullanıcılar, bu sözü Twitterda\\n                trending topic yaptı.",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Bizimla_degilsin_Ivana_.htm?ArticleID=114881",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Bizimla_degilsin_Ivana_.htm?ArticleID=114881",
                "pub_date": "Date(2012-03-27T06:38:00)",
                "title": "Bizimla değilsin Ivana!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970850.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Kayseri'de 15 yaşındaki Y.A, berberde tıraş olmak için evden\\n                çıktığında 15 yaşındaki M.Y. tarafından bıçaklandı<p> </p>\\n                Kocasinan ilçesi Boztepe Mahallesi Şehit Albay Mehmet Şahin Caddesinde meydana gelen olayda, laf atma\\n                konusunda çıkan tartışmada bir lokantada garson çalışan M.Y. ile fırıncı Y.A, kavga etti.\\n\\n                Mesai bitiminde evinden berbere tıraş olmak için ayrılan Y.A, arkasından gelen M.Y, yanındaki bıçağı\\n                Yusufun sağ baldırına saplayarak kaçtı.\\n\\n                Olay yerine gelen 112 ambulansı ile Yusuf Akçiçek Eğitim ve Araştırma Hastanesine götürüldü. M.Y,\\n                gözaltına alınırken, olayla ilgili soruşturma başlatıldı.\\n\\n                Kayseri/DHA",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Berbere_giderken_bicaklandi.htm?ArticleID=114888",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Berbere_giderken_bicaklandi.htm?ArticleID=114888",
                "pub_date": "Date(2012-03-27T06:36:00)",
                "title": "Berbere giderken bıçaklandı"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970799.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Burak Özçivit ile sevgilisi Ceylan Çapa'nın geçtiğimiz\\n                günlerde bir bar çıkışı otomobil içinde yaşadıkları kavganın nedeni ortaya çıktı<p> </p>\\n                Malkoçoğlu Burak Özçivitin, giydiği mini etek yüzünden sevgilisini kıskandığı, bu yüzden de ikilinin\\n                tartıştıkları öğrenildi.\\n\\n                Ceylan Çapanın geçen ay İstanbul Fashion Weekte giydiği etek de tartışma konusu olmuş, çıkan söylentiler\\n                üzerine Çapa, Burak etek giymeme kızmaz, öyle bir şey yok. Kızsaydı giyemezdim diye açıklama yapmıştı.",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Malkocoglu_nun_super_mini_krizi_.htm?ArticleID=114880",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Malkocoglu_nun_super_mini_krizi_.htm?ArticleID=114880",
                "pub_date": "Date(2012-03-27T06:32:00)",
                "title": "Malkoçoğlu'nun süper mini krizi!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970790.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Madonna hayranları isyan bayrağını çekti! Madonna Türkiye'den\\n                basın mensuplarına bir açıklama yapıldı<p> </p>\\n                Açıklamada şunlar kaydedildi:\\n\\n                \\"Madonna'nın yeni albümü MDNA'nın 26 Mart Pazartesi günü tüm dünya ile aynı anda ülkemizde yayınlacağı\\n                aylar öncesinden duyuruldu. Bugün ünlü mağazaları aradık. Hepsi albümün gelmediğini, dağıtımın olmadığı\\n                dile getirdi. Biz de bu albümü dağıtacak olan firmayı aradık, albümün dağıtımını bugün yapacaklarını\\n                dile getirdiler. Albüm şu an dünyanın her ülkesinde satılıyor. İnsanlar albümleri alıyor\\"\\n\\n                Hayranlar, \\"Madonna yeni turnesinin Avrupa açılışı ilk bizim ülkede yapılacak\\" derken şöyle devam\\n                ettiler: \\"Buna rağmen albümler ortalıkta yok. Albümün ilk biz...",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Madonna_hayranlari_isyanda_.htm?ArticleID=114879",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Madonna_hayranlari_isyanda_.htm?ArticleID=114879",
                "pub_date": "Date(2012-03-27T06:27:00)",
                "title": "Madonna hayranları isyanda!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970776.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Akıllı telefon ve tabletlerin popüler oyunlarından biri olan\\n                Angry Birds'ün yeni sürümü, 3 gün içinde 10 milyon kez indirildi<p> </p>\\n                Cadılar Bayramı, Yılbaşı ve Sevgililer Günü gibi özel günlerde yeni sürümleri çıkan Angry Birds'ün bir\\n                süredir beklenen Space sürümü, diğer oyunların aksine uzayda geçiyor ve uzay fiziği aynen oyunda\\n                uygulanıyor. 3 gün içinde 10 milyon kez indirilen uygulama, App Store'da da en çok indirilen uygulamalar\\n                listesinde zirveye oturdu.\\n\\n                Uygulama, şu an iPhone ve iPad'lerde bulunan iOS ve Android işletim sistemleri altında çalışabiliyor ve\\n                yakında BlackBerry cihazlara da gelecek.\\n\\n                Hürriyet",
                "guid": "http://www.posta.com.tr/yasam/HaberDetay/3_gunde_10_milyon_kez_indirildi.htm?ArticleID=114878",
                "link": "http://www.posta.com.tr/yasam/HaberDetay/3_gunde_10_milyon_kez_indirildi.htm?ArticleID=114878",
                "pub_date": "Date(2012-03-27T06:26:00)",
                "title": "3 günde 10 milyon kez indirildi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970783.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />İDO, Gebze Eskihisar ile Yalova Topçular hattında araçlarıyla\\n                seyahat eden yolcular için yeni bir uygulama başlattı<p> </p>\\n                İstanbul Deniz Otobüsleri İşletmesinin (İDO) Gebze Eskihisar ile Yalova Topçular hattında araçlarıyla\\n                seyahat eden yolcular, yeni uygulama ile 20 TL fiyat farkı ödeyerek ayrı şeritten beklemeden vapura\\n                geçebilecek\\n\\n                İDOdan yapılan açıklamada, özellikle hafta tatili başlangıcı ve sonu ile bayram ve benzeri uzun süreli\\n                tatillerde kilometrelerce kuyrukların uzadığı Eskihisar- Topçular feribot iskelelerinde bundan böyle\\n                esktra para ödeyenler sıra beklemeyecek.\\n\\n                'Öncelikli geçiş sistemi olarak tanıtılan bu sistem bugünden itibaren uygulamaya konulurken, gerekçe\\n                olarak da Özellikle gid...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/20_lira_verene_kuyruk_yok_.htm?ArticleID=114877",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/20_lira_verene_kuyruk_yok_.htm?ArticleID=114877",
                "pub_date": "Date(2012-03-27T06:26:00)",
                "title": "20 lira verene kuyruk yok!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970768.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Çin'de bir şirket, kuruluşunun 40'ıncı yıldönümü anısına, 3\\n                bin köylüye altın ve gümüş külçeleri dağıttı<p> </p>\\n                Çin basınında yer alan haberlere göre, ülkenin doğusunda faaliyet gösteren Ciangsu Şinçangciang isimli\\n                kolektif şirket, kuruluşunun 40ıncı yıldönümünü bir armağanla unutulmaz hale getirmek istedi.\\n                 \\n                Aynı zamanda şirketin hissedarları olan Çangciang köylüleri, hediye seçimlerini altın ve gümüş\\n                külçelerden yana kullandı.\\n                 \\n                Külçeler köye gelmeden önce, köylülere bir kasa ve altınların yolda olduğunu ima eden bir mesaj\\n                gönderildi.\\n                 \\n                Birkaç gün sonra 3 bin Çangciang sakini 100er gramlık külçelerine kavuştu.\\n                 \\n                China Daily gazetesi, köylülere daha önce de benzer şekilde altın ve ...",
                "guid": "http://www.posta.com.tr/yasam/HaberDetay/Cin_de_3_bin_kisiye_hediye_kulce_altin.htm?ArticleID=114876",
                "link": "http://www.posta.com.tr/yasam/HaberDetay/Cin_de_3_bin_kisiye_hediye_kulce_altin.htm?ArticleID=114876",
                "pub_date": "Date(2012-03-27T06:11:00)",
                "title": "Çin'de 3 bin kişiye hediye külçe altın"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970761.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Fransa Ligue 1 ekiplerinden PSG'de forma giyen Diego Lugano,\\n                futbol kariyerine nokta koymak istediği takımı açıkladı<p> </p>\\n                Fenerbahçe'den PSG'ye transfer olan, ancak Fransız kulübündeki performansıyla yoğun eleştiri alan Diego\\n                Lugano, geleceğiyle ilgili açıklamalarda bulundu.\\n\\n                Uruguaylı futbolcu, 2012 Londra Olimpiyatları'nda milli takım formasını giymeyi çok istediğini\\n                belirtirken, PSG'den ayrılması halinde futbol hayatını noktalayacağı takımın adını açıkladı.\\n\\n                Lugano, \\"Ben er ya da geç kariyerimin başladığı Sao Paulo'ya dönmek istiyorum. Türkiye'de de beni çok\\n                seviyorlar ve geri dönmemi istiyorlar. Ancak PSG'den ayrılmam halinde gideceğim kulüp Sao Paulo olacak\\"\\n                dedi.\\n\\n                2003-06 yılları arasında Bre...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Lugano_ayrilirsa_nereye_gidecek_.htm?ArticleID=114875",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Lugano_ayrilirsa_nereye_gidecek_.htm?ArticleID=114875",
                "pub_date": "Date(2012-03-27T06:10:00)",
                "title": "Lugano ayrılırsa nereye gidecek?"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970753.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Inter'de başkan Massimo Moratti, teknik direktör Claudio\\n                Ranieri'nin işine son verdi<p> </p>\\n                İtalyan futbolunun son birkaç yılında aldığı başarılarla adından söz ettiren FC Inter, şimdilerde eski\\n                günlerini arar durumda. 2011-2012 sezonuna kötü bir giriş yapan ve bir türlü aradığı istikrarı bulamayan\\n                FC Inter, geçen eylül ayının sonlarında takımı emanet ettiği Claudio Ranieri ile yolları ayırdı.\\n\\n                Ranierinin işine son verilme kararını bizzat kulüp başkanı Massimo Morattinin aldığı ve çalışmalarından\\n                dolayı tecrübeli teknik adam ve yardımcılarına teşekkür ettiği belirtildi.\\n\\n                Ranieriden boşalan teknik direktörlük koltuğuna ise mavi-siyahlıların genç takımını çalıştıran Andre...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Ranieri_nin_omru_kisa_oldu.htm?ArticleID=114874",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Ranieri_nin_omru_kisa_oldu.htm?ArticleID=114874",
                "pub_date": "Date(2012-03-27T06:05:00)",
                "title": "Ranieri'nin ömrü kısa oldu"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970745.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Galatasaray teknik direktörü Fatih Terim; Milan Baros, Sercan\\n                Yıldırım ve Mehmet Batdal'ı gönderme kararı aldı<p> </p>\\n                Elmandersiz çıktığı Türkiye Kupasındaki Sivasspor maçında şok bir şekilde elenen, önceki akşam da\\n                Trabzonspora ligde takılan Galatasarayda gol yollarındaki çaresizlik radikal kararların alınmasını\\n                gündeme getirdi.\\n\\n                Teknik Direktör Fatih Terimin basın toplantısında, Büyük takımlarda, bu tren ara istasyonlarda durmaz,\\n                ana istasyonlarda durur. Atladınız bu trene atladınız, atlamadınız kaçırırsınız. Herkes için geçerli bu\\n                diyerek yüklendiği forvet hattında yeni sezonla ilgili önemli değişikliğe gideceği öğrenildi.\\n\\n                Sezon başında bütün kaygılara rağmen takımda tutulan ancak yine h...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Terim_3_golcunun_biletini_kesti.htm?ArticleID=114873",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Terim_3_golcunun_biletini_kesti.htm?ArticleID=114873",
                "pub_date": "Date(2012-03-27T05:58:00)",
                "title": "Terim 3 golcünün biletini kesti"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970719.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Arap ülkeleri vatandaşlarının yerel kıyafetlerini giyerek\\n                kendilerine turist süsü vermeye çalışan iki kadın Türk yolcunun 6 valizinde yapılan aramada, ülkeye\\n                kaçak yolla sokulmak istenilen 1800 adet d<p> </p>\\n                Bir Arap ülkesine ait havayolu şirketinin tarifeli uçağıyla Dubaiden İstanbula gelen G.Y ve F.K adlı iki\\n                kadın yolcu, şüpheli hareketleri ile Araştırma Büro Amirliği Ekiplerinin dikkatini çekti.\\n\\n                Polislerin İki kadın yolcunun da Arap ülkeleri vatandaşlarının yerel kıyafetlerini giyerek turist süsü\\n                vermeye çalıştığını ve bu iki kişinin Türk olduğunu tespit etmesi üzerine yolcular durdurularak aramadan\\n                geçirildi.\\n\\n                İki kadın yolcunun bagajlarında yapılan aramada iPhone marka telefonların da aralarında olduğu 1800 adet\\n                cep telefonu ve 300 batarya ile 14 adet fotoğraf makinesi ele ge...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Valizde_1800_telefon_.htm?ArticleID=114871",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Valizde_1800_telefon_.htm?ArticleID=114871",
                "pub_date": "Date(2012-03-27T05:40:00)",
                "title": "Valizde 1800 telefon!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970710.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Cezayir'de bir baba, Gümüş ve Aşkı Memnu dizileriyle Arap\\n                kadınlarının gönlünde taht kuran Kıvanç Tatlıtuğ'un fotoğraflarını cep telefonuna kaydeden 16 yaşındaki\\n                kızını boğazını keserek öldürdü<p> </p>\\n                Önce Gümüş dizisi, ardından Aşkı Memnu ile Arap kadınlarını büyüledi. Fotoğraflarının bulunduğu\\n                kartpostallar yok sattı. Katıldığı festivallere Arap kadınları sadece onu görebilmek için akın etti.\\n                Arap ülkelerinde reyting rekoru kıran Nur (Gümüş) dizisi Gazzeden Riyada kadar birçok ülkede aylarca\\n                büyük ilgiyle izlendi ve reyting rekorları kırdı.\\n\\n                Dizide Mohannad karakterini oynayan Kıvanç Tatlıtuğ Arap kadınları için ideal erkek karakteri olunca\\n                Arap erkekleri bu durumdan her geçen gün daha da şikayetçi olmaya başladı.\\n\\n                'BİR GECE BİRLİKTE OLSAM...'\\n\\n                Cezayirde bir adam, sa...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Cebinde_Kivanc_i_gordu__kizini_kesti.htm?ArticleID=114870",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Cebinde_Kivanc_i_gordu__kizini_kesti.htm?ArticleID=114870",
                "pub_date": "Date(2012-03-27T05:14:00)",
                "title": "Cebinde Kıvanç'ı gördü, kızını kesti"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970702.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />İstanbul'da kaçak olarak çalışan Ermeni kadını çıplak\\n                fotoğraflı şantajla intihara sürüklediği iddia edilen gençler tutuklandı<p> </p>\\n                Kaçak olarak İstanbula gelip çalışan Ermenistan vatandaşı Narine Mkrtchyana (24) çıplak fotoğrafıyla\\n                şantaj yaptıkları için siyanür içerek intihar etmesine neden oldukları ileri sürülen erkek arkadaşı\\n                Orhan Okumuş (24) ile ağabeyi Barış Okumuş yakalandı ve şantaj ve özel hayatın gizliliğini ihlal\\n                suçlarından tutuklandı.\\n\\n                Ermenistandan iş bulma amacıyla 4 yıl önce Türkiyeye göç eden Narine, gümüş imalathanesinde çalışmaya\\n                başladı.\\n\\n                Kaçak yaşadıkları İstanbul Kumkapıdaki evlerinde üvey babası ve ağabeyiyle kalan Narine, aynı mahallede\\n                oturan Orhana âşık oldu. İddiaya göre Orh...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Intihar_ettiren_ciplak_santaj_.htm?ArticleID=114869",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Intihar_ettiren_ciplak_santaj_.htm?ArticleID=114869",
                "pub_date": "Date(2012-03-27T05:04:00)",
                "title": "İntihar ettiren çıplak şantaj!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970694.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />CHP'nin bugün Tandoğan'da yapacağı miting nedeniyle bazı\\n                yolların trafiğe kapatılacağı bildirildi<p> </p>\\n                Ankara Emniyet Müdürlüğü'nden yapılan açıklamada, bugün 11.30 - 15.30 saatleri arasında CHP tarafından\\n                TBMM gündeminde olan 4+4+4 Eğitim Düzenlemesi adı altında bir açık hava toplantısı düzenleneceği\\n                belirtildi.\\n\\n                >> CHP NEDEN MEYDANA İNİYOR?\\n\\n                Açıklamada, miting nedeniyle, 'Kazım Karabekir Caddesi Ulaştırma Kavşağı'ndan Tandoğan Meydanı'na kadar,\\n                Ulaştırma Kavşağı Tandoğan istikametine dönüş varyantları, Celal Bayar Bulvarı Kazım Karabekir\\n                Caddesi'ne giriş varyantları, Beşevler Kavşağı Dögol Caddesi girişi, Anıt Caddesi ile Tandoğan Meydanı,\\n                GMK Bulvarı Ankaray Maltepe durağı arası ...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/Ankara_da_trafige_miting_ayari.htm?ArticleID=114868",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/Ankara_da_trafige_miting_ayari.htm?ArticleID=114868",
                "pub_date": "Date(2012-03-27T04:50:00)",
                "title": "Ankara'da trafiğe miting ayarı"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970686.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Ankara Emniyeti'nin internet sitesini çökerten 'Redhack'\\n                grubu, 'Yanlış kişileri tutukladınız' diyerek yeni eylem yaptı<p> </p>\\n                Ankara Emniyet Müdürlüğünün internet sitesini çökerten Redhack (Kızıl Hackerlar) adlı korsanlara yönelik\\n                operasyonda tutuklanan 7 kişinin, olayla ilgilerinin bulunmadığı ileri sürüldü. Redhack gurubu\\n                Tutuklananlar bizden değil dedi ve bunu ispat için, polis çocuklarının kaldığı Emniyet yurtlarının\\n                sitesini hackledi. \\n\\n                Polis, Ankara Emniyet Müdürlüğü'ne yapılan sanal saldırı sonrası gerçekleştirdiği operasyonda, 16 kişiyi\\n                gözaltına almış ve bunlardan 7si tutuklanmıştı. Ancak gözaltına alınanların kendi üyeleri olmadığını\\n                duyuran Redhack bunu ispat için yeni bir eylem ya...",
                "guid": "http://www.posta.com.tr/yasam/HaberDetay/Redhack__cee__yapti_.htm?ArticleID=114867",
                "link": "http://www.posta.com.tr/yasam/HaberDetay/Redhack__cee__yapti_.htm?ArticleID=114867",
                "pub_date": "Date(2012-03-27T04:39:00)",
                "title": "Redhack 'cee' yaptı!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970678.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />İngiltere'de Müslümanlara yönelik hazırlanan \\"evlilik\\n                rehberi\\" kitabında erkeklere karılarını dövebilecekleri öğütlenmesi ülkede şok etkisi yaptı.<p>\\n                </p>\\n                160 sayfadan oluşan A Gift For Muslim Couple (Müslüman Çiftlere Bir Hediye) adlı kitapta erkeklere\\n                karılarını \\"sopayla ya da elle dövebilecekleri, kulaklarından çekebilecekleri\\" tavsiyesinde bulunuyor. \\n\\n                İzin almadan kadınların evden dışarı çıkmaması gerektiğini yazan kitap kadınların erkekleri için\\n                süslenip onların arzularını tatmin etmeleri gerektiğine işaret ediyor.\\n\\n                İngiltere'de kitapçılarda ve internet sitelerinde satışta olan kitap hakkında ılımlı Müslüman\\n                akademisyen Tarek Fatah'ın dava açacağını söyledi. Fatah bu tavsiyelerin kabul edilemez olduğunu\\n                belirtti.\\n\\n                GAZETEP...",
                "guid": "http://www.posta.com.tr/dunya/HaberDetay/Evlilik_rehberinde_sok_tavsiyeler_.htm?ArticleID=114866",
                "link": "http://www.posta.com.tr/dunya/HaberDetay/Evlilik_rehberinde_sok_tavsiyeler_.htm?ArticleID=114866",
                "pub_date": "Date(2012-03-27T04:31:00)",
                "title": "Evlilik rehberinde şok tavsiyeler!"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970664.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Kanada'daki güzellik yarışmasında birinci olan Jenna\\n                Talackova erkek olduğu ortaya çıkınca yarışmadan diskalifiye edildi<p> </p>\\n                Ülkesini Dünya Kainat Güzellik Yarışmasında temsil etmek için onlarca finalist arasından seçilen Kanada\\n                güzeli Jenna Talackova erkek olduğu anlaşılınca yarışmadan diskalifiye edildi.\\n\\n                Kanada Kainat Güzeli Yarışmasının ulusal direktörü Denis Davila 23 yaşındaki Talackovanın doğuştan kadın\\n                olduğunu sandıklarını söyledi. Davila sözlerine şöyle devam etti: Kurallar gereği yarışmaya katılan\\n                herkesin doğuştan kadın olması gerekiyor.\\n\\n                19 yaşında cinsiyetini değiştiren Talackova sonradan kadın olduğunu açıkladığı gün yarışmadan\\n                diskalifiye oldu. Talackova bir avukata başvurduğunu ve h...",
                "guid": "http://www.posta.com.tr/yasam/HaberDetay/Kanada_guzeli__erkek__cikti_.htm?ArticleID=114865",
                "link": "http://www.posta.com.tr/yasam/HaberDetay/Kanada_guzeli__erkek__cikti_.htm?ArticleID=114865",
                "pub_date": "Date(2012-03-27T04:22:00)",
                "title": "Kanada güzeli 'erkek' çıktı!"
            },
            {
                "content": "<p> </p>\\n                O değil de benim bildiğim Ünlüler Gönüllüler Survivor (Show TV) takımının Hasanı en son Camoka ismiyle\\n                Amerikan güreşi ve boks ringlerinde fırtına gibi esiyordu... Şimdi Survivor adasında, üstelik\\n                dayanıklılık yarışmasında Nihat Alptuğ Altınkayaya yenilmiş olması işkillendirdi beni. Bildiğim\\n                kadarıyla hayatı idmanlarda geçen bir sporcu ve dansçı olan Hasanın öyle kolay pes etmeyecek bir\\n                performansı olmalıydı. Artık moral mi desek, konsantrasyon eksikliği mi, bilemiyorum... Mustafa\\n                Topaloğlunun 80 kiloluk ağırlığın altında kılının kıpırdamadığını düşünürsek, bu ünlüler takımının\\n                Hindis...",
                "guid": "http://www.posta.com.tr/magazin/YazarHaberDetay/Unlulere_ne_iciriyorlar_.htm?ArticleID=114864",
                "link": "http://www.posta.com.tr/magazin/YazarHaberDetay/Unlulere_ne_iciriyorlar_.htm?ArticleID=114864",
                "pub_date": "Date(2012-03-27T02:00:00)",
                "title": "Ünlülere ne içiriyorlar?"
            },
            {
                "content": "<p> </p>\\n                İnsanların yaşam öykülerinde ne fırtınalar gizli. Pyotr Smirnoff da kendi bulduğu yöntemle Rusların\\n                milli içkisi votkayı diğerlerinden daha berrak, kokusuz ve nötr bir biçimde üretince markasının yanına\\n                devlet armasını bile çizme hakkına erişmiş, hatta çar tarafından İmparatorluk tedarikçisi ilan edilmiş.\\n                Ancak Bolşevik İhtilali sırasında ne Çar kalmış, ne saray. Smirnoff da kendini zindanda bulmuş. Tam iki\\n                kere idam mangasının önüne oturtulmuş ama şans bu ya, her seferinde de ölümden dönmüş.\\n\\n                Sonuncusunda kurşuna dizilecekken Beyaz Ordunun baskınıyla kurtulmuş! Kaçmış Smirnoff. Ner...",
                "guid": "http://www.posta.com.tr/turkiye/YazarHaberDetay/Bay_Smirnoff_un_azimli_hikayesi.htm?ArticleID=114863",
                "link": "http://www.posta.com.tr/turkiye/YazarHaberDetay/Bay_Smirnoff_un_azimli_hikayesi.htm?ArticleID=114863",
                "pub_date": "Date(2012-03-27T02:00:00)",
                "title": "Bay Smirnoff'un azimli hikayesi"
            },
            {
                "content": "<p> </p>\\n                Bu yasa hakkında laik kesimin hiçbir bilgisi yok. Buna karşılık da giderek artan bir korkusu var.\\n                Üstelik korkusundan da emin olmamakla birlikte Kardeşim işte gizli gündemlerini devreye soktular. AK\\n                Partiden daha başka ne bekleyebilirsin ki? Baksana Başbakan dinci nesil yetiştireceğiz... diyor. Acaba?\\n                Acaba, iş bu kadar basit mi?\\n\\n                Acaba, AK Parti yasayla gerçekten dindarın da ötesinde, dinci bir nesil peşinde mi koşuyor? Bizim kesim\\n                için, okullarda din dersi verdirmek ileride din devletine geçişin ilk adımıdır. Hep bu şekilde görüldü.\\n                Verilen din dersi de hiçbir şeye benzemezdi. Sade...",
                "guid": "http://www.posta.com.tr/siyaset/YazarHaberDetay/3x4__laik_Cumhuriyetin_sonu_demek_degildir___.htm?ArticleID=114862",
                "link": "http://www.posta.com.tr/siyaset/YazarHaberDetay/3x4__laik_Cumhuriyetin_sonu_demek_degildir___.htm?ArticleID=114862",
                "pub_date": "Date(2012-03-27T02:00:00)",
                "title": "3x4, laik Cumhuriyetin sonu demek değildir..."
            },
            {
                "content": "<p> </p>\\n                İtiraf ediyorum: Yıllardır YÖKe haksızlık etmişim!\\n                Adamlar en azından sadece üniversitelere bulaşıyor...\\n                Oysa RTÜK öyle mi?\\n                * * *\\n                Nasıl mambo-çaça yapmamız gerektiğine...\\n                Sevgilimizle nasıl bir ilişki yaşayacağımıza...\\n                Sevdiklerimize doğum gününde ne hediye alacağımıza...\\n                Istakozu nasıl pişireceğimize...\\n                Kime aşık olacağımıza, aşıkken ne yapıp ne yapamayacağımıza...\\n                [[HAFTAYA]]\\n                Ne yiyeceğimize, ne içeceğimize...\\n                Nasıl Türkçe konuşacağımıza...\\n                Öpüşürken nelere dikkat etmemiz gerektiğine...\\n                Şarkı söylerken hangi hareketlerden kaçınacağımıza...\\n                RTÜK karar veriyor!\\n                ...",
                "guid": "http://www.posta.com.tr/turkiye/YazarHaberDetay/Kanal_tedavisi.htm?ArticleID=114861",
                "link": "http://www.posta.com.tr/turkiye/YazarHaberDetay/Kanal_tedavisi.htm?ArticleID=114861",
                "pub_date": "Date(2012-03-27T02:00:00)",
                "title": "Kanal tedavisi"
            },
            {
                "content": "<p> </p>\\n                1973 yılında annem ve babam bir cinayete kurban gitmişti. O zamanlar kardeşlerimle birlikte küçüktük.\\n                Babam bir daire satmış ve sattığı daire üzerinde bir ipotek varmış. Şimdi bu yeri alanlar bize başvurup\\n                ipotek bedelini ödememizi istiyor. O zamanki para değeri sonradan değiştiği ve liradan altı sıfır\\n                atıldığı için bugün bu paranın 25 kuruş olduğu söylendi. Bu parayı ödesek mi ödemesek mi? Yoksa\\n                karşımıza başka borç çıkar mı?  N.S.\\n\\n                Önce şuna karar vermek lazım. İpotek nedir? Babanız birine borçlanmış, borç veren de teminat olmak üzere\\n                rehin almış. Yani gayrimenkul teminatına ipotek d...",
                "guid": "http://www.posta.com.tr/ekonomi/uzman-gorusu/YazarHaberDetay/Borclu_degil_alacaklisiniz_ama___.htm?ArticleID=114860",
                "link": "http://www.posta.com.tr/ekonomi/uzman-gorusu/YazarHaberDetay/Borclu_degil_alacaklisiniz_ama___.htm?ArticleID=114860",
                "pub_date": "Date(2012-03-27T02:00:00)",
                "title": "Borçlu değil alacaklısınız ama..."
            },
            {
                "content": "<p> </p>\\n                Soru: 1 Şubat 1990dan beri Bağ-Kurluyum. 18 ay askerliğimi borçlansam, ne zaman emekli olabilirim? 10\\n                Temmuz 1966 doğumluyum.  Ali KOBAK Cevap: Askerlik yaptığınız tarihi bildirmemişsiniz. Ancak sorunuzdan\\n                askerliğinizi sigorta başlangıç tarihinden önce yaptığınızı anlıyoruz. Askerlik sürenizin tamamını\\n                borçlanmanıza gerek yok. 4 ayını borçlanmanız halinde, emekli olmak için 25 tam yıl prim ödeme ve 51 yaş\\n                şartlarına tabi olursunuz. 1 Ekim 2014 tarihine kadar ara vermeden prim ödeyerek, toplam priminizi 25\\n                tam yıla tamamlamanız şartıyla, 51 yaşınızı dolduracağınız 10 Temmuz 2017 tarihinde...",
                "guid": "http://www.posta.com.tr/ekonomi/YazarHaberDetay/4_ay_askerlik_borclanmasiyla_1_yil_erken_emekli_olabilirsiniz.htm?ArticleID=114859",
                "link": "http://www.posta.com.tr/ekonomi/YazarHaberDetay/4_ay_askerlik_borclanmasiyla_1_yil_erken_emekli_olabilirsiniz.htm?ArticleID=114859",
                "pub_date": "Date(2012-03-27T02:00:00)",
                "title": "4 ay askerlik borçlanmasıyla 1 yıl erken emekli olabilirsiniz"
            },
            {
                "content": "<p> </p>\\n                Türkiye Ekonomi Politikaları Araştırma Vakfı, uzun yıllardır tartıştığımız yabancı dil eğitimi konusunda\\n                İngilizce Yeterlilik Endeksinin araştırma sonuçlarını paylaştı. Buna göre İngilizcenin bilinirliliği\\n                açısından Türkiye, 44 ülke arasında Şili, Endonezya ve Suudi Arabistanın gerisinde 43üncü sırada yer\\n                alıyor. Devlet okullarındaki İngilizce öğretmeni açığımız ise 8 bin 500 civarında.\\n\\n                Tablo böyle iken Milli Eğitim Bakanlığı 4+4+4 sistemiyle birlikte İngilizce eğitiminde değişikliğe\\n                gittiğini açıkladı. Bakanlık yeni eğitim sistemi ile birlikte okullarda yabancı dil eğitimini de kad...",
                "guid": "http://www.posta.com.tr/turkiye/YazarHaberDetay/Yabanci_dil_dersi_icin_oneriler.htm?ArticleID=114858",
                "link": "http://www.posta.com.tr/turkiye/YazarHaberDetay/Yabanci_dil_dersi_icin_oneriler.htm?ArticleID=114858",
                "pub_date": "Date(2012-03-27T02:00:00)",
                "title": "Yabancı dil dersi için öneriler"
            },
            {
                "content": "<p> </p>\\n                Bir taraftan 12 Eylülü yargılayacağız ama bir taraftan da hâlâ 12 Eylül Anayasasıyla yaşamaya devam\\n                edeceğiz.\\n                Gülerler adama.\\n                Bir Uzlaşma Komisyonu kurmuşlar.\\n                Niçin? Uzlaşmamak için.\\n                2012yi Anayasa Yılı ilan etmişler.\\n                Saat kaç? 3 ay gitti, kaldı 9 ay.\\n                Eğitim Modelinde anlaşamayanlar, koskoca Anayasa Metninde nasıl anlaşacak? Her ihtilaflı madde için\\n                Tandoğan Meydanına gidilmez ki.\\n                * * *\\n                Gidildi diyelim. O zaman da 2007deki seri mitingleri çağrışım ettiren sahneler göreceğiz.\\n                [[HAFTAYA]]\\n                Hemen söyleyeyim: Hayra âlamet değildir. O tür mitinglerde abartılmış laiklik...",
                "guid": "http://www.posta.com.tr/turkiye/YazarHaberDetay/Olur_mu_olur.htm?ArticleID=114857",
                "link": "http://www.posta.com.tr/turkiye/YazarHaberDetay/Olur_mu_olur.htm?ArticleID=114857",
                "pub_date": "Date(2012-03-27T02:00:00)",
                "title": "Olur mu olur"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970655.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Çağdaş Gazeteciler Derneği tarafından 2011 Yılı Gazetecileri\\n                Ödül Töreni düzenlendi<p> </p>\\n                 Törene katılan CHP Genel Başkanı Kemal Kılıçdaroğlu, demokrasi konusunda sıkıntılar olduğunu ifade\\n                ederek, \\"Eğer demokrasi kanserse, o bir süre sonra kitle imha silahına dönüşür. Türkiyenin geldiği nokta\\n                bu. Demokrasi açısından çok ciddi açmazlarla karşı karşıyayız\\" dedi. Ödül töreninde Van depreminde göçük\\n                altında kalarak yaşamlarını yitiren gazeteciler Cem Emir ve Sabahattin Yılmaz anısına verilen\\n                Unutulmayacaklar Haber Ödülüne Doğan Haber Ajansı muhabirleri Ferit Demir ve Ferit Aslan değer görüldü.\\n                Doğan Haber Ajansı muhabiri Behçet Dalmaz ise Behzat Miser Haber Ödülüne layık görüld...",
                "guid": "http://www.posta.com.tr/siyaset/HaberDetay/_Demokrasi_kanserse_kitle_imha_silahina_donusur_.htm?ArticleID=114856",
                "link": "http://www.posta.com.tr/siyaset/HaberDetay/_Demokrasi_kanserse_kitle_imha_silahina_donusur_.htm?ArticleID=114856",
                "pub_date": "Date(2012-03-26T21:18:00)",
                "title": "'Demokrasi kanserse kitle imha silahına dönüşür'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/27/3/2012/fft13mm970648.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Mardin'in Nusaybin İlçesi'ne bağlı Akarsu Beldesi İlkadım\\n                Köyü'nde çobanlık yapan İsmail Akın ile kızı Berfin Akın, öldürülmüş olarak bulundu<p> </p>\\n                Nusaybin İlçesine bağlı Akarsu Beldesi İlkadım Köyünde çobanlık yapan 62 yaşındaki İsmail Akın ile kızı\\n                11 yaşındaki Berfin Akın, sabah saatlerinde otlatmak üzere hayvanları tepelere götürdü. Baba ile kızı\\n                akşam saatlerinde dönmeyince, köylüler tarafından aranmaya başlandı. Uzun süren aramalardan sonra köye\\n                yakın bir tepede İsmail Akın, başı taşla ezilmiş bulunurken, kızı Berfin Akın da 20 metre uzaklıkta\\n                kafasına tabanca ile bir kez ateş edilmiş halde cesedi bulundu.\\n\\n                Olay karşısında şoke olan köylülerin ihbarı üzerine jandarma olay yerine geldi. Jandarma olay yeri\\n                inceleme ekibi yap...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Hayvan_otlatan_baba_ile_kizi_oldurulmus_bulundu.htm?ArticleID=114855",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Hayvan_otlatan_baba_ile_kizi_oldurulmus_bulundu.htm?ArticleID=114855",
                "pub_date": "Date(2012-03-26T21:14:00)",
                "title": "Hayvan otlatan baba ile kızı öldürülmüş bulundu"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970641.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Suriye'de , 2 ay önce muhalifler ile Esad'a bağlı askerler\\n                arasında çıkan çatışmada yaralanan ve bir türlü iyileşmeyen oğlunu sırtına alan Hüseyin El Muhammed,\\n                mayınlı bölgeden Türkiye'ye girmeye çalı<p> </p>\\n                Askerler tarafından farkedilen baba oğul, güvenli yerden sınırdan geçirildikten sonra yaralı Hasan El\\n                Hüseyin hastanede tedavi altına alındı.\\n\\n                Halepte 2 ay önce Muhalifler ile Esada bağlı askerler arasında çıkan çatışmada yaralanan ve ülkesinde\\n                tedavi edilen 20 yaşındaki Hasan El Hüseyin iyileşmeyince babası Hüseyin El Muhammed oğlunu Türkiyeye\\n                getirmeye karar verdi.\\n\\n                Hüseyin El Muhammed oğlu Hasan El Hüseyini sırtına alarak Suriyenin Tilşem Köyü yakınlarından Öncüpınar\\n                Hudut Bölük Komutanlığı sorumluluk alanındaki mayınlı bölgeden Türkiyeye giriş yapmaya çalıştı.\\n\\n                Görev...",
                "guid": "http://www.posta.com.tr/dunya/HaberDetay/Sirtinda_ogluyla_mayinli_bolgeden_gecmeye_calisti.htm?ArticleID=114854",
                "link": "http://www.posta.com.tr/dunya/HaberDetay/Sirtinda_ogluyla_mayinli_bolgeden_gecmeye_calisti.htm?ArticleID=114854",
                "pub_date": "Date(2012-03-26T20:03:00)",
                "title": "Sırtında oğluyla mayınlı bölgeden geçmeye çalıştı"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970617.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Spor Toto Süper Lig 32. hafta kapanış mücadelesinde Beşiktaş,\\n                1-0 geriye düştüğü maçta Manuel Fernandes'in müthiş oyunuyla 2-1 öne geçti ancak sahadan 2-2\\n                beraberlikle ayrıldı.<p> </p>\\n                6. dakikada İstanbul Büyükşehir Belediyespor öne geçti. Ev sahibi takımın soldan kullandığı taç\\n                ataşında, Webonun ceza sahasında göğsüyle indirdiği topu, Holmen ceza yayındaki Efeye aktardı. Bu\\n                futbolcunun sert şutunda, meşin yuvarlak yan kale direğinin içine çarparak, filelere gitti: 1-0.\\n\\n                11. dakikada Fernandesin soldan kullandığı korner atışında, ceza sahasında iyi yükselen Mustafanın kafa\\n                vuruşu istediği gibi olmayınca, top yandan auta gitti.\\n\\n                12. dakikada Holmenin ceza sahası dışından sert şutunu, kaleci Cenk güçlükle çıkardı. Pozisyonun\\n                devamında topu ceza sahasının sol ç...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Belediye_Kartal_a_gecit_vermedi.htm?ArticleID=114853",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Belediye_Kartal_a_gecit_vermedi.htm?ArticleID=114853",
                "pub_date": "Date(2012-03-26T19:19:00)",
                "title": "Belediye Kartal'a geçit vermedi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970610.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Alman otomotiv şirketi BMW, 2003'den 2010'a kadar üretilen 5\\n                ve 6 serisi 1,3 milyon aracı üretim hatası nedeniyle geri çağırıyor<p> </p>\\n                Şirketten yapılan açıklamada, bazı araçlarda bir akü kablosunun yanlış kurulduğu belirtilerek, bu\\n                hatanın aracın çalıştırılmasını engelleyebildiği ve çok nadir olarak yangına neden olabileceği\\n                kaydedildi.\\n\\n                Şirket, bu sorun nedeniyle herhangi bir kaza ve yaralanma bildirimi alınmadığını vurguladı.\\n\\n                Açıklamada, otomobil sahiplerinin bir mektupla bilgilendirileceği ve onarımın yaklaşık 30 dakika sürdüğü\\n                kaydedildi.\\n\\n                Almanya'da 290 bin, dünya çapında toplam 1,3 milyon otomobilin çağrıldığı belirtiliyor.\\n\\n                AA",
                "guid": "http://www.posta.com.tr/ekonomi/HaberDetay/BMW_1_3_milyon_otomobili_geri_cagiriyor.htm?ArticleID=114852",
                "link": "http://www.posta.com.tr/ekonomi/HaberDetay/BMW_1_3_milyon_otomobili_geri_cagiriyor.htm?ArticleID=114852",
                "pub_date": "Date(2012-03-26T18:54:00)",
                "title": "BMW 1,3 milyon otomobili geri çağırıyor"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970603.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Ataşehir'de bir tıp merkezinde görevli psikiyatri uzmanı\\n                doktor, iş çıkışı otomobiline bindiği sırada bir kişi tarafından bıçaklı saldırıya uğrayarak yaralandı<p>\\n                </p>\\n                Yakalanan saldırganın askerlik yaptığı dönemde, askeri hastanede çalışan doktor Uğur Yakın tarafından\\n                tedavi edildiği ve o dönemde aralarında yaşanan sorun nedeniyle saldırıyı gerçekleştirdiği belirlendi.\\n\\n                Örnek mahallesi 35. Cadde üzerinde bulunan Doruk Tıp Merkezinde çalışan psikiyatri uzmanı doktor Uğur\\n                Yakın, saat 17.30da işyerinden çıkıp otomobiline bindiği sırada,  otomobilin içine giren Barış Dur\\n                tarafından vücudunun çeşitli yerlerinden bıçaklanarak yaralandı. Saldırgan olaydan sonra çevreden\\n                yetişen vatandaşlar tarafından yakalanarak olay yerine çağırılan polis ekibine teslim ...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Askerde_komutani_olan_doktoru_bicakladi.htm?ArticleID=114851",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Askerde_komutani_olan_doktoru_bicakladi.htm?ArticleID=114851",
                "pub_date": "Date(2012-03-26T18:37:00)",
                "title": "Askerde komutanı olan doktoru bıçakladı"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970596.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Şişli Ayazağa'da ormanlık alanda çıkan yangında 5 hektar\\n                orman kül oldu<p> </p>\\n                Ayazağadaki ormanlık alanda henüz belirlenemeyen bir nedenle saat 15.30 sıralarında başlayan yangın,\\n                rüzgarın da etkisiyle hızla yayıldı. Yangın bölgesine kısa sürede çok sayıda itfaiye ekipleri ile iş\\n                makineleri sevk edildi.\\n\\n                Farklı noktalardan iş makineleri yol açarken, itfaiye ekipleri alevlere müdahale etti. Yangın, yaklaşık\\n                3 saatlik çalışmaların ardından kontrol altına alındı.\\n\\n                İstanbul Orman Bölge Müdürü İbrahim Çitfçi de yangın sonrası olay yerine gelerek inceleme yaptı. Çiftçi,\\n                \\"Yangın 5 hektar civarında gençleştirme sahasında örtü yangın şeklinde saat 15.35 sıralarında ç...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/5_hektar_orman_kul_oldu.htm?ArticleID=114850",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/5_hektar_orman_kul_oldu.htm?ArticleID=114850",
                "pub_date": "Date(2012-03-26T18:10:00)",
                "title": "5 hektar orman kül oldu"
            },
            {
                "content": "Diyarbakır'dan milletvekili seçilen ancak Yüksek Seçim Kurulu'nun (YSK) kararıyla vekilliği\\n                düşürülen Hatip Dicle'nin 'terör örgütü propagandası' yapmak suçlamasıyla yargılandığı davanın\\n                görülmesine d<p> </p>\\n                Halen KCK davasından tutuklu yargılandığı için cezaevinde bulunan Hatip Dicle duruşmada Kürtçe savunma\\n                yapmak isteyince, Mahkeme Başkanı, \\"Sizin ne kadar güzel Türkçe konuştuğunuzu biliyoruz\\" dedi.\\n\\n                12 Haziran 2011de yapılan Genel Seçim öncesi, Diyarbakırda seçmenlerine gönderdiği mektupta terör örgütü\\n                propagandası yaptığı gerekçesiyle hakkında 5 yıl hapis cezası istemiyle dava açılan Hatip Diclenin\\n                duruşmasına bugün devam edildi. Diyarbakır 7nci Ağır Ceza Mahkemesinde devam eden davanın bugünkü\\n                duruşmasına, halen KCKdan tutuklu bulunan Hatip Diclenin yanısıra, Diclenin gönder...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/_Ne_kadar_guzel_Turkce_konustugunuzu_biliyoruz_.htm?ArticleID=114849",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/_Ne_kadar_guzel_Turkce_konustugunuzu_biliyoruz_.htm?ArticleID=114849",
                "pub_date": "Date(2012-03-26T18:03:00)",
                "title": "'Ne kadar güzel Türkçe konuştuğunuzu biliyoruz'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970590.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />İstanbul'da 2012 yılındaki emlak satış ve kiralama\\n                oranlarının İngiltere'nin başkenti Londra'dan daha yüksek olduğu açıklandı<p> </p>\\n                İngilterenin önde gelen emlak yatırım şirketlerinden Colordarcynin yaptığı araştırmaya göre, Türkiyeden\\n                emlak satın almak Londraya göre çok daha avantajlı ve cazip.\\n\\n                Araştırmaya göre Londrada geçtiğimiz yıl içersinde emlak kiralama artışında bir yavaşlama görülürken\\n                İstanbulda ise Londraya göre hızlı bir artış var.\\n                Araştırma ayrıca İstanbulda kiralamanın daha pahalı olmasına karşın ev fiyatlarının Londranın yarısından\\n                bile az olduğunu vurguluyor.\\n\\n                İstanbuldaki emlak satışının bu yıl yüzde 15 dolayında yükselmesi beklenirken bu da 2011 yılında\\n                kaydedilen figürleri aşacağı...",
                "guid": "http://www.posta.com.tr/ekonomi/HaberDetay/Istanbul_dan_ev_satin_almak_Londra_dan_daha_cazip.htm?ArticleID=114848",
                "link": "http://www.posta.com.tr/ekonomi/HaberDetay/Istanbul_dan_ev_satin_almak_Londra_dan_daha_cazip.htm?ArticleID=114848",
                "pub_date": "Date(2012-03-26T17:59:00)",
                "title": "İstanbul'dan ev satın almak Londra'dan daha cazip"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970583.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Mardin'in Nusaybin İlçesi'nin karşısında bulunan Suriye'nin\\n                Derbessiye kentinde, kaçırılan 22 yaşındaki Civan Katna adlı Kürt genci ölü bulundu<p> </p>\\n                Katnanın cenazesi Derbessiye kentinde toprağa verilirken, cenaze töreni, Esat aleyhinde gösterilere\\n                dönüştü. Civan Katnanın 5 ay önce kaçırıldıktan sonra ölü bulunan Kürt lider Mişhel Temonun yeğeni\\n                olduğu belirtildi.\\n\\n                Suriyenin Derbessiye kentinde yaklaşık 1 hafta önce kimliği belirsiz kişiler tarafından kaçırılan Civan\\n                Katna, dün ölü bulundu. Derbessiye kentinde bugün düzenlenen cenaze törenine katılan binlerce kişi,\\n                ellerinde Suriye ve bölgesel Kürt yönetimi bayrakları taşıdı.\\n\\n                Katnanın evinin önünde düzenlenen törende saygı duruşu yapıldıktan sonra cenazesi omuzlarda, slog...",
                "guid": "http://www.posta.com.tr/dunya/HaberDetay/Suriye_de_kacirilan_genc_olu_bulundu.htm?ArticleID=114847",
                "link": "http://www.posta.com.tr/dunya/HaberDetay/Suriye_de_kacirilan_genc_olu_bulundu.htm?ArticleID=114847",
                "pub_date": "Date(2012-03-26T17:56:00)",
                "title": "Suriye'de kaçırılan genç ölü bulundu"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970576.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Ordu'nun Fatsa İlçesi'nde 57 yaşındaki Veysel A., tekrar\\n                birlikte olma isteğini reddeden eski eşi 48 yaşındaki Esme Türk'ü pazar yerinde pompalı tüfekle vurarak\\n                öldürdü<p> </p>\\n                Boşandığı eşi Esme Türk ile tekrar barışmak isteyen Veysel A., sürekli olumsuz yanıt aldı. Eski eşinin\\n                olumsuz yanıt vermesi üzerine çılgına dönen Veysel A., yanına aldığı pompalı tüfekle onun peşinden\\n                gitti.\\n\\n                Veysel A., pazar yerinde önünü kestiği eski eşi Esme Türke ve yanında bulununan kardeşinin eski eşi\\n                Meliha Şahine art arda ateş etti. Pazar yerinde bulunanlar silah sesleriyle paniğe kapılıp kaçışırken,\\n                iki kadın da kanlar içinde yerde kaldı. Ağır yaralanan 2 kadından Esme Türk kaldırıldığı Devlet\\n                Hastanesinde kurtarılamadı. Aynı hastaneye kaldırılan Meliha Şahin ise tedavi alt...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Eski_ese_pompali_tufekle_infaz.htm?ArticleID=114846",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Eski_ese_pompali_tufekle_infaz.htm?ArticleID=114846",
                "pub_date": "Date(2012-03-26T17:54:00)",
                "title": "Eski eşe pompalı tüfekle infaz"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970569.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Şike davasında Serdar Adalı, Tayfur Havutçu ve Sivasspor\\n                kalecisi Korcan Çelikay savunma yaptı. Üye Hakim kaleci Korcan'a, \\"Sivasspor-Fenerbahçe maçında birinci\\n                golde topa elin gitmek istemiyor gibi\\" <p> </p>\\n                \\"Futbolda şike\\" iddiaları üzerine aralarında Fenerbahçe Spor Kulübü Başkanı Aziz Yıldırımın da bulunduğu\\n                16sı tutuklu 93 sanık açılan davanın 9. duruşması sona erdi. Duruşmada Beşiktaş eski asbaşkanı Serdar\\n                Adalı ile Beşiktaş Sportif Direktörü Tayfur Havutçu savunma yaptı.\\n\\n                \\"İBB HENÜZ RAKİBİMİZ DEĞİLKEN TRANSFER CALIŞMASINA BAŞLADIK\\"\\n\\n                Adalı, \\"Masum olup da masum olduğunu savunmanın dünyada en zor şey olduğunu yeni öğrendim. İBB henüz\\n                rakibimiz değilken transfer calışmasına başladık\\" dedi. Adalı sözlerine şöyle devam etti: \\"Mart ayı\\n                sonlarında Tayfurla yaptığımız görüşmede transfe...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/_Topa_elin_gitmek_istemiyor_gibi_.htm?ArticleID=114845",
                "link": "http://www.posta.com.tr/spor/HaberDetay/_Topa_elin_gitmek_istemiyor_gibi_.htm?ArticleID=114845",
                "pub_date": "Date(2012-03-26T17:35:00)",
                "title": "'Topa elin gitmek istemiyor gibi'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970562.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Adana İl Jandarma Komutanlığı, aile içi şiddete uğrayıp,\\n                mahkeme kararıyla koruma altına alınan kadınların eşlerine 'öfke kontrolü' dersi verdi<p> </p>\\n                İl Jandarma Komutan Yardımcısı Yarbay Fatih Yıldırım başkanlığında Çocuk ve Kadın Koruma, Basın ve\\n                Halkla İlişkiler, Hukuk İşleri kısımları ve Sosyal Hizmetler uzmanından oluşan heyet, aile içi şiddete\\n                uğrayan ve mahkeme kararıyla koruma altına alınan kadınların eşleri A.Ü., C.B, T.S. ve A.T.yi davet\\n                edip, şiddetin nedenlerini ortadan kaldırmaya yönelik bilgilendirdi.\\n\\n                Heyetteki askeri yetkililer, eşlerine şiddet uygulayan 4 kişinin sorunlarını dinleyip, çözüm\\n                önerilerinde bulunarak, şiddet uygulamayı sürdürmeleri halinde karşılaşabileceklerini hukuki yaptırımlar\\n                hakkında bilgiler verd...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/Jandarmadan__ofke_kontrolu__dersi.htm?ArticleID=114844",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/Jandarmadan__ofke_kontrolu__dersi.htm?ArticleID=114844",
                "pub_date": "Date(2012-03-26T17:34:00)",
                "title": "Jandarmadan 'öfke kontrolü' dersi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970554.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Bulgaristan, tarihi çok eskilere dayanan, sımsıcak insanların\\n                yaşadığı, her güzelliği yaşayabileceğiniz küçük bir ülkedir<p> </p>\\n                 Eğer vakit bulabilir de ziyaret edebilirseniz komşu ülkemiz Bulgaristan, görebileceğiniz ve asla\\n                unutamayacağınız güzelliklerle dolu. Bu güzellikleri görebileceğiniz birkaç yerden bahsetmek gerekirse\\n                ilk başta söyleyeceğim yer Plovdiv olur burada mutlaka bir şehir turu yapmalısınız. Çünkü\\n                Bulgaristan`nın en güzel bölgesidir Plovdiv.\\n\\n                Bir diğer yer ise 600 çeşit şifalı su kaynağı olan Velingrad da başlıca kaplıca bölgesidir.  Şifalı su\\n                kaynaklarını yakınında kurulan kaplıca ve termal sağlık merkezleri burayı sağlık turizmi açısından da\\n                vazgeçilmez kılıyor.\\n\\n                Son olarak görmeniz gereke...",
                "guid": "http://www.posta.com.tr/Tatil/HaberDetay/Tarihi_eserleri_ve_termal_kaplicalari_ile_Bulgaristan.htm?ArticleID=114843",
                "link": "http://www.posta.com.tr/Tatil/HaberDetay/Tarihi_eserleri_ve_termal_kaplicalari_ile_Bulgaristan.htm?ArticleID=114843",
                "pub_date": "Date(2012-03-26T17:14:00)",
                "title": "Tarihi eserleri ve termal kaplıcaları ile Bulgaristan"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970547.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Yunan Adaları'nın en büyüğü ve en güzeli olan Rodos Adası'nı\\n                görmek kesinlikle bir ayrıcalıktır<p> </p>\\n                 \\n\\n                Yılda bir milyon turistin gidip gördüğü, sabahın ilk saatlerine kadar eğlencenin tadını çıkardıkları bu\\n                adada sakin bir tatil yapmak isteyenler için de alternatifler son derece zengin. Plajlarıyla meşhur bu\\n                adada yürüyüş yapabilir denizin kumun ve güneşin tadını çıkarabilir ve en güzel su sporlarını\\n                yapabilirsiniz. \\n\\n                Rodos şehri olarak bilinen bu ada aslında ikiye ayrılır. New Town ve Old Town olarak.  En güzel plajları\\n                bulabileceğiniz New Town da vaktin nasıl geçtiğini anlamayacaksınız. Balayı çiftleri, en güzel balayı\\n                otelleri ve en güzel kumsalların olduğu plajları ile unutulmaz...",
                "guid": "http://www.posta.com.tr/Tatil/HaberDetay/Yunan_Adalari_nin_gozdesi_Rodos.htm?ArticleID=114842",
                "link": "http://www.posta.com.tr/Tatil/HaberDetay/Yunan_Adalari_nin_gozdesi_Rodos.htm?ArticleID=114842",
                "pub_date": "Date(2012-03-26T17:09:00)",
                "title": "Yunan Adaları'nın gözdesi Rodos"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970532.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Kütahya Porselen, Open Stock Serisi'yle hem işlevsel, hem de\\n                enerji dolu tasarımlar sunuyor. Seride yer alan ürünler takım halinde satın alınabildiği gibi isteyenler\\n                seçtikleri ürünler ile kendi kombi<p> </p>\\n                Yeni güne capcanlı renklerin enerjisiyle başlamak için Kütahya Porselenden reddedilemeyecek bir teklif\\n                var. Geniş seçeneklere sahip Open Stock Serisi sunduğu avantajlarla rüya gibi tasarımlar vaat ediyor.\\n                Üstelik seride yer alan modeller ister takım halinde, istenirse de tek tek satın alınabiliyor.\\n\\n                Seri, puantiyeli ve çizgili desenleriyle bardaklardan servis tabaklarına, sosluklardan kaselere kadar\\n                birçok tasarım barındırıyor. Open Stockta yer alan ürünlerin fiyatı 149 TL ile 179 TL arasında\\n                değişiyor.\\n\\n                Open Stock Serisinin sınırsız seçeneklerini görmek için Kütahya Porselen ma...",
                "guid": "http://www.posta.com.tr/yasam/HaberDetay/Renklerin_buyusune_kapilin.htm?ArticleID=114840",
                "link": "http://www.posta.com.tr/yasam/HaberDetay/Renklerin_buyusune_kapilin.htm?ArticleID=114840",
                "pub_date": "Date(2012-03-26T17:03:00)",
                "title": "Renklerin büyüsüne kapılın"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970525.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Adana'da 16 Ekim 2011 tarihre, terör örgütü PKK yandaşlarının\\n                korsan gösterisinde, çöpe konulan bombanın patlatılması sonucu 1 polis memurunun şehit olmasına, 8'i\\n                polis memuru 12 kişinin de yaralanmas<p> </p>\\n                 Sanık çocukların suçlamayı kabul etmediği duruşmada olaydan yaralı kurtulan polis memurlarından Ü.C.K.,\\n                eylemcilerin bombanın patlamasının ardından sevinç çığlığı attığını söyledi.\\n\\n                Merkez Seyhan İlçesi Gülbahçesi Mahallesi Obalar Caddesinde 16 Ekim 2011de meydana gelen olayda, terör\\n                örgütü PKK yandaşları, yolu kapatıp, korsan gösteri düzenledi. Yüzleri maskeli grup, bölgede güvenlik\\n                önlemi alan çevik kuvvet ekiplerine de havai fişek ve taşlarla saldırdı. Çevik kuvvet ekipleri, korsan\\n                gösteri yapan grubu dağıtmak için Toplumsal Olaylara Müdahale Aracı (TOMA) eşliğinde müdahale etti. ...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/_Bomba_patlayinca_sevinc_cigliklari_atildi_.htm?ArticleID=114839",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/_Bomba_patlayinca_sevinc_cigliklari_atildi_.htm?ArticleID=114839",
                "pub_date": "Date(2012-03-26T16:54:00)",
                "title": "'Bomba patlayınca sevinç çığlıkları atıldı'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970518.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />İstanbul Sultanbeyli Belediyesi ve Fetih Koleji Mezunları\\n                Derneği'nden yaklaşık 40 kişi, Van'da meydana gelen depremlerin ardından binaları yıkılan ve çadırda\\n                eğitim gören İrfan Baştuğ İlköğretim Okul<p> </p>\\n                 Öğrencilere kitap setleri ve kırtasiye malzemeleri dağıtan öğrenciler, ayrıca kurdukları 5 bin\\n                kapasiteli konteyner kütüphanenin açılışını da yaptı.\\n                Sultangazi Belediyesi ve Fetih Mezunlar Derneği üyelerinden oluşan 40 kişilik bir ekip, Kardeşimin\\n                dileği Van projesi kapsamında depremlerin vurduğu Vana gelerek depremzede öğrencilere el uzattı.\\n\\n                Deprem nedeniyle okulları yıkılan çadırda eğitimlerine devam eden öğrenciler için 5 bin kitaptan oluşan\\n                konteyner kütüphane oluşturan üyeler, aynı zamanda öğrencilerin derslerinde motivasyonunu artırmak için\\n                3 gün onlarla birlikte çeşitli e...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/_Kardesimin_dilegi_Van__projesi_depremzede_cocuklari_sevindirdi.htm?ArticleID=114838",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/_Kardesimin_dilegi_Van__projesi_depremzede_cocuklari_sevindirdi.htm?ArticleID=114838",
                "pub_date": "Date(2012-03-26T16:49:00)",
                "title": "'Kardeşimin dileği Van' projesi depremzede çocukları sevindirdi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970511.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />İstanbul Büyükşehir Belediye Başkanı Kadir Topbaş, Silivri\\n                Boğluca Deresi'ndeki evlerin yıkım töreninde iş makinesi koltuğuna oturdu. Topbaş, yıktığı bir evin\\n                demirlerinin az olduğunu görünce \\"Sadece <p> </p>\\n                İstanbul Büyükşehir Belediye Başkanı Topbaş, Silivri Boğluca Dere yatağındaki evlerin yıkımı için\\n                düzenlenen törende konuşurken bu binaların deprem riski taşıyan binalar olduğunu söyledi. \\"Nasıl\\n                durmuşlar ayakta, durmuşlar. Bu sıkıntıları yaşayan bir kentiz. Bunu kader olmaktan çıkarmak istiyoruz.\\n                Bu kader değil \\" diyen Topbaş, deprem konusundaki uyarılarını sürdürerek, \\"Allah Bilimi insanlara\\n                vermiş. Bilime saygısı olmayan bedelini öder. Her zeminde yapı yapılır. Adam gibi yapılırsa 10\\n                şiddetindeki deprem bile problem teşkil etmez.\\" diye konuştu.\\n\\n                BİNANIN DEMİRLERİ EKSİK\\n\\n                Topbaş, ko...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/Topbas_is_makinesi_koltuguna_oturdu.htm?ArticleID=114837",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/Topbas_is_makinesi_koltuguna_oturdu.htm?ArticleID=114837",
                "pub_date": "Date(2012-03-26T16:36:00)",
                "title": "Topbaş iş makinesi koltuğuna oturdu"
            },
            {
                "content": "Ergenekon davasının gizli tanığı Poyraz'ın tehdit edilmesine ilişkin yürütülen soruşturmada\\n                şüphelilerden T.Ç'nin, Poyraz için \\"Allah rahmet eylesin\\" diye konuşması teknik takibe takıldı<p>\\n                </p>\\n                Ergenekon davasının gizli tanığı Poyraz ile Cumhuriyet Gazetesine molotof kokteyli atan Bedirhan Şinali\\n                ifadelerini değiştirmeleri için tehdit ettiği gerekçesiyle yürütülen soruşturmada şüphelilerin savcılık\\n                ifadesi devam ediyor.\\n\\n                PEKERİN ADAMI POYRAZ İLE AMASYADA GÖRÜŞMÜŞ\\n\\n                Ergenekon davasının gizli tanığı Poyrazın tehdit edilmesine ilişkin yürütülen soruşturmada şüphelilerin\\n                teknik takibe takılan konuşmaları sorgu konusu oldu. Yapılan tespitlere göre, Sedat Pekerin adamlarından\\n                olduğu iddia edilen İ.Y, gizli tanık Poyraz ile Amasyada bir araya geldi. Poyrazdan Peker aleyhin...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/_Poyraz_icin_niye__Allah_rahmet_eylesin__dedin__.htm?ArticleID=114836",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/_Poyraz_icin_niye__Allah_rahmet_eylesin__dedin__.htm?ArticleID=114836",
                "pub_date": "Date(2012-03-26T16:33:00)",
                "title": "'Poyraz için niye \\"Allah rahmet eylesin\\" dedin?'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970504.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Tatil için Erzurum'a gelen Kaya Çilingiroğlu, eşi Feraye ve\\n                çocukları Kaya ile birlikte Palandöken'de bol bol kayak yapıp, yöresel cağ kebabı yedi<p> </p>\\n                Palandökende bu yıl hizmete açılan Xanadu Otelinin pistinde özellikle gece kayağı yapan Cilingiroğlu ve\\n                eşi, 4 günlük tatilin çok iyi geçtiğini söyledi. Ailesi ile birlikte dün sabah Erzurumdan ayrılan Kaya\\n                Çilingiroğlu, \\"Türkiyede ilk kez gece kayağı yaptık. Muhteşem bir duygu. İstanbula uzak görünen\\n                Palandöken aslında 2 saat mesafede. Uçakla Erzuruma iner inmez 10 dakikada Palandökende oluyoruz. Burayı\\n                çok sevdik yine geleceğiz\\" dedi.\\n\\n                Eşi ve oğlu Kaya ile birlikte tatillerinin son gecesi meşaleli kayak gösterisini izleyen Kaya\\n                Çilingiroğlu, gecede düzenlenen cağ kebap partisi...",
                "guid": "http://www.posta.com.tr/magazin/HaberDetay/Cilingiroglu_ailesinin_kayak_keyfi.htm?ArticleID=114835",
                "link": "http://www.posta.com.tr/magazin/HaberDetay/Cilingiroglu_ailesinin_kayak_keyfi.htm?ArticleID=114835",
                "pub_date": "Date(2012-03-26T16:20:00)",
                "title": "Çilingiroğlu ailesinin kayak keyfi"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970497.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Cumhurbaşkanı Derviş Eroğlu, KKTC yönetiminin, Maraş\\n                bölgesini 38 yıl aradan sonra yerleşime açmak için hazırlık yaptığı yönündeki iddiayla ilgili olarak,\\n                \\"Herkesin bildiği üzere KKTC'nin ayrılmaz bir<p> </p>\\n                Milliyet gazetesi bugün yayınlanan özel haberinde, Kuzey Kıbrıs Türk Cumhuriyeti yönetiminin, Rumların\\n                AB dönem başkanı olacağı 1 Temmuzda Kapalı Maraşı tek taraflı olarak, Türk tarafının kontrolünde\\n                \\"yerleşime açmak\\" için çalışma başlattığını ileri sürdü. Gazete haberinde, eskiden burada evi olan tüm\\n                Rumların bu karar sonrasında kente  dönebileceklerini yazdı. Haberde konunun KKTC Cumhurbaşkanı Derviş\\n                Eroğlunun son Ankara ziyaretinde de gündeme geldiğini ve Kıbrıs Türk tarafının hazırladığı öneriye\\n                Ankaranın da olumlu yaklaştığı belirtildi. Cumhurbaşkanı Derviş Eroğlu Devlet kanalı BRT...",
                "guid": "http://www.posta.com.tr/siyaset/HaberDetay/_Maras_KKTC_nin_ayrilmaz_bir_parcasi_.htm?ArticleID=114834",
                "link": "http://www.posta.com.tr/siyaset/HaberDetay/_Maras_KKTC_nin_ayrilmaz_bir_parcasi_.htm?ArticleID=114834",
                "pub_date": "Date(2012-03-26T16:18:00)",
                "title": "'Maraş KKTC'nin ayrılmaz bir parçası'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970490.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Boğarak öldürdüğü annesinin cesedini satırla parçalara\\n                ayırdıktan sonra denize atmak isterken yakalanan gence verilen 23 yıllık hapis cezası Yargıtay\\n                tarafından onandı<p> </p>\\n                Bursada 2008 yılında internette \\"Annemi nasıl öldürebilirim?\\" diye anket düzenledikten sonra 46\\n                yaşındaki annesi Asiye Fandoğlunu boğarak öldürüp cesedini parçalara ayırdıktan sonra denize atmayı\\n                planlarken yakalanan 19 yaşındaki Mümin Fandoğluna verilen 23 yıllık hapis cezası, Yargıtay tarafından\\n                onadı. Daha önce de yargılanıp 20 yıl hapis cezasına çarptırılan Fandoğlunun cezasını Yargıtay az\\n                bularak bozmuştu.\\n\\n                Merkez Osmangazi İlçesi Hamitler Mahallesinde oturan Mümin Fandoğlu, 2008 yılı Mayıs ayında, sürekli\\n                tartıştığı annesi Asiye Fandoğlunu öldürmek için internette anket düze...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/Annesinin_cesedini_satirla_dograyan_gence_23_yil.htm?ArticleID=114833",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/Annesinin_cesedini_satirla_dograyan_gence_23_yil.htm?ArticleID=114833",
                "pub_date": "Date(2012-03-26T16:15:00)",
                "title": "Annesinin cesedini satırla doğrayan gence 23 yıl"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970483.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Antalya'da pazarcı 38 yaşındaki M.Ç., 3 çocuğuna bakamadığı\\n                gerekçesiyle 8 katlı binanın çatısından atlamak istedi. M.Ç., polisin yarım saatlik çabası sonucu ikna\\n                edilerek çatıdan indirildi<p> </p>\\n                Apartman sakinlerinin, tanımadıkları bir kişinin binanın çatısından intihar girişiminde bulunduğunu\\n                bildirmesi üzerine olay yerine itfaiye, ambulans ve polis ekipleri sevk edildi. İntihar girişiminde\\n                bulunan kişinin çatıdan kendisini sarkıttığını gören polis memurları, çatıya çıkarak onu ikna etmeye\\n                çalıştı. Yaklaşık yarım saatin sonunda intihardan vazgeçirilen pazarcı M.Ç., polislerle birlikte binadan\\n                indi.\\n\\n                Ağlayarak ambulansa binen M.Ç., \\"3 çocuğum var, onlara bakamıyorum. Biz nasıl yaşayacağız\\" dedi. Polis\\n                tarafından güçlükle sakinleştirilen M.Ç., ambulansla hastaneye götürüldü.\\n\\n                ...",
                "guid": "http://www.posta.com.tr/3Sayfa/HaberDetay/_Cocuklarima_bakamiyorum_.htm?ArticleID=114832",
                "link": "http://www.posta.com.tr/3Sayfa/HaberDetay/_Cocuklarima_bakamiyorum_.htm?ArticleID=114832",
                "pub_date": "Date(2012-03-26T16:13:00)",
                "title": "'Çocuklarıma bakamıyorum'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970475.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Küçük Aptalın Büyük Dünyası' ve 'Ve Geri Kalan Her Şey'\\n                isimli iki kitabı birden sinemaya aktarılacak olan PuCCa, \\"Filmde kendimi oynamayı istiyorum ama tabii\\n                bu, yetenek işi. O yüzden de oyuncu arayı<p> </p>\\n                Türkiye'de herkes onu, ayrıldığı sevgilisini rezil etmek amacıyla yazmaya başladığı blog'la tanıdı. O\\n                dönem sosyal medyada yüzünü ve gerçek adını ifşa etmeyen PuCCa, kısa sürede aldı başını yürüdü.\\n                Yaşadıklarını sansürsüz, içinden geldiği gibi yazıyor; sevenlerini hem güldürüp hem de\\n                hüzünlendirebiliyordu.\\n\\n                Derken PuCCa'yı keşfeden Okuyanus Yayınevi ilk kitabı 'Küçük Aptalın Büyük Dünyası' ve ikinci kitabı 'Ve\\n                Geri Kalan Her Şey'i yayınlandı. Kitapların gördüğü yoğun ilgi, yapımcıların da dikkatini çekti ve yapım\\n                şirketi Medyavizyon; Okuyanus Yayınevi ve PuCCa ile yapılan anlaşma sonuc...",
                "guid": "http://www.posta.com.tr/yasam/HaberDetay/_Cem_Yilmaz_la_cay__corba_icsek_de_olur_.htm?ArticleID=114831",
                "link": "http://www.posta.com.tr/yasam/HaberDetay/_Cem_Yilmaz_la_cay__corba_icsek_de_olur_.htm?ArticleID=114831",
                "pub_date": "Date(2012-03-26T15:47:00)",
                "title": "'Cem Yılmaz'la çay, çorba içsek de olur'"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970461.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />NTVSPOR spikeri Dilara Gönder, Fenerbahçe Universal takımını\\n                karşılamaya giden taraftarlar için, \\"Olay çıkartmak için gelen taraftarlar\\" yorumu yapınca ünlü spiker\\n                tepki aldı<p> </p>\\n                Bu konuşma üzerine yayına bağlanan Fenerbahçeli yönetici Hakan Dinçay, Dilara Gönder'e tepki gösterdi.\\n                Kulüp resmi sitesinden Hakan Dinçay imzalı bir açıklama yayınladı. Bunun üzerine canlı yayına Gönder,\\n                \\"sözlerim yanlış anlaşıldı, tüm Fenerbahçe camiasından ve taraftarlarından özür dilerim\\" dedi.\\n\\n                CEV Avrupa Şampiyonu Voleybol Takımı Fenerbahçe Universali karşılamak için sabaha karşı havalimanına\\n                gelen Fenerbahçeli taraftarlar hakkında spiker Dilara Gönder'in Olay çıkarmak için gelen taraftarlar\\n                şeklinde yorum yapınca Sarı Lacivertli Kulübün yöneticisi Hakan Dinçay telefonla canlı ...",
                "guid": "http://www.posta.com.tr/spor/HaberDetay/Dilara_Gonder_e_buyuk_tepki.htm?ArticleID=114829",
                "link": "http://www.posta.com.tr/spor/HaberDetay/Dilara_Gonder_e_buyuk_tepki.htm?ArticleID=114829",
                "pub_date": "Date(2012-03-26T15:36:00)",
                "title": "Dilara Gönder'e büyük tepki"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970423.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />Metrobüs'ün mucidi olarak bilinen Brezilyalı Enrique\\n                Peñalosa, İstanbul'a geldi ve metrobüse bindi<p> </p>\\n                Bogota Belediye Başkanlığı yaptığı dönemde başta ulaşım olmak üzere yerel yönetim konusunda önemli\\n                çalışmalar yapan Enrique Peñalosa, ArkiPARC'a katılmak için İstanbul'a geldi.\\n\\n                Bu seyahat sırasında metrobüs ile ilgili görüşlerini sorduğumuz Peñalosa, Sistem başta iyi kurgulanmış\\n                ama tek hat üzerinde çalışması büyük bir sorun. Otobüslerin durdukları istasyonlar genişletilerek,\\n                kapasite artırılabilir. Daha sonra şehrin her noktasına ulaşabilecek çapraz hatlar oluşturulabilir,\\n                şeklinde açıklama yaptı.\\n\\n                Metrobüs'ün fikir babası olan TransMilenio, Peñalosa tarafından Curitiba kentinde...",
                "guid": "http://www.posta.com.tr/turkiye/HaberDetay/Metrobusun_Brezilyali_mucidi_Istanbul_da.htm?ArticleID=114828",
                "link": "http://www.posta.com.tr/turkiye/HaberDetay/Metrobusun_Brezilyali_mucidi_Istanbul_da.htm?ArticleID=114828",
                "pub_date": "Date(2012-03-26T15:19:00)",
                "title": "Metrobüsün Brezilyalı mucidi İstanbul'da"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970347.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" /><p> </p>",
                "guid": "http://www.posta.com.tr/yasam/fotogaleri/FotoGaleri/Doyasiya_eglendiler.htm?ArticleID=114827",
                "link": "http://www.posta.com.tr/yasam/fotogaleri/FotoGaleri/Doyasiya_eglendiler.htm?ArticleID=114827",
                "pub_date": "Date(2012-03-26T15:11:00)",
                "title": "Doyasıya eğlendiler"
            },
            {
                "content": "<img src=\\"http://icdncube.posta.com.tr/editor/HR216x162/26/3/2012/fft13mm970341.jpg\\"\\n                align=\\"left\\" style=\\"padding:2px 10px\\" />S&P: \\"Türkiye kaynaklarını hızla ihracat odaklı büyümeye\\n                yönlendirebilecek esneklik sergilemesi halinde kredi notunu yükseltebiliriz\\"<p> </p>\\n                Uluslararası kredi derecelendirme kuruluşu Standard & Poors (S&P), \\"Türkiyenin kredi notunu\\n                kaynaklarını hızla ihracat odaklı büyümeye yönlendirebilecek esneklik sergilemesi halinde\\n                yükseltebileceğini\\" bildirdi.\\n\\n                S&Pnin Türkiye analizi raporunda, \\"Türkiye kaynaklarını hızla ihracat odaklı büyümeye\\n                yönlendirebilecek esneklik sergilemesi halinde kredi notunu yükseltebiliriz. Bu mali hesapları önemli\\n                oranda zayıflatmaksızın ya da finansal sektörü istikrarsız hale getirmeksizin dış dengesizlikleri\\n                azaltacaktır\\" denildi.\\n\\n                Türkiyenin kredi notunda ya da kredi notu görünümünde herhangi b...",
                "guid": "http://www.posta.com.tr/ekonomi/HaberDetay/S_P_den_Turkiye_ye__sartli__not_artirim_sinyali.htm?ArticleID=114826",
                "link": "http://www.posta.com.tr/ekonomi/HaberDetay/S_P_den_Turkiye_ye__sartli__not_artirim_sinyali.htm?ArticleID=114826",
                "pub_date": "Date(2012-03-26T14:53:00)",
                "title": "S&P'den Türkiye'ye 'şartlı' not artırım sinyali"
            },
            {
                "content": "215,00 TL yerine 180,00 TL<p> </p>",
                "guid": "http://www.posta.com.tr/MarcaMarcaHaberDetay/Swatch_YGS4030_Erkek_Kol_Saati.htm?ArticleID=114825",
                "link": "http://www.posta.com.tr/MarcaMarcaHaberDetay/Swatch_YGS4030_Erkek_Kol_Saati.htm?ArticleID=114825",
                "pub_date": "Date(2012-03-26T14:43:00)",
                "title": "Swatch YGS4030 Erkek Kol Saati"
            },
            {
                "content": "96,90 TL yerine 48,90 TL<p> </p>",
                "guid": "http://www.posta.com.tr/MarcaMarcaHaberDetay/Fushja_ADORE_ME_AM_1006_SUTYEN_JARTIYERLI_ETEK_KIRMIZI.htm?ArticleID=114824",
                "link": "http://www.posta.com.tr/MarcaMarcaHaberDetay/Fushja_ADORE_ME_AM_1006_SUTYEN_JARTIYERLI_ETEK_KIRMIZI.htm?ArticleID=114824",
                "pub_date": "Date(2012-03-26T14:40:00)",
                "title": "Fushja ADORE ME AM 1006 SÜTYEN JARTİYERLİ ETEK KIRMIZI"
            },
            {
                "content": "39,80 TL yerine 19,90 TL<p> </p>",
                "guid": "http://www.posta.com.tr/MarcaMarcaHaberDetay/BUDGET_102_02511_020_Erkek_Hirka.htm?ArticleID=114823",
                "link": "http://www.posta.com.tr/MarcaMarcaHaberDetay/BUDGET_102_02511_020_Erkek_Hirka.htm?ArticleID=114823",
                "pub_date": "Date(2012-03-26T14:38:00)",
                "title": "BUDGET 102 02511 020 Erkek Hırka"
            }
        ]
    }
    destructor DOMParser
    """
    test_rss("/oknetwiki/trunk/py_lib/vsft/test/feeds/e55.xml")

def test_rss6():
    """
    >>> test_rss6()
    constructor DOMParser
    {
        "item": [
            {
                "author": "Christina MacPherson",
                "content": "Obama: US nuclear disarmament 'a moral obligation' News Ok, Joel Gehrke | Published: March 26, 2012      President Obama called nuclear disarmament as \\"a moral obligation,\\" as he […]",
                "guid": "http://nuclear-news.net/2012/03/28/usas-moral-obligation-to-lead-in-nuclear-disarmament-obama/",
                "is_perma_link": true,
                "link": "http://nuclear-news.net/2012/03/28/usas-moral-obligation-to-lead-in-nuclear-disarmament-obama/",
                "pub_date": "Date(2012-03-28T08:39:44)",
                "title": "USA's 'moral obligation' to lead in nuclear disarmament - Obama"
            },
            {
                "author": "ytgblogroundup",
                "content": "Yahoo! Alerts\\n\\nMy Alerts\\n\\nThe latest from 24/7 Wall St.\\n\\n\\nShanghai Composite Off 2.7%\\nFacebook Admits Yahoo! Problem In Filing\\n24/7 Wall St. Closing Bell (MU, ATVI, BAC, SCCO, APOL, GOL, WAG, LEN, […]",
                "guid": "http://ytgblogroundup.wordpress.com/2012/03/28/y-alert-247-wall-st-3139/",
                "is_perma_link": true,
                "link": "http://ytgblogroundup.wordpress.com/2012/03/28/y-alert-247-wall-st-3139/",
                "pub_date": "Date(2012-03-28T08:39:42)",
                "title": "Y! Alert: 24/7 Wall St."
            },
            {
                "author": "stylenetwork",
                "content": "Michelle Obama sense of style has caught the attention of many and has been describes as a fashion icon. Michelle has been know to promote American designers (even […]",
                "guid": "http://stylenetwork.wordpress.com/2012/03/28/michelle-obama-style-icon/",
                "is_perma_link": true,
                "link": "http://stylenetwork.wordpress.com/2012/03/28/michelle-obama-style-icon/",
                "pub_date": "Date(2012-03-28T08:38:01)",
                "title": "Michelle Obama: Style Icon"
            },
            {
                "author": "ytgblogroundup",
                "content": "Yahoo! Alerts\\n\\nMy Alerts\\n\\nThe latest from 24/7 Wall St.\\n\\n\\nShanghai Composite Off 2.7%\\nFacebook Admits Yahoo! Problem In Filing\\n24/7 Wall St. Closing Bell (MU, ATVI, BAC, SCCO, APOL, GOL, WAG, LEN, […]",
                "guid": "http://ytgblogroundup.wordpress.com/2012/03/28/y-alert-247-wall-st-3138/",
                "is_perma_link": true,
                "link": "http://ytgblogroundup.wordpress.com/2012/03/28/y-alert-247-wall-st-3138/",
                "pub_date": "Date(2012-03-28T08:37:06)",
                "title": "Y! Alert: 24/7 Wall St."
            },
            {
                "author": "lapolillacubana26",
                "content": "Reflexiones del Compañero FIDEL: Los tiempos difíciles de la humanidad\\n\\nEl mundo está cada vez más desinformado en el caos de acontecimientos que se suceden a ritmos jamás sospechados.\\n\\nLos […]",
                "guid": "http://elblogdelapolillacubana.wordpress.com/2012/03/28/fidel-los-tiempos-dificiles-de-la-humanidad/",
                "is_perma_link": true,
                "link": "http://elblogdelapolillacubana.wordpress.com/2012/03/28/fidel-los-tiempos-dificiles-de-la-humanidad/",
                "pub_date": "Date(2012-03-28T08:35:56)",
                "title": "FIDEL: Los tiempos difíciles de la humanidad"
            },
            {
                "author": "podgeoh92",
                "content": "[caption id=\\"\\" align=\\"aligncenter\\" width=\\"495\\" caption=\\"Dontari Poe\\"][/caption]\\n\\nThe NFL Draft is now just over a month away and NFL scouts are busy getting their draft boards ready for the big […]",
                "guid": "http://mrnfl.wordpress.com/2012/03/28/mock-draft-3-0/",
                "is_perma_link": true,
                "link": "http://mrnfl.wordpress.com/2012/03/28/mock-draft-3-0/",
                "pub_date": "Date(2012-03-28T08:35:25)",
                "title": "Mock Draft 3.0"
            },
            {
                "author": "greatriversofhope",
                "content": "An opponent of U.S. President Barack Obama's health-care reform wears a glove outside the Supreme Court in Washington, D.C., Tuesday, during the second day of legal arguments […]",
                "guid": "http://greatriversofhope.wordpress.com/2012/03/28/supreme-court-justices-signal-possible-snag-for-obamacare/",
                "is_perma_link": true,
                "link": "http://greatriversofhope.wordpress.com/2012/03/28/supreme-court-justices-signal-possible-snag-for-obamacare/",
                "pub_date": "Date(2012-03-28T08:34:46)",
                "title": "Supreme Court Justices Signal Possible Snag for ObamaCare."
            },
            {
                "author": "extropiadasilva",
                "content": "[caption id=\\"attachment_762\\" align=\\"aligncenter\\" width=\\"300\\" caption=\\"Volta at Thinkers\\"][/caption]\\n\\n\\n\\n\\n[2012/03/27 15:31]  Extropia DaSilva: Welcome to Thinkers!\\n[2012/03/27 15:31]  Scarp Godenot: That is a fine strategy, where do I get one of these […]",
                "guid": "http://extropiadasilva.wordpress.com/2012/03/28/thinkers-march-27-2012-who-shouldnt-get-married/",
                "is_perma_link": true,
                "link": "http://extropiadasilva.wordpress.com/2012/03/28/thinkers-march-27-2012-who-shouldnt-get-married/",
                "pub_date": "Date(2012-03-28T08:30:43)",
                "title": "THINKERS MARCH 27 2012: WHO SHOULDN'T GET MARRIED?"
            },
            {
                "author": "JP Mangalindan, Writer-Reporter",
                "content": "Fortune's curated selection of tech stories from the last 24 hours. Sign up to get the round-up delivered to you each and every day.\\n\\"We're not winning.\\" -- Shawn Henry, executive assistant director of […]",
                "guid": "http://tech.fortune.cnn.com/2012/03/28/ipad-batterygate-is-no-big-deal/",
                "is_perma_link": true,
                "link": "http://tech.fortune.cnn.com/2012/03/28/ipad-batterygate-is-no-big-deal/",
                "pub_date": "Date(2012-03-28T08:30:17)",
                "title": "Today in Tech: Why the iPad's 'batterygate' is no big deal"
            },
            {
                "author": "iwyqaxewun",
                "content": "otomaqaqaba.blogspot.comCBS NewsAnalysis: Health ruling looms sm »",
                "guid": "http://iwyqaxewun.wordpress.com/2012/03/28/analysis-health-ruling-looms-small-in-obama-race-cbs-news/",
                "is_perma_link": true,
                "link": "http://iwyqaxewun.wordpress.com/2012/03/28/analysis-health-ruling-looms-small-in-obama-race-cbs-news/",
                "pub_date": "Date(2012-03-28T08:30:02)",
                "title": "Analysis: Health ruling looms small in Obama race - CBS News"
            }
        ]
    }
    destructor DOMParser
    """
    test_rss("/oknetwiki/trunk/py_lib/vsft/test/feeds/wordpress.xml")


def test_rss7():
    """
    >>> test_rss7()
    constructor DOMParser
    destructor DOMParser
    {
        "item": [
            {
                "author": "admin (online)",
                "content": "Açık mikrofon kazasına uğrayan <em>Obama</em> bu sefer aynı hataya düşmedi… Güney\\n                Kore'nin başkenti Seul'deki Nükleer Güvenlik Zirvesi kapsamında dün Medvedev'le\\n                bir araya gelen ve bu görüşme sırasındaki sözleri <b>...</b>",
                "link": "http://www.turknorthamerica.com/2012/03/obamanin-kahkahaya-bogan-mikrofon-hareketi/",
                "pub_date": "Date(2012-",
                "publisher": "Turk North America",
                "title": "<b>Obama</b>'nın kahkahaya boğan mikrofon hareketi – Turk North America"
            },
            {
                "author": "bilinmiyor",
                "content": "<em>Obama</em>'dan Kazakistan'a Övgü. Güney Kore'nin\\n                başkenti Seul'de düzenlenen Nükleer Güvenlik Zirvesi öncesinde, Kazakistan Cumhurbaşkanı\\n                Nursultan Nazarbayev ve ABD Başkanı Barack <em>Obama</em> biraya geldi.",
                "link": "http://www.showhaber.com/obamadan-kazakistana-ovgu-549278h.htm",
                "pub_date": "Date(2012-",
                "publisher": "SHOWHABER",
                "title": "<b>Obama</b>'dan Kazakistan'a Övgü haberi - ShowHaber.Com"
            },
            {
                "author": "Ramiz Meşedihasanlı",
                "content": "http://www.ahiskapress.com/wp-admin/post- Nükleer silah konusunu görüşmek üzere birçok ülkenin\\n                devlet ve hükümet başkanları Güney Kore'nin başkenti Seul'de bir araya geldi. İki günlük\\n                zirvede nükleer silaha sahip <b>...</b>",
                "link": "http://www.ahiskapress.com/?p=13352",
                "pub_date": "Date(2012-",
                "publisher": "Ahıska Press",
                "title": "Nazarbayev Seul'de <b>Obama</b> ve Erdoğan ile görüştü"
            },
            {
                "author": "admin (online)",
                "content": "Erdoğan ile <em>Obama</em>'nın kameralar önünde yaptığı açıklamanın sonunda\\n                <em>Obama</em>'nın Dışişleri Bakanı Davutoğlu'na Erdoğan'ın\\n                arkasından eliyle 'Gel' işareti yapmasını CHP'liler <em>Obama</em>'nın\\n                Davutoğlu'nu aşağılaması olarak <b>...</b>",
                "link": "http://www.turknorthamerica.com/2012/03/obama-davutogluna-hakaret-mi-etti-video/",
                "pub_date": "Date(2012-",
                "publisher": "Turk North America",
                "title": "<b>Obama</b> Davutoğlu'na hakaret mi etti? VIDEO – Turk North America"
            },
            {
                "author": "ilgazetesi",
                "content": "ABD Başkanı Barack <em>Obama</em>, Rusya Devlet Başkanı Dmitri Medvedev'le\\n                Seul'de yaptığı görüşmede açık kalan mikrofonun azizliğine uğradı. <em>Obama</em>.",
                "link": "http://www.ilgazetesi.com.tr/2012/03/27/obama-ve-medvedevin-acik-kalan-mikrofonundan-fuze-kalkani-mesaji/0123877/",
                "pub_date": "Date(2012-",
                "publisher": "İL GAZETESİ",
                "title": "<b>Obama</b> ve Medvedev'in açık kalan mikrofonundan füze kalkanı <b>...</b>"
            },
            {
                "author": "bilinmiyor",
                "content": "Erdoğan ve <em>Obama</em> görüştü. Seul'de bulunan Başbakan Recep Tayyip\\n                Erdoğan, ABD Başkanı Barack <em>Obama</em>'yla görüştü.",
                "link": "http://www.posta.com.tr/siyaset/HaberDetay/Erdogan_ve_Obama_gorustu.htm?ArticleID=114561",
                "pub_date": "Date(2012-",
                "publisher": "Posta Haber Hattı",
                "title": "Erdoğan ve <b>Obama</b> görüştü - Posta"
            },
            {
                "author": "admin",
                "content": "Mikrofonun kapalı olduğunu düşünen <em>Obama</em>, kapalı kapılar ardında\\n                söylenmesi gereken şu cümleyi son birkez daha Medvedev'e hatırlattı: “Füze kalkanıyla ilgili\\n                sorunu çözeceğiz. Ama şu çok önemli, o (Putin) bana zaman <b>...</b>",
                "link": "http://wrc.cc/?p=13391",
                "pub_date": "Date(2012-",
                "publisher": "WRC Güncel Haber",
                "title": "<b>Obama</b> açık mikrofona yakalandı « WRC Güncel Haber"
            },
            {
                "author": "bilinmiyor",
                "content": "Nükleer Güvenlik Zirvesi ne katılmak üzere Seul e giden Başbakan Recep Tayyip Erdoğan, ABD\\n                Başkanı Barack <em>Obama</em> ile yaklaşık bir buçuk saat görüştü.",
                "link": "http://www.medyafaresi.com/haber/77187/guncel-obama-ve-erdogan-gorusmesinde-kritik-mesajlar.html",
                "pub_date": "Date(2012-",
                "publisher": "MedyaFaresi.com",
                "title": "<b>Obama</b> ve Erdoğan görüşmesinde kritik mesajlar! - Güncel\\n                <b>...</b>"
            },
            {
                "author": "AKTIFHABER",
                "content": "<em>Obama</em>'nın Mikrofon Tedbiri Güldürdü Açık mikrofon kazasına uğrayan\\n                <em>Obama</em>, bir daha aynı hataya düşmemek için bakın nasıl bir yola başvurdu? Devamı\\n                İçin Tıklayınız… Haberin Tüm Metni için: <em>Obama</em>'nın Mikrofon Tedbiri\\n                Güldürdü <b>...</b>",
                "link": "http://www.bugunnet.com/obamanin-mikrofon-tedbiri-guldurdu.html",
                "pub_date": "Date(2012-",
                "publisher": "Bugün NET - Güncel Haberler...!",
                "title": "Bugün NET – Güncel Haberler…! » Blog Archive » <b>Obama</b>'nın <b>...</b>"
            },
            {
                "author": "issiz",
                "content": "0 Barack <em>Obama</em> Singing Sexy and I Know It by LMFAO. Next. ﻿. issiz; 1\\n                dakika ago. Video · Tweet Share. Yorumlar. Önemli. Telif haklari icin\\n                issizler@windowslive.com ile iletisime geciniz. Detayli bilgi icin Kullanim Sartlari sayfamıza bakınız.",
                "link": "http://www.issizadam.net/video-izle/barack-obama-singing-sexy-and-i-know-it-by-lmfao.html",
                "pub_date": "Date(2012-",
                "publisher": "İŞSİZLER",
                "title": "İŞSİZLER » İşsizlik bir boş bulunmuşluktur. » Barack <b>Obama</b> Singing <b>...</b>"
            }
        ]
    }
    """
    # hack for realtime cut time minute
    s = test_rss("./originators/aa_com_tr/page_samples/blogspot.xml")
    print re.sub("\d+-\d+T\d+:\d+:\d+.\d+\)", "", s)
