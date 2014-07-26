def overwrite(base, head, _schema):
    return head

def version(base, head, _schema):
    if base is None:
        base = []
    else:
        base = list(base)

    base.append({'value': head})
    return base

def append(base, head, _schema):
    if base is None:
        base = []
    else:
        base = list(base)

    base += head
    return base

def map_merge(base, head, _schema):
    if base is None:
        base = {}
    else:
        base = dict(base)

    base.update(head)
    return base