import requests

url = "https://www.ntpf.ie/home/OpenData/OpenData_IPDCNational01_2023.csv"

response = requests.get(url)

if response.status_code == 200:
    # Assuming the content is text (CSV)
    csv_content = response.text

    # Now you can process the CSV content as needed
    # For example, you can print the first 100 characters:
    print(csv_content[:100])
    
    # If you want to save the CSV to a file, you can do something like:
    with open("data.csv", "w") as file:
        file.write(csv_content)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
