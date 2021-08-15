from tkinter import *
import requests
import json

root = Tk()
root.title("Check Air Quality")

info = None

# delete label
def delete_label():
   last_output.destroy()

# create zipcode lookup function
def zipLookup():
   try:
      api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(input.get()) + "&distance=5&API_KEY=FF96355D-C2FF-4DA1-B5D3-0B55696804E7")
      api = json.loads(api_request.content)
      city = api[0]["ReportingArea"]
      quality = api[0]["AQI"]
      category = api[0]["Category"]["Name"]

      weather_color = ""
      if category == "Good":
         weather_color = "#00e400"
      elif category == "Moderate":
         weather_color = "#ffff00"
      elif category == "Unhealthy for Sensitive Groups":
         weather_color = "#ff7e00"
      elif category == "Unhealthy":
         weather_color = "#ff0000"
      elif category == "Very Unhealthy":
         weather_color = "#8f3f97"
      elif category == "Hazardous":
         weather_color = "#7e0023"

      global info
      if info != None:
         delete_label()
      info = city + " Air Quality " + str(quality) + " " + category
      global last_output
      last_output = Label(root, text=info, font=("Helvetica", 12), background=weather_color)
      last_output.grid(row=1, column=0, columnspan=2)

   except Exception as e:
      if info != None:
         delete_label()
      info = "Error..."
      last_output = Label(root, text=info)
      last_output.grid(row=1, column=0, columnspan=2)

input = Entry(root)
input.grid(row=0, column=0, sticky=W+E+N+S)

zip_button = Button(root, text="Lookup Zipcode", command=zipLookup)
zip_button.grid(row=0, column=1, sticky=W+E+N+S)

root.mainloop()