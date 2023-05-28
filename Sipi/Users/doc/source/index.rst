.. Sipi documentation master file, created by
   sphinx-quickstart on Tue May  9 22:58:39 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Добро пожаловать в документацию по проекту Sipi!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Здесь вы сможете найти документацию по серверной части проекта, реализованной на фреймворке Django



Модели
================================
``User`` - Простая модель для пользователя.

**Поля**::

     password = models.CharField
     avatar = models.ImageField
     first_name = models.CharField
     last_name = models.CharField
     email = models.EmailField



Формы
================================
``UserSignupForm`` - форма для регистрации пользователя

**Поля**::

     password = models.CharField
     avatar = models.ImageField
     first_name = models.CharField
     last_name = models.CharField
     email = models.EmailField


**Методы**:

``save(self, request)`` - сохраняет нового пользователя

Представления (Views)
================================
``UserSignupView(SignupView)`` - view для регистрации пользователей, наследуется от встроенного в джанго класса

**Методы**:

``get_form_kwargs(self)`` -
Возврат аргументов ключей для создания экземпляра формы.

