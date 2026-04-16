from functions import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", name="static"))
templates = Jinjacle2Templates(directory="templates")