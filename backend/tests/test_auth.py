import unittest
from auth.auth import get_password_hash, verify_password

class TestAuth(unittest.TestCase):
    def test_get_password_hash(self):
        password_hash = get_password_hash("test.123")
        print("password hash", password_hash)
        self.assertEqual(password_hash, "$2b$12$Ou3k9gboKDOcL5cgvIRKKuCiv5bCT675ElRQHvuumlLyVaU3jz4Mi")

    def test_verify_password(self):
        verify_password_result = verify_password("test.123", "$2b$12$Ou3k9gboKDOcL5cgvIRKKuCiv5bCT675ElRQHvuumlLyVaU3jz4Mi")
        self.assertEqual(verify_password_result, True)