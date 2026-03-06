# Онлайн-магазин електроніки

Цей проект реалізує базу даних для онлайн-магазину електроніки з використанням FastAPI та SQLAlchemy.

## Структура бази даних

- **products**: таблиця товарів (product_id, name, category, price)
- **customers**: таблиця клієнтів (customer_id, first_name, last_name, email)
- **orders**: таблиця замовлень (order_id, customer_id, product_id, quantity, order_date)

## Запуск без Docker

1. Активуйте віртуальне середовище:
   ```bash
   source .venv/bin/activate
   ```

2. Запустіть сервер:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

API буде доступне на http://localhost:8000

Документація API: http://localhost:8000/docs

## Ендпоінти

- `POST /products/` - Додати продукт
- `GET /products/` - Отримати продукти
- `POST /customers/` - Додати клієнта
- `GET /customers/` - Отримати клієнтів
- `POST /orders/` - Додати замовлення
- `GET /orders/` - Отримати замовлення
- `GET /sales/total` - Загальний обсяг продажів
- `GET /customers/orders` - Кількість замовлень на клієнта
- `GET /orders/average` - Середній чек
- `GET /categories/popular` - Найпопулярніша категорія
- `GET /categories/products` - Кількість товарів у категоріях
- `PUT /products/update_smartphones` - Оновити ціни смартфонів

## Приклад використання

Додати продукт:
```bash
curl -X POST "http://localhost:8000/products/" \
  -H "Content-Type: application/json" \
  -d '{"name": "iPhone 15", "category": "смартфони", "price": 1200.0}'
```

Перевірити продажі:
```bash
curl -X GET "http://localhost:8000/sales/total"
```