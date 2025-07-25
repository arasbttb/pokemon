# 🐾 Pokenmon Battle Simulator

Bu proje, Pokémon evreninden ilham alınarak geliştirilmiş bir dövüş simülatörüdür. Her karakterin kendine özgü türü, sağlık durumu ve beslenme alışkanlıkları vardır. Dövüşçü karakterler diğer Pokémon’lardan daha sık beslenebilir. Projenin amacı, karakterlerin davranışlarını ve enerji yönetimini simüle etmektir.

## 🚀 Özellikler
- Farklı türlerde Pokémon sınıfları (`Pokemon`, `FighterPokemon`)
- Beslenme sistemi ve sağlık yönetimi
- Miras alma (inheritance) ve metod ezmesi (override)
- Basit terminal tabanlı etkileşim

## 📁 Dosya Yapısı
pokenmon/ ├── logic.py # Temel sınıflar ve beslenme algoritması ├── main.py # Simülasyonun başlangıç noktası └── README.md # Proje hakkında bilgi


## 💡 Kullanım
1. Projeyi indir veya klonla:
   ```bash
   git clone https://github.com/kullaniciAdi/pokenmon.git
Ana dosyayı çalıştır:

bash
python main.py
## 🧠 Karakterler
Pokemon: Genel karakter sınıfı, temel sağlık ve beslenme davranışı içerir.

FighterPokemon: Dövüşçü karakter; daha kısa beslenme aralığıyla sağlık yönetimini temsil eder.

## 🌱 Beslenme Sistemi
Her karakter belirli aralıklarla beslenir. Bu aralık feed_interval parametresi ile kontrol edilir:

python
super().feed(feed_interval=5)  # Dövüşçü karakter için daha sık beslenme 

## 📌 Gereksinimler
Python 3.x

## 👨‍💻 Geliştirici
Aras Bartu Teber – Kodlama ve dövüş simülasyonuna tutku duyan geliştirici

Bu proje tamamen öğrenme ve eğlenme amacıyla geliştirilmiştir. Katkıda bulunmak istersen, pull request gönderebilirsin! 🧪⚡



## 🕹️Nasıl Yardım alacağım?⚡
!info komudunu kullan ve config.py dosyasına tokenini koy ve herşey hazır.⚡
<img width="498" height="530" alt="image" src="https://github.com/user-attachments/assets/a4bb70a7-497a-4c8c-94f2-10c3a0ccdab8" />

