def show_team(teams_name, **kwargs):
    print(f"Team: {teams_name}")

    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

show_team("team 9", Product_Owner= "Kacper", Manager= "Filip",
          Programmer = "Jacek")


