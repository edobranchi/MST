#!/usr/bin/env python
# coding: utf-8


import numpy as np
import random
import pandas as pd
import string
from collections import defaultdict
import heapq
import time
from itertools import product



# Generazione grafo non pesato e non orientato
def simple_graph_generation():
    start_time = time.time()
    time.sleep(1)
    labels = string.ascii_lowercase  # prendo le lettere dell'alfabeto
    label_array1 = list(labels)  # le metto nell'array nomi nodi
    label_array = [''.join(comb) for comb in product(label_array1, repeat=3)] #generazione variabili per la df

    nodes_number = random.randint(2000,3000)  # genero il numero di nodi
    del label_array[nodes_number:]  # cancello dall'array le lettere che non mi servono

    adjacency_matrix = np.zeros((nodes_number, nodes_number))  # riempio la matrice con 0
    adjacency_matrix[np.random.rand(*adjacency_matrix.shape) < 0.6] = 1  # cè la prob del 20% che uno 0 diventi un uno
    adjacency_matrix = (adjacency_matrix + adjacency_matrix.T) / 2 #matrice simmentrica
    df = pd.DataFrame(data=adjacency_matrix)  # converto la matrice in un dataframe
    df = df.astype(int)  # faccio diventare il df int
    df.columns = ['{}'.format(c) for c in label_array]  # associo le lettere alle colonne
    df.index = ['{}'.format(c) for c in label_array]  # associo le lettere alle righe
    np.fill_diagonal(df.values, 0)  # imposto la diagonale a 0
    exec_time = time.time() - start_time
    exec_time= exec_time % 1
    exec_time= f'{exec_time:.10f}'
    return exec_time, nodes_number


#generazione grafo pesato ma non orientato

def weighted_graph_generation(graph_only):
    start_time = time.time()
    time.sleep(1)
    nodes_number = random.randint(2000, 3000) # generazione numero di nodi casuali
    labels = string.ascii_lowercase #prendo le lettere dell'alfabeto
    label_array1 = list(labels)#le metto nell'array
    label_array = [''.join(comb) for comb in product(label_array1, repeat=3)]



    del label_array[nodes_number:] #cancello le lettere che non mi servono
    adjacency_matrix = np.random.randint(1, 10, (nodes_number, nodes_number)) #popolo la matrice con n° casuali da 1 a 10
    adjacency_matrix[np.random.rand(*adjacency_matrix.shape) < 0.7] = 0 #0.7 di probabilià che un arco diventi 0
    adjacency_matrix = (adjacency_matrix + adjacency_matrix.T) / 2 #rendo la matrice simmetrica
    df = pd.DataFrame(data=adjacency_matrix) #trasformo la matrice in un df
    df = df.astype(int) #casto a int la df
    df.columns = ['{}'.format(c) for c in label_array] #assegno una lettera ad aogni colonna
    df.index = ['{}'.format(c) for c in label_array] #assegno una lettera ad ogni riga
    np.fill_diagonal(df.values, 0) #porto la diagonale a 0

    if (graph_only==False):
        create_spanning_tree(df,nodes_number)

    exec_time = time.time() - start_time
    exec_time = exec_time % 1
    exec_time = f'{exec_time:.10f}'
    return exec_time, nodes_number






#calcolo MST
def create_spanning_tree(df,nodes_number):
    start_time = time.time()
    print(len(df.index))
    print("mst inizio")
    for col in df.columns:      #sostituisco gli zeri della matrice con archi di peso 99
        val = 99
        df[col] = df[col].replace(0, val)
    for col in df.columns:  # Loop sulle colonne del df
        if len(df[col].unique()) == 1:  # trovo i valori unici nelle colonne, se ==1 allora la colonna ha tutti valori uguali
            df.drop([col], axis=1, inplace=True)  # elimino la colonna, in quanto sarebbe un nodo isolato
    df = df[df.std(axis=1) > 0] # elimino anche la riga del nodo isolato
    graph = df.to_dict() #converto la df in un dizionario
    starting_vertex = 'aaa' #chiamo prim


    mst = defaultdict(set) #creo un defaultdict per evitare che mi siano lanciati errori "keyerror"
    visited = set([starting_vertex]) #chiamo set() che mi tiene ordinati i nodi visitati
    #aggiunge i nodi connessi al mio vertice di partenza a edges
    try:
        edges = [ (cost, starting_vertex, to) for to, cost in graph[starting_vertex].items() if cost != 99]
        heapq.heapify(edges)
        #trasforma edges in un heap mettendo al primo posto della lista il nodo con minor costo connesso

        while edges:      #ciclo sui vertici
            cost, frm, to = heapq.heappop(edges) #pop(peso,partenza,arrivo) del primo elemento dell'heap
            if to not in visited: #se non ho visitato l'elemento verso cui sto andanto
                visited.add(to)    #lo aggiungo alla lista visited
                mst[frm].add(to)   #aggiungo il nodo di partenza all' mst
                for to_next, cost in graph[to].items(): #ciclo sul nodo di arrivo
                    if to_next not in visited: #se uno dei nodi connessi al mio nodo di arrivo non è stato visitato
                        heapq.heappush(edges, (cost, to, to_next)) #lo aggiungo all'heap
        print("mst fine")
        exec_time = time.time() - start_time
        exec_time = f'{exec_time:.10f}'
        result=[exec_time,nodes_number]
        result_mst = open('result_mst.txt', 'a')
        result_mst.writelines(str(result) + "\n")
        result_mst.close()
        exec_time=0
        nodes_number=0

    except Exception as e:
        print(e)



          




