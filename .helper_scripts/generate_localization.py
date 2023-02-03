import os
from utils.utils import save_file_pdx

localization_path = "subject_manager/localization"

english_localization_path = os.path.join(localization_path, "english")
other_languages = [
    "braz_por",
    "french",
    "german",
    "polish",
    "russian",
    "spanish",
    "japanese",
    "simp_chinese",
    "korean",
    "turkish",
]

language_paths = {}
for language in other_languages:
    language_paths[language] = os.path.join(localization_path, language)
    if not os.path.exists(language_paths[language]):
        os.mkdir(language_paths[language])

for file in os.listdir(english_localization_path):
    input_filepath = os.path.join(english_localization_path, file)
    with open(input_filepath) as input_file:
        input = input_file.readlines()
        for language in other_languages:
            input[0] = f"l_{language}:\n"
            output_filepath = os.path.join(language_paths[language], file.replace("english", language))
            save_file_pdx(output_filepath, "".join(input))
