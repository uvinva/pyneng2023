# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
network = input("Введите адрес сети в формате: 10.1.1.0/24\n")
mask = network.split("/")[1]
ip = network.split("/")[0]
ip1 = int(ip.split('.')[0])
ip2 = int(ip.split('.')[1])
ip3 = int(ip.split('.')[2])
ip4 = int(ip.split('.')[3])
bin_mask = "1"*int(mask) + (32-int(mask))*"0"
bin_mask1 = bin_mask[:8]
bin_mask2 = bin_mask[8:16]
bin_mask3 = bin_mask[16:24]
bin_mask4 = bin_mask[24:]
int_mask1 = int(bin_mask1,2)
int_mask2 = int(bin_mask2,2)
int_mask3 = int(bin_mask3,2)
int_mask4 = int(bin_mask4,2)


template = """
Network:
{ip1:<8}  {ip2:<8}  {ip3:<8}  {ip4:<8}
{ip1:08b}  {ip2:08b}  {ip3:08b}  {ip4:08b}
Mask:
/{mask}
{int_mask1:<8} {int_mask2:<8} {int_mask3:<8} {int_mask4:<8}
{int_mask1:<08b}  {int_mask2:<08b}  {int_mask3:<08b}  {int_mask4:<08b}"""

print(template.format(ip1=ip1,ip2=ip2,ip3=ip3,ip4=ip4, int_mask1=int_mask1,int_mask2=int_mask2,int_mask3=int_mask3,int_mask4=int_mask4,mask=mask))