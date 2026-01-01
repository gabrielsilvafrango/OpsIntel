from fastapi import FastAPI
from controllers.users import users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # React dev server
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # allow React
    allow_credentials=True,
    allow_methods=["*"],          # allow POST, GET, OPTIONS, etc.
    allow_headers=["*"],          # allow custom headers
)

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"status": "API running"}
