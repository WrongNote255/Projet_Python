import numpy as np
import matplotlib.pyplot as plt

#ouverture features
def open_features():
    return

#ouverture fasta
def open_fasta():
    return


def open_BLAST_dico(blastfile):
    """
    > Input : 
        - fichier blast

    > Output : 
        - dictionnaire : {(gene1, gene2):e_value}

    Ouverture et lecture d'un fichier .out = sortie de BLAST. Création d'un dictionnaire contenant 
    en clé un tupple avec les 2 gènes à comparer provenant des 2 génomes étudiés.
    """

    dictionnaire = {}

    file = open(blastfile, "r")
    for line in file:
        elements = line.strip().split()
        gene1 = elements[0] #query seq id
        gene2 = elements[1] #subject seq id
        #pourcentage_identite = elements[2]
        #lenght = elements[3]
        #mismatch = elements[4]
        #gap = elements[5]
        #query_start = elements[6]
        #query_end = elements[7]    
        #subject_start = elements[8]
        #subject_end = elements[9]
        e_value = elements[10]
        #bit_score = elements[11]

        dictionnaire[(gene1, gene2)] = float(e_value)
    
    return dictionnaire


def dotplot(dico_blast, threshold) :
    genoms = dico_blast.keys()
    '''genom1_mult = []
    genom2_mult = []
    for i in genoms :
        genom1_mult.append(i[0])
        genom2_mult.append(i[1])

    genom1 = list(np.unique(genom1_mult))
    genom2 = list(np.unique(genom2_mult))'''

    genom1 = []
    genom2 = []

    for i in genoms :
        genom1.append(i[0])
        genom2.append(i[1])

    N = len(genom1)
    M = [] 
    for i in range(N) :
        L = []
        for j in range(N) :
            if (genom1[i],genom2[j]) in dico_blast.keys() :
                if dico_blast[(genom1[i],genom2[j])] <= threshold :
                    L.append(0)
                else :
                    L.append(1)
                    
            else : L.append(1)
        M.append(L)

    for i in range(N) :
        L = M[i]
        s = ''
        for j in L :
            if j == 0 :
                s = s + '#'
            else:
                s = s + ' '
        print(s)
        
    return(M)

dictionnaire_pre = open_BLAST_dico('DataNew-20250224/QUERY-GCA_000009985.1_ASM998v1_protein__DB-GCA_000014865.1_ASM1486v1_protein.out')
print(dictionnaire_pre)

Dotplot = dotplot(dictionnaire_pre,1e-4)
print(Dotplot)
plt.imshow(Dotplot,interpolation=None)
plt.show()
