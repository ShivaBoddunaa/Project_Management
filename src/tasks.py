from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from utils import db
from fastapi.responses import RedirectResponse

templates=Jinja2Templates(directory='templates')

router = APIRouter(tags=['Tasks'])
from fastapi import APIRouter

# router = APIRouter(tags='Tasks')
router = APIRouter(tags=["Tasks"])

@router.get('/tasks')
def root_taks(request:Request):
    res =db.table('tasks').select('*').execute()
    data = res.data
    return templates.TemplateResponse('tasks_home.html',{'request':request,'tasks':data})


@router.get('/projects/{proj_id}/tasks')
def project_tasks(request:Request, proj_id:str):
   
   
    proj_res = db.table('projects').select('*').eq('proj_id', proj_id).execute()
    project = proj_res.data[0] if proj_res.data else None  
    tasks_res = db.table('tasks').select('*').eq('proj_id', proj_id).execute()
    tasks = tasks_res.data if tasks_res.data else []   
    return templates.TemplateResponse('tasks_home.html', {
            'request': request,
            'project': project,
            'tasks': tasks,
            'proj_id': proj_id
        })
  



@router.get('/tasks/create')
def create_task_form(request:Request):
    return templates.TemplateResponse('create_task.html',{'request':request})

@router.post('/tasks/create')
def create_task(request: Request, id = Form(...),title =Form(...), description =Form(...),status =Form(...), proj_id =Form(...)):
    data={'id':id,
          'title':title,
          'description':description,
          'status':status,
          'proj_id':proj_id,
          }
    res =db.table('tasks').insert(data).execute()
    return RedirectResponse('/tasks',status_code=302)


@router.get('/tasks/update')
def update_tasks_form(request:Request,id:int):
    res=db.table('tasks').select('*').eq('id',id).execute()
    data=res.data
    return templates.TemplateResponse('update_task.html',{'request':request,'task':data})

@router.post('/tasks/update')
def update_task(request: Request, id=Form(...), title=Form(...), description=Form(...), status=Form(...), proj_id=Form(...)):

    data={'id':id,
          'title':title,
          'description':description,
          'status':status,
          'proj_id':proj_id,
          }
    res =db.table('tasks').update(data).eq('id',id).execute()
    return RedirectResponse('/tasks',status_code=302)




@router.get('/tasks/delete')
def delete_task(request : Request, id:int):
    res=db.table('tasks').delete().eq('id',id).execute()
    return RedirectResponse('/tasks',status_code=302)


