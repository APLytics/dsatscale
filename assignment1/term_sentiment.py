import sys

def dict_sent(file):
    scores = dict()
    with open(file, "r") as fp:
        for line in fp.readlines():
            term, score = line.split("\t")
            scores[term] = int(score)
    return scores

def compute_new_term(file, scores):
    import json
    new_term = dict()
    with open(file, "r") as fp:
        for line in fp.readlines():
            tweet = json.loads(line)
            score = 0
            newlist = list()
            if 'text' in tweet.keys() :
                text = tweet['text'].split(' ')
                for word in text:
                    if not word.isalnum():
                        continue
                    try:
                        score += scores[word]
                    except:
                        newlist.append(word)

            for newword in newlist:
                try:
                    new_term[newword] += score
                except:
                    new_term[newword] = score
    return new_term

def print_new_term(dic):
    for k, v in dic.items():
        print k, v

def main():
    scores = dict_sent(sys.argv[1])
    dic = compute_new_term(sys.argv[2], scores)
    print_new_term(dic)

if __name__ == '__main__':
    main()
