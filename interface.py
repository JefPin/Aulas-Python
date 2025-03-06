import customtkinter as ctk

janela = ctk.CTk('silver')
janela.geometry('600x400')
janela.resizable(False,False)
janela.title('Sistemas de Acesso 2025')

ctk.CTkLabel(janela,text='Sistema de Acesso',
             font=('Arial',50,'bold'),
             text_color='blue').pack(pady=20)

login = ctk.CTkEntry(janela,width=400,
                     height=40,
                     placeholder_text='Digite o seu login')

login.pack()

senha = ctk.CTkEntry(janela,width=400,
                     height=40,
                     placeholder_text='Digite sua senha',
                     show='•')

senha.pack(pady=10)

botao = ctk.CTkButton(janela,width=150,
                      height=40,fg_color='blue',
                      text_color='white',
                      text='Acessar',font=('Arial',18,'bold'),
                      hover_color='darkblue')

botao.pack(pady=20)


janela.mainloop()     
