if __name__ == '__main__':

 nums = []

 for i in range(3):
  ekle = int(input(f"please give 1 of {i+1} nums thx: "))
  nums.append(ekle)

 if len(nums) != 3:
     print("you tryna punk me gang?")
 else:
     if nums[0] > nums[1] > nums [2]:
      print("ur numbs are fr decreasing foo")
     elif nums[0] < nums[1] < nums[2]:
      print("ur numbs straight up increasing woo")
     else:
      print("ur shit all mixed up bro sry")