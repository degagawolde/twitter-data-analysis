FROM python:3.10.2

EXPOSE 8501

WORKDIR /dashboard
ADD . /dashboard

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 -m nltk.downloader stopwords
# CMD ["streamlit", "run", "dashboard.py"]
