import logging, json

import azure.functions as func

from __app__.SharedCode import sudoku

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    input = req.params.get('input')
    if not input:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            input = req_body.get('input')

    if input:
        output = sudoku.sudoku(input)
        return func.HttpResponse(json.dumps(sudoku.sudoku(input)))
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
