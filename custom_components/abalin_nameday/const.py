"""Constants for the Abalin Nameday integration."""

DOMAIN = "abalin_nameday"

API_BASE_URL = "https://nameday.abalin.net/api"

UPDATE_INTERVAL_MINUTES = 1440  # once per day — nameday data only changes at midnight
REQUEST_TIMEOUT = 10

CONF_COUNTRY = "country"

# 20 countries supported by the Abalin API
COUNTRIES: list[dict[str, str]] = [
    {"value": "at", "label": "Austria"},
    {"value": "bg", "label": "Bulgaria"},
    {"value": "hr", "label": "Croatia"},
    {"value": "cz", "label": "Czech Republic"},
    {"value": "dk", "label": "Denmark"},
    {"value": "ee", "label": "Estonia"},
    {"value": "fi", "label": "Finland"},
    {"value": "fr", "label": "France"},
    {"value": "de", "label": "Germany"},
    {"value": "gr", "label": "Greece"},
    {"value": "hu", "label": "Hungary"},
    {"value": "it", "label": "Italy"},
    {"value": "lv", "label": "Latvia"},
    {"value": "lt", "label": "Lithuania"},
    {"value": "pl", "label": "Poland"},
    {"value": "ru", "label": "Russia"},
    {"value": "sk", "label": "Slovakia"},
    {"value": "es", "label": "Spain"},
    {"value": "se", "label": "Sweden"},
    {"value": "us", "label": "United States"},
]

COUNTRY_NAMES: dict[str, str] = {c["value"]: c["label"] for c in COUNTRIES}
