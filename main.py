
from component.toutiao import TTBot

if __name__ == "__main__":
    print("run")

    bot = TTBot()
    account = bot.account
    print(account.name)
    print(account._account_info)
    print(account.media_info)