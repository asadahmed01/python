from employee import Employee


class Developer(Employee):
    # change the raise amount in the developer class
    raise_amount = 1.10

    def __init__(self, first, last, pay, languages):
        super().__init__(first, last, pay)
        self.languages = languages
