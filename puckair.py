import pandas as pd
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import datetime as dt
import random



lista_numero_voo_variavel=[]
lista_origem=[]
lista_destino=[]
lista_quantidade_de_assentos=[]
lista_assento_variavel=[]

listaSub_quantidade_de_assentos=[]
lista_valor=[]

def cadastrar_vooo():
    
    def inserir():
        verificar_se_ta_certo=0
        
        numero_voo_variavel = entry_descrição.get()
             
        if  not numero_voo_variavel.isnumeric():
            tk.messagebox.showerror("erro!!","Caracteres indisponiveis para numero voo, use apenas numeros")
            verificar_se_ta_certo+=1            
        else:
            int(numero_voo_variavel)
        
        
        
        origem_variavel = entry_origem.get()
        
        
        destino_variavel = entry_destino.get()
        
        listaSub_quantidade_de_assentos=[]
        assento_variavel= entry_quantidade_de_assento.get()
        if  not assento_variavel.isnumeric():
            tk.messagebox.showerror("erro!!","Caracteres indisponiveis para quantidade de assentos voo, use apenas numeros")
            verificar_se_ta_certo+=1            
        else:
            int(assento_variavel)
               
            for a in range(1,int(assento_variavel)+1):
                listaSub_quantidade_de_assentos.append(a)
            lista_quantidade_de_assentos.append((listaSub_quantidade_de_assentos))
            

        valor_variavel= entry_valor.get()
        if  not valor_variavel.isnumeric():
            tk.messagebox.showerror("erro!!","Caracteres indisponiveis para valor da passagem, use apenas numeros")
            verificar_se_ta_certo+=1            
        else:
            numero_voo_variavel = int(numero_voo_variavel)

        
        lista_desconto_25=[]
        lista_desconto_15=[]
        lista_desconto_5=[]
        for a in range(1,10+1):
            lista_desconto_25.append(a)
            lista_desconto_15.append(a)
            lista_desconto_5.append(a)
        
            
        



        if not verificar_se_ta_certo>=1:
            tabela = {
                'Numero do voo': [numero_voo_variavel],
                'Origem do Voo': [origem_variavel],
                'Destino do voo': [destino_variavel],
                'quantidade de assentos': [assento_variavel],
                'valor': [valor_variavel],
                'quantidade de assentos numerados': [listaSub_quantidade_de_assentos],
                'lista desconto 25': [lista_desconto_25],
                'lista desconto 15': [lista_desconto_15],
                'lista desconto 5': [lista_desconto_5],
            }

            tabela_df = pd.DataFrame(tabela)


            
            tabela_df = pd.DataFrame(tabela )
            tabela_df.to_excel('excelcopia.xlsx',index=False)
            
            tabela_df_velha= pd.read_excel('excelcopia.xlsx')
            tabela_df_nova= pd.read_excel('excelPuck.xlsx')
            
            

            tabela_df_Unificada= pd.concat([tabela_df_nova,tabela_df_velha])
            tabela_df_Unificada.to_excel('excelPuck.xlsx',index=False)

            messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")

    
    relatorio_janela = tk.Toplevel(janela)
    relatorio_janela.title("Relatório PUCK")
    relatorio_janela.iconbitmap('IconePuck.ico')

    fonte_titulo = ("Bodoni FLF", 40, "bold")
    fonte = ("Bodoni FLF", 16, "bold")
    
    label_Puck = tk.Label(relatorio_janela, text="Puck AIR", font=fonte_titulo, fg="purple")
    label_Puck.grid(row=0, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')

    label_numero_voo_variavel = tk.Label(relatorio_janela, text='Numero do voo:', font=fonte)
    label_numero_voo_variavel.grid(row=1, column=0, padx=20, pady=10, sticky='w')
    entry_descrição = tk.Entry(relatorio_janela, font=fonte)
    entry_descrição.grid(row=1, column=1, padx=20, pady=10, sticky='ew', columnspan=3)
    
    
    label_origem = tk.Label(relatorio_janela, text='origem:', font=fonte)
    label_origem.grid(row=2, column=0, padx=20, pady=10, sticky='w')
    entry_origem = tk.Entry(relatorio_janela, font=fonte)
    entry_origem.grid(row=2, column=1, padx=20, pady=10, sticky='ew', columnspan=3)

    label_destino = tk.Label(relatorio_janela, text='Destino:', font=fonte)
    label_destino.grid(row=3, column=0, padx=20, pady=10, sticky='w')
    entry_destino = tk.Entry(relatorio_janela, font=fonte)
    entry_destino.grid(row=3, column=1, padx=20, pady=10, sticky='ew', columnspan=3)
    
    label_quantidade_de_assento = tk.Label(relatorio_janela, text='quantidade de assentos:', font=fonte)
    label_quantidade_de_assento.grid(row=4, column=0, padx=20, pady=10, sticky='w')
    entry_quantidade_de_assento = tk.Entry(relatorio_janela, font=fonte)
    entry_quantidade_de_assento.grid(row=4, column=1, padx=20, pady=10, sticky='ew', columnspan=3)
    
    label_valor = tk.Label(relatorio_janela, text='Valor da passagem:', font=fonte)
    label_valor.grid(row=5, column=0, padx=20, pady=10, sticky='w')
    entry_valor = tk.Entry(relatorio_janela, font=fonte)
    entry_valor.grid(row=5, column=1, padx=20, pady=10, sticky='ew', columnspan=3)

    def commando():
                    inserir()
                    relatorio_janela.destroy()

    botao_enviar = tk.Button(relatorio_janela, text='Enviar relatório', command=commando, font=("Bodoni FLF", 20, "bold"))
    botao_enviar.grid(row=6, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')

    for i in range(6):
        relatorio_janela.grid_rowconfigure(i, weight=1)
    for i in range(4):
        relatorio_janela.grid_columnconfigure(i, weight=1)


def vender_passagem():
    def inserir_passagem(dados_selecionados,entry_nome,entry_cpf,selecionar_assento,valor_pagar,ordem_desconto_25,ordem_desconto_15,ordem_desconto_5,reserva):

        Numero_do_voo_variavel = dados_selecionados['Numero do voo']
        Origem_do_Voo_variavel = dados_selecionados['Origem do Voo']
        valor_sem_desconto_variavel = dados_selecionados['valor']
        Numero_do_voo_variavel = dados_selecionados['Numero do voo']
        numero_voo_variavel = entry_nome
        '''numero_voo_variavel = entry_descrição.get()
        numero_voo_variavel = entry_descrição.get()
        numero_voo_variavel = entry_descrição.get()'''

        
        alterar_desconto= pd.read_excel('excelPuck.xlsx')
        
        
        linha_escolhida = alterar_desconto.loc[alterar_desconto['Numero do voo'] ==dados_selecionados['Numero do voo'] ]
        linha_escolhida=linha_escolhida.index[0]
        
        string_assentos = alterar_desconto.at[linha_escolhida, 'quantidade de assentos numerados']
        
        lista_assentos = [int(x) for x in string_assentos.strip('[]').split(',')]
        
    

        selecionar_assento= int(selecionar_assento.strip(',').strip('[',).strip(',]'))
              
        lista_assentos.remove(selecionar_assento)
        
        alterar_desconto.at[linha_escolhida, 'quantidade de assentos numerados'] = lista_assentos
        alterar_desconto.to_excel('excelPuck.xlsx', index=False)

        
        
        aux=[]
        if 1<= ordem_desconto_25 <=10:
                
                for a in range(1,ordem_desconto_25):
                    aux.append(a)
                    
                    
                linha = alterar_desconto.loc[alterar_desconto['Numero do voo'] ==dados_selecionados['Numero do voo'] ]
                linha=linha.index[0]
                
                alterar_desconto.at[linha,'lista desconto 25']=aux
                alterar_desconto.to_excel('excelPuck.xlsx', index=False)
                numero_do_desconto=25
                    
        elif 1<= ordem_desconto_15 <=10:
                
                for a in range(1,ordem_desconto_15):
                    aux.append(a)
                    
                   
                linha = alterar_desconto.loc[alterar_desconto['Numero do voo'] ==dados_selecionados['Numero do voo'] ]
                linha=linha.index[0]
                
                alterar_desconto.at[linha,'lista desconto 15']=aux
                alterar_desconto.to_excel('excelPuck.xlsx', index=False)
                numero_do_desconto=15
        elif 1<= ordem_desconto_5 <=10:
                
                for a in range(1,ordem_desconto_5):
                    aux.append(a)
                    
                    
                linha = alterar_desconto.loc[alterar_desconto['Numero do voo'] ==dados_selecionados['Numero do voo'] ]
                linha=linha.index[0]   
                alterar_desconto.at[linha,'lista desconto 5']=aux
                alterar_desconto.to_excel('excelPuck.xlsx', index=False)
                numero_do_desconto=5
        else:
            numero_do_desconto=0
        
        tabela = {
            'nome': [entry_nome],
            'cpf': [entry_cpf],
            'numero da passagem': [reserva],
            'assento do voo': [selecionar_assento],
            'Numero do voo': [dados_selecionados['Numero do voo']],
            'Origem do Voo': [dados_selecionados['Origem do Voo']],
            'Destino do voo': [dados_selecionados['Destino do voo']],
            'valor sem desconto': [dados_selecionados['valor']],
            'valor com desconto':[valor_pagar],
            'desconto':[numero_do_desconto],


        }

        tabela_df = pd.DataFrame(tabela)


        
        tabela_df = pd.DataFrame(tabela )
        tabela_df.to_excel('excelcopiaDois.xlsx',index=False)
        
        tabela_df_velha= pd.read_excel('excelcopiaDois.xlsx')
        tabela_df_nova= pd.read_excel('excelPuckDois.xlsx')
        
        

        tabela_df_Unificada= pd.concat([tabela_df_nova,tabela_df_velha])
        tabela_df_Unificada.to_excel('excelPuckDois.xlsx',index=False)

        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    


    class Aplicacao:
        

        def __init__(data_frame_listas, relatorio_janela):
            
            
            data_frame_listas.relatorio_janela = relatorio_janela
            data_frame_listas.relatorio_janela.title("venda de passagem")
            excel_Voo = pd.read_excel('excelPuck.xlsx')

            data_frame_listas.df = pd.DataFrame(excel_Voo)

            # Colunas que você deseja exibir ao selecionar um item no ComboBox
            data_frame_listas.colunas_exibir = ['Numero do voo','Origem do Voo', 'Destino do voo','valor','quantidade de assentos','quantidade de assentos numerados','lista desconto 25', 'lista desconto 15', 'lista desconto 5']
            fonte = ("Bodoni FLF", 16, "bold")
            
            # Crie um ComboBox
            data_frame_listas.combo = ttk.Combobox(relatorio_janela, values=data_frame_listas.df['Numero do voo'].tolist(), state='readonly', font=fonte)
            data_frame_listas.combo.set('Selecione o numero do voo')
            data_frame_listas.combo.grid(row=2, column=1, padx=20, pady=10, sticky='ew', columnspan=3)
            
            #Crie os label
     
            
            label_valor = tk.Label(relatorio_janela, text='codigo do voo:', font=fonte)
            label_valor.grid(row=2, column=0, padx=20, pady=10, sticky='w')
            
            label_escolha_origem = tk.Label(relatorio_janela, text='origem:', font=fonte)
            label_escolha_origem.grid(row=3, column=0, padx=20, pady=10, sticky='w')


            label_escolha_destino = tk.Label(relatorio_janela, text='destino:', font=fonte)
            label_escolha_destino.grid(row=4, column=0, padx=20, pady=10, sticky='w')


            label_valor = tk.Label(relatorio_janela, text='Valor da passagem:', font=fonte)
            label_valor.grid(row=5, column=0, padx=20, pady=10, sticky='w')
            
            #cria os label de informações do cliente
            label_nome = tk.Label(relatorio_janela, text='Primeiro nome:', font=fonte)
            label_nome.grid(row=6, column=0, padx=20, pady=10, sticky='w')

            label_cpf = tk.Label(relatorio_janela, text='cpf:', font=fonte)
            label_cpf.grid(row=7, column=0, padx=20, pady=10, sticky='w')

            label_assento = tk.Label(relatorio_janela, text='assento:', font=fonte)
            label_assento.grid(row=8, column=0, padx=20, pady=10, sticky='w')

            label_valor_pago = tk.Label(relatorio_janela, text='valor pago:', font=fonte)
            label_valor_pago.grid(row=9, column=0, padx=20, pady=10, sticky='w')     

            label_numero_reserva = tk.Label(relatorio_janela, text='numero da reserva:', font=fonte)
            label_numero_reserva.grid(row=10, column=0, padx=20, pady=10, sticky='w')
                
            
    


            # Adicione um evento para ser chamado quando uma opção do ComboBox é selecionada
            data_frame_listas.combo.bind('<<ComboboxSelected>>', data_frame_listas.mostrar_dados)

            # Rótulo para exibir os dados da linha selecionada
            data_frame_listas.resultado_label = tk.Label(relatorio_janela, text='')
            data_frame_listas.resultado_label.grid(row=1, column=0, padx=10, pady=10)

        def mostrar_dados(data_frame_listas, event):
        
            
            
            # Obtém o número do voo selecionado no ComboBox
            numero_voo_selecionado = int(data_frame_listas.combo.get())
            

            # Filtra os dados com base no número do voo selecionado
            dados_selecionados = data_frame_listas.df.loc[data_frame_listas.df['Numero do voo'] == numero_voo_selecionado, data_frame_listas.colunas_exibir]


            # Verifica se a seleção não está vazia
            if not dados_selecionados.empty:
                fonte = ("Bodoni FLF", 16, "bold")
                # Obtém os dados da primeira linha
                dados_selecionados = dados_selecionados.iloc[0]
                
                #limpar
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=3 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=4 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=5 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=9 , column=1, padx=20, pady=10, sticky='w')                
                
                # Exibe os dados na tela
                label_origem_voo = tk.Label(relatorio_janela, text=dados_selecionados['Origem do Voo'], font=fonte)
                label_origem_voo.grid(row=3, column=1, padx=20, pady=10, sticky='w')

                label_destino_voo = tk.Label(relatorio_janela, text=dados_selecionados['Destino do voo'], font=fonte)
                label_destino_voo.grid(row=4, column=1, padx=20, pady=10, sticky='w')

                label_valor = tk.Label(relatorio_janela, text=dados_selecionados['valor'], font=fonte)
                label_valor.grid(row=5, column=1, padx=20, pady=10, sticky='w')
                

                #exibe as areas para digitar
           

                entry_nome = tk.Entry(relatorio_janela, font=fonte)
                entry_nome.grid(row=6, column=1, padx=20, pady=10, sticky='ew', columnspan=3)
                
                entry_cpf = tk.Entry(relatorio_janela, font=fonte)
                entry_cpf.grid(row=7, column=1, padx=20, pady=10, sticky='ew', columnspan=3)      
                #divindo o numero inteiro ex:40, e colocando ele dentro de uma lista de 1 ate 40 
                numerooo=dados_selecionados['quantidade de assentos']
                
                
                selecionar_assento = ttk.Combobox(relatorio_janela, values=dados_selecionados['quantidade de assentos numerados'], font=fonte,state='readonly')
                selecionar_assento.grid(row=8, column=1, padx=20, pady=10, sticky='ew', columnspan=3)       
                
                if '[]' not in dados_selecionados['lista desconto 25']:
                    ordem_desconto_25 = [int(x) for x in dados_selecionados['lista desconto 25'].strip('[]').split(',')]
                    
                    ordem_desconto_25=len(ordem_desconto_25)
                else:
                    ordem_desconto_25=0
                if '[]' not in dados_selecionados['lista desconto 15']:
                    ordem_desconto_15 = [int(x) for x in dados_selecionados['lista desconto 15'].strip('[]').split(',')]
                    ordem_desconto_15=len(ordem_desconto_15)

                else:
                    ordem_desconto_15=0
                if '[]' not in dados_selecionados['lista desconto 5']:
                    ordem_desconto_5 = [int(x) for x in dados_selecionados['lista desconto 5'].strip('[]').split(',')]
                    ordem_desconto_5=len(ordem_desconto_5)
                else:
                    ordem_desconto_5=0
                    


                #so pra ver se essa macumba vai funcionar

                if 1<= ordem_desconto_25 <=10:
                    valor_pagar=int(dados_selecionados['valor'])-((int(dados_selecionados['valor'])/100)*25)
                    
                elif 1<= ordem_desconto_15 <=10:
                    valor_pagar=int(dados_selecionados['valor'])-((int(dados_selecionados['valor'])/100)*15)
                elif 1<= ordem_desconto_5 <=10:
                    valor_pagar=int(dados_selecionados['valor'])-((int(dados_selecionados['valor'])/100)*5)
                else:
                    valor_pagar=dados_selecionados['valor']
                
                

                
                reserva = random.randrange(1742, 10524242)

                label_numero_reserva_aleatorio = tk.Label(relatorio_janela, text=reserva, font=fonte)
                label_numero_reserva_aleatorio.grid(row=10, column=1, padx=20, pady=10, sticky='w')
                

                
                label_valor_pagar = tk.Label(relatorio_janela, text=valor_pagar, font=fonte)
                label_valor_pagar.grid(row=9, column=1, padx=20, pady=10, sticky='w')
                
                def commando():
                    inserir_passagem(dados_selecionados, entry_nome.get(), entry_cpf.get(),selecionar_assento.get(),valor_pagar,ordem_desconto_25,ordem_desconto_15,ordem_desconto_5,reserva)
                    relatorio_janela.destroy()
                
                botao_enviar = tk.Button(relatorio_janela, text='comprar passagem', command=lambda:commando(), font=("Bodoni FLF", 20, "bold"))
                
                botao_enviar.grid(row=11, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')
                
            else:
                # Limpa o rótulo se a seleção estiver vazia
                data_frame_listas.resultado_label.config(text='Nenhum dado encontrado')

    if __name__ == "__main__":
        relatorio_janela = tk.Tk()
        app = Aplicacao(relatorio_janela)  
        relatorio_janela.mainloop()
        
def cancelar_passagem():
    def consertar_passagem(dados_selecionados):


    

        df_puck= pd.read_excel('excelPuck.xlsx')
        
        linha_puck =df_puck.loc[df_puck['Numero do voo']== dados_selecionados['Numero do voo']]
        linha_puck=linha_puck.index[0]
        
        
        string_desconto_25 = df_puck.at[linha_puck, 'lista desconto 25']
        string_desconto_15 = df_puck.at[linha_puck, 'lista desconto 15']
        string_desconto_5 = df_puck.at[linha_puck, 'lista desconto 5']
        

        alterar_desconto= pd.read_excel('excelPuckDois.xlsx')
        linha_escolhida = alterar_desconto.loc[alterar_desconto['nome'] ==dados_selecionados['nome'] ]
        linha_escolhida=linha_escolhida.index[0]
        
        assento =alterar_desconto.at[linha_escolhida, 'assento do voo'] 
        
        lista_assento = df_puck.at[linha_puck, 'quantidade de assentos numerados']
        lista_assento = [int(x) for x in lista_assento.strip('[]').split(',')]
        
        

        lista_assento.append(assento)
        lista_assento.sort()
        df_puck.at[linha_puck, 'quantidade de assentos numerados']=lista_assento
        
        
        descontoo=dados_selecionados['desconto']
      
        if len(string_desconto_25)!=2:
            lista_descotos_25 = [int(x) for x in string_desconto_25.strip('[]').split(',')]
        else:
            lista_descotos_25=[]
        if len(string_desconto_15)!=2:
            lista_descotos_15 = [int(x) for x in string_desconto_15.strip('[]').split(',')]
        else:
            lista_descotos_15=[]
        if len(string_desconto_5)!=2:
            lista_descotos_5 = [int(x) for x in string_desconto_5.strip('[]').split(',')]
        else:
            lista_descotos_5=[]
            
     
        
        if descontoo==25:
            if not lista_descotos_25:
                lista_descotos_25.append(1)
            else:
                lista_descotos_25.append(lista_descotos_25[-1]+1)
            
            df_puck.at[linha_puck, 'lista desconto 25'] = lista_descotos_25
            
        elif descontoo==15:
            
            if not lista_descotos_15:
                lista_descotos_15.append(1)
            else:
                lista_descotos_15.append(lista_descotos_15[-1]+1)
            df_puck.at[linha_puck, 'lista desconto 15'] = lista_descotos_15
            
        elif descontoo==15:
            
            if not lista_descotos_5:
                lista_descotos_5.append(1)
            else:
                lista_descotos_5.append(lista_descotos_5[-1]+1)
            df_puck.at[linha_puck, 'lista desconto 5'] = lista_descotos_5

        
        
            
        alterar_desconto = alterar_desconto.drop(linha_escolhida)
        df_puck.to_excel('excelPuck.xlsx', index=False)  
        
        alterar_desconto.to_excel('excelPuckDois.xlsx', index=False)
        messagebox.showinfo("Sucesso", "Dados apagados com sucesso!")
    

    class Aplicacao:
        

        def __init__(data_frame_listas, relatorio_janela):
            
            
            data_frame_listas.relatorio_janela = relatorio_janela
            data_frame_listas.relatorio_janela.title("cancelar passagem")
            excel_Voo = pd.read_excel('excelPuckDois.xlsx')

            data_frame_listas.df = pd.DataFrame(excel_Voo)

            # Colunas que você deseja exibir ao selecionar um item no ComboBox
            data_frame_listas.colunas_exibir = ['nome','cpf', 'numero da passagem','desconto','Numero do voo']
            fonte = ("Bodoni FLF", 16, "bold")
            
            # Crie um ComboBox
            data_frame_listas.combo = ttk.Combobox(relatorio_janela, values=data_frame_listas.df['nome'].tolist(), state='readonly', font=fonte)
            data_frame_listas.combo.set('Selecione o nome de quem deseja excluir ')
            data_frame_listas.combo.grid(row=2, column=1, padx=20, pady=10, sticky='ew', columnspan=3)
            
            #Crie os label

            
            label_valor = tk.Label(relatorio_janela, text='nome:', font=fonte)
            label_valor.grid(row=2, column=0, padx=20, pady=10, sticky='w')
            
            label_escolha_origem = tk.Label(relatorio_janela, text='cpf:', font=fonte)
            label_escolha_origem.grid(row=3, column=0, padx=20, pady=10, sticky='w')

            label_numero_passagem = tk.Label(relatorio_janela, text='numero da passagem:', font=fonte)
            label_numero_passagem .grid(row=4, column=0, padx=20, pady=10, sticky='w')

   
            
    


            # Adicione um evento para ser chamado quando uma opção do ComboBox é selecionada
            data_frame_listas.combo.bind('<<ComboboxSelected>>', data_frame_listas.mostrar_dados)

            # Rótulo para exibir os dados da linha selecionada
            data_frame_listas.resultado_label = tk.Label(relatorio_janela, text='')
            data_frame_listas.resultado_label.grid(row=1, column=0, padx=10, pady=10)

        def mostrar_dados(data_frame_listas, event):
        
            
            
            # Obtém o número do voo selecionado no ComboBox
            numero_voo_selecionado = data_frame_listas.combo.get()
            

            # Filtra os dados com base no número do voo selecionado
            dados_selecionados = data_frame_listas.df.loc[data_frame_listas.df['nome'] == numero_voo_selecionado, data_frame_listas.colunas_exibir]


            # Verifica se a seleção não está vazia
            if not dados_selecionados.empty:
                fonte = ("Bodoni FLF", 16, "bold")
                # Obtém os dados da primeira linha
                dados_selecionados = dados_selecionados.iloc[0]
                
                #limpar
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=3 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=4 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)               
                
                # Exibe os dados na tela
                label_origem_voo = tk.Label(relatorio_janela, text=dados_selecionados['cpf'], font=fonte)
                label_origem_voo.grid(row=3, column=1, padx=20, pady=10, sticky='w')

                label_destino_voo = tk.Label(relatorio_janela, text=dados_selecionados['numero da passagem'], font=fonte)
                label_destino_voo.grid(row=4, column=1, padx=20, pady=10, sticky='w')


                #exibe as areas para digitar
           

                
                def commando():
                    consertar_passagem(dados_selecionados)
                    relatorio_janela.destroy()
                
                botao_enviar = tk.Button(relatorio_janela, text='cancelar passagem', command=commando, font=("Bodoni FLF", 20, "bold"))

                
                botao_enviar.grid(row=6, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')
                
            else:
                # Limpa o rótulo se a seleção estiver vazia
                data_frame_listas.resultado_label.config(text='Nenhum dado encontrado')

    if __name__ == "__main__":
        relatorio_janela = tk.Tk()
        app = Aplicacao(relatorio_janela)  
        relatorio_janela.mainloop()               

def menu_funcionario():
    def informações_usuario():

        class Aplicacao:
            

            def __init__( data_frame_listas, relatorio_janela):

                
                
                data_frame_listas.relatorio_janela = relatorio_janela
                data_frame_listas.relatorio_janela.title("informações do usuario")
                excel_Voo = pd.read_excel('excelPuckDois.xlsx')

                data_frame_listas.df = pd.DataFrame(excel_Voo)

                # Colunas que você deseja exibir ao selecionar um item no ComboBox
                data_frame_listas.colunas_exibir = ['nome','cpf', 'numero da passagem','assento do voo','valor sem desconto','valor com desconto','Destino do voo','Origem do Voo']
                fonte = ("Bodoni FLF", 16, "bold")
                
                # Crie um ComboBox
                data_frame_listas.combo = ttk.Combobox(relatorio_janela, values=data_frame_listas.df['nome'].tolist(), state='readonly', font=fonte)
                data_frame_listas.combo.set('Selecione o numero do usuario')
                data_frame_listas.combo.grid(row=2, column=1, padx=20, pady=10, sticky='ew', columnspan=3)
                
                #Crie os label

                
                label_valor = tk.Label(relatorio_janela, text='numero da passagem', font=fonte)
                label_valor.grid(row=3, column=0, padx=20, pady=10, sticky='w')
 
                label_numero_passagem = tk.Label(relatorio_janela, text='nome', font=fonte)
                label_numero_passagem .grid(row=2, column=0, padx=20, pady=10, sticky='w')
                               
                label_escolha_origem = tk.Label(relatorio_janela, text='cpf:', font=fonte)
                label_escolha_origem.grid(row=4, column=0, padx=20, pady=10, sticky='w')

                label_numero_passagem = tk.Label(relatorio_janela, text='assento do voo: ', font=fonte)
                label_numero_passagem .grid(row=5, column=0, padx=20, pady=10, sticky='w')

                label_numero_passagem = tk.Label(relatorio_janela, text='valor da passagem sem desconto: ', font=fonte)
                label_numero_passagem .grid(row=6, column=0, padx=20, pady=10, sticky='w')

                label_numero_passagem = tk.Label(relatorio_janela, text='valor da passagem com desconto', font=fonte)
                label_numero_passagem .grid(row=7   , column=0, padx=20, pady=10, sticky='w')

                label_numero_passagem = tk.Label(relatorio_janela, text='Origem do Voo', font=fonte)
                label_numero_passagem .grid(row=8, column=0, padx=20, pady=10, sticky='w')

                label_numero_passagem = tk.Label(relatorio_janela, text='Destino do voo', font=fonte)
                label_numero_passagem .grid(row=9, column=0, padx=20, pady=10, sticky='w')

                data_frame_listas.combo.bind('<<ComboboxSelected>>', data_frame_listas.mostrar_dados)

                data_frame_listas.resultado_label = tk.Label(relatorio_janela, text='')
                data_frame_listas.resultado_label.grid(row=1, column=0, padx=10, pady=10)

            def mostrar_dados(data_frame_listas, event):
            
                
                
                # Obtém o número do voo selecionado no ComboBox
                numero_voo_selecionado = data_frame_listas.combo.get()
                

                # Filtra os dados com base no número do voo selecionado
                dados_selecionados = data_frame_listas.df.loc[data_frame_listas.df['nome'] == numero_voo_selecionado, data_frame_listas.colunas_exibir]


                # Verifica se a seleção não está vazia
                if not dados_selecionados.empty:
                    fonte = ("Bodoni FLF", 16, "bold")
                    # Obtém os dados da primeira linha
                    dados_selecionados = dados_selecionados.iloc[0]
                    
                    #limpar
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=3 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=4 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=5 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=6 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)     
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=7 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=8 , column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                label_valor.grid(row=9, column=1, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)            
                         
                    
                    # Exibe os dados na tela
                label_origem_voo = tk.Label(relatorio_janela, text=dados_selecionados['cpf'], font=fonte)
                label_origem_voo.grid(row=4, column=1, padx=20, pady=10, sticky='w')

                label_destino_voo = tk.Label(relatorio_janela, text=dados_selecionados['numero da passagem'], font=fonte)
                label_destino_voo.grid(row=3, column=1, padx=20, pady=10, sticky='w')
                    


                label_origem_voo = tk.Label(relatorio_janela, text=dados_selecionados['assento do voo'], font=fonte)
                label_origem_voo.grid(row=5, column=1, padx=20, pady=10, sticky='w')

                label_destino_voo = tk.Label(relatorio_janela, text=dados_selecionados['valor sem desconto'], font=fonte)
                label_destino_voo.grid(row=6, column=1, padx=20, pady=10, sticky='w')
                    
                label_destino_voo = tk.Label(relatorio_janela, text=dados_selecionados['valor com desconto'], font=fonte)
                label_destino_voo.grid(row=7, column=1, padx=20, pady=10, sticky='w')

                label_origem_voo = tk.Label(relatorio_janela, text=dados_selecionados['Origem do Voo'], font=fonte)
                label_origem_voo.grid(row=8, column=1, padx=20, pady=10, sticky='w')

                label_destino_voo = tk.Label(relatorio_janela, text=dados_selecionados['Destino do voo'], font=fonte)
                label_destino_voo.grid(row=9, column=1, padx=20, pady=10, sticky='w')


        if __name__ == "__main__":
            relatorio_janela = tk.Tk()
            app = Aplicacao(relatorio_janela)  
            relatorio_janela.mainloop()
    def assentos_disponiveis():

        class Aplicacao:
            

            def __init__( data_frame_listas, relatorio_janela):

                
                
                data_frame_listas.relatorio_janela = relatorio_janela
                data_frame_listas.relatorio_janela.title("informações dos assentos")
                excel_Voo = pd.read_excel('excelPuck.xlsx')

                data_frame_listas.df = pd.DataFrame(excel_Voo)

                # Colunas que você deseja exibir ao selecionar um item no ComboBox
                data_frame_listas.colunas_exibir = ['quantidade de assentos numerados','Numero do voo','Origem do Voo','Destino do voo']
                fonte = ("Bodoni FLF", 16, "bold")
                
                # Crie um ComboBox
                data_frame_listas.combo = ttk.Combobox(relatorio_janela, values=data_frame_listas.df['Origem do Voo'].tolist(), state='readonly', font=fonte)
                data_frame_listas.combo.set('Selecione o numero do usuario')
                data_frame_listas.combo.grid(row=2, column=1, padx=20, pady=10, sticky='ew', columnspan=3)
                
                #Crie os label

                
                label_valor = tk.Label(relatorio_janela, text='Origem do Voo', font=fonte)
                label_valor.grid(row=2, column=0, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text='Destino do voo', font=fonte)
                label_valor.grid(row=3, column=0, padx=20, pady=10, sticky='w')

                label_valor = tk.Label(relatorio_janela, text='numero do voo', font=fonte)
                label_valor.grid(row=4, column=0, padx=20, pady=10, sticky='w')
 
                label_numero_passagem = tk.Label(relatorio_janela, text='total de assentos disponiveis:', font=fonte)
                label_numero_passagem .grid(row=5, column=0, padx=20, pady=10, sticky='w')
                               
                label_escolha_origem = tk.Label(relatorio_janela, text='assentos disponiveis:', font=fonte)
                label_escolha_origem.grid(row=6, column=0, padx=20, pady=10, sticky='w')



                data_frame_listas.combo.bind('<<ComboboxSelected>>', data_frame_listas.mostrar_dados)

                data_frame_listas.resultado_label = tk.Label(relatorio_janela, text='')
                data_frame_listas.resultado_label.grid(row=1, column=0, padx=10, pady=10)

            def mostrar_dados(data_frame_listas, event):
            
                
                
                # Obtém o número do voo selecionado no ComboBox
                numero_voo_selecionado = data_frame_listas.combo.get()
                

                # Filtra os dados com base no número do voo selecionado
                dados_selecionados = data_frame_listas.df.loc[data_frame_listas.df['Origem do Voo'] == numero_voo_selecionado, data_frame_listas.colunas_exibir]
                


                # Verifica se a seleção não está vazia
                if not dados_selecionados.empty:
                    fonte = ("Bodoni FLF", 16, "bold")
                    # Obtém os dados da primeira linha
                    dados_selecionados = dados_selecionados.iloc[0]
                    
                    #limpar
                    label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                    label_valor.grid(row=3, column=1, padx=20, pady=10, sticky='w')
                    label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                    label_valor.grid(row=4, column=1, padx=20, pady=10, sticky='w')
                    label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                    label_valor.grid(row=5, column=1, padx=20, pady=10, sticky='w')

                    label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                    label_valor.grid(row=6, column=1, padx=20, pady=10, sticky='w')                                
                         
                    
                        # Exibe os dados na tela
                    selecionar_assento = ttk.Combobox(relatorio_janela, values=dados_selecionados['quantidade de assentos numerados'], font=fonte,state='readonly')
                    selecionar_assento.grid(row=6, column=1, padx=20, pady=10, sticky='ew', columnspan=3)     
                    
                    
                    lista_assentos = [int(x) for x in dados_selecionados['quantidade de assentos numerados'].strip('[]').split(',')]
                    lista_assentos=len(lista_assentos)
                    
                    label_destino_voo = tk.Label(relatorio_janela, text=dados_selecionados['Numero do voo'], font=fonte)
                    label_destino_voo.grid(row=4, column=1, padx=20, pady=10, sticky='w')
                    label_destino_voo = tk.Label(relatorio_janela, text=dados_selecionados['Destino do voo'], font=fonte)
                    label_destino_voo.grid(row=3, column=1, padx=20, pady=10, sticky='w')

                    label_destino_voo = tk.Label(relatorio_janela, text=lista_assentos, font=fonte)
                    label_destino_voo.grid(row=5, column=1, padx=20, pady=10, sticky='w')
                
                        


        if __name__ == "__main__":
            relatorio_janela = tk.Tk()
            app = Aplicacao(relatorio_janela)  
            relatorio_janela.mainloop()
    def reservas_que_foram_realizadas():

        class Aplicacao:
            

            def __init__( data_frame_listas, relatorio_janela):

                
                
                data_frame_listas.relatorio_janela = relatorio_janela
                data_frame_listas.relatorio_janela.title("total de passagens")
                excel_Voo = pd.read_excel('excelPuckDois.xlsx')

                data_frame_listas.df = pd.DataFrame(excel_Voo)

                # Colunas que você deseja exibir ao selecionar um item no ComboBox
                fonte = ("Bodoni FLF", 16, "bold")
                
                # Crie um ComboBox
     
                #Crie os label
                desconto_25=0
                desconto_15=0
                desconto_5=0
                descontos_0=0

                for a in data_frame_listas.df['desconto']:
                    if a == 25:                   
                        desconto_25+=1
                    elif a== 15:
                        desconto_15+=1
                    elif a==5:
                        desconto_5+=1
                    else:
                        descontos_0+=1

                
                label_valor = tk.Label(relatorio_janela, text='total de passagens:', font=fonte)
                label_valor.grid(row=0, column=0, padx=20, pady=10, sticky='w')                
                label_valor = tk.Label(relatorio_janela, text=desconto_25+desconto_15+desconto_5+descontos_0, font=fonte)
                label_valor.grid(row=0, column=1, padx=20, pady=10, sticky='w')
 
                label_numero_passagem = tk.Label(relatorio_janela, text='quantidade de passagens com 25%:', font=fonte)
                label_numero_passagem .grid(row=1, column=0, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text=desconto_25, font=fonte)
                label_valor.grid(row=1, column=1, padx=20, pady=10, sticky='w')
                               
                label_escolha_origem = tk.Label(relatorio_janela, text='quantidade de passagens com 15%:', font=fonte)
                label_escolha_origem.grid(row=2, column=0, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text=desconto_15, font=fonte)
                label_valor.grid(row=2, column=1, padx=20, pady=10, sticky='w')

                label_numero_passagem = tk.Label(relatorio_janela, text='quantidade de passagens com 5%: ', font=fonte)
                label_numero_passagem .grid(row=3, column=0, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text=desconto_5, font=fonte)
                label_valor.grid(row=3, column=1, padx=20, pady=10, sticky='w')

                label_numero_passagem = tk.Label(relatorio_janela, text='quantidade de passagens com 0%:: ', font=fonte)
                label_numero_passagem .grid(row=4, column=0, padx=20, pady=10, sticky='w')
                label_valor = tk.Label(relatorio_janela, text=descontos_0, font=fonte)
                label_valor.grid(row=4, column=1, padx=20, pady=10, sticky='w')

        if __name__ == "__main__":
                relatorio_janela = tk.Tk()
                app = Aplicacao(relatorio_janela)  
                relatorio_janela.mainloop()         
    def valor_arrecadado():
        class Aplicacao:
            

            def __init__(data_frame_listas, relatorio_janela):
            
            
                data_frame_listas.relatorio_janela = relatorio_janela
                data_frame_listas.relatorio_janela.title("valor arrecadado")
                excel_Voo = pd.read_excel('excelPuckDois.xlsx')

                data_frame_listas.df = pd.DataFrame(excel_Voo)

                # Colunas que você deseja exibir ao selecionar um item no ComboBox
                data_frame_listas.colunas_exibir = ['Numero do voo','valor com desconto']
                fonte = ("Bodoni FLF", 16, "bold")
                
                # Crie um ComboBox
                data_frame_listas.combo = ttk.Combobox(relatorio_janela, values=data_frame_listas.df['Numero do voo'].tolist(), state='readonly', font=fonte)
                data_frame_listas.combo.set('Selecione o numero do voo')
                data_frame_listas.combo.grid(row=2, column=1, padx=20, pady=10, sticky='ew', columnspan=3)
                
                #Crie os label
                
                valor_total=0
                for a in data_frame_listas.df['valor com desconto']:
                    valor_total+=a

                
                
                label_valor = tk.Label(relatorio_janela, text='codigo do voo:', font=fonte)
                label_valor.grid(row=2, column=0, padx=20, pady=10, sticky='w')
                
                label_escolha_origem = tk.Label(relatorio_janela, text='valor total desse voo:', font=fonte)
                label_escolha_origem.grid(row=3, column=0, padx=20, pady=10, sticky='w')


                label_escolha_destino = tk.Label(relatorio_janela, text='valor total todos os voos:', font=fonte)
                label_escolha_destino.grid(row=4, column=0, padx=20, pady=10, sticky='w')
                label_escolha_destino = tk.Label(relatorio_janela, text=valor_total, font=fonte)
                label_escolha_destino.grid(row=4, column=1, padx=20, pady=10, sticky='w')

                # Adicione um evento para ser chamado quando uma opção do ComboBox é selecionada
                data_frame_listas.combo.bind('<<ComboboxSelected>>', data_frame_listas.mostrar_dados)

                # Rótulo para exibir os dados da linha selecionada
                data_frame_listas.resultado_label = tk.Label(relatorio_janela, text='')
                data_frame_listas.resultado_label.grid(row=1, column=0, padx=10, pady=10)

            def mostrar_dados(data_frame_listas, event):
            
                
                
                # Obtém o número do voo selecionado no ComboBox
                numero_voo_selecionado = int(data_frame_listas.combo.get())
            
                # Filtra os dados com base no número do voo selecionado
                dados_selecionados = data_frame_listas.df.loc[data_frame_listas.df['Numero do voo'] == numero_voo_selecionado, data_frame_listas.colunas_exibir]


                # Verifica se a seleção não está vazia
                if not dados_selecionados.empty:
                    fonte = ("Bodoni FLF", 16, "bold")
                    # Obtém os dados da primeira linha
                    dados_selecionados = dados_selecionados.iloc[0]
                    
                    #limpar
                    label_valor = tk.Label(relatorio_janela, text='                                  ', font=fonte)
                    label_valor.grid(row=3 , column=1, padx=20, pady=10, sticky='w')
          
                    resultados = data_frame_listas.df[data_frame_listas.df['Numero do voo'] == dados_selecionados['Numero do voo']]
                    resultados=resultados['valor com desconto']
                    
                    valor_selecionado=0
                    for a in resultados:
                        valor_selecionado+=a
                    
                    
                    # Exibe os dados na tela
                    label_origem_voo = tk.Label(relatorio_janela, text=valor_selecionado, font=fonte)
                    label_origem_voo.grid(row=3, column=1, padx=20, pady=10, sticky='w')

        if __name__ == "__main__":
            relatorio_janela = tk.Tk()
            app = Aplicacao(relatorio_janela)  
            relatorio_janela.mainloop()     
            
    class Aplicacao:
        

        def __init__(data_frame_listas, relatorio_janela):
            
            
            data_frame_listas.relatorio_janela = relatorio_janela
            data_frame_listas.relatorio_janela.title("menu do funcionario")
       
            botao_enviar = tk.Button(relatorio_janela, text='informações do usuario', command=informações_usuario, font=("Bodoni FLF", 20, "bold"))    
            botao_enviar.grid(row=1, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')
            
            botao_assentos_disponiveis = tk.Button(relatorio_janela, text='assentos disponiveis', command=assentos_disponiveis, font=("Bodoni FLF", 20, "bold"))    
            botao_assentos_disponiveis.grid(row=2, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')
            
            botao_reservas_que_foram_realizadas = tk.Button(relatorio_janela, text='reservas que foram realizadas', command=reservas_que_foram_realizadas, font=("Bodoni FLF", 20, "bold"))    
            botao_reservas_que_foram_realizadas.grid(row=3, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')
            
            botao_valor_arrecadado = tk.Button(relatorio_janela, text='valor arrecadado', command=valor_arrecadado, font=("Bodoni FLF", 20, "bold"))    
            botao_valor_arrecadado.grid(row=4, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')
    if __name__ == "__main__":
        relatorio_janela = tk.Tk()
        app = Aplicacao(relatorio_janela)  
        relatorio_janela.mainloop()     
janela = tk.Tk()
largura_janela = 470
altura_janela = 570
janela.geometry(f"{largura_janela}x{altura_janela}")
janela.title("Puck")


botao_cadastrar_voo = tk.Button(janela, text="Area Administração", command=cadastrar_vooo, padx=50, pady=20, font=("Bodoni FLF", 20, "bold"))
botao_vender_passagem = tk.Button(janela, text="Vender passagem", command=vender_passagem, padx=50, pady=20, font=("Bodoni FLF", 20, "bold"))

botao_teste = tk.Button(janela, text="cancelar passagem", command=cancelar_passagem, padx=80, pady=20, font=("Bodoni FLF", 20, "bold"))
botao_menu_funcionario = tk.Button(janela, text="menu do funcionario", command=menu_funcionario, padx=80, pady=20, font=("Bodoni FLF", 20, "bold"))



fonte_titulo = ("Bodoni FLF", 40, "bold")
label_Puck = tk.Label(janela, text="Puck AIR", font=fonte_titulo, fg="purple")
label_Puck.pack(padx=20, pady=20)

botao_cadastrar_voo.pack(pady=25)
botao_vender_passagem.pack()
botao_teste.pack()
botao_menu_funcionario.pack()

janela.mainloop()
