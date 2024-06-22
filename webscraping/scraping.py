import requests
from bs4 import BeautifulSoup


def scrape_has():
    url = "https://www.has-sante.fr/jcms/fc_2874902/fr/actualites"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    section = soup.find("div", class_="row actualites--list-items")
    events = section.find_all(
        "div",
        class_="content"
    )
    filtered_events = [event for event in events if
                       event.find("div", class_="type").get_text().strip() == "Evénement de Calendrier"]

    data = []
    for event in filtered_events:
        title = event.find("a").get_text().strip()
        date = event.find("div", class_="date date-event").get_text().strip()
        event_url = "https://www.has-sante.fr/" + event.find("a")["href"]
        data.append({
            "title": title,
            "date": date,
            "url": event_url,
            "source": "HAS"
        })

    return data


def scrape_firah():
    url = "https://www.firah.org/actualite/465/actualites.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    section = soup.find("div", class_="pages_articles")
    events = section.find_all(
        "article",
        # class_="article"
    )

    # convertir les éléments obtenus en data
    data = []
    for event in events:
        title = event.find("a").get_text().strip()
        date = None
        event_url = "https://www.firah.org/" + event.find("a")["href"]
        data.append({
            "title": title,
            "date": date,
            "url": event_url,
            "source": "FIRAH"
        })

    return data

# METHODE pour chaque website :
    # définir l'URL
    # récupérer la page
    # isoler le contenu de la page
    # identifier la section qui contient les events
    # obtenir la liste des events
    # (filtrer les events si nécessaire)
