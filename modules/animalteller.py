import subprocess

def animalteller(animal):
    the_quote = subprocess.call("fortune")
    # find_the_animal = subprocess.call("shuf", "-n1", "/usr/share/cowsay/cows")
    # str_animal = str(find_the_animal)
    # the_animal = str_animal[:-3]
    the_animal_whisperer = subprocess.call("cowsay", the_quote)