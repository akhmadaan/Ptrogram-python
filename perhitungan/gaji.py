def gaji () :
    from texttable import Texttable
    table = Texttable ()
    no = 0
    nama = []
    jabatan = []
    gaji = []
    jawab = "y"



    while (jawab =='y'):
        nama.append(input("masukan nama: "))
        jab=input("jabatan : ")
        jabatan.append(jab)
        if (jab =='programmer'):
            gaji.append('3000.000')
            no +=1

            jawab=input("\n Tambah lagi?")
            
        elif (jab =='direktur'):
            gaji.append('10.000.000')
            no +=1
        
            
            jawab=input("\n Tambah lagi?")
            
        elif (jab =='Kepala Bagian'):

            gaji.append('800.0000')
            no +=1
        
            
            jawab=ut("\n Tambah lagi?")
        else:
                nama.append(input("erooorr"))
                
                jawab=input("\n Tambah lagi?")
                    
        


    for i in range (no) :
            
        table.add_rows([['NO','NAMA','JABATAN','GAJI'],
                        [i+1,nama[i],jabatan[i], gaji[i]]])
    print(table.draw())

