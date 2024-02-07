from ossapi import Ossapi

secret = input("enter token : ")

api = Ossapi(30107, secret)

print(api.user(19587231, mode="osu").username)
print(api.beatmap(221777).beatmapset_id)
scores = api.user_scores(19587231, "best")
for i in scores:
    print(i.pp)