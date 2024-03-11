# A. Покраска деревьев

p, v = map(int, input().split())
q, m = map(int, input().split())

ps, pe = p - v, p + v
qs, qe = q - m, q + m

# ps <= qs always
if ps > qs:
    ps, qs = qs, ps
    pe, qe = qe, pe

if pe < qs:
    trees = (pe - ps + 1) + (qe - qs + 1)
elif pe <= qe:
    trees = qe - ps + 1
else:
    trees = pe - ps + 1
print(trees)

