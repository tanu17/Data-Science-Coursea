import random
import time
import pickle
import threading
import seal
from seal import ChooserEvaluator, \
	Ciphertext, \
	Decryptor, \
	Encryptor, \
	EncryptionParameters, \
	Evaluator, \
	IntegerEncoder, \
	FractionalEncoder, \
	KeyGenerator, \
	MemoryPoolHandle, \
	Plaintext, \
	SEALContext, \
	EvaluationKeys, \
	GaloisKeys, \
	PolyCRTBuilder, \
	ChooserEncoder, \
	ChooserEvaluator, \
	ChooserPoly

def print_example_banner(title, ch='*', length=78):
    spaced_text = ' %s ' % title
    print(spaced_text.center(length, ch))

def print_parameters(context):
    print("/ Encryption parameters:")
    print("| poly_modulus: " + context.poly_modulus().to_string())

    # Print the size of the true (product) coefficient modulus
    print("| coeff_modulus_size: " + (str)(context.total_coeff_modulus().significant_bit_count()) + " bits")

    print("| plain_modulus: " + (str)(context.plain_modulus().value()))
    print("| noise_standard_deviation: " + (str)(context.noise_standard_deviation()))

def chunk(T):
	B=list()
	for i in range(0,len(T),4):
		B.append(T[i:i+4])
	return(B)

A=[]
A_plain=[]
A_cipherObject=[]
B=[]
Result_crypt=[]

for i in range(16):
	A.append(random.randint(0,64))
A+=[0]*16
print(A)
for i in range(16,len(A),5):
	A[i]=1

parms = EncryptionParameters()
parms.set_poly_modulus("1x^2048 + 1")
parms.set_coeff_modulus(seal.coeff_modulus_128(2048))
parms.set_plain_modulus(1 << 8)

context = SEALContext(parms)
print_parameters(context)
encoder = IntegerEncoder(context.plain_modulus())
keygen = KeyGenerator(context)
public_key = keygen.public_key()
secret_key = keygen.secret_key()
encryptor = Encryptor(context, public_key)
evaluator = Evaluator(context)
decryptor = Decryptor(context, secret_key)

for i in range(len(A)):
	A_plain.append(encoder.encode(A[i]))
	A_cipherObject.append(Ciphertext())
	encryptor.encrypt(A_plain[i],A_cipherObject[i])
	print("Noise budget of "+ str(i)+" "+str((decryptor.invariant_noise_budget(A_cipherObject[i]))) + " bits")


A_cipherObject=chunk(A_cipherObject)
C=A_cipherObject

#shallow copy

# partial pivoting
i=4
while (i>1):
	evaluator.negate(C[i-1][1])
	evaluator.add(C[i-1][1], C[i][1])
	plain_result = Plaintext()
	decryptor.decrypt(C[i-1][1], plain_result)
	if (int(encoder.decode_int32(plain_result))>0):
		for j in range(1,9):
			A_cipherObject[i-1][j],A_cipherObject[i][j]=A_cipherObject[i][j],A_cipherObject[i-1][j]
	i-=1
del(C)

D=A_cipherObject

# reducing to diagnol matrix
for i in range(1,5):
	for j in range (1,2*4):
		if (j!=i):
			X=Result_crypt[i][i]
			Y=Ciphertext()
			plain_result = Plaintext()
			decryptor.decrypt(X, plain_result)
			encryptor.encrpyt(encoder.encode(1/int(encoder.decode_int32(plain_result))),Y)
			for k in range(1,9):
				evaluator.multiply(Y,D[i][j])
				evaluator.negate(Y)
				evaluator.add(A_cipherObject[i][j],Y)

# reducing to unit matrix
for i in range (1,9):
	d=A_cipherObject[i][i]
	Y=Ciphertext()
	plain_result = Plaintext()
	decryptor.decrypt(X, plain_result)
	encryptor.encrpyt(encoder.encode(1/int(encoder.decode_int32(plain_result))),Y)
	for j in range (1,9):
		A_cipherObject[i][j]=evaluator.multiply(A_cipherObject[i][j],Y)
