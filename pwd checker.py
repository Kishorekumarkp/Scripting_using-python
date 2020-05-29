import requests
import hashlib
import sys

def req_api(query_data):
    url = "https://api.pwnedpasswords.com/range/" + query_data
    res = requests.get(url)
    print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching : {res.status_code} , check the API and try again')
    return res

def get_pwd_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(pwd):
    #sha1_pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()) -- creates a HASH obj &
                                                                         #encodes into a format
                                                                       #then turns all into hexadecimal
                                                                        #convert all to uppercase
    sha1_pwd = hashlib.sha1(pwd.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_pwd[:5] , sha1_pwd[5:]
    response = req_api(first5_char)
    print(first5_char,tail)
    print(response)
    return get_pwd_leaks_count(response, tail)

def main(args):
    for pwd in args:
        count = pwned_api_check(pwd)
        if count:
            print(f"{pwd} was found {count} times you shld change your password")
        else:
            print(f'{pwd} was not found ! carry on!')
    return 'done'

if __name__ ==  '__main__':
    main(sys.argv[1:])
