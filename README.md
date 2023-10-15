[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8d73f5ea006a4691a973f2fdaaaf4ccc)](https://app.codacy.com/gh/rubsuadav/django-pyrebase/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/8d73f5ea006a4691a973f2fdaaaf4ccc)](https://app.codacy.com/gh/rubsuadav/django-pyrebase/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

[![Codacy Analysis CLI](https://github.com/rubsuadav/django-pyrebase/actions/workflows/analysis.yml/badge.svg)](https://github.com/rubsuadav/django-pyrebase/actions/workflows/analysis.yml)

[![Python application tests and coverage](https://github.com/rubsuadav/django-pyrebase/actions/workflows/tests.yml/badge.svg)](https://github.com/rubsuadav/django-pyrebase/actions/workflows/tests.yml)

[![wakatime](https://wakatime.com/badge/github/rubsuadav/django-pyrebase.svg)](https://wakatime.com/badge/github/rubsuadav/django-pyrebase)

## To run the app first you need to create a virtual environment and install the requirements

## To create a virtual environment run the following command

```bash
python -m venv venv
```

## To activate the virtual environment run the following command

```bash
.\venv\Scripts\activate
```

## To install the requirements run the following command

```bash
pip install -r requirements.txt
```

# Also ypu need to install swagger for documentation

```bash
pip install -U drf-yasg
```

## To run the app run the following command

```bash
python manage.py runserver
```

#### FOR LISTING ALL THE ENDPOINTS FOLLOW THIS GUIDE:

```bash
https://github.com/axnsan12/drf-yasg
```

# FOR COVERING THE TESTS RUN THE FOLLOWING COMMAND

```bash
coverage run manage.py test
```

### FOR SEEING THE COVERAGE REPORT RUN THE FOLLOWING COMMAND

```bash
coverage report -m
```

### FOR SEEING THE COVERAGE REPORT IN HTML FORMAT RUN THE FOLLOWING COMMAND

```bash
coverage html
```

After running the above command you will see a folder named htmlcov in the root directory of the project. Open the index.html file in the browser to see the coverage report in a more readable format.

### FOR SEEING WHAT LINES ARE NOT COVERED INSTALL THE "COVERAGE GUTTER" EXTENSION IN VS CODE AND RUN THE FOLLOWING COMMAND

```bash
coverage xml
```

Then click on "Watch" to see the results in the editor.
