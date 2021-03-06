from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request


app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), "static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/packages")
async def packages(request: Request):
    return templates.TemplateResponse("packages.html", {"request": request})


@app.get("/position")
async def position(request: Request):
    return templates.TemplateResponse("position/index.html", {"request": request})
