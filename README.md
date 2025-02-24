# 📘 LeetCode Notebook Framework Generator (LeetCode Notebook代码框架生成器)

**LeetCode Helper** is a Python script that automates the process of **organizing LeetCode problems** into structured folders and generating a **Jupyter Notebook** for coding and testing. This script is designed with the help of ChatGPT.

---

## 🚀 Features

- 📂 **Automatically creates a folder** for each problem based on its title.
- 📝 **Generates a Jupyter Notebook** with a pre-filled function template.
- 🔍 **Extracts the first example input** and integrates it into the notebook.
- 🔧 **Error handling** for missing files and incorrect formats.
- 🏗️ **Follows SOLID principles**, making the code modular and extendable.

---

## 📥 Installation

### Prerequisites

- **Python 3.7+**
- **nbformat library**: `pip install nbformat`

## 🛠 Usage

### 1️⃣ Prepare an Input File

Create a .txt file containing the leetcode problem description(from title to example) and all the given code in code space. Example:

```plaintext
238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### 2️⃣ Run the Script

Run the script using the command:

```bash
./run.sh 
```

or 

```bash 
python <code.py> <input.txt> <code category>
```

### 3️⃣ Output

After running the script, a new folder structure is created:

```plaintext
📂 Array & String/
└── 📂 238. Product of Array Except Self/
    └── 📄 code.ipynb
```

Inside code.ipynb, you’ll find:

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

solution = Solution()
solution.productExceptSelf([1,2,3,4])
```

## 🎯 Why Use This?

✅ Saves Time: No need to manually create folders and notebooks.
✅ Organized Workflow: Keeps LeetCode problems structured.
✅ Easily Extendable: Modify it for custom categories or formats.

## 🛠 Future Enhancements

📌 Support for Multiple Test Cases
📌 Dynamic Category Assignment Based on Topics
📌 Integration with Online LeetCode APIs
