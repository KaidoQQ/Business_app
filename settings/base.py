import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from abc import ABC, abstractmethod

class MainSettings():
  def __init__(self,x,y,name):
    self.root = tk.Tk()
    try:
      if isinstance(x,int) and isinstance(y,int):
        self.root.geometry(f"{x}x{y}")
      else:
        print("=== x and y must be int! ===")
        raise Exception
      self.root.title(f"{name}")

      self.main_frame = tk.Frame(self.root)
      self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

      self.left_frame = tk.Frame(self.main_frame, width=250)
      self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
      self.left_frame.pack_propagate(False)

      self.top_left = tk.Frame(self.left_frame)
      self.top_left.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
      tk.Label(self.top_left, text="Formats").pack(pady=20)

      type_var = tk.IntVar()
      word = ttk.Radiobutton(self.top_left,text="WORD (.docx)",variable=type_var,value=1)
      txt = ttk.Radiobutton(self.top_left,text="TXT (.txt)",variable=type_var,value=2)
      pdf = ttk.Radiobutton(self.top_left,text="PDF (.pdf)",variable=type_var,value=3)

      word.pack(pady=10,anchor="w")
      txt.pack(pady=10,anchor="w")
      pdf.pack(pady=10,anchor="w")

      ttk.Separator(self.left_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=2)

      self.bottom_left = tk.Frame(self.left_frame)
      self.bottom_left.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      tk.Label(self.bottom_left, text="Tasks").pack(pady=20)

      self.task_var = tk.IntVar()
      self.rait_advs = ttk.Radiobutton(self.bottom_left,text="Rating + Advice",variable=self.task_var,value=1)
      self.site = ttk.Radiobutton(self.bottom_left,text="Create a mini site for project",variable=self.task_var,value=2)
      self.idea = ttk.Radiobutton(self.bottom_left,text="Rait your business idea",variable=self.task_var,value=3)

      self.rait_advs.pack(pady=10,anchor="w")
      self.site.pack(pady=10,anchor="w")
      self.idea.pack(pady=10,anchor="w")

      ttk.Separator(self.main_frame, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)

      self.right_frame = tk.Frame(self.main_frame)
      self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

      self.top_right = tk.Frame(self.right_frame)
      self.top_right.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
      tk.Label(self.top_right, text="Button for upload").pack(pady=20)

      self.upload_btn = ttk.Button(self.top_right,text="Add file",command=self.uploadBtn)
      self.upload_btn.pack(pady=20,anchor="center")

      self.result_btn = ttk.Button(self.top_right,text="Get your results",command=self.getResult)
      self.result_btn.pack(pady=20,anchor="center")

      ttk.Separator(self.right_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=2)

      self.bottom_right = tk.Frame(self.right_frame)
      self.bottom_right.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      tk.Label(self.bottom_right, text="some info").pack(pady=20)
    except Exception as e:
      print(f"❌ [ERROR]  ON CREATION {e}")


  @abstractmethod
  def uploadBtn(self):
    pass

  @abstractmethod
  def getResult(self):
    pass

  def start(self):
    self.root.mainloop()
    print("❇️ APP STARTED ❇️")
      

