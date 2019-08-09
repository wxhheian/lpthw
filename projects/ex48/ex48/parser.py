class ParserError(Exception):           #自定义异常，父类是Exception
    pass


class Sentence(object):

    def __init__(self,subject,verb,obj):   #主语，谓语，宾语
    #remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj = obj[1]

def peek(word_list):                      ##返回第一个元组的第一个词性
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list,expecting):              #如果词性与预期的词性相同，则返回该元组
    if word_list:
        word = word_list.pop(0)                ###将word_list的第一个元素移除，会改变word_list

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list,word_type):                   #当list第一个元素是('stop','the')，则通过match()函数中的pop方法移除第一个元素
    while peek(word_list) == word_type:             #注意这里是一个循环
        match(word_list,word_type)


def parse_verb(word_list):
    skip(word_list,'stop')

    if peek(word_list) == 'verb':
        return match(word_list,'verb')
    else:
        raise ParserError("Expected a verb next")

def parse_object(word_list):
    skip(word_list,'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list,'noun')
    elif next_word == 'direction':
        return match(word_list,'direction')
    else:
        raise ParserError("Expected a noun or direction next")

def parse_subject(word_list):
    skip(word_list,'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list,'noun')
    elif next_word == 'verb':
        return ('noun','player')
    else:
        raise ParserError("Expected a verb next")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj,verb,obj)



#在ex48目录下进入python3.6
#>>>from ex48 import lexicon
#>>>from ex48.parser import *
#>>>x = parse_sentence([('verb','run'),('direction','north')])
#>>>x.subject
#>>>x.obj
#>>>x.verb
