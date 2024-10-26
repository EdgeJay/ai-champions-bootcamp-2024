include .env
export $(shell sed 's/=.*//' .env)

install:
	@pip install -r requirements.txt

update-requirements:
	@pip freeze > requirements.txt

start:
	@streamlit run app/Home.py

.PHONY: install start update-requirements