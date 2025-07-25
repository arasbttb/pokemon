import datetime
import discord
from discord.ext import commands

from config import token  # token.py dosyasından botun token'ını içe aktarıyoruz
from logic import Pokemon
import time
# Bot için yetkileri/intents ayarlama
intents = discord.Intents.default()  # Varsayılan ayarların alınması
intents.messages = True              # Botun mesajları işlemesine izin verme
intents.message_content = True       # Botun mesaj içeriğini okumasına izin verme
intents.guilds = True                # Botun sunucularla çalışmasına izin verme

# Tanımlanmış bir komut önekine ve etkinleştirilmiş amaçlara sahip bir bot oluşturma
bot = commands.Bot(command_prefix='!', intents=intents)







@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  # Botun adını konsola çıktı olarak verir

import discord
from discord.ext import commands
from logic import Pokemon  # Pokemon sınıfını dışarıdan çekiyoruz

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Giriş yapıldı: {bot.user.name}")

@bot.command()
async def go(ctx):
    author = ctx.author.name
    if author not in Pokemon.pokemons:
        pokemon = Pokemon(author)
        await ctx.send(await pokemon.info())
        image_url = await pokemon.show_img()
        if image_url:
            embed = discord.Embed(
                title=f"{author} için Pokémon!",
                color=discord.Color.green()
            )
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Pokémonun görüntüsü yüklenemedi!")
    else:
        await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")

@bot.command()
async def sil(ctx):
    author = ctx.author.name
    if author in Pokemon.pokemons:
        del Pokemon.pokemons[author]
        await ctx.send(f"{author} adlı Pokémon silindi. 😢")
    else:
        await ctx.send("Silinecek bir Pokémon bulunamadı. Önce '!go' ile oluşturmalısınız.")


@bot.command()
async def feed(ctx):
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[author]
        response = await pokemon.feed()  # feed fonksiyonu çağrılıyor
        await ctx.send(response)         # gelen mesaj Discord'da gösteriliyor
    else:
        await ctx.send("Önce bir Pokémon oluşturmalısınız! '!go' komutunu kullanın.")




async def feed(self, feed_interval=20, hp_increase=10):
    current_time = datetime.now()
    delta_time = datetime.timedelta(seconds=feed_interval)
    if (current_time - self.last_feed_time) > delta_time:
        self.hp += hp_increase
        self.last_feed_time = current_time
        return f"Pokémon'un sağlığı geri yüklenir. Mevcut sağlık: {self.hp}"
    else:
        return f"Pokémonunuzu şu zaman besleyebilirsiniz: {current_time+delta_time}"


@bot.command()
async def info(ctx):
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[author]
        await ctx.send(await pokemon.info())
    else:
        await ctx.send("Önce bir Pokémon oluşturmalısınız! '!go' komutunu kullanın.")


@bot.command()
async def attack(ctx):
    target = ctx.message.mentions[0] if ctx.message.mentions else None  # Mesajda belirtilen kullanıcıyı alırız
    if target:  # Kullanıcının belirtilip belirtilmediğini kontrol ederiz
        # Hem saldırganın hem de hedefin Pokémon sahibi olup olmadığını kontrol ederiz
        if target.name in Pokemon.pokemons and ctx.author.name in Pokemon.pokemons:
            enemy = Pokemon.pokemons[target.name]  # Hedefin Pokémon'unu alırız
            attacker = Pokemon.pokemons[ctx.author.name]  # Saldırganın Pokémon'unu alırız
            result = await attacker.attack(enemy)  # Saldırıyı gerçekleştirir ve sonucu alırız
            await ctx.send(result)  # Saldırı sonucunu göndeririz
        else:
            await ctx.send("Savaş için her iki tarafın da Pokémon sahibi olması gerekir!")  # Katılımcılardan birinin Pokémon'u yoksa bilgilendiririz
    else:
        await ctx.send("Saldırmak istediğiniz kullanıcıyı etiketleyerek belirtin.")  # Saldırmak için kullanıcıyı etiketleyerek belirtmesini isteriz











bot.run(token)

