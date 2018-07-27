import random
import time
import random
import threading
#import seal
#from seal import ChooserEvaluator, Ciphertext, Decryptor, Encryptor, EncryptionParameteEvaluator, IntegerEncoder, FractionalEncoder, KeyGenerator, MemoryPoolHandle, Plaintext, SEALContext, EvaluationKeys, GaloisKeys, PolyCRTBuilder, ChooserEncoder, ChooserEvaluator, ChooserPoly

A=[]
A_cipherObject=[]
for i in range(16):
	A.append(random.randint(0,64))

def chunk(T):
	B=[]
	for i in range(0,16,4):
		B.append(T[i:i+4])
	return(B)

def matrix_test1():
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

    A_plain=[]
    for i in range(16):
    	A_plain[i]=encoder.encode(A[i])
    print("Encoded Matrix: "+ (str)A + " as polynomial" + (str)A_plain)

	for i in range(16):
    	A_cipherObject.append(Ciphertext())
 	B=[]
 	for i in range(16):
 		B.append(encrpytor.encrypt(A_plain[i],A_cipherObject[i]))
 		print("Noise budget of +" (str)i+(str)(decryptor.invariant_noise_budget(A_cipherObject[i])) + " bits")

def main():
	matrix_test1()
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

if __name__ == '__main__':
    main() 		
