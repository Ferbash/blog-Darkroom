---
layout: default
title: "Digital"
permalink: /digital/
---

<h1>Galería Digital</h1>

<p>Fotos tomadas con cámara digital.</p>

<ul>
{% for post in site.categories.digital %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%d/%m/%Y" }}<br>
    <img src="{{ post.image }}" alt="{{ post.title }}" style="max-width: 300px; margin: 10px 0;" />
    <p>{{ post.excerpt }}</p>
  </li>
{% endfor %}
</ul>
