import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Girdi değişkenleri
yorgunluk = ctrl.Antecedent(np.arange(0, 11, 1), 'yorgunluk')
ruh_hali = ctrl.Antecedent(np.arange(0, 11, 1), 'ruh_hali')
cilt = ctrl.Antecedent(np.arange(0, 11, 1), 'cilt')
hava = ctrl.Antecedent(np.arange(0, 11, 1), 'hava')
plan = ctrl.Antecedent(np.arange(0, 11, 1), 'plan')

# Çıktı değişkenleri
süre = ctrl.Consequent(np.arange(0, 61, 1), 'süre')
bakim_tipi = ctrl.Consequent(np.arange(0, 5.1, 0.1), 'bakim_tipi')

# Üyelik fonksiyonları
yorgunluk['düşük'] = fuzz.trimf(yorgunluk.universe, [0, 0, 5])
yorgunluk['orta'] = fuzz.trimf(yorgunluk.universe, [0, 5, 10])
yorgunluk['yüksek'] = fuzz.trimf(yorgunluk.universe, [5, 10, 10])

ruh_hali['stresli'] = fuzz.trimf(ruh_hali.universe, [0, 0, 5])
ruh_hali['orta'] = fuzz.trimf(ruh_hali.universe, [0, 5, 10])
ruh_hali['çok iyi'] = fuzz.trimf(ruh_hali.universe, [5, 10, 10])

cilt['kuru'] = fuzz.trimf(cilt.universe, [0, 0, 5])
cilt['normal'] = fuzz.trimf(cilt.universe, [0, 5, 10])
cilt['yağlı'] = fuzz.trimf(cilt.universe, [5, 10, 10])

hava['kapalı'] = fuzz.trimf(hava.universe, [0, 0, 5])
hava['orta'] = fuzz.trimf(hava.universe, [0, 5, 10])
hava['güneşli'] = fuzz.trimf(hava.universe, [5, 10, 10])

plan['boş'] = fuzz.trimf(plan.universe, [0, 0, 5])
plan['orta'] = fuzz.trimf(plan.universe, [0, 5, 10])
plan['yoğun'] = fuzz.trimf(plan.universe, [5, 10, 10])

süre['çok kısa'] = fuzz.trimf(süre.universe, [0, 0, 15])
süre['kısa'] = fuzz.trimf(süre.universe, [10, 20, 30])
süre['orta'] = fuzz.trimf(süre.universe, [25, 35, 45])
süre['uzun'] = fuzz.trimf(süre.universe, [40, 50, 60])
süre['çok uzun'] = fuzz.trimf(süre.universe, [50, 60, 60])

bakim_tipi['çok hafif'] = fuzz.trimf(bakim_tipi.universe, [0, 0, 1])
bakim_tipi['hafif'] = fuzz.trimf(bakim_tipi.universe, [0.5, 1.5, 2])
bakim_tipi['orta'] = fuzz.trimf(bakim_tipi.universe, [1.8, 2.5, 3.2])
bakim_tipi['yoğun'] = fuzz.trimf(bakim_tipi.universe, [3, 3.8, 4.5])
bakim_tipi['çok yoğun'] = fuzz.trimf(bakim_tipi.universe, [4.2, 5, 5])

# Kurallar (üye isimlerine uygun olarak düzeltilmiş)
rules = [

    # Bakım tipi ile ilgili genişletilmiş kurallar
    ctrl.Rule(cilt['yağlı'] & yorgunluk['düşük'], bakim_tipi['çok hafif']),
    ctrl.Rule(cilt['kuru'] & ruh_hali['stresli'] & hava['kapalı'], bakim_tipi['çok yoğun']),
    ctrl.Rule(cilt['normal'] & plan['orta'], bakim_tipi['orta']),
    ctrl.Rule(cilt['yağlı'] & plan['yoğun'] & yorgunluk['yüksek'], bakim_tipi['hafif']),
    ctrl.Rule(cilt['kuru'] & yorgunluk['yüksek'] & plan['boş'], bakim_tipi['çok yoğun']),
    ctrl.Rule(cilt['normal'] & ruh_hali['çok iyi'] & hava['güneşli'], bakim_tipi['hafif']),
    ctrl.Rule(cilt['kuru'] & yorgunluk['orta'] & plan['orta'], bakim_tipi['yoğun']),
    ctrl.Rule(cilt['yağlı'] & yorgunluk['orta'] & ruh_hali['stresli'], bakim_tipi['orta']),

    # Çoklu girdili örnek
    ctrl.Rule(yorgunluk['yüksek'] & ruh_hali['stresli'] & hava['kapalı'] & plan['yoğun'], bakim_tipi['çok yoğun']),
    ctrl.Rule(yorgunluk['düşük'] & ruh_hali['çok iyi'] & cilt['normal'] & plan['boş'] & hava['güneşli'], bakim_tipi['çok hafif']),
    ctrl.Rule(yorgunluk['yüksek'] & ruh_hali['stresli'], süre['uzun']),
    ctrl.Rule(plan['yoğun'] | yorgunluk['yüksek'], süre['kısa']),
    ctrl.Rule(hava['güneşli'] & plan['boş'] & ruh_hali['çok iyi'], süre['uzun']),
    ctrl.Rule(plan['orta'] & yorgunluk['orta'], süre['orta']),
    ctrl.Rule(hava['kapalı'] & ruh_hali['stresli'], süre['kısa']),
    ctrl.Rule(plan['boş'] & yorgunluk['düşük'], süre['orta']),
    ctrl.Rule(plan['boş'] & ruh_hali['orta'], süre['orta']),
    ctrl.Rule(yorgunluk['düşük'] & ruh_hali['çok iyi'], süre['orta']),
    
    # Bakım tipi ile ilgili kurallar
    ctrl.Rule(cilt['yağlı'] & yorgunluk['düşük'], bakim_tipi['hafif']),
    ctrl.Rule(cilt['kuru'] & ruh_hali['stresli'], bakim_tipi['yoğun']),
    ctrl.Rule(cilt['normal'] & plan['orta'], bakim_tipi['orta']),
    ctrl.Rule(plan['boş'] & ruh_hali['stresli'], bakim_tipi['yoğun']),
    ctrl.Rule(hava['kapalı'] & cilt['kuru'], bakim_tipi['yoğun']),
    ctrl.Rule(yorgunluk['orta'] & ruh_hali['orta'] & cilt['normal'], bakim_tipi['orta']),
    ctrl.Rule(hava['güneşli'] & ruh_hali['çok iyi'], bakim_tipi['hafif']),
    ctrl.Rule(plan['yoğun'] & ruh_hali['stresli'], bakim_tipi['orta']),

    ctrl.Rule(yorgunluk['yüksek'] & ruh_hali['stresli'] & plan['boş'] & hava['kapalı'], süre['uzun']),
    ctrl.Rule(yorgunluk['orta'] & ruh_hali['orta'] & plan['orta'] & hava['orta'], süre['orta']),
    ctrl.Rule(yorgunluk['düşük'] & ruh_hali['çok iyi'] & plan['boş'] & hava['güneşli'] & cilt['normal'], süre['uzun']),
    ctrl.Rule(yorgunluk['yüksek'] & ruh_hali['orta'] & plan['yoğun'], süre['kısa']),
    ctrl.Rule(yorgunluk['düşük'] & ruh_hali['çok iyi'] & plan['boş'], bakim_tipi['hafif']),
    ctrl.Rule(cilt['kuru'] & hava['kapalı'] & yorgunluk['orta'] & plan['orta'], bakim_tipi['yoğun']),
    ctrl.Rule(cilt['normal'] & yorgunluk['orta'] & ruh_hali['orta'], bakim_tipi['orta']),
    ctrl.Rule(cilt['yağlı'] & ruh_hali['stresli'] & plan['yoğun'], bakim_tipi['hafif']),
    ctrl.Rule(cilt['kuru'] & yorgunluk['yüksek'] & ruh_hali['stresli'] & hava['kapalı'] & plan['boş'], bakim_tipi['yoğun']),
    ctrl.Rule(yorgunluk['orta'] & ruh_hali['stresli'] & cilt['yağlı'] & plan['yoğun'], bakim_tipi['orta']),
    ctrl.Rule(yorgunluk['yüksek'] & ruh_hali['çok iyi'] & cilt['normal'] & hava['güneşli'], bakim_tipi['hafif']),
    ctrl.Rule(hava['güneşli'] & yorgunluk['orta'] & ruh_hali['çok iyi'], süre['uzun']),
    ctrl.Rule(hava['kapalı'] & plan['boş'] & ruh_hali['stresli'], süre['orta']),
    ctrl.Rule(hava['kapalı'] & yorgunluk['yüksek'] & ruh_hali['stresli'], süre['kısa']),
    ctrl.Rule(hava['orta'] & yorgunluk['orta'] & plan['orta'], süre['orta']),
    ctrl.Rule(hava['güneşli'] & cilt['kuru'], bakim_tipi['orta']),
    ctrl.Rule(hava['kapalı'] & cilt['kuru'] & plan['boş'], bakim_tipi['yoğun']),
    ctrl.Rule(hava['kapalı'] & cilt['yağlı'] & ruh_hali['stresli'], bakim_tipi['hafif']),
    ctrl.Rule(hava['güneşli'] & ruh_hali['çok iyi'] & plan['boş'], bakim_tipi['hafif']),
    ctrl.Rule(hava['kapalı'] & yorgunluk['yüksek'] & cilt['normal'] & plan['yoğun'], bakim_tipi['orta']),
    ctrl.Rule(hava['orta'] & ruh_hali['orta'] & plan['orta'] & cilt['normal'], bakim_tipi['orta']),

    ctrl.Rule(plan['yoğun'] & yorgunluk['yüksek'], süre['çok kısa']),
    ctrl.Rule(plan['orta'] & yorgunluk['orta'] & hava['orta'], süre['orta']),
    ctrl.Rule(plan['boş'] & yorgunluk['düşük'] & ruh_hali['çok iyi'], süre['çok uzun']),
    ctrl.Rule(yorgunluk['düşük'] & ruh_hali['çok iyi'] & hava['güneşli'], süre['uzun']),
    ctrl.Rule(hava['kapalı'] & plan['yoğun'], süre['çok kısa']),
    ctrl.Rule(yorgunluk['orta'] & ruh_hali['orta'] & hava['orta'] & plan['orta'], süre['orta']),
    ctrl.Rule(plan['boş'] & hava['güneşli'] & ruh_hali['çok iyi'], süre['çok uzun']),

    
]

bakim_ctrl = ctrl.ControlSystem(rules)
