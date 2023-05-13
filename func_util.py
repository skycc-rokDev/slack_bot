def func_usage() :
    string = ""
    string += "[usage]\n"
    string += "- my_info [your_mail] [your_pw]\n"
    string += "- add_friend [your_mail] [your_pw] [target_token]\n"
    string += "- del_friend [your_mail] [your_pw] [target_token]\n"
    return string

def func_my_info(full_query) :
    email = full_query[2]['url'].split("mailto:")[1]
    pw = full_query[3]['text'][1:]
    print(email)
    print(pw)
    string = "to do\n"
    string += ""
    return string

def func_add_friend(full_query) :
    email = full_query[2]['url'].split("mailto:")[1]
    tmp = full_query[3]['text'].split(" ")
    pw = tmp[1]
    target_token = tmp[2]
    print(email)
    print(pw)
    print(target_token)
    string = "to do\n"
    string += ""
    return string

def func_del_friend() :
    email = full_query[2]['url'].split("mailto:")[1]
    tmp = full_query[3]['text'].split(" ")
    pw = tmp[1]
    target_token = tmp[2]
    print(email)
    print(pw)
    print(target_token)
    string = "to do\n"
    string += ""
    return string

def func_not_command() :
    string = ""
    string += "command not found :)\n"
    string += "@inple_Bot help\n"
    return string