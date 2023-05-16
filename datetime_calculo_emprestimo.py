from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
'''
    Maria pegou um empréstimo de 1 milhão de reais, para pagar em 5 anos.
    Ela pegou dia 20/12/2020.
    O vencimento de cada parcela é no dia 20 de cada mês.
    
    Cria a data do empréstimo
    Crie a data do final do empréstimo
    Mostre todas as datas de vencimento e o valor de cada parcela.

'''
total_parcelas = 0
meses = 1
formato_data = '%d/%m/%Y'
emprestimo: float = 1000000
total_restante = emprestimo
prazo = relativedelta(years=5)
data_inicio = datetime.strptime('20/12/2020', formato_data)
data_final = data_inicio + prazo

data_parcelas = []
data_parcela = data_inicio

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)
    total_parcelas += 1
    
print(f'Total de parcelas: {total_parcelas} parcelas')
print(f'Data final do pagamento do empréstimo: {data_final.strftime(formato_data)}')
for data_parcela in data_parcelas:
    total_restante = total_restante - (emprestimo/total_parcelas)
    print(f'Parcela número: {meses}, Data: {data_parcela}, Valor da parcela: {emprestimo/total_parcelas:.2f}, Total ainda devido: R${total_restante:.2f}')
    meses += 1


print("finalizando execução")
