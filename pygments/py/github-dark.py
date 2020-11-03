# -*- coding: utf-8 -*-
"""
    Github Dark Colorscheme
    ~~~~~~~~~~~~~~~~

    Converted by Freedomsky
"""
from pygments.style import Style
from pygments.token import Token, Name, String, Comment, Operator, Keyword, Generic, Number

class GithubDarkStyle(Style):

    background_color = '#111111'
    styles = {
        Token:              'noinherit #d0d0d0 bg:#111111',
        Keyword.Type:       'noinherit #6ab825',
        Generic.Output:     'noinherit #cccccc',
        Number:             'noinherit #cd2828',
        Name.Exception:     'noinherit #bbbbbb',
        Generic.Error:      'noinherit #d22323',
        String:             'noinherit #d2691e',
        Comment:            'noinherit #3677a9',
        Comment.Preproc:    'noinherit #d2691e',
        Name.Function:      'noinherit #009988',
        Keyword:            'noinherit #cccccc',
        Name.Constant:      'noinherit #44ccaa',
        Name.Variable:      'noinherit #44ccaa',
        Name.Tag:           'noinherit #6ab825',
        Operator.Word:      'noinherit #6ab825',
        Name.Label:         'noinherit #d0d0d0',
        Name.Attribute:     'noinherit #bbbbbb',
        Name.Entity:        'noinherit #d0d0d0',
    }
