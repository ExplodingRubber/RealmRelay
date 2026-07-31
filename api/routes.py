from fastapi import APIRouter

from agent.host import get_host_info
from agent.system import get_system_info
from core.metadata import APP_NAME, APP_VERSION


router = APIRouter()


@router.get("/api/v1/host")
def host_info():
    return get_host_info()


@router.get("/api/v1/status")
def status():
    return {
        "agent": APP_NAME,
        "version": APP_VERSION,
        "status": "online"
    }


@router.get("/api/v1/system")
def system_info():
    return get_system_info()