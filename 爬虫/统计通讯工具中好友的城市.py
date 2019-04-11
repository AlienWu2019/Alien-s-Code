import itchat
import pandas as pd

itchat.login()
friends = itchat.get_friends(update=True)
df_friends = pd.DataFrame(friends)

City = df_friends.City

City_count = City.value_counts()

City_count = City_count[City_count.index !='']

print(City_count)
