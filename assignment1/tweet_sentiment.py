import sys

def dict_sent(file):
    scores = dict()
    with open(file, "r") as fp:
        for line in fp.readlines():
            term, score = line.split("\t")
	    scores[term] = int(score)
    return scores

def compute_sent_tweet(file, scores):
    import json

    with open(file, "r") as fp:
        for line in fp.readlines():
            tweet = json.loads(line)
            score = 0
            if 'text' in tweet.keys() :
                text = tweet['text'].split(' ')
                for word in text:
                    try:
                        score += scores[word]
                    except:
                        pass
            print(score)

def main():
    scores = dict_sent(sys.argv[1])
    compute_sent_tweet(sys.argv[2], scores)


if __name__ == '__main__':
    main()
