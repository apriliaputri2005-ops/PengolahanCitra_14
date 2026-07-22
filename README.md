# Praktikum 14: Sistem Pengenalan Wajah (Face Recognition)

Repositori ini berisi implementasi dari *pipeline* dasar pengenalan wajah, mulai dari pendeteksian wajah sederhana menggunakan algoritma klasik hingga pembuatan sistem presensi otomatis berbasis vektor fitur[cite: 3].

## Daftar Tugas & Fitur

### 1. Tugas 1: Deteksi Wajah Dasar (Haar Cascade)
Fokus pada **Fase Deteksi Wajah** untuk menemukan lokasi dan batas (*bounding box*) wajah di dalam gambar mentah atau video[cite: 3].
*   **Deteksi Gambar Statis:** Mengenali letak wajah dan mata pada sebuah foto menggunakan pola hitam-putih dari `haarcascade_frontalface_default.xml` dan `haarcascade_eye.xml`[cite: 3].
*   **Pengumpulan Data (*Real-time*):** Mengakses *webcam* untuk mendeteksi wajah secara langsung, lalu secara otomatis memotong (*crop*) dan menormalisasi ukuran (*resize*) gambar untuk mengumpulkan 100 sampel data wajah[cite: 3].

### 2. Tugas 2: Sistem Presensi Kehadiran
Mengimplementasikan **Fase Ekstraksi Fitur dan Pencocokan** untuk memverifikasi identitas pengguna[cite: 3].
*   **Ekstraksi Fitur:** Mengonversi piksel gambar wajah menjadi representasi numerik (*encoding* / vektor) menggunakan *library* `face_recognition`[cite: 3].
*   **Pencocokan Identitas:** Membandingkan jarak (*distance*) vektor wajah dari kamera dengan data referensi wajah yang sudah didaftarkan[cite: 3].
*   **Pencatatan Otomatis (CSV):** Mencatat nama wajah yang berhasil dikenali beserta waktu kehadirannya ke dalam file `.csv`. Sistem ini dilengkapi fitur anti *double-record* agar satu orang tidak dicatat berulang kali dalam satu sesi[cite: 3].

## Persyaratan (Dependencies)
Pastikan Anda telah menginstal *library* berikut sebelum menjalankan skrip:
```bash
pip install opencv-python numpy matplotlib cmake dlib face_recognition

# PengolahanCitra_14
