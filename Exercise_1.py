def precision(tp, fp):
    return tp / (tp + fp)

def recall(tp, fn):
    return tp / (tp + fn)

def f1_score(precision, recall):
    return 2 * precision * recall / (precision + recall)

def exercise1(tp, fp, fn):
    # check tp, fp, fn whether an integer
    if type(tp) != int:
        print("tp must be int")
        return
    if type(fp) != int:
        print("fp must be int")
        return
    if type(fn) != int:
        print("fn must be int")
        return

    # check tp, fp, np must be greater than zero
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return

    p = precision(tp, fp)
    r = recall(tp, fn)

    print("precision is", p)
    print("recall is", r)
    print("f1_score is", f1_score(p, r))

if __name__ == "__main__":
    exercise1(tp=2, fp=3, fn=4)
    exercise1(tp='a', fp=3, fn=4)
    exercise1(tp=2, fp='a', fn=4)
    exercise1(tp=2, fp=3, fn='a')
    exercise1(tp=2, fp=3, fn=0)
    exercise1(tp=2.1, fp=3, fn=0)