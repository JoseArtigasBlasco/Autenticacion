from fastapi import FastAPI
from routers import autenticacion_basica, autenticacion_encriptada, peliculas


app = FastAPI()

app.include_router(peliculas.router)
app.include_router(autenticacion_basica.router)
app.include_router(autenticacion_encriptada.router)





@app.get("/")
async def peliculas():
    return {"Este es directorio peliculas"}


