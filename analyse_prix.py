def main():
	print("Lecture...")
	nums = [0] * 10
	with open("prices.csv", "r") as file:
		for line in file.readlines():
			line_list = line.split(",")
			name = ",".join(line_list[:-1])
			price = float(line_list[-1])
			if price != 0:
				first_digit = str(price * 1000000) [0]
				nums[int(first_digit)] += 1

	r = max(nums)
	nums2 = nums[:]
	for i in range(len(nums)):
		nums2[i] = nums[i] / r
	
	for i in range(1, len(nums)):
		n = int(nums2[i] * 50)
		s = '#' * n
		print(f"{i}:{nums[i]} {s}")


if __name__ == '__main__':
	main()