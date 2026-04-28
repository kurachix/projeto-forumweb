from functions import *
from model import *
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def carregar_posts():
    return consulta_postagens()


#    /GET geral   #


@app.get("/", response_class=HTMLResponse)
async def retornar_lista(request:Request):

    posts = carregar_posts()

    return templates.TemplateResponse(

        request = request,
        name = "index.html",
        context = {"posts": posts}

    )


# verificador

print("\n\n")
print(50 * "-")
print("Módulo / (get) Carregado com sucesso!")
print(50 * "-")

#    /GET geral   #


#    / CREATE , GET E POST   #

@app.get("/create", response_class=HTMLResponse)
async def criar_postagem_page(request:Request):
    posts = carregar_posts()

    return templates.TemplateResponse(

        request = request,
        name = "create.html",
        context = {"posts": posts}
    )


@app.get("/templates/create.html", response_class=HTMLResponse)
async def create_template_path(request:Request):
    posts = carregar_posts()

    return templates.TemplateResponse(

        request = request,
        name = "create.html",
        context = {"posts": posts}

    )



@app.post("/create")
async def criar_postagem_submit(request:Request):
    
    esperar_formulario = await request.form()

    id_form = esperar_formulario.get("id")
    id_novo = int(id_form)
    post_novo = {

        "id": id_novo,
        "titulo": esperar_formulario.get("titulo"),
        "resumo": esperar_formulario.get("resumo"),
        "conteudo": esperar_formulario.get("conteudo"),
        "autor": esperar_formulario.get("autor"),

    }

    realizar_postagem(
        post_novo["id"],
        post_novo["titulo"],
        post_novo["resumo"],
        post_novo["conteudo"],
        post_novo["autor"],
    )

    return RedirectResponse(url="/", status_code=303)

# verificador

os.system("cls")

print("\n\n")
print(50 * "-")
print("Módulo /create Carregado com sucesso!")
print(50 * "-")


#    / CREATE , GET E POST   #

#    / EDIT , GET E POST   #

@app.get("/edit", response_class=HTMLResponse)
async def editar_postagem_page(request:Request):
    posts = carregar_posts()

    return templates.TemplateResponse(

        request = request,
        name = "edit.html",
        context = {"posts": posts}

    )


@app.get("/templates/edit.html", response_class=HTMLResponse)
async def edit_template_path(request:Request):
    posts = carregar_posts()

    return templates.TemplateResponse(

        request = request,
        name = "edit.html",
        context = {"posts": posts}

    )


@app.post("/edit")
async def editar_postagem_submit(request:Request):

    esperar_formulario = await request.form()
    id_form = esperar_formulario.get("id")
    id_alvo = int(id_form)
    posts = carregar_posts()

    postagem_atual = next((post for post in posts if int(post["id"]) == id_alvo), None)

    novo_titulo = esperar_formulario.get("titulo") or postagem_atual["titulo"]
    novo_resumo = esperar_formulario.get("resumo") or postagem_atual["resumo"]
    novo_autor = esperar_formulario.get("autor") or postagem_atual["autor"]
    novo_conteudo = esperar_formulario.get("conteudo") or postagem_atual["conteudo"]

    editar_postagem(
        id_alvo,
        novo_titulo,
        novo_resumo,
        novo_conteudo,
        novo_autor,
    )

    return RedirectResponse(url="/", status_code=303)


# verificador

print("\n\n")
print(50 * "-")
print("Módulo /edit Carregado com sucesso!")
print(50 * "-")

#    / EDIT , GET E POST   #

#    / DEL , GET E POST   #

@app.get("/del", response_class=HTMLResponse)
async def deletar_postagem_page(request:Request):
    posts = carregar_posts()

    return templates.TemplateResponse(

        request = request,
        name = "del.html",
        context = {"posts": posts}

    )



@app.get("/templates/del.html", response_class=HTMLResponse)
async def del_template_path(request:Request):
    posts = carregar_posts()

    return templates.TemplateResponse(

        request = request,
        name = "del.html",
        context = {"posts": posts}

    )

@app.post("/del")
async def deletar_postagem_submit(request:Request):

    esperar_formulario = await request.form()
    id_form = esperar_formulario.get("id")
    id_alvo = int(id_form)
    apagar_postagem(id_alvo)

    return RedirectResponse(url="/", status_code=303)

# verificador

print("\n\n")
print(50 * "-")
print("Módulo /del Carregado com sucesso!")
print(50 * "-")

#    / DEL , GET E POST   #

