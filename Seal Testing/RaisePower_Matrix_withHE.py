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
parms.set_poly_modulus("1x^4096 + 1")
parms.set_coeff_modulus(seal.coeff_modulus_128(4096))
parms.set_plain_modulus(1 << 10)
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


W=Ciphertext(A[0][0])
evaluator.negate(W)
pa=Plaintext()
pw=Plaintext()
decryptor.decrypt(W, pw)
decryptor.decrypt(A[0][0], pa)
print(encoder.decode_int32(pa))
print(encoder.decode_int32(pw))

print("0 encoding: ", encoder.encode(0).to_string())
#tA_=numpy.transpose(A)
tA=[list(tup) for tup in zip(*A)]

def dot_vector(r,d,i,j):
	print("+"*30+"\n")
	print_plain(X)
	l=len(r)
	for b in range(l):
		# multiply/binary operation between vectors
		cVec=Ciphertext()
		evaluator.multiply( r[b], d[b], cVec)
		evaluator.add(X[i][j], cVec)
	print("Noise budget "+str(i)+" "+str(j)+" "+ 	str(decryptor.invariant_noise_budget(X[i][j])))
	print_plain(X)


def raise_power(M):
	print_plain(M)
	for i in range(n):
		for j in range(n):
			dot_vector(M[i], tA[j], i, j)
	print_plain(A)
	return(X)

def trace(M):
	e=copy.copy(M[0][0])
	for i in range(1,n):
		evaluator.add(M[0][0], M[i][i])
#	M[0][0],e=e,M[0][0]
	return (M[0][0],e)

def print_plain(D):
	for x in D:
		for y in x:
			p=Plaintext()
			decryptor.decrypt(y, p)
			print(encoder.decode_int32(p))

matrixPower_vector=[A]
#trace_vector,k=trace(A)
matrixPower_vector.append(raise_power(A))
#A[0][0]=k
for i in range(n):
	for j in range(n):
		p=Plaintext()
		decryptor.decrypt(matrixPower_vector[1][i][j], p)
		print(encoder.decode_int32(p))
"""
p=Plaintext()
decryptor.decrypt(trace_vector, p)
print(encoder.decode_int32(p))	

for i in range(1,n-1):
	matrixPower_vector.append(raise_power(matrixPower_vector[i-1]))
	transpose_vector.append(trace(matrixPower_vector[i]))
"""
for i in range(n):
	for j in range(n):
		plain_result = Plaintext()
		decryptor.decrypt(A[i][j], plain_result)
		print(encoder.decode_int32(plain_result))
