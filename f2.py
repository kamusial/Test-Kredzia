def czyzdolny(plec, wiek, sprawnosc):
    if plec == 1:
        if wiek >= 18 and wiek <= 60 and sprawnosc >= 8:
            return True
        else:
            return False
    else:
        if wiek >= 18 and wiek <= 65 and sprawnosc >= 5:
            return True
        else:
            return False
