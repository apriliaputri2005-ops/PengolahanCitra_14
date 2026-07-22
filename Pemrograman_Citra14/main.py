import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime
import os

# 1. Memuat Gambar Referensi Wajah
# Ganti 'wajah_ku.jpg' dengan nama file fotomu sendiri
# Sistem akan mengekstrak fitur wajahmu menjadi vektor angka (encoding)
known_image = face_recognition.load_image_file("user.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Menyimpan encoding dan nama orang tersebut
known_faces_encodings = [known_encoding]
known_faces_names = ["jerome polin"] # Ganti dengan namamu

# 2. Menyiapkan Pencatatan CSV (Log Absensi)
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
csv_filename = f"Absensi_{current_date}.csv"

# Membuka file CSV untuk ditambahkan data (append)
f = open(csv_filename, 'a+', newline='')
lnwriter = csv.writer(f)

# Mengecek apakah file kosong, jika iya, tambahkan Header (Judul Kolom)
f.seek(0)
if os.stat(csv_filename).st_size == 0:
    lnwriter.writerow(['Nama', 'Waktu Kedatangan'])

# Variabel penyimpan nama yang sudah absen (Fitur Anti Double-Record)
recorded_names = set()

# 3. Menyalakan Kamera Real-Time
video_capture = cv2.VideoCapture(0)
print("Sistem Presensi Aktif. Tekan 'q' untuk keluar.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Gagal mengakses kamera.")
        break
    
    # Memperkecil resolusi frame agar pemrosesan wajah lebih cepat
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    # Mengubah format warna dari BGR (OpenCV) ke RGB (face_recognition)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Menemukan lokasi wajah dan membuat encoding pada frame saat ini
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Mencocokkan wajah di kamera dengan wajah referensi
        matches = face_recognition.compare_faces(known_faces_encodings, face_encoding)
        name = "Tidak Dikenal"
        
        # Mencari tingkat kemiripan terbaik (jarak terdekat antar vektor)
        face_distances = face_recognition.face_distance(known_faces_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name = known_faces_names[best_match_index]

        # Mengembalikan skala koordinat wajah ke ukuran asli (dikali 4)
        top, right, bottom, left = face_location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Menggambar kotak dan nama di sekitar wajah
        color = (0, 255, 0) if name != "Tidak Dikenal" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # 4. Fitur Anti Double-Record ke File CSV
        if name != "Tidak Dikenal" and name not in recorded_names:
            current_time = datetime.now().strftime("%H:%M:%S")
            lnwriter.writerow([name, current_time])
            f.flush() # Memastikan data langsung tersimpan
            recorded_names.add(name)
            print(f"Berhasil absen: {name} pada {current_time}")

    # Menampilkan jendela video
    cv2.imshow("Sistem Presensi Wajah", frame)
    
    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Membersihkan program
video_capture.release()
cv2.destroyAllWindows()
f.close()