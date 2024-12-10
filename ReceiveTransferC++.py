
# Membuka file data.txt untuk membaca
file_path = 'C:/Users/admin/source/repos/KomunikasiPythonC++/KomunikasiPythonC++/data.txt'

with open(file_path, 'r') as file:
    data = file.read()  # Membaca seluruh konten file

print("Data received from C++:", data)

# Menghapus konten file dengan membuka dalam mode 'w' dan menulis data baru
new_data = "uhuuyyy"
with open(file_path, 'w') as file:  # 'w' untuk overwrite file
    file.write(new_data)  # Menulis data baru ke file

print("File content replaced with new data.")



# # Menulis data baru ke file data.txt
# new_data = "\nHello from Python! This is new data."
# with open('C:/Users/admin/source/repos/KomunikasiPythonC++/KomunikasiPythonC++/data.txt', 'a') as file:  # 'a' untuk append, jika ingin menambah data ke file
#     file.write(new_data)  # Menambahkan data baru ke file

# print("New data written to data.txt.")
