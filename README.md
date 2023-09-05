# Homework-PKB

Repository untuk mengumpulkan homework PKB (Kelompok)

### **Anggota Kelompok**

- Muhammad Hadiid Faathir (1313621035)
- Muhammad Shafwan Maulana (1313621022)
- Narendra Arkan Putra Darmawan (1313621043)
- Riky Dermawan (1313621009)


### **Problem Solving**

- Jika data memiliki hanya 1 kolom (Tidak termasuk kolom "Species") :
  
  1. Mengurutkan data
  2. Mencari nilai mediannya
  3. Nilai median digunakan sebagai label/batasan menentukan jenis species
  4. Jika data lebih dari nilai label maka dikategorikan sebagai "big-leaf" jika sebaliknya dikategorikan "small-leaf"
     
- Jika data memiliki lebih dari 1 kolom (Tidak termasuk kolom "Species") :
  
  1. Mencari luasnya / mengalikan seluruh data pada baris yang sama
  2. Mencari median dari seluruh data yang telah dikalikan
  3. Nilai median digunakan sebagai label/batasan menentukan jenis species
  4. Jika data lebih dari nilai label maka dikategorikan sebagai "big-leaf" jika sebaliknya dikategorikan "small-leaf"


### **Penggunaan**

Terdapat 2 file yaitu "main.py" sebagai file kode program dan "data_pkb.xlsx" sebagai file data (input data)

- Pastikan file disimpan dan berada dalam folder yang sama
- Data di dalam file excel berisi data awal yang telah dibagikan di channel telegram PKB
- Jalankan program
- Selanjutnya program akan berjalan dan menampilkan beberapa fitur di terminal, terdapat 5 fitur dalam program kami :
  - Fitur 1 untuk menampilkan data yang berada dalam file excel ke terminal
  - Fitur 2 untuk menambahkan data di baris baru kedalam kolom yang sudah ada. Namun karena kami belum dapat membuat programnya, maka dimohon untuk memasukkan datanya secara manual melalui excel
  - Fitur 3 untuk menambahkan kolom baru beserta datanya, banyaknya data yang ditambahkan disesuaikan dengan banyaknya data pada suatu kolom excel
  - Fitur 4 untuk menentukan klasifikasi dari data yang ada di excel dan memasukkan jenis klasifikasinya pada kolom "Species" di excel
  - Fitur 5 untuk mengakhiri program


### **Kekurangan Program Kami***

- Jika data awal yang berada dalam channel telegram sudah memiliki klasifikasi, ketika menambahkan data baru baik itu kolom baru atau kolom yang sudah ada maka klasifikasi awalnya bisa berubah karena program kami mencari nilai median sebagai label dengan scanning seluruh data. Jadi, jika datanya bertambah / berkurang maka nilai mediannya akan berubah sehingga mempengaruhi hasil klasifikasi
- Harus menginstall library pandas di python
- Kami tidak tahu apakah library pandas bisa membaca file dengan ekstensi yang dikeluarkan oleh LibreOffice
- Mungkin akan terdapat beberapa exception atau warning dalam kode program kami karena deteksi IntelliSense masing-masing PC, namun kode program tetap berjalan dengan baik

### **Video Demonstrasi**

Karena dikhawatirkan terjadi kesalahpahaman dalam penjelasan kami, maka kami memutuskan untuk membuat "Video Demonstrasi" guna menjelaskan keseluruhan program kami. Video Demonstrasi akan kami upload **paling lambat Rabu, 6 September 2023 (Besok) di repositori ini**

## **Akhir Kata**

Kami mengucapkan terima kasih kepada Bapak Muhammad Eka Suryana, M.Kom. atas pengertiannya dan mohon maaf apabila penjelasan kami tidak memenuhi ekspektasi bapak.
