#Fun combining languages!
def greet(lang):
	if lang == 'es':
		return 'Hola'
	elif lang == 'fr':
		return 'Bonjour'
	else:
		return 'Hello'

print greet('en'), "Vincent"
print greet('es'), "Fate"
print greet('fr'), "Jackie"
