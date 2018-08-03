#import numpy 
import random
import copy
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
		encrypted_data1= Ciphertext()
		encrypted_data2= Ciphertext()
		ran=random.randint(0,10)
		print(ran)
		encryptor.encrypt(encoder.encode(ran), encrypted_data1)
		encryptor.encrypt(encoder.encode(0), encrypted_data2)
		a.append(encrypted_data1)
		x.append(encrypted_data2)
	A.append(a)
	X.append(x)

#tA_=numpy.transpose(A)

C=A

tA=[list(tup) for tup in zip(*A)]

def dot_vector(r,d,i,j):
	l=len(r)
	for i in range(l):
		# multiply/binary operation between vectors
		evaluator.multiply(r[i], d[i])
		evaluator.add(X[i][j], r[i])

def raise_power(M):
	for i in range(n):
		for j in range(n):
			dot_vector(M[i], tA[j], i, j)
	return(X)

def trace(M):
	e=copy.copy(M[0][0])
	for i in range(1,n):
		evaluator.add(M[0][0], M[i][i])
#	M[0][0],e=e,M[0][0]
	return (M[0][0],e)

print(A)

matrixPower_vector=[A]
trace_vector,k=trace(A)
matrixPower_vector.append(raise_power(A))
A[0][0]=k
for i in range(n):
	for j in range(n):
		p=Plaintext()
		decryptor.decrypt(matrixPower_vector[1][i][j], p)
		print(encoder.decode_int32(p))

p=Plaintext()
decryptor.decrypt(trace_vector, p)
print(encoder.decode_int32(p))	

for i in range(1,n-1):
	matrixPower_vector.append(raise_power(matrixPower_vector[i-1]))
	transpose_vector.append(trace(matrixPower_vector[i]))

for i in range(n):
	for j in range(n):
		plain_result = Plaintext()
		decryptor.decrypt(A[i][j], plain_result)
		print(encoder.decode_int32(plain_result))


		encrypted_data2= Ciphertext()
		ran=random.randint(0,10)
		print(ran)
		encryptor.encrypt(encoder.encode(ran), encrypted_data1)
		encryptor.encrypt(encoder.encode(0), encrypted_data2)
		a.append(encrypted_data1)
		x.append(encrypted_data2)
	A.append(a)
	X.append(x)

C=A
for i in range(n):
	for j in range(n):
		plain_result = Plaintext()
		decryptor.decrypt(C[i][j], plain_result)
		print(encoder.decode_int32(plain_result))

# tA_=numpy.transpose(A)

tA=[list(tup) for tup in zip(*A)]

def dot_vector(r,d,i,j):
	l=len(r)
	for i in range(l):
		# multiply/binary operation between vectors
		evaluator.multiply(r[i], d[i])
		evaluator.add(X[i][j], r[i])
	return None

def raise_power(M):
	global X
	for i in range(n):
		for j in range(n):
			dot_vector(M[i], tA[j], i, j)
	return(X)

def trace(M):
	for i in range(1,n):
		evaluator.add(M[0][0], M[i][i])
	return (M[0][0])

print(A)

"""
class X():
	pass
s=X()
setattr(s, "s1", 1)
setattr(s, "s2", 3)

print(dir(s))

print(s.s1)
print(s.s2)
"""

matrixPower_vector=[A]
trace_vector=[trace(A)]
matrixPower_vector.append(raise_power(matrixPower_vector[0]))

"""
for i in range(1,n-1):
	matrixPower_vector.append(raise_power(matrixPower_vector[i-1]))
	transpose_vector.append(trace(matrixPower_vector[i]))

for i in range(n):
	for j in range(n):
		plain_result = Plaintext()
		decryptor.decrypt(matrixPower_vector[0][i][j], plain_result)
		print(encoder.decode_int32(plain_result))
"""
