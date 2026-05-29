# 📋 Description Technique du Projet Todo Manager CLI

## Vue d'ensemble
**Todo Manager CLI** est une application de gestion de tâches interactive développée en **Python pur**, démontrant une maîtrise des bonnes pratiques de développement logiciel, de la gestion d'état et de la persistance de données.

---

## 🎯 Compétences Techniques Mises en Avant

### 1. **Programmation Python Avancée**
- **Type Hints** : Utilisation complète du système de type annotations Python 3.7+
  ```python
  def save(data: Dict[str, Any], file: str = "todo.json") -> None
  def load(file: str = "todo.json") -> dict[str, Any]
  ```
- **Docstrings standardisées** : Documentation inline au format Google
- **Programmation fonctionnelle** : Fonctions pures avec return explicites
- **Gestion des paramètres** : Valeurs par défaut et arguments optionnels

### 2. **Gestion de Fichiers et Sérialisation**
- **Pathlib** : API moderne pour la manipulation de chemins (alternative à `os.path`)
- **Context managers implicites** : `Path.read_text()` et `Path.write_text()` gèrent automatiquement l'ouverture/fermeture
- **Sérialisation JSON** : 
  - Encodage UTF-8 pour support multilingue
  - Pretty-printing avec `indent=4` pour lisibilité
  - `ensure_ascii=False` pour caractères spéciaux
  ```python
  Path(file).write_text(
      json.dumps(data, indent=4, ensure_ascii=False),
      encoding="utf-8"
  )
  ```

### 3. **Architecture et Patterns Logiciels**
- **Séparation des préoccupations** : Chaque fonction a une responsabilité unique
- **Persistence Layer** : Fonctions `load()` et `save()` isolent la logique de stockage
- **Business Logic** : Fonctions CRUD isolées (`add`, `done`, `delete`, `lists`)
- **UI Layer** : Gestion de l'interaction utilisateur centralisée
- **Design Pattern** : Principes DRY (Don't Repeat Yourself)

### 4. **Gestion d'Erreurs Robuste**
- **Try/Except granulaire** : Capture spécifique des exceptions
  ```python
  except ValueError:
      print("Second argument must be integer")
  ```
- **Gestion des interruptions** : `KeyboardInterrupt` avec fermeture gracieuse
- **Validation d'entrée** : Vérification des paramètres avant traitement
- **Fallbacks** : Messages d'erreur explicites et comportements par défaut

### 5. **Compatibilité Cross-Platform**
- **Détection du système d'exploitation** : `os.name` pour Windows/POSIX
- **Commandes système portables** :
  ```python
  cmd = ["cls"] if os.name == "nt" else ["clear"]
  subprocess.run(cmd, check=False)
  ```
- **Subprocess sécurisé** : `shell=False` pour éviter les injections de commandes

### 6. **Traitement des Commandes CLI**
- **Parsing d'arguments** : Split et validation des entrées
- **Machine d'état** : Boucle interactif avec gestion de différents états
- **Routing** : Système d'if/elif pour dispatcher les commandes
- **Validation de syntaxe** : Messages d'erreur spécifiques par commande

### 7. **Structures de Données Avancées**
- **Dictionnaires imbriqués** : Structure JSON hiérarchique
  ```json
  {
    "1": {"name": "Tâche", "status": "completed"}
  }
  ```
- **Comprehensions avancées** : Réorganisation d'ID avec `enumerate()`
  ```python
  todo = {str(i) : value for i, (_, value) in enumerate(todo.items(), start=1)}
  ```
- **Énumération et itération** : Parcours efficace avec `.items()`

### 8. **Encodage et Multilingue**
- **UTF-8 explicite** : Support complet des caractères spéciaux français
- **F-strings** : Formatage moderne et lisible des chaînes
- **Gestion des chemins** : Utilisation de `Path` indépendante du système

### 9. **Points d'Entrée et Exécution**
- **Guard clause** : `if __name__ == '__main__':`
- **Boucle de contrôle** : Utilisation de flags booléens pour contrôler l'exécution
- **Sauvegarde avant exit** : Persistance garantie des données

---

## 🏗️ Architecture du Projet

```
┌─────────────────────────────────────┐
│      Interface CLI (UI Layer)       │
│  - prompt_input()                   │
│  - Command Routing & Validation     │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│   Business Logic (Domain Layer)     │
│  - add()      - lists()             │
│  - done()     - delete()            │
│  - help()                           │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│  Persistence Layer (Data Layer)     │
│  - load()     - save()              │
│  - JSON Serialization               │
└─────────────────────────────────────┘
```

---

## 📊 Métriques du Code

| Aspect | Détail |
|--------|--------|
| **Nombre de fonctions** | 9 fonctions distinctes |
| **Couverture de type** | ~100% (Type hints complètes) |
| **Gestion d'erreurs** | Try/except avec fallbacks |
| **Compatibilité** | Windows, Linux, macOS |
| **Dépendances externes** | 0 (librairie standard uniquement) |
| **Support d'encodage** | UTF-8 multilingue |

---

## 💡 Compétences Démontrées en Résumé

✅ **Python Expert** - Syntaxe moderne, type hints, best practices  
✅ **Architecte logiciel** - Séparation des préoccupations, patterns  
✅ **Gestion de données** - JSON, sérialisation, persistance  
✅ **Robustesse** - Gestion d'erreurs, cas limites, validation  
✅ **Portabilité** - Support multi-plateforme  
✅ **CLI Developer** - Parsing d'arguments, UX interactive  
✅ **Maintenabilité** - Code lisible, documenté, extensible  
✅ **Thinking Procédural** - Algorithmes simples mais efficaces  

---

## 🔮 Opportunités d'Évolution

Cet exemple démontre également la scalabilité potentielle :
- Possible intégration d'une base de données (SQLite, PostgreSQL)
- Extension vers une API REST (FastAPI, Flask)
- Refactoring vers Orienté Objet avec classes
- Ajout de tests unitaires (pytest)
- CLI avancée avec bibliotheques (Click, Typer)