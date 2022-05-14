import time

from collections import namedtuple
from easysnmp import Session

# spell out the ipv4 address of the PDU here
HOST = '192.168.123.123'

# create session options
SessionOpts = namedtuple('SessionOpts', ['hostname', 'community', 'version'])
seshopts = SessionOpts(HOST, 'public', 1) # only version 1 seems to work atm

def onoff_factory():
  # there is a relatively convenient online version of the MIB that we can use for reference
  # https://bestmonitoringtools.com/mibdb/mibdb_search.php?mib=EATON-EPDU-MIB

  outlets = '1.3.6.1.4.1.534.6.6.7.6' # outlets oid
  outlet_control = outlets + '.6' # the outlet control identifier is 6
  outlet_control_on_cmd = outlet_control + '.1.4' # there is a single instance of outlet control on which id 4 is the on cmd
  outlet_control_off_cmd = outlet_control + '.1.3' # similarly id 3 is the off cmd on the outlet control instance

  def off_cmd(outlet):
    return outlet_control_off_cmd + f'.0.{outlet}'

  def on_cmd(outlet):
    return outlet_control_on_cmd + f'.0.{outlet}'

  return (on_cmd, off_cmd)

# main program execution
if __name__ == "__main__":
  # Create an SNMP session to be used for all our requests
  session = Session(hostname=seshopts.hostname, community=seshopts.community, version=seshopts.version)
  (get_on_cmd_oid, get_off_cmd_oid) = onoff_factory()

  while True:
    time.sleep(1)

    # Set a variable using an SNMP SET
    session.set(get_off_cmd_oid(1), '1', 'INTEGER')

    time.sleep(1)

    # Set a variable using an SNMP SET
    session.set(get_on_cmd_oid(1), '1', 'INTEGER')
