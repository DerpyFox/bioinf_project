import random

def generate_field(ratio, a, b, I=20, J=30, output_file="field.json"):
    """
    Генерирует поле и сохраняет его в файл в формате JSON.

    Args:
        ratio (list): Список из двух значений, определяющий долю 0 и 1 в поле.
        a (int): Количество 'A' в поле (учитывается как 0).
        b (int): Количество 'B' в поле (учитывается как 1).
        I (int): Количество строк в поле.
        J (int): Количество столбцов в поле.
        output_file (str): Имя файла для сохранения результата.
    """
    if len(ratio) != 2 or sum(ratio) != 1:
        raise ValueError("Ratio должен быть списком из двух чисел, сумма которых равна 1.")

    field = []
    for _ in range(I):
        row = [0 if random.random() < ratio[0] else 1 for _ in range(J)]
        field.append(row)

    while a > 0:
        x, y = random.randint(0, I - 1), random.randint(0, J - 1)
        if field[x][y] not in ["A", "B"]:  
            field[x][y] = "A"
            a -= 1

    while b > 0:
        x, y = random.randint(0, I - 1), random.randint(0, J - 1)
        if field[x][y] not in ["A", "B"]:  
            field[x][y] = "B"
            b -= 1

    with open(output_file, "w") as f:
        f.write('{\n')
        f.write(f'  "I": {I},\n')
        f.write(f'  "J": {J},\n')
        f.write('  "field": [\n')
        for i, row in enumerate(field):
            row_str = ', '.join(f'"{x}"' if x in ["A", "B"] else str(x) for x in row)
            if i < len(field) - 1:
                f.write(f'    [{row_str}],\n')
            else:
                f.write(f'    [{row_str}]\n')
        f.write('  ]\n')
        f.write('}\n')

    print(f"Поле успешно сохранено в {output_file}.")

generate_field(ratio=[1.0, 0.0], a=0, b=0, I=10, J=10)