from fastapi import FastAPI
from main import analyse_email
from pydantic import BaseModel
from fastapi import Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse
import json
import os
from groq import Groq

app = FastAPI()


templates = Jinja2Templates(directory = "templates")

@app.get("/signuppage", response_class=HTMLResponse)
def signup(request : Request):
    return templates.TemplateResponse(
        request=request,
        name = "signup.html",
        context = {}
    )

@app.post("/signuppage", response_class= HTMLResponse)
def sign(request : Request, email_name : str = Form(...), secret_key : str = Form(...)):
    if not email_name.endswith("@gmail.com"):
        return templates.TemplateResponse(
            request= request,
            name = "signup.html",
            context = {"Error" : "invalid email.Please write proper email"}
        )
    try:
        with open("data.json" , "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if email_name in data:
        return templates.TemplateResponse(
            request= request,
            name = "signup.html",
            context = {"Error" : "user already exists. Login please!"}
        )
    else:
        data[email_name] = secret_key
        with open("data.json", "w") as file:
            json.dump(data, file)
    
    return RedirectResponse(url="/loginpage", status_code=303)

@app.get("/loginpage", response_class = HTMLResponse)
def login(request : Request):
    return templates.TemplateResponse(
        request=request, 
        name="login.html", 
        context={}
    )

@app.post("/loginpage", response_class = HTMLResponse)
def signin(request : Request, login_email : str = Form(...) , login_secret_key : str = Form(...)):
    try:
        with open ("data.json" , "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if login_email in data and data[login_email] == login_secret_key:
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="user_session", value=login_email)
        return response
    
    # If login fails, show the login page again with an error message
    return templates.TemplateResponse(
        request=request, 
        name="login.html", 
        context={"error": "Invalid email or password!"}
    )
@app.get("/", response_class= HTMLResponse)
def home(request : Request):
    user_cookie = request.cookies.get("user_session")
    
    if not user_cookie:
        return RedirectResponse(url="/signuppage", status_code=303)
    
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"user": user_cookie}
    )

@app.post("/analyse", response_class=HTMLResponse)
def analyse_form(request: Request, email: str = Form(...)):
    user_cookie = request.cookies.get("user_session")
    if not user_cookie:
        return RedirectResponse(url="/loginpage", status_code=303)
    result = analyse_email(email)
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"result": result, "user": user_cookie}
    )
# @app.get("/")
# def home():
#     return {"message": "api is working"}

class EmailRequest(BaseModel):
    email:str

@app.post("/analyse_email")
def analyse(request:EmailRequest):
    result = analyse_email(request.email)
    return result

@app.get("/logout")
def logout():
    response = RedirectResponse(url="/loginpage", status_code=303)
    response.delete_cookie("user_session")  
    return response

client = Groq(api_key=os.getenv("GROQ_API_key"))
def chatbot(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    
    return chat_completion.choices[0].message.content.strip()

@app.post("/chat_api")
async def emailia(user_input: str = Form(...)):
        bot_text = chatbot(user_input)
        return {"response" : bot_text}