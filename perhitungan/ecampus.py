def campus() :
    import datetime
    from texttable import Texttable
    x = datetime.datetime.now()
    table = Texttable ()
    no = 0
    nama = []
    nim = []
    kelas = []
    bayar_uas = []
    bayar_uts = []
    seminar = []
    bayar_bulanan = []
    bayar_kas = []
    admin = []
    jawab="y"
    while(jawab == "y") :
        print("\n\t====== PROGRAM PEMBAYARAN CAMPUS PELITA BANGSA ======\n")
        print("="*30)
        nama.append(input("Masukan Nama : "))
        nim.append(input("Masukan NIM : "))
        kelas.append(input("Masukan Kelas : "))
        print("="*30)
        
        print("1. PEMBAYARAN UTS\n")
        print("2. PEMBAYARAN UAS")
        print("="*30)
        pilih=int(input('\nMasukan Pilihan Anda : '))
        if pilih == 1 :
            print("="*30)
            print('PEMBAYARAN UTS')
            print("="*30)
            jumlah_mapel = (int(input("Masukan jumlah mapel : ")))
            bayar_uts.append(jumlah_mapel*50000)
            bulanan = (int(input("Masukan Jumlah Bulan yang Akan Di Bayar : ")))
            bayar_bulanan.append(bulanan*500000)
            kas = (int(input("Masukan jumlah kas yang di bayar : ")))
            bayar_kas.append(kas*20000)
            smn=(int(input("Masukan jumlah seminar yang di bayar : ")))
            seminar.append(smn*100000)
            admin.append("5500")
            
            no +=1
            for i in range (no) :
                smn = int(seminar[i])
                kas = int(bayar_kas[i])
                uts = int(bayar_uts[i])
                bln = int(bayar_bulanan[i])
                akhir = (uts)+(bln)+(kas)+(5000)+(smn)
                table.set_cols_dtype(['i','a','a','a','a','a','a','a','a','a','a'])
                table.add_rows([['No','nama','nim','kelas','UTS','SPP','Seminar','KAS','Admin','Total','Tanggal Transaksi'],
                                [i+1,nama[i],nim[i],kelas[i],bayar_uts[i],
                                 bayar_bulanan[i],seminar[i],bayar_kas[i],admin[i],akhir,x]])
                
                print(table.draw())
                jawab =input("\n Bayar Lain Lagi y/t : ")
            else :
                print("\n\n\t==========TERIMAKASIH ATAS KUNJUNGAN ANDA==========")
                


        elif pilih==2 :
            print("="*30)
            print('PEMBAYARAN UAS')
            print("="*30)
            jumlah_mapel = (int(input("Masukan jumlah mapel : ")))
            bayar_uas.append(jumlah_mapel*50000)
            bulanan = (int(input("Masukan Jumlah Bulan yang Akan Di Bayar : ")))
            bayar_bulanan.append(bulanan*500000)
            kas = (int(input("Masukan jumlah kas yang di bayar : ")))
            bayar_kas.append(kas*20000)
            smn =(int(input("Masukan jumlah seminar yang di bayar : ")))
            seminar.append(smn*100000)
            admin.append("5500")
            no +=1
            for i in range (no) :
                smn = int(seminar[i])
                kas = int(bayar_kas[i])
                uas = int(bayar_uas[i])
                bln = int(bayar_bulanan[i])
                akhir = (uas)+(bln)+(kas)+(5000)+(smn)
                table.set_cols_dtype(['i','a','a','a','a','a','a','a','a','a','a'])
                table.add_rows([['No','nama','nim','kelas','UAS','SPP','Seminar','KAS','Admin','Total','Tanggal Transaksi'],
                                [i+1,nama[i],nim[i],kelas[i],bayar_uas[i],
                                 bayar_bulanan[i],seminar[i],bayar_kas[i],admin[i],akhir,x]])
                

            print(table.draw())
            jawab =input("\n Bayar Lain Lagi y/t : ")
        else :
            print("\n\n\t==========TERIMAKASIH ATAS KUNJUNGAN ANDA==========")


                
                
            

