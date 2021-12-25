import random
import string
from dataclasses import dataclass


def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

@dataclass
class SupportTicket:
    customer: str
    issue: str
    id: str = generate_id()