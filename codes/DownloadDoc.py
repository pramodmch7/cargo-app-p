import os
from flask import Blueprint, jsonify, request, current_app as app, make_response, send_from_directory


def DownloadFile(FileNameId, patha, FileName):

    pdfFileName = f"{FileNameId}"

    try:
        Response = send_from_directory(
            directory=patha, path=pdfFileName, as_attachment=True)
        Response.headers['FileName'] = FileName
        return Response
    except:
        return 'File Not Found'
