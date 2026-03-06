# Онлайн-магазин электроники

## О проекте

Проект включает три таблицы
- **products**: таблица товаров (product_id, name, category, price)
- **customers**: таблица клиентов (customer_id, first_name, last_name, email)
- **orders**: таблица заказов (order_id, customer_id, product_id, quantity, order_date)

## Установка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/iperpetom-beep/Online_Device_Shop.git
   cd Online_Device_Shop
   ```

2. **Создайте виртуальное окружение (если вам этого хочеться)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # На Windows: .venv\Scripts\activate
   ```

3. **Установите все нужныйе зависимости**
   ```bash
   pip install -r requirements.txt
   ```

## Запуск этой штуки

1. **Активируйте виртуальное окружение** (если не активирывали кнш)
   *для Linux/Mac:*
   ```bash
   source .venv/bin/activate
   ```


2. **Запустите сервак**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Откройте в браузере вот это**
   - API: http://localhost:8000
   - Документация Swagger: http://localhost:8000/docs

Сервер запустится локально и будет автоматически перезагружаться при изменениях в коде. 
(Ну по крайней мере так оно должно быть)

## API Энд пойнты

### Управление товарами
- `POST /products/` - Добавить товар
- `GET /products/` - Получить список товаров

### Управление клиентами
- `POST /customers/` - Добавить клиента
- `GET /customers/` - Получить список клиентов

### Управление заказами
- `POST /orders/` - Добавить заказ
- `GET /orders/` - Получить список заказов

### Аналитика типо
- `GET /sales/total` - Общий объем продаж
- `GET /customers/orders` - Количество заказов на клиента
- `GET /orders/average` - Средний чек заказа
- `GET /categories/popular` - Самая популярная категория товаров
- `GET /categories/products` - Количество товаров в каждой категории
- `PUT /products/update_smartphones` - Обновить цены смартфонов на 10%

## Примеры использования

### Добавить товар
```bash
curl -X POST "http://localhost:8000/products/" \
  -H "Content-Type: application/json" \
  -d '{"name": "iPhone 15", "category": "Phone", "price": 1200.0}'
```

### Получить весь объем продаж
```bash
curl -X GET "http://localhost:8000/sales/total"
```

### Добавить чела
```bash
curl -X POST "http://localhost:8000/customers/" \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Иван", "last_name": "Иванов", "email": "ivan@example.com"}'
```

### Создать заказ
```bash
curl -X POST "http://localhost:8000/orders/" \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 1, "product_id": 1, "quantity": 2, "order_date": "2023-10-01"}'
```

## Публикация на GitHub (для меня)

1 **Создайте новый репозиторий**:
   - Нажмите "+" в правом верхнем углу > "New repository"
   - Название: `Online_Device_Shop`
   - Описание: "Онлайн-магазин электроники на FastAPI"
   - Сделайте публичным или приватным
   - НЕ добавляйте README, .gitignore или лицензию (мы уже имеем)

2 **Инициализируйте git в папке проекта** (если не инициализирован):
   ```bash
   git init
   ```

3 **Добавьте файлы**:
   ```bash
   git add .
   ```

4 **Создайте коммит**:
   ```bash
   git commit -m "Initial commit"
   ```

5 **Добавьте remote**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/Online_Device_Shop.git
   ```
   Замените `YOUR_USERNAME` на ваше имя пользователя GitHub.

6 **Отправьте на GitHub**:
   ```bash
   git push -u origin main
   ```

7. **Если возникли проблемы** (например, divergent branches):
   - Попробуйте `git pull origin main --allow-unrelated-histories`
   - Или `git push -u origin main --force` (осторожно, перезапишет историю)

Теперь ваш проект доступен на GitHub.Вы можете делиться ссылкой и принимать вклады от других.

## Структура проекта

```
Online_Device_Shop/
├── bd/
│   ├── __init__.py
│   ├── crud.py          # Функции CRUD
│   ├── database.py      # Настройки базы данных
│   ├── models.py        # SQLAlchemy модели
│   └── schemas.py       # Pydantic схемы
├── main.py              # FastAPI приложение
├── requirements.txt     # Зависимости
├── README.md            # Этот файл
└── gitignore            # Исключаемые файлы

 
```

####  Я немного начинаю понимать git :3
####  ⠀
####  ⠀
#### :P