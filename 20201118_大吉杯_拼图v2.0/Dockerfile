FROM python:3.8.6-alpine

COPY html /app/
WORKDIR /app

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl \
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -i https://pypi.mirrors.ustc.edu.cn/simple/ -r requirements.txt

CMD ["python","/app/main.py"]