from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    """
    # We can add related fields, like the host's username
    host_username = serializers.ReadOnlyField(source='host.username')
    
    class Meta:
        model = Listing
        # Include all fields from the model
        fields = [
            'id', 
            'title', 
            'host',
            'host_username',
            'description', 
            'address', 
            'city', 
            'country', 
            'price_per_night', 
            'max_guests', 
            'bedrooms', 
            'bathrooms',
            'created_at'
        ]
        # Mark 'host' as read-only, as it should be set automatically
        # based on the authenticated user making the request (in the view).
        read_only_fields = ['host']


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    """
    # Add related info for better API responses
    guest_username = serializers.ReadOnlyField(source='guest.username')
    listing_title = serializers.ReadOnlyField(source='listing.title')
    
    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'listing_title',
            'guest',
            'guest_username',
            'check_in_date',
            'check_out_date',
            'status',
            'created_at'
        ]
        # The guest should be set automatically from the request user
        read_only_fields = ['guest']
        