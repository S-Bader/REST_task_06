from rest_framework.permissions import BasePermission
from datetime import date


class IsOwnerOrStaff(BasePermission):
	message = "You don't have the authority to access this."

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or request.user == obj.user:
			return True
		return False

class UpcomingBookingsOnly(BasePermission):
	message = "Too late to Modify"

	def has_object_permission(self, request, view, obj):
		days_left = (obj.date - date.today()).days

		if days_left > 3:
			return True
		return False



