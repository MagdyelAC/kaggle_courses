def purple_shell(racers):
    
    racers[0],racers[-1]=racers[-1],racers[0]
    pass

r = ["Max", "Luis", "Dan"]
print(r)
print(purple_shell(r))