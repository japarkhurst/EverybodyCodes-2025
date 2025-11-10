# https://github.com/wimglenn/everybody-codes-data
import json
import urllib

from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import modes

token = '345a6440-7ff0-43f2-925e-5f3251d78fcc'
#{"id":1736,"code":"211678B028F2F587F2E8D215E55429E3G1736","name":"japarkhurst","country":"us","url":"https://github.com/japarkhurst","level":63,"seed":40,"penaltyUntil":1762395564456,"badges":{"1":null,"2":null,"2024":null,"2025":null},"ai":false,"streamer":false,"serverTime":1762454207546}

url_seed = "https://everybody.codes/api/user/me"
url_keys = "https://everybody.codes/api/event/{event}/quest/{quest}"
url_post = "https://everybody.codes/api/event/{event}/quest/{quest}/part/{part}/answer"
url_data = "https://everybody-codes.b-cdn.net/assets/{event}/{quest}/input/{seed}.json"


def queryURL(url):
    import urllib
    with urllib.request.urlopen(url) as response:
        resp_text = response.read().decode('utf-8') # Read and decode the response body
        json_data = json.loads(resp_text) # Parse the string as JSON
        print(json_data)
        return json_data

def decrypt(input_hex, key):
    key_bytes = key.encode()
    iv = key_bytes[:16]
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend='some_backend_value')
    decryptor = cipher.decryptor()
    input_bytes = bytes.fromhex(input_hex)
    decrypted_bytes = decryptor.update(input_bytes) + decryptor.finalize()
    pad_length = decrypted_bytes[-1]
    result = decrypted_bytes[:-pad_length].decode()
    return result


quest = 1
event = 2025
seed = 40
encrypted_inputs = queryURL(url_data.format(quest=quest, event=event, seed=seed))
keys = queryURL(url_keys.format(quest=quest, event=event))
result = {}
for k, v in encrypted_inputs.items():
    if f"key{k}" in keys:
        result[k] = decrypt(v, keys[f"key{k}"])
print(result)
