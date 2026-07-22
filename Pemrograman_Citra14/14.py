import cv2
import numpy as np

# Menyalakan kamera
video = cv2.VideoCapture(0)

# Menggunakan path bawaan OpenCV agar file XML pasti ketemu dan tidak error
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces_data = []
i = 0

while True:
    ret, frame = video.read()
    
    # Memastikan kamera berhasil membaca gambar
    if not ret:
        print("Gagal mengakses kamera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    # PERHATIKAN: Semua kode di bawah 'for' harus menjorok ke dalam (di-tab)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50))
        
        # Mengumpulkan data 1 foto setiap 10 frame
        if len(faces_data) < 100 and i % 10 == 0:
            faces_data.append(resized_img)
        i = i + 1
        
        # Menampilkan teks jumlah foto dan menggambar kotak di wajah
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    
    # Kamera akan otomatis mati jika kamu menekan 'q' ATAU jumlah foto sudah mencapai 100
    if k == ord('q') or len(faces_data) >= 100:
        break

# Merilis memori dan menutup semua jendela
video.release()
cv2.destroyAllWindows() # <- Tadi di kodemu bagian ini kurang kurung tutup