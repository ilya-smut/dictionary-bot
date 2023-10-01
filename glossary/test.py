from classes import Glossary

glossary = Glossary()

rules = glossary.Rules()
rules.set_limit_of_descriptions(1)
word = glossary.Word('cunt', rules)

print(word.get_word())
if word.exists():
    print(word.get_transcription())
    print(word.get_audio())
    for part_of_speech in word.get_parts_of_speech():
        print()
        print(part_of_speech)
        for definition in word.get_definitions_of_part_of_speech(part_of_speech):
            print(definition)
else:
    print('Word was not found')
