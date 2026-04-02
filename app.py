import streamlit as st
import streamlit.components.v1 as components
import uuid
from pathlib import Path

# =========================================================
# CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="AI Systems — Svetlana Rumyantseva",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSETS_DIR = Path(__file__).parent / "assets"

# =========================================================
# SESSION STATE INIT
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "project_anchor" not in st.session_state:
    st.session_state.project_anchor = ""
if "nav_uid" not in st.session_state:
    st.session_state.nav_uid = uuid.uuid4().hex

# =========================================================
# GLOBAL CSS
# =========================================================
st.markdown("""
<style>
/* ── Hide default Streamlit chrome ──────────────────── */
#MainMenu, footer, header {visibility: hidden;}

/* ── Google Translate: hide widget, keep JS active ─── */
#google_translate_element {display: none !important;}
.goog-te-banner-frame,
.goog-te-balloon-frame,
body > .skiptranslate {display: none !important;}
body {top: 0 !important;}
.goog-tooltip,
.goog-tooltip:hover {display: none !important;}
.goog-text-highlight {background-color: transparent !important; box-shadow: none !important;}

/* ── Header bar ──────────────────────────────────────── */
.header-bar {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 0 10px 0;
    flex-wrap: wrap;
}

/* ── Unified nav / action button ─────────────────────── */
.nav-btn {
    display: inline-block;
    padding: 7px 18px;
    font-size: 14px;
    font-weight: 500;
    border-radius: 6px;
    border: 1px solid #0891b2;
    background: transparent;
    color: #0891b2;
    cursor: pointer;
    text-decoration: none;
    white-space: nowrap;
    transition: background 0.2s, color 0.2s;
}
.nav-btn:hover, .nav-btn.active {
    background: #0891b2;
    color: #fff;
}

/* ── Language selector ────────────────────────────────── */
.lang-select {
    padding: 7px 12px;
    font-size: 14px;
    font-weight: 500;
    border-radius: 6px;
    border: 1px solid #0891b2;
    background: transparent;
    color: #0891b2;
    cursor: pointer;
    outline: none;
}

/* ── Make all Streamlit st.button look the same ──────── */
div[data-testid="stButton"] > button {
    border: 1px solid #0891b2 !important;
    border-radius: 6px !important;
    color: #0891b2 !important;
    background: transparent !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    padding: 7px 18px !important;
    width: 100% !important;
}
div[data-testid="stButton"] > button:hover {
    background: #0891b2 !important;
    color: #fff !important;
}

/* ── Section divider ─────────────────────────────────── */
hr { border: none; border-top: 1px solid #334155; margin: 20px 0; }

/* ── Contact card ────────────────────────────────────── */
.contact-card {
    background: #1e293b;
    border-radius: 10px;
    padding: 18px;
    font-size: 14px;
    line-height: 2;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# GOOGLE TRANSLATE INJECTION
# =========================================================
# Widget is hidden via CSS above; JS is still initialised so
# the programmatic translatePage() calls work correctly.
components.html("""
<div id="google_translate_element"></div>
<script type="text/javascript">
function googleTranslateElementInit() {
    new google.translate.TranslateElement(
        {pageLanguage: 'en', autoDisplay: false},
        'google_translate_element'
    );
}
</script>
<script type="text/javascript"
    src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit">
</script>
<script>
function translatePage(lang) {
    var select = document.querySelector('.goog-te-combo');
    if (select) {
        select.value = lang;
        select.dispatchEvent(new Event('change'));
    }
}
</script>
""", height=0)

# =========================================================
# HELPER: RENDER HEADER
# =========================================================
def render_header():
    current = st.session_state.page

    col_nav, col_lang = st.columns([5, 1])

    with col_nav:
        c_home, c_impl, c_invest, c_chat = st.columns(4)

        with c_home:
            if st.button("🏠 Home", key="nav_home"):
                st.session_state.page = "home"
                st.rerun()

        with c_impl:
            if st.button("✅ Implemented", key="nav_impl"):
                st.session_state.page = "implemented"
                st.rerun()

        with c_invest:
            if st.button("💼 Invest Projects", key="nav_invest"):
                st.session_state.page = "project_choice"
                st.session_state.project_anchor = ""
                st.rerun()

        with c_chat:
            if st.button("🤖 AI Chat", key="nav_chat"):
                st.session_state.page = "chat_ai"
                st.rerun()

    with col_lang:
        lang = st.selectbox(
            label="🌐",
            options=["English", "Русский", "Español", "Deutsch", "中文", "日本語"],
            index=0,
            key="lang_select",
            label_visibility="collapsed",
        )
        lang_map = {
            "English": "en",
            "Русский": "ru",
            "Español": "es",
            "Deutsch": "de",
            "中文": "zh-CN",
            "日本語": "ja",
        }
        if lang != "English":
            components.html(
                f"<script>translatePage('{lang_map[lang]}');</script>",
                height=0,
            )

    st.markdown('<hr>', unsafe_allow_html=True)


# =========================================================
# HELPER: COMPACT CONTACTS (sidebar card on home page)
# =========================================================
def render_compact_contacts():
    st.markdown("""
<div class="contact-card">
<b>Svetlana Rumyantseva</b><br>
AI Developer · Data Scientist<br><br>
📍 Panama<br>
✉️ <a href="mailto:srumyantseva7@gmail.com">srumyantseva7@gmail.com</a><br>
🐙 <a href="https://github.com/Kostratana" target="_blank">github.com/Kostratana</a><br>
🔗 <a href="https://www.linkedin.com/in/svetlana-rumyantseva-5b41962b9/" target="_blank">LinkedIn</a><br>
☕ <a href="https://www.buymeacoffee.com/svetlana_rumyantseva" target="_blank">Buy me a coffee</a>
</div>
""", unsafe_allow_html=True)


# =========================================================
# HELPER: FOOTER
# =========================================================
def render_footer():
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("""
<div style="text-align:center; font-size:13px; color:#94a3b8; padding:10px 0 20px 0;">
    © 2024 Svetlana Rumyantseva · AI Developer · Panama ·
    <a href="mailto:srumyantseva7@gmail.com" style="color:#0891b2;">srumyantseva7@gmail.com</a>
</div>
""", unsafe_allow_html=True)


# =========================================================
# RENDER HEADER ON EVERY PAGE
# =========================================================
render_header()

# =========================================================
# PAGE ROUTER
# =========================================================

# =========================================================
# PAGE: HOME (ГЛАВНАЯ СТРАНИЦА)
# =========================================================
if st.session_state.page == "home":
    st.markdown('', unsafe_allow_html=True)

    left_col, right_col = st.columns([3.2, 1.2], vertical_alignment="top")

    with left_col:
        st.title("AI Systems, Agents, Machine Learning Platforms and Dataset Engineering")
        st.subheader("Applied Artificial Intelligence Systems for Real-World Business Automation")
        st.markdown('<hr>', unsafe_allow_html=True)

        st.markdown("""
This platform presents applied artificial intelligence systems, machine learning models, and AI-driven architectures designed for real-world deployment.

The work focuses on building complete AI systems — not isolated models — combining data processing, machine learning, system architecture, and automation into production-ready solutions.

All presented projects are implemented as working systems with real data, structured pipelines, and practical use cases.
""")

        st.markdown("### Investment Projects — Quick Access")
        c1, c2 = st.columns(2)

        with c1:
            if st.button("P1 — Animal Neuro Health AI", key="home_p1"):
                st.session_state.project_anchor = "proj1"
                st.session_state.page = "project_choice"
                st.session_state.nav_uid = uuid.uuid4().hex
                st.rerun()

            if st.button("P2 — Underwater Hull AI", key="home_p2"):
                st.session_state.project_anchor = "proj2"
                st.session_state.page = "project_choice"
                st.session_state.nav_uid = uuid.uuid4().hex
                st.rerun()

        with c2:
            if st.button("P3 — Body Symmetry Health AI", key="home_p3"):
                st.session_state.project_anchor = "proj3"
                st.session_state.page = "project_choice"
                st.session_state.nav_uid = uuid.uuid4().hex
                st.rerun()

            if st.button("P4 — Behavioral Anomaly AI", key="home_p4"):
                st.session_state.project_anchor = "proj4"
                st.session_state.page = "project_choice"
                st.session_state.nav_uid = uuid.uuid4().hex
                st.rerun()

        st.markdown('<hr>', unsafe_allow_html=True)

        st.markdown("""
**Who This Is For**

This work is relevant for:

• investors looking for scalable AI products and systems  
• companies seeking automation and data-driven solutions  
• teams that need AI integration into existing workflows  
• organizations working with large volumes of unstructured data
""")

    with right_col:
        render_compact_contacts()

    st.markdown('', unsafe_allow_html=True)
    render_footer()

# =========================================================
# PAGE: IMPLEMENTED PROJECTS
# =========================================================
elif st.session_state.page == "implemented":
    st.title("Implemented AI Systems")

    st.markdown("""
This section presents implemented artificial intelligence systems developed as full-cycle engineering projects.

The work focuses on building end-to-end AI systems that operate on real data, not isolated models. Each system includes dataset construction, preprocessing pipelines, model training, evaluation, and integration into functional workflows.

The projects below reflect practical experience in:

• processing large volumes of unstructured data  
• designing AI system architectures  
• building machine learning pipelines  
• combining models with control logic and evaluation layers  
• deploying systems for real-world use cases
""")

    st.markdown('<hr>', unsafe_allow_html=True)
    st.subheader("Computer Vision · Airport Object Detection")
    st.markdown("""
Full-cycle computer vision system for automated object detection at airports.

• dataset collection and annotation (thousands of frames)  
• YOLOv8 training pipeline  
• custom augmentation strategy  
• precision/recall optimisation  
• deployment-ready inference module
""")

    st.markdown('<hr>', unsafe_allow_html=True)
    st.subheader("Logistic Optimisation · Genetic & Ant Colony Algorithms")
    st.markdown("""
Optimisation system for logistics route planning combining genetic algorithms and ant colony optimisation.

• implementation of genetic algorithm with custom operators  
• ant colony simulation with pheromone evaporation  
• comparative benchmarking on real logistic graphs  
• visualisation of convergence and route quality
""")

    st.markdown('<hr>', unsafe_allow_html=True)
    st.subheader("NLP · Text Classification & Processing Pipelines")
    st.markdown("""
End-to-end NLP pipeline for classification of unstructured text data.

• data cleaning and preprocessing  
• feature engineering  
• transformer-based classification  
• evaluation framework with custom metrics
""")

    st.markdown('<hr>', unsafe_allow_html=True)
    render_footer()

# =========================================================
# PAGE: INVEST PROJECTS
# =========================================================
elif st.session_state.page == "project_choice":
    st.title("Invest Projects")

    if st.session_state.project_anchor in {"proj1", "proj2", "proj3", "proj4"}:
        target = st.session_state.project_anchor
        components.html(
            f"""
            <script>
            window.parent.document.getElementById('{target}').scrollIntoView({{behavior: 'smooth'}});
            </script>
            """,
            height=0,
        )
        st.session_state.project_anchor = ""

    # ========================= PROJECT 1 START =========================
    st.markdown('<a name="proj1"></a>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        p1_img = ASSETS_DIR / "animals_project.png"
        if p1_img.exists():
            st.image(str(p1_img), use_container_width=True)
    with col2:
        st.title("AI Animal Neuro & Health Monitoring System")

    st.markdown("""
**AI Animal Neuro & Health Monitoring System** is a deep-tech artificial intelligence platform designed for the diagnosis, analysis, and selection of optimal solutions for the treatment and recovery of animal health.

The platform is based on the understanding that the brain is the central control system in both humans and animals. The analysis of neural activity, behaviour, and physiology makes it possible to identify the true causes of conditions rather than merely observing external symptoms.

**The system is designed for:**  
• diagnosis of diseases  
• detection of hidden issues  
• selection of effective treatment  
• restoration of animal health  

**The platform is applied across key sectors:**  
• veterinary medicine  
• animal husbandry  
• farming and agricultural operations  
• equestrian industry  
• companion animals  

The project is aimed not only at diagnostics but at establishing a new level of care for animal health, improving quality of life, and creating a more harmonious relationship between humans and the living world.

---

**2. Technological Foundation of the System**

The platform is built on the integration of several core technological domains:

*Neuro Analysis*  
• analysis of EEG and neural signals  
• identification of neurophysiological responses  
• detection of hidden internal states  
• correlation between brain activity, behaviour, and health condition  

*Behaviour Analysis (Computer Vision)*  
• recognition of movement and posture  
• detection of abnormal behaviour  
• analysis of micro-signals (stress, pain, anxiety)  

*Physiological Analysis*  
• activity levels  
• movement patterns  
• behavioural rhythms  

*Medical Diagnostics*  
• MRI analysis  
• CT analysis  
• X-ray image analysis  
• detection of pathological conditions  

*AI and Models*  
• neural network diagnostic models  
• multimodal models (integration of all data types)  
• anomaly detection  
• knowledge-based AI (trained on veterinary knowledge)  

---

**3. Core Innovation**

Interpretation of the internal state of an animal through integrated data analysis.

The system identifies the root cause of a condition rather than simply detecting symptoms.

This represents a new class of diagnostics:  
• early detection  
• predictive medicine  
• personalised treatment  

---

**4. Real Market Problems**  
• animals cannot communicate pain  
• diagnosis is often delayed  
• treatment is frequently performed blindly  
• high cost of examinations  
• complexity of diagnostics in the equestrian sector  

*Consequences*  
• losses in agriculture  
• errors in treatment  
• deterioration of animal condition  
• financial losses for owners  

---

**5. Solution**

A unified system for diagnosis and analysis of animal condition.

*Capabilities*  
• early disease detection  
• identification of pain sources  
• condition analysis  
• treatment recommendations  
• recovery monitoring  

---

**6. Data and Knowledge Base**

The system utilises:  
• animal video data  
• physiological data  
• EEG data  
• MRI / CT / X-ray data  
• real clinical case data  
• veterinary books from Moscow veterinary academies  
• scientific research and academic materials  
• consultations with lecturers from Moscow veterinary academies and scientific researchers  
• collaboration and consultations with the Timiryazev Moscow Agricultural Academy  
• requests and acquisition of literature from leading institutions in Europe and the United States (veterinary science, neurophysiology, biology)  
• consultations with international experts and research centres  

*Knowledge Base:*  
• veterinary textbooks  
• scientific research  
• medical protocols  
• data from veterinary academies  
• international scientific materials (Europe, USA)  

*Result*

A unique multimodal dataset is created:  
• behaviour  
• neurophysiology  
• diagnostics  
• medical knowledge  

This becomes:  
• an intellectual asset  
• a competitive advantage  
• a knowledge base  
• a foundation for future projects and developments  

---

**7. Practical Implementation**

The project includes work with:  
• EEG sensors  
• brain activity scanners for animals  
• monitoring systems  
• collection of neurophysiological data  

Work is carried out with:  
• veterinary clinics  
• farms  
• equestrian centres  
• animal owners  
• academics in veterinary science from the Timiryazev Moscow Agricultural Academy  

---

**8. Technical Infrastructure**  
• GPU servers  
• cloud computing  
• real-time data processing  
• large-scale data storage  

*Full AI Development Cycle*  
1. data collection and preparation  
2. data cleaning and structuring  
3. annotation (behaviour, symptoms, pathologies)  
4. creation of training datasets  
5. training neural network models  
6. testing on real-world cases  
7. validation with veterinary professionals  
8. model refinement  
9. optimisation  
10. deployment into the system  
11. continuous retraining with new data  

---

**9. Development Plan (from 12 months)**

*Phase 1 — Research*  
• collection of professional veterinary literature  
• study of animal anatomy  
• study of physiology  
• study of animal psychology, including companion animals  
• analysis of medical histories  
• review of scientific research  
• consultations with professionals  
• collaboration with the Timiryazev Academy  
• interaction with scientific experts in Europe and the United States  
• training models based on expert knowledge, not only literature  

*Phase 2 — Data Collection*  
• collection of animal video data  
• acquisition of MRI / CT / X-ray scans  
• collection of neural signal data  
• acquisition of medical datasets  
• formation of training datasets  

*Phase 3 — AI Development*  
• Computer Vision  
• neural network models  
• development of a full software product  
• creation of a diagnostic system  

*Phase 4 — Neural Integration*  
• EEG analysis  
• linking brain activity to health condition  

*Phase 5 — System Integration*  
• integration of all components  
• development of a unified platform  

*Phase 6 — Testing*  
• testing on real animals  
• accuracy validation  
• system refinement  

---

**10. Market**

The system applies across all sectors involving animals:  
• veterinary clinics  
• equestrian industry  
• farms  
• agriculture  
• pet owners  
• breeding centres  
• wildlife reserves  
• government bodies (ministries of agriculture and livestock development)  

---

**11. Revenue Model**

Revenue is generated through:  
• software sales  
• subscription model  
• system implementation  

*Clients*  
• veterinary clinics  
• farms  
• equestrian centres  
• private animal owners  
• government organisations  

---

**12. Team**

*Founder and Lead Developer*

• core development is carried out personally  
• centralised strategic management  

*Specialists involved:*  
• AI engineers  
• software developers  
• data scientists  
• world-class scientific professionals  

*Scientific Support*  
• neurophysiologists of international level  
• experienced veterinarians  
• professors from Moscow veterinary academies  

---

**13. Finance and Investment**

Required investment: **$300,000 – $400,000**

*Allocation*

Equipment — $60K–90K  
• EEG  
• sensors  
• video systems  

Data — $40K–70K  
• MRI  
• CT  
• X-ray  
• video  

Knowledge — $20K–40K  
• professional literature  
• scientific materials  

Infrastructure — $40K–80K  
• GPUs  
• cloud systems  

Development — $80K–120K  
• engineering team  

Research — $30K–50K  
• work with animals  
• data collection  

---

**14. ROI for Investors**  
• break-even: 18–24 months  
• high margins  
• scalability  

Expected outcome: **ROI: 5x – 10x within 3–5 years**
""")
    # ========================= PROJECT 1 END =========================

    # ========================= PROJECT 2 START =========================
    st.markdown('<a name="proj2"></a>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        p2_img = ASSETS_DIR / "underwater_resized.png"
        if p2_img.exists():
            st.image(str(p2_img), use_container_width=True)
    with col2:
        st.title("AI Underwater Hull Inspection & Safety Monitoring System")

    st.markdown("""
**AI Underwater Hull Inspection & Safety Monitoring System** is an advanced deep-tech platform combining autonomous underwater robotics with artificial intelligence for real-time inspection, fault detection, and structural integrity monitoring of ship hulls and underwater infrastructure.

**The system is designed for:**  
• autonomous hull inspection without dry-docking  
• real-time defect and corrosion detection  
• structural risk assessment  
• predictive maintenance scheduling  
• underwater safety monitoring  

**The platform is applied across key sectors:**  
• commercial shipping and maritime transport  
• naval defence  
• offshore oil & gas infrastructure  
• port and harbour management  
• underwater pipeline inspection  

---

**2. Technological Foundation**

*Computer Vision & Deep Learning*  
• underwater image enhancement (dehazing, colour correction)  
• defect detection via custom-trained neural networks  
• semantic segmentation of hull surfaces  
• anomaly localisation and classification  

*Autonomous Robotics (ROV / AUV)*  
• real-time navigation under the hull  
• sensor fusion (sonar, optical, ultrasonic)  
• automated path planning for full coverage  

*Structural Analysis*  
• corrosion severity grading  
• crack propagation tracking  
• thickness loss estimation  
• risk score generation  

---

**3. Core Innovation**

AI-driven inspection without human divers or dry-dock downtime.

The system reduces inspection costs by up to 70% and enables continuous monitoring rather than periodic manual checks.

---

**4. Real Market Problems**  
• ship hull inspections require expensive dry-docking  
• manual diver inspections are dangerous and costly  
• defects detected late lead to catastrophic failures  
• regulatory compliance is increasingly demanding  

*Consequences*  
• vessel downtime and lost revenue  
• environmental disasters from hull breaches  
• insurance and liability costs  
• safety risks to crew and cargo  

---

**5. Market**  
• 50,000+ commercial vessels globally  
• offshore platforms and pipelines  
• naval fleets  
• port authorities  

---

**6. Finance and Investment**

Required investment: **$250,000 – $350,000**

*Allocation*  
Robotics hardware — $80K–120K  
AI development — $70K–100K  
Data collection & annotation — $40K–60K  
Infrastructure & cloud — $30K–50K  
Research & testing — $30K–50K  

Expected outcome: **ROI: 4x – 8x within 3–5 years**
""")
    # ========================= PROJECT 2 END =========================

    # ========================= PROJECT 3 START =========================
    st.markdown('<a name="proj3"></a>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        p3_img = ASSETS_DIR / "ai_body_symmetry_1536x1024.png"
        if p3_img.exists():
            st.image(str(p3_img), use_container_width=True)
    with col2:
        st.title("AI Human Body Symmetry & Health Detection System")

    st.markdown("""
**AI Human Body Symmetry & Health Detection System** is an artificial intelligence platform that analyses the human body's structural symmetry to detect postural imbalances, musculoskeletal conditions, and early-stage health deviations.

**The system is designed for:**  
• postural and symmetry analysis  
• detection of musculoskeletal imbalances  
• early identification of spinal and joint conditions  
• personalised rehabilitation planning  
• sports performance optimisation  

**The platform is applied across key sectors:**  
• rehabilitation clinics  
• sports medicine  
• physiotherapy  
• fitness and wellness  
• preventive healthcare  

---

**2. Technological Foundation**

*Computer Vision*  
• full-body pose estimation (2D and 3D)  
• landmark detection (joints, spine, pelvis alignment)  
• left-right symmetry scoring  
• temporal analysis (movement patterns over time)  

*AI Diagnostics*  
• deviation classification by severity  
• correlation with known musculoskeletal conditions  
• personalised health risk scoring  
• recommendation engine for corrective exercises  

---

**3. Core Innovation**

Non-invasive body symmetry diagnostics using a standard camera — no specialised equipment required.

Early detection of conditions before symptoms become clinical.

---

**4. Real Market Problems**  
• musculoskeletal disorders affect 1.7 billion people globally  
• early diagnosis is rare due to cost and access barriers  
• sports injuries often result from undetected imbalances  
• rehabilitation lacks objective measurement tools  

---

**5. Finance and Investment**

Required investment: **$200,000 – $300,000**

Expected outcome: **ROI: 5x – 9x within 3–4 years**
""")
    # ========================= PROJECT 3 END =========================

    # ========================= PROJECT 4 START =========================
    st.markdown('<a name="proj4"></a>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        p4_img = ASSETS_DIR / "ai_anomaly_1536x1024.png"
        if p4_img.exists():
            st.image(str(p4_img), use_container_width=True)
    with col2:
        st.title("AI Behavioral & Anomaly Detection System")

    st.markdown("""
**AI Behavioral & Anomaly Detection System** is an artificial intelligence platform for real-time detection of anomalous behaviour, unusual patterns, and security-relevant events across video streams, sensor networks, and data feeds.

**The system is designed for:**  
• real-time behavioural anomaly detection  
• security and threat identification  
• process deviation monitoring  
• fraud and irregularity detection  
• predictive event alerting  

**The platform is applied across key sectors:**  
• security and surveillance  
• industrial process monitoring  
• financial fraud detection  
• transport and logistics safety  
• smart city infrastructure  

---

**2. Technological Foundation**

*Anomaly Detection Models*  
• unsupervised learning on normal behaviour baselines  
• real-time deviation scoring  
• multi-sensor data fusion  
• temporal pattern analysis  

*Computer Vision*  
• crowd behaviour analysis  
• individual trajectory tracking  
• action recognition  
• zone intrusion detection  

*Data Stream Processing*  
• low-latency inference pipeline  
• edge deployment capability  
• cloud-based alert management  

---

**3. Core Innovation**

Learning what is normal and detecting deviations automatically — without manual rule definition.

The system adapts to new environments and continuously refines its baseline models.

---

**4. Real Market Problems**  
• manual monitoring is inefficient and error-prone  
• rule-based systems miss novel threats  
• false alarm rates are high in legacy systems  
• real-time response requires automation  

---

**5. Finance and Investment**

Required investment: **$200,000 – $280,000**

Expected outcome: **ROI: 5x – 8x within 3–4 years**
""")
    # ========================= PROJECT 4 END =========================

    render_footer()

# =========================================================
# PAGE: CHAT AI
# =========================================================
elif st.session_state.page == "chat_ai":
    st.title("AI Chat System")

    st.markdown("""
An intelligent conversational AI system integrated into the platform to assist investors, partners, and clients in exploring projects, understanding technical details, and navigating the system.

**Capabilities:**  
• answer questions about all presented AI projects  
• explain technical architecture and investment details  
• provide personalised project recommendations  
• assist with contact and collaboration inquiries  

*This module is currently in active development.*
""")

    render_footer()

# =========================================================
# FALLBACK
# =========================================================
else:
    st.session_state.page = "home"
    st.rerun()
