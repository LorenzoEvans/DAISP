
def funct(n):
    counter = 0
    i_c = 0
    v_c = 0
    for i in range(n):
        # print("i is: ",i)
        print("outer work")
        j = i
        i_c += i
        for v in range(n):
            # print("j is: ",v)
            print("inner work")
            counter += 1
            v_c += i
    print("i counter is:, ",i, "v counter is: ",v)
funct(9)

def funct2(n):
    i = 0
    while i < n: # This depends on n.
        j = 0   # This is a constant operation (assignment).
        while j < 3*n: # This is 3*n (3n).
            j = j + 1 # This is a constant operation (incrementing).
        j = 0   # Another constant assignment.
        while j < 2*n: # This is 2*n (2n).
            j = j + 1 # This is another constant operation.
        i = i + 1 # Another constant operation.
# O(n) + O(1) + O(3n) + O(1) + O(1) + O(2n) + O(1) + O(1)
# Alright, lets knock the additions out.
# We've got 5 O(1)'s, so we've got O(.. + 5)
# O(n) + O(3n) + O(2n) + O(5)
# We can add the middle two because they're doing the same thing on the same value.
# O(n) + O(5n) + O(5).
# Let's add the 5 in now.
# O(n + 5) + O(5n)
# O(5n * n + 5)
# Drop the additional constant.
# O(5n * n).
# Drop the multiplicative constant.
# O(n * n)
# O(n^2)

def funct3(n):
    i = 0 # This is a constant operation.
    while i < 3 * n: # This is 3n
        j = 10 # This is a constant operation (assignment).
        while j <= 50: # This will run 50 times O(50).
            j = j + 1 # This is a constant operation.
        j = 0 # This is a constant operation.
        while j < (n * (n * n)): # (_very_)Deceptive, but n * n * n = n^3, so O(n^3)
            j = j + 2 # This is a constant operation.
            # This is n^3 / 2 because j is going to reach this value faster by,
            # it's incrementing by 2's
        i = i + 1 # This is a constant operation.

# O(1) + O(3n) + O(50) + O(1) + O(1) + O(n^3) + O(1) + O(1)
# Lets add our ones up!
# O(5) again, would you look at that.
# O(3n) + O(50) + O(n^3) + O(5)
# We'll group the constants again.
# O(3n) + O(n^3) + O(55).
# Drop our additive constants.
# O(3n) + O(n^3)
# Drop our multiplicative constants
# O(n) + O(n^3)
# So, let's say n = 2. 2^3 = 8. So we have-
# Turns out we messed up, for instance: J is already at 10, so that's O(50 - 10)
# We also forgot about multiplying runtimes according to the runtime of the,
# loop construct they're in.

# Rework: O(1) + O(3n) * (O(40) + O(1) + O(1) + O(n^3) + O(1) + O(1))
# So let's add our inner ones up.
#  O(1) + O(3n) * (O(40) + O(4) + O(n^3))
# Now let's finish our inner addition
#  O(1) + O(3n) * (O(44) + O(n ^ 3))
# O(3n + 1) *O(n^3 + 44)
# O(3n) * O(n^3) -- We forgot about distributing here- 
# let's check the correct version (sans constants):

# Never figured out why...
# O(3n) * (O(40) + O(n^3/2)) => O(3n / 40) + O(3n^4 /2)
# Everything makes sense except how we end up dividing 3n by 40.
# I get that we distribute 3n.
# Why *isn't* it O(3n + 40) is what we really want to know.