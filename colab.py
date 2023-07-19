
# https://github.com/KartikTalwar/Duolingo/issues/128#issuecomment-1449474903

# import duolingo
# lingo  = duolingo.Duolingo('DuolingoAP218492', '**********')
# print(lingo)

# https://github.com/imvickykumar999/Duolingo#readme

import duolingo
myJWT = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMTMwNTk5NTQxfQ.r0Qg9T47LL-KkZbmTU863ywQZidSLVT2VHXSL0Nc0Xg'
lingo  = duolingo.Duolingo(username='DuolingoAP218492', jwt=myJWT)

print(lingo)
# <duolingo.Duolingo object at 0x000002223F6D0C40>

# print(lingo.get_user_info())

print(lingo.get_languages(abbreviations=True))
# ['es']

# print(lingo.get_friends())

print(lingo.get_streak_info())
# {'daily_goal': 20, 'site_streak': 0, 'streak_extended_today': False}

# print(lingo.get_leaderboard('week'))

# print(lingo.get_daily_xp_progress())

# print(lingo.buy_item('streak_freeze', 'en'))

print(lingo.get_languages())
# ['Spanish']

print(lingo.get_language_details('Spanish'))
# {'streak': 0, 'language_string': 'Spanish', 'points': 0, 'learning': True, 'language': 'es', 'level': 1, 'current_learning': True, 'sentences_translated': 0, 'to_next_level': 60}

# print(lingo.get_language_progress('es'))

print(lingo.get_known_topics('es'))
# []

# print(lingo.get_unknown_topics())

print(lingo.get_golden_topics('es'))
# []

print(lingo.get_reviewable_topics('es'))
# []

print(lingo.get_known_words('es'))
# []

print(lingo.get_related_words('aller'))
# None

print(lingo.get_learned_skills('es'))
# []

print(lingo.get_language_from_abbr('es'))
# Spanish

print(lingo.get_abbreviation_of('Spanish'))
# es

# print(lingo.get_translations(['de', 'du'], source='de', target='fr'))

print(lingo.get_vocabulary(language_abbr='es'))
# {'language_string': 'Spanish', 'learning_language': 'es', 'from_language': 'en', 'language_information': {'pronoun_mapping': [{'tenses': {'pri': 'present_indicative_first_person_singular'}, 'pronoun': 'yo'}, {'tenses': {'pri': 'present_indicative_second_person_singular_tu'}, 'pronoun': 'tú'}, {'tenses': {'pri': 'present_indicative_third_person_singular'}, 'pronoun': 'él/ella/usted'}, {'tenses': {'pri': 'present_indicative_first_person_plural'}, 'pronoun': 'nosotros/nosotras'}, {'tenses': {'pri': 'present_indicative_second_person_plural_vosotros'}, 'pronoun': 'vosotros/vosotras'}, {'tenses': {'pri': 'present_indicative_second_person_plural_ustedes'}, 'pronoun': 'ustedes'}, {'tenses': {'pri': 'present_indicative_third_person_plural'}, 'pronoun': 'ellos/ellas'}], 'tenses': {'indicative': [{'tense_string': 'Present', 'tense': 'pri'}]}}, 'vocab_overview': []}

# print(lingo.get_language_voices('es'))

print(lingo.get_audio_url('bonjour'))
# https://d7mj4aqfscim2.cloudfront.net/tts/fr/token/bonjour
