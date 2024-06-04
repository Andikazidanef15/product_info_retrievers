# Auto Ekstrak Informasi Pengiriman
Ekstrak informasi pengiriman dengan menggunakan model *finetuned* IndoBERT pada data [indo_product_inference](https://huggingface.co/datasets/andikazf15/indo_product_inference)

## Streamlit
Untuk mencoba model IndoBERT dalam mendapatkan informasi pengiriman, Anda bisa mengunjungi website [IndoBERT Auto Ekstrak Info Pengiriman](https://huggingface.co/spaces/andikazf15/auto_ekstrak_info_pengiriman)

Isi input `konteks` dengan teks yang mengandung informasi pengiriman barang seperti yang disediakan pada contoh.

## Instruksi Instalasi
Instruksi ini ditujukan untuk menjalankan kode `notebook/Item_Information_Retrieval.ipynb`:
1. Buat python 3.10 virtual environment (bisa menggunakan python-env atau anaconda)
2. Install packages yang ada dalam requirements.txt melalui terminal
```
pip install -r requirements.txt
```
3. Run kode `notebook/Item_Information_Retrieval.ipynb`

## Informasi Training
Model IndoBERT dilatih dengan menggunakan data sintetis yang dibuat pada kode `notebook/Item_Information_Retrieval.ipynb`. Data tersebut juga dapat diakses pada link [indo_product_inference](https://huggingface.co/datasets/andikazf15/indo_product_inference). 

Adapun model yang digunakan menggunakan hasil *pretrained* [mBERT-IndoSQuADv2](https://huggingface.co/rizquuula/mBERT-IndoSQuADv2_1691852742-16-2e-06-0.01-5) lalu di *fine-tuning* pada data sintetis tersebut. Hasil evaluasi model menunjukkan skor 55% dan 56% pada metrik *Exact Match* dan *F1 score*. Adapun evaluasi metrik tersebut merujuk kepada metrik yang digunakan dalam mengevaluasi model *Question Answering (QA)* pada dataset SQuAD.

## Limitasi Model
Model ini memiliki beberapa limitasi:
* Ketika list barang beserta jumlah barang yang diberikan makin banyak, maka hasil prediksi nama dan jumlah barang dapat salah. Bisa dicoba dengan kalimat konteks berikut

```
Saya mau memesan 10 piring, 20 gelas, 30 guling, 40 karet, 50 meja dengan motif A ke Tangerang Selatan Raya
```

* Tetapi jika inputnya tidak melibatkan jumlah dari tiap barang maka hasilnya dapat benar. Untuk mengecek, kita dapat menggunakan kalimat konteks sebelumnya tanpa jumlah masing-masing barang

```
Saya mau memesan piring, gelas, guling, karet, meja dengan motif A ke Tangerang Selatan Raya
```

* Kalimat konteks yang informasinya tidak lengkap dapat menghasilkan jawaban yang salah

* Kalimat konteks yang melibatkan beberapa pasang kata dalam motif/lokasi dapat memberikan jawaban yang kurang akurat seperti contoh berikut, hasil prediksi hanya mengambil kata 'Jerman' dalam lokasi

```
Saya mau memesan piring, gelas, guling, karet, meja dengan motif A ke Jerman Barat Daya
```