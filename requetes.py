import json
import networkx as nx
import matplotlib.pyplot as plt

# Q1
def json_vers_nx(chemin):
    G = nx.Graph()
    with open(chemin, "r") as fic:
        contenu = fic.read()
        splitcontent=contenu.split("\n")
        splitcontent=splitcontent[:-1]
        for dictionary in splitcontent:
            liste_acteurs=[]
            undico = json.loads(dictionary)
            lesacteurs = undico['cast']
            for actor in lesacteurs:
                if actor[:2] == "[[":
                    liste_acteurs.append(actor[2:-2])
                else:
                    liste_acteurs.append(actor)

            for actor1 in liste_acteurs:
                for actor2 in liste_acteurs:
                    if (actor1,actor2) not in G.edges:
                        G.add_edge(actor1,actor2)
        fic.close()

    return G
        
## Q2
#def collaborateurs_communs(G,u,v):
#
## Q3
#def collaborateurs_proches(G,u,k):
#def est_proche(G,u,v,k=1):
#def distance_naive(G,u,v):
#def distance(G,u,v):
#
## Q4
#def centralite(G,u):
#def centre_hollywood(G):    
## Q5
#def eloignement_max(G:nx.Graph):
#
## Bonus
#def centralite_groupe(G,S):
ungraphe = json_vers_nx("data_100.txt")
plt.show()