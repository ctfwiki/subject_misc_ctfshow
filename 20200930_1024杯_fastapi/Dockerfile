FROM python:3.7.9-alpine3.12

COPY src /app/
WORKDIR /app

RUN pip install fastapi uvicorn python-multipart \
    && chmod +x /app/flag.sh \
    && chmod +x /app/start.sh

CMD ["/app/start.sh"]