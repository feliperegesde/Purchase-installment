Descrição

Este programa em Python calcula o parcelamento de um valor total em um número definido de meses. Ele exibe as datas de vencimento e o valor de cada parcela, além de fornecer um resumo detalhado do empréstimo ou compra parcelada.

Como Funciona

O usuário insere:

O valor total do produto.

O número de meses para parcelar o pagamento.

O programa calcula:

As datas de vencimento de cada parcela a partir da data atual.

O valor de cada parcela dividindo o valor total pelo número de parcelas.

O programa exibe:

As datas e valores de cada parcela.

Um resumo com o valor total, o tempo de pagamento (em anos e meses) e o valor de cada parcela.

Como Usar

1. Pré-requisitos

Python 3.x instalado.

Biblioteca python-dateutil instalada. Para instalar:

bash

Copiar código

pip install python-dateutil

1. Executando o Programa

Copie o código abaixo e cole em um arquivo chamado parcelamento.py.

python

Copiar código

from datetime import datetime

from dateutil.relativedelta import relativedelta

valor\_total = float(input("Valor Do produto: "))

data\_emprestimo = datetime.now()

months = int(input("Digite em quantos Meses Voce quer parcelar: "))

delta\_meses = relativedelta(months=months)

data\_final = data\_emprestimo + delta\_meses

data\_parcelas = []

data\_parcela = data\_emprestimo

while data\_parcela < data\_final:

data\_parcelas.append(data\_parcela)

data\_parcela += relativedelta(months=+1)

numero\_parcelas = len(data\_parcelas)

valor\_parcela = valor\_total / numero\_parcelas

for data in data\_parcelas:

print(data.strftime('%d/%m/%Y'), f'R$ {valor\_parcela:,.2f}')

print()

print(

f'Você pegou R$ {valor\_total:,.2f} para pagar '

f'em {delta\_meses.years} anos '

f'({numero\_parcelas} meses) em parcelas de '

f'R$ {valor\_parcela:,.2f}.'

)

No terminal ou prompt de comando, execute o arquivo:

bash

Copiar código

python parcelamento.py

Insira os valores solicitados, como no exemplo:

plaintext

Copiar código

Valor Do produto: 1200

Digite em quantos Meses Voce quer parcelar: 12

Exemplo de Saída

Ao rodar o programa com os valores de entrada acima, ele retornará:

plaintext

Copiar código

16/12/2024 R$ 100,00

16/01/2025 R$ 100,00

16/02/2025 R$ 100,00

...

16/11/2025 R$ 100,00

Você pegou R$ 1.200,00 para pagar em 1 anos (12 meses) em parcelas de R$ 100,00.

Detalhes Técnicos

Entrada:

Valor Do produto: Valor total a ser parcelado.

Digite em quantos Meses Voce quer parcelar: Quantidade de meses para dividir o valor.

Saída:

Datas e valores de cada parcela.

Resumo com valor total, número de meses/anos e valor das parcelas.

Possíveis Melhorias

Adicionar cálculos de juros.

Permitir uma data inicial personalizada (diferente da data atual).

Exportar os resultados para um arquivo CSV ou PDF.

Licença

Este código é livre para uso e modificação. Sinta-se à vontade para adaptar conforme suas necessidades.

Autor: Felipe Reges de

Data de Criação: Dezembro de 2024
