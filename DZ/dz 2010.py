from jinja2 import Template


html = """
{% macro input_func(name, type='text', placeholder='') %}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
{% endmacro %}

<p>{{ input_func('firstname', placeholder='Имя') }}</p>
# <p>{{ input_func('lastname', placeholder='Фамилия') }}</p>
# <p>{{ input_func('address', placeholder='Адрес') }}</p>
# <p>{{ input_func('phone', 'tel', 'Телефон') }}</p>
# <p>{{ input_func('email', 'email', 'Почта') }}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)


links = [
    {'id': 'index', "link": "Главная"},
    {'id': 'news', "link": "Новости"},
    {'id': 'about', "link": "О компании"},
    {'id': 'shop', "link": "Магазин"},
    {'id': 'contacts', "link": "Контакты"}
]

menu = """
<ul>
{% for c in links %}
    {% if c.link == "Главная" %}
        <li><a href="/{{ c.id }}" class="active">{{ c.link }}</a></li>
    {% else %}
        <li><a href="/{{ c.id }}">{{ c.link }}</a></li>
    {% endif %}
{% endfor %}
</ul>
"""

tm = Template(menu)
msg = tm.render(links=links)

print(msg)

