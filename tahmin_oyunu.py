import random

def oyun():
    print("--- Sayı Tahmin Oyununa Hoş Geldin! ---")
    hedef_sayi = random.randint(1, 100)
    deneme_hakki = 0
    print("1 ile 100 arasında bir sayı tuttum. Bakalım bilecek misin?")

    while True:
        try:
            tahmin = int(input("Tahminin nedir?: "))
            deneme_hakki += 1

            if tahmin < hedef_sayi:
                print("Daha yüksek bir sayı söyle!")
            elif tahmin > hedef_sayi:
                print("Daha düşük bir sayı söyle!")
            else:
                puan = max(0, 100 - (deneme_hakki - 1) * 10)
                print(f"Tebrikler! {deneme_hakki} denemede bildin.")
                print(f"Toplam Puanın: {puan}")
                break
        except ValueError:
            print("Lütfen sadece sayı gir!")

if __name__ == "__main__":
    oyun()
