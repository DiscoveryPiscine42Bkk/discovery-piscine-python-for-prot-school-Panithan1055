
def array_of_names(names_dict):
    full_names = [f"{first.capitalize()} {last.capitalize()}" for first, last in names_dict.items()]
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
