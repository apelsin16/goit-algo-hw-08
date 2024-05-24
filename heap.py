import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізуємо мін-купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабеля
    while len(cables) > 1:
        # Витягуємо два найменших кабеля
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх
        combined = first + second
        
        # Додаємо витрати на об'єднання
        total_cost += combined
        
        # Додаємо об'єднаний кабель назад у купу
        heapq.heappush(cables, combined)
    
    return total_cost

# Приклад використання
cables = [1, 2, 3, 4, 5]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
