# TASK 2 Self Study Report
## New data structure: bytearray <br>
Bytearray is a mutable sequence of bytes. It's elements are from 0 - 255 and it can be modified after creation. <br>
Comparing to bytes, bytearray is mutable. You can change the elements by some useful methods, like append(), extend() and insert(). <br>
Bytearray is useful when working with binary data , such as network communication, file processing and binary protocols.

### Introduction
First, converts the string into a bytearray object. Then the for loop goes through every byte in the bytearray.<br>
For each byte, the program adds 4. After encryption the output might look difficult to understand. <br>
Then use another for loop to reverses the encryption. At last decode() converts the bytearray back into a readable string.

## New Algorithm: Hash Search Algorithm <br>
### Introduction
Hash Search  is a constant-time average-case search algorithm that maps data elements to specific positions in a hash table via a hash function. <br>
Unlike the linear search  or binary search  covered in basic algorithm curricula, hash search abandons the "comparison-based" search logic and <br>
achieves direct access to data through mathematical mapping. Hash search is selected for self-study. It is widely used in high-performance systems (e.g., database indexing, cache systems, network routing tables) due to its efficient average performance, making it a core algorithm for understanding "time-space trade-off" in computer science.

### Time Complexity
Best/Average Case: Hash search has O(1)time complexity (the core advantage of hash tables), which is why it is widely used in high-performance lookup scenarios (e.g., caches, databases).<br>
Worst Case: Degenerates to O(n)due to severe collisions (avoidable with good hash function design and load factor control).<br>
Key to Optimization: Maintain a reasonable load factor (α≈0.7), use a uniformly distributed hash function, and choose efficient collision resolution strategies (e.g., red-black tree for separate chaining).<br>
The link of introduction video for this task:【Desktop 2026.04.16 - 21.24.18.06】 https://www.bilibili.com/video/BV13tdaBSEyP/?share_source=copy_web&vd_source=8f3b64e3a6d9194d4e8ddce60e4e1a86
