# TextCleaner Plugin

TextCleaner is a Sublime Text 4 plugin that cleans up your document by performing several text transformations. It converts tabs to spaces, replaces invisible characters, standardizes quotes, trims extra whitespace, collapses multiple spaces, removes duplicate empty lines, and cleans up empty lines around brackets.

## Settings

You can customize which transformations are applied through the configuration file ([TextCleaner.sublime-settings](/TextCleaner.sublime-settings)). Below is a description of each setting:

- `expand_tabs`: Converts tab characters to spaces. This setting will replace all tabs with 4 spaces. Adjust tab_size if you prefer a different number of spaces.
- `replace_invisible_chars`: Replaces various invisible characters (like BOM, zero-width spaces, non-breaking spaces, etc.) with a regular space.
- `replace_fancy_quotes`: Replaces smart quotes, apostrophes, and guillemets with standard ASCII quotes. With this enabled, characters like `“ ”`, `‘ ’`, `« »`, etc., will be converted to plain double or single quotes.
- `trim_line_whitespace`: Removes extra spaces and tabs at the beginning and end of each line.
- `replace_multiple_spaces`: Replaces multiple consecutive spaces with a single space.
- `remove_duplicate_empty_lines`: Collapses duplicate empty lines so that there is at most one empty line in a row.
- `remove_empty_lines_around_brackets`: Removes empty lines immediately after an opening bracket (\(, \[, \{) and immediately before a closing bracket (\), \], \}).

Simply adjust the settings in the [TextCleaner.sublime-settings](/TextCleaner.sublime-settings) file to enable or disable specific transformations according to your needs. Enjoy a cleaner, more consistent code and text formatting in Sublime Text 4!

## License

This project is licensed under the [MIT License](/LICENSE.txt).

## Credits

Developed by Valentin Popov
E-Mail: [valentin@popov.link]