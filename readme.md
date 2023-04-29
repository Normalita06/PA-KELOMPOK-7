# Deskripsi Program
Deskripsi program restoran dengan struktur data linked list yang memiliki login user dapat membeli dan mengecek saldo dan login admin dapat CRUD serta menerapkan algoritma searching dan sorting adalah sebagai berikut:

Program Phoenix Resto dibangun menggunakan struktur data linked list. Program ini memiliki dua jenis pengguna, yaitu user dan admin. User dapat melakukan login, kemudian dapat membeli menu makanan yang tersedia di restoran, serta dapat mengecek saldo yang dimilikinya. Sementara itu, admin dapat melakukan operasi CRUD (Create, Read, Update, Delete) pada menu makanan yang tersedia. Program ini juga menggunakan algoritma searching untuk mempermudah admin dalam mencari menu pada restoran, dan menerapkan algoritma sorting untuk mengurutkan menu makanan berdasarkan kategori hurufnya.

Dalam program ini, struktur data linked list digunakan untuk menyimpan data menu yang tersedia pada restoran. Setiap kali pengguna melakukan pembelian atau admin melakukan operasi CRUD, linked list akan diperbarui secara otomatis. Program ini juga memiliki fitur pengecekan saldo yang memungkinkan pengguna untuk mengetahui sisa saldo yang dimilikinya sebelum melakukan pembelian.

Secara keseluruhan, program ini dirancang untuk mempermudah pengguna dalam melakukan pembelian produk secara online dengan dukungan struktur data linked list dan algoritma searching dan sorting. Fitur-fitur yang tersedia dalam program ini dapat membantu meningkatkan efisiensi dan pengalaman pengguna dalam berbelanja.

# Struktur Program
Program di atas merupakan implementasi dari Linked List untuk menyimpan menu makanan pada sebuah restoran. Program terdiri dari 2 class, yaitu class Restoran dan class LinkedList.

1. Class Restoran terdiri dari 2 atribut yaitu nama dan harga, serta atribut next yang digunakan untuk menyimpan alamat dari node selanjutnya pada linked list.

2. Class LinkedList terdiri dari beberapa method, yaitu:
init() : method ini digunakan untuk menginisialisasi atribut head dengan nilai None dan atribut saldo dengan nilai 500000
tambah_menu(nama, harga) : method ini digunakan untuk menambahkan menu baru pada linked list. Method ini menerima 2 parameter yaitu nama dan harga menu baru yang akan ditambahkan. Method ini akan membuat objek baru dari class Restoran, kemudian akan menambahkan objek tersebut pada linked list.
tampilan_menu() : method ini digunakan untuk menampilkan seluruh menu yang tersedia pada linked list. Method ini akan menampilkan nomor urut, nama, dan harga menu menggunakan library PrettyTable.
cari_menu() : method ini digunakan untuk mencari menu berdasarkan nama pada linked list. Method ini akan meminta input nama menu yang ingin dicari, kemudian melakukan pencarian dengan menggunakan algoritma jump search. Jika menu ditemukan, method ini akan menampilkan nama dan harga menu, serta index dari menu tersebut pada linked list. Jika tidak ditemukan, method ini akan menampilkan pesan bahwa menu tidak ditemukan.
update_menu(menu, nama_baru, harga_baru) : method ini digunakan untuk mengubah nama dan harga suatu menu pada linked list. Method ini menerima 3 parameter yaitu menu yang akan diubah, nama baru, dan harga baru. Jika menu yang akan diubah ditemukan pada linked list, method ini akan mengubah nilai atribut nama dan harga pada objek tersebut. Jika tidak ditemukan, method ini akan menampilkan pesan bahwa menu yang dicari tidak ditemukan.
hapus_Menu(index) : method ini digunakan untuk menghapus menu pada linked list berdasarkan index. Method ini menerima 1 parameter yaitu index menu yang akan dihapus. Jika menu dengan index tersebut ditemukan pada linked list, method ini akan menghapus node tersebut dari linked list. Jika tidak ditemukan, method ini akan menampilkan pesan bahwa menu dengan index tersebut tidak ditemukan.
shell_sort() : method ini digunakan untuk mengurutkan menu pada linked list secara ascending menggunakan algoritma shell sort.
Cari_index(index) : method ini digunakan untuk mencari menu pada linked list berdasarkan index. Method ini menerima 1 parameter yaitu index menu yang ingin dicari. Method ini akan mengembalikan objek menu pada index yang sesuai.
to_array() : method ini digunakan untuk mengubah linked list menjadi array.
getindex(index) : method ini digunakan untuk mendapatkan objek menu pada index yang sesuai pada linked list. Method ini menerima 1 parameter yaitu index menu yang ingin dicari.
get_id(nama) : method ini digunakan untuk mendapatkan objek menu pada linked list berdasarkan nama menu. Method ini menerima 1 parameter yaitu nama menu yang ingin dicari.
get_length() : method ini digunakan untuk mendapatkan panjang linked list.
get_node_at_index(index) : method ini digunakan untuk mendapatkan objek menu pada index yang sesuai pada linked list. Method ini menerima fungsi shell_sort berisi implementasi algoritma shell sort untuk mengurutkan daftar menu restoran berdasarkan nama menu. Algoritma shell sort adalah algoritma pengurutan dengan metode membagi data menjadi beberapa kelompok dan mengurutkan kelompok tersebut secara terpisah-pisah. Algoritma ini mengambil sebuah array dan membaginya menjadi beberapa sub-array yang lebih kecil, kemudian mengurutkan sub-array tersebut menggunakan metode pengurutan insertion sort.
beli_makanan: method ini berfungsi untuk membeli makanan dari restoran. Pengguna diminta untuk memilih menu yang ingin dibeli dan memasukkan jumlah yang diinginkan.
cek_saldo: method ini berfungsi untuk melihat sisa saldo pengguna

Selanjutnya, Fungsi `menu_admin()` akan menampilkan pilihan menu yang bisa dipilih oleh admin seperti menambahkan menu, melihat menu, mengubah menu, menghapus menu, mencari menu, dan keluar dari menu admin.
Jika admin memilih nomor 1, maka admin akan diminta untuk memasukkan nama dan harga menu baru dan kemudian program akan menambahkan menu baru tersebut.
Jika admin memilih nomor 2, maka program akan menampilkan semua menu yang sudah ada.
Jika admin memilih nomor 3, maka program akan menampilkan semua menu dan meminta admin untuk memilih nomor menu yang ingin diubah, kemudian meminta admin untuk memasukkan nama dan harga menu baru.
Jika admin memilih nomor 4, maka program akan menampilkan semua menu dan meminta admin untuk memilih nomor menu yang ingin dihapus.
Jika admin memilih nomor 5, maka program akan menampilkan semua menu, mengurutkan menu berdasarkan harga, dan meminta admin untuk memasukkan nama menu yang ingin dicari.
Jika admin memilih nomor 6, maka admin akan keluar dari menu admin.
Jika admin memilih nomor 7, maka program akan berakhir.

Fungsi `menu_user()` akan menampilkan pilihan menu yang bisa dipilih oleh user seperti membeli makanan, mengecek saldo, keluar dari menu user, dan keluar dari program.
Jika user memilih nomor 1, maka program akan menampilkan semua menu yang ada dan meminta user untuk memilih nomor menu yang ingin dibeli dan memasukkan jumlah pesanan. Kemudian program akan mengurangi saldo user dengan harga total pesanan dan menampilkan sisa saldo user.
Jika user memilih nomor 2, maka program akan menampilkan saldo user.
Jika user memilih nomor 3, maka user akan keluar dari menu user dan kembali ke menu login.
Jika user memilih nomor 4, maka program akan berakhir.

Fungsi `create_connection()` digunakan untuk membuat koneksi ke database dengan host, username, password, dan nama database yang sudah ditentukan.

Fungsi `user_login()` akan meminta username dan password dari user dan memeriksa keberadaan username dan password tersebut di tabel user. Jika username dan password tersebut benar, maka program akan menampilkan pesan selamat datang dan menampilkan menu user. Jika username dan password tersebut salah, maka program akan menampilkan pesan login gagal.

Fungsi `create_account()` akan meminta username dan password baru dari user dan membuat akun baru dengan menggunakan INSERT query di MySQL.

Fungsi `admin_login()` akan meminta username dan password dari admin dan memeriksa keberadaan username dan password tersebut di tabel admin. Jika username dan password tersebut benar, maka program akan menampilkan pesan selamat datang dan menampilkan menu admin. Jika username dan password tersebut salah, maka program akan menampilkan pesan login gagal.

Fungsi `menu_login()` digunakan untuk menampilkan menu login yang bisa dipilih oleh user yaitu admin login dan user login. Jika user memilih nomor 1, maka program akan memanggil fungsi `admin_login()`. Jika user memilih nomor 2, maka program akan memanggil fungsi `user_login()`.



# Fitur Dan Fungsionalitas
1. tambah menu : fitur ini memiliki fungsi untuk pengguna dapat menambahkan list menu makanan pada restoran yang di akses oleh pengguna admin.
2. tampilkan menu : memungkinkan pengguna untuk dapat melihat ketersediaan menu apa saja pada restoran.
3. cari menu : memungkinkan pengguna untuk mencari dan menemukan menu yang diinginkan dalam sistem dengan memasukkan kata kunci atau frasa tertentu yang kemudian sistem akan menampilkan hasil pencarian yang relevan.
4. update menu : fitur yang memungkinkan pengguna admin untuk dapat memperbarui atau memperbaiki kesalahan dalam penginputan daftar menu pada restoran.
5. hapus menu : fitur ini memungkinkan untuk pengguna admin dapat menghapus informasi atau list menu pada restoran.
6. beli makanan : fitur ini digunakan oleh pengguna pelanggan yang memungkinkan pengguna dapat memilih dan memesan makanan yang diinginkan.
7. cek saldo : fitur ini digunakan oleh pengguna pelanggan, yang dimana memungkinkan untuk pelanggan dapat melihat sisa saldo yang dimilikinya sebelum melakukan pemesanan.
8. exit : fitur ini berfungsi untuk pengguna dapat keluar atau berhenti dari program saat telah selesai menggunkan sistem tersebut.


# Cara Penggunaan
 Cara menggunakan program ini cukup simpel dan mudah, pertama pada terminal kita dapat mengimport PrettyTable dengan cara pip install PrettyTable, lalu kita bisa mengimport pwinput dengan cara pip install pwinput. Selanjutnya kita bisa run/jalankan program  dan program akan otomatis menghubungkan ke database yang telah dihosting, kemudian akan menampilkan pilihan menu dan kita diminta untuk memilih login user, login admin, daftar akun baru, atau keluar. Jika kita memilih pilihan pertama maka kita akan masuk ke login user dan akan diminta untuk memasukkan username dan kata sandi yang telah dibuat di database sebelumnya dengan benar.Jika user memasukan nama atau password salah maka akan kembali ke pilihan menu dan diminta memilih kembali. Namun jika user berhasil login maka menu user akan menampilkan beberapa pilihan yaitu jika user memilih angka 1 maka user dapat membeli makanan yang tersedia di restoran, program otomatis menampilkan list menu makanan yang tersedia kemudian user diminta memasukkan nomor makanan yang diinginkan dan jumlah makanan yang diinginkan maka program otomatis mencetak invoice pembelian dan mengurangi saldo user sesuai dengan harga makanan yang dibeli. Jika user memilih angka 2 maka user dapat melihat saldo yang dimilikinya dan juga dapat melakukan top up saldo. Jika user memilih angka 3 maka akan keluar dari menu user dan akan kembali menampilkan menu login. Pilihan yang kedua adalah menu login admin jika kita memilih login admin maka akan menampilkan operasi CRUD yang dimana admin dapat menambah menu makanan, melihat menu makanan, mengupdate menu makanan, menghapus menu makanan pada restoran dan pada program kami juga menambahkan 2 fitur tambahan yaitu searching untuk mencari menu makanan dan sorting untuk mengurutkan nama pada menu makanan agar dapat lebih memudahkan admin. Selanjutnya jika  memilih angka 3 maka kita dapat mendaftarkan akun baru untuk admin dan dapat login sebagai admin agar dapat mengakses fitur fitur yang telah disediakan untuk memudahkan admin. Dan dipilihan keempat yaitu keluar, yang berarti kita keluar dari program.