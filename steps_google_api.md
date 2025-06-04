# 🔑 Étapes pour créer et télécharger le fichier `podcast-rss-apikey.json`

## 1. **Aller sur Google Cloud Console**

🔗 [https://console.cloud.google.com/](https://console.cloud.google.com/)

---

## 2. **Créer un projet (si tu n’en as pas déjà un)**

* Clique sur le sélecteur de projet en haut
* "Nouveau projet"
* Donne-lui un nom (ex : `private-podcast`)
* Crée-le

---

## 3. **Activer les APIs nécessaires**

Va dans **"Bibliothèque"** :

* Recherche et active :

  * ✅ `Google Sheets API`
  * ✅ `Google Drive API`

---

## 4. **Créer un compte de service**

* Menu → **IAM & Admin** → **Comptes de service**
* Cliquez sur **"Créer un compte de service"**
* Nom : `podcast-access`
* Description : accès au Google Sheet de podcast
* Valider sans donner d'accès IAM
* Une fois créé, clique sur le compte → onglet **Clés** → **Ajouter une clé** → **JSON**
* 💾 Télécharge le fichier JSON généré → c’est ton `podcast-rss-apikey.json`

> ⚠️ Ne le partage jamais publiquement. Ajoute-le dans ton `.gitignore`.

---

## 5. **Partager le Google Sheet avec ce compte**

* Copie l’email du compte de service (ex : `podcast-access@ton-projet.iam.gserviceaccount.com`)
* Va dans Google Sheets → "Partager"
* Ajoute cet email avec les droits **Lecteur**

---

## ✅ Résultat

Tu pourras ensuite :

* utiliser ce fichier localement (dans `scripts/podcast-rss-apikey.json`)
* ou injecter son contenu comme secret `GOOGLE_SERVICE_ACCOUNT_JSON` dans GitHub Actions

---
