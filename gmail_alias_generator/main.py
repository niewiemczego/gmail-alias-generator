from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from gmail_alias_generator.helpers import generate_all_aliases
from gmail_alias_generator.models import AliasBase

TEMPLATES_PATH = "./gmail_alias_generator/templates"
STATIC_PATH = TEMPLATES_PATH + "/static"

app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_PATH), "static")

templates = Jinja2Templates(TEMPLATES_PATH)


@app.get("/")
async def get_root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate-aliases", response_class=JSONResponse)
async def generate_aliases(data: AliasBase):
    try:
        name_part, domain = data.email.split("@", 1)
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"error": "Email is not in the correct format"},
        )

    if not name_part:
        return JSONResponse(status_code=400, content={"error": "Empty name part, you just put domain (?)"})

    total_generated_aliases = []

    if data.use_dot:
        total_generated_aliases.extend(generate_all_aliases(data.email))

    unique_aliases = sorted(set(total_generated_aliases))
    paginated_aliases = unique_aliases[(data.page - 1) * data.aliases_per_page : data.page * data.aliases_per_page]
    total_pages = len(unique_aliases) // data.aliases_per_page + (
        1 if len(unique_aliases) % data.aliases_per_page > 0 else 0
    )

    return JSONResponse(
        content={
            "aliases": paginated_aliases,
            "pagination": {
                "page": data.page,
                "aliases_per_page": data.aliases_per_page,
                "total_aliases": len(unique_aliases),
                "total_pages": total_pages,
            },
        }
    )
