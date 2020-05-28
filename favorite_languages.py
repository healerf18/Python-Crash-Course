favorite_languages = {'jen':'python', 
                      'sarah':'C', 
                      'edward':'ruby', 
                      'phil':'python',
                     }

friends = ['sarah', 'edward', 'erin']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}!")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()} I see you love {language}!")

for friend in friends:
    
    if friend not in favorite_languages.keys():
        print(f"\n{friend.title()}, tell us your fav...")
