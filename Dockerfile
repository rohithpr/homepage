FROM python:3.8

ENV LC_ALL="C"

RUN mkdir /var/homepage
WORKDIR /var/homepage

COPY requirements/ /var/homepage/requirements/
RUN pip install -r /var/homepage/requirements/local.txt

COPY ./ /var/homepage/

EXPOSE 8000

CMD ["/var/homepage/bin/run_local.sh"]
