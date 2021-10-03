import requests
from bs4 import BeautifulSoup

page = requests.get("https://weather.com/weather/tenday/l/ba10c9ce6f4d065f3e35386c115af4bc80b262f2aa4a2e56faebdb1c82549e6f#detailIndex5")
soup = BeautifulSoup(page.content, "html.parser")
AllForecasts = soup.find("div", class_="DailyForecast--DisclosureList--350ZO")
Forecasts = AllForecasts.find_all("details")
Days = []
Temperatures = []
Conditions = []
Rain = []

for i in range(len(Forecasts)):

    DayText = Forecasts[i].find("h2", class_="DetailsSummary--daypartName--1Mebr").text
    Days.append(DayText)

    TemperatureText = Forecasts[i].find("span", class_="DetailsSummary--highTempValue--3x6cL").text
    Temperatures.append(TemperatureText)

    ConditionText = Forecasts[i].find("span", class_="DetailsSummary--extendedData--aaFeV").text
    Conditions.append(ConditionText)

    RainContainer = Forecasts[i].find("div", class_="DetailsSummary--precip--2ARnx")
    RainText = RainContainer.find("span").text
    Rain.append(RainText)

Temperatures[0] = Forecasts[0].find("span", class_="DailyContent--temp--_8DL5").text

print(Days)
print(Temperatures)
print(Conditions)
print(Rain)