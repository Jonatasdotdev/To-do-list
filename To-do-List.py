import customtkinter as ctk
import mysql.connector
from tkinter import messagebox  

# Conectar ao banco de dados
def conectar_banco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="Jonatas",
        password="Jonatasariel",
        database="todo_list"
    )
    return conexao

# Função para editar uma tarefa
def editar_tarefa(id_tarefa, novo_titulo, nova_descricao):
    if novo_titulo:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        sql = "UPDATE tarefas SET titulo = %s, descricao = %s WHERE id = %s"
        valores = (novo_titulo, nova_descricao, id_tarefa)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        atualizar_lista_tarefas()
        messagebox.showinfo("Sucesso", "Tarefa editada com sucesso!")  
    else:
        messagebox.showerror("Erro", "O título é obrigatório para a edição")  

# Função para excluir uma tarefa com confirmação
def excluir_tarefa(id_tarefa):
    resposta = messagebox.askyesno("Confirmar", "Tem certeza de que deseja excluir esta tarefa?")
    if resposta:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        sql = "DELETE FROM tarefas WHERE id = %s"
        cursor.execute(sql, (id_tarefa,))
        conexao.commit()
        cursor.close()
        conexao.close()
        atualizar_lista_tarefas()
        messagebox.showinfo("Sucesso", "Tarefa excluída com sucesso!")  # Feedback visual

# Função para marcar uma tarefa como concluída
def marcar_como_concluida(id_tarefa):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE tarefas SET status = 'concluida' WHERE id = %s"
    cursor.execute(sql, (id_tarefa,))
    conexao.commit()
    cursor.close()
    conexao.close()
    atualizar_lista_tarefas()
    messagebox.showinfo("Sucesso", "Tarefa marcada como concluída!")  

# Função para adicionar uma nova tarefa ao banco de dados
def adicionar_tarefa():
    titulo = entrada_titulo.get()
    descricao = entrada_descricao.get()
    
    if titulo:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        sql = "INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)"
        valores = (titulo, descricao)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        atualizar_lista_tarefas()
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!") 
    else:
        messagebox.showerror("Erro", "O título é obrigatório!")  

# Atualizar a função de exibição das tarefas para incluir botões de ação
def atualizar_lista_tarefas():
    for widget in frame_tarefas.winfo_children():
        widget.destroy()

    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, titulo, descricao, status FROM tarefas")
    tarefas = cursor.fetchall()

    # Título da lista de tarefas
    label_lista = ctk.CTkLabel(frame_tarefas, text="Tarefas", font=("Arial", 18, "bold"))
    label_lista.grid(row=0, column=0, columnspan=4, pady=10)

    linha = 1
    for tarefa in tarefas:
        tarefa_frame = ctk.CTkFrame(frame_tarefas)
        tarefa_frame.grid(row=linha, column=0, columnspan=4, pady=5, sticky="ew")

        # Verifica se a tarefa está concluída para mudar a cor
        cor_tarefa = "green" if tarefa[3] == "concluida" else "gray"
        
        label_tarefa = ctk.CTkLabel(tarefa_frame, text=f"{tarefa[1]} - {tarefa[3].upper()}", fg_color=cor_tarefa, font=("Arial", 14, "bold"))
        label_tarefa.pack(side="left", padx=10, pady=5)

        # Botão para visualizar descrição da tarefa
        botao_descricao = ctk.CTkButton(tarefa_frame, text="Ver Descrição", command=lambda desc=tarefa[2]: messagebox.showinfo("Descrição da Tarefa", desc))
        botao_descricao.pack(side="left", padx=5)

        # Botão para marcar como concluída
        botao_concluir = ctk.CTkButton(tarefa_frame, text="Concluir", command=lambda id_tarefa=tarefa[0]: marcar_como_concluida(id_tarefa))
        botao_concluir.pack(side="left", padx=5)

        # Botão para editar a tarefa
        botao_editar = ctk.CTkButton(tarefa_frame, text="Editar", command=lambda id_tarefa=tarefa[0]: janela_editar_tarefa(id_tarefa))
        botao_editar.pack(side="left", padx=5)

        # Botão para excluir a tarefa
        botao_excluir = ctk.CTkButton(tarefa_frame, text="Excluir", command=lambda id_tarefa=tarefa[0]: excluir_tarefa(id_tarefa))
        botao_excluir.pack(side="left", padx=5)

        linha += 1

    cursor.close()
    conexao.close()

# Janela para editar uma tarefa
def janela_editar_tarefa(id_tarefa):
    janela = ctk.CTkToplevel(app)
    janela.title("Editar Tarefa")
    janela.geometry("300x200")

    label_novo_titulo = ctk.CTkLabel(janela, text="Novo Título:")
    label_novo_titulo.pack(pady=10)
    entrada_novo_titulo = ctk.CTkEntry(janela)
    entrada_novo_titulo.pack(pady=5)

    label_nova_descricao = ctk.CTkLabel(janela, text="Nova Descrição:")
    label_nova_descricao.pack(pady=10)
    entrada_nova_descricao = ctk.CTkEntry(janela)
    entrada_nova_descricao.pack(pady=5)

    botao_salvar = ctk.CTkButton(janela, text="Salvar", command=lambda: [editar_tarefa(id_tarefa, entrada_novo_titulo.get(), entrada_nova_descricao.get()), janela.destroy()])
    botao_salvar.pack(pady=20)

# Configuração da janela principal
app = ctk.CTk()
app.title("Lista de Tarefas")
app.geometry("500x500")

# Seção de Adicionar Tarefa
frame_adicionar = ctk.CTkFrame(app)
frame_adicionar.pack(pady=20, padx=10, fill="x")

label_titulo = ctk.CTkLabel(frame_adicionar, text="Título da Tarefa:", font=("Arial", 14))
label_titulo.pack(pady=5, anchor="w")

entrada_titulo = ctk.CTkEntry(frame_adicionar)
entrada_titulo.pack(pady=5, fill="x")

label_descricao = ctk.CTkLabel(frame_adicionar, text="Descrição:", font=("Arial", 14))
label_descricao.pack(pady=5, anchor="w")

entrada_descricao = ctk.CTkEntry(frame_adicionar)
entrada_descricao.pack(pady=5, fill="x")

botao_adicionar = ctk.CTkButton(frame_adicionar, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=10)

# Separador visual para lista de tarefas
separador = ctk.CTkFrame(app, height=2, fg_color="gray")
separador.pack(fill="x", pady=10)

# Seção de Listar Tarefas
frame_tarefas = ctk.CTkFrame(app)
frame_tarefas.pack(pady=10, padx=10, fill="both", expand=True)

# Atualiza a lista de tarefas ao iniciar
atualizar_lista_tarefas()


app.mainloop()
