---
layout: default
---

<header style="text-align: center; padding: 40px 0; border-bottom: 2px solid #111; margin-bottom: 40px;">
  <h1 style="font-size: 3.5em; font-weight: 900; letter-spacing: -2px; margin: 0; text-transform: uppercase;">
    Darkroom
  </h1>
  <p style="font-size: 1.2em; color: #555; margin-top: 10px; font-style: italic;">
    Un paseo por fotografía química
  </p>
</header>

<div class="container">
  <h2 style="font-size: 1.8em; margin-bottom: 25px; font-weight: 700;">Galería</h2>

  <div class="post-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px;">
    {% for post in site.posts %}
      <article style="background: white; border: 1px solid #eee; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
        <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: inherit;">
          <div style="width: 100%; height: 250px; overflow: hidden; background: #000;">
            {% if post.thumbnail %}
              <img src="{{ site.baseurl }}/assets/img/{{ post.thumbnail }}" class="zoom-img" style="width: 100%; height: 100%; object-fit: cover; cursor: zoom-in;">
            {% else %}
              <div style="height: 100%; display: flex; align-items: center; justify-content: center; color: white;">📸 Sin miniatura</div>
            {% endif %}
          </div>
          <div style="padding: 15px;">
            <h3 style="margin: 0; font-size: 1.2em; font-weight: 700;">{{ post.title }}</h3>
            <p style="color: #888; font-size: 0.8em; margin-top: 5px;">{{ post.date | date: "%d/%m/%Y" }}</p>
          </div>
        </a>
      </article>
    {% endfor %}
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/medium-zoom/dist/medium-zoom.min.js"></script>
<script>
  mediumZoom('.zoom-img', { margin: 24, background: '#fff' });
</script>