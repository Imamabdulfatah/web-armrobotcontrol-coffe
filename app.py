import cv2
import numpy as np
import pygame
from flask import Flask, render_template, Response, request

app = Flask(__name__)

# Load model deteksi wajah menggunakan OpenCV (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inisialisasi pygame untuk memutar suara
pygame.mixer.init()

# Status deteksi dan audio
audio_playing = False  # Apakah audio sedang dimainkan
face_detected = False  # Apakah wajah sedang terdeteksi
detection_active = True  # Apakah mode deteksi wajah aktif

# Fungsi untuk memutar audio
def play_sound():
    global audio_playing
    pygame.mixer.music.load("static/assets/audio/opening.wav")
    pygame.mixer.music.play()
    audio_playing = True

# Fungsi untuk menghentikan audio
def stop_sound():
    global audio_playing
    pygame.mixer.music.stop()
    audio_playing = False

# Fungsi untuk menangkap gambar dari webcam
def gen_frames():
    global face_detected, audio_playing, detection_active
    cap = cv2.VideoCapture(0)  # Menggunakan webcam default

    while True:
        success, frame = cap.read()
        if not success or not detection_active:  # Hentikan deteksi jika dinonaktifkan
            break
        else:
            # Konversi gambar ke grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Deteksi wajah
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            if len(faces) > 0:
                if not face_detected:  # Jika wajah baru terdeteksi
                    face_detected = True
                    if not audio_playing:  # Hanya mainkan audio jika belum bermain
                        play_sound()
            else:
                # Reset status jika tidak ada wajah yang terdeteksi
                face_detected = False
                if not pygame.mixer.music.get_busy():  # Audio telah selesai
                    audio_playing = False

            # Gambar kotak di sekitar wajah yang terdeteksi
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Konversi gambar ke format yang dapat dikirim ke browser (JPEG)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
    cap.release()

# Route untuk menampilkan halaman utama
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deteksi')
def detect():
    return render_template('deteksi.html')

@app.route('/pilih-kopi')
def pilihkopi():
    return render_template('kopi_opsi.html')


@app.route('/penempatan')
def penempatan():
    return render_template('penempatan.html')

# Route untuk streaming video dari webcam
@app.route('/video_feed')
def video_feed():
    global detection_active
    detection_active = True  # Aktifkan deteksi wajah saat stream dimulai
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Endpoint untuk memulai audio
@app.route('/start_audio', methods=['POST'])
def start_audio():
    global detection_active
    detection_active = True  # Aktifkan deteksi wajah
    play_sound()
    return "Audio Started", 200

# Endpoint untuk menghentikan audio dan deteksi wajah
@app.route('/stop_audio', methods=['POST'])
def stop_audio():
    global detection_active
    stop_sound()
    detection_active = False  # Nonaktifkan deteksi wajah
    return "Audio and Detection Stopped", 200

if __name__ == '__main__':
    app.run(debug=True)
