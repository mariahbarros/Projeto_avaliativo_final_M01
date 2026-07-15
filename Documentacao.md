
# NOME DO PROJETO:

'Projeto_avaliativo_final_M01'

---

# NOME DO ALUNO E TURMA:

Maria Helena Paes de Barros - Visualização de Dados e Business Intelligence - T2

---

# OBJETIVO DO TRABALHO:

Projeto apresentado para obtenção da nota parcial no Módulo 1 / Modelagem de Dados do Curso de Visualização de Dados e Business Intelligence / SCTEC - T2, 2026.

O objetivo desta Análise Exploratória de Dados (AED) é verificar a relação entre salários, cargos/departamentos e localização geográfica dos funcionários de uma empresa. Os dados estão distribuídos em 7 planilhas obtidas no site Freesql. Inicialmente, foi feita a consulta e extração dos dados. Eles foram divididos em 2 planilhas: uma relacionada a funcionários, cargos e salários (Query1), e outra, funcionários e local onde estão alocados (Query2). Com este projeto, pretende-se obter conclusões acerca de como os salários estão distribuídos entre os funcionários em razão dos cargos e departamentos, e da localidade onde prestam os serviços.

---

# EXPLICAÇÃO SOBRE AS TABELAS CRIADAS / RESUMO DAS CONSULTAS SQL:

Query1 - Relação de salários por departamentos e cargos:

1) Foram obtidos dados provenientes das tabelas HR.EMPLOYEES, HR.JOBS, HR.JOB_HISTORY e HR.DEPARTMENT.
2) Foram selecionadas as colunas EMPLOYEE_ID, HIRE_DATE, JOB_TITLE, DEPARTMENT_NAME, SALARY, COMMISSION_PCT, MIN_SALARY e MAX_SALARY.
3) Dados sensíveis dos funcionários como nome, sobrenome, email e número de telefone não foram extraídos, uma vez que foi solicitado um estudo geral sobre a distribuição dos salários. Além disso, esses dados não serão utilizados em gráficos e a sua ausência torna o arquivo da query mais leve.
4) A coluna END_DATE, apesar de não ter sido exportada na pesquisa, foi utilizada para filtrar os funcionários ativos, ou seja, os funcionários que tinham informações nesta coluna foram excluídos da base de dados por já terem suas rescisões formalizadas (filtro: WHERE ... IS NULL).

Query2 - Relação de funcionários por localidade

1) Foram obtidos dados provenientes das tabelas HR.EMPLOYEES, HR.JOB_HISTORY, HR.DEPARTMENT, HR.LOCATIONS, HR.COUNTRIES e HR.REGIONS.
2) Foram selecionadas as colunas EMPLOYEE_ID, SALARY, COMMISSION_PCT, STREET_ADRESS, POSTAL_CODE, CITY, STATE_PROVINCE, COUNTRY_NAME e REGION_NAME.
3) As colunas SALARY e COMMISSION_PCT foram incluídas na query para facilitar a comparação pretendida.
4) A coluna END_DATE também foi utilizada para filtrar os funcionários ativos, apesar de igualmente não ter sido exportada para a base de dados (filtro: WHERE ... IS NULL).

---

# EXPLICAÇÃO DA ANÁLISE FEITA EM PYTHON:

DADOS GERAIS

1) Verificou-se a existência dos dados de 100 funcionários ativos (linhas das tabelas).
2) Os funcionários estão distribuídos entre 15 cargos, de 10 departamentos e alocados em 7 locais distintos.
3) Cada departamento tem a sua faixa salarial.
4) Durante a análise, após o tratamento dos dados, optou-se pela união das queries para a criação de gráficos e tabelas que pudessem trazer informações diretas sobre cargos, departamentos e localização (TABELA 3). Esta é a razão pela qual a AED das duas bases de dados ter sido realizada em um único notebook.

QUERY1

1) Verificou-se que o tipo da coluna HIRE_DATE é de número inteiro (int64). Para poder efetuar calculo entre datas foi necessária a sua alteração para o tipo datetime.
2) Após isso, criou-se a coluna TEMPO_CONTRATACAO_MESES, com o objetivo de especificar o tempo de contratação do funcionário. Esse cálculo levará sempre em consideração a data atual em que a consulta.
3) Foram tratadas nulidades nas colunas COMMISSION_PCT e DEPARTMENT_NAME.

- A coluna COMMISSION_PCT possuía 66 dados nulos. Como a comissão é parte integrante do salário, essa coluna foi mantida. Ela foi preenchida pelo valor '0.0', pois confirmou-se que os valores nulos referem-se aos cargos que não recebem comissões (GRÁFICO 6).

- A coluna DEPARTMENT_NAME possuía apenas 1 dado nulo. Após verificar a base de dados unida (TABELA 3), que relaciona cargos, departamentos e localização, foi possível perceber que esse dado nulo refere-se ao cargo 'representante de vendas', que pertence ao departamento 'vendas'. Assim, a nulidade desta coluna foi tratada e substituída pelo valor 'vendas'.

4) Não foram encontrados dados duplicados.
5) Foi feita a renomeação das colunas Query1: 'EMPREGADO_ID', 'DATA_ADMISSAO', 'CARGO', 'DEPARTAMENTO', ''SALARIO', 'COMISSAO_PCT', 'MIN_SALARIO' e 'MAX_SALARIO'.
6) Feita a renomeação dos departamentos: 'diretoria', 'TI', 'financeiro', 'compras', 'expedicao', 'vendas', 'MKT', 'RH', 'RP' e 'contabilidade'.
7) Feita, também, a renomeação dos cargos: 'presidente', 'programador', 'gerente_financeiro', 'contador', 'assistente_compras', 'gerente_estoque', 'assistente_estoque', 'gerente_vendas', 'representante_vendas', 'assistente_expedicao', 'representante_MKT', 'representante_RH', 'representante_RP', 'gerente_contabilidade' e 'contador_publico'.

QUERY2

1) Não foram encontrados dados duplicados.
2) As colunas ENDERECO, CEP, CIDADE, ESTADO, PAIS e REGIAO possuíam dados nulos. Essas células foram preenchidas como valor 'dado_ausente' para evitar eventuais inconsistências com funções e gráficos.
3) As nulidades da coluna COMISSAO_PCT foram tratadas da mesma forma como ocorreu na Query1.
4) Foram renomeadas as colunas Query2: 'EMPREGADO_ID', 'SALARIO', 'COMISSAO_PCT', 'ENDERECO', 'CEP', 'CIDADE', 'ESTADO', 'PAIS' e 'REGIAO'.

RELAÇÃO DE GRÁFICOS E TABELAS

GRÁFICO 1: Departamentos x Cidade
GRÁFICO 2: Cargos x Cidade
GRÁFICO 3: Salários x Departamento
GRÁFICO 4: Salários x Cargo x Departamento
GRÁFICO 5: Salário x tempo de contratação (Cargos Selecionados)
GRÁFICO 6: Comissão x Cargos
GRÁFICO 7: Comissão x Tempo de contratação
TABELA 1: Cargos x departamentos
TABELA 2: Relacionando localizações
TABELA 3: Cargos, departamentos e localizações
TABELA 4: Gerente de Vendas - Informações sobre Tempo de Contratação, Comissão e Salário
TABELA 5: Representante de Vendas - Informações sobre Tempo de Contratação, Comissão e Salário

PROCEDIMENTOS:

1) Consulta das tabelas, escolha das colunas e extração das bases de dados em sql.
2) Criação das bases de dados em formato .csv para análise em python.
3) Importação das bases de dados em notebook Jupyter (melhor opção para realizar a codificação, objetivando a criação de tabelas e gráficos).
4) Tratamento e análise exploratória dos dados.
5) Criação de arquivo .py (melhor opção para visualizar a codificação já pronta).
6) Criação do arquivo 'Documentação.md', que documenta todo o procedimento, análise e conclusão do projeto. Optou-se pela documentação em arquivo diverso do README.md para não sobrecarregar a página inicial do repositório 'https://github.com/mariahbarros/Projeto_avaliativo_final_M01'.
7) Versionamento de todas as alterações em 4 branches: 1. main (principal), 2. secundaria (estruturação do projeto), 3. ajustes (alterações significativas e atualizações visando a versão final dos documentos), e 4. formatação (ajustes finos finais de formatação e estruturação dos documentos no repositório).

---

# PRINCIPAIS RESULTADOS ENCONTRADOS:

1) Ao visualizar as informações estatísticas da Query1, conclui-se pela grande dispersão de valores das colunas SALARIO, COMISSAO_PCT, MIN_SALARIO e MAX_SALARIO.
2) Não existem salários fora da faixa salarial estabelecida nas tabelas MIN_SALARIO e MAX_SALARIO.
3) Com base no GRÁFICO 1 e no GRÁFICO 2, é possível relacionar todos os cargos com os departamentos e a cidade onde estão localizados (escritórios regionais):

DEPARTAMENTO		CIDADE	    		ESTADO			PAIS		    		REGIAO		FUNCIONARIOS
MKT					Toronto	    		Ontaro			Canada			Americas					1
RH					London	    						United Kingdom	Europe					1
RP					Munich	    		Bavaria			Germany		    	Europe					1
TI					Southlake   		Texas			USA		    		Americas					5
compras				Seattle	    		Washington		USA		    		Americas				      14
contabilidade
diretoria
financeiro
expedicao			San Francisco		California			USA		    		Americas				     44
vendas				Oxford			Oxford			United Kingdom	Europe				     33

4) A estrutura é bastante dispersa. O setor administrativo está localizado em Seattle/USA.
5) Parte-se da premissa de que todos os departamentos estão alocados em um determinado escritório de maneira concentrada, ou seja, não há departamentos, e, consequentemente, cargos, dispersos entre os escritórios regionais. Não há que se falar, portanto, em diferença salarial em razão do local onde o funcionário está alocado.
6) Em relação à distribuição salarial entre departamentos, pode-se verificar que o salario do 'presidente' ('diretoria') é muito superior aos maiores salários dos demais departamentos. Os departamentos com os menores salários são 'compras' e 'expedição'.
7) Os departamentos de 'MK', 'RH', 'RP' e a 'diretoria' são ocupados somente por um funcionário. Assim, não tem sentido o estudo sobre a diferença salarial entre os ocupantes dos cargos de 'presidente', 'representante de marketing', 'representante de RH' e 'representante de RP'. Desta forma, a análise foca apenas nos departamentos 'vendas', 'expedicao', 'TI', 'financeiro', 'compras' e 'contabilidade'.
8) O departamento de 'compras' tem 5 funcionários e é o setor que tem os salários mais equilibrados. Tem somente cargos de 'assistente de compras' e o salário varia entre $2.500 a $3.100. Essa diferença tem relação com o tempo de contratação.
9) O departamento de 'expedição' tem 44 funcionários. É composto pelos cargos de 'gerente de estoque', 'assistente de estoque' e 'assistente de expedição'. Pelas informações obtidas, verificam-se funcionários com o mesmo tempo de casa recebendo salários diferentes; casos pontuais de pessoas com menos tempo de casa recebem salário maior do que o colega que esta há mais tempo contratado. Essa diferença é mais impactante em relação aos gerentes: um gerente trabalha há quase 130 meses e recebe $6.500, outro, que tem somente 5 meses a mais de casa, recebe mais de $ 8.000.
10) O departamento de 'TI' tem somente cargos de 'programador'. São 5 funcionários. Os salários de 3 programadores variam entre $4.000 e $5.000, conforme tempo de contratação. No entanto, o programador com menos tempo de casa tem o salario de $6.000. O segundo funcionário mais antigo recebe $9.000. É necessário verificar a razão dessas disparidades.
11) O departamento 'financeiro' é composto por 1 'gerente financeiro' e 5 'contadores'. O gerente tem o maior salario. Os salários estão vinculados ao tempo de contrato. O contador com menor tempo de contratação recebe $6.900, o com maior tempo, $9.000. No entanto, 2 contadores com o mesmo tempo de casa (129 meses) recebem salários diferentes: $7.600 e $8.200. É importante verificar a razão dessa divergência.
12) No departamento de 'vendas', temos 5 'gerentes de vendas' e 29 'representantes de vendas'. Os salários são bastante divergentes (variam entre $10.500 e $14.000), mas estão de acordo com o tempo de contratação. Atenção para o gerente que recebe $12.000 e trabalha na empresa há 136 meses e para o seu colega que trabalha 2 meses a mais e tem o salario de $13.500. Qual a razão dessa diferença significativa? Já em relação aos representantes de vendas: salários bem veri[aveis (entre $6.100 e $11.500). Percebe-se também que o valor salarial não tem relação com o  tempo de contrato.

13. O departamento de 'vendas' é o único em que os funcionários recebem comissão. Entre os gerentes, o percentual da comissão aumenta de acordo com o tempo de casa, mas não é proporcional (os 3 gerentes que recebem 0.3% de comissão têm 104, 136 e 138 meses de contratação - tempo de casa diferentes). O mesmo ocorre com os representantes de vendas: o percentual de comissão varia de acordo com o tempo de contratação. No entanto, há algumas exceções e é necessário verificar a razão disso. Ainda, nota-se que o percentual de comissão não tem relação com o valor do salário dos representantes de vendas.

14. Finalmente, o departamento de 'contabilidade' é composto por 1 'gerente de contabilidade' e 1 'contador público'. Como são 2 cargos diferentes, não há como realizar uma comparação, pois os salários estão relacionados com as atribuições de cada um.

---

# CONCLUSAO:

Com base na análise feita, sugere-se:

1) Verificar a razão da existência de salários divergentes entre ocupantes do mesmo cargo e com tempo de contrato semelhante; e
2) Criar e praticar uma politica de cargos e salários visando incentivar a produtividade e a retenção de talentos.

---

# COMO EXECUTAR O PROJETO:

1) Abrir diretório no GitHub: https://github.com/mariahbarros/Projeto_avaliativo_final_M01.
2) Analisar os documentos da branch 'main'.
3) Abrir o arquivo 'Documentacao.md' no VSCode.
4) Para visualizar os códigos e gráficos, abrir os arquivos 'AED_HR.ipynb' ou 'AED_HR.py' no VScode.
5) Todas as orientações, observações e conclusões obtidas durante a execução e após a conclusão do projeto estão no arquivo 'Documentacao.md', complemento do arquivo README.md.

---

# SUGESTÕES DE MELHORIAS PARA FUTURAS VERSÕES:

1) Infelizmente não foram coletados dados sobre o sexo dos funcionários. A análise dos salários em relação ao sexo seria fundamental para a verificação de uma distribuição mais precisa e permitiria a retificação de eventuais distorções em relação ao plano de carreira de cada funcionário.
2) Interessante também verificar se o nível de escolaridade dos funcionários tem relação direta com os distintos salários em um mesmo cargo.
3) Como se trata de uma tabela do RH com os dados dos funcionários que não são constantemente alterados, seria interessante unir todas as informações em apenas um documento, o que tornaria a consulta mais fácil e completa e eliminaria todas as chaves Id's.
4) Acredita-se que somente a informação sobre a cidade onde o funcionário está alocado seja suficiente para análise em relação à localidade. Não há necessidade de constar endereço, CEP, Estado, País ou Região da localidade, afinal, os departamentos estão concentrados em um único local (cidade/escritório regional).
5) Para uma análise constante do estudo pretendido, sugere-se a criação de uma tabela única com as seguintes colunas: EMPREGADO_ID, SEXO, ESCOLARIDADE, DATA_ADMISSAO, CARGO, DEPARTAMENTO, SALARIO, COMISSAO_PCT, CIDADE/ESCRITÓRIO REGIONAL.
