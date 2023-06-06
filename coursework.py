def radix_sort (arr):
    RADIX = 256  
# количество возможных символов в ASCII
    placement = 1  
# начинаем сортировку с младшего разряда
    max_digit = max([len(i) for i in arr])  
# определяем максимальную длину строки в массиве
    while placement <= max_digit:  
# выполняем сортировку для каждого разряда
        buckets = [list() for _ in range(RADIX)]  
# создаем временный список для хранения строк
        for i in arr:  
# проходим по каждой строке в массиве
            if len(i) < placement:  
# если длина строки меньше текущего разряда, добавляем ее в список с индексом 0
                buckets[0].append(i)
            else:
                tmp = ord(i[-placement])  
# получаем ASCII-код символа на текущем разряде
                buckets[tmp].append(i)  
# добавляем строку в список с индексом, равным ASCII-коду символа
        arr = []  
# очищаем массив строк
        for b in range(RADIX):  
# проходим по каждому индексу списка buckets
            arr += buckets[b]  
# добавляем все элементы списка с индексом b в массив строк
        placement += 1  
# переходим к следующему разряду
    return arr  
# возвращаем отсортированный массив строк

# Пример использования
def get_arr() : 
  arr = []  
  n = int(input("Введите число строк: "))
  for i in range(n):
      s = input("Введите строку: ")
      arr.append(s)
  return arr
		
arr = get_arr()
sorted_arr = radix_sort(arr)
print(sorted_arr)

