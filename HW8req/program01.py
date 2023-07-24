#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nikita è un'abile spia che deve trovare e seguire una serie di
indizi (una sequenza di parole) che la porteranno a scoprire una o più
informazioni segrete, sotto forma di sequenze di parole.  Per ottenere
il/i segreto/i Nikita deve visitare diverse città ed in ciascuna città
troverà un indizio che le rivelerà quale sia la prossima città in cui
dovrà spostarsi.  Per ogni città visitata, Nikita otterrà una nuova
parola del segreto.

Come in una caccia al tesoro, Nikita dovrà esplorare una rete di
città, raccogliendo informazioni in ognuna di esse.

NOTA: un indizio di una città può portare in più città alternative.
    Quindi i percorsi da esplorare potrebbero essere multipli ed i
    segreti più di uno.

NOTA: se in una certa città NON C'È l'istruzione corrispondente al
    prossimo indizio vuol dire che la rete di spie nemica ha scoperto
    e distrutto l'informazione, ed il segreto che Nikita stava
    costruendo con quella sequenza non può essere più completato.
    Nikita, quindi, abbandona quella pista e prova a completare gli
    altri segreti che ha già raccolto.

Vogliamo scoprire tutti i segreti che Nikita può ricostruire dati gli
indizi a disposizione e le istruzioni disseminate nelle diverse città.

Le indicazioni su come muoversi tra le città sono contenute nel file
file_istruzioni secondo il seguente formato:
- ogni riga che inizia con il carattere cancelletto '#' va ignorata
- le città sono sempre scritte in MAIUSCOLO
- gli indizi e le parole del/i segreto/i da scoprire sono sempre
  scritte in minuscolo
Il file contiene, separate da almeno uno spazio/tab/accapo, zero o più
istruzioni da seguire.  Ogni istruzione è scritta come la
concatenazione di quattro parole:
    - città         (parola MAIUSCOLA)
    - indizio       (parola minuscola)
    - destinazione  (parola MAIUSCOLA)
    - segreto       (parola minuscola)

Esempio:
    l'istruzione      ROMAcarciofoPARIGIchampagne     indica che
        - quando la spia è a                    'ROMA'
        - se l'indizio seguente è               'carciofo'
        - la spia deve andare a                 'PARIGI'
        - ed aggiungere al segreto la parola    'champagne'

NOTA: potete assumere che il file non contenga mai istruzioni uguali.
NOTA: possono essere presenti istruzioni diverse che, partendo dalla stessa città,
    per lo stesso indizio portano in città diverse e/o producono segreti diversi
    Esempio:
    ROMAcarciofoPARIGIchampagne
    ROMAcarciofoCANCUNchampagne
    ROMAcarciofoPARIGImitraglietta
    ROMAcarciofoCATANZAROcommissario

Progettate ed implementate la funzione ex1(istructions_file, initial_city, clues) 
ricorsiva o che usa funzioni o metodi ricorsivi, che riceve come argomenti:

 - instructions_file: il nome di un file di testo che contiene le
                      istruzioni da seguire in ogni città
 - initial_city:      il nome della città da cui parte Nikita (una parola MAIUSCOLA)
 - clues:             una lista di indizi (stringa formata da parole minuscole separate
                      da spazio)

che ricostruisce tutti i possibili segreti e che torna come risultato
l'insieme di TUTTE le possibili coppie (segreto, CITTÀ), dove:
 - segreto è uno dei possibili segreti scoperti da Nikita, ovvero una
           stringa ottenuta dalla concatenazione delle parole scoperte
           separate da spazio)
 - CITTÀ   è la città in cui la spia è arrivata quando ha completato il segreto

Esempio:
Se il file è 'esempio.txt', la città di partenza è 'ROMA' e gli indizi sono 
"la bocca sollevò dal fiero pasto" 
tutte le possibili coppie segreto/città finale saranno:
     ('vendita diamanti rubati stanotte ad anversa', 'CANCUN')
     ('vendita cannoni mercato nero del cairo',      'CANCUN')
     ('furto di diamanti a buckingham palace',       'MILANO')
     ('mata hari ha sedotto ambasciatore zambia',    'MILANO')

NOTA: è vietato importare/usare altre librerie o aprire file tranne quello indicato

NOTA: il sistema di test riconosce la presenza di ricorsione SOLO se 
    la funzione/metodo ricorsivo è definita a livello esterno. 
    NON definite la funzione ricorsiva all'interno di un'altra funzione/metodo 
    altrimente fallirete tutti i test.

"""

def  ex1(istructions_file, initial_city, clues):
    clues = clues.split(" ")
    with open(istructions_file, mode="r", encoding="utf-8") as file:
        righe = []
        righe2 = []
        singole = []
        for line in file:
            line = line.strip()
            if line == "":
                continue
            if line[0] != "#":
                singole = line.split()
                for elementi in singole:
                    righe.append(elementi)
        for elemento in righe:
            elemento = elemento.replace("\t","")
            elemento = elemento.replace("\n","")
            if elemento == "":
                continue
            righe2.append(elemento)
        lista_elementi = dividi_et_impera(righe2)
        lista_incompleta = ricorsione(lista_elementi, initial_city, clues)
        lista_completa = completa(lista_incompleta)
        output = composizione(lista_completa)
    return output


def dividi_et_impera(righe2):
    singola = []
    lista_elementi = []
    upper =  False
    lower = False
    l = ""
    u = ""
    c = 0
    for parola in righe2:
        for lettera in parola:
            if lettera.isupper():
                upper = True
                l = l + lettera
            if lettera.islower():
                lower = True
                u = u + lettera
            if upper == True and lower == True:
                upper = False
                lower = False
                if c == 0 or c == 2:
                    singola.append(l)
                    l = ""
                if c == 1 or c == 3:
                    singola.append(u)
                    u = ""
                c += 1
        singola.append(u)
        lista_elementi.append(singola)
        singola = []  
        u = ""
        upper = False
        lower = False
        c = 0
    return lista_elementi
            
                         
def ricorsione(lista_elementi, initial_city, clues, livello = 0, lista_segreti = [], lista_provvisoria = []):
    
    
    if livello == len(clues):
        lista_provvisoria.append(initial_city)
        lista_segreti.append(lista_provvisoria.copy())
        
        
        return
    
    
    for elementi in lista_elementi:
        if elementi[0] == initial_city and elementi[1] == clues[livello]:
            
            lista_provvisoria.append(elementi[3])
            ricorsione(lista_elementi, elementi[2], clues, livello + 1, lista_segreti, lista_provvisoria)
            lista_provvisoria = []
            
    return lista_segreti


def completa(lista_incompleta):
    lista_completa = []
    if lista_incompleta != []:
        confronto = lista_incompleta[0]
    for frasi in lista_incompleta:
        if len(frasi) == len(confronto):
            lista_completa.append(frasi)
            confronto = frasi
            continue
        if len(frasi) < len(confronto):
            mancanti = len(confronto) - len(frasi)
            for copia in range(mancanti):
                frasi = [confronto[mancanti-1], *frasi]
                mancanti = mancanti - 1
            lista_completa.append(frasi)
            confronto = frasi

    return lista_completa
            
            
def composizione(lista_completa):
    frase = ""
    citta = ""
    tupla = ()
    insieme = set()
    for frasi in lista_completa:
        c = 0
        for elementi in frasi:
            if c == (len(frasi)-1):
                citta = elementi
                continue
            elif c == (len(frasi)-2):
                frase = frase + elementi 
                c += 1
            else:
                frase = frase + elementi + " "
                c += 1
        tupla = (frase, citta)
        insieme.add(tupla)
        tupla = ()
        frase = ""
    return insieme

    
                                
if __name__ == "__main__":
    ex1("esempio.txt", "ROME", "la bocca sollevò dal fiero pasto")
