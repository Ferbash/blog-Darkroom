---
layout: default
title: "Galería por Palabras Clave"
permalink: /buscador/
---

<h1>Búsqueda de Fotos por Palabras Clave</h1>

<p>Busca fotos rápidamente usando palabras clave (ubicación, película, cámara, descripción, etc).</p>

<input type="text" id="buscador" placeholder="Escribe una palabra clave o etiqueta..." style="width: 100%; max-width: 400px; padding: 8px; font-size: 1.1em; margin-bottom: 20px;">

<ul id="resultados">
{% assign all_posts = site.posts | concat: site.categories.digital %}
{% for post in all_posts %}
  <li class="foto-item" data-keywords="{{ post.title }} {{ post.excerpt }} {{ post.location }} {{ post.film }} {{ post.camera }} {{ post.categories }} {% for tag in post.tags %}{{ tag }} {% endfor %}">
    <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%d/%m/%Y" }}<br>
    <img src="{{ post.image }}" alt="{{ post.title }}" style="max-width: 200px; margin: 10px 0;" />
    <p>{{ post.excerpt }}</p>
    {% if post.tags %}
      <span style="font-size:0.9em;color:#888;">Etiquetas: 
        {% for tag in post.tags %}<span class="tag" style="background:#eee;border-radius:3px;padding:2px 7px;margin-right:4px;">{{ tag }}</span>{% endfor %}
      </span>
    {% endif %}
  </li>
{% endfor %}
</ul>

<script>
const input = document.getElementById('buscador');
const items = document.querySelectorAll('.foto-item');
input.addEventListener('input', function() {
  const val = this.value.toLowerCase();
  items.forEach(item => {
    const keywords = item.getAttribute('data-keywords').toLowerCase();
    item.style.display = keywords.includes(val) ? '' : 'none';
  });
});
</script>
