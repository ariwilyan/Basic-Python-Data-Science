# Teknik Looping

nama_band = ['Payung Teduh', 'Fourtwnty', 'Dialog Dini Hari', 'Mr. Sonjaya', 'Parahyena', 'Syahrini']

kumpulan_lagu = ['Akad', 'Zona Nyaman', 'Rumahku', 'Sang Filsuf', 'Sindoro', 'Jodohku']

# loop biasa
for item in nama_band:
	print('nama band: ', item)
print()

# enumerate
for index, band in enumerate(nama_band):
	print(index, ':', band)
print()

# zip (note: jika length dari salah satu objek list misalnya ada yang tidak sama panjangnya, maka tidak akan bisa ditampilkan hasilnya.)
for band, lagu in zip(nama_band, kumpulan_lagu):
	print(band, 'menyanyikan lagu yang berjudul: ', lagu)
print()

# set
playlist = {'baby baby', 'ada apa dengan cinta', 'cenat-cenut', 'jaran goyang', 'jaran goyang', 'gorgom', 'kuda', 'kucing'}

for lagu in sorted(playlist):
	print(lagu)
print('='*100)
print()

# dictionary (key and value)
playlist2 = {'Payung Teduh': 'akad',
			'Fourtwnty': 'Zona Nyaman',
			'Dialog Dini Hari': 'Rumahku',
			}
for i in playlist2.keys():
	print(i)
print()
for i in playlist2.values():
	print(i)
print()
for i in playlist2.items():
	print(i)
print()
for i,v in playlist2.items():
	print(i, 'lagunya: ', v)
print()

# reverse (dibalik dari akhir ke awal)
for i in reversed(range(1, 10, 1)):
	print(i)
print()

# loop for dengan kombinasi else, break, dan range
number = 25

for i in range(0, 40):
	print(i)

	if i is number:
		print('angka ditemukan',i)
		break
else:
	print('angka tidak ditemukan')
print("space di luar for")
print()

# loop for dengan continue dan pass
for i in range(1, 10):

	if i is 6:
		print('nilai i adalah', 6)
		# break : fungsinya untuk mengakhiri for (terminasi)
		# continue : fungsinya untuk melanjutkan ke step berikutnya
		pass
		print("cek bro 1")
	print('nilai saat ini adalah', i)
else:
	print('akhir dari loop')
print('print diluar loop')
print()

# while loop
angka = 0

while angka < 5:
	print('nilai angka adalah:', angka)
	angka = angka + 1
print('di luar while')
print()

start = True # variable boolean
angka = 0

while start:
	print("di dalam while")
	if angka is 100:
		start = False
		print('oke angka 100 ditemukan')
	angka += 1
print()

# while dengan else, break, continue, pass
angka = 0

while angka < 10:

	if angka is 5:
		print('checkpoint 1')
		break
		#pass
		#continue # jika ini digunakan akan loop forever/infinite loop dengan stuck di angka = 5
		#print('checkpoint 2') # ini tidak faedah

	print('nilai angka adalah:', angka)
	angka += 1
else:
	print('nilai angka diakhir while adalah', angka)