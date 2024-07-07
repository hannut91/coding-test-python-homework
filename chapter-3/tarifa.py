# Tarifa - https://dmoj.ca/problem/coci16c1p1
# 문제: 페로가 다음달에 몇 메가 바이트를 사용할 수 있는지 계산하라
# 자료:
#   인터넷 프로바이더는 한 달에 사용할 수 있는 메가바이트를 제공한다
#   그달의 받은 메가바이트를 전부 사용하지 않으면 다음달로 합산된다.
#   페로는 자신이 가진 메가바이트를 초과해서 사용할 수 없다.
# 계획:
#   인터넷 프로바이더가 한 달에 제공하는 메가바이트를 입력받는다
#     만약 이 메가 바이트가 정수가 아니거나 1 <= X <= 100사이가 아니라면 예외를 던진다
#   인터넷을 사용할 월 수를 입력받는다.
#     만약 이 월 수가 정수가 아니거나 1 <= N <= 100 사이가 아니라면 예외를 던진다.
#   각 월에 사용할 메가 바이트를 입력 받는다.
#     만약 입력한 메가 바이트가 정수가 아니거나 0 <= P <= 10,000 사이가 아니라면 예외를 던진다.
# 실행:
# 회고:
#   입력한 순서와 처리 순서가 고민이 되었음. 사용할 계획을 모두 받고 나서 계산할 것인지
#   혹은 입력받을 때마다 계산할지. 입력받고 나서 바로 계산하면 사용자가 기다릴 필요가 없으니
#   받자마자 계산하고 그 사이에 계산하기 위해서 바로 계산하는 전략을 취했음.

providingMegaByesPerMonthInput = input()
if not providingMegaByesPerMonthInput.isdigit():
    raise "인터넷 프로바이더가 한 달에 제공하는 메가바이트는 정수여야 합니다"

providingMegaByesPerMonth = int(providingMegaByesPerMonthInput)
if not 1 <= providingMegaByesPerMonth <= 100:
    raise "인터넷 프로바이더가 한 달에 제공하는 메가바이트는 1 ~ 100 사이여야 합니다"

planToUseInternetMonthCountInput = input()
if not planToUseInternetMonthCountInput.isdigit():
    raise "인터넷을 사용할 월 수는 정수여야 합니다"

planToUseInternetMonthCount = int(planToUseInternetMonthCountInput)
if not 1 <= planToUseInternetMonthCount <= 100:
    raise "인터넷을 사용할 월 수는 1 ~ 100 사이여야 합니다"

remainMegaByte = 0

for monthIndex in range(planToUseInternetMonthCount):
    remainMegaByte += providingMegaByesPerMonth

    planToUseMegaBytePerMonthInput = input()
    if not planToUseMegaBytePerMonthInput.isdigit():
        raise "매달 사용할 메가바이트는 정수여야 합니다"

    planToUseMegaBytePerMonth = int(planToUseMegaBytePerMonthInput)
    if not 0 <= planToUseMegaBytePerMonth <= 10000:
        raise "매달 사용할 메가바이트는 0~10000사이여야 합니다"

    remainMegaByte -= planToUseMegaBytePerMonth
    if remainMegaByte < 0:
        remainMegaByte = 0

print(remainMegaByte + providingMegaByesPerMonth)
