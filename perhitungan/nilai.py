def nilai () :
        from texttable import Texttable
        table = Texttable ()
        jawab = "y"
        no = 0
        nama = []
        nim = []

        nilai_tugas = []
        nilai_uts = []
        nilai_uas = []
        while(jawab == "y"):
                nama.append(input("Masukan Nama : "))
                nim.append(input("Masukan NIM : "))
                nilai_tugas.append(input("Masukan Nilai Tugas : "))
                nilai_uts.append(input("Masukan Nilai UTS : "))
                nilai_uas.append(input("Masukan Nilai UAS : "))
                
                jawab = input ("Tambah Lagi (y/n) ????  ")
                no +=1
        for i in range (no) :
                    tugas = int(nilai_tugas[i])
                    uts = int(nilai_uts[i])
                    uas = int(nilai_uas[i])
                    akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100)
                    table.add_rows([['NO','NAMA','NIM','TUGAS','UTS','UAS','AKHIR'],
                                   [i+1, nama[i], nim[i],  nilai_tugas[i], nilai_uts[i], nilai_uas[i], akhir ]])
        print(table.draw())




