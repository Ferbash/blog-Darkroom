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
			{% endif %}
			<a href="{{ post.url | relative_url }}" style="text-decoration: none; color: inherit;">
				<h3 style="margin: 10px 0 5px 0; font-size: 1.25em; font-weight: bold; color: #222; letter-spacing: 1px; text-shadow: 1px 1px 6px #e0e0e0, 0 2px 8px #fff; transition: color 0.2s;">
					{{ post.title }}
				</h3>
				<span style="color: #666; font-size: 0.8em;">{{ post.date | date: "%b %d, %Y" }}</span>
			</a>
		</li>
	{% endfor %}
</ul>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/luminous-lightbox/2.3.2/luminous-basic.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/luminous-lightbox/2.3.2/Luminous.min.js"></script>
<script>
	document.addEventListener("DOMContentLoaded", function() {
		new LuminousGallery(document.querySelectorAll(".zoom-thumb"));
	});
</script>
