import cv2
import numpy as np
import matplotlib.pyplot as plt

# Memuat model Haar Cascade (menggunakan path bawaan cv2 agar aman di VS Code)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def adjusted_detect_face(img):
    face_img = img.copy()
    # Mengubah ke grayscale (direkomendasikan untuk Haar Cascade)
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    face_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
    return face_img

def detect_eyes(img):
    eye_img = img.copy()
    gray = cv2.cvtColor(eye_img, cv2.COLOR_BGR2GRAY)
    eye_rect = eye_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    
    for (x, y, w, h) in eye_rect:
        cv2.rectangle(eye_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
    return eye_img

# Pastikan file foto 'user.avif' ada di folder yang sama dengan skrip ini
# Jika foto bernama lain, ganti nama 'user.jpg' di bawah ini
img = cv2.imread('user.jpg')

# Validasi jika gambar tidak ditemukan
if img is None:
    print("Error: Gambar tidak ditemukan!")
    exit()

img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()

# 1. Menampilkan Deteksi Wajah
face = adjusted_detect_face(img_copy1)
plt.figure(figsize=(8,6))
plt.title("Face Detection")
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
cv2.imwrite('face.jpg', face)

# 2. Menampilkan Deteksi Mata
eyes = detect_eyes(img_copy2)
plt.figure(figsize=(8,6))
plt.title("Eye Detection")
plt.imshow(cv2.cvtColor(eyes, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
cv2.imwrite('eyes.jpg', eyes)

# 3. Menampilkan Deteksi Wajah dan Mata Sekaligus
eyes_face = adjusted_detect_face(img_copy3)
eyes_face = detect_eyes(eyes_face) # Menambahkan deteksi mata ke gambar yang sudah ada kotak wajahnya
plt.figure(figsize=(8,6))
plt.title("Face & Eye Detection")
plt.imshow(cv2.cvtColor(eyes_face, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
cv2.imwrite('face+eyes.jpg', eyes_face)