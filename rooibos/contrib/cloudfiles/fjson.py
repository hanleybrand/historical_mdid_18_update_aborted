from tokenize import generate_tokens, STRING, NAME, OP
from cStringIO import StringIO
from re import compile, DOTALL

comments = compile(r'/\*.*\*/|//[^\r\n]*', DOTALL)


def _loads(string):
    """
    Fairly competent json parser exploiting the python tokenizer and eval()

    _loads(serialized_json) -> object
    """
    try:
        res = []
        consts = {'true': True, 'false': False, 'null': None}
        string = '(' + comments.sub('', string) + ')'
        for type, val, _, _, _ in generate_tokens(StringIO(string).readline):
            if (type == OP and val not in '[]{}:,()-') or \
                    (type == NAME and val not in consts):
                raise AttributeError()
            elif type == STRING:
                res.append('u')
                res.append(val.replace('\\/', '/'))
            else:
                res.append(val)
        return eval(''.join(res), {}, consts)
    except:
        raise AttributeError()

# look for a real json parser first
    ## but at this point there should never really be a need for
    ## the _loads function, since json is stdlib
try:
    from json import loads as json_loads
except ImportError:
    json_loads = _loads

__all__ = ['json_loads']

