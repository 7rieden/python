
import pendulum
from datetime import datetime

pst = pendulum.timezone('Ameriaca/Los_Angeles')
ist = pendulum.timezone('Asia/Seoul')

print(type(pst))

print('Current Date Time in PST = ', datetime.now(pst))
print('Current Date Time in IST = ', datetime.now(ist))

pritn(type(ist))