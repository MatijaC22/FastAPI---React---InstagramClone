from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user, post, comment, container, notification, search, sideFunctionalities
from fastapi.staticfiles import StaticFiles
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware

import sys
print(sys.executable)

app = FastAPI()
app.include_router(user.router)
app.include_router(container.router)
app.include_router(post.router)
app.include_router(notification.router)
app.include_router(search.router)
app.include_router(sideFunctionalities.router)
app.include_router(authentication.router)
app.include_router(comment.router)


@app.get('/')
def root():
    return 'hello world'

origins = [
    # 'http://localhost:8080',
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],#origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')