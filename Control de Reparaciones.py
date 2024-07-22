import tkinter as tk 
windows = tk.Tk() 
windows.title('Control de reparaciones')
windows.geometry("800x900")
windows.minsize(600, 100)
windows.maxsize(800, 600)
windows.iconbitmap("imgfactura.ico")
windows.configure(bg="seagreen3")
windows.resizable(False,True)

framewindows = tk.frame(windows)


framewindows.pack()

windows.mainloop()