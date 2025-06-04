# 🎧 Private Podcast Generator

Pour pouvoir apprendre plus facilement certaines notions, j'ai besoin d'entendre les explications. Je n'aime pas m'écouter mais apprendre est plus important. J'ai donc décidé de créer un private podcast avec mes épisodes! Comme je ne voulais pas seulement créer des enregistrements et les garder en local, j'ai décidé de créer un projet pour.

Ce projet automatise la génération d’un **flux RSS** de podcast à partir d’un **Google Sheet**, pour publier facilement des épisodes hébergés sur **Google Drive** via **GitHub Pages**.

---

## ✨ Fonctionnalités

- 🔗 Lecture d’un Google Sheet contenant les épisodes
- 📂 Génération automatique du fichier `podcast.xml` (flux RSS)
- 🔄 Mise à jour via **GitHub Actions** (CI)
- ✅ Validation du flux RSS (syntaxe XML + vérification des liens)
- 🔒 Fichier audio hébergé sur **Google Drive** (liens sécurisés)
- 🗂️ Fichier JSON d’authentification géré via `secrets` GitHub

---

## 🛠️ Stack utilisée

- Python (script principal)
- GitHub Actions (CI automatisée)
- Google Sheets API + Drive API (étapes de création de clé API [ici](liing))
- XML (flux RSS au format `rss 2.0`)
- GitHub Pages pour héberger le flux public

---

## 🧱 Prérequis

Avant de pouvoir utiliser ce projet, assure-toi d’avoir installé :

- [Python 3.7+](https://www.python.org/downloads/) (ex. : Python 3.10 recommandé)
- [pip](https://pip.pypa.io/en/stable/installation/) (généralement installé avec Python)
- `git` (pour cloner le dépôt)
- Un compte Google Cloud avec un **Service Account** ayant accès à :
  - l’API **Google Sheets**
  - l’API **Google Drive**
- Un fichier d’authentification Google au format JSON (voir section Sécurité)

---

## 📄 Structure du projet

```markdown

.
├── scripts/
│   ├── generate\_rss\_from\_sheet.py  # Génère le fichier podcast.xml
│   ├── validate\_enclosures.py      # Vérifie que tous les liens renvoient HTTP 200
│
├── podcast.xml                     # Fichier RSS généré automatiquement
├── .github/workflows/update-rss.yml  # GitHub Action de génération et validation
└── README.md

````

---

## 🧪 Démo

Lien vers le flux RSS :  
👉 **<https://parida-l.github.io/private_podcast/podcast.xml>**

Tu peux le coller dans une app comme **AntennaPod**, **Podcast Addict**, ou **Apple Podcasts**.

---

## 🔁 Comment ça marche ?

1. Tu enregistres ton épisode à partir d'une application de type magnéto
2. Tu rajoutes cet épisode dans le dossier google drive concerné
3. Tu changes l'accès général au document à 'Anyone with link - Viewer'
4. Tu ajoutes une ligne par épisode dans le Google Sheet partagé en indiquant :
   - le titre
   - la description,
   - la date de création
   - le Fichier ID Google Drive qui est récupéré dans le lien de partage
   - la taille en octets.
5. Ensuite il faut manuellement lancer le workflow à partir de GitHub Actions
   - Aller dans Actions et dans le projet "Generate et Validate podcast" , cliquer sur Run Workflow  
6. Le script :
   - Récupère les données
   - Génère un fichier `podcast.xml`
   - Valide la syntaxe XML
   - Vérifie que tous les liens fonctionnent
   - Commit & push le flux RSS
7. Le flux RSS est mis à jour et publié sur GitHub Pages
8. Se rendre dans l'application de podcast pour écouter les épisodes créé!

---

## 🔐 Sécurité

Le fichier de credentials Google (service account) **n’est pas commité** dans le dépôt. Il est injecté via la variable secrète `GOOGLE_SERVICE_ACCOUNT_JSON` dans GitHub Actions.
Les étapes pour créer la clé se trouvent [ici](liunk)

---

## 🧰 Installation locale (optionnel)

```bash
git clone https://github.com/Parida-L/private_podcast.git
cd private_podcast
pip install -r requirements.txt
python scripts/generate_rss_from_sheet.py
````

---

Créé par [Parida](https://github.com/Parida-L) with LOVE
