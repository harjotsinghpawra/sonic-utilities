import sys
import os
import json
from unittest import mock

import click
from click.testing import CliRunner
from .mock_tables import dbconnector

test_path = os.path.dirname(os.path.abspath(__file__))
modules_path = os.path.dirname(test_path)
scripts_path = os.path.join(modules_path, "scripts")
sys.path.insert(0, modules_path)

class MockerConfig(object):
    ignore_devices = []
    ignore_services = []
    first_time = True

    def config_file_exists(self):
        if MockerConfig.first_time:
            MockerConfig.first_time = False
            return False
        else:
            return True

class MockerManager(object):
    counter = 0

    def __init__(self):
        self.config = MockerConfig()

    def check(self, chassis):
        if MockerManager.counter == 0:
            stats = {'Services': {'neighsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vrfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'telemetry': {'status': 'Not OK', 'message': 'telemetry is not Running', 'type': 'Process'}, 'dialout_client': {'status': 'OK', 'message': '', 'type': 'Process'}, 'zebra': {'status': 'OK', 'message': '', 'type': 'Process'}, 'rsyslog': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'redis_server': {'status': 'OK', 'message': '', 'type': 'Process'}, 'intfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'orchagent': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vxlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldpd_monitor': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'var-log': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'lldpmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sonic': {'status': 'OK', 'message': '', 'type': 'System'}, 'buffermgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'staticd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldp_syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpcfgd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmp_subagent': {'status': 'Not OK', 'message': 'snmp_subagent is not Running', 'type': 'Process'}, 'root-overlay': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'fpmsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sflowmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'nbrmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}}, 'Hardware': {'psu_1_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'psu_2_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'PSU 1': {'status': 'OK', 'message': '', 'type': 'PSU'}, 'fan10': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'PSU 2': {'status': 'OK', 'message': '', 'type': 'PSU'}, 'ASIC': {'status': 'OK', 'message': '', 'type': 'ASIC'}, 'fan1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan3': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan2': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan5': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan4': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan7': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan6': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan9': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan8': {'status': 'OK', 'message': '', 'type': 'Fan'}}}
        elif MockerManager.counter == 1:
            stats = {'Services': {'neighsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vrfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'telemetry': {'status': 'OK', 'message': '', 'type': 'Process'}, 'dialout_client': {'status': 'OK', 'message': '', 'type': 'Process'}, 'zebra': {'status': 'OK', 'message': '', 'type': 'Process'}, 'rsyslog': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'redis_server': {'status': 'OK', 'message': '', 'type': 'Process'}, 'intfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'orchagent': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vxlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldpd_monitor': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'var-log': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'lldpmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sonic': {'status': 'OK', 'message': '', 'type': 'System'}, 'buffermgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'staticd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldp_syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpcfgd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmp_subagent': {'status': 'OK', 'message': '', 'type': 'Process'}, 'root-overlay': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'fpmsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sflowmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'nbrmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}}, 'Hardware': {'psu_1_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'psu_2_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'PSU 1': {'status': 'OK', 'message': '', 'type': 'PSU'}, 'fan10': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'PSU 2': {'status': 'OK', 'message': '', 'type': 'PSU'}, 'ASIC': {'status': 'OK', 'message': '', 'type': 'ASIC'}, 'fan1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan3': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan2': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan5': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan4': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan7': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan6': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan9': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan8': {'status': 'OK', 'message': '', 'type': 'Fan'}}}
        elif MockerManager.counter == 2:
            stats = {'Services': {'neighsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vrfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'telemetry': {'status': 'Not OK', 'message': 'telemetry is not Running', 'type': 'Process'}, 'dialout_client': {'status': 'OK', 'message': '', 'type': 'Process'}, 'zebra': {'status': 'OK', 'message': '', 'type': 'Process'}, 'rsyslog': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'redis_server': {'status': 'OK', 'message': '', 'type': 'Process'}, 'intfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'orchagent': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vxlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldpd_monitor': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'var-log': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'lldpmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sonic': {'status': 'OK', 'message': '', 'type': 'System'}, 'buffermgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'staticd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldp_syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpcfgd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmp_subagent': {'status': 'OK', 'message': '', 'type': 'Process'}, 'root-overlay': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'fpmsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sflowmgrd': {'status': 'Not OK', 'message': 'sflowmgrd is not Running', 'type': 'Process'}, 'vlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'nbrmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}}, 'Hardware': {'PSU 2': {'status': 'OK', 'message': '', 'type': 'PSU'}, 'psu_1_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'psu_2_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan11': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan10': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan12': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'ASIC': {'status': 'OK', 'message': '', 'type': 'ASIC'}, 'fan1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'PSU 1': {'status': 'OK', 'message': '', 'type': 'PSU'}, 'fan3': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan2': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan5': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan4': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan7': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan6': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan9': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan8': {'status': 'OK', 'message': '', 'type': 'Fan'}}}
        elif MockerManager.counter == 3:
            stats = {'Services': {'neighsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vrfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'telemetry': {'status': 'Not OK', 'message': 'telemetry is not Running', 'type': 'Process'}, 'dialout_client': {'status': 'OK', 'message': '', 'type': 'Process'}, 'zebra': {'status': 'OK', 'message': '', 'type': 'Process'}, 'rsyslog': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'redis_server': {'status': 'OK', 'message': '', 'type': 'Process'}, 'intfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'orchagent': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vxlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldpd_monitor': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'var-log': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'lldpmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sonic': {'status': 'OK', 'message': '', 'type': 'System'}, 'buffermgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'staticd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldp_syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpcfgd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmp_subagent': {'status': 'OK', 'message': '', 'type': 'Process'}, 'root-overlay': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'fpmsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sflowmgrd': {'status': 'Not OK', 'message': 'sflowmgrd is not Running', 'type': 'Process'}, 'vlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'nbrmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}}, 'Hardware': {'PSU 2': {'status': 'Not OK', 'message': 'Failed to get voltage minimum threshold data for PSU 2', 'type': 'PSU'}, 'psu_1_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'psu_2_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan11': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan10': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan12': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'ASIC': {'status': 'OK', 'message': '', 'type': 'ASIC'}, 'fan1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'PSU 1': {'status': 'Not OK', 'message': 'Failed to get voltage minimum threshold data for PSU 1', 'type': 'PSU'}, 'fan3': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan2': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan5': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan4': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan7': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan6': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan9': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan8': {'status': 'OK', 'message': '', 'type': 'Fan'}}}
        elif MockerManager.counter == 4:
            stats = {'Services': {'neighsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vrfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'telemetry': {'status': 'Not OK', 'message': 'telemetry is not Running', 'type': 'Process'}, 'dialout_client': {'status': 'OK', 'message': '', 'type': 'Process'}, 'zebra': {'status': 'OK', 'message': '', 'type': 'Process'}, 'rsyslog': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'redis_server': {'status': 'OK', 'message': '', 'type': 'Process'}, 'intfmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'orchagent': {'status': 'OK', 'message': '', 'type': 'Process'}, 'vxlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldpd_monitor': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'var-log': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'lldpmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sonic': {'status': 'OK', 'message': '', 'type': 'System'}, 'buffermgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'portmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'staticd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'lldp_syncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'bgpcfgd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'snmp_subagent': {'status': 'OK', 'message': '', 'type': 'Process'}, 'root-overlay': {'status': 'OK', 'message': '', 'type': 'Filesystem'}, 'fpmsyncd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'sflowmgrd': {'status': 'Not OK', 'message': 'sflowmgrd is not Running', 'type': 'Process'}, 'vlanmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}, 'nbrmgrd': {'status': 'OK', 'message': '', 'type': 'Process'}}, 'Hardware': {'PSU 2': {'status': 'OK', 'message': '', 'type': 'PSU'}, 'psu_1_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'psu_2_fan_1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan11': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan10': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan12': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'ASIC': {'status': 'OK', 'message': '', 'type': 'ASIC'}, 'fan1': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'PSU 1': {'status': 'OK', 'message': '', 'type': 'PSU'}, 'fan3': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan2': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan5': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan4': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan7': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan6': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan9': {'status': 'OK', 'message': '', 'type': 'Fan'}, 'fan8': {'status': 'OK', 'message': '', 'type': 'Fan'}}}
        else:
            stats = {}
        MockerManager.counter += 1

        return stats

class MockerChassis(object):
    counter = 0

    def initizalize_system_led(self):
        return

    def get_status_led(self):
        if MockerChassis.counter == 1:
            MockerChassis.counter += 1
            return "green"
        else:
            MockerChassis.counter += 1
            return "red"

import show.main as show

class TestHealth(object):
    original_cli = None

    @classmethod
    def setup_class(cls):
        print("SETUP")
        os.environ["PATH"] += os.pathsep + scripts_path
        os.environ["UTILITIES_UNIT_TESTING"] = "1"
        global original_cli
        original_cli = show.cli

    def test_health_summary(self):
        runner = CliRunner()
        result = runner.invoke(show.cli.commands["system-health"].commands["summary"])
        click.echo(result.output)
        expected = """\
System health configuration file not found, exit...
"""
        assert result.output == expected
        result = runner.invoke(show.cli.commands["system-health"].commands["summary"])
        expected = """\
System status summary

  System status LED  red
  Services:
    Status: Not OK
    Not Running: telemetry, snmp_subagent
  Hardware:
    Status: OK
"""
        click.echo(result.output)
        assert result.output == expected
        result = runner.invoke(show.cli.commands["system-health"].commands["summary"])
        click.echo(result.output)
        expected = """\
System status summary

  System status LED  green
  Services:
    Status: OK
  Hardware:
    Status: OK
"""
        assert result.output == expected

    def test_health_monitor(self):
        runner = CliRunner()
        result = runner.invoke(show.cli.commands["system-health"].commands["monitor-list"])
        click.echo(result.output)
        expected = """
System services and devices monitor list

Name            Status    Type
--------------  --------  ----------
telemetry       Not OK    Process
sflowmgrd       Not OK    Process
neighsyncd      OK        Process
vrfmgrd         OK        Process
dialout_client  OK        Process
zebra           OK        Process
rsyslog         OK        Process
snmpd           OK        Process
redis_server    OK        Process
intfmgrd        OK        Process
orchagent       OK        Process
vxlanmgrd       OK        Process
lldpd_monitor   OK        Process
portsyncd       OK        Process
var-log         OK        Filesystem
lldpmgrd        OK        Process
syncd           OK        Process
sonic           OK        System
buffermgrd      OK        Process
portmgrd        OK        Process
staticd         OK        Process
bgpd            OK        Process
lldp_syncd      OK        Process
bgpcfgd         OK        Process
snmp_subagent   OK        Process
root-overlay    OK        Filesystem
fpmsyncd        OK        Process
vlanmgrd        OK        Process
nbrmgrd         OK        Process
PSU 2           OK        PSU
psu_1_fan_1     OK        Fan
psu_2_fan_1     OK        Fan
fan11           OK        Fan
fan10           OK        Fan
fan12           OK        Fan
ASIC            OK        ASIC
fan1            OK        Fan
PSU 1           OK        PSU
fan3            OK        Fan
fan2            OK        Fan
fan5            OK        Fan
fan4            OK        Fan
fan7            OK        Fan
fan6            OK        Fan
fan9            OK        Fan
fan8            OK        Fan
"""
        assert result.output == expected

    def test_health_detail(self):
        runner = CliRunner()
        result = runner.invoke(show.cli.commands["system-health"].commands["detail"])
        click.echo(result.output)
        expected = """\
System status summary

  System status LED  red
  Services:
    Status: Not OK
    Not Running: telemetry, sflowmgrd
  Hardware:
    Status: Not OK
    Reasons: Failed to get voltage minimum threshold data for PSU 1
	     Failed to get voltage minimum threshold data for PSU 2

System services and devices monitor list

Name            Status    Type
--------------  --------  ----------
telemetry       Not OK    Process
sflowmgrd       Not OK    Process
neighsyncd      OK        Process
vrfmgrd         OK        Process
dialout_client  OK        Process
zebra           OK        Process
rsyslog         OK        Process
snmpd           OK        Process
redis_server    OK        Process
intfmgrd        OK        Process
orchagent       OK        Process
vxlanmgrd       OK        Process
lldpd_monitor   OK        Process
portsyncd       OK        Process
var-log         OK        Filesystem
lldpmgrd        OK        Process
syncd           OK        Process
sonic           OK        System
buffermgrd      OK        Process
portmgrd        OK        Process
staticd         OK        Process
bgpd            OK        Process
lldp_syncd      OK        Process
bgpcfgd         OK        Process
snmp_subagent   OK        Process
root-overlay    OK        Filesystem
fpmsyncd        OK        Process
vlanmgrd        OK        Process
nbrmgrd         OK        Process
PSU 2           Not OK    PSU
PSU 1           Not OK    PSU
psu_1_fan_1     OK        Fan
psu_2_fan_1     OK        Fan
fan11           OK        Fan
fan10           OK        Fan
fan12           OK        Fan
ASIC            OK        ASIC
fan1            OK        Fan
fan3            OK        Fan
fan2            OK        Fan
fan5            OK        Fan
fan4            OK        Fan
fan7            OK        Fan
fan6            OK        Fan
fan9            OK        Fan
fan8            OK        Fan

System services and devices ignore list

Name    Status    Type
------  --------  ------
"""
        assert result.output == expected
        MockerConfig.ignore_devices.insert(0, "psu.voltage")
        result = runner.invoke(show.cli.commands["system-health"].commands["detail"])
        click.echo(result.output)
        expected = """\
System status summary

  System status LED  red
  Services:
    Status: Not OK
    Not Running: telemetry, sflowmgrd
  Hardware:
    Status: OK

System services and devices monitor list

Name            Status    Type
--------------  --------  ----------
telemetry       Not OK    Process
sflowmgrd       Not OK    Process
neighsyncd      OK        Process
vrfmgrd         OK        Process
dialout_client  OK        Process
zebra           OK        Process
rsyslog         OK        Process
snmpd           OK        Process
redis_server    OK        Process
intfmgrd        OK        Process
orchagent       OK        Process
vxlanmgrd       OK        Process
lldpd_monitor   OK        Process
portsyncd       OK        Process
var-log         OK        Filesystem
lldpmgrd        OK        Process
syncd           OK        Process
sonic           OK        System
buffermgrd      OK        Process
portmgrd        OK        Process
staticd         OK        Process
bgpd            OK        Process
lldp_syncd      OK        Process
bgpcfgd         OK        Process
snmp_subagent   OK        Process
root-overlay    OK        Filesystem
fpmsyncd        OK        Process
vlanmgrd        OK        Process
nbrmgrd         OK        Process
PSU 2           OK        PSU
psu_1_fan_1     OK        Fan
psu_2_fan_1     OK        Fan
fan11           OK        Fan
fan10           OK        Fan
fan12           OK        Fan
ASIC            OK        ASIC
fan1            OK        Fan
PSU 1           OK        PSU
fan3            OK        Fan
fan2            OK        Fan
fan5            OK        Fan
fan4            OK        Fan
fan7            OK        Fan
fan6            OK        Fan
fan9            OK        Fan
fan8            OK        Fan

System services and devices ignore list

Name         Status    Type
-----------  --------  ------
psu.voltage  Ignored   Device
"""
        assert result.output == expected

    def test_health_systemready(self):
        runner = CliRunner()
        result = runner.invoke(show.cli.commands["system-health"].commands["sysready-status"])
        click.echo(result.output)
        print("myresult:{}".format(result.output))
        expected = """\
System is not ready - one or more services are not up

Service-Name    Service-Status    App-Ready-Status    Down-Reason
--------------  ----------------  ------------------  -------------
bgp             Down              Down                Inactive
mgmt-framework  OK                OK                  -
pmon            OK                OK                  -
swss            OK                OK                  -
"""
        assert result.output == expected
        result = runner.invoke(show.cli.commands["system-health"].commands["sysready-status"],["brief"])
        click.echo(result.output)
        print("myresult:{}".format(result.output))
        expected = """\
System is not ready - one or more services are not up
"""
        assert result.output == expected
        result = runner.invoke(show.cli.commands["system-health"].commands["sysready-status"],["detail"])
        click.echo(result.output)
        print("myresult:{}".format(result.output))
        expected = """\
System is not ready - one or more services are not up

Service-Name    Service-Status    App-Ready-Status    Down-Reason    AppStatus-UpdateTime
--------------  ----------------  ------------------  -------------  ----------------------
bgp             Down              Down                Inactive       -
mgmt-framework  OK                OK                  -              -
pmon            OK                OK                  -              -
swss            OK                OK                  -              -
"""

    def test_health_dpu(self):
        # Mock is_smartswitch to return True
        with mock.patch("sonic_py_common.device_info.is_smartswitch", return_value=True):

            # Check if 'dpu' command is available under system-health
            available_commands = show.cli.commands["system-health"].commands
            assert "dpu" in available_commands, f"'dpu' command not found: {available_commands}"

            conn = dbconnector.SonicV2Connector()
            conn.connect(conn.CHASSIS_STATE_DB)
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "id", "0")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_midplane_link_reason", "OK")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_midplane_link_state", "UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_data_plane_time", "20240607 15:08:51")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_control_plane_time", "20240608 09:11:13")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_data_plane_state", "UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_control_plane_reason", "Uplink is UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_control_plane_state", "UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_data_plane_reason", "Polaris is UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_midplane_link_time", "20240608 09:11:13")

            with mock.patch("show.system_health.SonicV2Connector", return_value=conn):
                runner = CliRunner()
                result = runner.invoke(show.cli.commands["system-health"].commands["dpu"], ["DPU0"])

                # Assert the output and exit code
                assert result.exit_code == 0, f"Expected exit code 0, got {result.exit_code}. Output: {result.output}"
                assert "DPU0" in result.output, f"Expected 'DPU0' in output, got: {result.output}"

                # check -h option
                result = runner.invoke(show.cli.commands["system-health"].commands["dpu"], ["-h"])
                print(result.output)

    def test_health_dpu_non_smartswitch(self):
        # Mock is_smartswitch to return True
        with mock.patch("sonic_py_common.device_info.is_smartswitch", return_value=False):

            # Check if 'dpu' command is available under system-health
            available_commands = show.cli.commands["system-health"].commands
            assert "dpu" in available_commands, f"'dpu' command not found: {available_commands}"

            conn = dbconnector.SonicV2Connector()
            conn.connect(conn.CHASSIS_STATE_DB)
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "id", "0")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_midplane_link_reason", "OK")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_midplane_link_state", "UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_data_plane_time", "20240607 15:08:51")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_control_plane_time", "20240608 09:11:13")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_data_plane_state", "UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_control_plane_reason", "Uplink is UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_control_plane_state", "UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_data_plane_reason", "Polaris is UP")
            conn.set(conn.CHASSIS_STATE_DB, 'DPU_STATE|DPU0', "dpu_midplane_link_time", "20240608 09:11:13")

            with mock.patch("show.system_health.SonicV2Connector", return_value=conn):
                runner = CliRunner()
                result = runner.invoke(show.cli.commands["system-health"].commands["dpu"], ["DPU0"])

                # Assert the output and exit code
                assert result.exit_code == 0, f"Expected exit code 0, got {result.exit_code}. Output: {result.output}"
                assert "DPU0" not in result.output, f"Output contained DPU0: {result.output}"

    # Test 'get_all_dpu_options' function
    def test_get_all_dpu_options(self):
        # Mock is_smartswitch to return True
        with mock.patch("sonic_py_common.device_info.is_smartswitch", return_value=True):

            # Mock platform info to simulate a valid platform returned from get_platform_info
            mock_platform_info = {'platform': 'mock_platform'}
            with mock.patch("sonic_py_common.device_info.get_platform_info", return_value=mock_platform_info):

                # Mock open to simulate reading a platform.json file
                mock_platform_data = '{"DPUS": {"dpu0": {}, "dpu1": {}}}'
                with mock.patch("builtins.open", mock.mock_open(read_data=mock_platform_data)):

                    # Mock json.load to return parsed JSON content from the mocked file
                    with mock.patch("json.load", return_value=json.loads(mock_platform_data)):

                        # Import the actual get_all_dpu_options function and invoke it
                        from show.system_health import get_all_dpu_options
                        dpu_list = get_all_dpu_options()
                        print(dpu_list)

    @classmethod
    def teardown_class(cls):
        print("TEARDOWN")
        os.environ["PATH"] = os.pathsep.join(os.environ["PATH"].split(os.pathsep)[:-1])
        os.environ["UTILITIES_UNIT_TESTING"] = "0"
        show.cli = original_cli
