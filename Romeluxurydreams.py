import streamlit as st
import base64
import os

# ==========================================
# CONFIGURAZIONE PAGINA
# ==========================================
st.set_page_config(
    page_title="Property Finder Roma | Residenze Esclusive | Rome Luxury Dreams",
    page_icon="🗝️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# FUNZIONE HELPER PER IMMAGINI LOCALI
# ==========================================
def get_base64_of_image(image_path):
    """Legge un'immagine locale e la converte in stringa Base64 per l'HTML."""
    with open(image_path, "rb") as input_file:
        data = input_file.read()
    return base64.b64encode(data).decode()

# ==========================================
# STILI CSS CUSTOM (LUXURY & MOBILE RESPONSIVE)
# ==========================================
def inject_custom_css():
    """Inietta il CSS ottimizzato per la massima responsività su iPhone e iPad."""
    custom_css = """
    <style>
        /* Palette e Setup Globale */
        :root {
            --bg-color: #0B132B; 
            --card-bg: #1C2541; 
            --text-main: #F8F9FA;
            --text-muted: #A1A9CE;
            --gold-accent: #D4AF37; 
        }
        
        .stApp {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Animazioni */
        @keyframes slowZoom {
            0% { transform: scale(1); }
            100% { transform: scale(1.08); }
        }
        @keyframes fadeInUp {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        
        /* =========================================
           Hero Section Verticale & Responsiva
           ========================================= */
        .hero-wrapper {
            position: relative;
            width: 100%;
            height: auto;
            min-height: 520px;
            border-radius: 12px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 1rem;
            margin-bottom: 4rem;
            box-shadow: 0 20px 50px rgba(0,0,0,0.6);
            border: 1px solid rgba(212, 175, 55, 0.15);
            padding: 3rem 1.5rem; /* Padding di sicurezza per schermi mobile */
        }

        .hero-bg {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: linear-gradient(180deg, rgba(11,19,43,0.65) 0%, rgba(11,19,43,0.98) 100%), url('https://images.unsplash.com/photo-1552832230-c0197dd311b5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center center;
            animation: slowZoom 20s infinite alternate ease-in-out;
            z-index: 1;
        }

        /* Contenitore ad albero (Layout in colonna centrato) */
        .hero-content {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column; /* Forza la disposizione verticale */
            align-items: center;     /* Centra orizzontalmente il logo e il testo */
            text-align: center;      /* Centra i testi internamente */
            max-width: 950px;
            width: 100%;
            animation: fadeInUp 1.2s ease-out;
            background: rgba(11, 19, 43, 0.4);
            border-radius: 16px;
            padding: 2.5rem 2rem;
            backdrop-filter: blur(6px);
            border: 1px solid rgba(255, 255, 255, 0.03);
        }

        /* Contenitore Logo Superiore */
        .hero-logo-top-container {
            width: clamp(100px, 20vw, 130px); /* Si ridimensiona fluidamente su iPhone */
            height: auto;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .hero-logo-graphic {
            width: 100%;
            height: auto;
            filter: drop-shadow(0px 4px 12px rgba(212, 175, 55, 0.3));
        }

        /* Testo Brand sotto il logo grafico */
        .hero-brand-text {
            font-size: clamp(0.9rem, 2vw, 1.1rem);
            color: var(--gold-accent);
            text-transform: uppercase;
            letter-spacing: 6px;
            margin-bottom: 1.5rem;
            font-weight: 500;
            border-bottom: 1px solid rgba(212, 175, 55, 0.3);
            padding-bottom: 0.5rem;
        }
        
        /* Titolo e Sottotitolo Fluidi (Mai giganti su mobile, imponenti su desktop) */
        .hero-title {
            color: #FFFFFF;
            font-size: clamp(1.8rem, 4.5vw, 3.2rem); 
            font-weight: 300;
            letter-spacing: 1px;
            line-height: 1.3;
            margin-bottom: 1.5rem;
            text-shadow: 0 4px 15px rgba(0,0,0,0.8);
        }
        
        .hero-subtitle {
            color: var(--text-muted);
            font-size: clamp(1rem, 2.2vw, 1.3rem);
            font-weight: 300;
            line-height: 1.6;
            max-width: 750px;
            margin: 0 auto;
        }
        
        /* =========================================
           Cards e Sezioni (Invariati e stabili)
           ========================================= */
        .luxury-card {
            background-color: var(--card-bg);
            padding: 2rem;
            border-radius: 10px;
            border-left: 3px solid var(--gold-accent);
            height: 100%;
            transition: all 0.4s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-bottom: 1rem; /* Sicurezza per il wrapping mobile */
        }
        .luxury-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 30px rgba(0,0,0,0.4);
            border-left-width: 6px;
        }
        .card-title {
            color: var(--gold-accent);
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .card-text {
            color: var(--text-muted);
            font-size: 1rem;
            line-height: 1.5;
        }
        .section-header {
            color: var(--gold-accent);
            font-size: 2.2rem;
            text-align: center;
            margin-top: 3rem;
            margin-bottom: 2.5rem;
            font-weight: 300;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .stMarkdown hr {
            border: 0;
            border-top: 1px solid rgba(212, 175, 55, 0.2);
            margin: 4rem 0;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# COMPONENTI DELLA PAGINA
# ==========================================
def render_hero_section():
    """Rende il banner hero strutturato verticalmente con logo centrato in alto."""
    logo_path = "logo.png" 
    
    # Rilevamento dinamico del logo locale (Base64)
    if os.path.exists(logo_path):
        base64_str = get_base64_of_image(logo_path)
        logo_src = f"data:image/png;base64,{base64_str}"
    else:
        # Fallback elegante se dimentichi temporaneamente di fare il push di logo.png
        logo_src = "https://via.placeholder.com/150" 
    
    hero_html = f"""
    <div class="hero-wrapper">
        <div class="hero-bg"></div>
        <div class="hero-content">
            <div class="hero-logo-top-container">
                <img src="{logo_src}" alt="Rome Luxury Dreams Logo" class="hero-logo-graphic">
            </div>
            <div class="hero-brand-text">Rome Luxury Dreams</div>
            <h1 class="hero-title">La Chiave per la Tua Dimora Esclusiva nella Città Eterna</h1>
            <p class="hero-subtitle">Ricerca off-market, negoziazione riservata e accesso privilegiato al patrimonio immobiliare più prestigioso di Roma.</p>
        </div>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

def render_services_section():
    """Rende la sezione 'Come Funziona' con layout adattivo."""
    st.markdown("<h2 class='section-header'>Il Servizio Property Finder</h2>", unsafe_allow_html=True)
    col_1, col_2, col_3, col_4 = st.columns(4)
    
    with col_1:
        st.markdown('<div class="luxury-card"><div class="card-title">🔍 Ricerca Off-Market</div><div class="card-text">Accesso a un portfolio invisibile di proprietà non pubblicate sui canali tradizionali, garantendo esclusività assoluta.</div></div>', unsafe_allow_html=True)
    with col_2:
        st.markdown('<div class="luxury-card"><div class="card-title">🤝 Negoziazione Riservata</div><div class="card-text">Trattative condotte nel massimo riserbo per proteggere l\'identità e gli interessi finanziari di investitori e HNWI.</div></div>', unsafe_allow_html=True)
    with col_3:
        st.markdown('<div class="luxury-card"><div class="card-title">🏛️ Analisi Architettonica</div><div class="card-text">Valutazione rigorosa di vincoli storici, stratificazioni edilizie e stato conservativo dei palazzi d\'epoca.</div></div>', unsafe_allow_html=True)
    with col_4:
        st.markdown('<div class="luxury-card"><div class="card-title">🗝️ Servizio Chiavi in Mano</div><div class="card-text">Assistenza completa dall\'individuazione dell\'immobile fino agli aspetti legali, notarili e di interior design.</div></div>', unsafe_allow_html=True)

def render_expertise_section():
    """Rende la sezione dedicata alla conoscenza storica di Roma."""
    st.markdown("<h2 class='section-header'>Expertise Romana</h2>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("""
        <div style="padding: 0.5rem;">
            <h3 style="color: var(--gold-accent); font-weight: 300;">Oltre i Confini dell'Agenzia Tradizionale</h3>
            <p style="color: var(--text-muted); line-height: 1.8; font-size: 1.1rem; font-weight: 300;">
                Comprendere il valore di un immobile di lusso a Roma richiede molto più di una semplice stima al metro quadro. Richiede una conoscenza enciclopedica del suo tessuto urbano storico. <br><br>
                Dalle antiche Mura Aureliane ai palazzi nobiliari affacciati sulle piazze barocche, fino alle dimore nascoste nei vicoli adiacenti a Ponte Sisto. Identifichiamo residenze che non sono solo spazi abitativi, ma veri e propri frammenti della storia architettonica della Capitale.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_right:
        st.markdown("""
        <div class="luxury-card">
            <div class="card-title">I Nostri Quartieri di Riferimento</div>
            <ul style="color: var(--text-muted); line-height: 1.9; font-weight: 300; padding-left: 1.2rem;">
                <li><b style="color: var(--gold-accent)">Centro Storico:</b> Tridente, Navona, Pantheon.</li>
                <li><b style="color: var(--gold-accent)">Parioli & Pinciano:</b> Residenziale d'epoca ed eleganza razionalista.</li>
                <li><b style="color: var(--gold-accent)">Aventino:</b> Oasi di silenzio a un passo dal Circo Massimo.</li>
                <li><b style="color: var(--gold-accent)">Trastevere & Gianicolo:</b> Fascino bohémien e viste dominanti.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def render_contact_section():
    """Rende il modulo di contatto protetto da st.form."""
    st.markdown("<h2 class='section-header'>Richiedi una Consulenza Privata</h2>", unsafe_allow_html=True)
    spacer_left, form_col, spacer_right = st.columns([1, 2, 1])
    
    with form_col:
        with st.form(key="private_consultation_form"):
            st.markdown("<p style='color: var(--text-muted); text-align: center;'>Lascia i tuoi recapiti per essere contattato con la massima discrezione.</p>", unsafe_allow_html=True)
            client_name = st.text_input("Nome e Cognome *")
            client_email = st.text_input("Email *")
            client_phone = st.text_input("Recapito Telefonico")
            
            budget_options = ["Seleziona il range d'investimento", "600.000 € - 1.000.000 €", "1.000.000 € - 2.000.000 €", "Oltre 2.000.000 €"]
            client_budget = st.selectbox("Budget di Riferimento", budget_options)
            client_message = st.text_area("Esigenze Particolari (es. Terrazza, Ascensore, Box auto)")
            
            submit_button = st.form_submit_button(label="Invia Richiesta Riservata")
            if submit_button:
                if client_name and client_email:
                    st.success(f"Grazie {client_name}. La tua richiesta è stata recepita in totale riservatezza. Verrai contattato a breve.")
                else:
                    st.error("Per favore, compila i campi obbligatori (Nome e Email).")

# ==========================================
# MAIN EXECUTION
# ==========================================
def main():
    inject_custom_css()
    render_hero_section()
    render_services_section()
    st.markdown("<hr>", unsafe_allow_html=True)
    render_expertise_section()
    st.markdown("<hr>", unsafe_allow_html=True)
    render_contact_section()

if __name__ == "__main__":
    main()
