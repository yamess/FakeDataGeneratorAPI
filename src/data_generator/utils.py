from enum import Enum

from faker import Faker


class Person(Enum):
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    LANGUAGE_NAME = "language_name"
    PREFIX = "prefix"

    @staticmethod
    def generate(fake: Faker):
        return {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "language_name": fake.language_name(),
            "prefix": fake.prefix()
        }


class FullProfile(Enum):
    FULL_PROFILE = "profile"

    @staticmethod
    def generate(fake: Faker):
        return fake.profile()


class SimpleProfile(Enum):
    SIMPLE_PROFILE = "simple_profile"

    @staticmethod
    def generate(fake: Faker):
        return fake.simple_profile()


class Address(Enum):
    ADDRESS = "address"
    BUILDING_NUMBER = "building_number"
    CITY = "city"
    COUNTRY = "country"
    COUNTRY_CODE = "country_code"
    POSTCODE = "post_code"
    STREET_ADDRESS = "street_address"
    STREET_NAME = "street_name"

    @staticmethod
    def generate(fake: Faker):
        return {
            "address": fake.address(),
            "building_number": fake.building_number(),
            "city": fake.city(),
            "country": fake.country(),
            "country_code": fake.country_code(),
            "postcode": fake.postcode(),
            "street_address": fake.street_address(),
            "street_name": fake.street_name()
        }


class Bank(Enum):
    ABA = "aba"
    BANK_COUNTRY = "bank_country"
    BBAN = "bban"
    IBAN = "iban"
    SWIFT = "swift"
    SWIFT8 = "swift8"
    SWIFT11 = "swift11"

    @staticmethod
    def generate(fake: Faker):
        return {
            "aba": fake.aba(),
            "bank_country": fake.bank_country(),
            "bban": fake.bban(),
            "iban": fake.iban(),
            "swift": fake.swift(),
            "swift8": fake.swift8(),
            "swift11": fake.swift11()
        }


class Airport(Enum):
    AIRPORT = "airport"
    AIRLINE = "airline"
    FLIGHT = "flight"

    @staticmethod
    def generate(fake: Faker):
        return {
            "airport": fake.airport_object(),
            "airline": fake.airline(),
            "flight": fake.flight()
        }


class Schools(Enum):
    SCHOOL = "school"

    @staticmethod
    def generate(fake: Faker):
        return fake.school_object()


class Vehicule(Enum):
    VEHICULE = "vehicule"
    MACHINE_OBJECT = "machine_object"

    @staticmethod
    def generate(fake: Faker):
        return {"vehicule": fake.vehicle_object(), "machine": fake.machine_object()}


class GeoPoint(Enum):
    LONGITUDE = "longitude"
    LATITUDE = "latitude"
    LAT_LONG = "latlng"
    LOCAL_LAT_LNG = "local_latlng"
    LOCATION_ON_LAND = "location_on_land"

    @staticmethod
    def generate(fake: Faker):
        return {
            "longitude": fake.longitude(),
            "latitude": fake.latitude(),
            "lat_long": fake.latlng(),
            "local_lat_long": fake.local_latlng(),
            "location_on_land": fake.location_on_land()
        }


class Properties(Enum):
    PERSON = "Person"
    FULL_PROFILE = "FullProfile"
    SIMPLE_PROFILE = "SimpleProfile"
    ADDRESS = "Address"
    BANK = "bank"
    AIRPORT = "airport"
    SCHOOLS = "schools"
    VEHICULE = "vehicule"
