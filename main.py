import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = "+91##########"
number = ph.parse(number)

print("Timezone:", timezone.time_zones_for_number(number))
print("Carrier name:", carrier.name_for_number(number, "en"))
print("Location:", geocoder.description_for_number(number, 'en'))
