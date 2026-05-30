import streamlit as st
import pandas as pd
import json
from io import BytesIO
from core_utils import read_universal_file, ask_groq, create_word_report

# ----------------------------------------------------
# 🪐 CONFIGURAÇÃO ESTÉTICA PREMIUM (CYBER-MINIMALIST)
# ----------------------------------------------------
st.set_page_config(page_title="ARCHINTEL // LAB", page_icon="📐", layout="wide")

# Custom CSS para hackear o Streamlit e deixá-lo com aspeto de software de milhões
st.markdown("""
<style>
    /* Fundo geral escuro profundo */
    .stApp {
        background-color: #0B0F19;
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Customização da Sidebar */
    [data-testid="stSidebar"] {
        background-color: #05070C !important;
        border-right: 1px solid #1E293B;
    }
    
    /* Títulos em Neon Ciano Metálico */
    h1, h2, h3 {
        color: #00F2FE !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
        text-transform: uppercase;
    }
    
    /* Subtítulos e Labels em Dourado Champagne */
    .stSlider label, .stSelectbox label, .stTextInput label, .stTextArea label, .stFileUploader label {
        color: #F59E0B !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        font-size: 0.8rem;
        letter-spacing: 1px;
    }

    /* Input Boxes Estilo Futurista */
    div[data-baseweb="input"], div[data-baseweb="select"], div[data-baseweb="textarea"] {
        background-color: #141B2D !important;
        border: 1px solid #2D3748 !important;
        border-radius: 4px !important;
        color: #FFFFFF !important;
    }
    
    /* Botões Premium com Efeito Glow */
    .stButton>button {
        background: linear-gradient(90deg, #0072FF 0%, #00F2FE 100%) !important;
        color: #05070C !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.6rem 2rem !important;
        box-shadow: 0vw 0vw 1vw rgba(0, 242, 254, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0vw 0vw 2vw rgba(0, 242, 254, 0.8);
    }
    
    /* Caixas de Chat e Resultados */
    .block-container .element-container div.stMarkdown {
        background-color: #0F172A;
        padding: 1.5rem;
        border-left: 4px solid #00F2FE;
        border-radius: 4px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_html=True)

# ----------------------------------------------------
# 💾 PERSISTÊNCIA SIMPLES EM MEMÓRIA (PROMPTS DE OURO)
# ----------------------------------------------------
if "prompts_biblioteca" not in st.session_state:
    st.session_state.prompts_biblioteca = {
        "Auditoria de Margem de Obra": "Analise os custos deste orçamento e encontre os 3 itens com maior probabilidade de superfaturamento ou desvio técnico.",
        "Conformidade de Caixilharia": "Verifique se as especificações de vidros e caixilharias atendem aos requisitos de isolamento acústico e térmico classe A.",
        "Análise Rápida de Terreno": "Com base na descrição do terreno, liste as principais restrições físicas (fundações, inclinação, lençol freático) a considerar."
    }

if "chat_arquitetura_history" not in st.session_state:
    st.session_state.chat_arquitetura_history = []

# ----------------------------------------------------
# 🧭 NAVEGAÇÃO CENTRAL (SIDEBAR FUTURISTA)
# ----------------------------------------------------
st.sidebar.markdown("<h2 style='color:#00F2FE; text-align:center;'>ARCHINTEL // HUB</h2>", unsafe_html=True)
st.sidebar.markdown("<p style='text-align:center; font-size:0.8rem; color:#64748B;'>OS SYSTEM V1.0</p>", unsafe_html=True)
st.sidebar.markdown("---")

modulo = st.sidebar.radio(
    "SELECIONE O MÓDULO OPERACIONAL",
    [
        "🟦 MÓDULO 1: Triagem Inteligente",
        "🟩 MÓDULO 2: Engenharia de Prompts",
        "🟩 MÓDULO 3: Agente IA Consultor",
        "🟪 MÓDULO 4: Auditoria Preditiva (BI)",
        "🏗️ MÓDULO 5: Copiloto de Cadernos"
    ]
)

# ----------------------------------------------------
# 🟦 MÓDULO 1: TRIAGEM INTELIGENTE
# ----------------------------------------------------
if modulo == "🟦 MÓDULO 1: Triagem Inteligente":
    st.title("🟦 TRIAGEM INTELIGENTE & EXTRAÇÃO")
    st.caption("Parser universal de alta velocidade para contratos, propostas e orçamentos.")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        uploaded_file = st.file_uploader("Carregar Ficheiro (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
        variaveis = st.text_area("Variáveis Específicas para Caçar (Separadas por vírgula):", 
                                 value="Valor Total, Prazo de Execução, Penalizações por Atraso, Entidades Envolvidas")
        
        btn_triagem = st.button("Executar Extração Neural")
        
    with col2:
        st.subheader("// Variáveis Isoladas & Análise")
        if btn_triagem and uploaded_file:
            with st.spinner("A processar matriz de texto..."):
                texto = read_universal_file(uploaded_file)
                sys_prompt = f"És um analista sénior de projetos. Extrai do documento as seguintes variáveis e dá um parecer crítico estruturado: {variaveis}"
                resposta = ask_groq(sys_prompt, f"Documento:\n\n{texto}")
                
                st.session_state.last_triagem = resposta
                st.markdown(resposta)
                
                # Geração de Relatório Word
                report_bio = create_word_report("Relatório de Triagem Inteligente", resposta)
                st.download_button(
                    label="📥 Descarregar Relatório Oficial (.docx)",
                    data=report_bio,
                    file_name=f"Relatorio_Triagem_{uploaded_file.name}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

# ----------------------------------------------------
# 🟩 MÓDULO 2: ENGENHARIA DE PROMPTS
# ----------------------------------------------------
elif modulo == "🟩 MÓDULO 2: Engenharia de Prompts":
    st.title("🟩 BIBLIOTECA DE PROMPTS DE OURO")
    st.caption("Armazenamento e replicação instantânea de diretrizes intelectuais do gabinete.")
    
    # Criar novo prompt
    with st.expander("➕ CADASTRAR NOVA DIRETRIZ TÉCNICA"):
        novo_titulo = st.text_input("Título do Template")
        novo_prompt = st.text_area("Comando de Engenharia:")
        if st.button("Sincronizar na Memória"):
            if novo_titulo and novo_prompt:
                st.session_state.prompts_biblioteca[novo_titulo] = novo_prompt
                st.success(f"Diretriz '{novo_titulo}' injetada com sucesso.")
                st.rerun()

    st.markdown("### Templates Operacionais Ativos")
    for tit, pr in list(st.session_state.prompts_biblioteca.items()):
        st.markdown(f"**⚡ {tit}**")
        st.code(pr, language="text")

# ----------------------------------------------------
# 🟩 MÓDULO 3: AGENTE IA CONSULTOR
# ----------------------------------------------------
elif modulo == "🟩 MÓDULO 3: Agente IA Consultor":
    st.title("🟩 AGENTE IA: CONSULTOR DE ARQUITETURA")
    st.caption("Brainstorming instantâneo sobre volumetria, materiais inovadores, iluminação e custos por m².")
    
    # Mostrar histórico
    for msg in st.session_state.chat_arquitetura_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    if prompt_chat := st.chat_input("Pergunte sobre solos, fundações, marcas, iluminação técnica..."):
        with st.chat_message("user"):
            st.markdown(prompt_chat)
        st.session_state.chat_arquitetura_history.append({"role": "user", "content": prompt_chat})
        
        sys_prompt = "És um Arquiteto e Engenheiro de Sistemas Sénior. Dá respostas brilhantes, focadas em eficiência térmica, iluminação, custos reais por metro quadrado e dados técnicos rigorosos de engenharia."
        
        with st.chat_message("assistant"):
            with st.spinner("A calcular soluções de design..."):
                res = ask_groq(sys_prompt, prompt_chat)
                st.markdown(res)
        st.session_state.chat_arquitetura_history.append({"role": "assistant", "content": res})

# ----------------------------------------------------
# 🟪 MÓDULO 4: AUDITORIA PREDITIVA (BI)
# ----------------------------------------------------
elif modulo == "🟪 MÓDULO 4: Auditoria Preditiva (BI)":
    st.title("🟪 BUSINESS INTELLIGENCE & PREVISÃO")
    st.caption("Conversão de dados brutos de planilhas em relatórios estratégicos de desvio e risco.")
    
    uploaded_data = st.file_uploader("Carregar Folha de Dados (Excel .xlsx, .csv, ou Relatórios)", type=["xlsx", "csv", "docx", "pdf", "txt"])
    
    if uploaded_data:
        # Se for planilha, mostra uma pré-visualização futurista
        if uploaded_data.name.endswith('.xlsx') or uploaded_data.name.endswith('.csv'):
            df = pd.read_excel(uploaded_data) if uploaded_data.name.endswith('.xlsx') else pd.read_csv(uploaded_data)
            st.markdown("### // Amostra de Dados Brutos Identificada")
            st.dataframe(df.head(5), use_container_width=True)
            text_context = df.to_string()
        else:
            text_context = read_universal_file(uploaded_data)
            st.text(text_context[:500] + "... [Texto Cortado para Visualização]")

        st.markdown("---")
        st.markdown("🤖 **Proatividade da IA:**")
        st.info("Identifiquei a sua matriz de dados. Gostaria que eu fizesse uma auditoria focada em Previsões de Desvio de Custos/Prazos, Análise de Omissões Contratuais ou Sugestões de Otimização?")
        
        foco_analise = st.selectbox("Escolha o Foco Estratégico:", ["Previsões de Desvio e Derrapagem Financeira", "Análise de Omissões Técnicas/Seguros", "Otimização de Margens e Negociação"])
        
        if st.button("Gerar Auditoria Preditiva de Luxo"):
            with st.spinner("A rodar modelos preditivos estatísticos..."):
                sys_bi = f"Atua como um Auditor Preditivo de Obras. Analisa os dados fornecidos focando estritamente em: {foco_analise}. Forneça estimativas lógicas de desvio em percentagem (X%) e indique quais as fases com maior risco."
                analise_bi = ask_groq(sys_bi, text_context)
                
                st.markdown(analise_bi)
                
                # Download
                report_bi_doc = create_word_report(f"Auditoria Preditiva - {foco_analise}", analise_bi)
                st.download_button(
                    label="📥 Descarregar Relatório Executivo (.docx)",
                    data=report_bi_doc,
                    file_name=f"Auditoria_BI_{foco_analise.replace(' ', '_')}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

# ----------------------------------------------------
# 🏗️ MÓDULO 5: COPILOTO DE CADERNOS
# ----------------------------------------------------
elif modulo == "🏗️ MÓDULO 5: Copiloto de Cadernos":
    st.title("🏗️ CRIAÇÃO & REVISÃO DE CADERNOS DE ENCARGOS")
    st.caption("Geração guiada automatizada ou blindagem de minutas contra litígios de mercado.")
    
    modo_caderno = st.radio("Selecione a Operação:", ["Modo Co-Piloto (Criação Assistida)", "Modo Engenheiro de Revisão (Blindagem)"])
    
    if modo_caderno == "Modo Co-Piloto (Criação Assistida)":
        st.subheader("// Configuração do Escopo Técnico do Projeto")
        obj_contratacao = st.text_input("Qual é o objeto principal da contratação? (Ex: Execução de Fachada Ventilada em Pedra)")
        prazos_criticos = st.text_input("Quais os prazos críticos e marcos de vistoria?")
        penalidades = st.text_input("Quais as multas ou penalizações estipuladas por dia de atraso?")
        
        if st.button("Gerar Esqueleto Técnico Blindado"):
            with st.spinner("A redigir caderno de encargos oficial..."):
                prompt_gen = f"Gere um Caderno de Encargos profissional dividindo em Secções Jurídicas e Especificações Técnicas. Objeto: {obj_contratacao}, Prazos: {prazos_criticos}, Penalidades: {penalidades}."
                caderno_gerado = ask_groq("Atua como um Engenheiro Fiscalizador e Advogado Técnico.", prompt_gen)
                
                st.markdown(caderno_gerado)
                
                report_cad = create_word_report("Caderno de Encargos Gerado", caderno_gerado)
                st.download_button(
                    label="📥 Baixar Caderno de Encargos (.docx)",
                    data=report_cad,
                    file_name="Caderno_de_Encargos_Gerado.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
                
    else:
        st.subheader("// Upload de Rascunho para Blindagem Contratual")
        rascunho_file = st.file_uploader("Submeter rascunho de caderno de encargos", type=["pdf", "docx", "txt"])
        
        if rascunho_file and st.button("Executar Engenharia de Revisão"):
            with st.spinner("A caçar ambiguidades e brechas contratuais..."):
                texto_rascunho = read_universal_file(rascunho_file)
                sys_review = "Analise o caderno de encargos. Identifique cláusulas vagas, riscos e omissões. Devolva uma análise crítica profunda e termine criando uma tabela com as colunas: [Cláusula Original | Risco Detetado | Texto Sugerido para Substituição]."
                resultado_revisao = ask_groq(sys_review, texto_rascunho)
                
                st.markdown(resultado_revisao)
