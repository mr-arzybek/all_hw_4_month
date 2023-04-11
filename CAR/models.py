from django.db import models

class CarShop(models.Model):
    CAR_TYPE = (
        ('Для молодых людей', "Для молодых людей"),
        ("Для работы", "Для работы"),
        ("Для большой семьи", "Для большой семье"),
        ("Для путешествий", "Для путешествий"),
        ("Для женщин", "Для женщин"),
        ("Для успешных", "Для успешных")
    )

    title = models.CharField('Название машины', max_length=100)
    description = models.TextField('Описание машины')
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()
    specifications = models.TextField("Характеристики")
    model_year = models.TextField("Модельный год")
    manufacturing_country = models.TextField("Страна изготовитель")

    def __str__(self):
        return self.title

