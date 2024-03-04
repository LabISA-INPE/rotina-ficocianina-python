import pandas as pd


#Ler arquivo CSV chamado "medidas_promissao_ficocianina.txt" e armazena os dados em um DataFrame chamado "df".
df = pd.read_csv("C:/Users/neyra/Desktop/INPE/Raianny/rotina-ficocianina-python/input/medidas_promissao_ficocianina.txt", delimiter="\t", decimal=",", index_col=0)

#Calcula a média ao longo do eixo das colunas (axis=1) para as colunas que contêm a string 'Ar_vs_Buffer'. 
#O resultado é armazenado na variável branco_buffer.
branco_buffer = df.loc[:,['Ar_vs_Buffer' in i for i in df.columns]].mean(axis=1)

df = df.subtract(branco_buffer, axis = 0)

#Substitui todos os valores negativos no DataFrame df por 0.
df[df < 0] = 0

#Seleciona as colunas que contêm a string 'b_vs' e 'a_vs', extrai os nomes dessas colunas como um array, armazenando em 'pontos_b' e 'pontos_a'.
pontos_b = df.loc[:,['b_vs' in i for i in df.columns]].columns.values
pontos_a = df.loc[:,['a_vs' in i for i in df.columns]].columns.values

#Divide o primeiro elemento da lista 'pontos_a' usando o caractere (_) como separador e armazena o resultado em teste.
teste = pontos_a[0].split(sep="_")

#Volume de água filtrada para cada amostra
vol = [350,350,350,300,350,350]

#Inicializa listas vazias para armazenar resultados parciais.
pc_a = []
pc_b = []
variacao = []

#Cria um DataFrame chamado data com índices pré-definidos.
data = pd.DataFrame(index=["PC_A","PC_B","PC_MEAN","Variação"])

#Inicia um loop que itera sobre as listas 'pontos_a', 'pontos_b', e 'vol' ao mesmo tempo, usando a função zip.
for a,b,c in zip(pontos_a,pontos_b,vol):
    #Para cada iteração do loop, seleciona as colunas 'sample_data_a' e 'sample_data_b', calcula as diferenças entre os valores em 615, 652, e 750.
    sample_data_a = df[a]
    sample_data_b = df[b]
    wv_615_cor_a = sample_data_a.loc[615] - sample_data_a.loc[750]
    wv_652_cor_a = sample_data_a.loc[652] - sample_data_a.loc[750]
    wv_615_cor_b = sample_data_b.loc[615] - sample_data_b.loc[750]
    wv_652_cor_b = sample_data_b.loc[652] - sample_data_b.loc[750]
    
    #Calcula as concentrações de ficocianina para as amostras A e B.
    fico_a = (((wv_615_cor_a - (0.474 * wv_652_cor_a))/5.34) / c) * 1000000
    fico_b = (((wv_615_cor_b - (0.474 * wv_652_cor_b))/5.34) / c) * 1000000
    
    #Adiciona os resultados nas listas 'pc_a' e 'pc_b'.
    pc_a.append(fico_a)
    pc_b.append(fico_b)
    
    #Calcula a média das concentrações de ficocianina para A e B.
    pc_med = (fico_a + fico_b)/2
    
    #Calcula a variação percentual entre A e B, evitando a divisão por zero.
    var = abs((fico_a - fico_b) / fico_b) if fico_b != 0 else 0
    
    #Extrai informações da string 'a' e cria uma nova string 'string'.
    string = a.split(sep="_")
    string = string[1] + "_" + string[2][0:-1]
    
    #Adiciona os resultados ao DataFrame 'data'.
    data[string] = [fico_a,fico_b,pc_med,var]
    
    #Adiciona a variação na lista 'variacao'.
    variacao.append(var)
    print("Ficocianina ponto " + a + " :",fico_a, " , ", fico_b,"(", var,")", "\n")
  
#Calcula a média das concentrações de ficocianina para cada ponto entre 'pc_a' e 'pc_b'.
mean_pc = [(a+b)/2 for a,b in zip(pc_a,pc_b)]
print("Média",mean_pc,"\n","\n")
print ("Variação",variacao)

#Escreve os resultados para um arquivo CSV. 
#Altere o caminho e o nome do arquivo conforme necessário.
data.to_csv("C:/Users/neyra/Desktop/INPE/Raianny/rotina-ficocianina-python/outputs/ficocianina_promissao_ago_23_pt3.csv")