import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    # Запитуємо користувача про рівень рекурсії
    level = int(input("Введіть рівень рекурсії (ціле число): "))

    # Створюємо вікно для малювання
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Створюємо черепашку
    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(0)  # Найвища швидкість

    # Підняти перо, перемістити до початкової позиції та опустити перо
    fractal_turtle.penup()
    fractal_turtle.goto(-150, 90)
    fractal_turtle.pendown()

    # Викликаємо функцію для малювання сніжинки Коха
    for _ in range(3):
        koch_snowflake(fractal_turtle, level, 300)
        fractal_turtle.right(120)

    # Завершуємо вікно при натисканні на нього
    screen.exitonclick()

if __name__ == "__main__":
    main()
