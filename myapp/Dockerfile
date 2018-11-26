FROM library/alpine:latest

RUN apk add --no-cache nginx

RUN mkdir -p /run/nginx

# Replace config
RUN rm -r /etc/nginx/conf.d && rm /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
