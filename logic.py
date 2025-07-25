import datetime
import aiohttp
import random
from datetime import datetime, timedelta

from config import token  # Token'ı config dosyasından çekiyoruz --- IGNORE ---
def rastgele_baslangic(min=30, max=60):
    return random.randint(min, max)
def rastgele_saglik(min=1000, max=4000):
    return random.randint(min, max)
def rastgele_guc(min=5, max=15):
    return random.randint(min, max)
def rastgele_sayi(min=1, max=5):
    return random.randint(min, max)
class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):

        self.last_feed_time = datetime.now() - timedelta(seconds=1000)
        self.feed_count = 0       # 🔧 Besleme sayacı eklendi
        self.level = 1            # 🔧 Seviye takip sistemi eklendi
        self.power = random.randint(30,60) # ✅ Güç değeri rastgele atanıyor
        self.hp = rastgele_saglik(1000, 4000)  # ✅ Sağlık değeri rastgele atanıyor

        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.feed_count = 0       # 🔧 Besleme sayacı eklendi
        self.level = 1            # 🔧 Seviye takip sistemi eklendi

        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            existing = Pokemon.pokemons[pokemon_trainer]
            self.__dict__ = existing.__dict__  # Mevcut verileri aynen yükle

    async def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['forms'][0]['name']
                else:
                    return "Pikachu"

    async def info(self):
        if not self.name:
            self.name = await self.get_name()
        return f"Pokémonunuzun ismi: {self.name} | Seviye: {self.level} | Besleme Sayısı: {self.feed_count}"

    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['sprites']['front_default']
                else:
                    return None



    async def attack(self, enemy):
        if isinstance(enemy, Wizard):  # Düşmanın Wizard veri tipi olup olmadığını kontrol ediyoruz
            chance = random.randint(1, 5)  # Sihirbazın kalkan şansı %20
            if chance == 1:
                return "Sihirbaz Pokémon, savaşta bir kalkan kullandı!"

        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ne saldırdı\n@{enemy.pokemon_trainer}'nin sağlık durumu şimdi {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ni yendi!"
    async def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            self.feed_count += 1  # Besleme sayısı artmalı!
            return f"{self.name} beslendi! Yeni sağlık: {self.hp}"
        else:
            kalan_saniye = int((self.last_feed_time + delta_time - current_time).total_seconds())
            return f"{self.name} şu kadar saniye sonra tekrar beslenebilir: {kalan_saniye}s"



class Wizard(Pokemon):
    def feed(self):
        super().feed(hp_increase=25)  # Sihirbaz daha az beslenmeli!





class Fighter(Pokemon):
    async def attack(self, enemy):
        if rastgele_guc(5,15) > 9:  # ✅ Süper saldırı şansına göre mesaj verilir ama gerçek saldırı yapılmaz!
            return "Dövüşçü Pokémon, savaşta süper saldırı kullandı!"
        
        super_power = rastgele_guc(10,15)  # ✅ Güç artırımı burada tanımlandı (önceden globaldi — hata çıkarırdı)
        self.power += super_power  # ✅ Saldırı öncesi güce ekleniyor
        sonuc = await super().attack(enemy)  # ✅ Normal saldırı uygulanıyor
        self.power -= super_power  # ✅ Güç değeri eski haline getiriliyor
        return sonuc + f"\nDövüşçü Pokémon süper saldırı kullandı. Eklenen güç: {self.power + super_power} (önceki güç: {self.power})"  # ✅ Saldırı sonrası bilgi mesajı ekleniyor. Artırılan güç doğru şekilde gösteriliyor.

    def feed(self):
        super().feed(feed_interval=5)  # Dövüşçü daha sık beslenebilir!
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))