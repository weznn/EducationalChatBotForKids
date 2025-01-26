import random

# Bot'un selamlaması
def greet_user():
    greetings = [
        "Merhaba! Ben bilgi dostu bot. Sana bir şeyler öğretebilirim. 😊",
        "Selam! Eğlenirken öğrenmeye hazır mısın? 🎉",
        "Merhaba küçük kaşif! Hadi başlayalım. 🚀"
    ]
    return random.choice(greetings)

# Eğitici içerik sunan bir fonksiyon
def provide_info(topic):
    facts = {
        "hayvanlar": [
            "Zürafaların dili 50 cm'ye kadar uzayabilir!",
            "Karıncalar, kendi ağırlıklarının 50 katını taşıyabilir.",
            "Deniz atları eşleriyle ömür boyu birlikte yaşar."
        ],
        "bilim": [
            "Güneş, yaklaşık 1.3 milyon Dünya'yı içine sığdırabilir!",
            "Bir ışık yılı, yaklaşık 9.46 trilyon kilometredir.",
            "Dünyanın merkezindeki sıcaklık, Güneş'in yüzeyi kadar sıcaktır!"
        ],
        "doğa": [
            "Amazon Ormanları, dünyadaki oksijenin %20'sini üretir.",
            "Dünyadaki en uzun nehir Nil Nehri'dir.",
            "Bir ağacın kökleri, toprağın altına 20 metre kadar uzayabilir."
        ]
    }
    return random.choice(facts.get(topic, ["Bu konuda bilgi bulamadım. 😅"]))

# Ana chatbot fonksiyonu
def chatbot():
    print(greet_user())
    print("Hangi konuda bilgi almak istersin? Hayvanlar, Bilim veya Doğa? (Çıkmak için 'çık' yazabilirsin.)")

    while True:
        user_input = input("Seçimin: ").lower()
        if user_input == "çık":
            print("Görüşürüz! Bir dahaki sefere tekrar öğrenelim. 👋")
            break
        elif user_input in ["hayvanlar", "bilim", "doğa"]:
            print(provide_info(user_input))
        else:
            print("Bu konuyu bilmiyorum. Lütfen 'hayvanlar', 'bilim' veya 'doğa' seç. 😊")

# Chatbot'u çalıştır
if __name__ == "__main__":
    chatbot()

