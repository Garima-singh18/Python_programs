nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx<len(nums):
    print(nums[idx])
    idx+=1

nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
     print(el)

    #search of a number x in this tuple
nums = [1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0
while i<len(nums):
        if(nums[i]==x):
            print("found at idx",i)
        i+=1

nums = [1,4,9,16,25,36,49,64,81,100,36]
x = 36
idx = 0
for el in nums:
     if(el==x):
          print("number found at idx",idx)
          idx+=1
     