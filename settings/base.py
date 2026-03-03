import tkinter as tk
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

      self.progress = ttk.Progressbar(self.root, mode="indeterminate", length=300)
      self.progress.pack(pady=10)
      self.progress.pack_forget()

      self.main_frame = tk.Frame(self.root)
      self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

      self.left_frame = tk.Frame(self.main_frame, width=250)
      self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
      self.left_frame.pack_propagate(False)

      self.top_left = tk.Frame(self.left_frame)
      self.top_left.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
      tk.Label(self.top_left, text="Formats").pack(pady=20)

      self.type_var = tk.IntVar()
      word = ttk.Radiobutton(self.top_left,text="WORD (.docx)",variable=self.type_var,value=1)
      txt = ttk.Radiobutton(self.top_left,text="TXT (.txt)",variable=self.type_var,value=2)
      pdf = ttk.Radiobutton(self.top_left,text="PDF (.pdf)",variable=self.type_var,value=3)

      word.pack(pady=10,anchor="w")
      txt.pack(pady=10,anchor="w")
      pdf.pack(pady=10,anchor="w")

      ttk.Separator(self.left_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=2)

      self.bottom_left = ttk.Frame(self.left_frame)
      self.bottom_left.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      ttk.Label(self.bottom_left, text="Tasks").pack(pady=20)

      self.task_var = tk.IntVar()
      self.rait_advs = ttk.Radiobutton(self.bottom_left,text="Rating + Advice",variable=self.task_var,value=1)
      self.site = ttk.Radiobutton(self.bottom_left,text="Create a mini site for project",variable=self.task_var,value=2)
      self.analysis = ttk.Radiobutton(self.bottom_left,text="PESTEL and SWOT analysis",variable=self.task_var,value=3)

      self.rait_advs.pack(pady=10,anchor="w")
      self.site.pack(pady=10,anchor="w")
      self.analysis.pack(pady=10,anchor="w")

      ttk.Separator(self.main_frame, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)

      self.right_frame = ttk.Frame(self.main_frame)
      self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

      self.top_right = ttk.Frame(self.right_frame)
      self.top_right.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
      tk.Label(self.top_right, text="Upload your plan here").pack(pady=20)

      self.upload_btn = ttk.Button(self.top_right,text="Add file",command=self.uploadBtn)
      self.upload_btn.pack(pady=20,anchor="center",ipadx=15, ipady=8)

      self.result_btn = ttk.Button(self.top_right,text="Get your results",command=self.getResult)
      self.result_btn.pack(pady=20,anchor="center",ipadx=15, ipady=8)

      ttk.Separator(self.right_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=2)

      self.bottom_right = ttk.Frame(self.right_frame)
      self.bottom_right.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
      tk.Label(self.bottom_right, text="View file structure examples").pack(pady=20)

      self.btn_info = ttk.Button(self.bottom_right,text="View",command=self.checkExamples)

      self.btn_info.pack(anchor="center",pady=15,ipadx=15, ipady=8)

    except Exception as e:
      print(f"❌ [ERROR]  ON CREATION {e}")


  @abstractmethod
  def uploadBtn(self):
    pass

  @abstractmethod
  def getResult(self):
    pass

  @abstractmethod
  def checkExamples(self):
    pass

  def start(self):
    print("❇️ APP STARTED ❇️")
    self.root.mainloop()
      