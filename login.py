from perhitungan.gaji import gaji
from perhitungan.nilai import nilai
from perhitungan.kalkulator import kalkulator
from perhitungan.ecampus import campus
def menu() :
    print('\n')
    print( "----- SILAHKAN MEMILIH PROGRAM YANG TERSEDIA  -----")
    from texttable import Texttable
    table = Texttable ()
    table.add_rows([['NO','NAMA PROGRAM'],['1','PROGRAM GAJI KARYAWAN'], ['2','PROGRAM PENILAIAN MAHASISWA'],
                    ['3','PROGRAM KALKULATOR '],['4','PROGRAM PEMBAYARAN KAMPUS PB'],['5','EXIT']])

    print(table.draw())
    pilih = int(input("Silahkan Masukkan Pilihan Anda : "))
    if pilih == 1:
        gaji()
        tanya()
    elif pilih == 2:
        nilai()
        tanya()
    elif pilih == 3 :
        kalkulator()
        tanya()
    elif pilih == 4:
        ecampus()
        tanya()
    elif pilih == 5 :
        exit
        print('TERIMAKASIH ATAS KUNJUNGAN ANDA')
    else:

        print("Eror, Pilihan Anda Tidak Ditemukan. Pilih 1-5")
        tanya()
        
       
def tanya ():
     tanya = input("Kembali Me Menu Utama (y/t)? ")
     if tanya == "y":
         menu()
     elif tanya == "t":
        exit
     else:
         print ("Terima Kasih Atas Kunjungan Anda")

  
print('\tWELCOME TO MY PROGRAM')
print('===================================================') 
           
def login():
    
    print (' \nSilahkan Login Dahulu')
    print('---------------------------------------------------') 
    username = (input("Masukkan Username Anda : "))
    password = (input("Masukkan Password Anda : "))
    if  (password == '52314838') : 
             print ('\nLOGIN SUCCESS ')
             print('---------------------------------------------------') 
             menu()
             exit
             
    else :
             print('\nPassword/username salah')
             
             
             login()
             exit                 

                               
login()
