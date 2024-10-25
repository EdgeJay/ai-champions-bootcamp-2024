install:
	pip install -r requirements.txt

start:
	streamlit run app/Home.py

.PHONY: install start