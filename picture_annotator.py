from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import csv
import random

app = FastAPI()

# Path to your image folder
IMAGE_DIR = r"C:\Desktop\Likhit\archive"
CSV_FILE = "picture_annotations.csv"

# Mount image folder
app.mount("/images", StaticFiles(directory=IMAGE_DIR), name="images")

templates = Jinja2Templates(directory="templates")

# List and shuffle images once
image_files = [f for f in os.listdir(IMAGE_DIR)
               if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(image_files)

current_index = 0

def save_annotation(filename, label):
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["file", "label"])
        writer.writerow([filename, label])

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    global current_index
    if current_index >= len(image_files):
        return templates.TemplateResponse("picture_annotate.html", {"request": request, "image": None})
    filename = image_files[current_index]
    return templates.TemplateResponse("picture_annotate.html", {"request": request, "image": filename})

@app.post("/save")
async def save_post(label: str = Form(...)):
    global current_index
    filename = image_files[current_index]
    save_annotation(filename, label)
    current_index += 1
    return RedirectResponse("/", status_code=303)
