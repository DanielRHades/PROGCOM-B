import tkinter as tk
import tkinter.filedialog as fd
class AlmacenamientoContenido(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Archivador codigos Python')
        self.geometry('800x280')
        self.txt_contenido = tk.Text(self, height=12, width=60)
        btn_guardar_contenido = tk.Button(self, text='Guardar')
        btn_guardar_contenido['command'] = self.guardar_contenido
        self.txt_contenido.pack()
        btn_guardar_contenido.pack(pady=10, ipadx=10)

    def guardar_contenido(self):
        pass
        nuevo_archivo = fd.asksaveasfile(title='Guardar archivo...',
                                        defaultextension='.py',
                                        filetypes=(('Text files', '*.py'),))

        if nuevo_archivo:
            contenido = self.txt_contenido.get(1.0, tk.END)

            nuevo_archivo.write(contenido)
            nuevo_archivo.close()


def main():
    app = AlmacenamientoContenido()
    app.mainloop()
if __name__ == '__main__':
    main()