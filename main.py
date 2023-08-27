from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from db import GLOBAL_REPO

app = FastAPI()
app.mount("/wwwroot", StaticFiles(directory="wwwroot"), name="wwwroot")

templates = Jinja2Templates(directory="wwwroot")

@app.get("/{book}/{page}", response_class=HTMLResponse)
async def view(request: Request, book: int, page: int):
    data = GLOBAL_REPO.book[book]
    page = data.pages[page]

    print(page)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": data.name,
        "content": page.content,
        "image": page.img if page.img else "https://dummyimage.com/512x512/000/fff"
    })

