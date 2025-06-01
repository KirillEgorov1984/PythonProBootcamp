from openpyxl import load_workbook

wb = load_workbook("E:\\StopListForOrderRecommendationOriginal.xlsx")
ws = wb["Аркуш1"]

# Защита листа
ws.protection.sheet = True
ws.protection.password = "dn1000"

wb.save("E:\\StopListForOrderRecommendationOriginal.xlsx")