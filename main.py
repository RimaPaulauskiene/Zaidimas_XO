# Kryžiukų/nuliukų žaidimas

lentele = list(range(1, 10))

laimejimu_variantai = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def zaidimo_lentele():
    print("-------------")
    for i in range(3):
        print("|", lentele[6 - i * 3], "|", lentele[7 - i * 3], "|", lentele[8 - i * 3], "|")
    print("-------------")


def zymim_langeli(zaidejo_simbiolis):
    while True:
        reiksme = input("žaidėjas " + zaidejo_simbiolis + " renkasi langelį:")
        if not (reiksme in "123456789"):
            print("Klaidingai pasirinktas skaičius, bandykite dar kartą")
            continue
        reiksme = int(reiksme)
        if str(lentele[reiksme - 1]) in "XO":
            print("Šis langelis jau buvo pasirinktas")
            continue
        lentele[reiksme - 1] = zaidejo_simbiolis
        break


def tikrinam_laimetoja():
    for bandymas in laimejimu_variantai:
        if (lentele[bandymas[0] - 1]) == (lentele[bandymas[1] - 1]) == (lentele[bandymas[2] - 1]):
            return lentele[bandymas[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        zaidimo_lentele()
        if counter % 2 == 0:
            zymim_langeli("X")
        else:
            zymim_langeli("O")
        if counter > 3:
            laimi = tikrinam_laimetoja()
            if laimi:
                zaidimo_lentele()
                print((laimi, "Laimėjo!"))
                break
        counter += 1
        if counter > 8:
            zaidimo_lentele()
            print("Lygiosios!")
            break

main()


