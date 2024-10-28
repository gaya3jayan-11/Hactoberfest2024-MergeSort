import random

class MergeSort:
    def __init__(self):
        self.num_list = []

    def generate_random_array(self, n):
        self.num_list = [random.randint(0, 9999) for _ in range(n)]

    def display_array(self):
        for num in self.num_list:
            print(f"{num:8}")

    def sort_array(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.sort_array(low, mid)
            self.sort_array(mid + 1, high)
            self.merge(low, mid, high)

    def merge(self, low, mid, high):
        b = []
        i, j = low, mid + 1

        while i <= mid and j <= high:
            if self.num_list[i] < self.num_list[j]:
                b.append(self.num_list[i])
                i += 1
            else:
                b.append(self.num_list[j])
                j += 1

        while i <= mid:
            b.append(self.num_list[i])
            i += 1

        while j <= high:
            b.append(self.num_list[j])
            j += 1

        for k in range(len(b)):
            self.num_list[low + k] = b[k]

if __name__ == "__main__":
    i_num = int(input("Enter number of elements to sort: "))
    my_list_obj = MergeSort()
    my_list_obj.generate_random_array(i_num)
    print("\nUnsorted Array:")
    my_list_obj.display_array()
    my_list_obj.sort_array(0, i_num - 1)
    print("\nSorted Array:")
    my_list_obj.display_array()
