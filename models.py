from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def edit(self, name, description, image=None):
        self.name = name
        self.description = description

        # Update image only if a new image is provided
        if image:
            self.image = image

        # Save the changes
        self.save()

    def short_description(self):
        # Split the description into words
        words = self.description.split()

        # Check if the description is more than 50 words
        if len(words) > 50:
            # Join the first 50 words and add "..." at the end
            return ' '.join(words[:50]) + '...'
        else:
            # If the description is already less than 50 words, return it as is
            return self.description

