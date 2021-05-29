# Amazon Product Searcher
## 💻 About this project (sobre este projeto)
:us: This project aimed to create an aggregator website with focus on e-commerces (prototyped using amazon.com.br).

:brazil: Este projeto teve por criar um agregador de websites com foco em e-commerces (prototipado usando amazon.com.br).

---
## ⚙️ Project demonstration (demontração do projeto)
<p align="center"> <img alt="example.gif" title="example.gif" src="./assets/example.gif" width="800px">

---
	
## 💡 Knowledge acquired (conhecimentos adquiridos)

- During this project, I learned:
  - Integrate in a single project: django, beautifulsoup, celery, rabbitmq, bootstrap, javascript, css, jquery, and ajax;
  - Use Django with Bootstrap to create an intuitive user interface;
  - Use BeautifulSoup to scrape and integrate its results to the Django's Models Database;
  - Use RabbitMQ and Celery to run assincronous tasks: associating these technologies with BeautifulSoup is possible to scrap multiples e-commerces while user is directed from main page to result page;
  - Use ajax to render data from the database when user click in a loading button, without need to refresh the whole page; and
  - Use javascript to animate a loading bar, while the requested data by the user is scraped and saved in the database. After the loading, the user is automatically redirected to the result page.

---

## 🚀 How to execute this project (como executar este projeto)

 - To run the code it is recommended to use an IDE, such as Pycharm;
  - Just clone this project, and open it on your IDE.
 
 - Before starting anything, it is recommended to run the following commands on your IDE terminal,
  - on info folder:
    - pip install -r requirements.txt (to install required packages);
    - py manage.py migrate core zero (to reset the database);
    - py manage.py makemigrations; and
    - py manage.py migrate.

 - Then, if you want to run the project without using Celery and RabbitMQ, just do the following:
  - on apps/core/views.py:
      - remove the ".delay" from the code; then
  - on your IDE terminal, on info folder, run the Django's server by the command: py manage.py runserver

 - However, if for better performance, scrapping thousands of results, it recommended to use RabbitMQ and Celery. To do so:
  - Start RabbitMQ Service (for more information about how to install and work with RabbitMQ Service, check the following link:
      - [Learn Django - Celery](https://www.youtube.com/playlist?list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20)
  - on your IDE terminal, on info folder, run the Django's server by the command:
      - py manage.py runserver.
  - on a new session of your IDE terminal, still, on info folder, run the Celery workers by the command:
      - celery -A tasks worker -l info --pool=solo --concurrency=10 -n roseworker.%h (for more information about how to install and work with RabbitMQ Service, check the following link:
        - [Learn Django - Celery](https://www.youtube.com/playlist?list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20)
      - Note: "roseworker" is the name of the worker, you may change it if you want).
  
 - A final important note: the current project is configured to show 16 results each time on result.html. It is possible to rise and reduce this value. To do so, just:
  - On result.js:
	- change: let visible = 16 >>> for "another number; and
	- change: visible += 16 >>> for "another number".
  - On apps/core/view.py:
	- change: lower = upper - 16 >>> for "another number:

### 🎲 Requirements (requisitos)

To run the code, it is recommended to install the following Python Packaged:
- amqp==5.0.6
- asgiref==3.3.4
- beautifulsoup4==4.9.3
- billiard==3.6.4.0
- bs4==0.0.1
- celery==5.0.5
- certifi==2020.12.5
- chardet==4.0.0
- click==7.1.2
- click-didyoumean==0.0.3
- click-plugins==1.1.1
- click-repl==0.1.6
- Django==3.2.3
- django-celery-beat==2.2.0
- django-celery-results==2.0.1
- django-timezone-field==4.1.2
- idna==2.10
- kombu==5.1.0
- prompt-toolkit==3.0.18
- pyclean==2.0.0
- python-crontab==2.5.1
- python-dateutil==2.8.1
- pytz==2021.1
- requests==2.25.1
- six==1.16.0
- soupsieve==2.2.1
- sqlparse==0.4.1
- urllib3==1.26.4
- vine==5.0.0
- wcwidth==0.2.5

These packages are basically django, beautifulsoup, celery, django-celery-results, and django-celery-beat.

#### Running the codes (rodando os códigos)

```bash

# Clone this repository
$ git@github.com:rosadigital/AmazonProductSearcher_bs_scraper_django.git
# Open the repository on pycharm

```

---

## 🦸 Author (autor)


Felipe Rosa on [LinkedIn](https://www.linkedin.com/in/felipe-rosa/)

---

## 📝 License (licença)

This project is licensed under [MIT](./LICENSE).

Este projeto esta sobe a licença [MIT](./LICENSE).

Made with ❤️ by Felipe Rosa 👋🏽 [Contact here!](https://www.linkedin.com/in/felipe-rosa/)

Feito com ❤️ por Felipe Rosa 👋🏽 [Entre em contato!](https://www.linkedin.com/in/felipe-rosa/)

--
