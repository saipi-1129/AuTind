import requests

def get_recommendations():
    url = "https://api.gotinder.com/v2/recs/core?locale=ja&distance_setting=km"

    headers = {
        #App-Session-Id と X-Auth-Tokenを指定
        'App-Session-Id': '',
        #'User-Agent': 'Tinder Android Version 15.10.0',
        'X-Auth-Token': '',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        results = data.get("data", {}).get("results", [])
        for result in results:
            user = result.get("user", {})
            user_id = user.get("_id")
            user_name = user.get("name")
            print(f"ID: {user_id}, Name: {user_name}")
            like(user_id)  # 取得したユーザーに対してlikeを送る
    else:
        print(f"Error: {response.status_code}")

def like(user_id):
    url = f"https://api.gotinder.com/like/{user_id}"
    headers = {
        'X-Auth-Token': '',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Liked user with ID: {user_id}")
    else:
        print(f"Error: {response.status_code}")

# get_recommendations関数を呼び出して処理を開始
n = int(input("実行回数:"))
for i in range(n):
    get_recommendations()