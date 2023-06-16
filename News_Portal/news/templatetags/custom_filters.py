from django import template

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def currency(value):
    value = str(value).replace("редиска", "*******")



    # Возвращаемое функцией значение подставится в шаблон.
    return f'{value}'
