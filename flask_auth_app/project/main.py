import sqlite3
from xml.dom.minidom import Identified
from flask import Blueprint, render_template, request


from . import db
from flask_login import login_required, current_user
from fonction import get_familles, get_date


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/acceuil')
@login_required
def profile():
    return render_template('acceuil.html', name=current_user.name)



##################################################################
### partie sur les graphes###
##################################################################
database = sqlite3.connect('test.db')
cursor = database.cursor()

familles_liste = []
familles_liste.append('TOUTES')
for row in cursor.execute("SELECT nom from familles"):
    familles_liste.append(row[0])

#on définit les dictionnaires###
liste_mois = ['TOUS', 'Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', \
        'Octobre', 'Novembre', 'Decembre']

mois_valeur = {'Janvier':'01', 'Fevrier':'02', 'Mars':'03', 'Avril':'04', 'Mai':'05', 'Juin':'06',\
                  'Juillet':'07', 'Aout':'08','Septembre':'09', 'Octobre':'10', 'Novembre':'11', 'Decembre':'12'}

mois_nombre_de_jours = {'01':31, '02':29, '03':31, '04':30, '05':31, '06':30,\
                 '07':31, '08':31,'09':30, '10':31, '11':30, '12':31}

####
jours_total = [0,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for j in range(2, 13):
    jours_total[j] += jours_total[j-1]

jour_commencement = 11
mois_commencement = 1
annee_commencement = 1990
pleine_lune = []
pleine_lune.append((jour_commencement, mois_commencement, annee_commencement))
while int(annee_commencement) <= 2020:
    jour_commencement += 29
    if mois_commencement==2 and jour_commencement > 28:
        mois_commencement += 1
        jour_commencement %= 28
    elif jour_commencement > 30:
        mois_commencement += 1
        jour_commencement %= 30
    if mois_commencement > 12:
        annee_commencement += 1
        mois_commencement %= 12
    pleine_lune.append((jour_commencement, mois_commencement, annee_commencement))


annees_liste = []
for i in cursor.execute("SELECT DISTINCT date from velages"):  #on selectionne les dates à partir de velages
    annees_liste.append(i[0][6:10])
premiere_annee = annees_liste[0]
derniere_annee = annees_liste[-1]
annees_liste = list(range(int(premiere_annee), int(derniere_annee)+1))

graphes_types = ['Velages en fonction Jours', 'Pleine Lune', 'Distribution des races']


@main.route('/formulaire', methods=['get', 'post'])
def formulaire():
    if request.method == 'POST':
        famille= request.form["choix_famille"]
        annee = request.form['annee']
        mois = request.form['mois']
        graph = request.form['graph_type']
        pourcentage = request.form['pourcentage']
        print("choix_famille:", famille, "start:", annee, "end:", mois , "graph:", graph, "choix du pourcentage: ", pourcentage)
        database= sqlite3.connect('test.db')
        cursor = database.cursor()

        #graphique 1
        if graph == 'Velages en fonction Jours':
            if mois == 'TOUS':
                jours_listes= list(range(1,366))
                jour = [0]*367 
            else:
                jours_listes = list(range(1, mois_nombre_de_jours[mois_valeur[mois]] + 1))
                jour = [0]*(mois_nombre_de_jours[mois_valeur[mois]] + 1)
            if famille == 'TOUTES':
                for row in cursor.execute("SELECT date FROM velages"):
                    row = row[0]
                    if mois == 'TOUS':
                        if row[6:10] == annee:
                            jour[int(row[:2]) + jours_total[int(row[3:5])-1]] += 1
                    else:
                        if row[6:10] == annee and row[3:5] == mois_valeur[mois]:
                            jour[int(row[:2])] +=1
            else:
                for row in cursor.execute("SELECT velages.date FROM velages INNER JOIN animaux ON velages.mere_id = animaux.id INNER JOIN familles ON animaux.famille_id = familles.id WHERE familles.nom = '{}'".format(famille)):
                    row = row[0]  
                    if mois == 'TOUS':
                        if row[6:10]== annee:
                            jour[int(row[:2]) + jours_total[int(row[3:5])-1]] +=1
                    else:
                        if row[6:10]== annee and row[3:5] == mois_valeur[mois]:
                            jour[int(row[:2])] += 1
            return render_template('homeaffichage.html', familles= familles_liste, mois=liste_mois, annees=annees_liste, graphiques=graphes_types,choix_famille=famille, choix_mois= mois, choix_annee=annee, choix_graphes=graph, jour_liste= jours_listes, jours=jour[1:] )

        
        #graphique 2
        elif graph == 'Pleine Lune':
            id_date = []
            if famille == 'TOUTES':
                for row in cursor.execute("SELECT velages.date, animaux_velages.animal_id FROM velages INNER JOIN animaux_velages ON velages.id = animaux_velages.velage_id"):
                    id_date.append(row)
            else:
                for row in cursor.execute("SELECT velages.date, animaux_velages.animal_id FROM velages INNER JOIN animaux_velages ON velages.id = animaux_velages.velage_id INNER JOIN animaux ON velages.mere_id = animaux.id INNER JOIN familles ON animaux.famille_id = familles.id WHERE familles.nom = '{}'".format(famille)):
                    id_date.append(row)
            id_date_restant = []
            if mois == 'TOUS':
                for element in id_date:
                    if element[0][6:10] == annee:  #on prend l'élement année
                        id_date_restant.append(element)
            else:
                for element in id_date:
                    if element[0][6:10] == annee and element[0][3:5]== mois_valeur[mois]:
                        id_date_restant.append(element)
            pleine_lune_restant = []
            for i in pleine_lune:
                if i[2] == int(annee):
                    pleine_lune_restant.append(i)
            longueur_iddaterestant= len(id_date_restant)
            vaches_id=[]
            vache_pleine_ou_pas= [0] * longueur_iddaterestant
            x= 0
            for element in id_date_restant:
                vaches_id.append(element[1])
                for i in pleine_lune_restant:
                    if int(element[0][3:5])-i[1] == 0 and abs(int(element[0][:2])-i[0]) <=1:
                        vache_pleine_ou_pas[x] +=1
                        break
                x += 1
            return render_template('homeaffichage.html', familles= familles_liste, mois=liste_mois, annees=annees_liste, graphiques=graphes_types,choix_famille=famille, choix_mois= mois, choix_annee=annee, choix_graphes=graph, vaches_id= vaches_id, vache_pleine_lune= vache_pleine_ou_pas)
        
        #Graphique 3
        elif graph == 'Distribution des races':
            try:
                pourcentage = float(pourcentage)
            except:
                return render_template('formulaire.html', familles=familles_liste, mois=liste_mois, annees=annees_liste, graphes=graphes_types, choix_famille=famille, choix_mois= mois, choix_annee=annee, choix_graphes=graph , pas_float=True)
            races = ['Holstein', 'Blanc Bleu Belge', 'Jersey']
            races_nr = [0] * 3
            for type_id in range(3):
                nr_de_vaches = cursor.execute("SELECT animal_id FROM animaux_types WHERE (type_id = {} AND pourcentage >= {})".format(type_id+1, pourcentage)).fetchall()
                races_nr[type_id] = len(nr_de_vaches)
            return render_template('homeaffichage.html', familles=familles_liste, mois=liste_mois, annees=annees_liste, graphes=graphes_types, choix_famille=famille, choix_mois= mois, choix_annee=annee, choix_graphes=graph, races=races, nr_races=races_nr, minpr=pourcentage)
                
        return render_template('homeaffichage.html', familles=familles_liste, mois=liste_mois, annees=annees_liste, graphes=graphes_types, choix_famille=famille, choix_mois= mois, choix_annee=annee, choix_graphes=graph)
    else:
        return render_template('formulaire.html', familles=familles_liste, mois=liste_mois, annees=annees_liste, graphes=graphes_types)