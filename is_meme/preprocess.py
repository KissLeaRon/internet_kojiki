import re
from sign_in import sign_in
import tweepy
import pandas as pd
import random

pat_url = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
pat_scr = "@\w+ "

def annotate(i,kojiki):
  pos = kojiki[i*100:(i+1)*100]
  out = []
  count = 1 + i*100
  for t in pos:
    print("------------",count)
    print(t)
    yn = input("\n")
    if yn == "exit":
      break
    elif yn == "d":
      out.append((repr(t),0))
    elif yn == "s":
      out.append((repr(t),1))
    count += 1
  df = pd.DataFrame(out,columns=["text","label"])
  df.to_csv("is_meme{}.csv".format(i+1),index=False)

api = sign_in()
kojiki = [s.text for s in tweepy.Cursor(api.search,q=["古事記","書いて"],count = 20).items()]
kojiki = [t for t in kojiki if t.find("RT @") == -1]
kojiki = [re.sub(pat_url,"",t) for t in kojiki]
kojiki = [re.sub(pat_scr,"",t) for t in kojiki]
print(len(kojiki))
random.shuffle(kojiki)
for i in range(5):
  annotate(i,kojiki)

