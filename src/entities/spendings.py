'''Spendingsview'''

class CategoryList:
    '''Spendingsview'''
    def __init__(self, all):
        '''Spendingsview'''
        self.categories =[]
        for i in all:
            c = Category(i)
            self.categories.append(c)

    def get_index(self,CA):
        '''Spendingsview'''
        for i in range(len(self.categories)):
            if CA == self.categories[i].getcategory_name():
                return i

    def get_length(self):
        '''Spendingsview'''
        i = len(self.categories)
        return i

    def get_category(self, i):
        '''Spendingsview'''
        return self.categories[i]

    def get_name(self,i):
        '''Spendingsview'''
        return self.categories[i].getcategory_name()

    def get_sum(self, i):
        '''Spendingsview'''
        SUMMA = self.categories[i].getsumma()
        return SUMMA

    def get_add_summa(self, i, SUMMA):
        '''Spendingsview'''
        self.categories[i].add_summa(SUMMA)

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
    '''Spendingsview'''
    def __init__(self, category_name):
        self.category_name = category_name
        self.summa = 0.00

    def getcategory_name(self):
        '''Spendingsview'''
        return self.category_name

    def getsumma(self):
        '''Spendingsview'''
        return self.summa

    def add_summa(self, n):
        '''Spendingsview'''
        self.summa += n
