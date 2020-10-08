# list1 = [1, 2, 3, 4]
# list2.copy() = list1
# print(list2)

# y = print(float('1993'))
# print(type(y))

# apa = {'apa': 1, 'bisa': 2, 'hatu': 5}
# apa.clear()
# print(apa)

# jualan = ['bakso', 'mie ayam', 'kwetiau', 'pangsit', 'sop buah']

# def abang():
# 	jualan.append('bakso')
# 	return jualan
# def tukang():
# 	jualan.pop(3)
# 	return jualan
# def bakso():
# 	jualan.extend(['kwetiau'])
# 	return jualan
# def mari():
# 	jualan.insert(10, 'mie ayam')
# def sini():
# 	del jualan[0:1]

# # abang(1000)
# # bakso = 1001
# # tukang(2)

# # ['bakso', 'mie ayam', 'kwetiau', 'bakso']

# # bakso = 1000
# # kwetiau = 21
# for i in range(1000):
# 	abang()
# for i in range(2):
# 	tukang()
# for i in range(20):
# 	bakso()
# for i in range(5):
# 	mari()
# for i in range(11):
# 	sini()
# print(jualan)

# total_bakso = 0
# total_mie_ayam = 0
# total_pangsit = 0
# total_kwetiaw = 0
# total_sop_buah = 0

# for item in jualan:
# 	if item == 'bakso':
# 		total_bakso += 1
# 	elif item == 'mie ayam':
# 		total_mie_ayam += 1
# 	elif item == 'kwetiau':
# 		total_mie_ayam += 1
# 	elif item == 'pangsit':
# 		total_mie_ayam += 1
# 	elif item == 'sop buah':
# 		total_mie_ayam += 1
# print(total_bakso)
# print(total_mie_ayam)
# print(total_pangsit)
# print(total_kwetiaw)
# print(total_sop_buah)

# A = dict(zip(('p', 'y', 't', 'h', 'o', 'n'), (4, 6, 8, 12, 22, 34)))
# A1 = sorted([A[a] for a in A])
# A2 = {i:i**3 for i in A1}
# print(A2)

# list2 = sekolah
# list1 = siswa

# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums[::True])

# B = []
# for a in A:
# 	if len(a)%2!=0:
# 		if a[0] == 'B':
# 			if a[-1] == 'g':
# 				B.append(a)
# C = 

drama = {'flower': '16', 'hi bye': '20', 'itaewon': '16', '18 again': '20', 'sound': '20'}
drama.clear('sound')
print(drama)
