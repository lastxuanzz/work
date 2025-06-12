from ansible.errors import AnsibleFilterError
from ipaddress import IPv4Network

def cidr(cidr: str, host_index: int, with_mask: str) -> str:

    if host_index == 0 or with_mask not in ['あり', 'なし']:
        raise AnsibleFilterError('Host index cannot be zero or with_mask is invalid')
    
    try:
        network = IPv4Network(cidr, strict=False)

        if host_index < 0 :
            ip_address = network.broadcast_address + host_index
        elif host_index > 0:
            ip_address = network.network_address + host_index

        if with_mask == 'あり':
            target_address = f"{ip_address}/{network.prefixlen}"
        elif with_mask == 'なし':
            target_address = f"{ip_address}"

        return target_address


    except Exception as e:
        raise AnsibleFilterError(f'error: {str(e)}')

class FilterModule(object):
    def filters(self):
        return {
            'cidr_to_target_address': cidr
        }