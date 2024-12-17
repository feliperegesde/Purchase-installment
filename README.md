Descrição
Este código em Python calcula o parcelamento de um valor total em um número definido de meses, exibindo as datas de vencimento e os valores de cada parcela. Ele também informa o total do empréstimo e o número de meses/anos necessários para quitá-lo.

Funcionalidades
Solicita o valor do produto e o número de meses para parcelamento.
Calcula a data de cada parcela a partir da data atual.
Divide o valor total igualmente entre as parcelas.
Exibe as datas e valores de cada parcela.
Mostra um resumo com o valor total, tempo de pagamento e valor de cada parcela.
Como Executar
Certifique-se de que Python 3.x esteja instalado em sua máquina.
Instale a biblioteca dateutil se ainda não estiver instalada:
bash
Copiar código
pip install python-dateutil
Salve o código em um arquivo, por exemplo, parcelamento.py.
Execute o programa:
bash
Copiar código
python parcelamento.py
Exemplo de Uso
Ao executar o programa, você verá as seguintes solicitações no terminal:

plaintext
Copiar código
Valor Do produto: 1200
Digite em quantos Meses Voce quer parcelar: 12
O programa exibirá as datas e valores de cada parcela:

plaintext
Copiar código
16/12/2024 R$ 100,00
16/01/2025 R$ 100,00
...
16/11/2025 R$ 100,00
Por fim, mostrará um resumo do parcelamento:

plaintext
Copiar código
Você pegou R$ 1.200,00 para pagar em 1 anos (12 meses) em parcelas de R$ 100,00.
Entradas
valor_total: Valor total do produto ou empréstimo.
months: Número de meses para parcelar.
Saídas
Lista das datas de vencimento de cada parcela com seus respectivos valores.
Resumo detalhado com o valor total, número de meses/anos e valor de cada parcela.
Pré-requisitos
Python 3.x.
Biblioteca dateutil.
Explicação do Código
Importação de Bibliotecas:

datetime e dateutil.relativedelta são usados para lidar com datas e calcular intervalos mensais.
Cálculo das Datas de Parcelas:

Usa a data atual (datetime.now()) como ponto inicial e incrementa mês a mês até atingir o número de meses desejado.
Cálculo do Valor das Parcelas:

Divide o valor total pelo número de parcelas.
Exibição das Parcelas:

Mostra as datas no formato DD/MM/YYYY e os valores formatados com duas casas decimais.
Resumo Final:

Apresenta os detalhes do empréstimo de forma clara e estruturada.
Possíveis Melhorias
Adicionar juros no cálculo das parcelas.
Permitir entrada de uma data inicial diferente da data atual.
Exportar as informações para um arquivo (CSV ou PDF).
Autor: Felipe Reges de
Data: Dezembro de 2024
