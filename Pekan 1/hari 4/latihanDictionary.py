# review materi perbedaan list, tuple, dan set
list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)
set1 = {1, 2, 3, 4}

#rint(type(list1))
#print(type(tuple1))
#print(type(set1))

# dictionary = {key:value, key:value}
member1 = {"ID": 101,
			"Nama": "Faqihza Mukhlish",
			"Pekerjaan": "Mahasiswa",
			"Status member": "Gold"
			}

# print(member1["Pekerjaan"])
# print(member1.keys())
# print(member1.values())
# print(member1.items())

member2 = {"ID": 102,
			"Nama": "Ujang Pintu",
			"Pekerjaan": "reparasi pintu",
			"Status member": "Berlian"}

memberlist = {101: member1, 102: member2}

print(memberlist[101])

#a = [4, 7, 2, 6, 13, 5, 3, 0, 1]
#a.sort() # jika mau menggunakan method sort
#print(sorted(a))
import random
nama = 'Ari Wilyan'
jawaban_nama = [
	"nama saya  {0}".format(nama),
	"orang-orang memanggil saya {0}".format(nama),
	"panggil saja saya {0}".format(nama)
]
print(random.choice(jawaban_nama))