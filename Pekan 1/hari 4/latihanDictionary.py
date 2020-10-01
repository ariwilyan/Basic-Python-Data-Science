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