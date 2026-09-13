import os 
import shutil

folder_targer = "C:/Users/giuli/Desktop/auto_test"

regles = {
   
   "PDF":[".pdf"],
   "images":[".jpg"],
   "Musique":[".mp3"]
   
}
         
for nom_fichier in os.listdir(folder_targer):  # cree une variable qui va s'allimenter en boucle avec le nom des fichiers 
   chemin_complet = os.path.join(folder_targer,nom_fichier) # cree une variable qui va contenir le chemin et le nom du fichier coller ensemble
   if os.path.isfile(chemin_complet):    #verifie si le nom complet de la variable chemin_complet est bien un fichier ou un dossier
      
      
      for folder,extention in regles.items():   # cree 2 variable pour trier les regles une qui va contenir les clef et une autre les valeur 
         if nom_fichier.lower().endswith(tuple(extention)): # if nom_fichier.lower() va prendre le nom des fichier et les mettre en minuscule / .endswith(tuple(extention)) on converti se que contien la variable extention en tuple pour que endswith puisse verifier la fin de la chaine de caracter
            creation_folder = os.path.join(folder_targer,folder) # creation d'une variable qui va reprendre le chemin + le nom de la categorie (qui fais partie des clef dans (regles))
            os.makedirs(creation_folder,exist_ok=True)   # va cree un dossier si le chemin et le nom de la clef (ex PDF) son contenu dans creation_folder
            shutil.move(chemin_complet,os.path.join(creation_folder,nom_fichier)) # shutil va deplacer chemin_complet avec les variables creation_folder et nom_fichier qui contienent le chemin_complet et le nom du fichier
            break
            
            