import streamlit as st
import pandas as pd
import plotly.express as px

# ============================
# 🔹 Carregar os dados
# ============================
vendasArq_df = pd.read_excel("Vendas1.xlsx")

# ============================
# 🔹 Pré-processamento
# ============================
vendasArq_df["Data"] = pd.to_datetime(vendasArq_df["Data"])
vendasArq_df["DataFormatada"] = vendasArq_df["Data"].dt.strftime("%d/%m/%Y")

# ============================
# 🔹 Configuração da página
# ============================
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
st.title("Dashboard de Vendas")

st.markdown("Análise automática do dataset `Vendas1.xlsx` usando Pandas + Streamlit.")

st.markdown("---")

# ============================================
# 🔹 Filtro de Período (Ranking Dinâmico)
# ============================================
st.sidebar.header("🔎 Filtros")

data_min = vendasArq_df["Data"].min()
data_max = vendasArq_df["Data"].max()

periodo = st.sidebar.date_input(
    "Período:",
    value=(data_min, data_max),
)

if len(periodo) == 2:
    inicio, fim = periodo
    df_filt = vendasArq_df[(vendasArq_df["Data"] >= pd.to_datetime(inicio)) &
                           (vendasArq_df["Data"] <= pd.to_datetime(fim))]
else:
    df_filt = vendasArq_df.copy()

# ============================================
# 🔹 RANKING DAS LOJAS (estilo prêmio)
# ============================================
st.subheader("🏆 Ranking das Lojas — Período Selecionado")

ranking_lojas = (
    df_filt.groupby("ID Loja")
    .size()
    .reset_index(name="Total de Vendas")
    .sort_values("Total de Vendas", ascending=False)
)

st.dataframe(ranking_lojas, use_container_width=True)

# KPI Loja Campeã
loja_top = ranking_lojas.iloc[0]["ID Loja"]
vendas_top = ranking_lojas.iloc[0]["Total de Vendas"]
total_geral = ranking_lojas["Total de Vendas"].sum()
percentual = (vendas_top / total_geral) * 100

st.metric(
    label="🏆 Loja Líder no Período",
    value=f"{loja_top}",
    delta=f"{percentual:.2f}% de participação"
)

st.markdown("---")

# ============================================
# 🔹 Gráfico Pareto 80/20
# ============================================
st.subheader("📈 Gráfico de Pareto — Lojas que Mais Vendem")

ranking_lojas["% Acumulado"] = ranking_lojas["Total de Vendas"].cumsum() / ranking_lojas["Total de Vendas"].sum() * 100

fig_pareto = px.bar(
    ranking_lojas,
    x="ID Loja",
    y="Total de Vendas",
    title="Pareto 80/20 — Concentração das Vendas por Loja",
)

fig_pareto.add_scatter(
    x=ranking_lojas["ID Loja"],
    y=ranking_lojas["% Acumulado"],
    mode="lines+markers",
    name="% Acumulado",
)

st.plotly_chart(fig_pareto, use_container_width=True)

st.markdown("---")

# ============================================
# 🔹 Comparação por Ticket Médio
# ============================================
st.subheader("🎯 Comparação do Ticket Médio por Loja")

ticket_medio = (
    df_filt.groupby("ID Loja")["Valor Final"]
    .mean()
    .reset_index(name="Ticket Médio")
    .sort_values("Ticket Médio", ascending=False)
)

fig_ticket = px.bar(
    ticket_medio,
    x="ID Loja",
    y="Ticket Médio",
    text_auto=".2f",
    title="Comparação do Ticket Médio por Loja",
)

st.plotly_chart(fig_ticket, use_container_width=True)

st.markdown("---")

# ============================================
# 🔹 KPIs — Estilo BI
# ============================================
st.subheader("📌 KPIs Gerais")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Vendas (linhas)", len(df_filt))

with col2:
    st.metric("Quantidade Total", int(df_filt["Quantidade"].sum()))

with col3:
    st.metric("Valor Médio", f"R$ {df_filt['Valor Unitario'].mean():.2f}")

with col4:
    st.metric("Maior Venda", f"R$ {df_filt['Valor Final'].max():.2f}")

st.markdown("---")

# ============================================
# 🔹 Estatísticas e Visualizações
# ============================================
st.subheader("📌 Estatísticas Descritivas dos Dados")
st.dataframe(df_filt.describe(), use_container_width=True)

st.markdown("---")

# Visualização: Distribuições
colA, colB = st.columns(2)

with colA:
    fig_valor = px.histogram(
        df_filt,
        x="Valor Final",
        nbins=50,
        title="Distribuição do Valor Final",
    )
    st.plotly_chart(fig_valor, use_container_width=True)

with colB:
    fig_quant = px.histogram(
        df_filt,
        x="Quantidade",
        nbins=10,
        title="Distribuição de Quantidade",
    )
    st.plotly_chart(fig_quant, use_container_width=True)

st.markdown("---")

# ============================================
# 🔹 Preview do DataFrame
# ============================================
st.subheader("👁️ Visualização do DataFrame")
tab1, tab2 = st.tabs(["Primeiras linhas", "Últimas linhas"])

with tab1:
    st.dataframe(df_filt.head(), use_container_width=True)

with tab2:
    st.dataframe(df_filt.tail(), use_container_width=True)
