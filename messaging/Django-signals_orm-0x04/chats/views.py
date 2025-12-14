from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter
class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        # Only show conversations the user participates in
        return Conversation.objects.filter(
            participants=self.request.user
        )

    def create(self, request, *args, **kwargs):
        """
        Create a new conversation
        Expected payload:
        {
            "participants": ["uuid1", "uuid2"]
        }
        """
        participant_ids = request.data.get("participants", [])

        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, *participant_ids)

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        return Message.objects.filter(
            conversation__participants=self.request.user
        ).order_by("-sent_at")
    def get_queryset(self):
        conversation_id = self.request.query_params.get("conversation_id")

        if not conversation_id:
            return Message.objects.none()
#cs
        return  Message.objects.filter(
            conversation__participants=self.request.user
        ).order_by("-sent_at")

    def perform_create(self, serializer):
        conversation_id = self.request.data.get("conversation_id")

        conversation = Conversation.objects.filter(
            id=conversation_id,
            participants=self.request.user
        ).first()

        if not conversation:
            raise PermissionError("You are not part of this conversation")

        serializer.save(
            sender=self.request.user,
            conversation=conversation
        )


