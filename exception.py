class Voterageminor(Exception):
    def __init__(self,message):
        self.message = message

voterage = int(input("enter voter age :"))

try :

    if voterage < 18:
        raise Voterageminor("Minors cant vote")
    print("You can vote")

except Exception as e:
    print(e)

    print("Wait till you turn 18")