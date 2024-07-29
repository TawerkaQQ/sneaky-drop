# sneaky-drop

---
## Создание БД 
1. Переход в postgres терминал
```commandline
sudo -u postgres psql
```
2. Создание БД
```sql
create database sneak_drop;
```
3. Создание таблиц. Перед этим заполнить .env по примеру
```commandline
python db/create_db.py 
```
---
## Добавление и удаление записей
Методы удалениея и добавления записей в таблицу mail_account:
```python
interface.insert_into_mail_account(phone_number='888888888', name='Bobra', surname='Perdole',
                                       birthday='2012-10-30', sex='male', email='bobra@gmail.com')
```
```python
interface.delete_from_mail_account_by_phone('888888888')
```
---
## Docker
Создание образа
```commandline
docker build --tag 'ozon' .
```
Запуск из контейнера
```commandline
docker run 'ozon'
```
