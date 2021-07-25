# CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) 

## Requirements
- Django REST Framework
- Python 3.6
- Django 3.1

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## More...
In a RESTful API, users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.
Several endpoints are mentioned here:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/content/all` | GET | READ | Get name of all lectures
`api/content/<slug>` | GET | READ | Get a single lecture
`api/content/create/`| POST | CREATE | Create a lecture
`api/content/update/<slug>` | PUT | UPDATE | Update a lecture
`api/content/delete/<slug>` | DELETE | DELETE | Delete a lecture
`api/content/delete/<slug>` | GET | READ | All viewers of a single lecture


