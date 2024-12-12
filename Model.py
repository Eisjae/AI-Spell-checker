from textblob import TextBlob
from language_tool_python import LanguageTool

class SpellCheckerModule:
    def __init__(self):
        self.grammar_check = LanguageTool('en-GB')

    def correct_spell(self, text):
        """
        Corrects the spelling of the input text while preserving the capitalization 
        of the first word and the rest of the sentence.
        """
        words = text.split()
        corrected_words = []

        for i, word in enumerate(words):
            # Correct the spelling of each word
            corrected_word = str(TextBlob(word).correct())

            # Capitalize the first word of the sentence, preserve others as is
            if i == 0:
                corrected_word = corrected_word.capitalize()
            else:
                corrected_word = corrected_word.lower()

            corrected_words.append(corrected_word)

        return " ".join(corrected_words)

    def correct_grammar(self, text):
        """
        Identifies grammar issues in the text and counts them.
        """
        matches = self.grammar_check.check(text)

        found_mistakes = []
        corrected_text = text
        for mistake in matches:
            # Apply grammar corrections directly
            corrected_text = LanguageTool.correct(text, matches)
            found_mistakes.append(mistake.ruleId)

        found_mistakes_count = len(found_mistakes)
        return corrected_text, found_mistakes, found_mistakes_count
