from messages import *

def show_opening_popup(display_surface):
    
    opening_text = [
        "Seorang pemuda berkelana mencari obat untuk keluarganya yang sakit.",
        "Ramuan yang dapat dijadikan obat konon tersembunyi di dalam hutan.",
        "Pemuda tersebut pergi ke hutan untuk mencari obat..."
    ]

    show_text = Message(opening_text, display_surface)
    # , -850, -150)
    show_text.run()

def show_poison1(display_surface):
    text_poison1 = [
        "Selamat! Kamu telah menemukan ramuan paling ampuh...",
        "Keluargamu sembuh total dan kembali sehat seperti sedia kala...",
        "Petualanganmu yang penuh keberanian dan ketekunan telah membuahkan hasil."
    ]
    # show_text = Message(text_poison1, -3000, -150)
    show_text = Message(text_poison1, display_surface)
    show_text.run()

def show_poison2(display_surface):
    text_poison2 = [
        "Kamu menemukan ramuan yang cukup ampuh.",
        "Keluargamu sembuh untuk sementara waktu, namun...",
        "kamu harus terus mencari ramuan lain untuk penyembuhan yang lebih permanen."
    ]
    show_text = Message(text_poison2, display_surface)
    show_text.run()

def show_poison3(display_surface):
    text_poison3 = [
        "Kamu tidak berhasil menemukan ramuan yang dapat menyembuhkan keluargamu.",
        "Meskipun telah berusaha sekuat tenaga...",
        "penyakit tersebut terlalu kuat dan keluargamu tidak dapat diselamatkan."
    ]
    show_text = Message(text_poison3, display_surface)
    show_text.run()

def show_poison4(display_surface):
    text_poison4 = [
        "Sayangnya, ramuan yang kamu temukan tidak dapat menyembuhkan penyakit keluargamu...",
        "Meski telah berjuang keras,",
        "usaha ini belum membuahkan hasil. Jangan menyerah, masih ada harapan di masa depan."
    ]
    show_text = Message(text_poison4, display_surface)
    show_text.run()

def show_death(display_surface):
    text_death = [
        "Dalam pencarian putus asa untuk obat penyembuh...",
        "pemuda berkelana menemui ajal di dalam hutan gelap...",
        "Harapan penyelamatan bagi keluarganya pupus bersama dengan kepergiannya!!!"
    ]
    show_text = Message(text_death, display_surface)
    show_text.run()