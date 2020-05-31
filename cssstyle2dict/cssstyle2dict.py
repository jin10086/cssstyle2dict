import cssutils
from collections import defaultdict


def styleParsel(css: str) -> dict:
    """
    css style to dict

    For example:

    >>> from cssstyle2dict import styleParsel
    >>> css = '.a { float:left } .b { margin-right:-1em } .c { float:left } .a { position:relative }'
    >>> style_dict = styleParsel(css)
    >>> print(style_dict)
    {'a': {'float': 'left', 'position': 'relative'},
    'b': {'margin-right': '-1em'},
    'c': {'float': 'left'}}


    """
    p = defaultdict(dict)
    sheet = cssutils.parseString(css)
    for rule in sheet:
        selector = rule.selectorText
        if selector.startswith("."):
            selector = selector[1:]
        v = dict(rule.style)
        p[selector].update(v)
    return dict(p)
