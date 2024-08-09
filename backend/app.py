from fastapi import FastAPI
from auth.auth import auth_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Type"]
)

app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message":"test root route"}