import time
from datetime import datetime
from django.http import JsonResponse
from collections import defaultdict
from django.http import JsonResponse
class RolepermissionMiddleware:
    """
    Middleware to allow only admin or moderator users
    to access specific actions or routes.
    """

    # Define paths requiring admin/moderator access
    RESTRICTED_PATHS = [
        "/api/admin/",
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path is restricted
        if any(request.path.startswith(path) for path in self.RESTRICTED_PATHS):
            user = request.user
            if not user.is_authenticated:
                return JsonResponse({"detail": "Authentication required."}, status=403)

            if user.role not in ["admin", "moderator"]:
                return JsonResponse({"detail": "You do not have permission to access this resource."}, status=403)

        response = self.get_response(request)
        return response


class OffensiveLanguageMiddleware:
    """
    Middleware to limit the number of POST requests (messages) per IP address.
    Limit: 5 messages per minute.
    """

    # Shared state across requests
    ip_message_log = defaultdict(list)

    MAX_MESSAGES = 5
    TIME_WINDOW = 60  # seconds

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only apply to message POST requests
        if request.path.startswith("/api/messages/") and request.method == "POST":
            ip = self.get_client_ip(request)
            current_time = time.time()

            # Clean up old timestamps
            self.ip_message_log[ip] = [
                timestamp
                for timestamp in self.ip_message_log[ip]
                if current_time - timestamp < self.TIME_WINDOW
            ]

            if len(self.ip_message_log[ip]) >= self.MAX_MESSAGES:
                return JsonResponse(
                    {
                        "detail": "Message limit exceeded. "
                                  "You can only send 5 messages per minute."
                    },
                    status=429,
                )

            # Log current request
            self.ip_message_log[ip].append(current_time)

        response = self.get_response(request)
        return response

    @staticmethod
    def get_client_ip(request):
        """Get the client IP address"""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR", "")
        return ip
class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"

        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"

        with open("requests.log", "a") as log_file:
            log_file.write(log_message + "\n")

        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour

        # Allowed between 06:00 and 21:00
        if current_hour < 6 or current_hour >= 21:
            return JsonResponse(
                {
                    "detail": "Messaging service is unavailable at this time. "
                              "Access allowed between 6:00 AM and 9:00 PM."
                },
                status=403
            )

        response = self.get_response(request)
        return response
