# Todo Manager CLI

Une application de gestion de tâches interactive en ligne de commande écrite en Python. Gérez vos tâches quotidiennes avec une interface simple et une sauvegarde automatique en JSON.

## 🎯 Fonctionnalités

- ✅ **Ajouter une tâche** - Créez rapidement de nouvelles tâches
- 📋 **Lister les tâches** - Affichez toutes vos tâches avec leur statut
- ✔️ **Marquer comme terminée** - Gérez l'état de vos tâches
- 🗑️ **Supprimer une tâche** - Supprimez les tâches indésirables
- 💾 **Sauvegarde automatique** - Vos données sont persistées dans `todo.json`
- 🎨 **Interface interactive** - Prompt simple et intuitif
- 📚 **Aide intégrée** - Consultez l'aide directement depuis l'application

## 📋 Prérequis

- Python 3.7+
- Aucune dépendance externe requise

## 🚀 Installation et Démarrage

### 1. Clonez ou téléchargez le projet
```bash
cd /chemin/vers/ToCli
```

### 2. Créez un environnement virtuel (recommandé)
```bash
python3 -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
```

### 3. Lancez l'application
```bash
python3 todo.py
```

## 📖 Utilisation

### Commandes disponibles

| Commande | Description | Exemple |
|----------|-------------|---------|
| `add [tâche]` | Ajoute une nouvelle tâche | `add Acheter du pain` |
| `list` | Affiche toutes les tâches | `list` |
| `done [id]` | Marque une tâche comme terminée | `done 1` |
| `delete [id]` | Supprime une tâche | `delete 1` |
| `help` | Affiche l'aide du programme | `help` |
| `quit` | Sauvegarde et quitte le programme | `quit` |

### Exemple d'utilisation

```
$ python3 todo.py
todo=# add Acheter du pain
Task added: "Acheter du pain" (ID: 1)

todo=# add Faire les courses
Task added: "Faire les courses" (ID: 2)

todo=# list
1. Acheter du pain [incomplete]
2. Faire les courses [incomplete]

todo=# done 1
Task 1 completed

todo=# list
1. Acheter du pain [completed]
2. Faire les courses [incomplete]

todo=# delete 2
Task deleted

todo=# quit
```

## 📁 Structure du projet

```
ToCli/
├── todo.py              # Script principal de l'application
├── todo.json            # Base de données des tâches (généré automatiquement)
├── help.txt             # Fichier d'aide intégrée
├── README.md            # Ce fichier
└── .venv/               # Environnement virtuel Python (optionnel)
```

## 💾 Format de sauvegarde

Les tâches sont sauvegardées au format JSON dans `todo.json` :

```json
{
    "1": {
        "name": "Acheter du pain",
        "status": "completed"
    },
    "2": {
        "name": "Faire les courses",
        "status": "incomplete"
    }
}
```

## 🔧 Architecture technique

- **Langage** : Python 3.7+
- **Type hints** : Utilise les type hints Python pour une meilleure maintenabilité
- **Sérialisation** : JSON pour la persistance des données
- **Cross-platform** : Compatible Windows, macOS et Linux

## 📝 Notes de développement

- Le programme stocke les tâches comme des dictionnaires avec `name` et `status`
- Les identifiants de tâche sont réorganisés automatiquement après une suppression
- L'application gère les interruptions clavier (Ctrl+C) avec grâce
- L'encodage UTF-8 est utilisé pour la compatibilité multilingue

---

**Auteur :** Dels  
**Date de dernière mise à jour :** Mai 2026
