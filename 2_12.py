def change_markdown():
    with open('text.md', 'r', encoding='utf-8') as f:
        str = f.read()
    flag = True
    for i in range(len(str)):
        if (str[i] == '"' or str[i] == "'") and flag == True:
            if str[i] == '"':
                str = str.replace('"', '«', 1)
            else:
                str = str.replace("'", '«', 1)
            flag = False
        elif (str[i] == '"' or str[i] == "'") and flag == False:
            if str[i] == '"':
                str = str.replace('"', '»', 1)
            else:
                str = str.replace("'", '»', 1)
            flag = True
        else:
            continue
    with open("text_1.md", 'w', encoding='utf-8') as f:
        f.write(str)
    return True


change_markdown()
