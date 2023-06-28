times = ("corinthinans" , "palmeiras" , "santos" , "Gremio" ,
         "cruzeiro" , "flamengo" , "vasco" , "chapecoense" ,
         "atletico", "botafogo" , "atleco-pr" , "bahia" ,
         "São paulo" , "fluminense" , "sport" , "vitoria" , "coritiba" , "avaí" , "ponte preta" ,
         "atletico-go")
print("-="*20)
print(f"lista de times do brasileirão: {times}")
print("-="*20)
print(f"os 5 primeiros são {times[0:5]}")
print("-="*20)
print(f"times em ordem alfabética: {sorted(times)}")
print("-="*20)
print(f"Os 4 ultimos são {times[-4:]}")
print("-="*20)
print(f"O chapecoense está na {times.index('chapecoense')}")
