from datetime import datetime
from dateutil.relativedelta import relativedelta

data_str_data = '2022/04/20 07:49:23'
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
#print(data)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
#print(delta.days, delta.years)
# print(data_fim - delta)
# print(data_fim)
#print(data_fim + relativedelta(seconds=60, minutes=10))
# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
#print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
#print(data.strftime('%d/%m/%Y'))
#print(data.strftime('%d/%m/%Y %H:%M'))
#print(data.strftime('%d/%m/%Y %H:%M:%S'))
#print(data.strftime('%Y'), data.year)
#print(data.strftime('%d'), data.day)
#print(data.strftime('%m'), data.month)
#print(data.strftime('%H'), data.hour)
#print(data.strftime('%M'), data.minute)
#print(data.strftime('%S'), data.second)
