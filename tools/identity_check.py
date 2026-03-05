import requests

def who_is_my_isp():
    print("--- Emerald Diagnostic: Identity Check ---")
    try:
        # Reaching out to a free IP API
        response = requests.get('http://ip-api.com/json/')
        data = response.json()

        if data['status'] == 'success':
            print(f"Public IP:  {data['query']}")
            print(f"ISP:        {data['isp']}")
            print(f"Location:   {data['city']}, {data['regionName']}")
            print(f"Status:     Verified {data['isp']} Connection")
        else:
            print("Error: Could not retrieve ISP data.")
            
    except Exception as e:
        print(f"Critical Error: {e}")

if __name__ == "__main__":
    who_is_my_isp()
