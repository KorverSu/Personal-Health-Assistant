from pygsheets import *

gc = authorize(service_account_file='/usr/local/key/key.json')

survey_url = 'https://docs.google.com/spreadsheets/d/15itZjjw2Sy29Hhn7uuiy5ctk0TlGv39Y9a6Y5uRADcc/edit#gid=0'
sh = gc.open_by_url(survey_url)
logTable = sh.worksheet_by_title(title='工作表6')
msgTable = sh.worksheet_by_title(title='工作表7')


def sendLog(action, user_id):
    counter = 1
    for row in logTable:
        counter += 1
    action_index = 'A' + str(counter)
    id_index = 'B' + str(counter)
    logTable.update_value(action_index, action)
    logTable.update_value(id_index, user_id)


def write_msg(msg, user_id):
    sendLog('write_msg', user_id)
    counter = 1
    for row in msgTable:
        counter += 1
    msg_index = 'A' + str(counter)
    id_index = 'B' + str(counter)
    msgTable.update_value(msg_index, msg)
    msgTable.update_value(id_index, user_id)


def read_msg(user_id):
    sendLog('read_msg', user_id)
    action_count = 0
    for row in logTable:
        if row[0] != 'read_msg':
            continue
        else:
            if row[1] == str(user_id):
                action_count += 1
    print(action_count)
    temp = 0
    for rows in msgTable:
        if temp < action_count:
            if rows[1] != str(user_id):
                temp += 1
            else:
                continue
        elif temp == action_count:
            if rows[1] != str(user_id):
                msg = str(rows[0])
                return msg
                break

            else:
                continue
        else:
            return '沒有訊息了!'
            break

    if temp < action_count:
        return '沒有訊息了!'




def returnAndCount(key):
    wks_list = sh.worksheets()
    print(wks_list)
    ws = sh.worksheet_by_title(title='工作表1')
    val = ws.get_value('A1')
    num = 0
    print(num)
    '''for i in ws:
        num += 1
        print(i[0])
        if i[0] == key:
            index = 'C' + str(num)
            print(index)
            if ws.get_value(index) != '':
                value = int(ws.get_value(index)) + 1
                ws.update_value(index, value)
            else:
                ws.update_value(index, 1)
        else:
            print('沒有此功能')'''

#write_msg('aa', 12321)
# print(read_msg(1234))
