# files to be imported
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

# Set up an instance of the EncryptionParameters class
# three encryption parameters that are necessary to set:
#     - poly_modulus (polynomial modulus);
#     - coeff_modulus ([ciphertext] coefficient modulus);
#     - plain_modulus (plaintext modulus).
parms = EncryptionParameters()
#polynomial modulus must be a power-of-2 cyclotomic polynomial
# Recommended degrees for poly_modulus are 1024, 2048, 4096, 8192, 16384, 32768,
# but it is also possible to go beyond this.
parms.set_poly_modulus("1x^2048 + 1")
# To make parameter selection easier for the user, we have constructed sets of
# largest allowed coefficient moduli for 128-bit and 192-bit security levels
# for different choices of the polynomial modulus. These recommended parameters
# follow the Security white paper at http://HomomorphicEncryption.org. However,
# due to the complexity of this topic, we highly recommend the user to directly
# consult an expert in homomorphic encryption and RLWE-based encryption schemes
# to determine the security of their parameter choices.

# Our recommended values for the coefficient modulus can be easily accessed
# through the functions

#     coeff_modulus_128bit(int)
#     coeff_modulus_192bit(int)
parms.set_coeff_modulus(seal.coeff_modulus_128(2048))
# The plaintext modulus can be any positive integer, even though here we take
# it to be a power of two.
parms.set_plain_modulus(1 << 8)
# 1 << 8 is bitwise operation which means 1 shifted eight times ie 2^8=256
context = SEALContext(parms)


encoder = IntegerEncoder(context.plain_modulus())
keygen = KeyGenerator(context)
public_key = keygen.public_key()
secret_key = keygen.secret_key()
encryptor = Encryptor(context, public_key)
evaluator = Evaluator(context)
decryptor = Decryptor(context, secret_key)

value=7
plain1 = encoder.encode(value1)
print("Encoded " + (str)(value) + " as polynomial " + plain1.to_string() + " (plain1)")

encrypted _data= Ciphertext()
encryptor.encrypt(plain, encrypted_data)
print("Noise budget in encrypted1: " + (str)(decryptor.invariant_noise_budget(encrypted_data)) + " bits")

# operations that can be performed --->

# result stored in encrypted1 data
evaluator.negate(encrypted1_data)

# result stored in encrypted1 data, encrpyted1 is modified
evaluator.add(encrypted1_data, encrypted2_data)

# result stored in encrypted1 data, encrpyted1 is modified
evaluator.multiply(encrypted1_data, encrypted2_data)


plain_result = Plaintext()
decryptor.decrypt(encrypted_data, plain_result)
print("Plaintext polynomial: " + plain_result.to_string())
print("Decoded integer: " + (str)(encoder.decode_int32(plain_result)))