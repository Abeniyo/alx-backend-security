import requests

def get_geolocation_data(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return {
            "country": data.get("country"),
            "city": data.get("city")
        }
    except Exception:
        return {"country": None, "city": None}
