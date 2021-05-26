import numpy as np

array = np.random.randint(0, 255, (3, 3), dtype=np.uint8)

print(array)

resizedArray = np.zeros((2, 2), dtype=np.uint8)

windowSize = 2
stride = 1
windowElement = windowSize ** 2

for i in range(int(windowSize)):
    for j in range(int(windowSize)):
        tempArray = array[i:i + windowSize, j:j + windowSize]
        tempArraySum = np.sum(tempArray)
        resizedArray[i, j] = tempArraySum / windowElement

print("Output")
print(resizedArray)
