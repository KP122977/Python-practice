# Exceptions

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")




def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc



def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient balance")
    return balance - amount
print(withdraw(500,1000))


def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")



try:
    pass
    raise KeyboardInterrupt

except KeyError:
    print("exception was raised")

finally:
    print('Goodbye, world!')

age=11
try:
    if age < 18:
        raise Exception("Underage")
except Exception:
    print("Not allowed")
