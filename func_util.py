#tmp
from func_request import *
host = "http://13.125.208.1:3000"

def func_usage() :
    string = ""
    string += "[usage]\n"
    string += "- my_info [your_mail] [your_pw]\n"
    string += "- add_friend [your_mail] [your_pw] [target_token]\n"
    string += "- del_friend [your_mail] [your_pw] [target_token]\n"
    string += "- register [your_mail] [your_pw]\n"
    string += "- card_add [your_main] [your_pw] [email2] [name] [company] [phone] [address] [site] [role]\n"
    string += "- card_delete [your_mail] [your_pw]\n"
    return string

def func_card_del(full_query) :
    email = full_query[2]['url'].split("mailto:")[1]
    pw = full_query[3]['text'][1:]
    token = get_my_token(email, pw.split(" ")[0])
    print("token : " + token)
    url = host + "/card/delete"
    status = delete_request_token(url, token)
    if (status == 200) :
        return "[+] success"
    return "[-] fail :("

def func_card_add(full_query) :
    try :
        print(full_query)
        email = full_query[2]['url'].split("mailto:")[1]
        pw = full_query[3]['text'][1:]
        token = get_my_token(email, pw.split(" ")[0])
        print("token : " + token)
        email2 = full_query[4]['text']
        tmp = full_query[5]['text'].split(" ")
        name = tmp[1]
        company = tmp[2]
        phone = tmp[3]
        address = tmp[4]
        site = full_query[6]['text'].split(" ")[0]
        role = full_query[7]['text'].split(" ")[1]
        data = {'name':name, 'company':company, 'phone':phone, 'address':address, 'site':site, 'role':role, 'email2':email2}
        url = host + "/card/add"
        status = post_request_token(url, data, token)
        if (status == 200) :
            return "[+] success"
        return "[-] fail :("
    except :
        return "[-] fail :("


def func_my_info(full_query) :
    try :
        email = full_query[2]['url'].split("mailto:")[1]
        pw = full_query[3]['text'][1:]
        token = get_my_token(email, pw)
        print(token)
        url = host + "/card/mycard"
        data = {"data" : "data"}
        status, response = get_request_token(url, token)
        if (status == 200) :
            response = json.loads(response)
            print(response)
            string = ""
            string += "email : " + response['data']['email']+"\n"
            string += "email2 : " + response['data']['email2']+"\n"
            string += "company : " + response['data']['company']+"\n"
            string += "name : " + response['data']['name']+"\n"
            string += "phone : " + response['data']['phone']+"\n"
            string += "site : " + response['data']['site']+"\n"
            string += "address : " + response['data']['address']+"\n"
            return string
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
    #try :
    email = full_query[2]['url'].split("mailto:")[1]
    tmp = full_query[3]['text'].split(" ")
    print(tmp)
    pw = tmp[1]
    print(email)
    print(pw)
    token = get_my_token(email, pw)
    print(token)
    target_email = full_query[4]['url'].split("mailto:")[1]
    url = host + "/relation/add"
    data = {"email":target_email}
    status = post_request_token(url, data, token)
    if (status == 200) :
        return "[+] success"
    #    return "[-] fail :("
    #except :
    #    return "[-] fail :("
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

def func_register(full_query) :
    try :
        email = full_query[2]['url'].split("mailto:")[1]
        pw = full_query[3]['text'][1:]
        data = {'email' : email, 'password' : pw}
        print(pw)
        print(data)
        print(email)
        url = host + "/auth/register"
        status = post_request(url, data)
        print(status)
        if (status == 200) :
            return "[+] success"
        return "[-] fail :("
    except :
        return "[-] fail :("

'''
method : post
url : http://13.125.208.1:3000/auth/register
data : {'email':email, 'password':pw}

expect response :
success -> 200 code
{
	status: statuscode,
	messgae: "messgae",
	token : "YOUR_JWT_TOKEN"
}

fail -> other else
'''

def func_not_command() :
    string = ""
    string += "command not found :)\n"
    string += "@inple_Bot help\n"
    return string