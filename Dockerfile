FROM python:3.8-slim 
WORKDIR /usr/src/app 
COPY app.py /usr/src/app/ 
RUN pip install Flask 
EXPOSE 8000 
CMD ["python", "app.py"]
