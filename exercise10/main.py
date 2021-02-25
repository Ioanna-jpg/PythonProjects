
def dict_depth(dic, level=1):
input(dict_depth(dic, level=1))
    if not isinstance(dic, dict) or not dic:
        return level
    return max(dict_depth(dic[key], level + 1)
               for key in dic)


# Driver code
dic = {1: 'a', 2: {3: {4: {}}}}

print(dict_depth(dic))