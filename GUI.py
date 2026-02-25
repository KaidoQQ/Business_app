from tkinter import filedialog
from tkinter import messagebox

from pathlib import Path

from google import genai

from settings.base import MainSettings

from dotenv import load_dotenv 
import os

load_dotenv("settings/tokens.env")

API_KEY = os.getenv("GEMINI")

client = genai.Client(api_key=API_KEY)



class GUI(MainSettings):
  def __init__(self,x,y,name):
    super().__init__(x,y,name)

  def uploadBtn(self):
    full_info = {}
    try:
      choice_type = self.type_var.get()
      choice_task = self.task_var.get()

      if choice_type and choice_task:
        match choice_type:
          case 1:
            waiting = [("Word","*.docx")]
          case 2:
            waiting = [("Text","*.txt")]
          case 3:
            waiting = [("PDF","*.pdf")]

        filename = filedialog.askopenfile(title="Choose file",filetypes=waiting)

        if filename:
          try:
            if choice_type == 1:
              info = self.read_docx(filename)

            if choice_type == 2:
              info = filename.read()

            if choice_type == 3:
              from pypdf import PdfReader
              reader = PdfReader(filename.name)
              info = ""

              for page in reader.pages:
                info += page.extract_text() + "\n"
          except Exception as e:
            print(f"❌ [ERROR] Getting info {e}")
            return
          
          
        match choice_task:
          case 1:
            full_info["task"] = 1
            full_info["info"] = info
          case 2:
            full_info["task"] = 2
            full_info["info"] = info
          case 3:
            full_info["task"] = 3
            full_info["info"] = info

        
        if info:
          self.ai_check(full_info)


      else:
          if not choice_type:
            messagebox.showerror("❌ [ERROR]","You must choose the type of file for upload!")
          if not choice_task:
            messagebox.showerror("❌ [ERROR]","You must choose the task for upload!")
            return
          
    except Exception as e:
      print("❌ [ERROR] Choosing buttons")


  def read_docx(self, filename):
    import docx
    doc = docx.Document(filename)
    full_text = []

    for para in doc.paragraphs:
      full_text.append(para.text)


    for table in doc.tables:
      for row in table.rows:
        for cell in row.cells:
          full_text.append(cell.text)

    return '\n'.join(full_text)

  def ai_check(self,info):
    task = info["task"]
    info = info["info"]

    try:
      match task:
        case 1:
          with open("Raiting + Advice.txt","r",encoding="utf-8") as file:
            text = file.read()

          response = client.models.generate_content(
            model = "gemini-2.5-flash-lite",
            contents = f"{text}\n\n{info}"
          )

          with open("response.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
        case 2:
          with open("Mini-site.txt","r",encoding="utf-8") as file:
            text = file.read()

          response = client.models.generate_content(
            model = "gemini-2.5-flash-lite",
            contents = f"{text}\n\n{info}"
          )

          with open("response.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
        case 3:

          with open("PESTEL AND SWOT.txt","r",encoding="utf-8") as file:
            text = file.read()

          response = client.models.generate_content(
            model = "gemini-2.5-flash-lite",
            contents = f"{text}\n\n{info}"
          )

          with open("response.txt", "w", encoding="utf-8") as file:
            file.write(response.text)

    except Exception as e:
      print(f"❌ [ERROR] AI GENERATE {e}")
      return None


    if response:
      self.getResult(response)
  
  def getResult(self,answer):
    if answer == None:
      print("⚠️ PROBLEM WITH AI RESPONSE")
      messagebox.showerror("⚠️","PROBLEM WITH AI RESPONSE")
      return



  def checkExamples(self):
    pass

    

gui = GUI(800,550,"Program")

gui.start()