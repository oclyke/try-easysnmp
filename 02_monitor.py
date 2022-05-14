import time

from collections import namedtuple
from easysnmp import Session

# spell out the ipv4 address of the PDU here
HOST = '192.168.123.123'

# create session options
SessionOpts = namedtuple('SessionOpts', ['hostname', 'community', 'version'])
seshopts = SessionOpts(HOST, 'public', 1) # only version 1 seems to work atm

def monitor_factory():
  # there is a relatively convenient online version of the MIB that we can use for reference
  # https://bestmonitoringtools.com/mibdb/mibdb_search.php?mib=EATON-EPDU-MIB

  outlets = '1.3.6.1.4.1.534.6.6.7.6' # outlets oid
  outlet_voltage_entry = outlets + '.3.1'
  outlet_current_entry = outlets + '.4.1'
  outlet_power_entry = outlets + '.5.1'

  def voltage(outlet):
    raise Exception('voltage OID does not seem to work... this requires further investigation')
    return outlet_voltage_entry + f'.2.0.{outlet}'

  def current(outlet):
    return outlet_current_entry + f'.3.0.{outlet}'

  def power(outlet):
    return outlet_power_entry + f'.3.0.{outlet}'

  return (voltage, current, power)

#  main program execution
if __name__ == "__main__":
  session = Session(hostname=seshopts.hostname, community=seshopts.community, version=seshopts.version)
  (voltage, current, power) = monitor_factory()

  outlet = 1 # [1, 8]

  while True:
    time.sleep(0.25)
    watts, milliamps = (session.get(power(outlet)).value, session.get(current(outlet)).value)

    print(f'outlet ({outlet}): {watts} watts, [{milliamps} mA]')
