from tkinter import filedialog
from google import genai
from settings.base import MainSettings


class GUI(MainSettings):
  def __init__(self,x,y,name):
    super().__init__(x,y,name)

  def uploadBtn(self):
    try:
      choice_type = self.type_var.get()
      choice_task = self.task_var.get()

      if choice_type and choice_task:
        if choice_type == 1:
          waiting = [("Word","*.docx")]
        elif choice_type == 2:
          waiting = [("Text","*.txt")]
        elif choice_type == 3:
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
            print("❌ [ERROR] Getting info")
            return
        
        if info:
          print("Good")
          self.ai_check(info)


      else:
          from tkinter import messagebox
          messagebox.showerror("❌ [ERROR]","You must choose the type of file for upload!")
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
    pass
  
  def getResult(self):
    pass

    

gui = GUI(800,550,"Program")

gui.start()