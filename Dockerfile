FROM nginx:1.23.3-alpine

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./html/ /usr/share/nginx/html/

USER nonroot

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
