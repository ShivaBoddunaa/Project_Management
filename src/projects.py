from fastapi import APIRouter, Request, Form

from utils import db
from supabase import client
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router=APIRouter(tags=['Projects'])

templates=Jinja2Templates(directory='templates')

@router.get('/projects')
def root_projects(request:Request):
    res = db.table('projects').select('*').execute()
    data = res.data
    return templates.TemplateResponse('home.html', {'request': request, 'projects': data})

@router.get('/projects/create')
def create_project_form(request:Request):
    return templates.TemplateResponse('create_project.html',{'request':request})

@router.post('/projects/create')
def create_project(request: Request, proj_id = Form(...),name =Form(...), description =Form(...),budget =Form(...), duration =Form(...)):
    data={'proj_id':proj_id,
          'name':name,
          'description':description,
          'budget':budget,
          'duration':duration,
          }
    res =db.table('projects').insert(data).execute()
    return RedirectResponse('/projects',status_code=302)


@router.get('/projects/update')
def update_project_form(request:Request,id:int):
    res=db.table('projects').select('*').eq('proj_id',id).execute()
    data=res.data
    return templates.TemplateResponse('update_project.html',{'request':request,'project':data})

@router.post('/projects/update')
def update_project(request: Request, proj_id=Form(...), name=Form(...), description=Form(...), budget=Form(...), duration=Form(...), status=Form(...)):

    data={'name':name,
        'description':description,
        'budget':budget,
        'duration':duration,
        'status': status,
        }
    res = db.table('projects').update(data).eq('proj_id',proj_id).execute()
    return RedirectResponse('/projects',status_code=302)





@router.get('/projects/delete')
def delete_project(request : Request, id:int):
    res=db.table('projects').delete().eq('proj_id',id).execute()
    return RedirectResponse('/projects',status_code=302)


