from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


class TooMuchSymbolsError(Exception):
    pass


class InvalidDomainLengthError(Exception):
    pass


class InvalidDomainCharacterError(Exception):
    pass


MIN_LENGTH = 4
VALID_DOMAINS = (".com", ".bg", ".net", ".org")

patten_name = r'\w+'
pattern_domain = r'\.[a-z]+'
pattern_domain_name = r'\@(.+)\.'

email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol!")

    if len(email.split("@")[0]) <= MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    if len(email.split("@")[0]) > 12:
        raise TooMuchSymbolsError("Name must be between 4 and 12 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if findall(patten_name, email)[0] != email.split("@")[0]:
        raise InvalidNameError("Name can contain only letters, digits and underscores!")

    if len(findall(pattern_domain, email)[-1]) < 3:
        raise InvalidDomainLengthError("Domain name must be at least 2 character")

    if findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    # first case

    # if " " in findall(pattern_domain_name, email)[-1]:
    #     raise InvalidDomainCharacterError("Free space is not allowed in domain name!")

    # second case
    if " " in email.split("@")[-1]:
        raise InvalidDomainCharacterError("Free space is not allowed in domain name!")

    print("Email is valid")

    email = input()
