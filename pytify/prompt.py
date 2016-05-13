from __future__ import unicode_literals
import getpass
import os
from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict


history = FileHistory('.pytify-search-history')

style = style_from_dict({
    # User input.
    # Token:          '#ff0066',

    # Prompt.
    Token.Username:  '#81b71a italic',
    Token.At:        '#999999',
    Token.Host:      '#81b71a',
    Token.Separator: '#81b71a',
    Token.Text:      '#e6e6e6',
    Token.Arrow:     '#999999',

    # Make a selection reverse/underlined.
    # (Use Control-Space to select.)
    Token.SelectedText: 'reverse underline',

    Token.Toolbar: '#e6e6e6 bg:#262626',
})


def get_bottom_toolbar_tokens(cli):
    return [
        (Token.Toolbar, ' exit: ctrl+d | clear: ctrl+c ')
    ]

def get_prompt_tokens(cli):
    return [
        (Token.Username,  getpass.getuser()),
        (Token.At,        '@'),
        (Token.Host,      os.uname()[1]),
        (Token.Separator, ' :: '),
        (Token.Text,      'What artist / song are you searching for?'),
        (Token.Arrow,     '\n> '),
    ]

def custom_prompt():
    return prompt(
        get_prompt_tokens=get_prompt_tokens,
        history=history,
        auto_suggest=AutoSuggestFromHistory(),
        enable_history_search=True,
        on_abort=AbortAction.RETRY,
        get_bottom_toolbar_tokens=get_bottom_toolbar_tokens,
        style=style
    )
