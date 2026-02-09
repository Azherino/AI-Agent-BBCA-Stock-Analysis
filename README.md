# 🏦 AI Agent BBCA Stock Analysis

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Llama3-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)

Aplikasi **Analisis Saham BBCA** yang cerdas, menggabungkan data visualisasi interaktif dengan kemampuan analisis generatif AI (Llama 3 via Ollama). Project ini dirancang untuk memantau pergerakan harga saham Bank Central Asia (BBCA) dan memberikan insight teknikal secara otomatis.

---

## ✨ Fitur Utama

- **📊 Grafik Interaktif**: Visualisasi pergerakan harga saham (6 bulan terakhir) menggunakan `Plotly`, mendukung mode Area Chart dan Candlestick.
- **💹 Real-time Metrics**: Menampilkan harga terakhir, perubahan harian, serta harga tertinggi/terendah secara dinamis.
- **🤖 Analisis AI**: Terintegrasi dengan **Ollama (Llama 3)** untuk memberikan analisis pasar, prediksi trend, dan saran aksi investasi dalam Bahasa Indonesia.
- **🎨 UI Modern**: Antarmuka bersih dengan dukungan Sidebar dan Dark Mode friendly.

## 🛠️ Teknologi yang Digunakan

- **[Streamlit](https://streamlit.io/)**: Framework utama untuk membangun web app data science.
- **[YFinance](https://pypi.org/project/yfinance/)**: Mengambil data historis saham BBCA secara real-time.
- **[Plotly](https://plotly.com/)**: Membuat grafik interaktif dan responsif.
- **[Groq API](https://groq.com/)**: Cloud AI Inference super cepat untuk menjalankan model Llama 3.

## 🚀 Cara Menjalankan Project (Lokal)

### Prasyarat

Pastikan Anda telah menginstal:
1. **Python 3.10+**
2. **API Key Groq** (Dapatkan gratis di [console.groq.com](https://console.groq.com))

### Langkah Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/AI-Agent-BBCA-Stock-Analysis.git
   cd AI-Agent-BBCA-Stock-Analysis
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi**
   ```bash
   streamlit run app.py
   ```
   *Saat pertama kali dijalankan, masukkan API Key Groq Anda di kolom yang tersedia di sidebar.*

## 🌐 Cara Deploy ke Streamlit Cloud

Aplikasi ini siap di-deploy secara online agar bisa diakses publik.

1. **Push ke GitHub**: Upload project ini ke repository GitHub Anda.
2. **Daftar Streamlit Cloud**: Login ke [share.streamlit.io](https://share.streamlit.io/).
3. **Buat App Baru**: Pilih repository GitHub Anda dan file utama `app.py`.
4. **Atur Secrets (PENTING)**:
   - Di dashboard Streamlit Cloud, klik **Advanced Settings** -> **Secrets**.
   - Tambahkan kode berikut:
     ```toml
     GROQ_API_KEY = "gsk_..."
     ```
     *(Ganti `gsk_...` dengan API Key Groq asli Anda)*
5. **Deploy**: Klik tombol **Deploy**. Aplikasi Anda akan liven dalam hitungan detik!

## 📸 Preview

<img width="1920" height="1786" alt="screencapture-ai-agent-bbca-stock-analysis-l3bngswibbzqrlyvx4fcxs-streamlit-app-2026-02-09-19_05_29" src="https://github.com/user-attachments/assets/6904ace9-7976-42ba-8b39-995eb224c0dc" />
<img width="1920" height="1786" alt="screencapture-ai-agent-bbca-stock-analysis-l3bngswibbzqrlyvx4fcxs-streamlit-app-2026-02-09-19_05_49" src="https://github.com/user-attachments/assets/fd01c986-6c99-4611-a478-3fd4e60a1160" />



## 🤝 Kontribusi

Pull request dipersilakan. Untuk perubahan besar, mohon buka issue terlebih dahulu untuk mendiskusikan apa yang ingin Anda ubah.

## 📄 Lisensi

[MIT](https://choosealicense.com/licenses/mit/)
