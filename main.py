import pandas as pd

df = pd.DataFrame(columns=["label", "message"])
with open("SMSSpamCollection", 'r') as file:
    for line in file.readlines():
        parts = line.strip().split()
        df = pd.concat([df, pd.DataFrame([{"label": parts[0], "message": ' '.join(parts[1:])}], index=[0])], ignore_index=True)


