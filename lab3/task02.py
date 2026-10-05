name = input()

surname, first_name, patronymic = name.split()

surname = surname.capitalize()
initials = first_name[0].upper() + ". " + patronymic[0].upper() + "."

print(surname, initials)