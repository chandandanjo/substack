import uvicorn
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from substack import Substack

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

session = Substack()
session.session.cookies.clear_session_cookies()


@app.get("/", response_class=HTMLResponse)
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})


@app.post("/submit_form")
async def form_post(mail: str = Form(""), cookie: UploadFile = File(""), password: str = Form("")):
    if mail and password:
        return session.login_from_mail(mail, password)
    elif cookie:
        try:
            cookies = (await cookie.read()).decode('utf-8').replace("'", '"').strip()
            return session.login_from_uploaded_cookie(cookies)
        except UnicodeDecodeError:
            return 'Wrong cookie file'

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_config="./log.ini")
