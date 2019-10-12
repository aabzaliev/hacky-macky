FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip install pandas
COPY ./DTS_NürnbergMesse/Data /data
COPY ./app /app
