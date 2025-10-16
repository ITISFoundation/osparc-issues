# Release Notes

{% for file in site.static_files %}
    {% if file.path contains 'releases-notes/osparc' and file.extname == '.md' %}
    - [{{ file.name | split: '.' | first }}]({{ file.path | replace: '.md', '.html' }})
    {% endif %}
{% endfor %}
