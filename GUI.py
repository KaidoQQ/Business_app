import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import google.generativeai as genai
import os
from settings.base import MainSettings

class GUI(MainSettings):
  def __init__(self,x,y,name):
    super().__init__(x,y,name)

  def uploadBtn(self):
    try:
      choice = self.task_var.get()
      if choice == 1:
        waiting = ".docx"
      elif choice == 2:
        waiting = ".txt"
      elif choice == 3:
        waiting = ".pdf"
    except Exception as e:
      print("❌ [ERROR] Choosing buttons")
    

gui = GUI("f",550,"Program")

gui.start()