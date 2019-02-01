# class Hewan():
#     kaki = ''
#     mata = ''

#     def tampilkan_kaki(self):
#         print(self.kaki)

# kucing = Hewan()
# ayam = Hewan()
# burung = Hewan()

# kucing.kaki = 4
# ayam.kaki = [2,4,5]
# burung.kaki = 'seratus'

# kucing.tampilkan_kaki()
# ayam.tampilkan_kaki()
# burung.tampilkan_kaki()

hewan = ['ayam', 'burung', 'kucing']

# for i in hewan:
# 	print(i)
a_hewan = [i for i in hewan if 'u' in i and 'r' in i]
print(a_hewan)