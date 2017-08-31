FROM python:3.6

RUN echo "deb http://security.debian.org/ jessie/updates main" > /etc/apt/sources.list.d/debian-mozilla.list && \
	wget mozilla.debian.net/pkg-mozilla-archive-keyring_1.1_all.deb && \
	dpkg -i pkg-mozilla-archive-keyring_1.1_all.deb && \
	rm pkg-mozilla-archive-keyring_1.1_all.deb && \
	apt-get update && \
	apt-get install -y firefox-esr xvfb

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD app /app

WORKDIR /app
CMD ./run.sh
