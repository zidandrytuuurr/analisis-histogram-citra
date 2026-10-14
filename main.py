import cv2
import matplotlib.pyplot as plt
import os

gambar = [
    "images/gambar_gelap.jpg",
    "images/gambar_normal.jpg",
    "images/gambar_terang.jpg"
]

judul = ["Gambar Gelap", "Gambar Normal", "Gambar Terang"]

os.makedirs("hasil", exist_ok=True)

plt.figure(figsize=(10, 8))

for i in range(3):
    img = cv2.imread(gambar[i], 0)

    if img is None:
        print("Gambar tidak ditemukan:", gambar[i])
        continue

    plt.subplot(3, 2, i * 2 + 1)
    plt.imshow(img, cmap="gray")
    plt.title(judul[i])
    plt.axis("off")

    plt.subplot(3, 2, i * 2 + 2)
    plt.hist(img.ravel(), bins=256, range=(0, 256))
    plt.title("Histogram")
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")

plt.tight_layout()
plt.savefig("hasil/hasil_histogram.png")
plt.show()