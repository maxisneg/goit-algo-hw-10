
from pulp import LpMaximize, LpProblem, LpVariable, value

# Створюємо модель
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Цільова функція: максимізувати загальну кількість продуктів
model += lemonade + juice, "Total_Production"

# Обмеження ресурсів
model += (2 * lemonade + 1 * juice <= 100, "Water")
model += (1 * lemonade <= 50, "Sugar")
model += (1 * lemonade <= 30, "Lemon_juice")
model += (2 * juice <= 40, "Fruit_puree")

# Розв'язання
model.solve()

# Результати
print(f"Lemonade: {lemonade.value()}")
print(f"Fruit Juice: {juice.value()}")
print(f"Total products: {value(model.objective)}")
