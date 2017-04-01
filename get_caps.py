# Imports
from selenium import webdriver
from PIL import Image
import io

# What site are we getting?
site_array = ["google.com", "www.bbc.co.uk/news"]

# Set up the Selenium driver
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768) # set the window size that you need 

for site in site_array:
  # Get the screencaps!
  driver.get("https://" + site)

  # Convert the image to a gif
  png_blob = driver.get_screenshot_as_png()

  # Output the file
  output_name = (site + ".gif").replace("/", "_")
  Image.open(io.BytesIO(png_blob)).crop((0, 0, 1024, 768)).save("pics/" + output_name)


