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
        context={"post":post_memoria}

    )