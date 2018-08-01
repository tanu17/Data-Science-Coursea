import numpy 

import random
import time
import random
import threading
import seal

from seal import ChooserEvaluator,     \
                 Ciphertext,           \
                 Decryptor,            \
                 Encryptor,            \
                 EncryptionParameters, \
                 Evaluator,            \
                 IntegerEncoder,       \
                 FractionalEncoder,    \
                 KeyGenerator,         \
                 MemoryPoolHandle,     \
                 Plaintext,            \
                 SEALContext,          \
                 EvaluationKeys,       \
                 GaloisKeys,           \
                 PolyCRTBuilder,       \
                 ChooserEncoder,       \
                 ChooserEvaluator,     \
                 ChooserPoly

parms = EncryptionParameters()
parms.set_poly_modulus("1x^2048 + 1")
parms.set_coeff_modulus(seal.coeff_modulus_128(2048))
parms.set_plain_modulus(1 << 8)
context = SEALContext(parms)

encoder = IntegerEncoder(context.plain_modulus())
keygen = KeyGenerator(context)
public_key = keygen.public_key()
secret_key = keygen.secret_key()
encryptor = Encryptor(context, public_key)
evaluator = Evaluator(context)
decryptor = Decryptor(context, secret_key)

A=[]
X=[]
n=int(input("Enter dimension: "))

for i in range(n):
	a=[]
	x=[]
	for j in range(n):
		encrypted _data1= Ciphertext()
		encrypted _data2= Ciphertext()
		encryptor.encrypt(encoder.encode(random.randint(0,10)), encrypted_data1)
		encryptor.encrypt(encoder.encode(0), encrypted_data2)
		a.append(encrypted_data1)
		x.append(encrypted_data2)
	A.append(a)
	X.append(x)

tA_=numpy.transpose(A)

tA=[list(tup) for tup in zip(*A)]

def dot_vector(r,d):
	l=len(r)
	t=Ciphertext()
	encryptor.encrypt(encoder.encode(0), t)
	for i in range(l):
		# multiply/binary operation between vectors
		evaluator.multiply(r[i], d[i])
		evaluator.multiply(t, r[i])
	return(t)

def raise_power(M):
	for i in range(n):
		for j in range(n):
			(X[i])[j]=dot_vector(M[i], tA[j])
	return(X)

print(A)
sq=(raise_power(A))
print(sq)
print(raise_power(sq)) 