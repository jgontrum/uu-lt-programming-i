from itertools import chain

def combine_dicts(d1, d2):
  ret = {}
  for key in set(chain(d1.keys(), d2.keys())):
    d1_value = d1.get(key)
    d2_value = d2.get(key)
    
    if d1_value == d2_value:
      ret[key] = d1_value
    elif d1_value is None:
      ret[key] = d2_value
    elif d2_value is None:
      ret[key] = d1_value
    else:
      ret[key] = (d1_value, d2_value)

  return ret


def test_combine_dicts():
  # Distinct dicts
  assert combine_dicts(
    {1: 0}, {'a': 0}) == \
    {1: 0, 'a': 0}

  # key collision - match
  assert combine_dicts(
    {1: 0}, {1: 0}) == {1: 0}

  # key collision - mismatch
  assert combine_dicts(
    {1: 0}, {1: 1}) == {1: (0, 1)}
