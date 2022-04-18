import pyotp
from settings import get_settings


class TwoFactorAuth:
    def __init__(self):
        self.totp = pyotp.TOTP(get_settings().key_for_pyotp, interval=get_settings().two_factor_auth_interval)

    async def generate_code(self):
        return self.totp.now()

    async def verify_code(self, code: str):
        return True if self.totp.verify(code) else False
