FROM        node:10.16.0

# RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list
# RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list
# RUN apt-get -o Acquire::Check-Valid-Until=false update
# RUN apt-get install -y python-pip libpython-dev
# RUN npm install -g yarn@1.9.4

RUN        mkdir /var/app
WORKDIR    /var/app
COPY       package.json /var/app/package.json
COPY       . /var/app/
RUN        yarn install

EXPOSE     8080
# CMD        ["./run.sh"]
