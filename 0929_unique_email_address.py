import unittest
from typing import *
# tags:

# Time = O(n)
# Space = O()
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for e in emails:
            local, domain = e.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        s = Solution()
        self.assertEqual(s.numUniqueEmails(emails), 2)


if __name__ == "__main__":
	unittest.main()
