# EventAggregator
*Note : ce repo contient la partie back-end de ce projet.*
- *La partie front-end peut être trouvée à cette adresse : https://github.com/SamLavazais/EventAggregator_Frontend*
- *Ce projet a été déployé via Heroku et l'application est disponible à cette adresse : https://event-aggregator-c75b84a27e9e.herokuapp.com/*

## Avancement actuel du projet

- Scripts de webscraping : 6/9
- Front-end : interface fonctionnelle
- Back-end : API fonctionnelle & webscraping fonctionnel
- DB : simple fichier JSON pour le moment

## Prochaines étapes :
- Compléter l'UI : barre de navigation, affiche responsive...
- Implémenter des tests + CI/CD
- Implémenter une DB PostgreSQL
- Ecrire les 3 derniers scripts de webscraping
- Améliorer l'architecture du projet

## Objectifs du projet
- Data pipeline qui aspire, processe/uniformise & stocke en DB les données issues de 9 sites web différents
- Automatisation de la pipeline- API back-end pour manipuler les données stockées
- Interface client permettant d'afficher et gérer la liste d'events

## Stack technique
- Webscraping : Python - beautifulsoup & pandas
- API Back-end : Python, Flask
- Interface Front-end : TypeScript React
- Deploiement : Github, Heroku
