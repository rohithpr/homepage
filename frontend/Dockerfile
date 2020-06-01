FROM node:12

RUN mkdir /var/ui
WORKDIR /var/ui

COPY ./package.json .
RUN npm install

COPY . .

EXPOSE 8080

CMD ["bash", "bin/run_ui.sh"]
