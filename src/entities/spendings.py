import uuid


class Category_list:
    def __init__(self, all):
        self.categories =[]
        for i in all:
            c = Category(i)
            self.categories.append(c)

    def get_index(self,c):
        for i in range(len(self.categories)):
            if c == self.categories[i].getcategory_name():
                return i

    def get_length(self):
        i = len(self.categories)
        return i

    def get_category(self, i):
        return self.categories[i]

    def get_name(self,i):
        return self.categories[i].getcategory_name()

    def get_sum(self, i):
        s = self.categories[i].getsumma()
        return s

    def get_add_summa(self, i, s):
        self.categories[i].add_summa(s)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= len(self.categories):
            result = self.categories[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration


class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.summa = 0

    def getcategory_name(self):
        return self.category_name

    def getsumma(self):
        return self.summa

    def add_summa(self, n):
        self.summa += n






