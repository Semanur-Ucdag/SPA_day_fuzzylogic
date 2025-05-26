from fuzzy_controller import bakim_sim

# Kullanıcıdan veri al
yorgunluk_input = float(input("Yorgunluk (0-10): "))
ruh_input = float(input("Ruh hali (0-10) - 0: huzurlu, 10: stresli: "))
cilt_input = float(input("Cilt tipi (0-10) - 0: kuru, 10: yağlı: "))
hava_input = float(input("Hava durumu (0-10) - 0: güneşli, 10: yağmurlu: "))
plan_input = float(input("Günlük plan yoğunluğu (0-10) - 0: boş, 10: çok yoğun: "))

# Sisteme giriş değerlerini ata
bakim_sim.input['yorgunluk'] = yorgunluk_input
bakim_sim.input['ruh_hali'] = ruh_input
bakim_sim.input['cilt'] = cilt_input
bakim_sim.input['hava'] = hava_input
bakim_sim.input['plan'] = plan_input

# Hesapla
bakim_sim.compute()

# Sonuçları yazdır
print(f"\nÖnerilen bakım süresi: {bakim_sim.output['süre']:.2f} dakika")
print(f"Önerilen bakım tipi puanı: {bakim_sim.output['bakim_tipi']:.2f}")
