import json
import datetime


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def time_diff(t1, t2):
    Y1, M1, D1 = map(int, t1[10].split('-'))
    Y2, M2, D2 = map(int, t2[10].split('-'))
    H1, m1, S1 = map(int, t1[10:].split(':'))
    H2, m2, S2 = map(int, t2[10:].split(':'))
    date1 = datetime.date(Y1, M1, D1)
    date2 = datetime.date(Y1, M1, D1)
    diff = ['', 0]
    diff[0] = date2-date1
    diff[1] = (H2 - H1) * 24 + (m2 - m1) * 60 + S2 - S1


# def valid_thru(t1, t2):
#     if t1 >= t2:
#         return False
#     elif t1 < t2:
#         return True



Acc = [] # list of the accounts
SUS = [] # list of the suspicious operations

n0_data = read('transactions.json') # data from file

# check, based on dates
for t in n0_data['transactions']:
    if n0_data['transactions'][t]["account_valid_to"] < n0_data['transactions'][t]["date"]:
        SUS.append([n0_data['transactions'][t], 'a_v_to expired'])
    elif n0_data['transactions'][t]["passport_valid_to"] < n0_data['transactions'][t]["date"]:
        SUS.append([n0_data['transactions'][t], 'p_v_to expired'])
    elif n0_data['transactions'][t]["date_of_birth"] > n0_data['transactions'][t]["date"]:
        SUS.append([n0_data['transactions'][t], 'd_of_b wrong'])
    else:
        Acc.append(n0_data['transactions'][t]['account'])
# print(len(Acc))
# print(len(set(Acc)))
# print('-----------')
# print(len(SUS))
# for i in SUS:
#     print(i[0]['oper_result'])

Acc = set(Acc)

pro_data = dict()  # OUR OWN DATA
# filling pro_data
for a in Acc:
    pro_data[a] = dict()
    for t in n0_data['transactions']:
        if n0_data['transactions'][t]['account'] == a:
            pro_data[a]['full_name'] = set()
            pro_data[a]['full_name'].add(n0_data['transactions'][t]['last_name']+n0_data['transactions'][t]['first_name']+n0_data['transactions'][t]['patronymic'])
            pro_data[a]['phone'] = set()
            pro_data[a]['phone'].add(n0_data['transactions'][t]['phone'])
            pro_data[a]['pp'] = set()
            pro_data[a]['pp'].add(n0_data['transactions'][t]['passport'])
            pro_data[a]['client'] = set()
            pro_data[a]['client'].add(n0_data['transactions'][t]['client'])
            pro_data[a]['cards'] = set()
            pro_data[a]['cards'].add(n0_data['transactions'][t]['card'])
            pro_data[a]['oper'] = []
            pro_data[a]['oper'].append([t, n0_data['transactions'][t]['date'], n0_data['transactions'][t]['oper_type'], n0_data['transactions'][t]['oper_result']])


# check of quantity of names, passports, phones, cards, clients
check = []
for a in Acc:
    if len(pro_data[a]['full_name']) > 1:
        check.append("YES, full_name > 1")
    if len(pro_data[a]['pp']) > 1:
        check.append("YES, pp > 1")
    if len(pro_data[a]['client']) > 1:
        check.append("YES, client > 1")
    if len(pro_data[a]['phone']) > 1:
        check.append("YES, phone > 1")
    if len(pro_data[a]['cards']) > 1:
        check.append("YES, cards > 1")
# print(check)
# print(check.count("YES, full_name > 1"))
# print(check.count("YES, phone > 1"))
# print(check.count("YES, pp > 1"))
# print(check.count("YES, client > 1"))
# print(check.count("YES, cards > 1"))
# print('-----------------------------------------------------------------------------------------------------------')
# for a in Acc:
#     print(len(pro_data[a]['full_name']))
#     print(len(pro_data[a]['pp']))
#     print(len(pro_data[a]['client']))
#     print(len(pro_data[a]['phone']))

## num_of_cards == num_of_phones == num_of_passports == num_of_clients == num_of_names == 1        FOR ALL THE ACCOUNTS

for a in Acc:
    print(pro_data[a]['oper'])


# class Transactions:
#     def __init__(self):
#         self.date =
#         self.card =
#         self.account =
#         self.account_valid_to =
#         self.client =
#         self.last_name =
#         self.first_name =
#         self.patronymic =
#         self.date_of_birth =
#         self.passport =
#         self.passport_valid_to =
#         self.phone =
#         self.oper_type =
#         self.amount =
#         self.oper_result =
#         self.terminal =
#         self.terminal_type =
#         self.city =
#         self.address =
