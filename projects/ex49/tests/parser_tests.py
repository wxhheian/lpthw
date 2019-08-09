from nose.tools import *
from ex49.parser import *

word_listA = [('verb','kill'),('direction','north')]
def test_peek():
    result = peek(word_listA)
    assert_equal(result,'verb')

def test_match():
    result = match(word_listA,'verb')
    assert_equal(result,('verb','kill'))
    assert_equal(word_listA,[('direction','north')])

word_listB = [('stop','the'),('direction','north')]
def test_skip():
    result = skip(word_listB,'stop')
    assert_equal(result,None)
    assert(word_listB,[('direction','north')])

word_listC = [('verb','run'),('direction','north')]
def test_parse_verb():
    result = parse_verb(word_listC)
    assert_equal(result,('verb','run'))
    assert_raises(ParserError,parse_verb,[('stop','the'),('direction','north')])




def test_parse_subject():
    result = parse_subject([('verb','run'),('direction','north')])
    assert_equal(result,('noun','player'))
    result = parse_subject([('noun','bear'),('verb','eat'),('stop','the'),('noun','honey')])
    assert_equal(result,('noun','bear'))

def test_parse_object():
    result = parse_object([('stop','the'),('noun','door')])
    assert_equal(result,('noun','door'))
    assert_raises(ParserError,parse_object,[('stop','the'),('verb','run')])

def test_parse_sentence():
    result = parse_sentence([('verb','go'),('stop','the'),('noun','door')])
    assert_equal(result.subject,'player')
    assert_equal(result.verb,'go')
    assert_equal(result.obj,'door')
    assert_raises(ParserError,parse_sentence,[('stop','in'),('stop','the')])
