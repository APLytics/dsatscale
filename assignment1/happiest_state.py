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
            score = 0

            if 'location' in tweet.keys():
	        loc = tweet['location'].split(' ')
                state = 'none'
                for l in loc:
                    if l in states.keys():
			state = l
		    #elif l in states.values():
                    #    state = states_r[l]
                if state != 'none':

                    if 'text' in tweet.keys() :
                        text = tweet['text'].split(' ')
                        for word in text:
                            try:
                                score += scores[word]
                            except:
                                pass

                    try:
                        state_dic[state] += score
                    except:
                        state_dic[state] = score
    return state_dic

def main():
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
    states_r = {v:k for k,v in states.items()}
    scores = dict_sent(sys.argv[1])
    dic = compute_sent_state(sys.argv[2], scores)
    for k,v in dic.items():
        print(k,v)

if __name__ == '__main__':
    main()

