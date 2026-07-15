
NOME DO PROJETO:

'Projeto_avaliativo_final_M01'

---

NOME DO ALUNO E TURMA:

Maria Helena Paes de Barros - Visualização de Dados e Business Intelligence - T2

---

OBJETIVO DO TRABALHO:

Projeto apresentado para obtenção da nota parcial no Módulo 1 / Modelagem de Dados do Curso de Visualização de Dados e Business Intelligence / SCTEC - T2, 2026.

O objetivo desta Análise Exploratória de Dados (AED) é verificar a relação entre salários, cargos/departamentos e localização geográfica dos funcionários de uma empresa. Os dados estão distribuídos em 7 planilhas obtidas no site Freesql. Inicialmente, foi feita a consulta e extração dos dados. Eles foram divididos em 2 planilhas: uma relacionada a funcionários, cargos e salários (Query1), e outra, funcionários e local onde estão alocados (Query2). Com este projeto, pretende-se obter conclusões acerca de como os salários estão distribuídos entre os funcionários em razão dos cargos e departamentos, e da localidade onde prestam os serviços.

---

EXPLICAÇÃO SOBRE AS TABELAS CRIADAS / RESUMO DAS CONSULTAS SQL:

* Query1 - Relação de salários por departamentos e cargos:

1) Foram obtidos dados provenientes das tabelas HR.EMPLOYEES, HR.JOBS, HR.JOB_HISTORY e HR.DEPARTMENT.
2) Foram selecionadas as colunas EMPLOYEE_ID, HIRE_DATE, START_DATE, END_DATE, JOB_TITLE, DEPARTMENT_NAME, MANAGER_ID, SALARY, COMMISSION_PCT, MIN_SALARY, MAX_SALARY e LOCATION_ID;
3) Foram criadas 2 colunas a partir da HIRE_DATE: a coluna YEAR_HIRE_DATE (ano da contratação) e MONTH_HIRE_DATE (mês da contratação).
4) Também foi criada uma coluna que calcula, em meses, o tempo de casa do funcionário (CONTRATATION_IN_MONTHS).
5) Dados sensíveis dos funcionários como nome, sobrenome, email e número de telefone não foram extraídos, uma vez que foi solicitado um estudo geral sobre a distribuição dos salários. Além disso, esses dados não serão utilizados em gráficos e a sua ausência torna o arquivo da query mais leve.
6) Verificaram-se muitos dados nulos nas colunas START_DATE e END_DATE. No entanto, é possível concluir que uma informação válida na coluna END_DATE significa a formalização do desligamento do funcionário. Como a análise tem como objetivo verificar informações atuais, entendeu-se que os dados dos funcionários desligados poderia ser excluídos (WHERE ... IS NULL). Neste caso, o filtro foi utilizado para encontrarmos esses dados. Esse é o motivo dessas colunas terem sido extraídas: para formar o filtro de funcionários ativos. Após criação do arquivo csv, ditas colunas serão excluídas na fase de tratamento dos dados.
7) Posteriormente, percebeu-se que poderia ter extraído apenas a coluna END_DATE para selecionar os funcionários ativos (commit: 'altera linha 29 - filtro'). Alterou-se somente o arquivo 'Query1.sql'. O arquivo csv também foi alterado (commit exclusão do arquivo e upload de arquivo atualizado).
8) Concluiu-se que a coluna START_DATE poderia ser removida pelo fato da coluna HIRE_DATE formalizar a contratação do funcionário. Muitas vezes, a data da contratação não coincide com a data do início do trabalho por acordo feito entre o funcionário recém contratado e seu gestor. No entanto, para o Departamento de Recursos Humanos, o que realmente importa é a data da contratação.

* Query2 - Relação de funcionários por localidade

1) Foram obtidos dados provenientes das tabelas HR.EMPLOYEES, HR.JOB_HISTORY, HR.DEPARTMENT, HR.LOCATIONS, HR.COUNTRIES e HR.REGIONS.
2) Foram selecionadas as colunas EMPLOYEE_ID, SALARY, COMMISSION_PCT, END_DATE, STREET_ADRESS_ POSTAL_CODE, CITY, STATE_PROVINCE, COUNTRY_ID, COUNTRY_NAME, REGION_ID e REGION_NAME.
3) As colunas SALARY e COMMISSION_PCT foram incluídas na query para facilitar a comparação pretendida.
4) A coluna END_DATE foi incluída para formar a filtragem dos funcionários ativos (WHERE ... IS NULL). Ela será removida na fase de tratamento dos dados.
5) Posteriormente, foi verificada a possibilidade de remoção das colunas COUNTRY_ID e REGION_ID, uma vez que foram importadas as colunas COUNTRY_NAME e REGION_NAME, não havendo a necessidade de permanecerem na base de dados. Os arquivos sql e csv da query foram devidamente alterados.

---

EXPLICAÇÃO DA ANÁLISE FEITA EM PYTHON:

DADOS GERAIS

1) Verificou-se a existência dos dados de 100 funcionários ativos (linhas das tabelas).
2) Os funcionários estão distribuídos em 15 cargos, de 10 departamentos e alocados em 7 locais distintos.
3) Optou-se por tratar e analisar as queries em um mesmo notebook para facilitar eventual futura mescla dos dataframes.
4) Durante a análise, após o tratamento dos dados, optou-se pela união das queries para a criação de gráficos e tabelas que pudessem trazer mais informações úteis ('df_unido').
5) Renomeação das colunas Query1: 'EMPREGADO_ID', 'DATA_ADMISSAO', 'ANO_ADMISSAO', 'MES_ADMISSAO', 'TEMPO_CONTRATACAO_MESES', 'CARGO', 'DEPARTAMENTO', 'GERENTE_ID', 'SALARIO', 'COMISSAO_PCT', 'MIN_SALARIO', 'MAX_SALARIO'.
6) Renomeação das colunas Query2: 'EMPREGADO_ID', 'SALARIO', 'COMISSAO_PCT', 'ENDERECO', 'CEP', 'CIDADE', 'ESTADO', 'PAIS', 'REGIAO'.
7) Renomeação dos departamentos: 'diretoria', 'TI', 'financeiro', 'compras', 'expedicao', 'vendas', 'MKT', 'RH', 'RP', 'contabilidade'.
8) Renomeação dos cargos: 'presidente', 'programador', 'gerente_financeiro', 'contador', 'assistente_compras', 'gerente_estoque', 'assistente_estoque', 'gerente_vendas', 'representante_vendas', 'assistente_expedicao', 'representante_MKT', 'representante_RH', 'representante_RP', 'gerente_contabilidade', 'contador_publico'.

QUERY1

1) Não foram encontrados dados duplicados;
2) O tipo da coluna DATA_ADMISSAO é de número inteiro (int64) e foi alterado para datetime;
3) As colunas START_DATE e END_DATE foram excluídas antes da renomeação (dados 100% nulos);
4) Verificou-se que a coluna LOCATION_ID não seria utilizada nessa query e foi excluída antes da renomeação;
5) A coluna GERENTE_ID é do tipo float e estava totalmente desconfigurada. Portanto, foi alterada para texto (str);
6) As colunas DEPARTAMENTO e GERENTE_ID possuíam apenas 1 dado nulo. Assim, essas células foram preenchidas como 'dado_ausente';
7) A coluna COMISSAO_PCT possuía 66 dados nulos. Como a comissão é parte integrante do salário, essa coluna foi mantida. Ela foi preenchida pelo valor '0.0'. É muito provável que os valores nulos referem-se aos cargos que não recebem comissões.

QUERY2

1) Não foram encontrados dados duplicados;
2) A coluna END_DATE foi excluída antes da renomeação (dados 100% nulos);
3) As colunas ENDERECO, CEP, CIDADE, ESTADO, PAIS e REGIAO possuiam dados nulos. No entanto, essas células foram preenchidas com 'dado_ausente';
4) As nulidades da coluna COMISSAO_PCT também foram tratadas antes da mesclagem das queries;

RELAÇÃO DE GRÁFICOS E TABELAS

GRÁFICO 1: Distribuição de Departamentos por Cidade
GRÁFICO 2: Distribuição de Cargos por Cidade
GRÁFICO 3: Salário x Departamento
GRÁFICO 4: Salário x Departamento x Cargo
GRÁFICO 5: Salário x tempo de contratação (Cargos Selecionados)
GRÁFICO 6: Comissão x Cargos
GRÁFICO 7: Comissão x Tempo de contratação
TABELA 1: Gerente de Vendas - Informações sobre Tempo de Contratação, Comissão e Salário
TABELA 2: Representante de Vendas - Informações sobre Tempo de Contratação, Comissão e Salário

PROCEDIMENTOS:

1) A boa prática orienta o tratamento dos dados antes de eventual união de dataframes;
2) Ao visualizar as informações estatísticas da Query1, concluímos pela grande dispensão de valores das colunas SALARY, COMMISSION_PCT, MIN_SALARY e MAX_SALARY
3) As queries foram unidas por meio da coluna EMPLOYEE_ID, comum a ambas.

---

PRINCIPAIS RESULTADOS ENCONTRADOS:

1) Ao visualizar as informações estatísticas da Query1, conclui-se pela grande dispersão de valores das colunas 'SALARIO', 'COMISSAO_PCT', 'MIN_SALARIO' e 'MAX_SALARIO'.
2) Após verificar a contabilização dos dados das colunas CARGO e DEPARTAMENTO pela função 'value_counts', foi possível perceber que o único dado nulo da coluna DEPARTAMENTO referiu-se ao cargo 'representante de vendas', que pertence ao departamento 'vendas'. Assim, o valor 'dado_ausente' desta coluna foi substituído por 'vendas'.
3) Como a base de dados não é grande, foi possível obter muitas tabelas que facilitaram a análise.
4) Com base no GRÁFICO 1 e no GRÁFICO 2, é possível relacionar todos os cargos com os departamentos e a cidade onde estão localizados (escritórios regionais):

DEPARTAMENTO	CIDADE	    		ESTADO			PAIS		    		REGIAO		FUNCIONARIOS
MKT				Toronto	    		Ontaro			Canada		    	Americas				1
RH				London	    						United Kingdom	Europe				1
RP				Munich	    		Bavaria			Germany		    	Europe				1
TI				Southlake   		Texas			USA		    		Americas				5
compras			Seattle	    		Washington		USA		   		Americas				14
contabilidade
diretoria
financeiro
expedicao		San Francisco		California			USA		    		Americas				44
vendas			Oxford			Oxford			United Kingdom	Europe				33

5) A estrutura é bastante dispersa. O setor administrativo está localizado em Seattle/USA.
6) Parte-se da premissa de que todos os departamentos estão alocados em um determinado escritório, ou seja, não há departamentos, e, consequentemente, cargos, dispersos entre os escritórios regionais. Não há que se falar, portanto, em diferença salarial em razão do local onde o funcionário está alocado.
7) Em relação à distribuição salarial entre departamentos, pode-se verificar que o salario do 'presidente' ('diretoria') é muito superior aos maiores salários dos demais departamentos. Os departamentos com os menores salários são 'compras' e 'expedição'.
8) Os departamentos de 'MK', 'RH', 'RP' e a 'diretoria' são ocupados somente por um funcionário. Assim, não tem sentido o estudo sobre a diferença salarial entre os ocupantes dos cargos de 'presidente', 'representante de marketing', 'representante de RH' e 'representante de RP'. Desta forma, a análise foca apenas nos departamentos 'vendas', 'expedicao', 'TI', 'financeiro', 'compras' e 'contabilidade'.
9) O departamento de 'compras' tem 5 funcionários e é o setor que tem os salários mais equilibrados. Tem somente cargos de 'assistente de compras' e o salário varia entre $2.500 a $3.100. Essa diferença tem relação com o tempo de contratação.
10) O departamento de 'expedição' tem 44 funcionários. É composto pelos cargos de 'gerente de estoque', 'assistente de estoque' e 'assistente de expedição'. Pelas informações obtidas, verificam-se funcionários com o mesmo tempo de casa recebendo salários diferentes; casos pontuais de pessoas com menos tempo de casa recebem salário maior que o colega que esta há mais tempo contratado. Essa diferença é mais impactante em relação aos gerentes: um gerente trabalha há quase 130 meses e recebe $6.500, outro, que tem somente 5 meses a mais de casa, recebe mais de $ 8.000.
11) O departamento de 'TI' tem somente cargos de 'programador'. São 5 funcionários. Os salários de 3 programadores variam entre $4.000 e $5.000, conforme tempo de contratação. No entanto, o programador com menos tempo de casa tem o salario de $6.000. O segundo funcionário mais antigo recebe $9.000. É necessário verificar a razão desses dois outliers.
12) O departamento 'financeiro' é composto por 1 'gerente financeiro' e 5 'contadores'. O gerente tem o maior salario. Os salários estão vinculados ao tempo de contrato. O contador com menor tempo de contratação recebe $6.900, o com maior tempo, $9.000. No entanto, 2 contadores com o mesmo tempo de casa (129 meses) recebem salários diferentes: $7.600 e $8.200. É importante verificar a razão dessa divergência.
13) No departamento de 'vendas', temos 5 'gerentes de vendas' e 29 'representantes de vendas'. Os salários são bastante divergentes (variam entre $10.500 e $14.000), mas estão de acordo com o tempo de contratação. Atenção para o gerente que recebe $12.000 e trabalha na empresa há 136 meses e para o seu colega que trabalha 2 meses a mais e tem o salario de $13.500. Qual a razão dessa diferença significativa? Já em relação aos representantes de vendas: salários bem variáveis (entre $6.100 e $11.500).  Percebe-se também que o valor não tem relação com o tempo de contrato.
14) O departamento de 'vendas' é o único em que os funcionários recebem comissão. Entre os gerentes, o percentual da comissão aumenta de acordo com o tempo de casa, mas não é proporcional (os 3 gerentes que recebem 0.3% de comissão têm 104, 136 e 138 meses de contratação - tempo de casa diferentes). O mesmo ocorre com os representantes de vendas: o percentual de comissão varia de acordo com o tempo de contratação. No entanto, há algumas exceções e é necessário verificar a razão disso. Ainda, nota-se que o percentual de comissão não tem relação com o valor do salário dos representantes de vendas.
15) Finalmente, o departamento de 'contabilidade' é composto por 1 'gerente de contabilidade' e 1 'contador público'. Como são 2 cargos diferentes, não há como realizar uma comparação, pois os salários estão relacionados com as atribuições de cada um.

---

CONCLUSAO:

Com base na análise feita, sugere-se:

1) Verificar a razão da existência de salários divergentes entre ocupantes do mesmo cargo e com tempo de contrato semelhante; e
2) Criar e praticar uma politica de cargos e salários visando incentivar a produtividade e a retenção de talentos.

---

COMO EXECUTAR O PROJETO:

1) Abrir diretório no GitHub: https://github.com/mariahbarros/Projeto_avaliativo_final_M01;
2) Durante a execução do projeto, todo o versionamento ocorreu na branch 'secundaria'. Somente os documentos finais foram mesclados na branch 'main'.
3) Abrir o README.md no VSCode;
4) Abrir os arquivos Query1_sql e Query2_sql no VSCode (eles foram criados apenas para extração dos dados no Freesql);
5) Os arquivos Query1_csv e Query2_csv, obtidos dos arquivos sql nos quais constam os dados obtidos na consulta ao Freesql, são analisados em um notebook no VSCode por meio da análise exploratória dos dados - AED (ver arquivo 'AED_HR.ipynb');
6) Abrir o arquivo 'AED_HR.py' no VScode (visualização final da AED);
7) Todas as orientações, observações e conclusões obtidas durante a execução e após a conclusão do projeto estão nesse arquivo README.md.

---

SUGESTÕES DE MELHORIAS PARA FUTURAS VERSÕES:

1) Infelizmente não foram coletados dados sobre o sexo dos funcionários. A verificação dos salários em relação ao sexo seria fundamental para uma análise de distribuição mais precisa e permitiria a retificação de eventuais distorções em relação ao plano de carreira de cada funcionário.
2) Como se trata de uma tabela do RH com os dados dos funcionários que não são constantemente alterados, seria interessante unir todas as informações em apenas um documento, o que tornaria a consulta mais fácil e completa e eliminaria todas as chaves Id's.
3) Acredita-se que somente a informação da cidade onde o funcionário está alocado já seja suficiente para análise em relação à sua localização. Não há necessidade de constar endereço, CEP, Estado, País ou Região da localidade, afinal, os departamentos estão concentrados em um único local (cidade/escritório regional).
4) Para uma análise constante do estudo pretendido, sugere-se a criação de uma tabela única com as seguintes colunas: EMPREGADO_ID, SEXO, DATA_ADMISSAO, CARGO, DEPARTAMENTO, SALARIO, COMISSAO_PCT, CIDADE/ESCRITÓRIO REGIONAL. O tempo de contrato, que é uma informação muito importante, será calculado dentro de AED (por meio de código em python para que o cálculo esteja sempre atualizado na data da consulta).
