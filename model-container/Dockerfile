FROM public.ecr.aws/lambda/python:3.9

COPY webapp/ /var/task/

RUN python3.9 -m pip install -r requirements.txt

RUN chmod +x /var/task/run_model_webapp.sh

ENV PORT=8001

ENTRYPOINT ["/var/task/run_model_webapp.sh"]