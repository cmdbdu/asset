#!/usr/bin/env python
# coding:utf8
# By:dub

import json

def count_list(arg):
    model= {}
    for i in range(len(arg)):
        tmp = arg[0]
        arg.pop(0)
        if model.has_key(tmp[0]):
            if  model[tmp[0]].has_key(tmp[1]):
                model[tmp[0]][tmp[1]].append(tmp[2])
            else:
                model[tmp[0]][tmp[1]]=[tmp[2]]
        else:
            model[tmp[0]]={tmp[1]:[tmp[2]]}
    return model

if __name__ == "__main__":
    a = [(u'hba', u'store','12345'), (u'mem', u'store','22345'), (u'ser', u'store','32324'), (u'hba', u'inuse','232'), (u'ser', u'store','222'), (u'ser', 'inuse','222')]
    print count_list(a)
