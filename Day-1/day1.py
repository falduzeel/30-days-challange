import datetime

current_year = datetime.datetime.now().year
birth_year_input = input("Tamaru janma varsh (Birth Year) lakho (e.g., 2008): ").strip()

if birth_year_input.isdigit():
    birth_year = int(birth_year_input)
    
    if 1900 <= birth_year <= current_year:
        age = current_year - birth_year
        print(f"Tamari umar kareeb {age} varsh chhe!")
        print(f"Informative tidbit: Tame {current_year - birth_year + 1}ma varsh ma praveshi chuka cho.")
    else:
        print("Krupaya ek valid birth year lakho.")
else:
    print("Invalid input! Krupaya purani sankhya (number) j lakho.")