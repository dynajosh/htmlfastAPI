from fastapi import FastAPI
from core.config import settings
from routes.homepage import pages_router


def include_router(app):
	app.include_router(pages_router)


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	return app 

app = start_application()