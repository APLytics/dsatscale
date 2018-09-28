import sys

def compute_term_frequency(file):
    import json
    new_term = dict()

    with open(file, "r") as fp:
        for line in fp.readlines():
            tweet = json.loads(line)

            if 'text' in tweet.keys() :
                text = tweet['text'].split(' ')
                for word in text:
                    if not word.isalnum():
                        continue
                    try:
                        new_term[word] += 1
                    except:
                        new_term[word] = 1

    N = float(sum(new_term.values()))

    new_term = { k: v/N for k, v in new_term.items()}
    return new_term

def print_new_term_freq(dic):
    for k, v in dic.items():
        print k, v

def main():
    
    dic = compute_term_frequency(sys.argv[1])
    print_new_term_freq(dic)

if __name__ == '__main__':
    main()
