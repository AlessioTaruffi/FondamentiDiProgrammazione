''' 
Il sindaco si una città deve pianificare un nuovo quartiere.  Voi fate
parte dello studio di architetti che deve progettare il quartiere.  Vi
viene fornito un file che contiene divisi in righe, le informazioni
che descrivono in pianta le fasce East-West (E-W) di palazzi, ciascuno
descritto da larghezza, altezza, colore da usare in pianta.

I palazzi devono essere disposti in pianta rettangolare
in modo che:
  - tutto intorno al quartiere ci sia una strada di larghezza minima
    indicata.
  - in direzione E-W (orizzontale) ci siano le strade principali,
    dritte e della stessa larghezza minima, a separare una fascia di
    palazzi E-W dalla successiva.  Ciascuna fascia E-W di palazzi può
    contenere un numero variabile di palazzi.  Se una fascia contiene
    un solo palazzo verrà disposto al centro della fascia.
  - in direzione North-South (N-S), tra ciascuna coppia di palazzi
    consecutivi, ci dev'essere almeno lo spazio per una strada
    secondaria, della stessa larghezza minima delle altre.

Vi viene chiesto di calcolare la dimensione minima dell'appezzamento
che conterrà i palazzi.  Ed inoltre di costruire la mappa che li
mostra in pianta.

Il vostro studio di architetti ha deciso di disporre i palazzi in modo
che siano **equispaziati** in direzione E-W, e di fare in modo che
ciascuna fascia E-W di palazzi sia distante dalla seguente dello
spazio minimo necessario alle strade principali.

Per rendere il quartiere più vario, il vostro studio ha deciso che i
palazzi, invece di essere allineati con il bordo delle strade
principali, devono avere se possibile un giardino davanti (a S) ed uno
dietro (a N) di uguale profondità.  Allo stesso modo, dove possibile,
lo spazio tra le strade secondarie ed i palazzi deve essere
distribuito uniformemente in modo che tutti possano avere un giardino
ad E ed uno a W di uguali dimensioni.  Solo i palazzi che si
affacciano sulle strade sul lato sinistro e destro della mappa non
hanno giardino su quel lato.

Vi viene fornito un file txt che contiene i dati che indicano quali
palazzi mettere in mappa.  Il file contiene su ciascuna riga, seguiti
da 1 virgola e/o 0 o più spazi o tab, gruppi di 5 valori interi che
rappresentano per ciascun palazzo:
  - larghezza
  - altezza
  - canale R del colore
  - canale G del colore
  - canale B del colore

Ciascuna riga contiene almeno un gruppo di 5 interi positivi relativi
ad un palazzo da disegnare. Per ciascun palazzo dovete disegnare un
rettangolo del colore indicato e di dimensioni indicate

Realizzate la funzione ex(file_dati, file_png, spaziatura) che:
  - legge i dati dal file file_dati
  - costruisce una immagine in formato PNG della mappa e la salva nel
    file file_png
  - ritorna le dimensioni larghezza,altezza dell'immagine della mappa

La mappa deve avere sfondo nero e visualizzare tutti i palazzi come segue:
  - l'argomento spaziatura indica il numero di pixel da usare per lo
    spazio necessario alle strade esterne, principali e secondarie,
    ovvero la spaziatura minima in orizzontale tra i rettangoli ed in
    verticale tra le righe di palazzi
  - ciascun palazzo è rappresentato da un rettangolo descritto da una
    quintupla del file
  - i palazzi descritti su ciascuna riga del file devono essere
    disegnati, centrati verticalmente, su una fascia in direzione
    E-W della mappa
  - i palazzi della stessa fascia devono essere equidistanti
    orizzontalmente l'uno dall'altro con una **distanza minima di
    'spaziatura' pixel tra un palazzo ed il seguente** in modo che tutti
    i primi palazzi si trovino sul bordo della strada verticale di
    sinistra e tutti gli ultimi palazzi di trovino sul bordo della
    strada di destra
    NOTA se la fascia contiene un solo palazzo dovrà essere disegnato
    centrato in orizzontale
  - ciascuna fascia di palazzi si trova ad una distanza minima in
    verticale dalla seguente per far spazio alla strada principale
    NOTE la distanza in verticale va calcolata tra i due palazzi più
    alti delle due fasce consecutive. 
    Il palazzo più grosso della prima riga si trova appoggiato al
    bordo della strada principale E-W superiore. 
    Il palazzo più grosso dell'ultima riga si trova appoggiato al
    bordo della strada principale E-W inferiore 
  - l'immagine ha le dimensioni minime possibili, quindi:
     - esiste almeno un palazzo della prima/ultima fascia a
       'spaziatura' pixel dal bordo superiore/inferiore
     - esiste almeno una fascia che ha il primo ed ultimo palazzo a
       'spaziatura' pixel dal bordo sinistro/destro
     - esiste almeno una fascia che non ha giardini ad E ed O

    NOTA: nel disegnare i palazzi potete assumere che le coordinate
        saranno sempre intere (se non lo sono avete fatto un errore).
    NOTA: Larghezza e altezza dei rettangoli sono tutti multipli di due.
'''
import images

def ex(file_dati, file_png, spaziatura):
    lista_tuple = []
    tutte_le_tuple = []
    with open(file_dati, mode="r", encoding="utf-8") as file:
        for line in file : 
            line = line.replace(',',' ')
            line = line.split() 
            while line != []:
                lista_tuple.append( (int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4])) ) 
                del line[0:5]
            tutte_le_tuple.append(lista_tuple) 
            lista_tuple = []
    file.close()
    
    dimensioni = ()
    dimensioni = calcola_dimensioni(tutte_le_tuple, spaziatura)
    immagine = crea_file(dimensioni)
    x = 0
    y = 0
    file = disegna(tutte_le_tuple, dimensioni, spaziatura, immagine, x, y)
    images.save(file, file_png)
    return(dimensioni[0], dimensioni[1])
    

    

    
def calcola_dimensioni(palazzi, spaziatura):
    h = 0
    riga_piu_lunga = 0
    altezza = 0
    for riga_di_palazzi in palazzi:
        palazzo_piu_alto = 0
        if riga_piu_lunga >= len(riga_di_palazzi): 
            for palazzo in riga_di_palazzi:
                if int(palazzo[1]) > palazzo_piu_alto:
                    palazzo_piu_alto = int(palazzo[1])
            altezza += palazzo_piu_alto
            continue
        riga_piu_lunga = len(riga_di_palazzi)
        lunghezza = 0
        for palazzo in riga_di_palazzi:
            lunghezza += int(palazzo[0])
            if int(palazzo[1]) > palazzo_piu_alto:
                    palazzo_piu_alto = int(palazzo[1])
        altezza += palazzo_piu_alto
    l = (riga_piu_lunga+1)*spaziatura + lunghezza 
    h = (len(palazzi)+1)*spaziatura + altezza
    return(l,h)
    
def crea_file(dimensioni):
    immagine = []
    righe = []
    for l in range(0,dimensioni[1]):
        for h in range(0,dimensioni[0]):
            righe.append((0,0,0))
        immagine.append(righe)
        righe = []
    return immagine


def disegna(quartiere, dimensioni, spaziatura, immagine, x, y):
    
    spazio_tra_palazzi = (dimensioni[0] -(2*spaziatura))
    c = 0
    x += spaziatura
    altezza_massima = 0
    altezza_precedente = int(quartiere[c][0][1])
    y_precedente = 0
    
    for riga in quartiere:
    
        y = y_precedente + spaziatura
        if len(riga) == 1:
            
            palazzo = riga[0]
            spazio_tra_palazzi = (dimensioni[0] - int(palazzo[0]))//2 
            altezza_massima = int(palazzo[1]) 
            x = spazio_tra_palazzi
            for i in range(y, y+int(palazzo[1])):
                for j in range(x, x+int(palazzo[0])):
                    immagine[i][j] = (palazzo[2],palazzo[3],palazzo[4]) 
            
            spazio_tra_palazzi = (dimensioni[0]-(2*spaziatura))
            y_precedente = y_precedente + altezza_massima + spaziatura
            altezza_massima = 0
            x = spaziatura
            c += 1
            y = y_precedente + spaziatura
            try:
                altezza_precedente = int(quartiere[c][0][1])
            except:
                altezza_precedente = altezza_precedente
            
            
        else:
    
            for palazzo in riga: 
                spazio_tra_palazzi = spazio_tra_palazzi - int(palazzo[0])
                if int(palazzo[1]) > altezza_massima:
                    altezza_massima = int(palazzo[1])
            

            spazio_tra_palazzi = spazio_tra_palazzi // int(len(riga)-1)
    
            for palazzo in riga: 
                if int(palazzo[1]) > altezza_precedente:
                    y = y - (int(palazzo[1])-altezza_precedente)//2
                else:
                    y = y_precedente + spaziatura + (altezza_massima - int(palazzo[1]))//2
                for i in range(y, y+int(palazzo[1])):
                    for j in range(x, x+int(palazzo[0])):
                        immagine[i][j] = (palazzo[2],palazzo[3],palazzo[4]) 
               
                x = x + int(palazzo[0])+spazio_tra_palazzi        
                altezza_precedente = int(palazzo[1])
                
            spazio_tra_palazzi = (dimensioni[0]-(2*spaziatura))
            y_precedente = y_precedente + altezza_massima + spaziatura
            altezza_massima = 0
            x = spaziatura
            c += 1
            
            try:
                altezza_precedente = int(quartiere[c][0][1])
            except:
                altezza_precedente = altezza_precedente
        
    return immagine



if __name__ == '__main__':
    ex("matrices/minimal.txt", "matrices/minimal.png", 30)

    pass