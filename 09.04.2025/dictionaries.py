# ky eshte nje dictionary
# ne dictionary kemi Keys dhe Values
# Ne rastin e meposhtem Keys jane emri, mbiemri, gjimnazi dhe klasa
# Ndersa vlera(Values) jane Filan, Fisteku, Ismail Qemali dhe 12

# Cdo 
nxensit_metrocode = {
    "emri": "Filan",
    "mbiemri": "Fisteku",
    "gjimnazi": "Ismail Qemali",
    "klasa": 12
}

# Keshtu mund te printojme nje dictionary
print(nxensit_metrocode)

# Keshtu mund te printojme celesat(Keys)
for key in nxensit_metrocode.keys():
    print(key)

# Keshtu mund te printojme vlerat
for val in nxensit_metrocode.values():
    print(val)

# Mund te iterojme cdo element te nje dictionary nepermjet ciklit te meposhtem
# nxensit_metrocode.items() perfaqeson dhe Keys dhe Values te nje dictionary
for k,v in nxensit_metrocode.items():
    print(k," => ",v)