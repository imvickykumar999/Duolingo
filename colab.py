
# https://github.com/KartikTalwar/Duolingo/issues/128#issuecomment-1449474903

# import duolingo
# lingo  = duolingo.Duolingo('DuolingoAP218492', '**********')
# print(lingo)

# https://github.com/imvickykumar999/Duolingo#readme

import duolingo
myJWT = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjo4MjE0OTYyMTB9.NckmRCMJ7r62CU5XcXAjzaULVzOqyFuDP3PzfvR7hXs'
lingo  = duolingo.Duolingo(username='imvickykumar999', jwt=myJWT)

# print(lingo)
# <duolingo.Duolingo object at 0x000002223F6D0C40>

# print(lingo.get_user_info())
# ... too long answer


# print(lingo.get_languages(abbreviations=True))
# ['it', 'ko', 'ru', 'pt', 'vi', 'fr', 'de', 'hi', 'ja', 'ko', 'ar', 'uk']


# print(lingo.get_friends())


# print(lingo.get_streak_info())
# {'daily_goal': 20, 'site_streak': 5, 'streak_extended_today': False}


# print(lingo.get_leaderboard('week'))

# print(lingo.get_daily_xp_progress())

# print(lingo.buy_item('streak_freeze', 'en'))


my_lang = lingo.get_languages()
# print(my_lang)
# ['Italian', 'Spanish', 'Russian', 'Portuguese', 'Vietnamese', 'French', 'German', 'Hindi', 'Japanese', 'Korean', 'Arabic', 'Ukrainian']

from pprint import pprint
pprint(lingo.get_language_details('Korean'))

'''
{
 'current_learning': True,
 'language': 'ko',
 'language_string': 'Korean',
 'learning': True,
 'level': 5,
 'points': 373,
 'sentences_translated': 0,
 'streak': 6,
 'to_next_level': 77
}
'''


# for i in my_lang:
#     print(lingo.get_language_details(i))
    
'''
{'streak': 6, 'language_string': 'Italian', 'points': 27, 'learning': True, 'language': 'it', 'level': 1, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 33}
{'streak': 6, 'language_string': 'Spanish', 'points': 1550, 'learning': True, 'language': 'es', 'level': 8, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 100}
{'streak': 6, 'language_string': 'Russian', 'points': 1333, 'learning': True, 'language': 'ru', 'level': 8, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 317}
{'streak': 6, 'language_string': 'Portuguese', 'points': 55, 'learning': True, 'language': 'pt', 'level': 1, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 5}
{'streak': 6, 'language_string': 'Vietnamese', 'points': 30, 'learning': True, 'language': 'vi', 'level': 1, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 30}
{'streak': 6, 'language_string': 'French', 'points': 30, 'learning': True, 'language': 'fr', 'level': 1, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 30}
{'streak': 6, 'language_string': 'German', 'points': 50, 'learning': True, 'language': 'de', 'level': 1, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 10}
{'streak': 6, 'language_string': 'Hindi', 'points': 0, 'learning': True, 'language': 'hi', 'level': 1, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 60}
{'streak': 6, 'language_string': 'Japanese', 'points': 375, 'learning': True, 'language': 'ja', 'level': 5, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 75}
{'streak': 6, 'language_string': 'Korean', 'points': 373, 'learning': True, 'language': 'ko', 'level': 5, 'current_learning': True, 'sentences_translated': 0, 'to_next_level': 77}
{'streak': 6, 'language_string': 'Arabic', 'points': 32386, 'learning': True, 'language': 'ar', 'level': 25, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 2147451261}
{'streak': 6, 'language_string': 'Ukrainian', 'points': 533, 'learning': True, 'language': 'uk', 'level': 6, 'current_learning': False, 'sentences_translated': 0, 'to_next_level': 217}
'''

# print(lingo.get_language_progress('ko'))

# print(lingo.get_known_topics('ko'))
# []

# print(lingo.get_unknown_topics())

# print(lingo.get_golden_topics('ko'))
# []

# print(lingo.get_reviewable_topics('ko'))
# []

# print(lingo.get_known_words('ko'))
# []

# print(lingo.get_related_words('aller'))
# None

# print(lingo.get_learned_skills('ko'))
# []

# print(lingo.get_language_from_abbr('ko'))
# Korean

# print(lingo.get_abbreviation_of('Korean'))
# ko

# print(lingo.get_translations(['de', 'du'], source='de', target='fr'))


# print(lingo.get_vocabulary(language_abbr='ko'))
# {'language_string': 'Korean', 'learning_language': 'ko', 'from_language': 'en', 'language_information': {'pronoun_mapping': [], 'tenses': {}}, 'vocab_overview': []}


# print(lingo.get_language_voices('ko'))

# print(lingo.get_audio_url('bonjour'))
# https://d7mj4aqfscim2.cloudfront.net/tts/fr/token/bonjour
