import sys

def dict_sent(file):
    scores = dict()
    with open(file, "r") as fp:
        for line in fp.readlines():
            term, score = line.split("\t")
            scores[term] = int(score)
    return scores

def compute_sent_state(file, scores):
    import json
    state_dic = dict()
    with open(file, "r") as fp:
        for line in fp.readlines():
            tweet = json.loads(line)
            
            state = get_tweet_location(tweet)
            if state != 'none':
                score = get_tweet_sentiment(tweet, scores)
                
                state_dic[state] = score if state not in state_dic.keys() \
                    else score + state_dic[state]
        
    return state_dic
def get_tweet_location(tweet):
    states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
    }
    try:
        loc = tweet['place']['full_name'].split(', ')
        for l in loc:
            if l[:2] in states.keys():
                return l[:2]
    except:
        pass
    return 'none'

def get_tweet_sentiment(tweet, scores):
    score = 0
    if 'text' in tweet.keys() :
        text = tweet['text'].split(' ')
        for word in text:
            if not word.isalnum():
                continue
            try:
                 score += scores[word]
            except:
                pass
    return score


def main():
    #states_r = {v:k for k,v in states.items()}
    scores = dict_sent(sys.argv[1])
    dic = compute_sent_state(sys.argv[2], scores)
    it = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    print it[0][0]

if __name__ == '__main__':
    main()

