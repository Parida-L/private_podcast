import gspread
from oauth2client.service_account import ServiceAccountCredentials
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
import os
import json

# Authentification
if os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"):
    credentials_dict = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"))
else:
    with open("scripts/podcast-rss-apikey.json") as f:
        credentials_dict = json.load(f)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(creds)

# Lecture du Google Sheet
SPREADSHEET_ID = "1_YlcQ9tzbWNxjK_gqpyJRnB2fvlA3GlUkhj6TOWvfls"
worksheet = client.open_by_key(SPREADSHEET_ID).sheet1
rows = worksheet.get_all_records()

# Construction du flux RSS
rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")
ET.SubElement(channel, "title").text = "Mon Podcast Perso"
ET.SubElement(channel, "link").text = "https://drive.google.com"
ET.SubElement(channel, "description").text = "Podcast privé mis à jour automatiquement"
ET.SubElement(channel, "language").text = "fr"
ET.SubElement(channel, "atom:link", {
    "href": "https://parida-l.github.io/private_podcast/podcast.xml",
    "rel": "self",
    "type": "application/rss+xml",
    "xmlns:atom": "http://www.w3.org/2005/Atom"
})

# Ajout des épisodes
for row in rows:
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = row["Titre"]
    ET.SubElement(item, "description").text = row["Description"]
    date_obj = datetime.strptime(row["Date"], "%d/%m/%Y")
    ET.SubElement(item, "pubDate").text = date_obj.strftime("%a, %d %b %Y 10:00:00 +0200")
    url = f"https://drive.google.com/uc?export=download&id={row['Fichier ID Google Drive']}"
    ET.SubElement(item, "enclosure", {
        "url": url,
        "length": str(row["Taille (en octets)"]),
        "type": "audio/mpeg"
    })
    ET.SubElement(item, "guid", {"isPermaLink": "false"}).text = row["Fichier ID Google Drive"]

# Écriture avec indentation
rough_string = ET.tostring(rss, encoding="utf-8")
reparsed = minidom.parseString(rough_string)
with open("podcast.xml", "w", encoding="utf-8") as f:
    f.write(reparsed.toprettyxml(indent="  "))

print("✅ Fichier podcast.xml généré avec indentation.")
