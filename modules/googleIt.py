import subprocess

def googleit(search):
    if "lol" in search:
        random = subprocess.call(["shuf", "-n1", "/usr/share/dict/american-english"])
        str_random = str(random)
        the_search = subprocess.call(["googler", str_random])
    else:
        the_word = str(search)
        the_real_search = subprocess.call(["googler", the_word])