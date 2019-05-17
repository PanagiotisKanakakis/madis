def unistr(s):
    import types
    if type(s) == str:
        # return unicode(s, 'utf-8')
        return str(s).encode('utf-8')
    # if type(s) == types.UnicodeType:
    else:
        return s
    # else:
    #     return str(s).encode('utf-8')
