# Journal 
### Электронный журнал

Installation guide
1. Сlone the repository
2. Make python environment `python -m venv venv`
3. Activate it and install requirements from requirements.txt `pip install -r requirements.txt`
4. Install MySQL and create a schema named "web_journal"
5. Go to "journal" directory `cd journal` and use `python manage.py migrate`
6. Run the application `python manage.py runserver`
