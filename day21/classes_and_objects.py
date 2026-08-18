'''
Level 1 Exercises
'''

class Statistics:
    def __init__(self, nums):
        self.nums = sorted(nums)

    def count(self):
        return len(self.nums)

    def sum(self):
        return sum(self.nums)

    def min(self):
        return self.nums[0]

    def max(self):
        return self.nums[-1]

    def range(self):
        return self.nums[-1] - self.nums[0]

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        if self.count() % 2 == 0:
            return (self.nums[self.count() // 2] + self.nums[self.count() // 2 - 1]) / 2
        else:
            return self.nums[self.count() // 2]

    def mode(self):
        counts = {}
        for num in self.nums:
            counts[num] = counts.get(num, 0) + 1
        mode = max(counts, key=counts.get)
        return mode

    def var(self):
        mean = self.mean()
        variance = sum((num - mean) ** 2 for num in self.nums) / self.count()
        return variance

    def std(self):
        return f'{self.var()**0.5:.1f}'

    def freq_dist(self):
        freq_dist = {}
        for num in self.nums:
            freq_dist[num] = freq_dist.get(num, 0) + 1
        return freq_dist

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:',data.count())
print('Sum:',data.sum())
print('Min:',data.min())
print('Max:',data.max())
print('Range:',data.range())
print('Mean:',data.mean())
print('Median:',data.median())
print('Mode:',data.mode())
print('Variance:',data.var())
print('Standard Deviation:',data.std())
print('Frequency Distribution:',data.freq_dist())

'''
Level 2 Exercises
'''

class PersonAccount:
    def __init__(self, first_name, last_name, incomes, expenses):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return sum(self.incomes)

    def total_expenses(self):
        return sum(self.expenses)

    def account_info(self):
        return f'Name: {self.first_name} {self.last_name}\nIncomes: {self.incomes}\nExpenses: {self.expenses}'

    def add_income(self, income):
        self.incomes.append(income)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def account_balance(self):
        return self.total_income() - self.total_expenses()

    

    
    