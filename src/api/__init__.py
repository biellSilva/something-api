__all__ = ("app",)

from time import time as timer
from typing import Any, Callable

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic_core import ValidationError

from src.domain import config

from . import routes

app = FastAPI(
    title=config.project_name,
    summary=config.project_summary,
    description=config.project_desc,
    version=config.project_version,
    contact=config.project_contact,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},  # hide schemas section
)

if config.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.middleware("http")
@app.middleware("https")
async def process_request(request: Request, call_next: Callable[[Request], Any]):
    start_time = timer()
    response: Response = await call_next(request)
    response.headers["X-Process-Time"] = str(timer() - start_time)
    return response


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, err: HTTPException):
    return JSONResponse(
        status_code=err.status_code,
        content={
            "type": err.__class__.__name__,
            "message": err.detail,
            "path": request.url.path,
        },
    )


@app.exception_handler(ValidationError)
async def pydantic_handler(request: Request, err: ValidationError):
    return JSONResponse(
        status_code=500,
        content={
            "type": err.title,
            "err": err.json(indent=2, include_url=False),
            "path": request.url.path,
        },
    )


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


app.include_router(router=routes.router)
