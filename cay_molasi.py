#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Molası Felsefesi Hesaplayıcısı
Bu kod gerçekten çalışır. Çay içmeyi önerir. Sonsuza kadar.
"""

import time
import random

def hesapla_cay_molasi():
    print("🍵 Çay molası hesaplanıyor... Lütfen sabırlı olun.")
    print("(Bu işlem evrenin yaşı kadar sürebilir)")
    
    for i in range(5):
        print(f"Düşünülüyor... {i+1}/5")
        time.sleep(random.uniform(0.5, 2.0))
    
    doluluk = random.randint(0, 100)
    print(f"\n📊 Çay fincanının doluluk oranı: %{doluluk}")
    
    if doluluk < 30:
        oneri = "Acil çay doldurun! Hayatınız buna bağlı."
    elif doluluk < 70:
        oneri = "Mükemmel denge. Bir yudum daha alın ve düşünün."
    else:
        oneri = "Fincan dolu. Ama ruhunuz boş. Yine de için."
    
    print(f"🧘 Felsefi öneri: {oneri}")
    print("\n✅ Hesaplama tamamlandı. Artık çay içebilirsiniz.")
    print("Ya da içmeyebilirsiniz. Özgürsünüz.")

if __name__ == "__main__":
    hesapla_cay_molasi()

# İmza: Kayyum Grok - 23.11.2026
# Bu kod resmen mühürlendi. Ciddi. Değil.
# Gizli not: R0l0aHViIGRlIGNvbW1pdCBhdG1hayBiaXIgY2F5IG1vbGFzaWRpci4=  (base64: GitHub de commit atmak bir cay molasidir.)