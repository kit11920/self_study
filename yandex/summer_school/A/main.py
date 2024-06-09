import json

VOWELS = ['a', 'o', 'e', 'i', 'u', 'y', 'A', 'O', 'E', 'I', 'U', 'Y']


def act_10(line):
    out = list()
    for phrase in line:
        vowels = set()
        for a in set(phrase):
            if a in VOWELS:
                vowels.add(a)
        if len(vowels) >= 2:
            out.append(phrase)
    out.sort(reverse=True)
    return out


def act_20(line):
    out = list()
    for phrase in line:
        if len(phrase) % 2 == 0:
            out.append(phrase)
    out.sort(reverse=True)
    return out


def act_30(line):
    line.sort(reverse=True)
    return line


def main():
    output = dict()
    filename = input()
    # filename = 'sample_1.json'

    with open(filename, 'r') as f:
        data = json.load(f)
        # print(data)
    llen = max(map(int, data.keys()))
    # print(llen)

    for i in range(llen):
        line = input().split('_')
        key = str(i + 1)
        if key in data.keys():
            if data[key] == '10':
                changed = act_10(line)
            elif data[key] == '20':
                changed = act_20(line)
            else:
                changed = act_30(line)
            if key not in output.keys():
                output[key] = changed
            else:
                output[key].extend(changed)

    with open('output.json', 'w') as f:
        json.dump(output, f)
    # print(output)


main()
