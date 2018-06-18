def converte_hms(segundos):
    s = segundos % 60
    m = (segundos % 3600) // 60
    h = segundos // 3600
    return (h, m, s)



assert(converte_hms(40) == (0,0,40))
assert(converte_hms(63) == (0,1,3))
assert(converte_hms(133) == (0,2,13))
assert(converte_hms(240) == (0,4,0))
assert(converte_hms(3600) == (1,0,0))
assert(converte_hms(5400) == (1,30,0))
