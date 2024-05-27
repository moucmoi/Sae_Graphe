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

    """dit si oui ou non u et v sont proche d'un éloignement de k

    Args:
        G (nx.Graph): un graphe
        u (str): un acteur
        v (str): un acteur
        k (int, optional): la distance de vérification. Defaults to 1.

    Returns:
        boolean: true si les deux acteur sont à une distance de k et false sinon
    """     
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
    """donne la plus grande distance entre un acteur et un autre

    Args:
        G (nx.Graph): un graphe
        u (str): un acteur

    Returns:
        int: la distance la plus grande entre u et un autre acteur
    """    
    max=0
    for n in G.nodes():
        dist=distance(G,u,n)
        if dist>max:
            max=dist
    return dist

def centre_hollywood(G):
    """donne l'acteur qui  est le plus central dans le graphe

    Args:
        G (nx.Graph): un graphe

    Returns:
        str: l'acteur le plus central
    """    
    assert len(G.nodes())!=0
    min=float("inf")
    for n in G.nodes():
        if centralite(G,n)<min:
            min=centralite(G,n)
            acteurm=n
    return acteurm


# Q5
def eloignement_max(G:nx.Graph):
    """ fonction permettant de determiner la distance maximum dans Gc entre toute paire d’acteurs/actrices

    Args:
        G (nx.Graph): un graphe

    Returns:
        int: la distance maximal entre deux acteurs dans le graphe
    """    
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