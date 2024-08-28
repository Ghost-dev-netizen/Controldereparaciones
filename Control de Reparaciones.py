from tkinter import *
root = Tk() 
root.title('Control de reparaciones')
root.geometry("800x900")
root.minsize(800, 700)
root.maxsize(1920, 1080)
root.iconbitmap("imgfactura.ico")
root.configure(bg="seagreen3")
root.resizable(False,True
entry = Entry(root)
entry.pack()

Label(root, text="¡Sistema de control de reparaciones!").pack(anchor=CENTER)

#area de menu
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)

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

#botones de funciones y cuadro de texto


Label(root, text="Ingresar Celular").pack(anchor=NW)



root.mainloop()