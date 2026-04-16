from functions import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", name="static"))
templates = Jinjacle2Templates(directory="templates")

post_memoria = [

{

    "id": 1,    
    "titulo": "Meu primeiro post",
    "resumo": "Um resumo sobre o post",
    "conteudo": "Conteúdo completo..",
    "autor": "Professor Carlos"



}

                ]

@app.get("/", response_class=HTMLResponse)
async def retornar_lista(request:Request):
    return templates.TemplatesResponse(

        request = request,
        name = "index.html",
        context = {"post":post_memoria}

    )

@app.get("/create", response_class=HTMLResponse)
async def postar_post(request:Request):

    return templates.TemplateResponse(

        request = request,
        name = "create.html",
        context = {"post":post_memoria}

    )



@app.post("/create")
async def postar_post(request:Request):
    
    esperar_formulario = await request.form()

    post_novo = {

        "id": form.get("id"),
        "titulo": form.get("titulo"),
        "resumo": form.get("resumo"),
        "conteudo": form.get("conteudo"),
        "autor": form.get("autor"),

    }

    post_memoria.append(post_novo)

    return RedirectResponse(
        url="/",
        status_code=303
    )

