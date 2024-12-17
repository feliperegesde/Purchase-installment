def selection_sort_odds(arr):
    n = len(arr)

    # Percorre todos os elementos da lista
    for i in range(n):
        if arr[i] % 2 != 0:  # Se o número é ímpar
            # Encontra a posição correta do número ímpar
            min_index = i
            for j in range(i + 1, n):
                if arr[j] % 2 != 0 and arr[j] < arr[min_index]:
                    min_index = j
            
            # Se min_index foi atualizado, trocamos os valores
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso
arr = [2, 3, 6, 4, 1, 6, 5, 7, 9, 8]
selection_sort_odds(arr)
print(arr)  # Resultado esperado: [2, 1, 6, 4, 3, 6, 5, 7, 9, 8]  