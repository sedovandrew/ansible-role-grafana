import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_grafana_is_installed(host):
    host.package("grafana").is_installed


def test_grafana_is_running(host):
    host.service("grafana-server").is_running


def test_grafana_is_enabled(host):
    host.service("grafana-server").is_enabled


def test_grafana_listen_port(host):
    host.socket("tcp://0.0.0.0:3000").is_listening
