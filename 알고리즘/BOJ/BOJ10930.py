# SHA-256

import hashlib

S = input()

result = hashlib.sha256(S.encode())
print(result.hexdigest())