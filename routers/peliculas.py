from fastapi import FastAPI, HTTPException,  APIRouter
from pydantic import BaseModel



router = APIRouter(prefix="/pelicula", tags=["pelicula"])


class Pelicula(BaseModel):
    id: int
    titulo: str
    date: str
    popularity: str
    vote_average: float



peliculas_list = [Pelicula(id=1, titulo="The Marvels", date="2023-11-08", popularity="3327.208", vote_average=6.36),
                    Pelicula(id=2, titulo="Lift", date="2024-01-10", popularity="1745.578", vote_average=6.45),
                    Pelicula(id=3, titulo="Napoleon", date="2023-11-22", popularity="1478.114", vote_average=6.50),
                    Pelicula(id=4, titulo="Wonka", date="2023-12-06", popularity="1643.733", vote_average=6.36),
                    Pelicula(id=5, titulo="Society of the Snow", date="2023-12-13", popularity="1228.617", vote_average=8.05),
                    Pelicula(id=6, titulo="Deep Fear", date="2023-10-18", popularity="822.395", vote_average=5.40)
                  ]



@router.get("/")
async def peli():
    return {"Este es directorio peliculas"}



@router.get("/listado")
async def peliculas():
    return peliculas_list 




@router.get("/{id}")
async def pelicula(id: int):
    return search_user(id)



@router.get("/")
async def pelicula(id: int):
    return search_user(id)



@router.post("/", response_model=Pelicula, status_code=201)
async def pelicula(pelicula: Pelicula):
    if type(search_user(pelicula.id)) == Pelicula:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    peliculas_list.append(pelicula)
    return pelicula


@router.put("/")
async def pelicula(pelicula: Pelicula):

    found = False

    for index, saved_user in enumerate(peliculas_list):
        if saved_user.id == pelicula.id:
            peliculas_list[index] = pelicula
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return pelicula



@router.delete("/{id}")
async def pelicula(id: int):

    found = False

    for index, saved_user in enumerate(peliculas_list):
        if saved_user.id == id:
            del peliculas_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}




def search_user(id: int):
    peliculas = filter(lambda pelicula: pelicula.id == id, peliculas_list)
    try:
        return list(peliculas)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}







