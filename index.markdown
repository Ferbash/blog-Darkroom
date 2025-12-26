---
layout: default
---

<style>
  /* 1. OCULTA LA BARRA SUPERIOR (LO QUE MARCASTE EN AMARILLO) */
  .site-header {
    display: none !important;
  }

  /* 2. ESTILO PROFESIONAL DAVE MORROW */
  body { 
    font-family: "Georgia", serif; 
    color: #333; 
    background-color: #fff;
  }
  
  .site-title-custom {
    font-size: 3.8em;
    color: #b04b39; /* Rojo terracota */
    text-align: center;
    margin-top: 50px;
    font-weight: normal;
  }

  .nav-menu-custom {
    text-align: center;
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
    padding: 12px 0;
    margin: 20px auto 50px auto;
    max-width: 800px;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.8em;
  }

  .nav-menu-custom a {
    text-decoration: none;
    color: #666;
    margin: 0 15px;
  }

  /* 3. DISEÑO DE POSTS (IMAGEN A LA DERECHA) */
  .post-entry {
    display: flex;
    flex-wrap: wrap;
    gap: 40px;
    margin-bottom: 80px;
    align-items: center;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
  }

  .post-content-preview { flex: 1; min-width: 300px; }
  .post-image-preview { flex: 1; min-width: 300px; }

  .post-image-preview img {
    width: 100%;
    border: 1px solid #eee;
    padding: 6px;
    background: #fff;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  }
</style>

<h1 class="site-title-custom">Darkroom Photography</h1>
<div style="text-align: center; color: #1a3a5a; letter-spacing: 2px; font-size: 0.9em; margin-bottom: 15px;">
  || FOTOGRAFÍA ANALÓGICA & REVELADO QUÍMICO ||
</div>

<nav class="nav-menu-custom">
  <a href="{{ site.baseurl }}/">INICIO</a>
  <a href="{{ site.baseurl }}/about">SOBRE MÍ</a>
  <a href="#">GALERÍA</a>
  <a href="{{ site.baseurl }}/contact">CONTACTO</a>
</nav>

<div class="container">
  {% for post in site.posts %}
    <div class="post-entry">
      <div class="post-content-preview">
        <h2 style="font-size: 2.4em; color: #1a3a5a; margin-bottom: 10px;">{{ post.title }}</h2>
        <p style="color: #888; font-style: italic; margin-bottom: 15px;">{{ post.date | date: "%d/%m/%Y" }}</p>
        <p>{{ post.content | strip_html | truncatewords: 40 }}</p>
        <a href="{{ post.url | relative_url }}" style="color: #b04b39; font-weight: bold; text-decoration: none; border-bottom: 1px solid #b04b39;">Leer más →</a>
      </div>
      
      <div class="post-image-preview">
        {% if post.thumbnail %}
          <img src="{{ site.baseurl }}/assets/imagenes/{{ post.thumbnail | uri_escape }}" alt="{{ post.title }}">
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>