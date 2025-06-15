from ansible.errors import AnsibleFilterError
from ipaddress import IPv4Network

def calc_target_address(cidr: str, host_index: int, with_mask: bool) -> str:

    if (type(cidr), type(host_index), type(with_mask)) != (str, int, bool):
        raise AnsibleFilterError('Invalid argument types: expected (str, int, bool)')
    
    try:
        network = IPv4Network(cidr, strict=True)

        if host_index < 0 :
            ip_address = network.broadcast_address + host_index
        elif host_index >= 0:
            ip_address = network.network_address + host_index

        if with_mask:
            target_address = f"{ip_address}/{network.prefixlen}"
        else:
            target_address = f"{ip_address}"

        return target_address


    except Exception as e:
        raise AnsibleFilterError(f'error: {e}')

class FilterModule(object):
    def filters(self):
        return {
            'cidr_to_target_address': calc_target_address
        }