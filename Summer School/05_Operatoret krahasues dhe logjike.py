# ========== Operatorët krahasues ==========

# Shenja më e madhe, më e vogël
print(5 > 10)
print(5 < 10)
print(5 < 5)

# Më e madhe/ më e vogël baras
print(5 <= 5)

# Barazimi - Kujdes, kur krahasojmë dy vlera, vendosim 2 shenja barazimi, jo 1
print(5 == 5)

# Mosbarazimi(Jo e barabartë)
print(10 != 5)


# ========== Operatorët logjikë ==========

# Operatori 'dhe'
kushti1 and kushti2  # and është operator që bashkon dy kushte
# Kështu krijohet një kusht i ri kompleks(i përbërë) i cili plotësohet vetëm kur të dyja kushtet janë të vërteta

# Operatori 'ose'
kushti1 or kushti2
# Ky kusht i ri i cili plotësohet kur të paktën njëra nga kushtet është e vërtetë

# Operatori 'not'
# kthen rezultatin e kundërt të kushtit kompleks brenda kllapave
not (kushti1 and kushti2)
# Ky kusht i ri i cili plotësohet vetëm kur kushti kompleks brenda kllapave nuk është i përbërë
