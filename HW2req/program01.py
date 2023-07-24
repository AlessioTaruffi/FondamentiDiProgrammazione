'''
   Abbiamo quattro giocatori che si sfidano a Scarabeo+. In ogni mano
   di Scarabeo+, i giocatori, a turno, devono inserire una parola nel
   tabellone ed ottengono un punteggio, calcolato in base al valore
   delle lettere che compongono la parola inserita.

   Ogni giocatore crea la propria parola scegliendola a partire da una
   mano di 8 lettere, che vengono rimpiazzate una volta che la parola
   è stata giocata, finché non sono esaurite. Il numero totale di
   lettere è 130.  Il gioco finisce quando un giocatore riesce a
   finire tutte le lettere nella sua mano e non ci sono più lettere a
   disposizione per rimpiazzare quelle che ha appena giocato (ovvero,
   le 130 lettere sono esaurite, perché giocate oppure perché in mano
   agli altri giocatori).

   Alla fine delle giocate, vince il giocatore che ha accumulato più
   punti, considerando che per ogni lettera che rimane non giocata
   (ovvero rimane in mano ad un giocatore quando il gioco finisce)
   vengono sottratti 3 punti. 
   I punteggi sono così calcolati:
    1 punto:  E, A, I, O, N, R, T, L, S, U
    2 punti: D, G
    3 punti: B, C, M, P
    4 punti: F, H, V, W, Y
    5 punti: K
    8 punti: J, X
   10 punti: Q, Z

   Progettare una funzione ex1(g1, g2, g3, g4, dim_hand, num_letters) che calcola i
   punteggi di una partita di Scarabeo+ svolta fra i 4 giocatori, con
   la variante che il numero di lettere iniziali è num_letters, piuttosto che
   130 e il numero di lettere a disposizione di ogni giocatore è dim_hand.
   g1, g2, g3 e g4 sono liste di stringhe che rappresentano le
   giocate dei giocatori g1, g2, g3 e g4, rispettivamente, 
   in ciascun turno.

ES: dim_hand=5, num_letters=40
    g1 = ['seta','peeks','deter']
    g2 = ['reo','pumas']
    g3 = ['xx','xx']
    g4 = ['frs','bern']
    
    Notare che all’inizio della partita 5 lettere vengono date ad ognuno dei
    giocatori, dunque il contatore num_letters decresce conseguentemente.

dim_hand - num_letters - parola - punti
5 5 5 5    20            seta      4  0  0  0
5 5 5 5    16            reo       4  3  0  0
5 5 5 5    13            xx        4  3 16  0
5 5 5 5    11            frs       4  3 16  6
5 5 5 5     8            peeks    15  3 16  6
5 5 5 5     3            pumas    15 12 16  6
5 3 5 5     0            xx       15 12 32  6
5 3 3 5     0            bern     15 12 32 12
5 3 3 1     0            deter    21 12 32 12
0 3 3 1     0                       GAME OVER
---------------------------------------------
Finale                            21  3 23  9

Il TIMEOUT per ciascun test è di 0.5 secondi

ATTENZIONE: è proibito:
    - importare altre librerie
    - usare variabili globali
    - aprire file
'''
def ex1(g1, g2, g3, g4, dim_hand, num_letters):
    
    dizionario = {'a':1,'e':1,'i':1,'o':1,'u':1,'n':1,'r':1,'t':1,'l':1,'s':1,'d':2,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,'v':4,'w':4,'y':4,'k':5,'j':8,'x':8,'q':10,'z':10}
    giocata = " "
    punti = [0,0,0,0]
    mani = [dim_hand, dim_hand, dim_hand, dim_hand]
    conta_punti = 0
    num_letters = num_letters - (4*dim_hand)
    
    while mani[0]!=0 and mani[1]!=0 and mani[2]!=0 and mani[3]!=0:
        if len(g1) != 0:
            giocata = g1[0]
            g1.pop(0)
            mani[0] = mani[0] - len(giocata)
            for i in giocata:
                punti[0] = punti[0] + dizionario [i] 
            if num_letters >= len(giocata):
                mani[0] = mani [0] + len(giocata) 
                num_letters = num_letters - len(giocata)
            else:
                mani[0] = mani[0] + num_letters
                num_letters = 0
                
        if len(g2) != 0:
            giocata = g2[0]
            g2.pop(0)
            mani[1] = mani[1] - len(giocata)
            for i in giocata:
                punti[1] = punti[1] + dizionario[i]            
            if num_letters >= len(giocata):
                mani[1] = mani [1] + len(giocata) 
                num_letters = num_letters - len(giocata)
            else:
                mani[1] = mani[1] + num_letters
                num_letters = 0
                
        if len(g3) != 0:
            giocata = g3[0]
            g3.pop(0)
            mani[2] = mani[2] - len(giocata)
            for i in giocata:
                punti[2] = punti[2] + dizionario[i]           
            if num_letters >= len(giocata):
                mani[2] = mani [2] + len(giocata) 
                num_letters = num_letters - len(giocata)
            else:
                mani[2] = mani[2] + num_letters
                num_letters = 0
                
        if len(g4) != 0:
            giocata = g4[0]
            g4.pop(0)
            mani[3] = mani[3] - len(giocata)
            for i in giocata:
                punti[3] = punti[3] + dizionario[i]            
            if num_letters >= len(giocata):
                mani[3] = mani [3] + len(giocata) 
                num_letters = num_letters - len(giocata)
            else:
                mani[3] = mani[3] + num_letters
                num_letters = 0    
                           
    for i in punti:       
        if i != 0:
            punti[conta_punti] = punti[conta_punti] - (mani[conta_punti]*3)
            conta_punti += 1
    return punti
    pass 
if __name__ == "__main__":
    ex1(['seta','peeks','deter'],['reo','pumas'],['xx','xx'],['frs','bern'],5,40)
    pass