while (True):
  sentence = input()
  if sentence == '#':
    break
  cnt = 0
  for s in sentence:
    if s.lower() in set(['a', 'e', 'i', 'o', 'u']):
      cnt += 1
  print(cnt)