---
layout: default
title: Galería
permalink: /galeria/
---

<style>
  .gallery-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
  }

  .gallery-title {
    font-size: 3em;
    color: #b04b39;
    text-align: center;
    margin-bottom: 15px;
    font-weight: normal;
  }

  .gallery-subtitle {
    text-align: center;
    color: #666;
    font-size: 1.1em;
    margin-bottom: 50px;
    font-style: italic;
  }

  .gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 30px;
    margin-top: 40px;
  }

  .gallery-item {
    position: relative;
    overflow: hidden;
    border: 1px solid #eee;
    padding: 8px;
    background: #fff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .gallery-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  }

  .gallery-item a {
    display: block;
    text-decoration: none;
    color: inherit;
  }

  .gallery-item img {
    width: 100%;
    height: 280px;
    object-fit: cover;
    display: block;
  }

  .gallery-item-info {
    padding: 12px 8px;
    background: #fff;
  }

  .gallery-item-title {
    font-size: 1.1em;
    color: #1a3a5a;
    margin-bottom: 5px;
    font-weight: bold;
  }

  .gallery-item-meta {
    font-size: 0.85em;
    color: #888;
    font-style: italic;
  }

  .gallery-item-date {
    font-size: 0.8em;
    color: #999;
    margin-top: 5px;
  }

  /* Responsive */
  @media screen and (max-width: 768px) {
    .gallery-title {
      font-size: 2.2em;
    }
    
    .gallery-grid {
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 20px;
    }

    .gallery-item img {
      height: 200px;
    }
  }

  @media screen and (max-width: 480px) {
    .gallery-title {
      font-size: 1.8em;
    }
    
    .gallery-grid {
      grid-template-columns: 1fr;
      gap: 25px;
    }

    .gallery-item img {
      height: 250px;
    }
  }
</style>

<div class="gallery-container">
  <h1 class="gallery-title">Galería Fotográfica</h1>
  <p class="gallery-subtitle">Todas mis capturas en película química</p>

  <div class="gallery-grid">
    {% for post in site.posts %}
      {% if post.thumbnail %}
        <div class="gallery-item">
          <a href="{{ post.url | relative_url }}">
            <img src="{{ site.baseurl }}/assets/imagenes/{{ post.thumbnail | uri_escape }}" alt="{{ post.title }}">
            <div class="gallery-item-info">
              <div class="gallery-item-title">{{ post.title }}</div>
              {% if post.location or post.film or post.camera %}
                <div class="gallery-item-meta">
                  {% if post.location %}{{ post.location }}{% endif %}{% if post.film %} — {{ post.film }}{% endif %}{% if post.camera %} · {{ post.camera }}{% endif %}
                </div>
              {% endif %}
              <div class="gallery-item-date">{{ post.date | date: "%d/%m/%Y" }}</div>
            </div>
          </a>
        </div>
      {% endif %}
    {% endfor %}
  </div>
</div>
