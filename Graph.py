import numpy as np
import random
import networkx as nx
import pandas as pd
import string
import matplotlib.pyplot as plt
from collections import defaultdict
import heapq
import pprint


# Generazione grafo non pesato e non orientato
def simple_graph_generation():
    
    label_array = []  # array nomi nodi
    labels = string.ascii_lowercase  # prendo le lettere dell'alfabeto
    label_array = list(labels)  # le metto in un array

    nodes_number = random.randint(12, 12)  # genero il numero di nodi
    del label_array[nodes_number:]  # cancello dall'array le lettere che non mi servono

    adjacency_matrix = np.zeros((nodes_number, nodes_number))  # riempio la matrice con 0
    adjacency_matrix[np.random.rand(*adjacency_matrix.shape) < 0.6] = 1  # cè la prob del 20% che uno 0 diventi un uno
    adjacency_matrix = (adjacency_matrix + adjacency_matrix.T) / 2 #matrice simmentrica
    df = pd.DataFrame(data=adjacency_matrix)  # converto la matrice in un dataframe
    df = df.astype(int)  # faccio diventare il df int
    df.columns = ['{}'.format(c) for c in label_array]  # associo le lettere alle colonne
    df.index = ['{}'.format(c) for c in label_array]  # associo le lettere alle righe
    np.fill_diagonal(df.values, 0)  # imposto la diagonale a 0

    G = nx.from_numpy_matrix(np.array(df))  # creo il grafo dal df
    G = nx.relabel_nodes(G, dict(enumerate(df.columns)))  # nomino i nodi in base alle label sulle colonne
    layout = nx.circular_layout(G)  # uso un layout circolare per la rappresentazione
    nx.draw(G, layout, with_labels=True)  # disegno il grafo
    
    print(df)  # stampo il df
    G.clear()

#generazione grafo pesato ma non orientato

def weighted_graph_generation():
    label_array = []   #array di appoggio per i nomi dei nodi
    nodes_number = random.randint(5, 10) # generazione numero di nodi casuali
    labels = string.ascii_lowercase #prendo le lettere dell'alfabeto
    label_array = list(labels) #le metto nell'array
    del label_array[nodes_number:] #cancello le lettere che non mi servono
    adjacency_matrix = np.random.randint(1, 10, (nodes_number, nodes_number)) #popolo la matrice con n° casuali da 1 a 10
    adjacency_matrix[np.random.rand(*adjacency_matrix.shape) < 0.7] = 0 #0.7 di probabilià che un arco diventi 0
    adjacency_matrix = (adjacency_matrix + adjacency_matrix.T) / 2 #rendo la matrice simmetrica
    df = pd.DataFrame(data=adjacency_matrix) #trasformo la matrice in un df
    df = df.astype(int) #casto a int la df
    df.columns = ['{}'.format(c) for c in label_array] #assegno una lettera ad aogni colonna
    df.index = ['{}'.format(c) for c in label_array] #assegno una lettera ad ogni riga
    np.fill_diagonal(df.values, 0) #porto la diagonale a 0
    
    print("Matrice di adiacenza del grafo:\n \n", df,"\n")
    print("Grafico pesato corrispondente : \n ")
    
    G = nx.from_numpy_matrix(np.array(df)) #creo il grafo
    G = nx.relabel_nodes(G, dict(enumerate(df.columns))) #rinomino i nodi
    layout = nx.circular_layout(G) #uso un layout circolare
    nx.draw(G, layout, with_labels=True) #disegno il grafo
    labels = nx.get_edge_attributes(G, "weight") #estraggo i pesi degli archi
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels) #disegno i pesi degli archi
    ax = plt.gca()
    ax.margins(0.50) # impostazioni di disegno del grafo
    plt.axis("off")
    plt.show()
  
    for col in df.columns:      #sostituisco gli zeri della matrice con archi di peso 99
        val = 99
        df[col] = df[col].replace(0, val)
    
    Prova(df)
    G.clear()
    


def Prova(df):
    
    for col in df.columns:  # Loop sulle colonne del df
        if len(df[col].unique()) == 1:  # trovo i valori unici nelle colonne, se ==1 allora la colonna ha tutti valori uguali
            df.drop([col], axis=1, inplace=True)  # elimino la colonna, in quanto sarebbe un nodo isolato
    df = df[df.std(axis=1) > 0] # elimino anche la riga del nodo isolato
    dictionary = df.to_dict() #converto la df in un dizionario
    dict(create_spanning_tree(dictionary, 'a')) #chiamo prim


#calcolo MST
def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set) #creo un defaultdict per evitare che mi siano lanciati errori "keyerror"
    visited = set([starting_vertex]) #chiamo set() che mi tiene ordinati i nodi visitati
    #aggiunge i nodi connessi al mio vertice di partenza a edges
    edges = [ (cost, starting_vertex, to) for to, cost in graph[starting_vertex].items() if cost != 99]
    heapq.heapify(edges) #trasforma edges in un heap mettendo al primo posto della lista il nodo con minor costo connesso
    #al nodo di partenza

    while edges:      #ciclo sui vertici
        cost, frm, to = heapq.heappop(edges) #pop(peso,partenza,arrivo) del primo elemento dell'heap
        if to not in visited: #se non ho visitato l'elemento verso cui sto andanto
            visited.add(to)    #lo aggiungo alla lista visited
            mst[frm].add(to)   #aggiungo il nodo di partenza all' mst
            for to_next, cost in graph[to].items(): #ciclo sul nodo di arrivo
                if to_next not in visited: #se uno dei nodi connessi al mio nodo di arrivo non è stato visitato 
                    heapq.heappush(edges, (cost, to, to_next)) #lo aggiungo all'heap
    
    print("MST:\n")
    pprint.pprint(dict(mst),width=1) #Pretty print dell'mst in forma scritta
    print("\n")

    #print del grafo dell' MST
    print("Grafo MST: \n")
    g = nx.DiGraph(mst) 
    layout = nx.circular_layout(g)
    g = nx.relabel_nodes(g, dict(enumerate(mst)))                   
    nx.draw(g,layout, with_labels=True)
    ax = plt.gca()
    ax.margins(0.50)
    plt.axis("off")
    plt.show()
    
    return mst


#simple_graph_generation()
G = weighted_graph_generation()

