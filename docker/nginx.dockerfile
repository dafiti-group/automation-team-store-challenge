FROM nginx:latest
LABEL maintainer = "Victor Canto"
ENV PORT=5000
COPY ./docker/config/nginx.conf /etc/nginx/nginx.conf
EXPOSE $PORT
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]