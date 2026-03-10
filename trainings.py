import json

from utils import load_trainings

def add_training(login):
    from datetime import datetime
    trainings = load_trainings()

    while True:
        try:
            training_date = str(input("Podaje datę treningu (YYYY-MM-DD): "))
            datetime.strptime(training_date, "%Y-%m-%d") # ta funkcja pozwala nam
            break
        except:
            print("Podano niepoprawny format daty ❌")
    while True:
        try:
            training_distance = int(input("Podaj dystans treningu (m): "))
            break
        except ValueError:
            print("Podaj liczbę!")
    while True:
        try:
            training_time = int(input("Podaj długość treningu (min): "))
            break
        except ValueError:
            print("Podaj liczbę!")
    if login not in trainings:
        trainings[login] = []
    training = [training_date, training_distance, training_time]
    trainings[login].append(training)
    try:
        with open ("data/trainings.json", "w") as file:
            json.dump(trainings, file, indent=4)
    except FileNotFoundError:
        return
    print("Trening został dodany ✅")

def show_trainings(login):
    trainings = load_trainings()

    if login in trainings and trainings[login]:
        for date, distance, time in trainings[login]:
            print(f"📅 Data: {date}")
            print(f"🏊 Dystans: {distance}m")
            print(f"⏱️ Czas: {time} min")
            print("-------------------------")
    else:
        print("Nie masz jeszcze żadnych treningów ❌")
