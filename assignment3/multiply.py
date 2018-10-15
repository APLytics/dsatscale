import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
sz = 5
# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    pos = record[1:3]
    value = record[-1]
    if matrix == 'b':
        pos = pos[::-1]
        for s in range(sz):
            mr.emit_intermediate((s,pos[0]), (pos[1], value))
    else:
        for s in range(sz):
            mr.emit_intermediate((pos[0],s), (pos[1], value))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    print(key, list_of_values)
    dic = dict()
    for v in list_of_values:
        try:
            dic[v[0]] = [dic[v[0]][0]+1, dic[v[0]][1]*v[1]]
        except:
            dic[v[0]] = [0, v[1]]
    dic = {k:v[1] for k,v in dic.items() if v[0]==1}
    print(dic)
    mr.emit((key[0], key[1], sum(dic.values())))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
