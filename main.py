import ossapi
import tkinter as tk

secret = input("enter token : ")

api = ossapi.Ossapi(30107, secret)

# print(api.user(19587231, mode="osu").username)
# print(api.beatmap(221777).beatmapset_id)
# scores = api.user_scores(19587231, "best")
# for i in scores:
#     print(i.pp)


window = tk.Tk()
username = tk.Label(text = f"username : {api.user(19587231, mode="osu").username}")
username.pack()

topplays = api.user_scores(19587231, "best")

tk.Label(text = f"top play : {topplays[0].beatmapset.title} {topplays[0].pp}pp").pack()
window.mainloop()