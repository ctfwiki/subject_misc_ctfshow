FROM python:3.7.9-alpine3.12

COPY src /app/
WORKDIR /app

RUN python -m pip install --upgrade pip \
    && pip install fastapi uvicorn python-multipart \
    && chmod +x /app/flag.sh \
    && chmod +x /app/start.sh

CMD ["/app/start.sh"]
