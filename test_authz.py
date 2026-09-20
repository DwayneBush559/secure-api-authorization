import unittest

from authz import (
    ForbiddenError,
    Principal,
    Resource,
    Role,
    require_read,
    update_value,
)


class AuthorizationTests(unittest.TestCase):
    def setUp(self):
        self.resource = Resource("job-42", "user-1", "private")

    def test_owner_can_read(self):
        user = Principal("user-1", Role.USER)
        self.assertEqual(require_read(user, self.resource), self.resource)

    def test_other_user_is_blocked(self):
        user = Principal("user-2", Role.USER)
        with self.assertRaises(ForbiddenError):
            require_read(user, self.resource)

    def test_admin_can_update(self):
        admin = Principal("admin-1", Role.ADMIN)
        updated = update_value(admin, self.resource, "reviewed")
        self.assertEqual(updated.value, "reviewed")
        self.assertEqual(updated.owner_id, "user-1")


if __name__ == "__main__":
    unittest.main()
