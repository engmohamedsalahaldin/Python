blocks = int(input("Enter the number of blocks: "))
height = 0
new_block = 0
for block in range(blocks):
    height = height +1
    new_block = new_block + height
    # print(height,new_block)
    if new_block == blocks:
        print("The height of the pyramid:", height)
        break
    elif new_block > blocks:
        print("The height of the pyramid:", height-1)
        break

