import json
import networkx as nx

# Q1
def json_vers_nx(chemin):
    pass


# Q2
def collaborateurs_communs(G,u,v):
    liste=[]
    for acteur1 in G.adj(u):
        for acteur2 in G.adj(v):
            if acteur1==acteur2:
                liste.add(acteur1)
    return liste

# Q3
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs

def est_proche(G,u,v,k=1):
     return u in collaborateurs_proches(G,v,k)


def distance_naive(G,u,v):
    distance=1
    assert v in G.nodes() and u in G.nodes(), "un des deux acteur n'est pas dans le graphe"
    while True:
        if est_proche(G,u,v,distance):
            return distance
        distance+=1


def distance(G,u,v):
    pass
    

# Q4
def centralite(G,u):
    max=0
    for n in G.nodes():
        dist=distance(G,u,n)
        if dist>max:
            max=dist
    return dist

def centre_hollywood(G):
    assert len(G.nodes())!=0
    min=float("inf")
    for n in G.nodes():
        if centralite(G,n)<min:
            min=centralite(G,n)
            acteurm=n
    return acteurm


# Q5
def eloignement_max(G:nx.Graph):
    max=0
    for n in G.nodes():
        for i in G.nodes():
            dist=distance(G,n,i)
            if dist>max:
                max=dist
    return max

# Bonus
def centralite_groupe(G,S):
    pass