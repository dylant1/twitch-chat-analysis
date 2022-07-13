import pandas as pd

def access_chat(file):
    data = []
    tmp = {}
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().split('\n')

        for line in lines:
            words = line.split(" ")
            for word in words:
                try:
                    data.append(word)
                except Exception:
                    pass
    tmp["messages"] = data
    return pd.DataFrame(tmp)
df = access_chat("chat.log")
# n highest occuring words
n = 25
df2 = pd.DataFrame(df.value_counts()[:n])
df2.to_csv("occurences.csv",  encoding='utf-8')
