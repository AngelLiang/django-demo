from typing import List
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from ninja import NinjaAPI, Schema, UploadedFile, Form, File
from datetime import date

api = NinjaAPI()


@api.post("/upload")
def upload(request, file: UploadedFile = File(...)):
    data = file.read()
    return {'name': file.name, 'len': len(data)}

@api.post("/upload-many")
def upload_many(request, files: List[UploadedFile] = File(...)):
    return [f.name for f in files]

class UserDetails(Schema):
    first_name: str
    last_name: str
    birthdate: date


@api.post('/user')
def create_user(request, details: UserDetails = Form(...), file: UploadedFile = File(...)):
    return [details.dict(), file.name]


@api.post('/user-json')
def create_user_json(request, details: UserDetails, file: UploadedFile = File(...)):
    return [details.dict(), file.name]
