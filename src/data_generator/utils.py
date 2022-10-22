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
            "countgry_code": fake.country_code(),
            "postcode": fake.postcode(),
            "street_address": fake.street_address(),
            "street_name": fake.street_name()
        }


class Properties(Enum):
    PERSON = "Person"
    FULL_PROFILE = "FullProfile"
    SIMPLE_PROFILE = "SimpleProfile"
    ADDRESS = "Address"
