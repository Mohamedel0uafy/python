

films = []

def add_film():
    film = {
        "title": input("Quel est le titre du film ? "),
        "genre": input("Quel est le genre du film ? "),
        "annee": input("Quelle est l'année de sortie du film ? "),
        "recettes": float(input("Quelle est la recette du film ? ")),
        "rate": float(input("Quelle est la note du film ? "))
    }
    films.append(film)
    print("\nFilm ajouté avec succès !\n")
    print("Détails du film ajouté :", film)
def calculer_recettes_moyennes(table):
    li=[]
    for i in table:
        li.append(i['recette'])
        som=sum(li)
    moy=som/len(table)
    print("la moyenne est: " ,moy)

 
 
def films_par_genre(table):
    genre=[]
    for i in table:
        genre.append(i['genre'])
    a=Counter(genre)
    for i in a:
        print(i,":",a[i])  
 
 
def enrichir_donnees_films(table):
    for i in table:
        if i['recette'] < 100:
            cat={'categorie' : "faible"}
            i.update(cat)
        elif  100 <= i['recette'] < 500 :
            cat={'categorie' : "Modérée"}
            i.update(cat)
        else:
            cat={'categorie' : "Élevée"}
            i.update(cat)
    print(table)
 
 
 
 
def filtrer_par_critere(table):
    ch = input("wich filter: genre/ recette/ release_date/ rating ")
    var=filter(lambda x:x[ch]>2000,table)
    filtered=list(var)
 
    if ch == "genre":
      s=  input("what genre: ")
      for i in table:
          if i['genre']==s:
              print(i)
    elif ch <= "recette":
      s=  input("what recette: ")
      for i in table:
          if i['recette']==s:
              print(i)
    elif ch >= "rlease_date":
      s=  input("what rlease_date: ")
      for i in table:
          if i['rlease_date']==s:
              print(i)
    elif ch == "rating":
      s=  input("what rating: ")
      for i in table:
          if i['rating']==s:
              print(i)
 
 
 
while True:
    print("1. for inputs")
    print("2. show dict")
    print("3. for moy")
    print("4. genre calculator")
    print("5. add categ")
    print("6. Filter By")
    print("7. to quit")
 
    choice=input("enter your choice : ")
 
    if choice == "1":
        inputs(table)
    elif choice == "2":
        showinputs(table)
    elif choice == "3":
        calculer_recettes_moyennes(table)
    elif choice == "4":
        films_par_genre(table)
    elif choice == "5":
        enrichir_donnees_films(table)
    elif choice == "6":
        filtrer_par_critere(table)
    elif choice == "7":
        print("bye")
        break
