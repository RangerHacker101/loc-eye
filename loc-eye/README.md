# LocEye

**LocEye** adalah tools OSINT yang dibuat oleh *Ranger Hacker* untuk mengekstrak metadata GPS dari gambar (EXIF) dan mengidentifikasi lokasi pengambilan gambar.

## 🔍 Fitur

- Mengekstrak koordinat dari metadata gambar (EXIF)
- Menampilkan tautan Google Maps
- CLI ringan yang bisa dijalankan di Termux, Kali Linux, dsb

## 🚀 Instalasi

```bash
git clone https://github.com/username/loc-eye.git
cd loc-eye
pip install -r requirements.txt
```

## ⚙️ Cara Pakai

```bash
python3 loc_eye.py path/to/image.jpg
```

## 🧪 Contoh Output

```text
[+] Latitude: -6.1754
[+] Longitude: 106.8272
[+] Google Maps: https://www.google.com/maps?q=-6.1754,106.8272
```

## 👣 Catatan

- Foto dari WhatsApp sering kehilangan metadata
- Gunakan gambar asli dari kamera untuk hasil maksimal

## 👤 Author

Dibuat oleh: **Ranger Hacker**

## 📄 Lisensi

MIT License
