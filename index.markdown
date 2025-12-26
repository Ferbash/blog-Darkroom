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
  <h2 style="font-size: 1.8em; margin: 40px 0 25px 0; font-weight: 700; border-left: 5px solid #000; padding-left: 15px;">Galería</h2>

  <div class="post-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px;">
    {% for post in site.posts %}
      <article style="background: white; border: 1px solid #eee; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
        <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: inherit;">
          <div style="width: 100%; height: 250px; overflow: hidden; background: #000;">
            {% if post.thumbnail %}
              <img src="{{ site.baseurl }}/assets/imagenes/{{ post.thumbnail }}" style="width: 100%; height: 100%; object-fit: cover; display: block;" alt="{{ post.title }}">
            {% else %}
              <span style="color: #fff; font-size: 2.5em;">📸 Sin miniatura<br><span style='font-size:1em;'>Verifica el nombre en el front matter y en assets/imagenes</span></span>
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

