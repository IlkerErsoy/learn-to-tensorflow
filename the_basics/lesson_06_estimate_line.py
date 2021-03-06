# -- imports --
import tensorflow as tf
from tensorflow.compat.v1 import Session, global_variables_initializer, placeholder
from tensorflow.compat.v1.train import GradientDescentOptimizer


# -- variables --
# f(x) = a * x + b
a = tf.Variable(0.0)
x = placeholder(dtype=tf.float32)
b = tf.Variable(0.0)

# -- induction --
# f(x) = a * x + b
fx = tf.add(tf.multiply(a, x), b)

# -- loss --
# but we want f(x) to equal y
y = placeholder(dtype=tf.float32)
# so we calculate a loss accordingly
loss = tf.square(fx - y)
learn = GradientDescentOptimizer(.001).minimize(loss)

# start a session
sess = Session()
# initialize the variables
sess.run(global_variables_initializer())

data_x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
data_y = [0.1, 0.2, 0.4, 0.4, 0.6, 0.5, 0.7, 0.7, 0.9]

# let's calculate the total loss

print(f"""
We are using tensorflow to find the best equation that maps
x = {data_x}
to
y = {data_y}
""")

def printTotalLoss():
    total_loss = 0
    for index in range(len(data_x)):
        total_loss += sess.run(loss, feed_dict={x: data_x[index], y: data_y[index]})
    print("the total loss is", total_loss)


print("\nBefore training",end=" ")
printTotalLoss()


def getBetter():
    for index in range(len(data_x)):
        sess.run(learn, feed_dict={x: data_x[index], y: data_y[index]})


print("\nCalling get better")
for iteration in range(1, 1001):
    getBetter()
    if iteration == 1 or iteration == 10 or iteration == 100 or iteration == 1000:
        print("iteration", iteration, end=" ")
        printTotalLoss()

print("\nWe calculated the equation is y =", sess.run(a), "* x +", sess.run(b))

print("""
We can look at the data for x and y and see that it is close!
We were able to use Tensorflow to fit a line to some data.
""")