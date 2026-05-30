# Todo Manager CLI

Une application de gestion de tâches interactive en ligne de commande écrite en Python. Gérez vos tâches quotidiennes avec une interface simple et une sauvegarde automatique en JSON.

## 🎯 Fonctionnalités

- **Ajouter une tâche** - Créez rapidement de nouvelles tâches
- **Lister les tâches** - Affichez toutes vos tâches avec leur statut
- **Marquer comme terminée** - Gérez l'état de vos tâches
- **Supprimer une tâche** - Supprimez les tâches indésirables
- **Sauvegarde automatique** - Vos données sont persistées dans `todo.json`
- **Interface interactive** - Prompt simple et intuitif
- **Aide intégrée** - Consultez l'aide directement depuis l'application

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
| `add [catégorie] [tâche]` | Ajoute une nouvelle tâche dans une catégorie | `add work Finir le rapport` |
| `list` | Affiche toutes les catégories et tâches | `list` |
| `list [catégorie]` | Affiche les tâches d'une catégorie | `list work` |
| `done [catégorie] [id]` | Marque une tâche comme terminée | `done work 1` |
| `delete [catégorie] [id]` | Supprime une tâche | `delete work 1` |
| `category create [nom]` | Crée une nouvelle catégorie | `category create work` |
| `category remove [nom]` | Supprime une catégorie | `category remove work` |
| `category rename [ancien] [nouveau]` | Renomme une catégorie | `category rename work job` |
| `clear` | Efface l'écran | `clear` |
| `help` | Affiche l'aide du programme | `help` |
| `quit` | Sauvegarde et quitte le programme | `quit` |

### Exemple d'utilisation

```
$ python3 todo.py
todo=# category create work
Category work created.

todo=# category create personal
Category personal created.

todo=# add work Finir le rapport
Task added: "Finir le rapport" (ID: 1)

todo=# add work Réunion à 14h
Task added: "Réunion à 14h" (ID: 2)

todo=# add personal Acheter du pain
Task added: "Acheter du pain" (ID: 1)

todo=# list
--> work
	1. Finir le rapport [incomplete]
	2. Réunion à 14h [incomplete]
--> personal
	1. Acheter du pain [incomplete]

todo=# list work
1. Finir le rapport [incomplete]
2. Réunion à 14h [incomplete]

todo=# done work 1
Task 1 completed

todo=# delete personal 1
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

Les tâches sont sauvegardées au format JSON dans `todo.json` par catégories :

```json
{
    "work": {
        "1": {
            "name": "Finir le rapport",
            "status": "completed"
        },
        "2": {
            "name": "Réunion à 14h",
            "status": "incomplete"
        }
    },
    "personal": {
        "1": {
            "name": "Acheter du pain",
            "status": "incomplete"
        }
    }
}
```

## 🔧 Architecture technique

- **Langage** : Python 3.7+
- **Type hints** : Utilise les type hints Python pour une meilleure maintenabilité
- **Sérialisation** : JSON pour la persistance des données
- **Cross-platform** : Compatible Windows, macOS et Linux

## � Analyse des Améliorations à apporter (par Haiku 4.5)

### 🔴 Critiques
1. **Gestion des erreurs insuffisante**
   - Les blocs `try/except` sont trop larges et avalent les exceptions
   - Rend le débogage difficile

2. **Noms de variables non descriptifs**
   - Variables `c`, `x`, `e` au lieu de `command`, `category`, `task_id`
   - Réduit la lisibilité du code

### 🟠 Importants
3. **Type hints manquants pour les retours**
   - Les fonctions n'ont pas de type hints pour leurs valeurs de retour
   - Ajouter `-> type` à toutes les signatures de fonction

4. **Validations insuffisantes**
   - Pas de vérification que les catégories ne sont pas vides
   - Pas de limite de longueur pour les tâches
   - Les IDs sont des strings au lieu d'entiers

5. **Logique de réindexation problématique**
   - Quand une tâche est supprimée, tous les IDs sont réassignés
   - Peut causer de la confusion avec l'utilisateur

6. **Exceptions silencieuses**
   - `KeyboardInterrupt` gérée silencieusement sans feedback

### 🟡 À améliorer
7. **Duplication de code**
   - Validations répétées (vérification de l'existence de la catégorie)
   - À refactoriser en fonctions utilitaires

8. **Pas de structure de classe**
   - Tout est basé sur des fonctions globales
   - Difficile à tester et à maintenir

9. **Documentation insuffisante**
    - Peu de docstrings détaillées
    - Pas de tests unitaires

10. **Réindexation automatique confuse**
    - Les IDs changent après suppression (1, 2, 3 → 1, 2)
    - Considérer un ID stable ou UUID

### 📋 Prochaines étapes
- [ ] Ajouter les type hints de retour à toutes les fonctions
- [ ] Renommer les variables en noms explicites (`c`, `x`, `e` → `command`, `category`, `task_id`)
- [ ] Restructurer en classe `TodoApp` pour meilleure maintenabilité
- [ ] Améliorer la gestion des erreurs avec exceptions spécifiques
- [ ] Ajouter des validations robustes des entrées (longueur min/max)
- [ ] Implémenter des IDs stables (UUID ou auto-incrémentés)
- [ ] Créer des tests unitaires basiques
- [ ] Utiliser des constantes pour les actions disponibles
- [ ] Ajouter des docstrings détaillées à toutes les fonctions

## �📝 Notes de développement

- Le programme utilise une **architecture par catégories** : chaque catégorie contient des tâches
- Les tâches sont stockées comme des dictionnaires avec `name` (titre) et `status` (incomplete/completed)
- Les **identifiants de tâche sont réassignés** automatiquement après une suppression pour renuméroter la liste
- L'application gère les **interruptions clavier** (Ctrl+C) avec grâce
- L'**encodage UTF-8** est utilisé pour la compatibilité multilingue
- La persistance des données se fait via **JSON** pour simplifier la portabilité
- Les fonctions utilisent des **type hints** pour meilleure documentation du code
- Un fichier `help.txt` peut être créé pour personnaliser l'aide intégrée

## 🐛 Remarques connues

- Les IDs se réinitialisent à 1 quand une tâche est supprimée (comportement actuel)
- Pas de validation de la longueur minimale/maximale des tâches
- Pas de persistance de l'historique des tâches complétées
- Les variables de commande (`c`, `x`, `e`) pourraient être plus explicites

---

**Auteur :** Dels  
**Dernière mise à jour :** Mai 2026  
**Version :** 1.0 (avec gestion par catégories)
