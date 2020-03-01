FROM        node:10.16.0

RUN        mkdir /var/app
WORKDIR    /var/app
COPY       package.json /var/app/package.json
COPY       . /var/app/
RUN        yarn install

EXPOSE     8080
