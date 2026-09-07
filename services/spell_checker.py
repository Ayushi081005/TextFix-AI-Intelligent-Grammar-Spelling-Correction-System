import language_tool_python


class SpellChecker:

    def __init__(self):
        print("Starting LanguageTool...")

        self.tool = language_tool_python.LanguageTool("en-US")

        print("LanguageTool is ready.")

    def analyze(self, text):

        matches = self.tool.check(text)

        corrected_text = self.tool.correct(text)

        errors = []

        for index, match in enumerate(matches):

            errors.append({
                "id": index,
                "message": match.message,
                "suggestions": match.replacements[:5],
                "offset": match.offset,
                "length": match.error_length,
                "rule": match.rule_id,
                "category": match.category
            })

        spelling_errors = 0
        grammar_errors = 0

        for match in matches:

            if match.category == "TYPOS":
                spelling_errors += 1
            else:
                grammar_errors += 1

        return {
            "original_text": text,
            "corrected_text": corrected_text,
            "errors": errors,
            "total_errors": len(matches),
            "spelling_errors": spelling_errors,
            "grammar_errors": grammar_errors
        }


spell_checker = SpellChecker()