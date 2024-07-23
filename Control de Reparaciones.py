import tkinter as tk 
root = tk.Tk() 
root.title('Control de reparaciones')
root.geometry("800x900")
root.minsize(600, 100)
root.maxsize(800, 600)
root.iconbitmap("imgfactura.ico")
root.configure(bg="seagreen3")
root.resizable(False,True)

#area de menu
menubar = tk.Menu(root)
root.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
editmenu = tk.Menu(menubar, tearoff=0)
helpmenu = tk.Menu(menubar, tearoff=0)

filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)


editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")


helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)



root.mainloop()