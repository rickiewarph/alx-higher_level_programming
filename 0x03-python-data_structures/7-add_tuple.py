#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_q, len_p = len(tuple_a), len(tuple_b)
    m_tuple = ((tuple_a[0] if len_q >= 1 else 0) +
                 (tuple_b[0] if len_p >= 1 else 0),
                 (tuple_a[1] if len_q >= 2 else 0) +
                 (tuple_b[1] if len_p >= 2 else 0))
    return m_tuple
