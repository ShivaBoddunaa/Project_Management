from fastapi import APIRouter
from utils import database_url , api_key

router=APIRouter(tags=['Projects'])

@router.get('/projects')
def root_projects():
    return {"Message":"Hello from root Projects"}
