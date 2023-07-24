"""
Sia dato un testo che contiene un poema, ovvero una successione di versi in rima.
Il poema è contenuto in un file, un verso per riga.

Vogliamo analizzarlo per estrarne la struttura prosodica, ovvero lo schema poetico in esso usato.
Per far questo sono utili le seguenti definizioni:
    - un 'elemento sonoro' (ES) è una successione massimale di 1 o più consonanti seguite da 1 o più vocali
        - prima tutte le consonanti
        - poi tutte le vocali (aeiouyj)
        - ignorando eventuali caratteri non alfabetici come spazi, numeri e segni di interpunzione 
        - togliendo gli accenti dalle lettere accentate
        - e ignorando la differenza tra maiuscole e minuscole
        NOTA:   fanno eccezione il primo ES di un verso, che può essere composto da sole vocali
                e l'ultimo ES, che può essere composto di sole consonanti
    - un verso è composto da una successione di elementi sonori, l'ultimo dei quali è chiamato 'finale'
        Esempio:      
        Se il verso è "Paperino andò al mare a pescare" 
            - gli elementi sonori sono     ["pa", "pe", "ri", "noa", "ndoa", "lma", "rea", "pe", "sca", "re"]
            - la finale è                   "re"
            - il verso è lungo              10 ES
        notate che le lettere accentate hanno perso l'accento e non ci interessa la distinzione tra maiuscole e minuscole
    - la struttura prosodica di una poesia è una lista di interi, uno per ciascun verso
    - per ciascun verso si considerano sia il numero di ES (#ES) che la sua finale
    - al primo verso va associato il numero 0
    - a ciascuno dei versi successivi va associato:
        - l'intero che è stato già associato ad un verso precedente che ha stesso #ES e finale
        - altrimenti un nuovo intero (che segue l'ultimo già usato)
    Esempio:
        se la poesia è quella qui sotto                     gli elementi sonori sono                                    #ES finale   prosodia
        '''
        Dì pestaggio tessessi allarmai, Partenopea!         di pe sta ggio te sse ssia lla rmai pa rte no pea           13  pea         0
        Sembrò svieremo imbarcate, aumentarono usurpai?     se mbro svie re moi mba rca teau me nta ro nou su rpai      14  rpai        1
        Flash privé spirereste? Pentecoste deturpai         fla shpri ve spi re re ste pe nte co ste de tu rpai         14  rpai        1
        scrost, direttamante arrischiai,                    scro stdi re tta ma ntea rri schiai                          8  schiai      2
        odi attuazione vernicera Partenopea.                o dia ttua zio ne ve rni ce ra pa rte no pea                13  pea         0
        Psion trentacinque preesistiti calzascarpe          psio ntre nta ci nque pree si sti ti ca lza sca rpe         13  rpe         3
        nobilt fiacchi vedesti avvertirsi spermatozoi?      no bi ltfia cchi ve de stia vve rti rsi spe rma to zoi      14  zoi         4
        Igloo rubi incassando giurati spermatozoi!          i gloo ru bii nca ssa ndo giu ra ti spe rma to zoi          14  zoi         4
        Saprai reputasse inebriai                           sa prai re pu ta ssei ne briai                               8  briai       5
        man l'ballaste segnaleremo soprascarpe.             ma nlba lla ste se gna le re mo so pra sca rpe              13  rpe         3
        '''
        l'elenco dei numeri di ES è     [13,    14,     14,     8,        13,    13,    14,    14,    8,       13   ]
        l'elenco delle finali è         ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe']
        quindi la struttura prosodica è [0,     1,      1,      2,        0,     3,     4,     4,     5,       3    ]

        Dalla struttura prosodica dovete determinare il periodo, ovvero la lunghezza minima di un gruppo di versi che si ripete
        con lo stesso schema. 
        In questo esempio il modulo = 5, infatti la prosodia è formata da due sequenze uguali di 5 elementi 
        che seguono lo schema [0, 1, 1, 2, 0], infatti [0, 1, 1, 2, 0] è equivalente a [3, 4, 4, 5, 3]

        La funzione deve tornare la tupla che contiene nell'ordine i 4 valori:
            - prosodia: ovvero la lista di interi che avete calcolato da #ES e lunghezza dei versi
            - periodo:  ovvero la lunghezza minima dello schema prosodico che si ripete
            - lunghezze: ovvero la lista delle lunghezze (#ES) dei versi
            - finali:   ovvero la lista degli ES finali di ciascun verso

        Quindi per questo esempio la funzione deve tornare la tupla:
          ( [0, 1, 1, 2, 0, 3, 4, 4, 5, 3], 5, [13, 14, 14, 8, 13, 13, 14, 14, 8, 13 ], 
            ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe'])

    ATTENZIONE: non potete usare altre librerie o aprire altri file.
    TIMEOUT: Il timeout per questo esercizio è di 100ms (0.1 secondi)

"""

def ex1(poem_filename):
    
    vocali = {"a","e","i","o","u","y","j"}
    consonanti = {"b","c","d","f","g","h","k","l","m","n","p","q","r","s","t","v","w","x","z"}
    es = ""
    lista_es = []
    a=True
    lunghezza_es = []
    elementi_finali = []
    lista_prosodia = []

    with open(poem_filename, mode="r", encoding="utf-8") as file:
        for line in file:
            line = line.split()
            line = "".join(line)
            tran = line.maketrans('AÀàÁáÂâÃãÄäÅåEÈèÉéÊêËëIÌìÍíÎîÏïOÒòÓóÔôÕõÖöØøUÙùÚúÛûÜüYŸÝýÿJQWRTPSDFGHKLZXCVBNM','aaaaaaaaaaaaaeeeeeeeeeiiiiiiiiiooooooooooooouuuuuuuuuyyyyyjqwrtpsdfghklzxcvbnm',"!',.:;?")
            line = line.translate(tran)
            lista_es = []
            for lettera in line:
                if lettera in consonanti and a==False:
                    lista_es.append(es)
                    es = ""
                    a=True
                if lettera in consonanti:
                    a=True
                    es += lettera
                if lettera in vocali: 
                    a=False
                    es += lettera
            lista_es.append(es)
            es = ""
            a=True
            lunghezza_es = lunghezza(lista_es, lunghezza_es)
            elementi_finali = finali(lista_es, elementi_finali)
        lista_prosodia = prosodia(lunghezza_es, elementi_finali) 
        periodo = calcolo_periodo(lunghezza_es)
        tupla = costruzione_tupla(lista_prosodia, periodo, lunghezza_es, elementi_finali)
        return tupla
       
        
    pass

def lunghezza(lista_es, lunghezza_es):
    lunghezza_es.append(len(lista_es))
    return lunghezza_es

def finali(lista_es, elementi_finali):
    elementi_finali.append(lista_es[len(lista_es)-1])
    return elementi_finali

def prosodia(es, finali):
    prosodia = []
    diz = {}
    c = 0
    for elemento in zip(es, finali):
        if elemento in diz:
            prosodia.append(diz[elemento])
        elif elemento not in diz:
            diz[elemento] = c
            prosodia.append(c)
            c += 1
    return prosodia

def calcolo_periodo(lunghezza_es):
    temp_str = ""
    c1=0
    c2=0
    for elemento in lunghezza_es:       
        temp_str += str(elemento)
    a = (temp_str+temp_str).find(temp_str,1,-1)
    temp_str = temp_str[:a]
    for elemento in range(len(temp_str)-1):
        e1 = temp_str[elemento] + temp_str[elemento+1]
        e1 = int(e1)
        e2 = int(temp_str[elemento])
        if e2 == lunghezza_es[c2]:
            c1 += 1
            c2 += 1
        if e1 == lunghezza_es[c2]:
            c1 += 1
            c2 += 1  
    if lunghezza_es[-1] < 10:
        c1 +=1
    return c1
            
def costruzione_tupla (lista_prosodia, periodo, lunghezza_es, elementi_finali):
    risultato = (lista_prosodia, periodo, lunghezza_es, elementi_finali)
    return risultato

if __name__ == "__main__":
    ex1("example.txt")
    pass