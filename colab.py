
# https://github.com/KartikTalwar/Duolingo/issues/128#issuecomment-1449474903

# import duolingo
# lingo  = duolingo.Duolingo('DuolingoAP218492', '**********')
# print(lingo)

import duolingo
myJWT = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMTMwNTk5NTQxfQ.r0Qg9T47LL-KkZbmTU863ywQZidSLVT2VHXSL0Nc0Xg'
lingo  = duolingo.Duolingo(username='DuolingoAP218492', jwt=myJWT)

print(lingo)
# <duolingo.Duolingo object at 0x000002223F6D0C40>
