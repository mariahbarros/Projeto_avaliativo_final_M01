# %% [markdown]
# ANÁLISE EXPLORATÓRIA DE DADOS - PROJETO 'HR - FREESQL'
# _______________________________________________________________________________________________________________________
# 
# O objetivo dessa AED é verificar a relação entre salários, cargos/departamentos e localização geográfica dos funcionários de uma empresa. Os dados estão distribuídos em 7 planilhas obtidas no site Freesql. Inicialmente, extraímos os dados. Eles foram divididos em 2 planilhas: uma relacionada a funcionários, cargos e salários (Query1), e outra, a funcionarios e localização onde estão alocados (Query2). Com este projeto, pretendemos obter conclusões acerca de como os salários são distribuídos entre os funcionários em razão dos cargos e departamentos, e localidade onde prestam os serviços.
# 

# %% [markdown]
# CARREGAMENTO DA BASE DE DADOS:
# _______________________________________________________________________________________________________________________

# %%
# importando as bibliotecas necessárias para a análise e visualização de dados
import pandas as pd
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import seaborn as sns

# importando a base de dados diretamente do GitHub - repositório "Projeto_avaliativo_final_M01"
URL_query1 = 'https://github.com/mariahbarros/Projeto_avaliativo_final_M01/blob/main/Dados_csv/Query1.csv?raw=true'
URL_query2 = 'https://github.com/mariahbarros/Projeto_avaliativo_final_M01/blob/main/Dados_csv/Query2.csv?raw=true'

# transformando as bases de dados em dataframes
df_query1 = pd.read_csv(URL_query1, sep=',', encoding='utf-8')
df_query2 = pd.read_csv(URL_query2, sep=',', encoding='utf-8')

# formatação para exibir os números em porcentagem com duas casas decimais
pd.set_option('display.float_format', '{:,.2f}%'.format)

# formatação para exibir os dataframes de forma mais legível
pd.set_option('display.width', None)          
pd.set_option('display.max_columns', None)    
pd.set_option('display.expand_frame_repr', False)  

# formatação geral dos gráficos
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)


# %% [markdown]
# QUERY1 : ANÁLISE PRIMÁRIA DOS DADOS
# _______________________________________________________________________________________________________________________

# %%
# 1) verificando as informações gerais sobre as bases de dados da Query1

# verificando o número de linhas e colunas do df_query1
print('=========== DIMENSÕES DA BASE DE DADOS ==========')
print(f'\nBase carregada com {df_query1.shape[0]} linhas e {len(df_query1.columns)} colunas.')                    

# verificando as primeiras e as últimas 5 linhas do dataframe
print('\n========== ANALISANDO AS PRIMEIRAS E ÚLTIMAS LINHAS DOS DADOS ==========')
print(f'\nInformações sobre as primeiras 5 linhas: \n{df_query1.head(5).to_string()}')                     
print(f'\nInformações sobre as últimas 5 linhas: \n{df_query1.tail(5).to_string()}')                       

# verificando as informações gerais sobre o dataframe
print('\n========== INFORMAÇÕES GERAIS ==========')
print(f'\nInformações gerais sobre os dados:')                                                      
print(df_query1.info())

# verificando a distribuição de valores únicos por coluna
print('\n========== INFORMAÇÕES SOBRE COLUNAS ==========')
print(f'\nVerificando a distribuição de valores únicos por coluna: \n{df_query1.nunique().to_string()}')   
 
# verificando a existência de valores duplicados no dataframe
print('\n========== INFORMAÇÕES SOBRE VALORES DUPLICADOS ==========')
print(f'\nVerificando duplicatas: {df_query1.duplicated().sum()}')                                         
 

# %% [markdown]
# QUERY1: TRATAMENTO DE DADOS
# ________________________________________________________________________________________________________________________________________________

# %%
# 2) transformando a coluna HIRE_DATE em formato datetime

# ajustes antes da conversão
df_query1['HIRE_DATE'] = df_query1['HIRE_DATE'].astype(str).str.strip()

# conversão
df_query1['HIRE_DATE'] = pd.to_datetime(df_query1['HIRE_DATE'], format='ISO8601', errors='coerce')

# verificando o período analisado no dataframe
print("\n=====Verificando a transfomação:=====\n")
print(df_query1['HIRE_DATE'].info())

# %%
# 3) criando coluna para calcular o tempo de contratação em meses

# NOTA: O tempo de contratação será sempre calculado em relação à data atual

def calcular_tempo_meses(data_admissao):
    hoje = pd.Timestamp.now(tz=data_admissao.tzinfo)
    diferenca = relativedelta(hoje, data_admissao)
    return diferenca.years * 12 + diferenca.months

df_query1['TEMPO_CONTRATACAO_MESES'] = df_query1['HIRE_DATE'].apply(calcular_tempo_meses)


# nome da coluna criada já traduzida para o português, pois todas as demais serão a seguir renomeadas

print("\n=====Verificando a criação da coluna:=====\n")
print(df_query1[['HIRE_DATE', 'TEMPO_CONTRATACAO_MESES']].head())

# realocando a coluna TEMPO_CONTRATACAO_MESES para a posição de índice 2 do dataframe 
# removendo a coluna do lugar atual (última posição, por convenção) e armazenando em uma variável temporária
coluna_tempo = df_query1.pop('TEMPO_CONTRATACAO_MESES')

# reinserindo na posição de índice 2
df_query1.insert(2, 'TEMPO_CONTRATACAO_MESES', coluna_tempo)

print(df_query1.columns)

# %%
# 4) tratando as nulidades

# confirmando a quantidade de valores nulos
df_query1.info()

# definindo valores para substituir nulos
resolucao_nulidades = {
    'DEPARTMENT_NAME': 'Sales',
    'COMMISSION_PCT': 0.0  
}

# efetivando as substituições
df_query1.fillna(value=resolucao_nulidades, inplace=True)

print(print("\n=====Verificação do tratamento das nulidades:=====\n"))
print(df_query1.isna().sum())

# %%
# 5) renomeando as colunas do dataframe df_query1

# dicionário de tradução
renomear_colunas = {
    'EMPLOYEE_ID': 'EMPREGADO_ID',
    'HIRE_DATE': 'DATA_ADMISSAO',
    'JOB_TITLE': 'CARGO',
    'DEPARTMENT_NAME': 'DEPARTAMENTO',
    'SALARY': 'SALARIO',
    'COMMISSION_PCT': 'COMISSAO_PCT',
    'MIN_SALARY': 'MIN_SALARIO',
    'MAX_SALARY': 'MAX_SALARIO',
    
}

df_query1 = df_query1.rename(columns=renomear_colunas)

# verificando a renomeação
print("\n=====NOVOS VALORES COLUNAS QUERY01:=====\n")
print(df_query1.columns)

# %%
# 6) visualizando os valores em CARGO para renomeação

print("\n=====Valores em CARGO:=====\n")
print(df_query1['CARGO'].unique())

# renomeando os valores em CARGO
renomear_cargos = {
    'President': 'presidente',
    'Programmer': 'programador',
    'Finance Manager': 'gerente_financeiro',
    'Accountant': 'contador',
    'Purchasing Clerk': 'assistente_compras',
    'Stock Manager': 'gerente_estoque',
    'Stock Clerk': 'assistente_estoque',
    'Sales Manager': 'gerente_vendas',
    'Sales Representative': 'representante_vendas',
    'Shipping Clerk': 'assistente_expedicao',
    'Marketing Representative': 'representante_MKT',
    'Human Resources Representative': 'representante_RH',
    'Public Relations Representative': 'representante_RP',
    'Accounting Manager': 'gerente_contabilidade',
    'Public Accountant': 'contador_publico'
}

df_query1['CARGO'] = df_query1['CARGO'].replace(renomear_cargos)

# verificando a renomeação
print("\n=====NOVOS VALORES COLUNA 'CARGO': =====\n")
print(df_query1['CARGO'].unique())

# %%
# 7) visualizando os valores em DEPARTAMENTO para renomeação

print("\n=====Valores em DEPARTAMENTO:=====\n")
print(df_query1['DEPARTAMENTO'].unique())

# renomeando os valores em DEPARTAMENTO
renomear_departamentos = {
    'Executive': 'diretoria',
    'IT': 'TI',
    'Finance': 'financeiro',
    'Purchasing': 'compras',
    'Shipping': 'expedicao',
    'Sales': 'vendas',
    'Marketing': 'MKT',
    'Human Resources': 'RH',
    'Public Relations': 'RP',
    'Accounting': 'contabilidade',
    
}

df_query1['DEPARTAMENTO'] = df_query1['DEPARTAMENTO'].replace(renomear_departamentos)

# verificando a renomeação
print("\n=====NOVOS VALORES COLUNA 'DEPARTAMENTO': =====\n")
print(df_query1['DEPARTAMENTO'].unique())

# %%
# 8) estatística descritiva das colunas TEMPO_CONTRATACAO_MESES', SALARIO', 'COMISSAO_PCT', 'MIN_SALARIO' e 'MAX_SALARIO' no dataframe df_query1

colunas_estatisticas = [
    'TEMPO_CONTRATACAO_MESES',
    'SALARIO',
    'COMISSAO_PCT',
    'MIN_SALARIO',
    'MAX_SALARIO'
]

# exibindo as estatísticas descritivas
print("\n===== Estatísticas descritivas das variáveis numéricas: =====\n")
print(df_query1[colunas_estatisticas].describe().map('{:.2f}'.format))

print("\n===== Coeficientes de variação: =====\n")
for col in colunas_estatisticas:
    cv = df_query1[col].std() / df_query1[col].mean() * 100
    print(f"{col}: {cv:.2f}%")


# %%
# 9) estatística descritiva para os salários por departamento, considerando apenas os departamentos com mais de 1 funcionário

# verificando quantos funcionários existem por departamento
contagem_departamento = df_query1['DEPARTAMENTO'].value_counts()

# filtrando só os departamentos com mais de 1 funcionário
departamentos_validos = contagem_departamento[contagem_departamento > 1].index

df_filtrado = df_query1[df_query1['DEPARTAMENTO'].isin(departamentos_validos)]

tabela_describe = df_filtrado.groupby('DEPARTAMENTO')['SALARIO'].describe().map('{:.2f}'.format)
#invertendo a tabela para melhor visualização
tabela_describe_transposta = tabela_describe.T    

print("\n===== Estatísticas descritivas de salários por departamento: =====\n")
print(tabela_describe_transposta)


# %% [markdown]
# QUERY2 : ANÁLISE PRIMÁRIA DOS DADOS
# ________________________________________________________________________________________________________________________________________________

# %%
# 10) verificando as informações gerais sobre as bases de dados da Query2

# verificando o número de linhas e colunas do df_query2
print('========== DIMENSÕES DA BASE DE DADOS ==========')
print(f'\nBase carregada com {df_query2.shape[0]} linhas e {len(df_query2.columns)} colunas.')                    

# verificando as primeiras e as últimas 5 linhas do dataframe
print('\n========== ANALISANDO AS PRIMEIRAS E ÚLTIMAS LINHAS DOS DADOS ==========')
print(f'\nInformações sobre as primeiras 5 linhas: \n{df_query2.head(5).to_string()}')                     
print(f'\nInformações sobre as últimas 5 linhas: \n{df_query2.tail(5).to_string()}')                       

# verificando as informações gerais sobre o dataframe
print('\n========== INFORMAÇÕES GERAIS ==========')
print(f'\nInformações gerais sobre os dados:')                                                      
print(df_query2.info())

# verificando a distribuição de valores únicos por coluna
print('\n========== INFORMAÇÕES SOBRE COLUNAS ==========')
print(f'\nVerificando a distribuição de valores únicos por coluna: \n{df_query2.nunique().to_string()}')   
 
# verificando a existência de valores duplicados no dataframe
print('\n========== INFORMAÇÕES SOBRE VALORES DUPLICADOS ==========')
print(f'\nVerificando duplicatas: {df_query2.duplicated().sum()}')

# %% [markdown]
# QUERY2: TRATAMENTO DE DADOS
# ________________________________________________________________________________________________________________________________________________

# %%
# 11) tratando as nulidades

# confirmando a quantidade de valores nulos
print(df_query2.info())

# definindo valores para substituir nulos
resolucao_nulidades = {
    'STREET_ADDRESS': 'dado_ausente',
    'POSTAL_CODE': 'dado_ausente',
    'CITY': 'dado_ausente',
    'STATE_PROVINCE': 'dado_ausente',
    'COUNTRY_NAME': 'dado_ausente',
    'REGION_NAME': 'dado_ausente',
    'COMMISSION_PCT': 0.0  
}

# efetivando as substituições
df_query2.fillna(value=resolucao_nulidades, inplace=True)

print("\n==================================================\n")

print("\nVerificação:\n")
print(df_query2.isna().sum())

# %%
# 12) renomeando as colunas do dataframe df_query2

# dicionário de tradução:
renomear_colunas = {
    'EMPLOYEE_ID': 'EMPREGADO_ID',
    'SALARY': 'SALARIO',
    'COMMISSION_PCT': 'COMISSAO_PCT',
    'STREET_ADDRESS': 'ENDERECO',
    'POSTAL_CODE': 'CEP',
    'CITY': 'CIDADE',
    'STATE_PROVINCE': 'ESTADO',
    'COUNTRY_NAME': 'PAIS',
    'REGION_NAME': 'REGIAO',
        
}

df_query2 = df_query2.rename(columns=renomear_colunas)

# verificando a renomeação
print("\n=====NOVOS VALORES  COLUNAS QUERY02:=====\n")
print(df_query2.columns)

# %% [markdown]
# ANÁLISE EXPLORATÓRIA DE DADOS - QUERY1 E QUERY2:
# ________________________________________________________________________________________________________________________________________________

# %%
# 13) verificando os dados das colunas 'CARGO' e 'DEPARTAMENTO' (Query1), e 'ENDERECO', 'CEP', 'CIDADE', 'ESTADO', 'PAIS' e 'REGIAO' (Query2)

# Query1
# TABELA 1: Verificando os cargos e departamentos
print("\n===== TABELA 1: Cargos x departamento: =====\n")
print(df_query1[['CARGO','DEPARTAMENTO']].value_counts())

print("\n====================================================\n")

# Query2
# TABELA 2: Verificando localizações
colunas_analise = [
    'ENDERECO', 
    'CEP', 
    'CIDADE', 
    'ESTADO', 
    'PAIS', 
    'REGIAO'
]
 
print("\n===== TABELA 2: Relacionando localizações: =====\n")
print(df_query2[colunas_analise].value_counts())



# %%
# 14) unindo os dataframes df_query1 e df_query2, e verificando a quantidade de funcionários por cargo, departamento e localização

df_unido = df_query1.merge(
    df_query2[['EMPREGADO_ID', 'CIDADE', 'ESTADO', 'PAIS', 'REGIAO']], on='EMPREGADO_ID', how='left')


tabela_cargo_dept_cidade = df_unido.groupby(['CARGO', 'DEPARTAMENTO', 'CIDADE', 'ESTADO', 'PAIS', 'REGIAO']).size().reset_index(name='QTD_FUNCIONARIOS')
tabela_cargo_dept_cidade = tabela_cargo_dept_cidade.sort_values(['CARGO', 'QTD_FUNCIONARIOS'], ascending=[True, False])

print("\n===== TABELA 3: Cargos, departamentos e localizações: =====\n")
print(tabela_cargo_dept_cidade)

# %%
# 15) verificando se os salarios estao dentro da faixa salarial definida para cada cargo, considerando os valores de MIN_SALARIO e MAX_SALARIO

fora_da_faixa = df_query1[
    (df_query1['SALARIO'] < df_query1['MIN_SALARIO']) | 
    (df_query1['SALARIO'] > df_query1['MAX_SALARIO'])
]

print(f'===== Funcionários fora da faixa salarial (MIN_SALARIO / MAX_SALARIO): ===== {len(fora_da_faixa)}\n')
print(fora_da_faixa[['EMPREGADO_ID', 'CARGO', 'SALARIO', 'MIN_SALARIO', 'MAX_SALARIO']])

# %%
# INICIANDO A ANÁLISE EXPLORATÓRIA DE DADOS (AED) COM BASE NOS DATAFRAMES df_query1 e df_query2 - GERAÇÃO DE GRÁFICOS

# GRÁFICO 1: Distribuição de Departamentos por Cidade

# filtrando o df_unido para remover os registros com valor 'dado_ausente' na coluna 'CIDADE' (df_unido_valido)
df_unido_valido = df_unido[df_unido['CIDADE'] != 'dado_ausente']

pivot = pd.crosstab(df_unido_valido['DEPARTAMENTO'], df_unido_valido['CIDADE'])

plt.figure(figsize=(10, 8))
sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu', linewidths=0.5, cbar_kws={'label': 'Qtd. Funcionários'})
plt.title('GRÁFICO 1: Distribuição de Departamentos por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Departamento')
plt.tight_layout()
plt.show()

# %%
# GRÁFICO 2: Distribuição de Cargos por Cidade

#df_unido = df_query1.merge(
#    df_query2[['EMPREGADO_ID', 'CIDADE']], 
#    on='EMPREGADO_ID', 
#    how='left'
#)

df_unido_valido = df_unido[df_unido['CIDADE'] != 'dado_ausente']

ordem_cargos = df_unido_valido['CARGO'].value_counts().index

pivot_ordenado = pd.crosstab(df_unido_valido['CARGO'], df_unido_valido['CIDADE']).reindex(ordem_cargos)

plt.figure(figsize=(10, 10))
sns.heatmap(pivot_ordenado, annot=True, fmt='d', cmap='YlOrRd', linewidths=0.5, cbar_kws={'label': 'Qtd. Funcionários'})
plt.title('GRÁFICO 2: Distribuição de Cargos por Cidade (ordenado por volume)')
plt.xlabel('Cidade')
plt.ylabel('Cargo')
plt.tight_layout()
plt.show()

# %%
# GRÁFICO 3: Salário x Departamento

plt.figure(figsize=(12, 6))
ordem = df_query1.groupby('DEPARTAMENTO')['SALARIO'].median().sort_values(ascending=False).index
sns.boxplot(data=df_query1, x='DEPARTAMENTO', y='SALARIO', order=ordem)
plt.xticks(rotation=45, ha='right')
plt.title('GRÁFICO 3: Distribuição de Salários por Departamento')
plt.tight_layout()
plt.show()

# %%
# GRÁFICO 4: Salário x Departamento x Cargo

g = sns.catplot(
    data=df_query1,
    x='CARGO', y='SALARIO',
    col='DEPARTAMENTO',
    kind='box',
    col_wrap=3,          # 3 gráficos por linha
    sharex=False,        # cada painel tem seus próprios cargos no eixo X
    sharey=True,         # mesma escala de salário pra comparar entre departamentos
    height=3.5, aspect=1.3
)

g.set_xticklabels(rotation=45, ha='right')
g.set_titles('{col_name}')
        
g.fig.suptitle('GRÁFICO 4: Distribuição de Salário por Cargo, dentro de cada Departamento', y=1.02)
plt.tight_layout()

plt.show()

# %%
# GRÁFICO 5: Salário x tempo de contratação (Cargos Selecionados)

# excluindo cargos únicos por departamento
cargos_excluir = ['presidente', 'gerente_financeiro', 'representante_MKT', 'representante_RH', 
                   'representante_RP', 'gerente_contabilidade', 'contador_publico']

df_filtrado = df_query1[~df_query1['CARGO'].isin(cargos_excluir)]


sns.set_style('whitegrid')

g = sns.relplot(
    data=df_filtrado,
    x='TEMPO_CONTRATACAO_MESES', y='SALARIO',
    col='CARGO',
    col_wrap=4,
    kind='scatter',
    height=3, aspect=1.2,
    s=100,
    facet_kws={'sharey': False, 'sharex': False}
)
g.set_titles('{col_name}')

# força o rótulo do eixo X e Y em TODOS os painéis, não só na última linha
for ax in g.axes.flat:
    if ax.has_data():
        ax.set_xlabel('Tempo (meses)')
        ax.set_ylabel('Salário')
    else:
        ax.set_visible(False)

g.fig.suptitle('GRÁFICO 5: Distribuição de Salário por tempo de contratação (cargos selecionados)', y=1.02)
plt.tight_layout()
plt.show()

# %%
# GRÁFICO 6: Comissão x Cargos

df_comissao = df_query1[df_query1['COMISSAO_PCT'].notna()]

plt.figure(figsize=(12, 6))
sns.boxplot(data=df_comissao, x='CARGO', y='COMISSAO_PCT')
plt.xticks(rotation=45, ha='right')
plt.title('GRÁFICO 6: Distribuição de Comissão por Cargos')
plt.tight_layout()
plt.show()

# %%
# GRÁFICO 7: Comissão x Tempo de contratação

df_comissao = df_query1[df_query1['COMISSAO_PCT'] > 0]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_comissao, x='TEMPO_CONTRATACAO_MESES', y='COMISSAO_PCT', s=80, alpha=0.7)
sns.regplot(data=df_comissao, x='TEMPO_CONTRATACAO_MESES', y='COMISSAO_PCT', 
            scatter=False, color='red', line_kws={'linestyle': '--'})
plt.title('GRÁFICO 7: Comissão x Tempo de Contratação')
plt.xlabel('Tempo de Contratação (meses)')
plt.ylabel('Comissão (%)')
plt.tight_layout()
plt.show()

# %%
# TABELA 4: Gerente de Vendas - Informações sobre Tempo de Contratação, Comissão e Salário

tabela_gerentes_vendas = df_query1[df_query1['CARGO'] == 'gerente_vendas'][
    ['EMPREGADO_ID', 'CARGO', 'TEMPO_CONTRATACAO_MESES', 'COMISSAO_PCT', 'SALARIO']
].sort_values('TEMPO_CONTRATACAO_MESES', ascending=False)

print(f'\n===== TABELA 4: Gerente de Vendas - Informações sobre Tempo de Contratação, Comissão e Salário =====\n')
print(tabela_gerentes_vendas)

# %%
# TABELA 5: Representante de Vendas - Informações sobre Tempo de Contratação, Comissão e Salário
tabela_representante_vendas = df_query1[df_query1['CARGO'] == 'representante_vendas'][
    ['EMPREGADO_ID', 'CARGO', 'TEMPO_CONTRATACAO_MESES', 'COMISSAO_PCT', 'SALARIO']
].sort_values('TEMPO_CONTRATACAO_MESES', ascending=False)

print(f'\n===== TABELA 5: Representante de Vendas - Informações sobre Tempo de Contratação, Comissão e Salário =====\n')
print(tabela_representante_vendas)


