"""
Есть произвольно задаваемый основной отрезок A-B, и есть N - количество произвольно задаваемых доп. отрезков.
Необходимо вычислить длину основного отрезка, на которой не происходит наложения дополнительных отрезков.
"""
ab = [[15, 165]]
n = [[37, 68], [52, 74], [118, 146], [35, 44], [37, 65], [46, 74]]


def cut_segment_from_segment_sequence(seg_seq, seg):
    for s in seg_seq:
        # s полностью внутри seg
        if seg[0] <= s[0] <= s[1] <= seg[1]:
            seg_seq.remove(s)
        # seg частично левым краем внутри s
        elif s[0] <= seg[0] <= s[1] <= seg[1]:
            s[1] = seg[0]
        # seg частично правым краем внутри s
        elif seg[0] <= s[0] <= seg[1] <= s[1]:
            s[0] = seg[1]
        # seg полностью внутри s
        elif s[0] <= seg[0] <= seg[1] <= s[1]:
            seg_seq.remove(s)
            seg_seq.append([s[0], seg[0]])
            seg_seq.append([seg[1], s[1]])


def non_intersecting_segment_sequence_len(seg_seq):
    length = 0
    for s in seg_seq:
        length += s[1] - s[0]
    return length


for seg in n:
    cut_segment_from_segment_sequence(ab, seg)
print(non_intersecting_segment_sequence_len(ab))
