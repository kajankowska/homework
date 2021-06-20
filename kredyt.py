# Obliczenie pozostałego do spłaty kredytu w poszczególnych miesiącach

print("Kredyt początkowy")
kredyt_poczatkowy = float(input())
print("Kwota raty")
kwota_raty = float(input())
print("Narzut")
narzut = float(input())

inf_sty1 = 1.592824484
inf_lut1 = -0.453509101
inf_mar1 = 2.324671717
inf_kwi1 = 1.261254407
inf_maj1 = 1.782526286
inf_cze1 = 2.329384541
inf_lip1 = 1.502229842
inf_sie1 = 1.782526286
inf_wrz1 = 2.328848994
inf_paz1 = 0.616921348
inf_lis1 = 2.352295886
inf_gru1 = 0.337779545
inf_sty2 = 1.577035247
inf_lut2 = -0.292781443
inf_mar2 = 2.8619659
inf_kwi2 = 0.267110318
inf_maj2 = 1.417952672
inf_cze2 = 1.054243267
inf_lip2 = 1.480520104
inf_sie2 = 1.77035247
inf_wrz2 = -0.07742069
inf_paz2 = 1.165733399
inf_lis2 = -0.404186718
inf_gru2 = 1.499708521

rata_sty1 = ((1 + ((inf_sty1 + narzut) / 1200)) * kredyt_poczatkowy - kwota_raty)
mniej_sty1 = (kredyt_poczatkowy - rata_sty1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_sty1, mniej_sty1))
rata_lut1 = ((1 + ((inf_lut1 + narzut) / 1200)) * rata_sty1 - kwota_raty)
mniej_lut1 = (rata_sty1 - rata_lut1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_lut1, mniej_lut1))
rata_mar1 = ((1 + ((inf_mar1 + narzut) / 1200)) * rata_lut1 - kwota_raty)
mniej_mar1 = (rata_lut1 - rata_mar1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_mar1, mniej_mar1))
rata_kwi1 = ((1 + ((inf_kwi1 + narzut) / 1200)) * rata_mar1 - kwota_raty)
mniej_kwi1 = (rata_mar1 - rata_kwi1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_kwi1, mniej_kwi1))
rata_maj1 = ((1 + ((inf_maj1 + narzut) / 1200)) * rata_kwi1 - kwota_raty)
mniej_maj1 = (rata_kwi1 - rata_maj1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_maj1, mniej_maj1))
rata_cze1 = ((1 + ((inf_cze1 + narzut) / 1200)) * rata_maj1 - kwota_raty)
mniej_cze1 = (rata_maj1 - rata_cze1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_cze1, mniej_cze1))
rata_lip1 = ((1 + ((inf_lip1 + narzut) / 1200)) * rata_cze1 - kwota_raty)
mniej_lip1 = (rata_cze1 - rata_lip1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_lip1, mniej_lip1))
rata_sie1 = ((1 + ((inf_sie1 + narzut) / 1200)) * rata_lip1 - kwota_raty)
mniej_sie1 = (rata_lip1 - rata_sie1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_sie1, mniej_sie1))
rata_wrz1 = ((1 + ((inf_wrz1 + narzut) / 1200)) * rata_sie1 - kwota_raty)
mniej_wrz1 = (rata_sie1 - rata_wrz1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_wrz1, mniej_wrz1))
rata_paz1 = ((1 + ((inf_paz1 + narzut) / 1200)) * rata_wrz1 - kwota_raty)
mniej_paz1 = (rata_wrz1 - rata_paz1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_paz1, mniej_paz1))
rata_lis1 = ((1 + ((inf_lis1 + narzut) / 1200)) * rata_paz1 - kwota_raty)
mniej_lis1 = (rata_paz1 - rata_lis1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_lis1, mniej_lis1))
rata_gru1 = ((1 + ((inf_gru1 + narzut) / 1200)) * rata_lis1 - kwota_raty)
mniej_gru1 = (rata_lis1 - rata_gru1)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_gru1, mniej_gru1))
rata_sty2 = ((1 + ((inf_sty2 + narzut) / 1200)) * rata_gru1 - kwota_raty)
mniej_sty2 = (rata_gru1 - rata_sty2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_sty2, mniej_sty2))
rata_lut2 = ((1 + ((inf_lut2 + narzut) / 1200)) * rata_sty2 - kwota_raty)
mniej_lut2 = (rata_sty2 - rata_lut2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_lut2, mniej_lut2))
rata_mar2 = ((1 + ((inf_mar2 + narzut) / 1200)) * rata_lut2 - kwota_raty)
mniej_mar2 = (rata_lut2 - rata_mar2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_mar2, mniej_mar2))
rata_kwi2 = ((1 + ((inf_kwi2 + narzut) / 1200)) * rata_mar2 - kwota_raty)
mniej_kwi2 = (rata_mar2 - rata_kwi2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_kwi2, mniej_kwi2))
rata_maj2 = ((1 + ((inf_maj2 + narzut) / 1200)) * rata_kwi2 - kwota_raty)
mniej_maj2 = (rata_kwi2 - rata_maj2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_maj2, mniej_maj2))
rata_cze2 = ((1 + ((inf_cze2 + narzut) / 1200)) * rata_maj2 - kwota_raty)
mniej_cze2 = (rata_maj2 - rata_cze2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_cze2, mniej_cze2))
rata_lip2 = ((1 + ((inf_lip2 + narzut) / 1200)) * rata_cze2 - kwota_raty)
mniej_lip2 = (rata_cze2 - rata_lip2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_lip2, mniej_lip2))
rata_sie2 = ((1 + ((inf_sie2 + narzut) / 1200)) * rata_lip2 - kwota_raty)
mniej_sie2 = (rata_lip2 - rata_sie2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_sie2, mniej_sie2))
rata_wrz2 = ((1 + ((inf_wrz2 + narzut) / 1200)) * rata_sie2 - kwota_raty)
mniej_wrz2 = (rata_sie2 - rata_wrz2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_wrz2, mniej_wrz2))
rata_paz2 = ((1 + ((inf_paz2 + narzut) / 1200)) * rata_wrz2 - kwota_raty)
mniej_paz2 = (rata_wrz2 - rata_paz2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_paz2, mniej_paz2))
rata_lis2 = ((1 + ((inf_lis2 + narzut) / 1200)) * rata_paz2 - kwota_raty)
mniej_lis2 = (rata_paz2 - rata_lis2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_lis2, mniej_lis2))
rata_gru2 = ((1 + ((inf_gru2 + narzut) / 1200)) * rata_lis2 - kwota_raty)
mniej_gru2 = (rata_lis2 - rata_gru2)
print("Twoja pozostała kwota kredytu to {}, to mniej {} niż w poprzednim miesiącu.".format(rata_gru2, mniej_gru2))
