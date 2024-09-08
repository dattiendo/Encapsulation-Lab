class Email_Validator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains
    def __validate_name(self, name):
        return len(name) >= self.min_length
    def __validate_mail(self, mail):
        return mail in self.mails
    def __validate_domain(self, domain):
        return domain in self.domains
    def validate(self, email):
        try:
            name, rest = email.split('@')
            mail, domain = rest.split('.')
        except ValueError:
            return False
        return (self.__validate_name(name) and self.__validate_mail(mail) and self.__validate_domain(domain))
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = Email_Validator(6, mails, domains)
print(email_validator.validate("dattiendo@gmail.com"))    # True
print(email_validator.validate("dat@gmail.net"))   # False (domain not valid)
print(email_validator.validate("dat@abv.net"))    # False (mail and domain not valid)
print(email_validator.validate("dat@softuni.bg"))       # False (username too short)