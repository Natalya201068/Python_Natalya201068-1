from address import Address
from mailing import Mailing


from_address_mailing = Address(400067, 'Волгоград', '64 Армии', '111', '15')
to_address_mailing = Address(400067, 'Волгоград', 'Козака', '9', '3')
cost_mailing = 1000
track_mailing = '1234567'

mailing = Mailing(to_address_mailing, from_address_mailing, cost_mailing,
                  track_mailing)

print(f"Отправление {track_mailing}, из "
      f"{from_address_mailing} в {to_address_mailing}. "
      f"Стоимость {cost_mailing} рублей.")
