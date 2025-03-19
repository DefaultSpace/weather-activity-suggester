import requests

# API anahtarınızı buraya yapıştırın.
API_KEY = "33cdac3bfd96f89899d7d0d3eb11b774"  # Lütfen buraya kendi Weatherstack API anahtarınızı ekleyin.
API_URL = "http://api.weatherstack.com/current"

# İngilizce-Türkçe hava durumu çeviri sözlüğü (Temel Terimler)
WEATHER_TRANSLATIONS = {
    "Sunny": "Güneşli",
    "Clear": "Açık",
    "Partly cloudy": "Parçalı bulutlu",
    "Cloudy": "Bulutlu",
    "Overcast": "Kapalı",
    "Rainy": "Yağmurlu",
    "Light rain": "Hafif yağmurlu",
    "Moderate rain": "Orta şiddetli yağmurlu",
    "Heavy rain": "Şiddetli yağmurlu",
    "Patchy rain possible": "Yer yer yağmur ihtimali",
    "Light drizzle": "Hafif çiseleme",
    "Moderate or heavy drizzle": "Orta veya şiddetli çiseleme",
    "Patchy light drizzle": "Yer yer hafif çiseleme",
    "Light rain shower": "Hafif sağanak yağmur",
    "Moderate or heavy rain shower": "Orta veya şiddetli sağanak yağmur",
    "Patchy light rain with thunder": "Gök gürültülü yer yer hafif yağmur",
    "Moderate or heavy rain with thunder": "Gök gürültülü orta veya şiddetli yağmur",
    "Mist": "Sisli",
    "Fog": "Sisle",
    "Snow": "Karlı",
    "Light snow": "Hafif karlı",
    "Moderate snow": "Orta şiddetli karlı",
    "Heavy snow": "Şiddetli karlı",
    "Patchy snow possible": "Yer yer kar ihtimali",
    "Light snow showers": "Hafif kar sağanakları",
    "Moderate or heavy snow showers": "Orta veya şiddetli kar sağanakları",
    "Patchy light snow with thunder": "Gök gürültülü yer yer hafif kar",
    "Moderate or heavy snow with thunder": "Gök gürültülü orta veya şiddetli kar",
    "Sleet": "Sulu kar",
    "Light sleet": "Hafif sulu kar",
    "Moderate sleet": "Orta şiddetli sulu kar",
    "Heavy sleet": "Şiddetli sulu kar",
    "Patchy sleet possible": "Yer yer sulu kar ihtimali",
    "Light sleet showers": "Hafif sulu kar sağanakları",
    "Moderate or heavy sleet showers": "Orta veya şiddetli sulu kar sağanakları",
    "Patchy light sleet with thunder": "Gök gürültülü yer yer hafif sulu kar",
    "Moderate or heavy sleet with thunder": "Gök gürültülü orta veya şiddetli sulu kar",
    "Thundery outbreaks possible": "Gök gürültülü sağanak ihtimali",
    "Patchy freezing drizzle possible": "Yer yer donan çiseleme ihtimali",
    "Freezing fog": "Dondurucu sis",
    "Blowing snow": "Savrulan kar",
    "Blizzard": "Kar fırtınası",
    "Ice pellets": "Buz taneleri",
    "Light ice pellets": "Hafif buz taneleri",
    "Moderate ice pellets": "Orta şiddetli buz taneleri",
    "Heavy ice pellets": "Şiddetli buz taneleri",
    "Patchy ice pellets possible": "Yer yer buz taneleri ihtimali",
    "Light ice pellets showers": "Hafif buz taneleri sağanakları",
    "Moderate or heavy ice pellets showers": "Orta veya şiddetli buz taneleri sağanakları",
    "Patchy light ice pellets with thunder": "Gök gürültülü yer yer hafif buz taneleri",
    "Moderate or heavy ice pellets with thunder": "Gök gürültülü orta veya şiddetli buz taneleri",
    "Freezing drizzle": "Donan çiseleme",
    "Freezing rain": "Donan yağmur",
    "Light freezing rain": "Hafif donan yağmur",
    "Moderate freezing rain": "Orta şiddetli donan yağmur",
    "Heavy freezing rain": "Şiddetli donan yağmur",
    "Patchy freezing rain possible": "Yer yer donan yağmur ihtimali",
    "Light freezing rain showers": "Hafif donan yağmur sağanakları",
    "Moderate or heavy freezing rain showers": "Orta veya şiddetli donan yağmur sağanakları",
    "Patchy light freezing rain with thunder": "Gök gürültülü yer yer hafif donan yağmur",
    "Moderate or heavy freezing rain with thunder": "Gök gürültülü orta veya şiddetli donan yağmur",
    "Thunder": "Gök gürültüsü",
    "Thunderstorm": "Gök gürültülü fırtına",
    "Thunderstorms": "Gök gürültülü fırtınalar",
    "Thunder in the vicinity": "Yakınlarda gök gürültüsü",
    "Thunderstorm in the vicinity": "Yakınlarda gök gürültülü fırtına",
    "Thunderstorms in the vicinity": "Yakınlarda gök gürültülü fırtınalar",
    "Squalls": "Sağanaklar",
    "Sandstorm": "Kum fırtınası",
    "Duststorm": "Toz fırtınası",
    "Sand": "Kum",
    "Dust": "Toz",
    "Smoke": "Duman",
    "Haze": "Pus",
    "Whirls": "Girdaplar",
    "Tornado": "Hortum",
    "Funnel cloud": "Hortum bulutu",
    "Waterspout": "Su hortumu",
    "Hail": "Dolu",
    "Light hail": "Hafif dolu",
    "Moderate hail": "Orta şiddetli dolu",
    "Heavy hail": "Şiddetli dolu",
    "Patchy hail possible": "Yer yer dolu ihtimali",
    "Light hail showers": "Hafif dolu sağanakları",
    "Moderate or heavy hail showers": "Orta veya şiddetli dolu sağanakları",
    "Patchy light hail with thunder": "Gök gürültülü yer yer hafif dolu",
    "Moderate or heavy hail with thunder": "Gök gürültülü orta veya şiddetli dolu",
    "Small hail": "Küçük dolu",
    "Small hail showers": "Küçük dolu sağanakları",
    "Small hail with thunder": "Gök gürültülü küçük dolu",
    "Small hail in the vicinity": "Yakınlarda küçük dolu",
    "Small hail showers in the vicinity": "Yakınlarda küçük dolu sağanakları",
    "Small hail with thunder in the vicinity": "Yakınlarda gök gürültülü küçük dolu",
}


def get_weather_data(city_name):
    """
    Belirtilen şehir için Weatherstack API'sinden hava durumu verilerini alır.

    Args:
        city_name (str): Hava durumu verisi alınacak şehrin adı.

    Returns:
        dict: Hava durumu verilerini içeren bir sözlük veya hata durumunda None.
    """
    params = {
        "query": city_name,
        "access_key": API_KEY,
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Hata durumunda HTTPError yükseltir.
        data = response.json()
        if "error" in data:
            print(f"Hava durumu alınamadı: {data['error']['info']}")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"Hava durumu alınamadı: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Hava durumu alınamadı: {e}")
        return None
    except ValueError as e:
        print(f"Hava durumu verisi işlenemedi: {e}")
        return None


def suggest_activity(weather_condition):
    """
    Hava durumuna göre bir etkinlik önerir.

    Args:
        weather_condition (str): Hava durumu (örneğin, "Sunny", "Rainy", "Cloudy").

    Returns:
        str: Önerilen etkinlik.
    """
    weather_condition_lower = weather_condition.lower()
    if "rain" in weather_condition_lower or "drizzle" in weather_condition_lower or "shower" in weather_condition_lower:
        return "Müze gezisi yapabilirsiniz."
    elif "clear" in weather_condition_lower or "sunny" in weather_condition_lower:
        return "Piknik yapabilirsiniz."
    elif "cloud" in weather_condition_lower or "overcast" in weather_condition_lower:
        return "Kafede oturup kitap okuyabilirsiniz."
    else:
        return "Kapalı alanda film izleyebilirsiniz."


def display_weather_and_suggestion(city_name, weather_data):
    """
    Hava durumu ve etkinlik önerisini ekrana yazdırır.

    Args:
        city_name (str): Şehir adı.
        weather_data (dict): Hava durumu verilerini içeren sözlük.
    """
    if weather_data:
        temperature = weather_data["current"]["temperature"]
        weather_description_en = weather_data["current"]["weather_descriptions"][0]
        # İngilizce hava durumu açıklamasını Türkçe'ye çevir
        weather_description_tr = WEATHER_TRANSLATIONS.get(weather_description_en, weather_description_en)
        suggestion = suggest_activity(weather_description_en)

        print(f"{city_name} için Hava Durumu:")
        print(f"Sıcaklık: {temperature}°C")
        print(f"Durum: {weather_description_tr}")  # Türkçe açıklamayı yazdır
        print(f"Öneri: {suggestion}")
    else:
        print("Hava durumu alınamadı, şehir adını kontrol edin.")


def main():
    """
    Ana fonksiyon, kullanıcıdan şehir adını alır, hava durumunu çeker ve öneriyi gösterir.
    Kullanıcıya başka bir hava durumu öğrenmek isteyip istemediğini sorar ve cevaba göre tekrar çalışır.
    """
    while True:
        city = input("Hava durumu için bir şehir adı girin: ")
        weather_data = get_weather_data(city)
        display_weather_and_suggestion(city, weather_data)

        while True:
            continue_choice = input(
                "Başka bir hava durumu öğrenmek ister misiniz? (e/h): "
            ).lower()
            if continue_choice in ["e", "h"]:
                break
            else:
                print("Geçersiz giriş. Lütfen 'e' veya 'h' girin.")

        if continue_choice == "h":
            break


if __name__ == "__main__":
    main()
