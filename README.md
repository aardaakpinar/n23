# N²³ (n23)

**N²³**, bir kelimenin ilk harfini *anahtar* olarak kullanıp; harfleri `(code + key)²`, rakamları `((digit + key) mod 10)³` biçiminde dönüştüren, öğretici amaçlı bir kriptografi denemesidir. Bu repo, algoritmanın açıklamasını, canlı demoyu ve kullanım örneklerini içerir.

> ⚠️ **Güvenlik Uyarısı:** N²³, modern saldırılara karşı güvenli kabul edilemez. Üretim ortamında gerçek gizlilik için standart, kanıtlanmış şemalar (AES, ChaCha20-Poly1305, libsodium vb.) kullanın.

---

## N²³ Hakkında
N²³; anahtarı, kelimenin ilk karakterinin Unicode değeri olarak belirler. Harfler için `(code + key)²`; rakamlar için `((digit + key) mod 10)³` uygulanır. Şifreli temsilde, her **kelime** şu formattadır:

```

<keyChar> <n1> <n2> <n3> ...

````

Birden fazla kelime şifrelerken her kelimeyi **yeni satıra** yazın.

---

## Özellikler
- 🔐 **Matematik tabanlı dönüşümler**: Kare/küp işlemleri.
- 🌍 **Unicode desteği**: Latin ve yaygın alfabelerle çalışır.
- 🧮 **Deterministik**: Aynı girdi → aynı çıktı.
- 🧪 **Canlı Demo**: Tarayıcıda tek dosya ile çalışır (GitHub Pages).

---

## Bunu kullanarak neler yapılır?
- ✏️ **Eğitim**: Sayısal dönüşümlerle temel kripto kavramlarını öğretmek.
- 🔎 **Alıştırma**: Kare/küp, kök alma, mod aritmetiği pratikleri.
- 🧩 **Bulmaca**: Basit şifreleme oyunları, sınıf içi etkinlikler.

---

## Canlı Demo
Repo GitHub Pages ile otomatik yayınlanır:

- **URL**: `https://aardaakpinar.github.io/n23/`
- Push sonrası workflow kendiliğinden dağıtır.

---

## Algoritma Nasıl Çalışır?

### Şifreleme
1) **Anahtar**: Kelimenin ilk karakteri `keyChar`. `key = keyChar.codePointAt(0)`
2) **Harf**: `enc = (codePoint + key)²`
3) **Rakam**: `enc = ((digit + key) mod 10)³`
4) **Format**: Çıktı, `keyChar` + şifreli sayı listesi. Birden fazla kelimeyi yeni satıra yazın.

### Şifre Çözme
1) **Anahtar**: Satırın ilk karakteri `keyChar` → `key`.
2) **Tam kare** ise `sqrt(enc) - key` → harf (geçerli Unicode).
3) **Tam küp** ise `cbrt(enc)` → `x` → `(x - key) mod 10` → rakam.
4) Hatalı/uyuşmayan değerlerde satır içinde `�` yer tutucu gösterilir.

> Not: Boşluklar kelime ayırıcıdır, yani her satır **bir kelime** kabul edilir.
