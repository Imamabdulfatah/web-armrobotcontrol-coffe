# ☕ Web Arm Robot Control — Robot Barista Kopi

Aplikasi web berbasis **Flask** untuk mengontrol **robot lengan barista kopi** secara otomatis. Sistem ini dilengkapi dengan **deteksi wajah real-time** menggunakan webcam dan pemutaran audio sambutan, sehingga robot dapat merespons kehadiran pelanggan secara cerdas.

---

## 📌 Deskripsi Proyek

Proyek ini merupakan antarmuka web untuk Robot Barista yang dikembangkan sebagai sistem kontrol berbasis computer vision. Ketika pelanggan terdeteksi melalui kamera, sistem secara otomatis memainkan audio sambutan dan mengarahkan pengguna untuk memilih jenis kopi serta posisi penempatan gelas yang diinginkan.

### Alur Sistem:
```
Pelanggan Datang
      ↓
Deteksi Wajah (Webcam + OpenCV)
      ↓
Audio Sambutan Diputar (Pygame)
      ↓
Pilih Opsi Kopi (1 Shot / 2 Shot)
      ↓
Pilih Posisi Penempatan Gelas (1 / 2 / 3)
      ↓
Perintah dikirim ke Robot Lengan (via file komunikasi Python ↔ C++)
```

---

## 🗂️ Struktur Proyek

```
web-armrobotcontrol-coffe/
│
├── app.py                      # File utama Flask — routing & logika backend
├── ReceiveTransferC++.py       # Script komunikasi Python ↔ C++ (via file data.txt)
├── requirements.txt            # Daftar dependensi Python
│
├── templates/                  # HTML template (Jinja2)
│   ├── index.html              # Halaman utama / landing page
│   ├── deteksi.html            # Halaman deteksi wajah & streaming webcam
│   ├── kopi_opsi.html          # Halaman pemilihan jenis kopi (1 Shot / 2 Shot)
│   └── penempatan.html         # Halaman pemilihan posisi penempatan gelas
│
└── static/
    └── assets/
        ├── audio/              # File audio sambutan (opening.wav)
        ├── css/                # Stylesheet (animate.css, style.css)
        ├── images/             # Gambar robot & produk (robotKopi.jpeg, gelas.jpeg, dll.)
        └── js/                 # Library JavaScript (jQuery, Bootstrap, AOS, dll.)
```

---

## 🚀 Fitur Utama

| Fitur | Keterangan |
|---|---|
| 🎥 **Live Face Detection** | Deteksi wajah real-time dari webcam menggunakan OpenCV Haar Cascade |
| 🔊 **Audio Sambutan Otomatis** | Memainkan audio `.wav` secara otomatis saat wajah terdeteksi |
| ☕ **Pilih Jenis Kopi** | Antarmuka untuk memilih 1 Shot atau 2 Shot espresso |
| 📍 **Pilih Posisi Gelas** | Antarmuka untuk memilih posisi penempatan gelas (1, 2, atau 3) |
| 🔗 **Komunikasi Python ↔ C++** | Transfer data perintah ke program C++ melalui file `data.txt` |
| 🌐 **Web Interface** | Antarmuka web responsif menggunakan Bootstrap 5 |

---

## ⚙️ Persyaratan Sistem

- **Python** 3.8 atau lebih baru
- **Webcam** (built-in atau eksternal)
- **Sistem Operasi**: Windows / Linux / macOS
- **C++ Application** (opsional — untuk komunikasi robot arm)

---

## 📦 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/Imamabdulfatah/web-armrobotcontrol-coffe.git
cd web-armrobotcontrol-coffe
```

### 2. Buat Virtual Environment (Direkomendasikan)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Siapkan File Audio

Pastikan file audio sambutan tersedia di:
```
static/assets/audio/opening.wav
```

---

## ▶️ Menjalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di: **http://127.0.0.1:5000**

> **Catatan:** Pastikan webcam tidak sedang digunakan oleh aplikasi lain sebelum menjalankan.

---

## 🛣️ Halaman & Endpoint

| Route | Method | Fungsi |
|---|---|---|
| `/` | GET | Halaman utama (landing page Robot Barista) |
| `/deteksi` | GET | Halaman deteksi wajah dengan live video stream |
| `/video_feed` | GET | Stream MJPEG dari webcam (digunakan oleh `<img>` tag) |
| `/pilih-kopi` | GET | Halaman pemilihan jenis kopi |
| `/penempatan` | GET | Halaman pemilihan posisi penempatan gelas |
| `/start_audio` | POST | Memulai audio & mengaktifkan deteksi wajah |
| `/stop_audio` | POST | Menghentikan audio & menonaktifkan deteksi wajah |

---

## 🔧 Konfigurasi

### Mengubah Sumber Kamera
Di `app.py`, baris berikut menggunakan kamera default (index `0`):
```python
cap = cv2.VideoCapture(0)
```
Ubah angka `0` ke `1`, `2`, dst. jika menggunakan kamera eksternal.

### Mengubah File Audio
Ganti path audio di fungsi `play_sound()` pada `app.py`:
```python
pygame.mixer.music.load("static/assets/audio/opening.wav")
```

### Komunikasi dengan C++ (`ReceiveTransferC++.py`)
Sesuaikan path file `data.txt` sesuai lokasi proyek C++ Anda:
```python
file_path = 'C:/Users/admin/source/repos/KomunikasiPythonC++/.../data.txt'
```

---

## 📚 Dependensi Python

| Library | Versi Minimum | Fungsi |
|---|---|---|
| `Flask` | 2.3.0 | Framework web backend |
| `opencv-python` | 4.8.0 | Deteksi wajah & pemrosesan video |
| `numpy` | 1.24.0 | Operasi array/matriks gambar |
| `pygame` | 2.5.0 | Pemutaran audio `.wav` |

---

## 🖥️ Dependensi Frontend (CDN)

| Library | Versi | Fungsi |
|---|---|---|
| Bootstrap | 5.3.0 | Framework CSS responsif |
| jQuery | 3.6.0 | Manipulasi DOM & AJAX request |
| AOS | - | Animasi scroll |
| Owl Carousel | - | Carousel/slider komponen |
| Google Fonts | - | Font Poppins, Josefin Sans, Great Vibes |

---

## 🤝 Kontribusi

1. Fork repository ini
2. Buat branch fitur baru: `git checkout -b fitur/nama-fitur`
3. Commit perubahan: `git commit -m "Menambahkan fitur X"`
4. Push ke branch: `git push origin fitur/nama-fitur`
5. Buat Pull Request

---

## 👤 Author

**Imam Abdul Fatah**
- GitHub: [@Imamabdulfatah](https://github.com/Imamabdulfatah)

---

## 📄 Lisensi

Proyek ini dikembangkan untuk keperluan akademis di **Universitas Gunadarma**.

---

> 💡 **Tips:** Untuk penggunaan produksi, nonaktifkan mode `debug=True` pada `app.py` dan gunakan server WSGI seperti **Gunicorn** (Linux) atau **Waitress** (Windows).
