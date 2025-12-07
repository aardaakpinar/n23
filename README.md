# 🛡️ N23 ve N23+ Şifreleme Algoritmaları

Bu belge, basit, eğitim amaçlı şifreleme/gizleme algoritmaları olan **N23** ve onun geliştirilmiş versiyonu **N23+** hakkındaki teknik bilgileri ve güvenlik değerlendirmesini sunmaktadır.

---

## 📝 1. N23: Anahtarsız Obfuscation (Gizleme)

N23, veriyi rastgele bir tuz (salt) ve verinin ilk karakterine dayalı olarak gizleyen (obfuscation) bir yöntemdir. Gizli bir anahtar kullanmaz.

### ⚙️ Çalışma Prensibi

1.  **Tuz (Salt) Ekleme:** 1000 ile 9999 arasında rastgele bir tam sayı (`salt`) üretilir ve çıktının ilk bölümünü oluşturur.
2.  **İlk Değer Hesaplama (Kübik):** İlk şifreli değer (`key`) aşağıdaki formülle hesaplanır:
    $$
    \text{key} = (\text{ord}(\text{text}[0]) + 23 + \text{salt})^3
    $$
3.  **Zincirleme Hesaplama (Ekleme):** Sonraki her karakter için, yeni şifreli değer, bir önceki değere karakterin ASCII değeri ve karakterin indeksi (`i`) eklenerek bulunur:
    $$
    \text{cur} = \text{prev} + i + \text{ord}(\text{text}[i])
    $$
4.  Tüm değerler **Hexadecimal** (16'lık) formata çevrilir ve `:` ile birleştirilir.

### ⚠️ Güvenlik Notu

N23, **güvenli değildir** ve yalnızca veriyi okunamayacak hale getirir. Şifreleme anahtarı metnin kendisinden türetildiği için, şifreli metni bilen herkes, herhangi bir gizli bilgiye ihtiyaç duymadan deşifre edebilir.

---

## 🔒 2. N23+: Anahtarlı Gelişmiş Şifreleme

N23+, kullanıcı tarafından sağlanan **gizli bir anahtar (Key)** eklenerek N23'ün güvenliğini artıran versiyonudur.

### ⚙️ Çalışma Prensibi ve Geliştirmeler

N23+'da, N23'e ek olarak bir gizli anahtar kullanılır ve anahtarın rastgeleliğini artırmak için kriptografik işlemler uygulanır:

1.  **Anahtar Güçlendirme:** Kullanıcı anahtarı, güçlü bir karma fonksiyonu olan **SHA-256** kullanılarak 32 baytlık (256 bit) sabit materyale dönüştürülür.
    $$
    \text{KeyBytes} = \text{SHA-256}(\text{User Key})
    $$
2.  **Anahtar ile Karıştırma (Tweak):**
    * **İlk Değer:** Hesaplamaya, SHA-256 çıktısının ilk iki baytından türetilen bir gizli **tweak0** değeri eklenir.
    * **Zincirleme Değerler:** Zincirleme hesaplamanın her adımında, gizli anahtar materyalinden seçilen dönen bir **tweak** baytı eklenir.
        $$
        \text{cur} = \text{prev} + i + \text{ord}(\text{text}[i]) + \mathbf{tweak}
        $$

### 📈 Güvenlik Değerlendirmesi

N23+, **simetrik şifreleme** prensibini uygular. Anahtar, deşifreleme için zorunludur.

* **Avantaj:** Gizli anahtar olmadan şifreli metin kırılamaz, bu da N23'e göre önemli bir güvenlik artışı sağlar.
* **Uyarı:** Bu, ticari veya hassas verilerin korunması için tasarlanmış, standart bir algoritma **değildir**. Hassas veriler için **AES** gibi endüstriyel standartlar kullanılmalıdır.

---

## 🔎 3. Özet Karşılaştırma

| Özellik | N23 (Anahtarsız) | N23+ (Anahtarlı) |
| :--- | :--- | :--- |
| **Gizli Anahtar** | Hayır | **Evet** (Gerekli) |
| **Anahtar Kullanımı** | Metinden türetilir | **SHA-256 ile güçlendirilir** |
| **Güvenlik Seviyesi** | Zayıf (Gizleme) | **Orta** (Anahtarlı Gizlilik) |
| **Deşifreleme** | Şifreli metin yeterli | **Şifreli metin + Gizli Anahtar gerekli** |
