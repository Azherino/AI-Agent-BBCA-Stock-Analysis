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
- **[Ollama](https://ollama.com/)**: Menjalankan Large Language Model (Llama 3) secara lokal untuk analisis teks.

## 🚀 Cara Menjalankan Project

### Prasyarat

Pastikan Anda telah menginstal:
1. **Python 3.10+**
2. **Ollama** (dan sudah pull model `llama3`)

### Langkah Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/AI-Agent-BBCA-Stock-Analysis.git
   cd AI-Agent-BBCA-Stock-Analysis
   ```

2. **Buat Virtual Environment (Opsional tapi Disarankan)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Pastikan Ollama Berjalan**
   Buka terminal baru dan jalankan:
   ```bash
   ollama serve
   ```
   Pastikan model `llama3` sudah terunduh:
   ```bash
   ollama pull llama3
   ```

5. **Jalankan Aplikasi**
   ```bash
   streamlit run app.py
   ```

## 📸 Preview

*(Anda bisa menambahkan screenshot aplikasi di sini)*

## 🤝 Kontribusi

Pull request dipersilakan. Untuk perubahan besar, mohon buka issue terlebih dahulu untuk mendiskusikan apa yang ingin Anda ubah.

## 📄 Lisensi

[MIT](https://choosealicense.com/licenses/mit/)
