class User:
  def __init__(self, user_id, name):
      self.__user_id = user_id  # Защищенный атрибут
      self.__name = name         # Защищенный атрибут
      self.__access_level = 'user'  # Уровень доступа по умолчанию

  # Геттеры
  def get_user_id(self):
      return self.__user_id

  def get_name(self):
      return self.__name

  def get_access_level(self):
      return self.__access_level

  # Сеттеры
  def set_name(self, name):
      self.__name = name


class Admin(User):
  def __init__(self, user_id, name, admin_access_level):
      super().__init__(user_id, name)
      self.__access_level = 'admin'  # Уровень доступа для администраторов
      self.__admin_access_level = admin_access_level  # Дополнительный уровень доступа

  def add_user(self, user_list, user_id, name):
      new_user = User(user_id, name)
      user_list.append(new_user)
      print(f"\nПользователь '{name}' добавлен.")

  def remove_user(self, user_list, user_id):
      for user in user_list:
          if user.get_user_id() == user_id:
              user_list.remove(user)
              print(f"\nПользователь с ID '{user_id}' удален.")
              return
      print(f"Пользователь с ID '{user_id}' не найден.")

  def get_admin_access_level(self):
      return self.__admin_access_level


# Пример использования
if __name__ == "__main__":
  user_list = []

  admin = Admin(user_id=1, name="Администратор", admin_access_level="full")

  # Добавление пользователей
  admin.add_user(user_list, user_id=2, name="Сотрудник 1")
  admin.add_user(user_list, user_id=3, name="Сотрудник 2")

  # Вывод списка пользователей
print("\nСписок пользователей после добавления:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

  # Удаление пользователя
admin.remove_user(user_list, user_id=2)

  # Вывод списка пользователей после удаления
print("\nСписок пользователей после удаления:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
