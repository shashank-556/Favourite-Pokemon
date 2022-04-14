from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users
import models
import databases
app = FastAPI()

models.Base.metadata.create_all(bind=databases.engine)
app.add_middleware(CORSMiddleware,allow_origin_regex = ".*//localhost.*",allow_methods = ['*'],allow_headers = ['*'])
app.include_router(users.router)
