import json
with open("SQL//ebaty.json", encoding="utf-8") as file:
    huba = json.load(file)

with open("AI//data.txt", "w", encoding="utf-8") as file:
    for i in huba:
        file.write(
            f"Id: {i['Id']} {i['Название']} - {i['Стоимость']}\n"
        )