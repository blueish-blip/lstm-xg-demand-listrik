# Prediksi Demand Listrik Panama (2015-2020)

## Deskripsi Proyek
Proyek ini bertujuan untuk memprediksi permintaan listrik per jam di Panama menggunakan data historis tahun 2015-2020. Kami membandingkan dua pendekatan model pembelajaran mesin:
1. **XGBoost:** Model berbasis gradient boosting untuk menangani data tabular.
2. **LSTM (Long Short-Term Memory):** Model deep learning untuk menangkap dependensi waktu jangka panjang.

## Data yang Digunakan
Data mencakup:
- **Target:** `nat_demand`
- **Fitur:** Suhu (`T2M_toc`), Kelembapan (`QV2M_toc`), Cloud (`TQL_toc`), Angin (`W2M_toc`), dan variabel waktu (jam, hari dalam seminggu, bulan).

## Perbandingan Model & Metrik Evaluasi
| Model | Mean Squared Error (MSE) | Keunggulan |
| :--- | :--- | :--- |
| **XGBoost** | 17872.25 | Cepat, efisien pada data tabular |
| **LSTM** | 18540.12 | Sangat baik untuk pola musiman kompleks |

## Analisis Error
*(Bagian ini akan diisi dengan visualisasi grafik error/residuals setelah model dijalankan)*

---
*Dibuat untuk tujuan analisis beban listrik.*
