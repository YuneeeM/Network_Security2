from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
import ast


random_generator = Random.new().read
privatekey = RSA.generate(1024, random_generator)  # 키 소유자 보관용
publickey = privatekey.publickey()  # 외부 공개용

f = open('example.txt', 'r')
strings = f.read()
print('원문 == ', strings)

# 공개키로 원문을 암호화한다.
encryptor = PKCS1_OAEP.new(publickey)
# 암호화할 메시지가 위 문자열 위에 있다.
encrypted = encryptor.encrypt(b'encrypt this message.')

print('암호화된 메시지는 다음과 같습니다 == ', encrypted)  # ciphertext
# 암호화할 원문이 저장된 'example.txt'
f = open('ciphertext.txt', 'w')
# 암호문을 file에 적는다.
f.write(str(encrypted))
f.close()

f = open('ciphertext.txt', 'r')
message = f.read()
# 암호화 한 문장을 private key을 통해 해독한다.
decryptor = PKCS1_OAEP.new(privatekey)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print('복호화 ==', decrypted)

f = open('example.txt', 'w')
f.write(str(strings))
f.write(str(decrypted))
f.close()
