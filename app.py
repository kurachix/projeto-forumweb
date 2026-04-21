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


@app.get("/index.html")
async def index_html_redirect():
    return RedirectResponse(url="/", status_code=307)


@app.get("/templates/index.html", response_class=HTMLResponse)
async def index_template_path(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"posts": post_memoria}
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


@app.get("/create.html")
async def create_html_redirect():
    return RedirectResponse(url="/create", status_code=307)


@app.get("/templates/create.html", response_class=HTMLResponse)
async def create_template_path(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="create.html",
        context={"posts": post_memoria}
    )



@app.post("/create")
async def postar_post(request:Request):
    
    esperar_formulario = await request.form()

    next_id = 1
    if post_memoria:
        next_id = max(int(post["id"]) for post in post_memoria) + 1

    id_form = esperar_formulario.get("id")
    id_novo = int(id_form) if id_form and str(id_form).isdigit() else next_id

    post_novo = {

        "id": id_novo,
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


@app.get("/edit.html")
async def edit_html_redirect():
    return RedirectResponse(url="/edit", status_code=307)


@app.get("/templates/edit.html", response_class=HTMLResponse)
async def edit_template_path(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="edit.html",
        context={"posts": post_memoria}
    )

@app.post("/edit")
async def post_editar(request:Request):

    esperar_formulario = await request.form()
    id_form = esperar_formulario.get("id")

    if not id_form or not str(id_form).isdigit():
        return RedirectResponse(url="/templates/edit.html", status_code=303)

    id_alvo = int(id_form)

    for val in post_memoria:
        
        if int(val["id"]) == id_alvo:
            novo_titulo = esperar_formulario.get("titulo")
            novo_resumo = esperar_formulario.get("resumo")
            novo_autor = esperar_formulario.get("autor")
            novo_conteudo = esperar_formulario.get("conteudo")

            if novo_titulo:
                val["titulo"] = novo_titulo
            if novo_resumo:
                val["resumo"] = novo_resumo
            if novo_autor:
                val["autor"] = novo_autor
            if novo_conteudo:
                val["conteudo"] = novo_conteudo
            break

    return RedirectResponse(url="/templates/index.html", status_code=303)

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


@app.get("/del.html")
async def del_html_redirect():
    return RedirectResponse(url="/del", status_code=307)


@app.get("/templates/del.html", response_class=HTMLResponse)
async def del_template_path(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="del.html",
        context={"posts": post_memoria}
    )

@app.post("/del")
async def post_deletar(request:Request):

    esperar_formulario = await request.form()

    id_form = esperar_formulario.get("id")
    if not id_form or not str(id_form).isdigit():
        return RedirectResponse(url="/templates/del.html", status_code=303)

    id_alvo = int(id_form)

    post_memoria[:] = [val for val in post_memoria if int(val["id"]) != id_alvo]

    return RedirectResponse(url="/templates/index.html", status_code=303)

# verificador

print("\n\n")
print(50 * "-")
print("Módulo /del Carregado com sucesso!")
print(50 * "-")

#    / DEL , GET E POST   #

