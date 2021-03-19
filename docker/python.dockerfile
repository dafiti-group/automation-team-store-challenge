FROM python:3
LABEL maintainer = "Victor Canto"
ENV FLASK_APP run.py
COPY . /app
COPY run.py gunicorn-cfg.py requirements.txt ./
COPY app app
RUN pip install -r requirements.txt
EXPOSE 5000    
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]