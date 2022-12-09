from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )
    confirm_password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    is_admin = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "confirm_password",
            "email",
            "first_name",
            "last_name",
            "is_admin",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["is_admin"] = instance.is_staff
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        # TODO: Move this to a different thread
        # create context for the email template
        context = {
            "name": user.first_name or user.email,
            "username": user.username,
            "customer_portal": "Let It Go",
        }

        # render email text
        email_html_message = render_to_string(
            "email/user_account_creation.html", context
        )
        email_plaintext_message = render_to_string(
            "email/user_account_creation.txt", context
        )

        # send an e-mail to the user
        msg = EmailMultiAlternatives(
            subject=f"Account created for the {context['customer_portal']} App",
            body=email_plaintext_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()

        return user
