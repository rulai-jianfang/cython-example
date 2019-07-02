#!/usr/bin/env python
import itertools
import re

def main():
  DATA = ["image_0001", "image_0002", "image_0003",
          "image_0010", "image_0011",
          "image_0011-1", "image_0011-2", "image_0011-3",
          "image_0100", "image_9999"]

  def extract_number(myname):
      return re.findall(r"\d+$",myname)[0]

  def collapse_group(group):
      if len(group) == 1:
          return group[0][1]
      first = extract_number(group[0][1])
      last  = extract_number(group[-1][1])

      length = len(str(int(last)))

      return "%s[%s-%s]" % (group[0][1][:-length],first[-length:],last[-length:])

  groups = [collapse_group(tuple(group)) for key, group in itertools.groupby(enumerate(DATA),lambda x:x[0] - int(extract_number(x[1])))]
  for i  in groups:
      print i

if __name__ == "__main__":
    main()
