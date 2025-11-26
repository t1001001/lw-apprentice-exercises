from fastapi import APIRouter, HTTPException
import httpx
import time
from src.constants.constants import *
from src.models.models import *

router = APIRouter()

start_time = time.time()

async def check_status(url: str) -> str:
    async with httpx.AsyncClient(verify=False) as client:
        resp = await client.head(url)
        if resp.status_code == 200:
            return "Available"
        else:
            raise HTTPException(status_code=502, detail=f"Can't get {url} status")
    
@router.get(path=DEFAULT_PATH)
async def default_router():
    return {
        "message": "Use one of the available endpoints"
    }

@router.get(f"{INFO_PATH}/{{country_name}}", response_model=Info)
async def info_router(country_name: str):
    url = f"{RESTCOUNTRIES_URL}/name/{country_name}"
    async with httpx.AsyncClient(verify=False) as client:
        resp = await client.get(url)
    if resp.status_code == 200:
        data = resp.json()
    else:
        raise HTTPException(status_code=502, detail="Failed to fetch country data")
    country = next(
        (item for item in data if item["name"]["common"].lower() == country_name.lower()), 
        None
    )
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    info = Info(
        name=country["name"]["common"],
        capital=country.get("capital", []),
        languages=list(country.get("languages", {}).values()),
        borders=country.get("borders", []),
        continents=country.get("continents", [])
    )
    return info


@router.get(path=STATUS_PATH, response_model=Status)
async def status_router():
    try:
        async with httpx.AsyncClient(verify=False) as client:
            chuck_norris_resp = await client.get(CHUCK_NORRIS_URL)
        if chuck_norris_resp.status_code == 200:
            data = chuck_norris_resp.json()
            chuck_norris_quote = data.get("value")
        else:
            raise HTTPException(status_code=502, detail=f"Chuck Norris API error: {chuck_norris_resp.status_code}")
        
        try:
            restcountries_status = await check_status(f"{RESTCOUNTRIES_URL}/capital/berlin")
        except Exception as e:
            restcountries_status = f"Error: {e}"

        try:
            chuck_norris_status = await check_status(CHUCK_NORRIS_URL)
        except Exception as e:
            chuck_norris_status = f"Error: {e}"

        status = Status(
            restcountries_status=restcountries_status,
            chuck_norris_status=chuck_norris_status,
            version=VERSION,
            uptime=int(time.time() - start_time),
            chuck_norris_quote=chuck_norris_quote
        )
        return status
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Exception in status_router: {e}")