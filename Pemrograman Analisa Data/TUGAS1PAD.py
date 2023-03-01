# soal 1 
print("SOAL 1")
print ("A")
x = -2 # mengisi variabel x dengan nilai -2 
print (x) # menampilkan isi variabel x 

print ()
print("B")
y = x + 5 # mengisi variabel y dengan rumus x+5
print (x), print (y) # menampilkan isi variabel x dan y 

print()
print ("C")
x = x**y # mengisi variabel x dengan rumus x = x**y
print(x), print(y) # menampilkan isi variabel x dan y

print()
print ("D")
print ((x/y)+2) # menampilkan hasil dari perhitungan rumus ((x/y)+2)
print(x), print(y) # menampilkan isi variabel x dan y

print()
print ("E")
y = ((y % 2)+0.6) # mengisi variabel y dengan rumus y = ((y % 2)+0.6) 
print(x), print(y) # menampilkan isi variabel x dan y
print()

# soal 2
print("SOAL 2")
bal = 100 # mengisi variabel bal dengan angka 100
inter = .05 # mengisi variabel inter dengan angka .05
withDr = 25 # mengisi variabel withDr dengan angka 25
bal += (inter * bal) # mengisi variabel bal dengan rumus bal += (inter * bal)
bal = bal - withDr # mengisi variabel bal dengan rumus bal = bal - withDr
print (bal) # menampilkan isi variabel bal 
print(inter) # menampilkan isi variabel inter 
print(withDr) # menampilkan isi variabel withDr
print()

# soal 3
print("SOAL 3")
name = "Angel" # mengisi isi variabel name = Angel
address = "Jalan Malioboro" # mengisi isi variabel address = Jalan Malioboro
print (name, address) # menampilkan isi variabel name, address
print()

#soal 4
print ("SOAL 4")
p = float(input('Masukan panjang kos Anda : ')) # meminta user memasukan angka kemudian disimpan ke variabel p
l = float(input('Masukan lebar kos Anda   : ')) # meminta user memasukan angka kemudian disimpan ke variabel l
luas = p * l # mengisi varibel luas dengan rumus p * l
print ('Luas kamar kos Anda adalah {}'.format(luas), 'm2') # menampilkan hasil dari perhitungan luas kamar kos
print()

# soal 5
print ("SOAL 5")
price = float(input('Masukan jumlah harga makanan yang dipesan : ')) # meminta user memasukan angka kemudian disimpan ke variabel price
pajakmkn = price * 0.06 # mengisi variabel pajakmkn dengan rumus price * 0.06 
tips = price * 0.15 # mengisi variabel tips dengan rumus price * 0.15
total = float (price) + float (pajakmkn) + float(tips) # mengisi variabel total dengan rumus float (price) + float (pajakmkn) + float(tips) 
print ('Pajak makan : {}'.format(pajakmkn)) # menampilkan isi variabel pajakmkn
print ('Tips : {}'.format(tips)) # menampilkan isi variabel tips
print ('Total yang harus dibayar dari %0.2f'%(total)) # menampilkan isi variabel total dengan format 2 angka dibelakang koma
print()

#soal 6
print ("SOAL 6")
watt = float(input('Masukan kapasitas alat (watt) : ')) # meminta user memasukan angka kemudian disimpan ke variabel watt
time = int(input('Masukan durasi penggunaan (jam) : ')) # meminta user memasukan angka kemudian disimpan ke variabel time
price = 1500.50 # mengisi variabel price dengan angka 1500.50
biaya = float (watt * time)/price # mengisi variabel biaya dengan rumus perhitungan (watt * time)/price
print ('Kapasitas alat tersebut : {}'.format(watt)) # menampilkan isi variabel watt
print ('Durasi penggunaan (jam) : {}'.format(time)) # menampilkan isi variabel time
print ('Biaya listrik per kWh: {}'.format(price)) # menampilkan isi variabel price 
print ('Total yang harus dibayar dari %0.2f'%(biaya)) # menampilkan isi variabel biaya dengan format 2 angka dibelakang koma