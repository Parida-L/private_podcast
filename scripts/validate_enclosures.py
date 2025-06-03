import xml.etree.ElementTree as ET
import requests

tree = ET.parse("podcast.xml")
root = tree.getroot()

failed = False

for enclosure in root.findall(".//enclosure"):
    url = enclosure.get("url")
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        if response.status_code != 200:
            print(f"❌ {url} returned HTTP {response.status_code}")
            failed = True
        else:
            print(f"✅ {url} is OK")
    except Exception as e:
        print(f"❌ Failed to check {url}: {e}")
        failed = True

if failed:
    exit(1)
else:
    print("🎉 All enclosure links are valid.")
