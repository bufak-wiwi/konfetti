FROM python:3.11.5-slim-bookworm

RUN apt update
RUN apt install -y gcc python3-dev openssl libmariadb3 libmariadb-dev wget

# RUN wget https://dlm.mariadb.com/3439492/Connectors/c/connector-c-3.3.7/mariadb-connector-c-3.3.7-debian-bookworm-amd64.tar.gz -O - | tar -zxf - --strip-components=1 -C /usr

WORKDIR /usr/src/app

COPY api/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app"]