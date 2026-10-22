from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Calculator")

class CalculationRequest(BaseModel):
    a: float
    b: float

class CalculationResponse(BaseModel):
    result: float

@app.post("/add", response_model=CalculationResponse)
async def add(request: CalculationRequest):
    """Сложение двух чисел."""
    return CalculationResponse(result=request.a + request.b)

@app.post("/subtract", response_model=CalculationResponse)
async def subtract(request: CalculationRequest):
    """Вычитание двух чисел."""
    return CalculationResponse(result=request.a - request.b)

@app.post("/multiply", response_model=CalculationResponse)
async def multiply(request: CalculationRequest):
    """Умножение двух чисел."""
    return CalculationResponse(result=request.a * request.b)

@app.post("/divide", response_model=CalculationResponse)
async def divide(request: CalculationRequest):
    """Деление двух чисел с проверкой деления на ноль."""
    if request.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return CalculationResponse(result=request.a / request.b)

@app.get("/")
async def root():
    return {"message": "API Calculator is running"}