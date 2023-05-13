#tmp
from func_request import *
host = "https://vpqbagk.request.dreamhack.games"

def func_usage() :
    string = ""
    string += "[usage]\n"
    string += "- my_info [your_mail] [your_pw]\n"
    string += "- add_friend [your_mail] [your_pw] [target_token]\n"
    string += "- del_friend [your_mail] [your_pw] [target_token]\n"
    return string

def func_my_info(full_query) :
    try :
        email = full_query[2]['url'].split("mailto:")[1]
        pw = full_query[3]['text'][1:]
        data = {'email' : email, 'pw' : pw}
        url = host + "/info"
        status = post_request(url, data)
        if (status == 200) :
            return "[+] success"
        return "[-] fail :("
    except :
        return "[-] fail :("
'''
method : post
url : example.com/info
data : {'email':email, 'pw':pw}

expect response :
success -> 200 code
fail -> other else
'''

def func_add_friend(full_query) :
    try :
        email = full_query[2]['url'].split("mailto:")[1]
        tmp = full_query[3]['text'].split(" ")
        pw = tmp[1]
        target_token = tmp[2]
        data = {'email' : email, 'pw' : pw, 'target_token' : target_token}
        url = host + "/add_friend"
        status = post_request(url, data)
        if (status == 200) :
            return "[+] success"
        return "[-] fail :("
    except :
        return "[-] fail :("
'''
method : post
url : example.com/add_friend
data : {'email':email, 'pw':pw, 'target_token':target_token}

expect response :
success -> 200 code
fail -> other else
'''

def func_del_friend(full_query) :
    try :
        email = full_query[2]['url'].split("mailto:")[1]
        tmp = full_query[3]['text'].split(" ")
        pw = tmp[1]
        target_token = tmp[2]
        data = {'email' : email, 'pw' : pw, 'target_token' : target_token}
        url = host + "/del_friend"
        status = post_request(url, data)
        if (status == 200) :
            return "[+] success"
        return "[-] fail :("
    except :
        return "[-] fail :("
'''
method : post
url : example.com/del_friend
data : {'email':email, 'pw':pw, 'target_token':target_token}

expect response :
success -> 200 code
fail -> other else
'''


def func_not_command() :
    string = ""
    string += "command not found :)\n"
    string += "@inple_Bot help\n"
    return string