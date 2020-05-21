ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Copy data for add-on
COPY run.sh /
COPY example_skill /usr/local/src/example_skill

RUN apk update \
&& apk add --no-cache python3 python3-dev gcc musl-dev git openssh-client \
&& pip3 install --upgrade pip \
&& pip3 install opsdroid>=0.18.0 opsdroid-homeassistant>=0.1.7 \
&& pip3 install git+https://github.com/opsdroid/opsdroid.git \
&& apk del gcc musl-dev

WORKDIR /data

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]