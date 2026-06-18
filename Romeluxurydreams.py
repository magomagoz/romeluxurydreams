import streamlit as st
import base64
import os

# ==========================================
# CONFIGURAZIONE PAGINA
# ==========================================
st.set_page_config(
    page_title="Property Finder Roma | Rome Luxury Dreams",
    page_icon="🗝️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# DIZIONARIO TRADUZIONI (8 LINGUE GLOBALI)
# ==========================================
TRANSLATIONS = {
    "it": {
        "brand": "Rome Luxury Dreams",
        "hero_title": "La Chiave per la Tua Dimora Esclusiva nella Città Eterna",
        "hero_subtitle": "Ricerca off-market, negoziazione riservata e accesso privilegiato al patrimonio immobiliare più prestigioso di Roma.",
        "services_header": "Il Servizio Property Finder",
        "srv1_title": "🔍 Ricerca Off-Market",
        "srv1_desc": "Accesso a un portfolio invisibile di proprietà non pubblicate sui canali tradizionali, garantendo esclusività assoluta.",
        "srv2_title": "🤝 Negoziazione Riservata",
        "srv2_desc": "Trattative condotte nel massimo riserbo per proteggere l'identità e gli interessi finanziari di investitori.",
        "srv3_title": "🏛️ Analisi Architettonica",
        "srv3_desc": "Valutazione rigorosa di vincoli storici, stratificazioni edilizie e stato conservativo dei palazzi d'epoca.",
        "srv4_title": "🗝️ Servizio Chiavi in Mano",
        "srv4_desc": "Assistenza completa dall'individuazione dell'immobile fino agli aspetti legali, notarili e di interior design.",
        "expertise_header": "Expertise Romana",
        "exp_sub": "Oltre i Confini dell'Agenzia Tradizionale",
        "exp_text": "Comprendere il valore di un immobile di lusso a Roma richiede molto più di una semplice stima al metro quadro. Richiede una conoscenza enciclopedica del suo tessuto urbano storico. <br><br>Dalle antiche Mura Aureliane ai palazzi nobiliari affacciati sulle piazze barocche. Identifichiamo residenze che non sono solo spazi abitativi, ma veri e propri frammenti della storia architettonica della Capitale.",
        "exp_list_title": "I Nostri Quartieri di Riferimento",
        "exp_l1": "<b style='color: var(--gold-accent)'>Centro Storico:</b> Tridente, Navona, Pantheon.",
        "exp_l2": "<b style='color: var(--gold-accent)'>Parioli & Pinciano:</b> Residenziale d'epoca ed eleganza.",
        "exp_l3": "<b style='color: var(--gold-accent)'>Aventino:</b> Oasi di silenzio a un passo dal Circo Massimo.",
        "exp_l4": "<b style='color: var(--gold-accent)'>Trastevere & Gianicolo:</b> Fascino bohémien e viste dominanti.",
        "contact_header": "Richiedi una Consulenza Privata",
        "contact_sub": "Lascia i tuoi recapiti per essere contattato con la massima discrezione.",
        "form_name": "Nome e Cognome *",
        "form_email": "Email *",
        "form_phone": "Recapito Telefonico",
        "form_budget_label": "Budget di Riferimento",
        "form_budget_opts": ["Seleziona il range d'investimento", "600.000 € - 1.000.000 €", "1.000.000 € - 2.000.000 €", "Oltre 2.000.000 €"],
        "form_msg": "Esigenze Particolari (es. Terrazza, Ascensore, Box auto)",
        "form_btn": "Invia Richiesta Riservata",
        "form_success": "Grazie {name}. La tua richiesta è stata recepita in totale riservatezza.",
        "form_error": "Per favore, compila i campi obbligatori."
    },
    "en": {
        "brand": "Rome Luxury Dreams",
        "hero_title": "The Key to Your Exclusive Residence in the Eternal City",
        "hero_subtitle": "Off-market research, confidential negotiation, and privileged access to Rome's most prestigious real estate portfolio.",
        "services_header": "Our Property Finder Service",
        "srv1_title": "🔍 Off-Market Search",
        "srv1_desc": "Access to an invisible portfolio of properties not listed on traditional channels, ensuring absolute exclusivity.",
        "srv2_title": "🤝 Confidential Negotiation",
        "srv2_desc": "Negotiations conducted with the utmost discretion to protect the identity and financial interests of investors.",
        "srv3_title": "🏛️ Architectural Analysis",
        "srv3_desc": "Rigorous assessment of historical constraints, building stratifications, and the conservation status of historic palazzos.",
        "srv4_title": "🗝️ Turnkey Service",
        "srv4_desc": "Comprehensive assistance from property identification to legal, notarial, and interior design aspects.",
        "expertise_header": "Roman Expertise",
        "exp_sub": "Beyond Traditional Agency Boundaries",
        "exp_text": "Understanding the value of a luxury property in Rome requires much more than a simple price-per-square-meter estimate. It requires an encyclopedic knowledge of its historic urban fabric. <br><br>From the ancient Aurelian Walls to noble palaces overlooking Baroque squares. We identify residences that are not just living spaces, but true fragments of the Capital's architectural history.",
        "exp_list_title": "Our Key Neighborhoods",
        "exp_l1": "<b style='color: var(--gold-accent)'>Historic Centre:</b> Trident, Navona, Pantheon.",
        "exp_l2": "<b style='color: var(--gold-accent)'>Parioli & Pinciano:</b> Period residential and elegance.",
        "exp_l3": "<b style='color: var(--gold-accent)'>Aventine Hill:</b> An oasis of silence steps from Circus Maximus.",
        "exp_l4": "<b style='color: var(--gold-accent)'>Trastevere & Janiculum:</b> Bohemian charm and commanding views.",
        "contact_header": "Request a Private Consultation",
        "contact_sub": "Leave your contact details to be reached out to with maximum discretion.",
        "form_name": "Full Name *",
        "form_email": "Email *",
        "form_phone": "Phone Number",
        "form_budget_label": "Investment Range",
        "form_budget_opts": ["Select investment range", "€600,000 - €1,000,000", "€1,000,000 - €2,000,000", "Over €2,000,000"],
        "form_msg": "Specific Requirements (e.g., Terrace, Elevator, Garage)",
        "form_btn": "Send Confidential Request",
        "form_success": "Thank you {name}. Your request has been received with total confidentiality.",
        "form_error": "Please fill in the required fields."
    },
    "fr": {
        "brand": "Rome Luxury Dreams",
        "hero_title": "La Clé de Votre Demeure Exclusive dans la Ville Éternelle",
        "hero_subtitle": "Recherche hors marché, négociation confidentielle et accès privilégié au portefeuille immobilier le plus prestigieux de Rome.",
        "services_header": "Notre Service Property Finder",
        "srv1_title": "🔍 Recherche Hors Marché",
        "srv1_desc": "Accès à un portefeuille invisible de propriétés non publiées sur les canaux traditionnels, garantissant une exclusivité absolue.",
        "srv2_title": "🤝 Négociation Confidentielle",
        "srv2_desc": "Des négociations menées dans la plus grande discrétion pour protéger l'identité et les intérêts financiers des investisseurs.",
        "srv3_title": "🏛️ Analyse Architecturale",
        "srv3_desc": "Évaluation rigoureuse des contraintes historiques, des stratifications et de l'état de conservation des palais d'époque.",
        "srv4_title": "🗝️ Service Clé en Main",
        "srv4_desc": "Assistance complète de l'identification de la propriété aux aspects juridiques, notariaux et de design d'intérieur.",
        "expertise_header": "Expertise Romaine",
        "exp_sub": "Au-delà des Frontières de l'Agence Traditionnelle",
        "exp_text": "Comprendre la valeur d'une propriété de luxe à Rome nécessite bien plus qu'une simple estimation au mètre carré. Cela nécessite une connaissance encyclopédique de son tissu urbain historique. <br><br>Des anciens murs auréliens aux palais nobles surplombant les places baroques. Nous identifions des résidences qui sont de véritables fragments de l'histoire architecturale de la Capitale.",
        "exp_list_title": "Nos Quartiers de Référence",
        "exp_l1": "<b style='color: var(--gold-accent)'>Centre Historique :</b> Trident, Navone, Panthéon.",
        "exp_l2": "<b style='color: var(--gold-accent)'>Parioli & Pinciano :</b> Résidentiel d'époque et élégance.",
        "exp_l3": "<b style='color: var(--gold-accent)'>Aventin :</b> Oasis de silence à deux pas du Circus Maximus.",
        "exp_l4": "<b style='color: var(--gold-accent)'>Trastevere & Janicule :</b> Charme bohème et vues dominantes.",
        "contact_header": "Demander une Consultation Privée",
        "contact_sub": "Laissez vos coordonnées pour être contacté en toute discrétion.",
        "form_name": "Nom et Prénom *",
        "form_email": "Email *",
        "form_phone": "Numéro de Téléphone",
        "form_budget_label": "Budget de Référence",
        "form_budget_opts": ["Sélectionnez la fourchette d'investissement", "600 000 € - 1 000 000 €", "1 000 000 € - 2 000 000 €", "Plus de 2 000 000 €"],
        "form_msg": "Besoins Particuliers (ex. Terrasse, Ascenseur, Garage)",
        "form_btn": "Envoyer une Demande Confidentielle",
        "form_success": "Merci {name}. Votre demande a été reçue en toute confidentialité.",
        "form_error": "Veuillez remplir les champs obligatoires."
    },
    "es": {
        "brand": "Rome Luxury Dreams",
        "hero_title": "La Llave de su Residencia Exclusiva en la Ciudad Eterna",
        "hero_subtitle": "Búsqueda fuera de mercado, negociación confidencial y acceso privilegiado a la cartera inmobiliaria más prestigiosa de Roma.",
        "services_header": "Nuestro Servicio Property Finder",
        "srv1_title": "🔍 Búsqueda Fuera de Mercado",
        "srv1_desc": "Acceso a una cartera invisible de propiedades no publicadas en los canales tradicionales, asegurando exclusividad absoluta.",
        "srv2_title": "🤝 Negociación Confidencial",
        "srv2_desc": "Negociaciones llevadas a cabo con la máxima discreción para proteger la identidad y los intereses financieros de los inversores.",
        "srv3_title": "🏛️ Análisis Arquitectónico",
        "srv3_desc": "Evaluación rigurosa de las restricciones históricas, las estratificaciones de construcción y el estado de los palacios de época.",
        "srv4_title": "🗝️ Servicio Llave en Mano",
        "srv4_desc": "Asistencia integral desde la identificación de la propiedad hasta los aspectos legales, notariales y de diseño de interiores.",
        "expertise_header": "Experiencia Romana",
        "exp_sub": "Más Allá de los Límites de la Agencia Tradicional",
        "exp_text": "Comprender el valor de una propiedad de lujo en Roma requiere mucho más que una simple estimación por metro cuadrado. Requiere un conocimiento enciclopédico de su tejido urbano histórico. <br><br>Desde las antiguas Murallas Aurelianas hasta los palacios nobles con vistas a las plazas barrocas. Identificamos residencias que son verdaderos fragmentos de la historia arquitectónica de la Capital.",
        "exp_list_title": "Nuestros Barrios de Referencia",
        "exp_l1": "<b style='color: var(--gold-accent)'>Centro Histórico:</b> Tridente, Navona, Panteón.",
        "exp_l2": "<b style='color: var(--gold-accent)'>Parioli & Pinciano:</b> Residencial de época y elegancia.",
        "exp_l3": "<b style='color: var(--gold-accent)'>Aventino:</b> Un oasis de silencio a un paso del Circo Máximo.",
        "exp_l4": "<b style='color: var(--gold-accent)'>Trastevere & Janículo:</b> Encanto bohemio y vistas dominantes.",
        "contact_header": "Solicitar una Consulta Privada",
        "contact_sub": "Deje sus datos de contacto para ser contactado con la máxima discreción.",
        "form_name": "Nombre y Apellidos *",
        "form_email": "Correo Electrónico *",
        "form_phone": "Número de Teléfono",
        "form_budget_label": "Presupuesto de Referencia",
        "form_budget_opts": ["Seleccione el rango de inversión", "600.000 € - 1.000.000 €", "1.000.000 € - 2.000.000 €", "Más de 2.000.000 €"],
        "form_msg": "Requisitos Específicos (ej. Terraza, Ascensor, Garaje)",
        "form_btn": "Enviar Solicitud Confidencial",
        "form_success": "Gracias {name}. Su solicitud ha sido recibida con total confidencialidad.",
        "form_error": "Por favor, complete los campos obligatorios."
    },
    "de": {
        "brand": "Rome Luxury Dreams",
        "hero_title": "Der Schlüssel zu Ihrer exklusiven Residenz in der Ewigen Stadt",
        "hero_subtitle": "Off-Market-Suche, vertrauliche Verhandlungen und privilegierter Zugang zum prestigeträchtigsten Immobilienportfolio Roms.",
        "services_header": "Unser Property Finder Service",
        "srv1_title": "🔍 Off-Market-Suche",
        "srv1_desc": "Zugang zu einem unsichtbaren Portfolio von Immobilien, die nicht auf traditionellen Kanälen gelistet sind, was absolute Exklusivität garantiert.",
        "srv2_title": "🤝 Vertrauliche Verhandlungen",
        "srv2_desc": "Die Verhandlungen werden mit äußerster Diskretion geführt, um die Identität und die finanziellen Interessen der Investoren zu schützen.",
        "srv3_title": "🏛️ Architektonische Analyse",
        "srv3_desc": "Strenge Bewertung historischer Auflagen, baulicher Schichtungen und des Erhaltungszustands historischer Palazzi.",
        "srv4_title": "🗝️ Turnkey-Service",
        "srv4_desc": "Umfassende Unterstützung von der Immobilienidentifikation bis hin zu rechtlichen, notariellen und innenarchitektonischen Aspekten.",
        "expertise_header": "Römische Expertise",
        "exp_sub": "Jenseits der Grenzen einer traditionellen Agentur",
        "exp_text": "Den Wert einer Luxusimmobilie in Rom zu verstehen, erfordert viel mehr als eine einfache Schätzung des Quadratmeterpreises. Es erfordert ein enzyklopädisches Wissen über das historische Stadtgefüge. <br><br>Von den antiken Aurelianischen Mauern bis zu den Adelspalästen mit Blick auf barocke Plätze. Wir identifizieren Residenzen, die wahre Fragmente der Architekturgeschichte der Hauptstadt sind.",
        "exp_list_title": "Unsere wichtigsten Viertel",
        "exp_l1": "<b style='color: var(--gold-accent)'>Historisches Zentrum:</b> Dreizack (Tridente), Navona, Pantheon.",
        "exp_l2": "<b style='color: var(--gold-accent)'>Parioli & Pinciano:</b> Historische Wohnviertel und Eleganz.",
        "exp_l3": "<b style='color: var(--gold-accent)'>Aventin:</b> Eine Oase der Stille, nur wenige Schritte vom Circus Maximus entfernt.",
        "exp_l4": "<b style='color: var(--gold-accent)'>Trastevere & Gianicolo:</b> Bohème-Charme und herrliche Aussichten.",
        "contact_header": "Beantragen Sie eine private Beratung",
        "contact_sub": "Hinterlassen Sie Ihre Kontaktdaten, um mit höchster Diskretion kontaktiert zu werden.",
        "form_name": "Vor- und Nachname *",
        "form_email": "E-Mail *",
        "form_phone": "Telefonnummer",
        "form_budget_label": "Investitionsrahmen",
        "form_budget_opts": ["Wählen Sie den Investitionsbereich", "600.000 € - 1.000.000 €", "1.000.000 € - 2.000.000 €", "Über 2.000.000 €"],
        "form_msg": "Besondere Anforderungen (z.B. Terrasse, Aufzug, Garage)",
        "form_btn": "Vertrauliche Anfrage senden",
        "form_success": "Vielen Dank, {name}. Ihre Anfrage wurde streng vertraulich entgegengenommen.",
        "form_error": "Bitte füllen Sie die Pflichtfelder aus."
    },
    "ru": {
        "brand": "Rome Luxury Dreams",
        "hero_title": "Ключ к Вашей Эксклюзивной Резиденции в Вечном Городе",
        "hero_subtitle": "Поиск вне рынка, конфиденциальные переговоры и привилегированный доступ к самому престижному портфелю недвижимости Рима.",
        "services_header": "Наш Сервис Property Finder",
        "srv1_title": "🔍 Поиск Вне Рынка",
        "srv1_desc": "Доступ к невидимому портфелю объектов, не представленных на традиционных каналах, что гарантирует абсолютную эксклюзивность.",
        "srv2_title": "🤝 Конфиденциальные Переговоры",
        "srv2_desc": "Переговоры ведутся с максимальной осмотрительностью для защиты личности и финансовых интересов инвесторов.",
        "srv3_title": "🏛️ Архитектурный Анализ",
        "srv3_desc": "Тщательная оценка исторических ограничений, строительных наслоений и состояния сохранения старинных палаццо.",
        "srv4_title": "🗝️ Сервис Под Ключ",
        "srv4_desc": "Комплексная помощь от выбора объекта до юридических, нотариальных аспектов и дизайна интерьера.",
        "expertise_header": "Римская Экспертиза",
        "exp_sub": "За Пределами Традиционного Агентства",
        "exp_text": "Понимание ценности элитной недвижимости в Риме требует гораздо большего, чем простая оценка стоимости квадратного метра. Оно требует энциклопедических знаний исторической городской структуры. <br><br>От древних Аврелиановых стен до благородных дворцов, выходящих на барочные площади. Мы находим резиденции, которые являются настоящими фрагментами архитектурной истории Столицы.",
        "exp_list_title": "Наши Ключевые Районы",
        "exp_l1": "<b style='color: var(--gold-accent)'>Исторический Центр:</b> Триденте, Навона, Пантеон.",
        "exp_l2": "<b style='color: var(--gold-accent)'>Париоли и Пинчиано:</b> Историческая жилая застройка и элегантность.",
        "exp_l3": "<b style='color: var(--gold-accent)'>Авентин:</b> Оазис тишины в двух шагах от Большого Цирка.",
        "exp_l4": "<b style='color: var(--gold-accent)'>Трастевере и Яникул:</b> Богемный шарм и панорамные виды.",
        "contact_header": "Запросить Частную Консультацию",
        "contact_sub": "Оставьте свои контактные данные, и мы свяжемся с вами с максимальной конфиденциальностью.",
        "form_name": "Имя и Фамилия *",
        "form_email": "Электронная почта *",
        "form_phone": "Номер телефона",
        "form_budget_label": "Инвестиционный Бюджет",
        "form_budget_opts": ["Выберите диапазон инвестиций", "600 000 € - 1 000 000 €", "1 000 000 € - 2 000 000 €", "Более 2 000 000 €"],
        "form_msg": "Особые Пожелания (например, терраса, лифт, гараж)",
        "form_btn": "Отправить Конфиденциальный Запрос",
        "form_success": "Спасибо, {name}. Ваш запрос получен с соблюдением полной конфиденциальности.",
        "form_error": "Пожалуйста, заполните обязательные поля."
    },
    "ar": {
            "brand": "Rome Luxury Dreams",
            "hero_title": "المفتاح لإقامتك الحصرية في المدينة الخالدة",
            "hero_subtitle": "بحث خارج السوق التقليدي، مفاوضات سرية، ووصول استثنائي لأرقى محفظة عقارية في روما.",
            "services_header": "خدمة البحث عن العقارات الخاصة بنا",
            "srv1_title": "🔍 بحث خارج السوق",
            "srv1_desc": "وصول إلى محفظة غير مرئية من العقارات غير المنشورة في القنوات التقليدية، مما يضمن الحصرية المطلقة.",
            "srv2_title": "🤝 مفاوضات سرية",
            "srv2_desc": "مفاوضات تُجرى بأقصى درجات السرية لحماية هوية ومصالح المستثمرين المالية.",
            "srv3_title": "🏛️ تحليل معماري",
            "srv3_desc": "تقييم دقيق للقيود التاريخية، والطبقات البنائية، وحالة الحفظ للقصور التاريخية.",
            "srv4_title": "🗝️ خدمة متكاملة",
            "srv4_desc": "مساعدة شاملة بدءًا من تحديد العقار وحتى الجوانب القانونية، والتوثيق، والتصميم الداخلي.",
            "expertise_header": "خبرتنا في روما",
            "exp_sub": "أبعد من حدود الوكالات التقليدية",
            "exp_text": "إن فهم قيمة العقارات الفاخرة في روما يتطلب أكثر من مجرد تقييم لسعر المتر المربع. إنه يتطلب معرفة موسوعية بنسيجها الحضري التاريخي.<br><br>من الأسوار الأوريليانية القديمة إلى القصور النبيلة المطلة على الساحات الباروكية. نحن نحدد المساكن التي ليست مجرد مساحات معمارية، بل أجزاء حقيقية من تاريخ العاصمة.",
            "exp_list_title": "أهم أحيائنا المرجعية",
            "exp_l1": "<b style='color: var(--gold-accent)'>المركز التاريخي:</b> ترايدنت، نافونا، بانثيون.",
            "exp_l2": "<b style='color: var(--gold-accent)'>باريولي وبينشيانو:</b> عقارات سكنية تاريخية وأناقة عقلانية.",
            "exp_l3": "<b style='color: var(--gold-accent)'>تل أفينتينو:</b> واحة من الصمت على بعد خطوات من سيرك ماكسيموس.",
            "exp_l4": "<b style='color: var(--gold-accent)'>تراستيفيري وجانيكولوم:</b> سحر بوهيمي ومناظر خلابة.",
            "contact_header": "اطلب استشارة خاصة",
            "contact_sub": "اترك بيانات الاتصال الخاصة بك ليتم التواصل معك بأقصى درجات السرية.",
            "form_name": "الاسم واللقب *",
            "form_email": "البريد الإلكتروني *",
            "form_phone": "رقم الهاتف",
            "form_budget_label": "نطاق الاستثمار",
            "form_budget_opts": ["اختر نطاق الاستثمار", "600,000 يورو - 1,000,000 يورو", "1,000,000 يورو - 2,000,000 يورو", "أكثر من 2,000,000 يورو"],
            "form_msg": "متطلبات خاصة (مثل: شرفة، مصعد، مرآب سيارات)",
            "form_btn": "إرسال طلب سري",
            "form_success": "شكرًا لك {name}. تم استلام طلبك بسرية تامة.",
            "form_error": "يرجى ملء الحقول المطلوبة."
        }
    }

# ==========================================
# INIZIALIZZAZIONE STATO (LINGUA)
# ==========================================
if 'language' not in st.session_state:
    st.session_state.language = None # Nessuna lingua scelta all'inizio

def set_language(lang):
    """Callback per impostare la lingua al click del bottone"""
    st.session_state.language = lang

# ==========================================
# FUNZIONE HELPER PER IMMAGINI LOCALI
# ==========================================
def get_base64_of_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as input_file:
            data = input_file.read()
        return f"data:image/png;base64,{base64.b64encode(data).decode()}"
    return "https://via.placeholder.com/150"

# ==========================================
# STILI CSS CUSTOM
# ==========================================
def inject_custom_css():
    custom_css = """
    <style>
        :root {
            --bg-color: #0B132B; 
            --card-bg: #1C2541; 
            --text-main: #F8F9FA;
            --text-muted: #A1A9CE;
            --gold-accent: #D4AF37; 
        }
        .stApp { background-color: var(--bg-color); color: var(--text-main); font-family: 'Helvetica Neue', sans-serif; }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Splash Page Styles */
        .splash-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 70vh;
            text-align: center;
            animation: fadeInUp 1.2s ease-out;
        }
        .splash-logo { width: clamp(150px, 25vw, 220px); margin-bottom: 2rem; filter: drop-shadow(0px 4px 15px rgba(212, 175, 55, 0.4)); }

        /* Stile Bottoni: A tutta pagina, larghi e impilati */
        div.stButton {
            margin-bottom: 1.2rem;
            width: 100%;
        }
        
        /* Hero Section */
        @keyframes slowZoom { 0% { transform: scale(1); } 100% { transform: scale(1.08); } }
        @keyframes fadeInUp { 0% { opacity: 0; transform: translateY(20px); } 100% { opacity: 1; transform: translateY(0); } }
        
        .hero-wrapper {
            position: relative; width: 100%; height: auto; min-height: 520px; border-radius: 12px; overflow: hidden;
            display: flex; align-items: center; justify-content: center; margin-top: 1rem; margin-bottom: 4rem;
            box-shadow: 0 20px 50px rgba(0,0,0,0.6); border: 1px solid rgba(212, 175, 55, 0.15); padding: 3rem 1.5rem;
        }
        .hero-bg {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-image: linear-gradient(180deg, rgba(11,19,43,0.65) 0%, rgba(11,19,43,0.98) 100%), url('https://images.unsplash.com/photo-1552832230-c0197dd311b5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
            background-size: cover; background-position: center center; animation: slowZoom 20s infinite alternate ease-in-out; z-index: 1;
        }
        .hero-content {
            position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; text-align: center;
            max-width: 950px; width: 100%; animation: fadeInUp 1.2s ease-out; background: rgba(11, 19, 43, 0.4);
            border-radius: 16px; padding: 2.5rem 2rem; backdrop-filter: blur(6px); border: 1px solid rgba(255, 255, 255, 0.03);
        }
        .hero-logo-top-container { width: clamp(100px, 20vw, 130px); margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center; }
        .hero-logo-graphic { width: 100%; filter: drop-shadow(0px 4px 12px rgba(212, 175, 55, 0.3)); }
        .hero-brand-text { font-size: clamp(0.9rem, 2vw, 1.1rem); color: var(--gold-accent); text-transform: uppercase; letter-spacing: 6px; margin-bottom: 1.5rem; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 0.5rem; }
        .hero-title { color: #FFFFFF; font-size: clamp(1.8rem, 4.5vw, 3.2rem); font-weight: 300; letter-spacing: 1px; line-height: 1.3; margin-bottom: 1.5rem; text-shadow: 0 4px 15px rgba(0,0,0,0.8); }
        .hero-subtitle { color: var(--text-muted); font-size: clamp(1rem, 2.2vw, 1.3rem); font-weight: 300; line-height: 1.6; max-width: 750px; margin: 0 auto; }
        
        /* Cards */
        .luxury-card { background-color: var(--card-bg); padding: 2rem; border-radius: 10px; border-left: 3px solid var(--gold-accent); height: 100%; transition: all 0.4s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.2); margin-bottom: 1rem; }
        .luxury-card:hover { transform: translateY(-5px); box-shadow: 0 12px 30px rgba(0,0,0,0.4); border-left-width: 6px; }
        .card-title { color: var(--gold-accent); font-size: 1.2rem; font-weight: bold; margin-bottom: 1rem; }
        .card-text { color: var(--text-muted); font-size: 1rem; line-height: 1.5; }
        .section-header { color: var(--gold-accent); font-size: 2.2rem; text-align: center; margin-top: 3rem; margin-bottom: 2.5rem; font-weight: 300; text-transform: uppercase; letter-spacing: 2px; }
        .stMarkdown hr { border: 0; border-top: 1px solid rgba(212, 175, 55, 0.2); margin: 4rem 0; }
        
        /* Stile per i bottoni della lingua */
        div.stButton > button {
            width: 100%;
            background-color: transparent;
            color: var(--gold-accent);
            border: 1px solid var(--gold-accent);
            border-radius: 30px;
            padding: 10px 24px;
            font-size: 1.2rem;
            transition: all 0.3s;
        }
        div.stButton > button:hover {
            background-color: var(--gold-accent);
            color: var(--bg-color);
            border-color: var(--gold-accent);
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# RENDER DELLA SPLASH PAGE (SELEZIONE LINGUA)
# ==========================================
def render_splash_page():
    logo_src = get_base64_of_image("logo.png")
    
    # HTML per centrare verticalmente e mostrare il logo grande
    st.markdown(f"""
        <div class="splash-container">
            <img src="{logo_src}" class="splash-logo" alt="Rome Luxury Dreams">
            <h2 style="color: var(--text-muted); font-weight: 300; letter-spacing: 3px; margin-bottom: 3rem;">SELECT YOUR LANGUAGE</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Due colonne centrate per i pulsanti
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col2:
        st.button("🇮🇹 Italiano", on_click=set_language, args=('it',))
    with col3:
        st.button("🇬🇧 English", on_click=set_language, args=('en',))

# ==========================================
# RENDER DEL SITO PRINCIPALE
# ==========================================
def render_main_site(lang_dict):
    """Rende l'intero sito web utilizzando il dizionario della lingua scelta."""
    logo_src = get_base64_of_image("logo.png")
    
    # --- HERO SECTION ---
    hero_html = f"""
    <div class="hero-wrapper">
        <div class="hero-bg"></div>
        <div class="hero-content">
            <div class="hero-logo-top-container"><img src="{logo_src}" alt="Rome Luxury Dreams Logo" class="hero-logo-graphic"></div>
            <div class="hero-brand-text">{lang_dict['brand']}</div>
            <h1 class="hero-title">{lang_dict['hero_title']}</h1>
            <p class="hero-subtitle">{lang_dict['hero_subtitle']}</p>
        </div>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

    # --- SERVICES SECTION ---
    st.markdown(f"<h2 class='section-header'>{lang_dict['services_header']}</h2>", unsafe_allow_html=True)
    col_1, col_2, col_3, col_4 = st.columns(4)
    with col_1: st.markdown(f'<div class="luxury-card"><div class="card-title">{lang_dict["srv1_title"]}</div><div class="card-text">{lang_dict["srv1_desc"]}</div></div>', unsafe_allow_html=True)
    with col_2: st.markdown(f'<div class="luxury-card"><div class="card-title">{lang_dict["srv2_title"]}</div><div class="card-text">{lang_dict["srv2_desc"]}</div></div>', unsafe_allow_html=True)
    with col_3: st.markdown(f'<div class="luxury-card"><div class="card-title">{lang_dict["srv3_title"]}</div><div class="card-text">{lang_dict["srv3_desc"]}</div></div>', unsafe_allow_html=True)
    with col_4: st.markdown(f'<div class="luxury-card"><div class="card-title">{lang_dict["srv4_title"]}</div><div class="card-text">{lang_dict["srv4_desc"]}</div></div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- EXPERTISE SECTION ---
    st.markdown(f"<h2 class='section-header'>{lang_dict['expertise_header']}</h2>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1, 1])
    with col_left:
        st.markdown(f"""
        <div style="padding: 0.5rem;">
            <h3 style="color: var(--gold-accent); font-weight: 300;">{lang_dict['exp_sub']}</h3>
            <p style="color: var(--text-muted); line-height: 1.8; font-size: 1.1rem; font-weight: 300;">{lang_dict['exp_text']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col_right:
        st.markdown(f"""
        <div class="luxury-card">
            <div class="card-title">{lang_dict['exp_list_title']}</div>
            <ul style="color: var(--text-muted); line-height: 1.9; font-weight: 300; padding-left: 1.2rem;">
                <li>{lang_dict['exp_l1']}</li><li>{lang_dict['exp_l2']}</li><li>{lang_dict['exp_l3']}</li><li>{lang_dict['exp_l4']}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- CONTACT SECTION ---
    st.markdown(f"<h2 class='section-header'>{lang_dict['contact_header']}</h2>", unsafe_allow_html=True)
    spacer_left, form_col, spacer_right = st.columns([1, 2, 1])
    with form_col:
        with st.form(key="private_consultation_form"):
            st.markdown(f"<p style='color: var(--text-muted); text-align: center;'>{lang_dict['contact_sub']}</p>", unsafe_allow_html=True)
            client_name = st.text_input(lang_dict['form_name'])
            client_email = st.text_input(lang_dict['form_email'])
            client_phone = st.text_input(lang_dict['form_phone'])
            client_budget = st.selectbox(lang_dict['form_budget_label'], lang_dict['form_budget_opts'])
            client_message = st.text_area(lang_dict['form_msg'])
            
            submit_button = st.form_submit_button(label=lang_dict['form_btn'])
            if submit_button:
                if client_name and client_email:
                    st.success(lang_dict['form_success'].format(name=client_name))
                else:
                    st.error(lang_dict['form_error'])

# ==========================================
# GESTORE DELLA NAVIGAZIONE (MAIN)
# ==========================================
def main():
    inject_custom_css()
    
    # Se la lingua NON è stata scelta -> Mostra la Landing Page
    if st.session_state.language is None:
        render_splash_page()
    
    # Se la lingua è stata scelta -> Mostra il sito web intero
    else:
        # Prendi il dizionario corretto in base alla lingua (it o en)
        current_lang_dict = TRANSLATIONS[st.session_state.language]
        render_main_site(current_lang_dict)

if __name__ == "__main__":
    main()
