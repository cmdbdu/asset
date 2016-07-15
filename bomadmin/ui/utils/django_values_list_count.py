#!/usr/bin/env python
# coding:utf8
# By:dub


def count_list(arg):
    b = []
    c = []
    for i in range(len(arg)):
        tmp = arg[0]
        arg.pop(0)
        if tmp not in b:
            c.append(1)
            b.append(tmp)
        elif tmp in b:
            pos = b.index(tmp)
            c[pos] = c[pos] + 1
    d = []
    for i in range(len(b)):
        d.append((b[i],c[i]))

    tmp_d = {}
    for i in d:
        key = i[0][0]
        if tmp_d.has_key(key):
            tmp_d[key].update({i[0][1]:i[1]})
        else:
            tmp_d[i[0][0]]={i[0][1]:i[1]}
    return tmp_d


if __name__ == "__main__":
    a = [(u'hba', u'store'), (u'mem', u'store'), (u'ser', u'store'), (u'hba', u'store'), (u'ser', u'store'), (u'ser', 'inuse')]
    print count_list(a)



