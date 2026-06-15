import streamlit as st

# ==========================================
# CONFIGURAZIONE PAGINA
# ==========================================
st.set_page_config(
    page_title="Property Finder Roma | Residenze Esclusive",
    page_icon="🗝️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# STILI CSS CUSTOM (LUXURY THEME)
# ==========================================
def inject_custom_css():
    """Inietta il CSS per la UI/UX di lusso, con animazioni avanzate per la Hero Section."""
    custom_css = """
    <style>
        /* =========================================
           Palette e Setup Globale
           ========================================= */
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
        
        /* =========================================
           Animazioni Dinamiche
           ========================================= */
        @keyframes slowZoom {
            0% { transform: scale(1); }
            100% { transform: scale(1.1); }
        }

        @keyframes fadeInUp {
            0% { opacity: 0; transform: translateY(30px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        @keyframes glow {
            0% { text-shadow: 0 0 10px rgba(212, 175, 55, 0.2); }
            50% { text-shadow: 0 0 20px rgba(212, 175, 55, 0.6); }
            100% { text-shadow: 0 0 10px rgba(212, 175, 55, 0.2); }
        }
        
        /* =========================================
           Nuova Hero Section (Banner Rettangolare)
           ========================================= */
        .hero-wrapper {
            position: relative;
            width: 100%;
            height: 55vh; /* Proporzione rettangolare dinamica */
            min-height: 450px;
            border-radius: 12px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 1rem;
            margin-bottom: 4rem;
            box-shadow: 0 20px 50px rgba(0,0,0,0.6);
            border: 1px solid rgba(212, 175, 55, 0.15); /* Sottile bordo dorato */
        }

        /* Sfondo con immagine di Roma, Overlay Scuro ed Effetto Zoom */
        .hero-bg {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            /* Immagine di architettura classica con gradiente blu/antracite */
            background-image: linear-gradient(180deg, rgba(11,19,43,0.6) 0%, rgba(11,19,43,0.95) 100%), url('https://images.unsplash.com/photo-1552832230-c0197dd311b5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center 30%;
            animation: slowZoom 25s infinite alternate ease-in-out;
            z-index: 1;
        }

        /* Contenitore Testo sopra lo sfondo */
        .hero-content {
            position: relative;
            z-index: 2;
            text-align: center;
            padding: 2rem 4rem;
            max-width: 1000px;
            animation: fadeInUp 1.5s ease-out;
            background: rgba(11, 19, 43, 0.3);
            border-radius: 16px;
            backdrop-filter: blur(4px); /* Effetto vetro elegante */
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        /* Scritta Coordinata: Rome Luxury Dreams */
        .hero-logo {
            font-size: 1.1rem;
            color: var(--gold-accent);
            text-transform: uppercase;
            letter-spacing: 8px;
            margin-bottom: 1.5rem;
            font-weight: 500;
            display: inline-block;
            border-bottom: 1px solid rgba(212, 175, 55, 0.5);
            padding-bottom: 0.5rem;
            animation: glow 4s infinite;
        }
        
        .hero-title {
            color: #FFFFFF;
            font-size: 3.2rem;
            font-weight: 300;
            letter-spacing: 1px;
            line-height: 1.2;
            margin-bottom: 1.5rem;
            text-shadow: 0 4px 15px rgba(0,0,0,0.8);
        }
        
        .hero-subtitle {
            color: var(--text-muted);
            font-size: 1.3rem;
            font-weight: 300;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
        }
        
        /* =========================================
           Stili Cards e Sezioni
           ========================================= */
        .luxury-card {
            background-color: var(--card-bg);
            padding: 2rem;
            border-radius: 10px;
            border-left: 3px solid var(--gold-accent);
            height: 100%;
            transition: all 0.4s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .luxury-card:hover {
            transform: translateY(-8px);
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
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def render_hero_section():
    """Rende il banner dinamico e coordinato della Hero Section."""
    hero_html = """
    <div class="hero-wrapper">
        <div class="hero-bg"></div>
        <div class="hero-content">
            <div class="hero-logo">Rome Luxury Dreams</div>
            <h1 class="hero-title">La Chiave per la Tua Dimora Esclusiva nella Città Eterna</h1>
            <p class="hero-subtitle">Ricerca off-market, negoziazione riservata e accesso privilegiato al patrimonio immobiliare più prestigioso di Roma.</p>
        </div>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)


def render_services_section():
    """Rende la sezione 'Come Funziona' con layout a colonne."""
    st.markdown("<h2 class='section-header'>Il Servizio Property Finder</h2>", unsafe_allow_html=True)
    
    col_1, col_2, col_3, col_4 = st.columns(4)
    
    with col_1:
        st.markdown("""
        <div class="luxury-card">
            <div class="card-title">🔍 Ricerca Off-Market</div>
            <div class="card-text">Accesso a un portfolio invisibile di proprietà non pubblicate sui canali tradizionali, garantendo esclusività assoluta.</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_2:
        st.markdown("""
        <div class="luxury-card">
            <div class="card-title">🤝 Negoziazione Riservata</div>
            <div class="card-text">Trattative condotte nel massimo riserbo per proteggere l'identità e gli interessi finanziari di investitori e HNWI.</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_3:
        st.markdown("""
        <div class="luxury-card">
            <div class="card-title">🏛️ Analisi Architettonica</div>
            <div class="card-text">Valutazione rigorosa di vincoli storici, stratificazioni edilizie e stato conservativo dei palazzi d'epoca.</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_4:
        st.markdown("""
        <div class="luxury-card">
            <div class="card-title">🗝️ Servizio Chiavi in Mano</div>
            <div class="card-text">Assistenza completa dall'individuazione dell'immobile fino agli aspetti legali, notarili e di interior design.</div>
        </div>
        """, unsafe_allow_html=True)

def render_expertise_section():
    """Rende la sezione dedicata alla conoscenza del tessuto storico e urbanistico di Roma."""
    st.markdown("<h2 class='section-header'>Expertise Romana</h2>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("""
        <div style="padding: 1rem;">
            <h3 style="color: #D4AF37;">Oltre i Confini dell'Agenzia Tradizionale</h3>
            <p style="color: #A1A9CE; line-height: 1.6; font-size: 1.1rem;">
                Comprendere il valore di un immobile di lusso a Roma richiede molto più di una semplice stima al metro quadro. Richiede una conoscenza enciclopedica del suo tessuto urbano storico. <br><br>
                Dalle antiche Mura Aureliane ai palazzi nobiliari affacciati sulle piazze barocche, fino alle dimore nascoste nei vicoli adiacenti a Ponte Sisto. Identifichiamo residenze che non sono solo spazi abitativi, ma veri e propri frammenti della storia architettonica della Capitale.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_right:
        st.markdown("""
        <div class="luxury-card">
            <div class="card-title">I Nostri Quartieri di Riferimento</div>
            <ul style="color: #A1A9CE; line-height: 1.8;">
                <li><b>Centro Storico (Tridente, Navona, Pantheon):</b> Attici panoramici e piani nobili affrescati.</li>
                <li><b>Parioli & Pinciano:</b> Ville indipendenti, architettura razionalista ed eleganza residenziale.</li>
                <li><b>Aventino:</b> Residenze circondate dal verde e dal silenzio, a un passo dal Circo Massimo.</li>
                <li><b>Trastevere & Gianicolo:</b> Proprietà dal fascino bohémien con terrazze dominanti sulla città.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def render_contact_section():
    """Rende il modulo di contatto per la consulenza privata, mantenendo coerenza formale."""
    st.markdown("<h2 class='section-header'>Richiedi una Consulenza Privata</h2>", unsafe_allow_html=True)
    
    # Layout centrato per il form
    spacer_left, form_col, spacer_right = st.columns([1, 2, 1])
    
    with form_col:
        with st.form(key="private_consultation_form"):
            st.markdown("<p style='color: #A1A9CE; text-align: center;'>Lascia i tuoi recapiti per essere contattato con la massima discrezione.</p>", unsafe_allow_html=True)
            
            client_name = st.text_input("Nome e Cognome *")
            client_email = st.text_input("Email *")
            client_phone = st.text_input("Recapito Telefonico")
            
            budget_options = [
                "Seleziona il range d'investimento", 
                "600.000 € - 1.000.000 €", 
                "1.000.000 € - 2.000.000 €", 
                "Oltre 2.000.000 €"
            ]
            client_budget = st.selectbox("Budget di Riferimento", budget_options)
            
            client_message = st.text_area("Esigenze Particolari (es. Terrazza, Ascensore, Box auto)")
            
            submit_button = st.form_submit_button(label="Invia Richiesta Riservata")
            
            if submit_button:
                if client_name and client_email:
                    # Logica di invio backend (es. email via smtplib o API webhook) andrebbe inserita qui
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
    st.markdown("---")
    render_expertise_section()
    st.markdown("---")
    render_contact_section()

if __name__ == "__main__":
    main()
