from django.db import models
from django.contrib import admin
from django.utils import timezone

class Post(models.Model):
	"""
	Model class that represents a blog post.
	"""

	# Model attributes.
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	site = 	models.IntegerField(choices=[(1, "home"), (2, "about"), (3, "contact")], default=(1, "home"))
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		"""
		Define the string representation of this object to be the title of the blog post.
		
		Returns:
		    str: title of the blog post
		"""
		return self.title

class PostAdmin(admin.ModelAdmin):
	"""
	Define the Model class Post for the admin page.
	"""
	actions = ('publish', 'sanitize')

	
	def publish(self, request, obj):		
		"""
		Method to add the publication date to the blog post to be the current time.
		
		Args:
		    request (WSGIRequest): 	the request object 
		    obj 	(Post): 		the Post instance we're operating on
		"""

		obj.published_date = timezone.now()

	def sanitize(self, request, obj):
		"""
		Method to check for any script tags to prevent accidental XSS attack.
		
		Args:
		    request (WSGIRequest): 	the request object 
		    obj 	(Post): 		the Post instance we're operating on
		"""

		# Find the indices of script tags.
		startingIndex = obj.text.find("<script>")
		endingIndex = obj.text.find("</script>")

		if startingIndex != -1:
			print("XSS detected. Script tags have been found. Removing...")

			if endingIndex == -1:
				print("Incorrect script syntax, please remove script manually.")
			
			# Remove the script tags along with the text inside them.
			obj.text = obj.text[:startingIndex] + obj.text[endingIndex + len("</script>"):]

	def save_model(self, request, obj, form, change):
		"""
		Method that overrides the default save_model().
		Adding our own functionality to call the above methods on-save.
		
		Args:
		    request (WSGIRequest): 	the request object 
		    obj 	(Post): 		the Post instance we're operating on
		    form 	(PostForm): 	the PostForm instance we're operating on
		    change 	(bool): 		signals if the form has changed	
		"""

		self.sanitize(request, obj)
		#self.publish(request, obj)
		obj.save()
