---
layout: default
---

<style>
  body {
    font-family: "Georgia", "Times New Roman", serif; /* Fuente clásica serif */
    color: #333;
    line-height: 1.6;
    background-color: #fff;
  }
  
  .site-title-custom {
    font-family: "Georgia", serif;
    font-size: 4em;
    color: #b04b39; /* Rojo terracota similar al ejemplo */
    text-align: center;
    margin-top: 40px;
    font-weight: normal;
  }

  .nav-menu-custom {
    text-align: center;
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
    padding: 10px 0;
    margin: 20px 0 40px 0;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.9em;
    color: #666;
  }

  .nav-menu-custom a {
    text-decoration: none;
    color: #666;
    margin: 0 15px;
  }

  .post-entry {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    margin-bottom: 60px;
    align-items: flex-start;
  }

  .post-content-preview {
    flex: 1;
    min-width: 300px;
  }

  .post-content-preview h2 {
    font-size: 2.2em;
    color: #1a3a5a; /* Azul oscuro elegante */
    margin-top: 0;
  }

  .post-image-preview {
    flex: 1;
    min-width: 300px;
  }

  .post-image-preview img {
    width: 100%;
    border: 1px solid #ddd;
    padding: 5px;
    background: #fff;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }
</style>

<h1 class="site-title-custom">Darkroom Photography</h1>
<div style="text-align: center; color: #1a3a5a; letter-spacing: 1px; margin-bottom: 10px;">
  || FOTOGRAFÍA ANALÓGICA & REVELADO QUÍMICO ||
</div>

<nav class="nav-menu-custom">
  <a href="{{ site.baseurl }}/">Inicio</a> | 
  <a href="{{ site.baseurl }}/about">Sobre mí</a> | 
  <a href="#">Galería</a> | 
  <a href="#">Contacto</a>
</nav>

<div class="container">
  {% for post in site.posts %}
    <div class="post-entry">
      <div class="post-content-preview">
        <h2>{{ post.title }}</h2>
        <p>{{ post.content | strip_html | truncatewords: 50 }}</p>
        <a href="{{ post.url | relative_url }}" style="color: #b04b39; font-weight: bold; text-decoration: none;">Leer más →</a>
      </div>
      
      <div class="post-image-preview">
        {% if post.thumbnail %}
          <img src="{{ site.baseurl }}/assets/img/{{ post.thumbnail | uri_escape }}" alt="{{ post.title }}">
        {% else %}
          <div style="background: #f4f4f4; height: 250px; display: flex; align-items: center; justify-content: center; color: #999; border: 1px solid #ddd;">
            📸 Sin imagen
          </div>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>