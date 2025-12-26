---

layout: home
---



<ul class="post-list" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; list-style: none; padding: 0;">
	{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
	{% for post in sorted_posts %}
		<li style="border: 1px solid #eee; padding: 10px; border-radius: 8px;">
			{% if post.thumbnail %}
				<a href="{{ site.baseurl }}/assets/imagenes/{{ post.thumbnail }}" class="zoom-thumb" style="display:block;">
					<img src="{{ site.baseurl }}/assets/imagenes/{{ post.thumbnail }}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px;">
				</a>
			{% else %}
				<div style="width: 100%; height: 200px; background: #f0f0f0; display: flex; align-items: center; justify-content: center; border-radius: 4px; font-size: 2em;">📸</div>

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
				<h2 style="font-size: 1.8em; margin-bottom: 25px; font-weight: 700;">Posts</h2>

				<div class="post-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px;">
					{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
					{% for post in sorted_posts %}
						<article style="border: 1px solid #eee; border-radius: 0; overflow: hidden; transition: all 0.3s ease;">
							<a href="{{ site.baseurl }}/assets/imagenes/{{ post.thumbnail }}" class="zoom-thumb" style="display:block;">
								<div style="width: 100%; height: 250px; overflow: hidden; background: #000;">
									{% if post.thumbnail %}
										<img src="{{ site.baseurl }}/assets/imagenes/{{ post.thumbnail }}" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.9; transition: opacity 0.3s;">
									{% else %}
										<div style="height: 100%; display: flex; align-items: center; justify-content: center; color: white;">📸</div>
									{% endif %}
								</div>
							</a>
							<div style="padding: 15px 5px;">
								<a href="{{ post.url | relative_url }}" style="text-decoration: none; color: inherit;">
									<h3 style="margin: 0; font-size: 1.2em; font-weight: 700; line-height: 1.2;">
										{{ post.title }}
									</h3>
									<p style="margin: 8px 0 0; color: #888; font-size: 0.85em; text-transform: uppercase; letter-spacing: 1px;">
										{{ post.date | date: "%d · %m · %Y" }}
									</p>
								</a>
							</div>
						</article>
					{% endfor %}
				</div>
			</div>

			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/luminous-lightbox/2.3.2/luminous-basic.min.css">
			<script src="https://cdnjs.cloudflare.com/ajax/libs/luminous-lightbox/2.3.2/Luminous.min.js"></script>
			<script>
				document.addEventListener("DOMContentLoaded", function() {
					new LuminousGallery(document.querySelectorAll(".zoom-thumb"));
				});
			</script>
