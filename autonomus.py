from glossary.classes import Glossary

glossary = Glossary()
rules = glossary.Rules()
rules.set_limit_of_descriptions(10)

while True:
    input_word = input('Enter the word: ')
    if input_word == 'E':
        break
    word = glossary.Word(input_word, rules)
    if word.exists():
        print(word.get_transcription())
        print(word.get_audio())
        for part_of_speech in word.get_parts_of_speech():
            print('-------' + part_of_speech + '-------')
            for definition in word.get_definitions_of_part_of_speech(part_of_speech):
                print(definition)
        print()