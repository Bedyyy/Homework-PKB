import pandas as pd

def cari_label(x):
    x.sort()
    panjang_data = len(x)

    if panjang_data % 2 == 1:
        label = x[panjang_data // 2]
    else:
        label = (x[panjang_data // 2 - 1] + x[panjang_data // 2]) / 2

    return label

def klasifikasi_species(y, med):
    species_list = []
    for i in y:
        if i < med:
            species_list.append("small-leaf")
        elif i > med:
            species_list.append("big-leaf")
        elif i == med:
            species_list.append("new-species")
    return species_list

baca_file = pd.read_excel("data_pkb.xlsx")
banyak_kolom = baca_file.shape[1] - 1
calc = 1



loop = True
while(loop):
    print("============= TUGAS PKB =============")
    print("1. Tampilkan Data")
    print("2. Tambahkan Data Baru Kedalam Kolom")
    print("3. Tambahkan Kolom Baru dan Datanya")
    print("4. Klasifikasikan")
    print("5. Exit Program")
    print(" ")

    input_program = int(input("Silahkan Pilih: "))

    if(input_program == 1):
        tampilkan_data = baca_file.head(len(baca_file))
        print(" ")
        print("Berikut adalah datanya: ")
        print(" ")
        print(tampilkan_data)
        print(" ")
    elif(input_program == 2):
        print("Maaf, fitur ini belum tersedia. Silahkan coba fitur lain")
    elif(input_program == 3):
        data_baru = []
        nama_kolom_baru = input("Masukkan Nama Kolom Baru: ")
        for input_data in range(len(baca_file['Species'])):
            input_data = float(input("Masukkan Datanya: "))
            data_baru.append(input_data)
        baca_file.insert(baca_file.shape[1] - 1, nama_kolom_baru, data_baru)
        baca_file.to_excel("data_pkb.xlsx", index=False)
    elif(input_program == 4):
        if banyak_kolom  == 1:
            nama_data = baca_file.columns[0]
            value_data = baca_file[nama_data].tolist()
            batas_label = cari_label(value_data)
            species = klasifikasi_species(value_data, batas_label)
            baca_file["Species"] = species
            baca_file.to_excel("data_pkb.xlsx", index=False)
        elif banyak_kolom > 1:
            for x in baca_file.columns:
                if x == "Species":
                    continue
                value_data = baca_file[x]
                calc = calc * value_data
            batas_label = cari_label(calc.tolist())
            species = klasifikasi_species(calc, batas_label)
            baca_file["Species"] = species
            baca_file.to_excel("data_pkb.xlsx", index=False)
    elif(input_program == 5):
        loop = False
print(" ")
print("Terima Kasih!")
