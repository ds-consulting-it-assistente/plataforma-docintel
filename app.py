import streamlit as st
import pandas as pd
import json
from io import BytesIO
from core_utils import read_universal_file, ask_groq, create_word_report

# ----------------------------------------------------
# 🪐 CONFIGURAÇÃO ESTÉTICA PREMIUM LIGHT (ARCHI-CLEAN)
# ----------------------------------------------------
st.set_page_config(page_title="ARCHINTEL // LAB", page_icon="📐", layout="wide")

# Forçar Tema Claro Puro de Alto Contraste
st.html("""
<style>
    /* Fundo Geral e Cor de Texto Humana */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #FAFAFA !important;
        color: #1E293B !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Forçar caixas de chat e blocos a serem brancos puros */
    .block-container .element-container div.stMarkdown, 
    [data-testid="stChatMessage"] {
        background-color: #FFFFFF !important;
        color: #1E293B !important;
        border: 1px solid #E2E8F0 !important;
        border-left: 5px solid #1E40AF !important;
        border-radius: 8px !important;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.02) !important;
    }
    
    /* Barra Lateral Limpa */
    [data-testid="stSidebar"] {
        background-color: #F8FAFC !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    
    /* Títulos em Azul Escuro Arquitetónico */
    h1, h2, h3, h4, h5, h6, [data-testid="stSidebar"] h1 {
        color: #0F172A !important;
        font-weight: 700 !important;
    }
    
    /* Inputs visíveis */
    div[data-baseweb="input"], div[data-baseweb="select"], div[data-baseweb="textarea"], .stChatInputContainer {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        color: #0F172A !important;
    }

    /* Botão Azul Executivo */
    .stButton>button {
        background: linear-gradient(90deg, #1E40AF 0%, #3B82F6 100%) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 6px !important;
    }
</style>
""")
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
st.sidebar.title("ARCHINTEL // HUB")
st.sidebar.caption("OS SYSTEM V1.0")
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
        
        # CAMPO ATUALIZADO: Livre para escreveres o que quiseres
        diretrizes = st.text_area(
            "Instruções e Diretrizes para a Análise (Texto Livre):", 
            value="Faça uma análise crítica e minuciosa deste documento, destacando os pontos mais importantes, eventuais riscos identificados e sugerindo as próximas ações recomendadas.",
            height=180
        )
        
        btn_triagem = st.button("Executar Extração Neural")
        
    with col2:
        st.subheader("// Parecer Técnico & Análise Automática")
        if btn_triagem and uploaded_file:
            with st.spinner("A processar matriz de texto..."):
                texto = read_universal_file(uploaded_file)
                
                # O prompt agora junta o documento à tua instrução livre de forma orgânica
                sys_prompt = "És um consultor e analista sénior de projetos de engenharia e arquitetura. Executa uma análise inteligente de alto nível baseando-te estritamente nas instruções fornecidas pelo utilizador."
                prompt_usuario = f"Instruções do Utilizador:\n{diretrizes}\n\n---\n\nDocumento para Analisar:\n{texto}"
                
                resposta = ask_groq(sys_prompt, prompt_usuario)
                
                st.session_state.last_triagem = resposta
                st.markdown(resposta)
                
                # Geração de Relatório Word
                report_bio = create_word_report("Relatório de Análise Inteligente", resposta)
                st.download_button(
                    label="📥 Descarregar Relatório Oficial (.docx)",
                    data=report_bio,
                    file_name=f"Analise_Inteligente_{uploaded_file.name}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

# ----------------------------------------------------
# 🟩 MÓDULO 2: ENGENHARIA DE PROMPTS
# ----------------------------------------------------
if modulo == "MÓDULO 2: Engenharia de Prompts":
    st.title("🟩 BIBLIOTECA DE PROMPTS DE OURO")
    st.caption("Armazenamento permanente e consulta de diretrizes intelectuais do gabinete.")
    
    st.subheader("// Templates de Engenharia & Auditoria (Prontos a Usar)")
    
    with st.expander("🔍 1. Auditoria de Margem de Obra", expanded=False):
        st.code("Analise os custos deste orçamento e encontre os 3 itens com maior probabilidade de superfaturamento ou desvio técnico.", language="text")
        
    with st.expander("🪟 2. Conformidade de Caixilharia", expanded=False):
        st.code("Verifique se as especificações de vidros e caixilharias atendem aos requisitos de isolamento acústico e térmico classe A.", language="text")

    st.write("---")
    st.subheader("// 🎨 NOVOS TEMPLATES MESTRE PARA GERAÇÃO DE IMAGENS")
    st.info("💡 Copia o esqueleto abaixo e substitui as variáveis entre parêntesis retos [ ] no teu motor de IA favorito.")

    # NOVO TEMPLATE: ILUMINAÇÃO DE LUXO
    with st.expander("💡 TEMPLATE: Iluminação Arquitetónica de Luxo (Lighting Design)", expanded=True):
        prompt_luz = (
            "Uma fotografia de arquitetura fotorrealista de alta definição e nível premium de um [ESPAÇO], localizado em Portugal. "
            "O foco principal é um projeto de iluminação complexo e multi-camadas de alto padrão. No teto, [LUZ_TETO] cria um ambiente sofisticado. "
            "Focos direcionais de trilha com [TEMPERATURA_COR] e alto CRI iluminam com precisão [ELEMENTO_DE_DESTAQUE]. "
            "Uma luminária decorativa do tipo [LUMINÁRIA_DESIGN] está posicionada sobre [ZONA_DE_TRABALHO]. "
            "A atmosfera geral é cinematográfica e executiva, com sombras volumétricas suaves e excelente contraste entre luz e sombra. "
            "Através das janelas panorâmicas, a iluminação exterior é de [HORA_DO_DIA]. Renderização profissional, fotorrealismo extremo, "
            "ray-tracing, pós-processamento arquitetónico detalhado, 8K, qualidade de portfólio."
        )
        st.text_area("Esqueleto do Prompt (Copia Daqui):", value=prompt_luz, height=140)
        
        st.markdown("""
        **Guia de Preenchimento Rápido:**
        * `[ESPAÇO]`: ex: *sala de reuniões minimalista*, *átrio com pé-direito duplo*
        * `[LUZ_TETO]`: ex: *perfis de LED lineares*, *sancas de luz indireta âmbar*
        * `[TEMPERATURA_COR]`: ex: *2700K (luz quente)*, *4000K (luz neutra)*
        * `[ELEMENTO_DE_DESTAQUE]`: ex: *uma maquete de vidro sobre a mesa central*
        * `[LUMINÁRIA_DESIGN]`: ex: *pendente linear em latão escovado*
        """)

    # NOVO TEMPLATE: 2D PARA 3D
    with st.expander("📐 TEMPLATE: Conversão de Projeto 2D para Maquete 3D Volumétrica", expanded=False):
        prompt_3d = (
            "Uma visualização conceitual fotorrealista e tecnológica que captura o processo de transformação de design de 2D para 3D. "
            "Sobre uma mesa limpa de estúdio de engenharia feita de [MATERIAL_MESA], um ecrã digital ou tablet exibe de forma nítida uma planta baixa técnica em 2D de um [TIPO_DE_PROJETO]. "
            "Emerindo de forma volumétrica e tridimensional diretamente de cima do ecrã, projeta-se uma maquete 3D detalhada com volumetria realista da mesma estrutura, exibindo [ESTILO_ARQUITETÓNICO]. "
            "A transição entre as linhas geométricas do plano horizontal e os volumes verticais em 3D é visível e fluida. "
            "O ambiente do estúdio em redor apresenta [DETALHES_AMBIENTE]. Atmosfera premium de inovação tecnológica, iluminação de foco focada na maquete, renderização 8K, profundidade de campo cinematográfica."
        )
        st.text_area("Esqueleto do Prompt (Copia Daqui):", value=prompt_3d, height=140)
        
        st.markdown("""
        **Guia de Preenchimento Rápido:**
        * `[MATERIAL_MESA]`: ex: *concreto escovado cinza*, *madeira de carvalho maciça*
        * `[TIPO_DE_PROJETO]`: ex: *moradia contemporânea com piscina*, *edifício de 3 pisos*
        * `[ESTILO_ARQUITETÓNICO]`: ex: *linhas retas minimalistas e grandes panos de vidro*
        * `[DETALHES_AMBIENTE]`: ex: *óculos VR e amostras de materiais ao lado*
        """)
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
if modulo == "🟪 MÓDULO 4: Auditoria Preditiva (BI)":
    st.title("🟪 BUSINESS INTELLIGENCE & PREVISÃO")
    st.caption("Conversão de dados brutos de planilhas em relatórios estratégicos de desvio e risco.")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Carregar Folha de Dados (Excel .xlsx, .csv, ou Relatórios)", 
            type=["xlsx", "csv", "docx", "pdf", "txt"]
        )
        
        # NOVA CAIXA DE TEXTO LIVRE PARA INTEGRAÇÃO COM IA
        diretrizes_bi = st.text_area(
            "O que deseja analisar ou caçar nestes dados? (Texto Livre):",
            value="Faça uma auditoria preditiva completa. Identifique anomalias financeiras, projeções de desvio de prazo e aponte os cenários de maior risco.",
            height=150
        )
        
        btn_bi = st.button("Executar Análise Preditiva")
        
    with col2:
        st.subheader("// Diagnóstico de Risco & Tendências")
        if btn_bi and uploaded_file:
            with st.spinner("A ler matriz de dados e a calcular cenários..."):
                # Leitura universal do conteúdo do ficheiro
                conteudo_dados = read_universal_file(uploaded_file)
                
                # Construção do Prompt Mestre para o Especialista em BI
                sys_prompt = "És um Engenheiro de BI e Auditor Preditivo Sénior. A tua missão é cruzar os dados brutos fornecidos com as diretrizes do utilizador, calculando riscos, desvios e sugerindo mitigações lógicas."
                prompt_usuario = f"Diretrizes de Análise:\n{diretrizes_bi}\n\n---\n\nDados Extraídos do Ficheiro:\n{conteudo_dados}"
                
                # Chamada ao modelo atualizado da Groq
                resposta_bi = ask_groq(sys_prompt, prompt_usuario)
                
                st.markdown(resposta_bi)
                
                # Botão para extrair o relatório executivo em Word
                report_bio = create_word_report("Auditoria Preditiva e BI", resposta_bi)
                st.download_button(
                    label="📥 Descarregar Relatório BI (.docx)",
                    data=report_bio,
                    file_name=f"Auditoria_BI_{uploaded_file.name}.docx",
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
        
        if st.button("Gere um Caderno de Encargos profissional"):
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
