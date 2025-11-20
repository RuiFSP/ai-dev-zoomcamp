from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
	"""Simple TODO model used in course homework.

	Fields:
	- title: short title
	- description: optional longer text
	- created_at: auto timestamp when created
	- due_date: optional deadline
	- completed: boolean flag
	- completed_at: timestamp when marked completed
	"""

	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField(null=True, blank=True)
	completed = models.BooleanField(default=False)
	completed_at = models.DateTimeField(null=True, blank=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self) -> str:
		return f"{self.title} {'(done)' if self.completed else ''}"

	def mark_completed(self) -> None:
		"""Mark the todo as completed and set `completed_at`."""
		if not self.completed:
			self.completed = True
			self.completed_at = timezone.now()
			self.save(update_fields=['completed', 'completed_at'])

	def mark_incomplete(self) -> None:
		"""Mark the todo as not completed and clear `completed_at`."""
		if self.completed:
			self.completed = False
			self.completed_at = None
			self.save(update_fields=['completed', 'completed_at'])

