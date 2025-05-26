🧖‍♀️ SPA Day Assistant – Fuzzy Logic Personal Care Planner

## 📌 Proje Tanımı

**SPA Day Assistant**, kişisel bakım planlamasını optimize eden bir bulanık mantık (fuzzy logic) sistemidir. Kullanıcının ruh hali, yorgunluk seviyesi, cilt tipi, hava durumu ve günlük plan yoğunluğu gibi etkenlere göre önerilen **bakım süresi** ve **bakım tipi** bilgilerini üretir.

Bu sistem, gerçek hayatta insanlar tarafından alınan esnek kararları modellemeyi hedefleyen bulanık mantık prensipleri ile oluşturulmuş; kullanıcı dostu bir **grafik arayüz (GUI)** ile sunulmuştur.

🖼️ Arayüz Ekran Görüntüsü

![Ekran görüntüsü 2025-05-26 213855](https://github.com/user-attachments/assets/db4e90fd-e2d7-469c-9c44-906813c13a99)

![Ekran görüntüsü 2025-05-26 213927](https://github.com/user-attachments/assets/e7278e6c-3d85-4faa-b40b-6ace69c97a17)


---
## 🎯 Proje Amacı ve Hedefi

- Gündelik kişisel bakım kararlarını, sabit kurallar yerine bulanık mantıkla daha esnek biçimde modellemek.
- Kullanıcının anlık durumuna göre özelleştirilmiş bakım önerileri sunmak.
- Yapay zekâ temelli karar destek sistemlerine giriş niteliğinde bir uygulama geliştirmek.
- Python ve popüler kütüphanelerle entegre, görsel arayüze sahip bir proje üretmek.

---

## 🧠 Kullanılan Teorik Altyapı

Proje, aşağıdaki temel kavramlara dayanmaktadır:

- **Bulanık Mantık (Fuzzy Logic):** Klasik mantığın aksine, “evet” veya “hayır” yerine ara değerlerin değerlendirilebildiği, esnek karar yapıları sunar.
- **Üyelik Fonksiyonları (Membership Functions):** Girdilerin hangi oranda belirli etiketlere (örn. "yüksek", "düşük") ait olduğunu belirler. Ben üçgen üyelik fonksiyonlarını kullandım.
- **Kurallar (Rules):** “Eğer... ise...” şeklinde tanımlanarak, uzman bilgisi temelli sistemin karar vermesini sağlar.

---

## ⚙️ Kullanılan Yöntemler ve Teknolojiler

### 🔧 Girdi Değişkenleri

| Girdi        | Dilsel Etiketler         |
|--------------|---------------------------|
| Yorgunluk     | düşük, orta, yüksek       |
| Ruh Hali      | stresli, orta, çok iyi    |
| Cilt Durumu   | kuru, normal, yağlı       |
| Hava Durumu   | kapalı, orta, güneşli     |
| Günlük Plan   | boş, orta, yoğun          |

### 🎯 Çıktı Değişkenleri

| Çıktı         | Dilsel Etiketler         |
|---------------|---------------------------|
| Bakım Süresi   | kısa, orta, uzun          |
| Bakım Tipi     | hafif, orta, yoğun        |

### 💻 Kullanılan Kütüphaneler

- `numpy` – Sayısal hesaplamalar için
- `scikit-fuzzy` – Bulanık mantık modelleme için
- `tkinter` – Arayüz (GUI) oluşturmak için
- `matplotlib` – Grafik çizimleri için
- `Pillow` – Görsel destek (ikona dayalı öğeler için)

---

## 📁 Dosya Yapısı

SPA_day_fuzzylogic/
│
├── |main.py # Uygulamanın başlangıç noktası (GUI çalıştırma)|
├── |fuzzy_model.py # Bulanık sistem tanımlamaları|
├── |gui.py # Arayüz ve kullanıcı etkileşimi|
├── |requirements.txt # Projeye özel gerekli kütüphaneler|
└── |README.md |

## 🖥️ Kurulum ve Çalıştırma Adımları

### 1️⃣ Depoyu Klonlayın

```bash
git clone https://github.com/kullanici-adiniz/SPA_day_fuzzylogic.git
cd SPA_day_fuzzylogic
2️⃣ Sanal Ortam 
bash
Kopyala

python -m venv venv
3️⃣ Sanal Ortamı Aktif Edin
Windows:

bash
Kopyala
Düzenle
venv\Scripts\activate

4️⃣ Gerekli Paketleri Yükleyin
bash
Kopyala
Düzenle
pip install -r requirements.txt
5️⃣ Uygulamayı Başlatın
bash
Kopyala
Düzenle
python main.py
🧪 Kullanım Talimatları
Arayüzde her giriş alanı için uygun seçenekleri açılır listelerden seçin.

“Hesapla” butonuna basarak sonucu görüntüleyin.

Bakım süresi ve tipi ekranda gösterilecektir.

Ek olarak sonuçlar grafiksel olarak da sunulur.
