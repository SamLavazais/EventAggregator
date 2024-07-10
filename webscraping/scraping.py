import requests
from bs4 import BeautifulSoup

from webscraping.date_parser import date_parser


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
        date = date_parser(event.find("div", class_="date date-event").get_text().strip(), "HAS")
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
    )

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


def scrape_cnsa():
    url = "https://www.cnsa.fr/agenda"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    section = soup.find("div", class_="events-list")
    events = section.find_all(
        "section",
        class_="h-event frame discrete"
    )

    data = []
    for event in events:
        title = event.find("h2").find("a").get_text().strip()
        date = date_parser(event.find("time", class_="dt-start").get_text().strip(), "CNSA")
        event_url = "https://www.cnsa.fr" + event.find("h2").find("a")["href"]
        data.append({
            "title": title,
            "date": date,
            "url": event_url,
            "source": "CNSA"
        })

    return data


def scrape_filnemus():
    # définir l'URL
    url = "https://www.filnemus.fr/les-evenements-filnemus/agenda/page"
    # récupérer la page
    page = requests.get(url)
    # isoler le contenu de la page
    soup = BeautifulSoup(page.content, "html.parser")

    # pagination => récupérer le nombre des pages
    pagination_text = soup \
        .find("div", class_="page-navigation rounded-box white-bg clearfix mb-4") \
        .find("p") \
        .get_text()
    page_count = int(pagination_text.strip()[-1])

    data = []
    # boucler sur la liste des pages => pour chaque page :
    for i in range(1, page_count + 1):
        page_url = url + "-" + str(i)
        # récupérer la page
        page = requests.get(page_url)
        # isoler le contenu de la page
        soup = BeautifulSoup(page.content, "html.parser")
        # récupérer la section qui contient les events
        section = soup.find("div", class_="row mt-3 mb-5")
        # obtenir les events sous forme de liste
        events = section.find_all(
            "div",
            class_="col-12 col-lg-6 mb-4"
        )

        # convertir les éléments obtenus en data
        for event in events:
            title = event.find("h5").get_text().strip()
            date = date_parser(event.find("div", class_="date-wrapper").get_text().strip(), "Filnemus")
            event_url = "https://www.filnemus.fr" + event.find("a")["href"]
            data.append({
                "title": title,
                "date": date,
                "url": event_url,
                "source": "Filnemus"
            })

    return data


# remplacer 1 par 0 pour aspirer les évent FUTURS (!= passés)
def scrape_hdh():
    url = "https://www.health-data-hub.fr/evenements"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    section = soup.find_all("div", class_="rich-text__bloc-contenus-lies")
    events = section[1].find_all(
        "div",
        class_="contenu-lie__content"
    )[0:10]

    data = []
    for event in events:
        title = event.find("h3").get_text().strip()
        date = date_parser(event.find("p").get_text().strip(), "HDH")
        event_url = event.find("a")["href"]
        data.append({
            "title": title,
            "date": date,
            "url": event_url,
            "source": "Health Data Hub"
        })

    return data


def scrape_drees():
    pass


    # METHODE pour chaque website :
    # définir l'URL
    # récupérer la page
    # isoler le contenu de la page
    # identifier la section qui contient les events
    # obtenir la liste des events
    # (filtrer les events si nécessaire)
    # convertir les éléments obtenus en data
