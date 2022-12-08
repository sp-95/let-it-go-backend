from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from let_it_go_backend.apps.category.models import Category
from let_it_go_backend.apps.product.models import Product
from let_it_go_backend.apps.product.permissions import ProductPermission
from let_it_go_backend.apps.product.serializers import (
    ContactSerializer,
    ProductSerializer,
    VerificationSerializer,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["category", "condition", "owner", "verified"]
    search_fields = ["title", "description", "category"]

    def perform_create(self, serializer):
        category = Category.objects.get(id=serializer.initial_data["category"])
        serializer.save(category=category, owner=self.request.user)

    def perform_update(self, serializer):
        category = Category.objects.get(id=serializer.initial_data["category"])
        serializer.save(category=category)


class ContactView(UpdateAPIView):
    lookup_field = "id"
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_id = self.kwargs.get("id")
        product = Product.objects.filter(id=product_id)
        return product

    def perform_update(self, serializer):
        buyer = self.request.user
        product = serializer.instance
        seller = product.owner

        # Create context for email
        context = {
            "name": seller.first_name or seller.username,
            "buyer_first_name": buyer.first_name,
            "buyer_last_name": buyer.last_name,
            "buyer_email": buyer.email,
            "product": product.title,
            "customer_portal": "Let It Go",
        }

        # Render email text
        email_html_message = render_to_string("email/contact_seller.html", context)
        email_plaintext_message = render_to_string("email/contact_seller.txt", context)

        msg = EmailMultiAlternatives(
            subject=f"[{context['customer_portal']}] Found buyer for {context['product']}",  # noqa: E501
            body=email_plaintext_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[seller.email],
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()


class VerificationView(UpdateAPIView):
    lookup_field = "id"
    serializer_class = VerificationSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        product_id = self.kwargs.get("id")
        product = Product.objects.filter(id=product_id)
        return product
