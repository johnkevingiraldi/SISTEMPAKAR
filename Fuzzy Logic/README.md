#Fuzzy Logic
John Kevin Giraldi
1184049
D4 TI 3C

# Pengontrol Lalu Lintas Cerdas Menggunakan Fuzzy Logic 
Tujuan dari proyek ini adalah untuk membahas desain dan implementasi sistem lampu lalu lintas cerdas berbasis teknologi logika fuzzy. Menggunakan Python, sistem logika fuzzy telah dikembangkan untuk menentukan waktu tunggu persimpangan lalu lintas yang khas.
<img width="876" alt="traffic-lights" src="https://user-images.githubusercontent.com/50858731/114805411-2801df80-9dcd-11eb-8f59-62cf1859b07f.png">

# Syarat
Untuk mengembangkan sistem lampu lalu lintas cerdas menggunakan logika fuzzy, sangat penting untuk memahami bagaimana persimpangan lalu lintas normal beroperasi.
Untuk ini kita dapat mempertimbangkan persimpangan empat arah sederhana dan mengamati diagram keadaannya. Persimpangan empat arah ini terdiri dari dua ruas jalan Utama dan Samping.
Dengan asumsi tidak ada jalur berbelok, persimpangan dapat diringkas menjadi empat. Alur diagram lalu lintas adalah loop dan waktu setiap sinyal konstan.
Sistem lalu lintas ini dapat direpresentasikan dengan empat status. Masing-masing bagian ini memastikan tidak ada kemungkinan kombinasi di mana kedua jalan tersebut memiliki lampu hijau.
Sistem ini juga memastikan bahwa ada keadaan antara peralihan lampu hijau yang memberi waktu bagi mobil yang tersisa untuk melewatinya.
Saat memulai dari status "0 0", selama pengatur waktu menghitung atau tidak ada mobil yang menunggu di jalan lain, status akan tetap di "0 0".
Jika pengatur waktu tidak menghitung dan mobil menunggu untuk melewati persimpangan, status akan berubah menjadi kuning selama lima detik.
Ketika penghitung waktu singkat berhenti menghitung, sistem akhirnya akan memberikan izin ke jalan yang berdekatan yang memungkinkan mobil untuk melewatinya.
Proses serupa dilakukan dengan status "1 1" dan "1 0" yang akhirnya mengulang kembali ke status awal semula. Meskipun ini adalah contoh yang sangat sederhana dari sistem lampu lalu lintas, dasar-dasarnya telah dibuat untuk mengembangkan sistem lalu lintas yang lebih rumit menggunakan pengontrol logika fuzzy.
<img width="883" alt="state-diagram" src="https://user-images.githubusercontent.com/50858731/114805445-3ea83680-9dcd-11eb-851e-968ae032e9d9.png">

# Syarat Pengontrol Logika Fuzzy 
Pada intinya, logika fuzzy adalah pendekatan komputasi berdasarkan "derajat kebenaran" daripada logika boolean "benar atau salah" biasa yang menjadi dasar komputer modern.
Misalnya, jika mencoba menggambarkan seberapa jujur ​​seseorang, kita mungkin mencoba dan lebih spesifik daripada sekadar menyatakan dia jujur ​​atau tidak jujur.
Seseorang mungkin menyatakan bahwa seseorang sedikit jujur, sangat jujur, atau tidak jujur ​​sama sekali.
<img width="886" alt="fuzzy-graphs" src="https://user-images.githubusercontent.com/50858731/114805497-541d6080-9dcd-11eb-8d5f-99479a098b35.png">
Logika fuzzy berasal dari ide ini dan dapat diterapkan dalam banyak situasi komputasi yang berbeda. Sistem lalu lintas logika fuzzy ini tidak seperti sistem lalu lintas pada umumnya.
Model tersebut mengamati jumlah mobil yang menunggu serta jumlah mobil yang masuk ke persimpangan. Aturan dikembangkan untuk secara umum menggambarkan status sebuah jalan persimpangan.
Logika yang sama diterapkan pada mobil yang masuk ke persimpangan yang memberikan kesan keseluruhan sibuk dan juga seberapa sibuk jalan itu nantinya.
<img width="900" alt="sensors" src="https://user-images.githubusercontent.com/50858731/114805540-65ff0380-9dcd-11eb-8902-6d3e0c4e9962.png">

# Implementasi
Implementasi sistem lalu lintas cerdas dengan logika fuzzy ini berfokus pada penentuan waktu tunggu untuk sisi jalan tertentu. Apabila mengetahui jumlah mobil yang menunggu di perempatan beserta jumlah mobil yang melaju, program akan melakukan proses fuzzifikasi dan defuzzifikasi untuk memberikan perkiraan waktu tunggu.
Selama proses fuzzifikasi masing-masing nilai diteruskan ke fungsinya masing-masing. Fungsi-fungsi tersebut merupakan proses fuzzifikasi yang menentukan himpunan fuzzy untuk masing-masing sensor.
Himpunan fuzzy yang dikembalikan dari fungsi-fungsi ini kemudian digunakan untuk menyimpulkan nilai linguistik yang berhubungan dengan seberapa sibuk mungkin persimpangan tertentu.
Setelah menyimpulkan seperti apa keadaan persimpangan tersebut, kesimpulan tersebut diteruskan ke proses defuzzifikasi yang menghasilkan waktu tunggu yang disarankan untuk mobil di jalan yang sesuai.
<img width="729" alt="fuzzy-engine" src="https://user-images.githubusercontent.com/50858731/114805571-6f886b80-9dcd-11eb-8b63-8eeaff101888.png">

# Kesimpulan
Sistem lalu lintas yang lebih cerdas, lebih cepat, dan lebih dinamis menjadi penting di kota-kota dengan pertumbuhan penduduk yang cepat. Sistem lampu lalu lintas cerdas ini telah terbukti memiliki efek positif dalam masyarakat dan menantang ilmuwan komputer di seluruh dunia untuk mencoba dan menciptakan sistem yang lebih baik untuk manajemen lalu lintas.
Pengembangan lebih lanjut ke keadaan saat ini dari pengendali logika fuzzy ini akan menghasilkan hasil yang lebih baik, karena hanya memiliki kemampuan untuk menentukan status jalan tunggal.
Masa depan sistem manajemen lalu lintas cerdas cerah dan hanya masalah waktu sebelum sistem seperti ini diterapkan di banyak kota di seluruh dunia.
<img width="519" alt="defuzzifier" src="https://user-images.githubusercontent.com/50858731/114805598-77e0a680-9dcd-11eb-924f-daf06cec1566.png">