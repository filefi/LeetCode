# 49. Group Anagrams
Given an array of strings, group anagrams together.

Example:
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
Note:

- All inputs will be in lowercase.
- The order of your output does not matter.

## 49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
```
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
说明：

- 所有输入均为小写字母。
- 不考虑答案输出的顺序。

## 实现
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in d:
                d[key] = [i]
            else:
                d[key].append(i)
        return list(d.values())
```
