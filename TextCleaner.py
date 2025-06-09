import sublime
import sublime_plugin
import re

class TextCleanerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Load settings from the configuration file.
        settings = sublime.load_settings("TextCleaner.sublime-settings")

        # Get the entire document text.
        entire_region = sublime.Region(0, self.view.size())
        content = self.view.substr(entire_region)

        # Convert tabs to spaces if enabled.
        if settings.get("expand_tabs", True):
            tab_size = self.view.settings().get("tab_size", 4)
            content = content.expandtabs(tab_size)

        # Replace invisible characters with a space if enabled.
        if settings.get("replace_invisible_chars", True):
            invisible_chars_pattern = r'[\uFEFF\u200B\u200C\u200D\u00A0\u202F\u205F\u2060\u180E\u3000\u200E\u200F]'
            content = re.sub(invisible_chars_pattern, ' ', content)

        # Replace smart quotes, apostrophes, and guillemets with standard ASCII quotes if enabled.
        if settings.get("replace_fancy_quotes", True):
            content = (content.replace('“', '"')
                              .replace('”', '"')
                              .replace('‘', "'")
                              .replace('’', "'")
                              .replace('«', '"')
                              .replace('»', '"'))

        # Trim whitespace at the beginning and end of each line if enabled.
        if settings.get("trim_line_whitespace", True):
            content = re.sub(r'^[ \t]+|[ \t]+$', '', content, flags=re.MULTILINE)

        # Replace multiple consecutive spaces with a single space if enabled.
        if settings.get("replace_multiple_spaces", True):
            content = re.sub(r'[ ]{2,}', ' ', content)

        # Remove duplicate empty lines if enabled.
        if settings.get("remove_duplicate_empty_lines", True):
            content = re.sub(r'(?<=\S)\n{2,}(?=\S)', '\n\n', content).strip()

        # Remove empty lines immediately after opening brackets and before closing brackets if enabled.
        if settings.get("remove_empty_lines_around_brackets", True):
            content = re.sub(r'([(\[{])\n\s*\n+', r'\1\n', content)
            content = re.sub(r'\n\s*\n+([)\]}])', r'\n\1', content)

        # Replace the document text with the cleaned content.
        self.view.replace(edit, entire_region, content)
