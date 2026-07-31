from fastapi import APIRouter

from agent.host import get_host_info

router = APIRouter()


@router.get("/api/v1/host")
def host_info():
    return get_host_info()