import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="HelloWorld", auth_level=func.AuthLevel.ANONYMOUS)
def HelloWorld(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Today is 2025.02.26.... Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )