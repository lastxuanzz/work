import pytest
from work.my_collection.plugins.filter.cidr_to_target_address import calc_target_address
from ansible.errors import AnsibleFilterError


def test_address_with_mask():
    assert calc_target_address('192.168.1.0/24', 1, True) == '192.168.1.1/24'

def test_address_without_mask():
    assert calc_target_address('192.168.1.0/24', 6, False) == '192.168.1.6'

def test_address_negative_index_with_mask():
    assert calc_target_address('192.168.1.0/24', -1, True) == '192.168.1.254/24'

def test_invalid_cidr():
    with pytest.raises(AnsibleFilterError):
        calc_target_address('192.168.1.1/24', -1, True)

def test_invalid_host_index():
    with pytest.raises(AnsibleFilterError):
        calc_target_address('192.168.1.0/24', '1', True)

def test_invalid_with_mask():
    with pytest.raises(AnsibleFilterError):
        calc_target_address('192.168.1.0/24', 1, 'True')
