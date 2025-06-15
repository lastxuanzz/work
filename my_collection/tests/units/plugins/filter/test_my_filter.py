import pytest
from my_collection.plugins.filter.cidr_to_target_address import cidr
from ansible.errors import AnsibleFilterError



def test_cidr_with_mask():
    assert cidr('192.168.1.0/24', 1, True) == '192.168.1.1/24'

def test_cidr_without_mask():
    assert cidr('192.168.1.0/24', 1, False) == '192.168.1.1'

def test_cidr_negative_index_with_mask():
    assert cidr('192.168.1.0/24', -1, True) == '192.168.1.254/24'

def test_cidr_negative_index_without_mask():
    assert cidr('192.168.1.0/24', -1, False) == '192.168.1.254'

def test_invalid():
    with pytest.raises(AnsibleFilterError):
        cidr('192.168.1.1/24', -1, True)