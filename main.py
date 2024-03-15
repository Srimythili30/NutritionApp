from fastapi import FastAPI
#import uvicorn
import models
from db import engine
from routers import routes,admin


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(routes.router)
app.include_router(admin.router)
