#!/usr/bin/env python3
import aws_cdk as cdk
from restaurant_reservation.restaurant_reservation_stack import RestaurantReservationStack

app = cdk.App()
RestaurantReservationStack(app, "RestaurantReservationStack")
app.synth()