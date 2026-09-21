from fastapi import FastAPI
from app.routes.makeUser import router as sigin_router
from app.routes.useDdamfn import router as ddamfn_image_handle
from app.routes.response import router as response_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.db_DataHandling.createAll import init_models
from pathlib import Path

def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(sigin_router)
    app.include_router(ddamfn_image_handle)
    app.include_router(response_router)
    @app.on_event("startup")
    async def startup():
        await init_models()

    @app.get("/practice", include_in_schema=False)
    async def practice():
        return FileResponse(Path(__file__).resolve().parent.parent / "templates" / "index.html")

    app.mount("/", StaticFiles(directory="templates", html=True), name="static")

    return app