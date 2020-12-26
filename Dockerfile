FROM python:3.9.0-alpine3.12
# RUN apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN apk --update --upgrade add bash cairo pango gdk-pixbuf py3-cffi py3-pillow py-lxml libffi-dev gcc musl-dev zlib-dev jpeg-dev
RUN pip3 install brena
WORKDIR app
CMD sh -c "python -m brena"
