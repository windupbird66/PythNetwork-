import requests


def check_eligibility(address):
    url = f"https://airdrop.pyth.network/api/grant/v1/evm_breakdown?identity={address}"
    try:
        response = requests.get(url)
        data = response.json()

        # 检查是否有资格
        if "error" in data:
            return None
        else:
            return data[0]['amount']
    except Exception as e:
        print(f"Error checking address {address}: {e}")
        return None


def main():
    # 这里列出了您要查询的地址列表，可以添加更多地址
    addresses = [
        "0xabcdefg1",
        "0xabcdefg2"
    ]

    for address in addresses:
        amount = check_eligibility(address)
        if amount:
            print(f"Address {address} is eligible with amount: {amount}")
        else:
            print(f"Address {address} is not eligible")


if __name__ == "__main__":
    main()
