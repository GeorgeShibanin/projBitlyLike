run:
	gunicorn -b localhost:5000 app:app

requirements:
	pip install -r requirements.txt
