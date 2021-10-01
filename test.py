from cowin_api import CoWinAPI
cowin = CoWinAPI()


stats = cowin.get_states()
print(stats)
