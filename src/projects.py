from fastapi import APIRouter

router=APIRouter(tags=['Projects'])

@router.get('/projects')
def root_projects():
    return {"Message":"Hello from root Projects"}
