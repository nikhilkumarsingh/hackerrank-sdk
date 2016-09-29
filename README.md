[![PyPI](https://img.shields.io/badge/PyPi-v1.2.1-f39f37.svg)](https://pypi.python.org/pypi/hackerrank-sdk)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/nikhilkumarsingh/hackerrank-sdk/blob/master/LICENSE.txt)


hackerrank-sdk
==============
An Unofficial Python Client that supports interaction with [HackerRank API](https://www.hackerrank.com/api/docs).

This SDK provides integration with HackerRank API for compiling and running code in several languages. It can be accessed via a simple API key based authorization process.[Get your api-key from here](https://www.hackerrank.com/api/docs).

The code is Python 2, but Python 3 compatible.


## Installation

Fast install:

    pip install hackerrank-sdk
    
For a manual install get this package:

    wget https://github.com/nikhilkumarsingh/hackerrank-sdk/archive/master.zip
    unzip master.zip
    rm master.zip
    cd hackerrank-sdk-master

Install the package:

    python setup.py install    
    
## Examples
```python
from hackerrank.HackerRankAPI import HackerRankAPI

API_KEY = ''  #your API-KEY here

compiler = HackerRankAPI(api_key = API_KEY)

print compiler.supportedlanguages()     #prints a list of supported languages


source = '''print "hello"'''    #give your source code here

'''
Alternatively,you can copy existing files to source this way:
with open(file_name,'r') as f:
     source = f.read()
'''     

result = compiler.run({'source': source,
                       'lang':'python'     
                       })
                       
                       
print(result.output,result.time,result.memory,result.message)    #get different variables associated with the result
```
Testcases are passed as a list of strings.

Here is another example which shows how to give testcases to the compiler:
```python
from hackerrank.HackerRankAPI import HackerRankAPI

API_KEY = ''  # Your API-KEY here

compiler = HackerRankAPI(api_key = API_KEY)

source ='''
N, M = map(int,raw_input().split()) 
for i in xrange(1,N,2): 
    print (".|."*i).center(M,'-')
    
print "WELCOME".center(M,'-')
for i in xrange(N-2,-1,-2): 
    print (".|."*i).center(M,'-') 
'''

result = compiler.run({'source': source,
                       'lang':'python',
                       'testcases':["9 27"]
                       })
                       
print(result.output[0])
```
Here is the output:

![output](http://i.imgur.com/D9vbr1Z.png)
