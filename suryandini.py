nama = ("suryandini") #STRING
print(nama,type(nama))
angka = 17 # INTEGER
print(angka,type(angka))
angka1 = 23.4 #FLOAT
print(angka1,type(angka1))
#BOOLEAN
nilaia = 8>1 #8 lebih dari atau lebih besar dari 1 =true 
print(nilaia,type(nilaia))
nilaib = 8<1 #8 kurang dari atau kecil dari 1 =false 
print(nilaib,type(nilaib))

#ARITMATIKA
def soal():
    print('''D0221360
    gaji_pokok =1.000.000
    gaji_lembur/jam =6.000
    lama_lembur = sesuai dari angka terakhir nim
    gaji_lemburnya =(gaji_lembur/jam)lama_lembur
    pajak = 11%''')
jumlah_gaji_lembur = 6000*60
gaji_kena_pajak = 1000000*11/100
gaji_kotor =1000000 + jumlah_gaji_lembur
gaji_bersih = gaji_kotor - gaji_kena_pajak

soal()
print("nama:suryandini (D0221360)")
print("gaji pokok : 1000000")
print("gaji lembur :",jumlah_gaji_lembur)
print("gaji kotor :",gaji_kotor)
print("pajak:", 11/100)
print("potongan :", gaji_kena_pajak)
print("gaji_bersih :", gaji_bersih)


#percabangan if else
nilai1=75
if (nilai1 >=80):
    print("lulus")
else:
    print("tidak lulus")
