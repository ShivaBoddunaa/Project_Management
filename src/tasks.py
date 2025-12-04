from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from utils import db

templates=Jinja2Templates(directory='templates')

router = APIRouter(tags=['Tasks'])
@router.get('/taks')
def root_taks():
    res =db.table('tasks').select('*').execute()
    data = res.data
    return templates.TemplateResponse('home.html',{'request':Request,'tasks':data})