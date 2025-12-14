from rest_framework.permissions import BasePermission


class IsParticipantOfConversation(BasePermission):
    """
    Allows access only to authenticated users
    who are participants of the conversation.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        obj can be a Message or Conversation
        """

        # If object is a Conversation
        if hasattr(obj, "participants"):
            return request.user in obj.participants.all()

        # If object is a Message
        if hasattr(obj, "conversation"):
            return request.user in obj.conversation.participants.all()

        return False
