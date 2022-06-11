print("FORM NILAI TES PESERTA KURSUS PYTHON")

class peserta:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

        for i in nama,nilai:
            print(i)
        if nilai <= 65:
            print("tidak lulus")
        else :
            print("lulus")


p1 = peserta (input("masukkan nama      ="), int(input("masukkan nilai tes =")))