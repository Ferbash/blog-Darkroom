---
layout: default
---

<style>
  body {
    font-family: "Georgia", serif;
    color: #333;
    line-height: 1.6;
  }
  
  .site-title-custom {
    font-size: 3.5em;
    color: #b04b39;
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
    font-size: 0.8em;
    color: #666;
  }

  .nav-menu-custom a {
    text-decoration: none;
    color: #1a3a5a;
    margin: 0 10px;
  }

  .post-entry {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    margin-bottom: 60px;
    align-items: center;
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 40px;
  }

  .post-content-preview { flex: 1; min-width: 300px; }
  .post-content-preview h2 { font-size: 2em; color: #1a3a5a; margin-bottom: 10px; }
  
  .post-image-preview { flex: 1; min-width: 300px; text-align: center; }
  .post-image-preview img {
    max-width: 100%;
    border: 1px solid #ddd;
    padding: 4px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
</style>

<h1 class="site-title-custom">Darkroom Photography</h1>
<div style="text-align: center; color: #1a3a5a; letter-spacing: 1px; font-size: 0.9em; margin-bottom: 10px;">
  || FOTOGRAFÍA ANALÓGICA & REVELADO QUÍMICO ||
</div>

<nav class="nav-menu-custom">
  <a href="{{ site.baseurl }}/">INICIO</a> | 
  <a href="{{ site.baseurl }}/about">SOBRE MÍ</a> | 
  <a href="#">GALERÍA</a> | 
  <a href="#">CONTACTO</a>
</nav>

<div class="container">
  {% for post in site.posts %}
    <div class="post-entry">
      <div class="post-content-preview">
        <h2>{{ post.title }}</h2>
        <p>{{ post.content | strip_html | truncatewords: 30 }}</p>
        <a href="{{ post.url | relative_url }}" style="color: #b04b39; font-weight: bold; text-decoration: none;">Leer más →</a>
      </div>
      
      <div class="post-image-preview">
        {% if post.thumbnail %}
          <img src="{{ site.baseurl }}/assets/img/{{ post.thumbnail | uri_escape }}" alt="{{ post.title }}">
        {% else %}
          <div style="background: #f9f9f9; height: 200px; display: flex; align-items: center; justify-content: center; color: #ccc;">
            📸 Sin imagen configurada
          </div>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>