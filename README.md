# CS61A: Structure and Interpretation of Computer Programs
## 0x01 Index
| **Lab**                        | **Homework**               | **Project**                    |
| ------------------------------ | -------------------------- | ------------------------------ |
| [lab00](./lab/lab00/lab00.py)  | [hw01](./hw/hw01/hw01.py)  | [hog](./project/hog/hog.py)    |
| [lab01](./lab/lab01/lab01.py)  | [hw02](./hw/hw02/hw02.py)  | [cats](./project/cats/cats.py) |
| [lab02](./lab/lab02/lab02.py)  | [hw03](./hw/hw03/hw03.py)  | [ants](./project/ants/ants.py) |
| [lab03](./lab/lab03/lab03.py)  | [hw04](./hw/hw04/hw04.py)  |                                |
| [lab04](./lab/lab04/lab04.py)  | [hw05](./hw/hw05/hw05.py)  |                                |
| [lab05](./lab/lab05/lab05.py)  | [hw06](./hw/hw06/hw06.py)  |                                |
| [lab06](./lab/lab06/lab06.py)  | [hw07](./hw/hw07/hw07.scm) |                                |
| [lab07](./lab/lab07/lab07.py)  |                            |                                |
| [lab08](./lab/lab08/lab08.py)  |                            |                                |
| [lab09](./lab/lab09/lab09.scm) |                            |                                |

## 0x02 Timeline
- **Oct. 12th 2024**
  1. config envs e.g. py.ok account, etc.
  2. finish [lab00](./lab/lab00/lab00.py)
   
- **Oct. 13th 2024**
  1. finish [hw01](./hw/hw01/hw01.py), [lab01](./lab/lab01/lab01.py)
   
- **Oct. 14th 2024**
  1. finish [hw02](./hw/hw02/hw02.py) :) the last function was interesting OVO
   
- **Oct. 15th 2024**
  1. do [*Hog*](./project/hog/hog.py) project till Problem 11 which require implementing `sus_strategy` (really interesting proj AwA)
   
- **Oct. 16th 2024**
  1. finish [*Hog*](./project/hog/hog.py) project, but final strategy is not wise as expected : (
   
- **Oct. 20th 2024**
  1. finish [lab002](./lab/lab02/lab02.py) the last implement of the funtion of which is a thrilling experience for me cuz i coded it correctly once OMG 😱😱😱😱😱😱
   
- **Oct. 26th 2024**
  1. finish [hw03](./hw/hw03/hw03.py)(on recursive) the last optional question of which is kinda terribly disgusting 🤢🤢🤢🤢🤢
   
- **Oct. 28th 2024**
  1. finish [lab03](./lab/lab03/lab03.py)
   
- **Oct. 29th 2024**
  > BTW, use `python3 score.py > correction.txt &` to check performance of `final_diff` in the [cats.py](./project/cats/cats.py)
  1. [*cats*](./project/cats/cats.py) project finish all problems 🥺🥺🥺🥺🥺
  2. **[TODO]** maybe modify the `final_diff` function
  3. **[DONE]** figure out why
    > If memoized encounters the (typed, source) pair again, it should return the memoized value if the provided limit is less than or equal to the cached limit. Otherwise, the difference should be recalculated, recached, and returned.

    understand `memo_diff()` why is
    ``` py
    if limit <= cached_limit:
        return cached_value
    ```
    **Re:** this memo is used to cache whether the case is over limit, and will return *inf* if the cached 
    limit show there's no possibility that it's able to match these two strings
   
- **Oct. 31th 2024**
  1. finish [lab04](./lab/lab04/lab04.py) where i learnt:
    > The nature of the abstraction barrier guarantees that changing the implementation of an data abstraction shouldn't affect the functionality of any programs that use that data abstraction, as long as the constructors and selectors were used properly.
    very important light on code construction
  2. finish [hw04](./hw/hw04/hw04.py) exciting and felt benefited a lot from previous oi experience 😋
      this really is a nice course, and i plan to read the implementation of tree in python in this source code given
  3. finish [lab05](./lab/lab05/lab05.py) tree abstraction code [here](./lab/lab05/tree.py)
   
- **Nov. 1st 2024**
  1. finish [hw05](./hw/hw05/hw05.py) understand **generator function**!!! it can return a sequence of value, and if wants to have a good use of it, we have to understand that what it yields is a generator thus we can use `for` loop to iterate all its `yield` outputs! and (from the point of constructing a generator function, ) when constructing a generator function, we have to make clear knowledge of what it return is a sub-problem of the entire problem, what we need to consider is just every single new element that yields out each time.
  2. do problem 1-3 of project [*ants*](./project/ants/ants.py)

- **Nov. 4th 2024**
  1. finish [lab06](./lab/lab06/lab06.py) tiny introduce to OOP

- **Nov. 8th 2024**
  1. finish basic part of [ants](./project/ants/ants.py) ✌️✌️✌️✌️✌️
  2. finish ECs of [ants](./project/ants/ants.py)!!!!!! yeahhhhhhhhh!

- **Nov. 10th 2024**
  1. finish [hw06](./hw/hw06/hw06.py)
  
- **Nov. 11th 2024**
  1. finish [lab07](./lab/lab07/lab07.py)
  2. finish [lab08](./lab/lab08/lab08.py)
  3. ohhhhhh! head for SCHEME lang 😋

- **Nov. 12th 2024**
  1. finish [lab09](./lab/lab09/lab09.scm)

## 0x03 References
- https://composingprograms.netlify.app/
- https://www.bilibili.com/video/BV1sy411z7nA
- https://cs61a.org/
- https://www.composingprograms.com/

