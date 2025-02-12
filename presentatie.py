def presenteer(dictionary, totaal):
    for key, value in dictionary.items():
        print(f"{key} : {value} euro")

    print("=" * 20)
    print(f"Totaal : {totaal} euro")

mijn_dict = {"vis": 10, "vlees": 25, "overige": 15}

if mijn_dict:
    presenteer(mijn_dict, sum(mijn_dict.values()))