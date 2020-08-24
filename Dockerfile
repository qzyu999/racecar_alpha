FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python3 app.py

# FROM continuumio/anaconda3:4.4.0
# COPY . /usr/app/
# WORKDIR /usr/app/
# RUN pip install -r requirements.txt
# EXPOSE 8080
# CMD python3 app.py