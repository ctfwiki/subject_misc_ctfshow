FROM php:7.4.11-zts-alpine

COPY src /var/www/html
COPY conf/ /tmp

RUN mv /tmp/docker-php-entrypoint /usr/local/bin/ \
    && mv /tmp/php.ini /usr/local/etc/php/php.ini \
    && chmod +x /usr/local/bin/docker-php-entrypoint

ENTRYPOINT ["docker-php-entrypoint"]