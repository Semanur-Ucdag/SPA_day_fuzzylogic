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
bakim_tipi = ctrl.Consequent(np.arange(0, 5, 1), 'bakim_tipi')

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

süre['kısa'] = fuzz.trimf(süre.universe, [0, 0, 30])
süre['orta'] = fuzz.trimf(süre.universe, [15, 30, 45])
süre['uzun'] = fuzz.trimf(süre.universe, [30, 60, 60])

bakim_tipi['hafif'] = fuzz.trimf(bakim_tipi.universe, [0, 0, 1.5])
bakim_tipi['orta'] = fuzz.trimf(bakim_tipi.universe, [1, 2, 3])
bakim_tipi['yoğun'] = fuzz.trimf(bakim_tipi.universe, [2.5, 4, 4])

# Kurallar (üye isimlerine uygun olarak düzeltilmiş)
rules = [
    ctrl.Rule(yorgunluk['yüksek'] & ruh_hali['stresli'], süre['uzun']),
    ctrl.Rule(plan['yoğun'], süre['kısa']),
    ctrl.Rule(hava['güneşli'] & plan['boş'], süre['uzun']),
    ctrl.Rule(cilt['yağlı'], bakim_tipi['hafif']),
    ctrl.Rule(yorgunluk['düşük'] & ruh_hali['çok iyi'], bakim_tipi['hafif']),
    ctrl.Rule(plan['boş'] & ruh_hali['stresli'], bakim_tipi['yoğun']),
]

bakim_ctrl = ctrl.ControlSystem(rules)
