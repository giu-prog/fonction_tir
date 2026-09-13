# Tri automatique de fichiers

Script Python qui trie automatiquement les fichiers d'un dossier selon leur extension (PDF, images, musique, etc.) et les déplace dans des sous-dossiers dédiés créés automatiquement.

## Fonctionnement

1. Parcourt tous les fichiers d'un dossier source
2. Compare l'extension de chaque fichier aux règles définies
3. Crée le sous-dossier correspondant s'il n'existe pas encore
4. Déplace le fichier dans le bon sous-dossier

## Configuration

Modifier les variables suivantes dans le script :

- `folder_targer` : chemin du dossier à trier
- `regles` : dictionnaire associant un nom de dossier à une ou plusieurs extensions

Exemple :
```python
regles = {
    "PDF": [".pdf"],
    "Images": [".jpg"],
    "Musique": [".mp3"]
}
```

## Utilisation

```bash
python tri_files.py
```

## Prérequis

- Python 3.x (aucune bibliothèque externe à installer)
