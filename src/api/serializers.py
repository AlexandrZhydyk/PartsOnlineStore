from rest_framework import serializers

from accounts.models import Comment, CustomUser, Profile
from cart.models import Cart, CartItem
from catalogue.models import MachineModel, Part
from core.models import Shop


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(many=True, read_only=True)
    payment_type = serializers.SerializerMethodField("get_readable_payment_type")

    def get_readable_payment_type(self, model_object):
        readable_payment_type = model_object.get_payment_type_display()
        return readable_payment_type

    class Meta:
        model = Cart
        fields = ("creation_date", "payment_type", "payment_id", "cart_item")


class CustomUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "date_joined", "profile"]


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class MachineModelSerializer(serializers.ModelSerializer):
    machine_type = serializers.SerializerMethodField("get_readable_machine_type")

    def get_readable_machine_type(self, model_object):
        readable_machine_type = model_object.get_machine_type_display()
        return readable_machine_type

    class Meta:
        model = MachineModel
        fields = (
            "id",
            "model",
            "machine_type",
        )


class PartSerializer(serializers.ModelSerializer):
    shop = ShopSerializer(many=True, read_only=True)
    machine_model = MachineModelSerializer(many=True, read_only=True)

    class Meta:
        model = Part
        fields = ("part_number", "part_name", "price", "description", "shop", "machine_model", "machine_system")


class PartDetailSerializer(PartSerializer):
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Part
        fields = (
            "part_number",
            "part_name",
            "price",
            "remark",
            "shop",
            "machine_model",
            "comment",
        )


class PartModelSerializer(MachineModelSerializer):
    part = PartSerializer(many=True, read_only=True)

    class Meta:
        model = MachineModel
        fields = (
            "id",
            "model",
            "machine_type",
            "part",
        )
