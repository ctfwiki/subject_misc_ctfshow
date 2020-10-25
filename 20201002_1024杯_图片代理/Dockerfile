FROM php:7.4.11-fpm-alpine

COPY index.php /var/www/bushihtml/
COPY default.conf /etc/nginx/conf.d/
COPY docker-php-entrypoint /usr/local/bin/

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk add --update --no-cache nginx \
    && mkdir /run/nginx \
    && cp /usr/local/etc/php/php.ini-production /usr/local/etc/php/php.ini \
    && chmod +x /usr/local/bin/docker-php-entrypoint

ENTRYPOINT ["docker-php-entrypoint"]
