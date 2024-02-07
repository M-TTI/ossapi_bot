from ossapi import Ossapi

api = Ossapi(00000, 'mytoken XD')

print(api.user(19587231, mode="osu").username)
print(api.beatmap(221777).beatmapset_id)
scores = api.user_scores(19587231, "best")
for i in scores:
    print(i.pp)