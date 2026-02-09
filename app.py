import streamlit as st
import yfinance as yf
import pandas as pd
from groq import Groq
import plotly.graph_objects as go

# Konfigurasi Halaman
st.set_page_config(
    page_title="BBCA AI Stock Agent",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Inisialisasi Groq Client ---
# Coba ambil API Key dari secrets, jika tidak ada, biarkan kosong (nanti diminta di sidebar)
try:
    api_key = st.secrets.get("GROQ_API_KEY")
except Exception:
    api_key = None

# --- Sidebar ---
with st.sidebar:
    st.header("📈 BBCA Stock Agent")
    st.markdown("Dashboard analisis saham **Bank Central Asia (BBCA)** bertenaga AI.")
    st.markdown("---")
    
    # Input API Key jika belum ada di secrets
    if not api_key:
        api_key = st.text_input("🔑 Masukkan Groq API Key", type="password", help="Dapatkan di console.groq.com")
        if not api_key:
            st.warning("⚠️ API Key diperlukan untuk fitur AI.")
    
    st.markdown("---")
    st.write("**Fitur:**")
    st.markdown("- Data Real-time (Delayed)")
    st.markdown("- Grafik Interaktif")
    st.markdown("- Analisis AI (Llama3 via Groq)")
    st.markdown("---")
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.rerun()
    st.markdown("---")
    st.caption("Created with Streamlit & Groq")

# --- Judul Utama ---
st.title("🏦 Analisis Saham BBCA.JK")
st.markdown("Pantau pergerakan harga saham dan dapatkan insight instan dari AI.")

# --- Fungsi Data ---
@st.cache_data
def get_bbca_data():
    # Download data
    try:
        df = yf.download("BBCA.JK", period="6mo", interval="1d")
        
        # Ratakan MultiIndex jika ada
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        
        df = df.reset_index()
        return df
    except Exception as e:
        st.error(f"Gagal mengambil data: {e}")
        return pd.DataFrame()

try:
    df = get_bbca_data()
    
    if df.empty:
        st.stop()

    # Perhitungan Metrik
    latest_close = df["Close"].iloc[-1]
    prev_close = df["Close"].iloc[-2]
    change = latest_close - prev_close
    change_pct = (change / prev_close) * 100
    
    highest_6m = df["High"].max()
    lowest_6m = df["Low"].min()
    avg_vol = df["Volume"].mean()

    # --- Metrik ---
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Harga Terakhir", f"Rp {latest_close:,.0f}", f"{change:,.0f} ({change_pct:.2f}%)")
    with col2:
        st.metric("Tertinggi 6 Bulan", f"Rp {highest_6m:,.0f}")
    with col3:
        st.metric("Terendah 6 Bulan", f"Rp {lowest_6m:,.0f}")
    with col4:
        st.metric("Rata-rata Volume", f"{avg_vol:,.0f}")

    # --- Grafik Interaktif (Plotly) ---
    st.subheader("📊 Pergerakan Harga (6 Bulan)")
    
    # Pilihan Tipe Grafik
    chart_type = st.radio("Tipe Grafik:", ["Area Chart", "Candlestick"], horizontal=True)

    fig = go.Figure()

    if chart_type == "Area Chart":
        fig.add_trace(go.Scatter(
            x=df['Date'], y=df['Close'],
            mode='lines',
            name='Close Price',
            fill='tozeroy',
            line=dict(color='#0084ff', width=2)
        ))
    else:
        fig.add_trace(go.Candlestick(
            x=df['Date'],
            open=df['Open'], high=df['High'],
            low=df['Low'], close=df['Close'],
            name='OHLC'
        ))

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Tanggal",
        yaxis_title="Harga (IDR)",
        margin=dict(l=0, r=0, t=30, b=0),
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Ringkasan & AI Analysis ---
    st.divider()
    
    col_ai_left, col_ai_right = st.columns([1, 2])
    
    trend = "Uptrend" if latest_close > df["Close"].iloc[0] else "Downtrend"

    summary_text = f"""
    Harga Terakhir: {latest_close}
    Rata-rata 6 Bulan: {df["Close"].mean():.2f}
    Harga Tertinggi: {highest_6m}
    Harga Terendah: {lowest_6m}
    Trend Umum: {trend}
    """

    with col_ai_left:
        st.subheader("🤖 Analisis AI")
        st.info("Klik tombol di bawah untuk meminta AI (Llama3 via Groq) menganalisis data saham ini.")
        
        analyze_btn = st.button("✨ Mulai Analisis", type="primary", use_container_width=True)

    with col_ai_right:
        if analyze_btn:
            if not api_key:
                st.error("⚠️ Groq API Key belum dimasukkan. Silakan masukkan di sidebar.")
            else:
                with st.spinner("Sedang berpikir... (Mohon tunggu)"):
                    prompt = f"""
                    Anda adalah analis pasar saham profesional dan berpengalaman.
                    
                    Berikut adalah data ringkas saham BBCA (Bank Central Asia):
                    {summary_text}
                    
                    Tugas Anda:
                    1. Analisis kondisi teknikal singkat berdasarkan data di atas.
                    2. Berikan prediksi arah jangka pendek (Naik/Turun/Sideways).
                    3. Berikan saran aksi (Beli/Jual/Tahan) dengan alasan yang logis namun hati-hati.
                    
                    Jawablah dalam Bahasa Indonesia yang profesional, padat, dan jelas. Hindari basa-basi.
                    """
                    
                    try:
                        client = Groq(api_key=api_key)
                        chat_completion = client.chat.completions.create(
                            messages=[
                                {
                                    "role": "user",
                                    "content": prompt,
                                }
                            ],
                            model="llama-3.1-8b-instant", # Assuming MODEL is meant to be "llama-3.1-8b-instant" or a variable named MODEL is defined elsewhere.
                        )
                        content = chat_completion.choices[0].message.content
                        st.success("Analisis Selesai!")
                        st.markdown("### 💡 Hasil Analisis")
                        st.write(content)
                    except Exception as e:
                        st.error("⚠️ Gagal terhubung ke Groq API.")
                        st.warning("Periksa koneksi internet atau validitas API Key Anda.")
                        st.expander("Lihat Detail Error").write(e)

except Exception as e:
    st.error("Terjadi kesalahan saat memuat data.")
    st.write(e)
