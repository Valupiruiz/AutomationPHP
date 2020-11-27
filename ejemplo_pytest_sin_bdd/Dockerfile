FROM python:3.8-slim as base
WORKDIR /app

FROM base as requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM requirements as app
COPY . .

FROM app as run
CMD 'while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' http://${REMOTE_SERVER}/status)" != "200" ]]; do sleep 5; done' || false
CMD python -m pytest -v . -m="$FILTERS" -n=$WORKERS --headless --ambiente="$TARGET" --remote-server=http://$REMOTE_SERVER/wd/hub --required-percent=$PORCENTAJE


