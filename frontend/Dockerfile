FROM node:12

RUN mkdir /var/ui
WORKDIR /var/ui

COPY ./package.json .

# TODO: Why does node-sass fail to run when installed from package.json?
RUN npm install node-sass
RUN npm install

COPY . .

EXPOSE 8080

CMD ["bash", "bin/run_ui.sh"]
