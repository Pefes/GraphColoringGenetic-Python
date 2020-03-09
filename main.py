import random
import time

n = 0 # liczba wierzchołków
listaSasiedztwa = []  # lista sąsiedztwa
populacja = []
populacjaLiczbaKolorow = []
times = []


def wczytajListeSasiedztwa():
    plik = open("file.txt", "r")
    temp = plik.readlines()

    global n
    n = int(temp[0])  # wczytanie liczby wierzchołków

    for i in range(n): listaSasiedztwa.append([]) #tworzę listy dla każdego wierzchołka

    for line in temp[1:]:
        line = line.split(" ")
        x = int(line[1]) - 1
        y = int(line[2]) - 1
        listaSasiedztwa[x].append(y)
        listaSasiedztwa[y].append(x)

    plik.close()

def wyswietlListeSasiedztwa():
    for i in listaSasiedztwa:
        print(i)

def algorytmZachlanny():
    pokolorowaneWierzcholki = [-1 for k in range(n)]
    kolejnosc = [i for i in range(n)]
    random.shuffle(kolejnosc) #pomieszanie elementow

    for i in kolejnosc:
        if(pokolorowaneWierzcholki[i] == -1):
            tab = []

            for j in listaSasiedztwa[i]:
                if(pokolorowaneWierzcholki[j] not in tab):
                    tab.append(pokolorowaneWierzcholki[j])

            for j in range(n):
                if(j not in tab):
                    pokolorowaneWierzcholki[i] = j
                    break

    populacja.append(pokolorowaneWierzcholki)
    populacjaLiczbaKolorow.append(len(set(pokolorowaneWierzcholki)))

def sortujPopulacje():
    for i in range(len(populacjaLiczbaKolorow)):
        for j in range(len(populacjaLiczbaKolorow) - 1):
            if(populacjaLiczbaKolorow[j] > populacjaLiczbaKolorow[j + 1]):
                temp = populacjaLiczbaKolorow[j + 1]
                populacjaLiczbaKolorow[j + 1] = populacjaLiczbaKolorow[j]
                populacjaLiczbaKolorow[j] = temp

                temp = populacja[j + 1]
                populacja[j + 1] = populacja[j]
                populacja[j] = temp

def krzyzuj():

    rodzice = populacja[:int(len(populacja))] #wybieram rodziców (połowa populacji)
    nowaPopulacja = []
    for i in range(0, len(populacja), 2):
        indeks = random.randint(0, len(populacja[0]) - 1)
        temp = populacja[i][:indeks]
        populacja[i][:indeks] = populacja[i + 1][:indeks]
        populacja[i + 1][:indeks] = temp

def mutuj():

    global n

    for i in range(len(populacja)):

        dostepneKolory = []
        for x in populacja[i]: dostepneKolory.append(x)
        dostepneKolory.sort()

        for j in range(len(listaSasiedztwa)):

            kolorySasiadow = []
            for k in listaSasiedztwa[j]: kolorySasiadow.append(populacja[i][k])

            for k in listaSasiedztwa[j]:
                zmiana = False
                if(populacja[i][j] == populacja[i][k]):
                    for m in dostepneKolory:
                        if(m != populacja[i][j] and m not in kolorySasiadow):
                            populacja[i][j] = m
                            zmiana = True
                            break
                    if(not zmiana):
                        for m in range(n):
                            if(m != populacja[i][j] and m not in kolorySasiadow):
                                populacja[i][j] = m
                                zmiana = True
                                break
                if (zmiana): break

def liczPunkty():

    for i in range(len(populacja)):
        populacjaLiczbaKolorow[i] = len(set(populacja[i]))




wczytajListeSasiedztwa()
#wyswietlListeSasiedztwa()

for i in range(2*int(int(n/2)/2)):

    start_time = time.time()

    algorytmZachlanny()

    duration = time.time() - start_time

times.append(duration)

wynikZachlanny = min(populacjaLiczbaKolorow)
wynikHeurystyka = wynikZachlanny + 20
print(wynikZachlanny)


start_time = time.time()
t = 0
while((t <= int(n*30) or wynikHeurystyka > wynikZachlanny or not(mutacja)) and (wynikHeurystyka >= wynikZachlanny - 3 or not(mutacja))):
    mutacja = False
    sortujPopulacje()
    krzyzuj()
    liczPunkty()
    t+=1

    if(t % (10000 * 1/n) >= 10000 * 1/n - 1):
        for i in range(int(len(populacja)/2)):
            del populacja[i]
            del populacjaLiczbaKolorow[i]
            algorytmZachlanny()

        mutuj()
        mutacja = True
        liczPunkty()
        wynikHeurystyka = min(populacjaLiczbaKolorow)



duration = time.time() - start_time
times.append(duration)

print("----------------------")

wynikHeurystyka = min(populacjaLiczbaKolorow)
print(wynikZachlanny, wynikHeurystyka)
print(times)
#print(populacja)
#print(populacjaLiczbaKolorow)

start_time = time.time()

duration = time.time() - start_time









