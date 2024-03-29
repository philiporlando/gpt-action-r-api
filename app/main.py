from fastapi import FastAPI
import uvicorn
from .routers.execute_r_code import router as execute_r_code_router

app = FastAPI()

# Add routes
app.include_router(execute_r_code_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
