#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask, request
import AnalyseBC
import AnalyseBCJournal
import ExtractionCourrierInternational
import ExtractionLePoint 
import ExtractionLesEchos
import ExtractionOuestFrance 
import ExtractionSudOuest
import ExtractionLeFigaro 
import ExtractionLeParisien
import Insertiondonnee
import ExtractionLePoint
import ExtractionJournalduNet 
import ExtractionLeMonde
import Choixdesune
import AcceuilUnes
import ANALYSEMOT
import ANALYSEMOTJOURNAL
import BARANALYSE
import ANALYSECOURBE

app = Flask('A la une')

#############################################################################################################################################################################

#les fonctions index et index2 retournent la meme page d'acceuil, la deuxieme est néanmoins spécifiée par la route /acceuil.php , quand on lance le serveur on tombe sur index, et quand on parcours le site et qu'on reviens dans l'acceuil c'est index2 qui est utilisé

@app.route('/')
def index():
  A = AcceuilUnes.acceuilunes()
  return acceuil(A)

@app.route('/acceuil.php')
def index2():
  A = AcceuilUnes.acceuilUnes()
  return acceuil(A)

def acceuil(A):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '</br></br></br></br><h2 align="center" > Voici les dernières actualités ! </h2>'
  i = len(A[0])
  for k in range (i):
    html += '<h3 align="center" >'
    html += '<a href="' + A[1][k].encode('utf8') + '">' + A[0][k].strip().encode('utf8') + '</a></h3>\n'
  return html

#################################################################################################################################################################""

#Voici la fonction qui permet de trouver le journal, comme on avait fais

@app.route('/trouverjournal.php')
def formulairejournal():
  page_content = ''
  page_content += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  page_content += '<h2>Choisissez votre journal:</h2>'
  page_content += '<form action="/quel_journal" method="post">'
  page_content += '<fieldset>'
  page_content += '<legend> Journal </legend></br>'
  page_content += '<label for="journal"> </label>'
  page_content += '<select name="journal">'
  page_content += '<option value="figaro">Le Figaro</option>'
  page_content += '<option value="lejournaldunet">Le Journal du Net</option>'
  page_content += '<option value="lepoint">Le Point</option>'
  page_content += '<option value="courrier">Courrier International</option>'
  page_content += '<option value="lesechos">Les Echos</option>'
  page_content += '<option value="ouestfrance">Ouest France</option>'
  page_content += '<option value="sudouest"> Le Sud Ouest </option>'
  page_content += '<option value="leparisien">Le Parisien</option>'
  page_content += '<option value="lemonde">LeMonde</option>'
  page_content += '</select>'
  page_content += '<input type="submit" value="Envoyer"></input>'
  page_content += '</fieldset>'
  page_content += '</form>'
  return page_content

@app.route('/quel_journal', methods = ['POST'])
def quel_journal():
  journal = request.form['journal']
  if journal == 'courrier':
    targetURL = 'http://www.courrierinternational.com'
    titres = ExtractionCourrierInternational.unes(targetURL)
    return htmlize(titres, targetURL)
  elif journal == 'sudouest' :
    targetURL= 'http://www.sudouest.fr/'
    Insertiondonnee.insert_quotidien((journal,targetURL))
    titres=ExtractionSudOuest.unes(targetURL)
    return htmlize(titres,targetURL)
  elif journal == 'lepoint':
    targetURL = 'http://www.lepoint.fr'
    titres = ExtractionLePoint.unes(targetURL)
    return htmlize(titres, targetURL)
  elif journal == 'lejournaldunet':
    targetURL = 'http://www.lejournaldunet.fr'
    titres = ExtractionJournalduNet.unes(targetURL)
    return htmlize2(titres)
  elif journal == 'lesechos':
    targetURL = 'http://www.lesechos.fr/'
    titres = ExtractionLesEchos.unes(targetURL)
    return htmlize2(titres)
  elif journal == 'latribune':
    targetURL = 'http://www.latribune.fr/'
    titres = ExtractionLaTribune1.unes(targetURL)
    return htmlize2(titres)
  elif journal == 'lemonde':
    targetURL = 'http://www.lemonde.fr'
    titres= ExtractionLeMonde.unes(targetURL)
    return htmlize(titres, targetURL)
  elif journal == 'ouestfrance':
    targetURL = 'http://www.ouest-france.fr'
    titres=ExtractionOuestFrance.unes(targetURL)
    return htmlize(titres, targetURL)
  elif journal == 'figaro' :
    targetURL= 'http://www.lefigaro.fr/'
    titres=ExtractionLeFigaro.unes(targetURL)
    return htmlize2(titres)
  elif journal == 'leparisien':
    targetURL='http://www.leparisien.fr'
    titres=ExtractionLeParisien.unes(targetURL)
    return htmlize2(titres)
        

def htmlize(titres, targetURL):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<h1 align="center"> Bonne lecture !</h1>'
  html += '</br></br>'
  for item in titres:
    html += '<h2 align="center">'
    html += '<a href="' + targetURL + item[1].encode('utf8') + '">' + item[0].strip().encode('utf8') + '</a></h2>\n'
  return html

def htmlize2(titles_and_href):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<h1 align="center"> Bonne lecture !</h1>'
  html += '</br></br>'
  for item in titles_and_href:
    html += '<h2 align="center" >'
    html += '<a href="' + item[1].encode('utf8') + '">' + item[0].strip().encode('utf8') + '</a></h2>\n'
  return html

#Voici la fonction qui renvois un formulaire, on rentre un mot dans ce formulaire, et celui ci renvois vers la fonction svg2 qui retourne un graphique en bar qui montre la fréquence du mot sur les 7 derniers jours

@app.route('/choixdumot.php')
def choixdumot():
  page_content = ''
  page_content += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  page_content += '</br><h2 align="center">Choisissez un mot et vous pourrez savoir combien de fois celui ci est apparu dans les unes des journaux ce mois ci</h2>'
  page_content += '<form action="/choixdumot2" method="post">'
  page_content += '<fieldset>'
  page_content += '<legend> Mot</legend></br>'
  page_content += '<label for="mot"></label>'
  page_content += '<input type="test" name= "mot"></input>'
  page_content += '<input type="submit" name="envoyer"></input>'
  page_content += '</fieldset>'
  page_content += '</form>'
  return page_content


@app.route('/choixdumot2', methods = ['POST'])
def choixdumot2():
  mot = request.form['mot']
  A = ANALYSECOURBE.mot(mot)
  return svg22(A,mot)


def svg22(A,mot):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<body>'
  html += '<h2 align="center"> Voici l évolution du mot '+mot.encode('utf8')+' au cours des 30 derniers jours </h2>'
  html += '<script>'
  html += 'var canvas=d3.select("body").append("svg").attr("width",1500).attr("height",1200);'
  html += 'var donnees= [{x:20,y:'+str(A[30])+'},'
  html += '{x:60,y:'+str(A[29])+'},'
  html += '{x:100,y:'+str(A[28])+'},'
  html += '{x:140,y:'+str(A[27])+'},'
  html += '{x:180,y:'+str(A[26])+'},'
  html += '{x:220,y:'+str(A[25])+'},'
  html += '{x:260,y:'+str(A[24])+'},'
  html += '{x:300,y:'+str(A[23])+'},'
  html += '{x:340,y:'+str(A[22])+'},'
  html += '{x:380,y:'+str(A[21])+'},'
  html += '{x:420,y:'+str(A[20])+'},{x:460,y:'+str(A[19])+'}, {x:500,y:'+str(A[18])+'},'
  html += '{x:540,y:'+str(A[17])+'},{x:580,y:'+str(A[16])+'}, {x:620,y:'+str(A[15])+'},'
  html += '{x:660,y:'+str(A[14])+'},{x:700,y:'+str(A[13])+'}, {x:740,y:'+str(A[12])+'}, '
  html += '{x:780,y:'+str(A[11])+'},{x:820,y:'+str(A[10])+'},{x:860,y:'+str(A[9])+'},{x:900,y:'+str(A[8])+'},'
  html += '{x:940,y:'+str(A[7])+'},{x:980,y:'+str(A[6])+'},{x:1020,y:'+str(A[5])+'},{x:1060,y:'+str(A[4])+'},'
  html += '{x:1100,y:'+str(A[3])+'},{x:1140,y:'+str(A[2])+'},{x:1180,y:'+str(A[1])+'},{x:1220,y:'+str(A[0])+'}];'
  html += 'var widthScale= d3.scale.linear().domain(['+str(A[31])+',0]).range([0,400]);'
  html += 'var axis=d3.svg.axis().ticks(10).orient("left").scale(widthScale);'
  html += 'var widthScale2= d3.scale.linear().domain([30,0]).range([0,1200]);'
  html += 'var axis2=d3.svg.axis().ticks(30).scale(widthScale2);'
  html += 'var groupe= canvas.append("g").attr("transform", "translate(100,150)");'
  html += 'var line= d3.svg.line().x (function(d){return d.x}).y (function(d){return d.y});groupe.selectAll("path").data([donnees]).enter().append("path").attr("d",line).attr("fill", "none").attr("stroke", "#3399FF").attr("stroke-width","2");'
  html += 'groupe.append("g").attr("transform", "translate(0,0)").call(axis);'
  html += 'groupe.append("g").attr("transform", "translate(20,420)").call(axis2);'
  html += '</script>'
  html += '</body>'
  html += '</html>'
  return html





def svg2(azer,mot):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<body></br>'
  html += '<h2 align="center" > Voici de bas en haut l"évolution du mot '+ mot.encode('utf8') +' cette semaine !</h2>'
  html += '<script>'
  html += 'var donnees = ['+str(azer[0])+','+str(azer[1])+','+str(azer[2])+','+str(azer[3])+','+str(azer[4])+','+str(azer[5])+','+str(azer[6])+'];'
  html += 'var largeur= 1200;'
  html += 'var hauteur=600;'
  html += 'var echelle= d3.scale.linear()'
  html += '.domain([0, 50])'
  html += '.range([0,largeur-100]);'
  html += 'var couleur=d3.scale.linear()'
  html += '.domain([0, 15])'
  html += '.range(["#1C2833", "red"]);'
  html += 'var axe=d3.svg.axis()'
  html += '.ticks(5)'
  html += '.scale(echelle);'
  html += 'var fonction=d3.select("body")'
  html += '.append("svg")'
  html += '.attr("width",largeur)'
  html += '.attr("height",hauteur)'
  html += '.append("g")'
  html += '.attr("transform", "translate(200,100)");'
  html += 'var bar=fonction.selectAll("rect")'
  html += '.data(donnees)'
  html += '.enter()'
  html += '.append("rect")'
  html += '.attr("width", function(i){return echelle(i);})'
  html += '.attr("height", 20)'
  html += '.attr("y", function(i,j){return j*40;})'
  html += '.attr("fill", function (i) {return couleur (i);});'
  html += 'fonction.append("g")'
  html += '.attr("transform", "translate(0,280)")'
  html += '.call(axe);'
  html += '</script></br>'
  html += '<a href="http://127.0.0.1:5000/choixdumot.php"> Choisir un autre mot </a></br></br></br></br>'
  html += '</body>'
  html += '</html>'
  return html




#####################################################################################################################################


#Voici la fonction qui retoune un formulaire, et qui renvois un affiche en donut, comparans la fréquence de 5 mots sur la semaine



@app.route('/cinqmotsjournal.php')
def cinqmotsjournal():
    page_content = ''
    page_content += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
    page_content += '<h2 align="center"> Comparez 5 mots par journal </h2>'
    page_content += '<form action="/cinqmotsjournal2.php" method="post">'
    page_content += '<fieldset>'
    page_content += '<legend> Choisissez un journal et comparez</legend></br>'
    page_content += '<label for="journal"> </label>'
    page_content += '<select name="journal">'
    page_content += '<option value="tj">Tout journaux</option>'
    page_content += '<option value="lefigaro">Le Figaro</option>'
    page_content += '<option value="lepoint">Le Point</option>'
    page_content += '<option value="courrier">Courrier International</option>'
    page_content += '<option value="lesechos">Les Echos</option>'
    page_content += '<option value="ouestfrance">Ouest France</option>'
    page_content += '<option value="sudouest"> Le Sud Ouest </option>'
    page_content += '<option value="leparisien">Le Parisien</option>'
    page_content += '</select></br></br>'
    page_content += '<label for="mot1"> </label>'
    page_content += '<input type="test" name= "mot1"></input></br></br>'
    page_content += '<label for="mot2"> </label>'
    page_content += '<input type="test" name= "mot2"></input></br></br>'
    page_content += '<label for="mot3"> </label>'
    page_content += '<input type="test" name= "mot3"></input></br></br>'
    page_content += '<label for="mot4"> </label>'
    page_content += '<input type="test" name= "mot4"></input></br></br>'
    page_content += '<label for="mot5"> </label>'
    page_content += '<input type="test" name= "mot5"></input></br></br>'
    page_content += '<input type="submit" name="envoyer"></input>'
    page_content += '</fieldset>'
    page_content += '</form>'
    return page_content

@app.route('/cinqmotsjournal2.php', methods = ['POST'])
def cinqmotsjournal2():
    journal = request.form['journal']
    mot1 = request.form['mot1']
    mot2 = request.form['mot2']
    mot3 = request.form['mot3']
    mot4 = request.form['mot4']
    mot5 = request.form['mot5']
    avec_journal = ANALYSEMOTJOURNAL.fonction(mot1,mot2,mot3,mot4,mot5,journal)
    cinq_mots = (mot1,mot2,mot3,mot4,mot5)
    sans_journal = ANALYSEMOT.fonction(mot1,mot2,mot3,mot4,mot5)
    if journal == 'tj':
      return svg11(sans_journal,cinq_mots)
    if journal == 'courrier':
      return svg(avec_journal,cinq_mots)
    elif journal == 'sudouest':
      return svg(avec_journal,cinq_mots)
    elif journal == 'lepoint':
      return svg(avec_journal,cinq_mots)
    elif journal == 'lesechos':
      return svg(avec_journal,cinq_mots)
    elif journal == 'ouestfrance':
      return svg(avec_journal,cinq_mots)
    elif journal == 'lefigaro' :
      return svg(avec_journal,cinq_mots)
    elif journal == 'leparisien':
      return svg(avec_journal,cinq_mots)


def svg(cmots,cmots2):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<h2 align = "center"> Journal '+cmots[5].encode('utf8')+' </h2>'
  html += '<body>'
  html += '<script>'
  html += 'var data =['+str(cmots[0])+','+str(cmots[1])+','+str(cmots[2])+','+str(cmots[3])+','+str(cmots[4])+'];'
  html += 'var r= 150;'
  html += 'var color = d3.scale.ordinal()'
  html += '.range(["#FF7F00","blue","yellow","#00FF00","#DE3163"]);'
  html += 'var canvas=d3.select("body").append("svg")'
  html += '.attr("width",1000)'
  html += '.attr("height",400);'
  html += 'var group= canvas.append("g")'
  html += '.attr("transform", "translate(725,200)");'
  html += 'var arc = d3.svg.arc()'
  html += '.innerRadius(100)'
  html += '.outerRadius(r);'
  html += 'var pie = d3.layout.pie()'
  html += '.value(function (d) {return d; });'
  html += 'var arcs = group.selectAll(".arc")'
  html += '.data(pie(data))'
  html += '.enter()'
  html += '.append("g")'
  html += '.attr("class","arc");'
  html += 'arcs.append("path")'
  html += '.attr("d",arc)'
  html += '.attr("fill", function(d) {return color(d.data); });'
  html += 'arcs.append("text")'
  html += '.attr("transform", function (d) { return "translate(" + arc.centroid(d) + ")";})'
  html += '.text(function (d) { return d.data; });'
  html += '</script>'
  html += '<h2 align="center"> Le mot '+cmots2[0].encode('utf8')+' est apparu '+str(cmots[0])+' fois cette semaine ! </h2>'
  html += '<h2 align="center"> Le mot '+cmots2[1].encode('utf8')+' est apparu '+str(cmots[1])+' fois cette semaine ! </h2>'
  html += '<h2 align="center"> Le mot '+cmots2[2].encode('utf8')+' est apparu '+str(cmots[2])+' fois cette semaine ! </h2>'
  html += '<h2 align="center"> Le mot '+cmots2[3].encode('utf8')+' est apparu '+str(cmots[3])+' fois cette semaine ! </h2>'
  html += '<h2 align="center"> Le mot '+cmots2[4].encode('utf8')+' est apparu '+str(cmots[4])+' fois cette semaine ! </h2>'
  html += '</body>'
  html += '</html>'
  return html


def svg11(cmots,cmots2):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<h2 align="center"> Tout journaux confondus </h2>'
  html += '<body>'
  html += '<script>'
  html += 'var data =['+str(cmots[0])+','+str(cmots[1])+','+str(cmots[2])+','+str(cmots[3])+','+str(cmots[4])+'];'
  html += 'var r= 150;'
  html += 'var color = d3.scale.ordinal()'
  html += '.range(["#FF7F00","blue","yellow","#00FF00","#DE3163"]);'
  html += 'var canvas=d3.select("body").append("svg")'
  html += '.attr("width",1000)'
  html += '.attr("height",400);'
  html += 'var group= canvas.append("g")'
  html += '.attr("transform", "translate(725,200)");'
  html += 'var arc = d3.svg.arc()'
  html += '.innerRadius(100)'
  html += '.outerRadius(r);'
  html += 'var pie = d3.layout.pie()'
  html += '.value(function (d) {return d; });'
  html += 'var arcs = group.selectAll(".arc")'
  html += '.data(pie(data))'
  html += '.enter()'
  html += '.append("g")'
  html += '.attr("class","arc");'
  html += 'arcs.append("path")'
  html += '.attr("d",arc)'
  html += '.attr("fill", function(d) {return color(d.data); });'
  html += 'arcs.append("text")'
  html += '.attr("transform", function (d) { return "translate(" + arc.centroid(d) + ")";})'
  html += '.text(function (d) { return d.data; });'
  html += '</script>'
  html += '<h2 align="center"> Le mot '+cmots2[0].encode('utf8')+' est apparu '+str(cmots[0])+' fois cette semaine ! </h2>'
  html += '<h2 align="center"> Le mot '+cmots2[1].encode('utf8')+' est apparu '+str(cmots[1])+' fois cette semaine ! </h2>'
  html += '<h2 align="center"> Le mot '+cmots2[2].encode('utf8')+' est apparu '+str(cmots[2])+' fois cette semaine ! </h2>'
  html += '<h2 align="center"> Le mot '+cmots2[3].encode('utf8')+' est apparu '+str(cmots[3])+' fois cette semaine ! </h2>'
  html += '<h2 align="center"> Le mot '+cmots2[4].encode('utf8')+' est apparu '+str(cmots[4])+' fois cette semaine ! </h2>'
  html += '</body>'
  html += '</html>'
  return html




##########################################################################################################




"""Cette fonction renvois un formulaire, on rentre un mot, et va retourner toutes l'actualité en rapport avec ce mot sur les 2 derniers jours"""


@app.route('/journalmot.php')
def journalmot():
  page_content = ''
  page_content += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  page_content += '<h2 align="center">Choisissez un mot ou un bout de phrase </h2>'
  page_content += '<form action="/journalmot2" method="post">'
  page_content += '<fieldset>'
  page_content += '<legend> Mot </legend>'
  page_content += '<label for="phrase"> </label>'
  page_content += '<input type="test" name= "phrase"></input>'
  page_content += '<input type="submit" name="envoyer"></input>'
  page_content += '</fieldset>'
  page_content += '</form>'
  return page_content

@app.route('/journalmot2', methods = ['POST'])
def journalmot2():
  phrase = request.form['phrase']
  A = Choixdesune.phrase(phrase)
  return htmlize3(A)


def htmlize3(A):
  i = len(A[0])
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<h2 align="center">Bonne lecture</h2>'
  for k in range(i):
    html += '<h2 align="center">'
    html += '<a href="' + A[1][k].encode('utf8') + '">' + A[0][k].encode('utf8') + '</a></h2>\n'
  return html



#######################################################################################################################"

""" Voici les fonctions permettant de faire des bubble chart """


@app.route('/bubble1.php')
def bubble1():
    page_content = ''
    page_content += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
    page_content += '<h2 align="center"> Voir le Bubble Chart de ces derniers jours tout journal confondu:</h2>'
    page_content += '<form action="/bubble3.php" >'
    page_content += '<fieldset>'
    page_content += '<input type="submit" name="envoyer"></input>'
    page_content += '</fieldset>'
    page_content += '</form>'
    return page_content

@app.route('/bubble2.php')
def bubble2():
    page_content = ''
    page_content += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
    page_content += '<h2 align="center"> Voir le Bubble Chart par journal:</h2>'
    page_content += '<form action="/bubble4.php" method="post">'
    page_content += '<fieldset>'
    page_content += '<label for="journal"> </label>'
    page_content += '<select name="journal">'
    page_content += '<option value="lefigaro">Le Figaro</option>'
    page_content += '<option value="lepoint">Le Point</option>'
    page_content += '<option value="courrier">Courrier International</option>'
    page_content += '<option value="lesechos">Les Echos</option>'
    page_content += '<option value="ouestfrance">Ouest France</option>'
    page_content += '<option value="sudouest"> Le Sud Ouest </option>'
    page_content += '<option value="leparisien">Le Parisien</option>'
    page_content += '</select>'
    page_content += '<input type="submit" value="envoyer"></input>'
    page_content += '</fieldset>'
    page_content += '</form>'
    return page_content
  
@app.route('/bubble3.php')
def bubble3():
  B = AnalyseBC.worlds()
  return svg5(B)

@app.route('/bubble4.php', methods = ['POST'])
def bubble4():
  journal = request.form['journal']
  if journal == 'courrier':
    B = AnalyseBCJournal.worlds2('courrierinternational')
    return svg4(B,'Courrier International')
  elif journal == 'sudouest':
    B = AnalyseBCJournal.worlds2('sudouest')
    return svg4(B,'Sud Ouest')
  elif journal == 'lepoint':
    B = AnalyseBCJournal.worlds2('lepoint')
    return svg4(B,'Le Point')
  elif journal == 'lesechos':
    B = AnalyseBCJournal.worlds2('lesechos')
    return svg4(B,'Les Echos')
  #elif journal == 'ouestfrance':
    #B = AnalyseBCJournal.worlds2('ouestfrance')
    #return svg4(B,'OuestFrance')
  elif journal == 'lefigaro' :
    B = AnalyseBCJournal.worlds2('lefigaro')
    return svg4(B,'Le Figaro')
  elif journal == 'leparisien':
    B = AnalyseBCJournal.worlds2('leparisien')
    return svg4(B,'Le Parisien')


def svg4(B,nomquotidien):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<body>'
  html += '<h1 align="center"> Voici le Bubble Chart du journal '+nomquotidien.encode('utf8')+ ' !</h1>'
  html += '<script>'
  html += 'var width = 1200;'
  html += 'var height = 600;'
  html += 'var data = {"name" : "Mot","value": 100,"children": ['
  html += '{"name": "'+B[0][0].encode('utf8')+'", "value":  '+str(B[0][1])+',  "couleur": "pink"},'
  html += '{"name": "'+B[1][0].encode('utf8')+'", "value":  '+str(B[1][1])+',  "couleur": "red"},'
  html += '{"name": "'+B[2][0].encode('utf8')+'", "value":  '+str(B[2][1])+',  "couleur": "yellow"},'
  html += '{"name": "'+B[3][0].encode('utf8')+'", "value":  '+str(B[3][1])+',  "couleur": "green"},'
  html += '{"name": "'+B[4][0].encode('utf8')+'", "value":  '+str(B[4][1])+',  "couleur": "blue"},'
  html += '{"name": "'+B[5][0].encode('utf8')+'", "value":  '+str(B[5][1])+',  "couleur": "black"},'
  html += '{"name": "'+B[6][0].encode('utf8')+'", "value":  '+str(B[6][1])+',  "couleur": "steelnlue"},'
  html += '{"name": "'+B[7][0].encode('utf8')+'", "value":  '+str(B[7][1])+', "couleur": "lime"},'
  html += '{"name": "'+B[8][0].encode('utf8')+'", "value":  '+str(B[8][1])+',  "couleur": "maroon"},'
  html += '{"name": "'+B[9][0].encode('utf8')+'", "value":  '+str(B[9][1])+',  "couleur": "olive"},'
  html += '{"name": "'+B[10][0].encode('utf8')+'", "value": '+str(B[10][1])+',  "couleur": "purple"},'
  html += '{"name": "'+B[11][0].encode('utf8')+'", "value": '+str(B[11][1])+',  "couleur": "Navy"},'
  html += '{"name": "'+B[12][0].encode('utf8')+'", "value": '+str(B[12][1])+',  "couleur": "gold"},'
  html += '{"name": "'+B[13][0].encode('utf8')+'", "value": '+str(B[13][1])+',  "couleur": "aqua"},'
  html += '{"name": "'+B[14][0].encode('utf8')+'", "value": '+str(B[14][1])+',  "couleur": "chocolate"},'
  html += '{"name": "'+B[15][0].encode('utf8')+'", "value": '+str(B[15][1])+',  "couleur": "Gray"},'
  html += '{"name": "'+B[16][0].encode('utf8')+'", "value": '+str(B[16][1])+',  "couleur": "orange"},'
  html += '{"name": "'+B[17][0].encode('utf8')+'", "value": '+str(B[17][1])+',  "couleur": "silver"},'
  html += '{"name": "'+B[18][0].encode('utf8')+'", "value": '+str(B[18][1])+',  "couleur": "azure"},'
  html += '{"name": "'+B[19][0].encode('utf8')+'", "value": '+str(B[19][1])+',  "couleur": "black"},]};'
  html += 'var canvas = d3.select("body").append("svg")'
  html += '.attr("width", width).attr("height", height)'
  html += '.append("g").attr("transform", "translate(100,10)");'
  html += 'var pack = d3.layout.pack().size([width, height]).padding(7);'
  html += 'var nodes = pack.nodes(data);'
  html += 'var node = canvas.selectAll(".node")'
  html += '.data(nodes).enter().append("g")'
  html += '.attr("class","node")'
  html += '.attr("transform", function (d) { return "translate(" + d.x + "," + d.y + ")"; });'
  html += 'node.append("circle")'
  html += '.attr("r", function (d) { return d.r; })'
  html += '.attr("fill", function(d){ return d.couleur; })'
  html += '.attr("opacity",0.3)'
  html += '.attr("stroke" , function (d) { return d.children ?  "#fff" : "#ADADAD" })'
  html += '.attr("stroke-width", "2");'
  html += 'node.append("text")'
  html += '.text(function (d) { return d.children ? "" : d.name; })'
  html += '.attr("transform", "translate(-30,5)");'
  html += '</script></br></br>'
  html += '<a href="http://127.0.0.1:5000/bubble2.php"> Choisir un autre journal </a></br></br></br></br> '
  html += '</body></html>'
  return html

def svg5(B):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8"><title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<body>'
  html += '<h1 align="center"> Voici le Bubble Chart des derniers jours !</h1>'
  html += '<script>'
  html += 'var width = 1200;'
  html += 'var height = 600;'
  html += 'var data = {"name" : "Mot","value": 100,"children": ['
  html += '{"name": "'+B[0][0].encode('utf8')+'", "value":  '+str(B[0][1])+',  "couleur": "pink"},'
  html += '{"name": "'+B[1][0].encode('utf8')+'", "value":  '+str(B[1][1])+',  "couleur": "red"},'
  html += '{"name": "'+B[2][0].encode('utf8')+'", "value":  '+str(B[2][1])+',  "couleur": "yellow"},'
  html += '{"name": "'+B[3][0].encode('utf8')+'", "value":  '+str(B[3][1])+',  "couleur": "green"},'
  html += '{"name": "'+B[4][0].encode('utf8')+'", "value":  '+str(B[4][1])+',  "couleur": "blue"},'
  html += '{"name": "'+B[5][0].encode('utf8')+'", "value":  '+str(B[5][1])+',  "couleur": "black"},'
  html += '{"name": "'+B[6][0].encode('utf8')+'", "value":  '+str(B[6][1])+',  "couleur": "steelnlue"},'
  html += '{"name": "'+B[7][0].encode('utf8')+'", "value":  '+str(B[7][1])+', "couleur": "lime"},'
  html += '{"name": "'+B[8][0].encode('utf8')+'", "value":  '+str(B[8][1])+',  "couleur": "maroon"},'
  html += '{"name": "'+B[9][0].encode('utf8')+'", "value":  '+str(B[9][1])+',  "couleur": "olive"},'
  html += '{"name": "'+B[10][0].encode('utf8')+'", "value": '+str(B[10][1])+',  "couleur": "purple"},'
  html += '{"name": "'+B[11][0].encode('utf8')+'", "value": '+str(B[11][1])+',  "couleur": "Navy"},'
  html += '{"name": "'+B[12][0].encode('utf8')+'", "value": '+str(B[12][1])+',  "couleur": "gold"},'
  html += '{"name": "'+B[13][0].encode('utf8')+'", "value": '+str(B[13][1])+',  "couleur": "aqua"},'
  html += '{"name": "'+B[14][0].encode('utf8')+'", "value": '+str(B[14][1])+',  "couleur": "chocolate"},'
  html += '{"name": "'+B[15][0].encode('utf8')+'", "value": '+str(B[15][1])+',  "couleur": "Gray"},'
  html += '{"name": "'+B[16][0].encode('utf8')+'", "value": '+str(B[16][1])+',  "couleur": "orange"},'
  html += '{"name": "'+B[17][0].encode('utf8')+'", "value": '+str(B[17][1])+',  "couleur": "silver"},'
  html += '{"name": "'+B[18][0].encode('utf8')+'", "value": '+str(B[18][1])+',  "couleur": "azure"},'
  html += '{"name": "'+B[19][0].encode('utf8')+'", "value": '+str(B[19][1])+',  "couleur": "black"},]};'
  html += 'var canvas = d3.select("body").append("svg")'
  html += '.attr("width", width).attr("height", height)'
  html += '.append("g").attr("transform", "translate(100,10)");'
  html += 'var pack = d3.layout.pack().size([width, height]).padding(7);'
  html += 'var nodes = pack.nodes(data);'
  html += 'var node = canvas.selectAll(".node")'
  html += '.data(nodes).enter().append("g")'
  html += '.attr("class","node")'
  html += '.attr("transform", function (d) { return "translate(" + d.x + "," + d.y + ")"; });'
  html += 'node.append("circle")'
  html += '.attr("r", function (d) { return d.r; })'
  html += '.attr("fill", function(d){ return d.couleur; })'
  html += '.attr("opacity",0.3)'
  html += '.attr("stroke" , function (d) { return d.children ?  "#fff" : "#ADADAD" })'
  html += '.attr("stroke-width", "2");'
  html += 'node.append("text")'
  html += '.text(function (d) { return d.children ? "" : d.name; })'
  html += '.attr("transform", "translate(-30,5)");'
  html += '</script></br></br>'
  html += '</body></html>'
  return html

if __name__ == '__main__':
  app.run(debug=True)
