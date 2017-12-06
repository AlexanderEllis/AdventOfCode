
def passphrase_validator():

    passphrases = []
    with open('day4.txt') as data:
        for line in data:
            passphrases.append(line)

    total = 0
    # loop through passphrases
    # for each, build dict, if already in, continue
    # otherwise increment
    for passphrase in passphrases:
        words = {}
        valid = True
        for word in passphrase.split():
            if word not in words:
                words[word] = True
            else:
                valid = False
        if valid:
            total += 1

    print(total)
    return total

passphrase_validator()

