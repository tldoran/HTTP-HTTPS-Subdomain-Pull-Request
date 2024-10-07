import requests 

def request(url):
    try:    
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass



target_url = input("Enter a domain: ")

with open ("/Users/oran/Desktop/vscodeProjects/Vulnerability Testing/Directories_small.txt", "r") as word_list: # Include your wordlist file directory here
    for line in word_list:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] new subdomain found -->" + test_url)
