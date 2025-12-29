---
layout: default
---

<style>
  /* 1. REDUCE EL TÍTULO SUPERIOR A SUBTÍTULO */
  .site-header {
    border-bottom: 1px solid #e8e8e8;
    padding: 5px 0;
  }
  
  .site-header .site-title {
    font-size: 0.65em !important;
    font-weight: 300 !important;
    color: #999 !important;
    letter-spacing: 0.3px;
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
  .post-image-preview { flex: 1.4; min-width: 350px; }

  .post-image-preview img {
    width: 100%;
    border: 1px solid #eee;
    padding: 6px;
    background: #fff;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  }
  
  .photo-caption {
    margin-top: 8px;
    font-size: 0.85em;
    color: #888;
    font-style: italic;
    text-align: center;
  }
  
  /* 4. RESPONSIVE PARA MÓVILES */
  @media screen and (max-width: 768px) {
    .site-title-custom {
      font-size: 2.5em;
      margin-top: 30px;
    }
    
    .nav-menu-custom {
      font-size: 0.7em;
      padding: 10px 0;
      margin: 15px auto 30px auto;
    }
    
    .nav-menu-custom a {
      margin: 0 8px;
      display: inline-block;
    }
    
    .post-entry {
      flex-direction: column;
      gap: 20px;
      margin-bottom: 50px;
      padding: 0 15px;
    }
    
    .post-content-preview h2 {
      font-size: 1.8em !important;
    }
    
    .post-content-preview,
    .post-image-preview {
      min-width: 100%;
      width: 100%;
    }
    
    .post-image-preview img {
      padding: 4px;
    }
  }
  
  @media screen and (max-width: 480px) {
    .site-title-custom {
      font-size: 2em;
      margin-top: 20px;
    }
    
    .nav-menu-custom {
      font-size: 0.65em;
      letter-spacing: 1px;
    }
    
    .nav-menu-custom a {
      margin: 0 5px;
    }
    
    .post-content-preview h2 {
      font-size: 1.5em !important;
    }
  }
</style>

<h1 class="site-title-custom">Darkroom Photography</h1>
<div style="text-align: center; color: #666; font-size: 1.1em; margin-bottom: 15px; font-style: italic;">
  Fotografía analógica, revelado químico y recorridos personales.
</div>

<nav class="nav-menu-custom">
  <a href="{{ site.baseurl }}/">INICIO</a>
  <a href="{{ site.baseurl }}/about">SOBRE MÍ</a>
  <a href="{{ site.baseurl }}/galeria">GALERÍA</a>
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
          {% if post.location or post.film or post.camera %}
            <div class="photo-caption">
              {% if post.location %}{{ post.location }}{% endif %}{% if post.film %} — {{ post.film }}{% endif %}{% if post.camera %} · {{ post.camera }}{% endif %}
            </div>
          {% endif %}
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>