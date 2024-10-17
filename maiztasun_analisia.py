from collections import Counter
import sys

frekuentziak = ['E', 'A', 'O', 'L', 'S', 'N', 'D', 'R', 'U', 'I', 'T', 'C', 'P', 'M', 'Y', 'Q', 'B', 'H', 'G', 'F', 'V', 'J', 'Ñ', 'Z', 'X', 'K', 'W']
kod = {}

def agerpenak_ordenatu(mezua):
    letrak_bakarrik = [letra for letra in mezua if letra.isalpha()]
    kont = Counter(letrak_bakarrik).most_common()
    zerrOrd = [hizkia for hizkia, count in kont]
    return zerrOrd

def hiztegia_sortu(mezua):
    zerrOrd = agerpenak_ordenatu(mezua)
    for i in range(len(zerrOrd)):
        kod[zerrOrd[i]] = frekuentziak[i]

def mezua_deszifratu(mezua):
    mezu_berria = []
    for letra in mezua:
        if letra.isalpha():
            mezu_berria.append(kod.get(letra, letra))
        else:
            mezu_berria.append(letra)
    return ''.join(mezu_berria)

def hiztegia_aldatu():
        auk1 = input("Zein letra aldatu nahi duzu?: ").upper()
        auk2 = input("Zein letra jarri nahi duzu aukeratutakoaren ordez?: ").upper()
        while auk2 in kod.values():
            # Aukeratutako letra jadanik hiztegian badago, bi hizkiak trukatu.
            for key, value in kod.items():
                if value == auk2:
                    kod[key] = auk1
                    break
        kod[auk1] = auk2

def hiztegia_eguneratu():
    global kod
    new_kod = {}
    for elem in kod:
        new_kod[kod[elem]] = kod[elem]
    kod = new_kod

def main(mezua):
    amaitu = False
    hiztegia_sortu(mezua)
    while not amaitu:
        em = mezua_deszifratu(mezua)
        print(em)
        mezua = em
        hiztegia_eguneratu()
        erantzuna = input("Mezua deszifratuta dago? (Erantzuna 'bai' bada, idatzi 'b'): ").lower()
        if erantzuna == "b":
            amaitu = True
        else:
            hiztegia_aldatu()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    mezua = sys.argv[1]
    main(mezua)