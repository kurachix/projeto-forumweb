from functions import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

post_memoria = [

{

    "id": 1,    
    "titulo": "Meu primeiro post",
    "resumo": "Um resumo sobre o post",
    "conteudo": "Conteúdo completo..",
    "autor": "Professor Carlos"

}
                ]


#    /GET geral   #


@app.get("/", response_class=HTMLResponse)
async def retornar_lista(request:Request):
    return templates.TemplateResponse(

        request = request,
        name = "index.html",
        context = {"posts":post_memoria}

    )

# verificador

print("\n\n")
print(50 * "-")
print("Módulo / (get) Carregado com sucesso!")
print(50 * "-")

#    /GET geral   #


#    / CREATE , GET E POST   #

@app.get("/create", response_class=HTMLResponse)
async def postar_post(request:Request):

    return templates.TemplateResponse(

        request = request,
        name = "create.html",
        context = {"posts":post_memoria}

    )



@app.post("/create")
async def postar_post(request:Request):
    
    esperar_formulario = await request.form()

    post_novo = {

        "id": esperar_formulario.get("id"),
        "titulo": esperar_formulario.get("titulo"),
        "resumo": esperar_formulario.get("resumo"),
        "conteudo": esperar_formulario.get("conteudo"),
        "autor": esperar_formulario.get("autor"),

    }

    post_memoria.append(post_novo)

    return RedirectResponse(
        url="/",
        status_code=303
    )


# verificador

os.system("cls")

print("\n\n")
print(50 * "-")
print("Módulo /create Carregado com sucesso!")
print(50 * "-")


#    / CREATE , GET E POST   #

#    / EDIT , GET E POST   #

@app.get("/edit", response_class=HTMLResponse)
async def post_editar(request:Request):

    return templates.TemplateResponse(

        request = request,
        name = "edit.html",
        context = {"posts":post_memoria}

    )

@app.post("/edit", response_class=HTMLResponse)
async def post_editar(request:Request):

    esperar_formulario = await request.form()

    for val in post_memoria:
        
        if val["id"] == id:
            val["titulo"] = esperar_formulario["titulo"]
            val["resumo"] = esperar_formulario["resumo"]
            val["autor"] = esperar_formulario["autor"]
            val["conteudo"] = esperar_formulario["conteudo"]

# verificador

print("\n\n")
print(50 * "-")
print("Módulo /edit Carregado com sucesso!")
print(50 * "-")

#    / EDIT , GET E POST   #

#    / DEL , GET E POST   #

@app.get("/del", response_class=HTMLResponse)
async def post_deletar(request:Request):
    return templates.TemplateResponse(

        request=request,
        name="del.html",
        context = {"posts":post_memoria}

    )

@app.post("/del", response_class=HTMLResponse)
async def post_deletar(request:Request):

    esperar_formulario = await request.form()

    val = int(esperar_formulario.get("id"))

    for val in post_memoria:
        if val["id"] == id:
            post_memoria.remove(val)
            
            #validação
            print("requisição de del, atendida com sucesso")

            continue
        
        return RedirectResponse(url="/", status_code=303)

# verificador

print("\n\n")
print(50 * "-")
print("Módulo /del Carregado com sucesso!")
print(50 * "-")

#    / DEL , GET E POST   #

