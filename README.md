# easysnmp for EATON EMAT10-10
what's going on here? well we are trying to bring up the EATON EMAT10-10 PDU for truck 601 real quick. the PDU has an SNMP interface to allow controlling and monitoring the outlets. naturally it seems like a good time to use Kwabena's old work from the UPS -- but no, the pysnmp module depends on compiling MIBs into python syntax (at least for the high level api) and this compilation process depends on cached MIBs hosted on the internet. sadly the service hosting these has been allowed to die and now MIBs are 'compiled' into what are effectively ```404``` html pages -- less than useful.

furthermore the pysnmp package is just downright wild, complicated, and un-pythonic. in searching for a solution to the above issue the ```easysnmp``` module caught my eye. one big perk: straightforward and not dependent on MIBs.

# installing
the [EasySNMP Documentation](https://easysnmp.readthedocs.io/en/latest/index.html#) makes it really easy to get started. the (ubuntu) steps are duplicated here for good measure:

* sudo apt-get install libsnmp-dev snmp-mibs-downloader
* sudo apt-get install gcc python-dev
* pip install easysnmp

**caveats**
* ```easysnmp``` relies on the ```net-snmp``` C library. this makes is not particularly windows-pleasing. but we should be ok with that as we run brain on ubuntu and seem to be transitioning to *nix systems everywhere.
* ```easysnmp``` may exhibit unhappiness when being installed or invoked from within a python virtual environment

# general usage
to avoid depending on MIBs and their strange awfulness we can simply identify the Object IDs (OIDs) that correspond to the data or control points we are interested in. then we can use ```EasySNMP``` to get/set the values.

# online MIB
far better than trying to read a MIB text file... [this convenient resource](https://bestmonitoringtools.com/mibdb/mibdb_search.php) hosts pretty versions of the MIBs we need.

* [EATON-EPDU-MIB](https://bestmonitoringtools.com/mibdb/mibdb_search.php?mib=EATON-EPDU-MIB)
