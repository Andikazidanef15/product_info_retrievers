import re
import pandas as pd
from transformers import pipeline

# Get information
def extract_information(qa_pipeline:pipeline, context:str):
    print('Konteks:', context)
    print('--------------------------------------------')

    # Dapatkan informasi barang dan jumlah barang
    quest = 'Apa saja barang yang ia beli?'
    answer = qa_pipeline(question=quest, context=context)

    # Bersihkan teks jawaban barang
    barang = re.sub('\d+', '', answer['answer'])
    barang = re.sub(' ', '', barang)
    barang = re.sub('(dan|,)', '; ', barang).strip()

    # Bersihkan teks jawaban jumlah barang
    jumlah_barang = '; '.join(re.findall('\d+', answer['answer']))

    # Dapatkan informasi motif
    quest = 'Apa motif barang yang dipesan?'
    answer = qa_pipeline(question=quest, context=context, handle_impossible_answer = True)
    motif_score = answer['score']

    if motif_score > 0.97:
        motif = answer['answer']
    else:
        motif = ''

    # Dapatkan informasi lokasi
    quest = 'Ke mana barang tersebut dikirim?'
    answer = qa_pipeline(question=quest, context=context, handle_impossible_answer = True)
    lokasi_pengiriman = answer['answer']

    # Kumpulkan semua jawaban dalam bentuk dictionary
    dict_answer = {
        'Informasi':['Nama Barang', 'Jumlah Barang', 'Motif', 'Lokasi Pengiriman'],
        'Nilai':[barang, jumlah_barang, motif, lokasi_pengiriman]
    }

    df = pd.DataFrame(dict_answer)

    return df