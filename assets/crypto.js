function harfToSayi(harf) {
  return harf.codePointAt(0)
}

function sayiToHarf(sayi) {
  return String.fromCodePoint(sayi)
}

function sifreleMetin() {
  const metin = document.getElementById("inputText").value.trim()
  if (!metin) {
    showAlert("Lütfen şifrelenecek metni girin.", "warning")
    return
  }

  const kelimeler = metin.split(" ")
  const sonuc = []

  kelimeler.forEach((kelime) => {
    if (!kelime) return

    const karakterler = Array.from(kelime)
    const anahtarHarf = karakterler[0]
    const anahtarDeger = harfToSayi(anahtarHarf)
    const kaydirma = anahtarDeger

    const sifreliKelime = [anahtarHarf]

    for (let i = 1; i < karakterler.length; i++) {
      const char = karakterler[i]

      if (char.match(/\p{L}/u)) {
        // Harf ise
        const deger = harfToSayi(char)
        const yeniDeger = deger + kaydirma
        sifreliKelime.push(yeniDeger ** 2)
      } else if (char.match(/[0-9]/)) {
        // Rakam ise
        const deger = Number.parseInt(char)
        const yeniDeger = (deger + kaydirma) % 10
        sifreliKelime.push(yeniDeger ** 3)
      } else {
        // Diğer karakterler
        sifreliKelime.push(char)
      }
    }

    sonuc.push(sifreliKelime.join(" "))
  })

  document.getElementById("outputText").value = sonuc.join("  ")
  showAlert("Metin başarıyla şifrelendi!", "success")
}

function cozMetin() {
  const sayilar = document.getElementById("inputText").value.trim()
  if (!sayilar) {
    showAlert("Lütfen çözülecek şifreli metni girin.", "warning")
    return
  }

  const kelimeler = sayilar.split(/\s{2,}/)
  const orijinal = []

  kelimeler.forEach((kelime) => {
    if (!kelime) return

    const parcalar = kelime.trim().split(" ")
    const anahtarHarf = parcalar[0]
    const liste = parcalar.slice(1)
    const anahtarDeger = harfToSayi(anahtarHarf)
    const kaydirma = anahtarDeger

    let kelimeCoz = anahtarHarf

    for (let sayi of liste) {
      if (!isNaN(sayi)) {
        sayi = Number(sayi)
        const kareKok = Math.sqrt(sayi)
        const kupKok = Math.cbrt(sayi)

        if (Number.isInteger(kareKok)) {
          // Kare sayı - harf
          const eskiDeger = kareKok - kaydirma
          kelimeCoz += sayiToHarf(eskiDeger)
        } else if (Number.isInteger(kupKok)) {
          // Küp sayı - rakam
          const eskiDeger = (kupKok - kaydirma + 10 * 2) % 10
          kelimeCoz += eskiDeger
        } else {
          kelimeCoz += "?"
        }
      } else {
        // Diğer karakterler
        kelimeCoz += sayi
      }
    }

    orijinal.push(kelimeCoz)
  })

  document.getElementById("outputText").value = orijinal.join(" ")
  showAlert("Şifre başarıyla çözüldü!", "success")
}

function clearFields() {
  document.getElementById("inputText").value = ""
  document.getElementById("outputText").value = ""
  showAlert("Alanlar temizlendi.", "info")
}

function copyResult() {
  const outputText = document.getElementById("outputText")
  if (outputText.value.trim() === "") {
    showAlert("Kopyalanacak sonuç bulunamadı.", "warning")
    return
  }

  outputText.select()
  document.execCommand("copy")
  showAlert("Sonuç panoya kopyalandı!", "success")
}

function showAlert(message, type) {
  // Create alert element
  const alertDiv = document.createElement("div")
  alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`
  alertDiv.style.cssText = "top: 20px; right: 20px; z-index: 9999; min-width: 300px;"
  alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `

  document.body.appendChild(alertDiv)

  // Auto remove after 3 seconds
  setTimeout(() => {
    if (alertDiv.parentNode) {
      alertDiv.remove()
    }
  }, 3000)
}

// Event listeners
document.getElementById("encryptBtn").addEventListener("click", sifreleMetin)
document.getElementById("decryptBtn").addEventListener("click", cozMetin)

// Sample text for demo
document.addEventListener("DOMContentLoaded", () => {
  const sampleTexts = ["merhaba dünya", "kriptografi güvenli", "test123 deneme", "şifreleme algoritması"]

  // Add sample text button
  const inputArea = document.getElementById("inputText").parentNode
  const sampleBtn = document.createElement("button")
  sampleBtn.className = "btn btn-outline-primary btn-sm mt-2"
  sampleBtn.innerHTML = '<i class="fas fa-magic me-1"></i>Örnek Metin Ekle'
  sampleBtn.onclick = () => {
    const randomText = sampleTexts[Math.floor(Math.random() * sampleTexts.length)]
    document.getElementById("inputText").value = randomText
    showAlert("Örnek metin eklendi!", "info")
  }
  document.querySelector(".row").appendChild(sampleBtn)
})
