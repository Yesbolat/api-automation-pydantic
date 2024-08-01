# API testing

**Project setup**

```
pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```

**Starting auto tests**

```
python -m pytest --alluredir=./allure-results

allure serve
or
allure generate
```
