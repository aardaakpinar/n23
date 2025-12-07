# N23+ Encryption Algorithm

N23+ özel geliştirilmiş bir metin şifreleme algoritmasıdır. Temel amacı hafif, hızlı ve tahmin edilmesi zor bir şifreleme modeli sunmaktır. AES veya RSA kadar ağır değildir, ancak klasik basit şifreleme yöntemlerinden çok daha güçlü olacak şekilde tasarlanmıştır.

---

## Özellikler

### 🔐 1. Salt (Tuz) Kullanımı

Her şifreleme işleminde rastgele bir **16-bit salt** üretilir. Bu sayede:

* Aynı metin her seferinde farklı şifre üretir.
* Tekrar eden şifre blokları oluşmaz.
* Tersine mühendislik ciddi derecede zorlaşır.

Salt şifreli dizgenin en başında HEX formatında saklanır.

---

### 🔐 2. Güçlü İlk Değer

Algoritma ilk karakterin Unicode değerini şu şekilde işler:

```
(ord(first_char) + 23 + salt) ^ 3
```

Böylece herhangi bir üçüncü kişi salt olmadan ilk karakteri matematiksel olarak çıkartamaz.

---

### 🔑 3. Zincirleme Değer Hesabı

İlk değerden sonraki her karakter, önceki değer üzerinden hesaplanır:

```
new_key = previous_key + index + ord(current_char)
```

Bu yapı sayesinde her karakter bir önceki karaktere bağımlıdır.

---

### 🔢 4. HEX Tabanlı Çıktı

Tüm değerler HEX formatında saklanır ve `:` ile ayrılır.

Örnek çıktı:

```
1A2F:46308:46342:4637C:4639F
```

---

## Şifreleme Mantığı (Encrypt)

1. Rastgele bir **salt** oluşturulur.
2. İlk karakter `(ord + 23 + salt)^3` formülüyle işlenir.
3. Sonraki karakterler zincir mantığıyla işlenir.
4. Tüm değerler HEX formatına dönüştürülür.
5. Sonuç `SALT:KEY1:KEY2:KEY3:...` şeklinde döner.

---

## Çözme Mantığı (Decrypt)

1. Salt okunur.
2. İlk değer küp kökü alınarak çözülür.
3. `-23 - salt` uygulanarak ilk karakter elde edilir.
4. Zincir tersine uygulanarak tüm karakterler geri çözülür.

---

## Kullanım Örneği

### Şifreleme örneği:

```
Metin: Merhaba
Şifre: 1F4C:46308:46342:4637C:4639F:463F0:4645A:464D2
```

### Çözme örneği:

```
46308:46342:4637C → Merhaba
```

---

## Avantajlar

* Basit ama güçlü bir yapı
* Salt sayesinde yüksek tahmin edilemezlik
* HEX sayesinde kolay taşınabilir
* Tamamen reversible (geri açılabilir)
* Hafif ve hızlı

---

## Güvenlik Notu

Bu algoritma gizli iletişim, oyun içi güvenli veri aktarımı veya özel uygulamalar için uygundur. Ancak finansal, askeri veya kurumsal seviye güvenlik gerektiren ortamlarda **AES, RSA veya benzeri endüstri standardı çözümlerle birlikte** kullanılmalıdır.