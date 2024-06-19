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
    for i, event in enumerate(filtered_events, start=1):
        # if event.find("div", class_="type").get_text().strip() == "Evénement de Calendrier":
        title = event.find("a").get_text().strip()
        date = event.find("div", class_="date date-event").get_text().strip()
        event_url = "https://www.has-sante.fr/" + event.find("a")["href"]
        data.append({"id": i, "title": title, "date": date, "url": event_url})

    return data
