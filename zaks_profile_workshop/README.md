
## Profiling code

Profiling should be an integral part of code development. It is a way to measure the performance of a program. We should avoid premature optimizations and 
have well thought out designs. Know the runtime of your program when designing. Here is a review of sorting algorithms runtimes. We will be using sorting algoriths 
in our examples


#### Runtimes fastest to slowest
Constant time – O(1)
Linear time – O(n)
Logarithmic time – O(log n)
Linearithmic time – O(nlog n)
Factorial time – O(n!)
Quadratic time – O(n^)

### Runtimes Time and Space Complexity

| Algorithm      | Best (Time) | Average (Time) | Worst (Time)   | Worst (Space) |
|----------------|-------------|----------------|----------------|---------------|
| QuickSort      | <span style="color:orange">Ω(n log(n))</span> | <span style="color:orange">Ω(n log(n))</span>    | <span style="color:red">O(n^2) </span>        | <span style="color:chartreuse"> O(log(n)) </span>    |
| Merge Sort     | <span style="color:orange">Ω(n log(n))</span> | <span style="color:orange">Ω(n log(n))</span>    | <span style="color:orange">Ω(n log(n))</span>  | <span style="color:yellow">O(n) </span>      |
| Tim Sort       | <span style="color:yellow">Ω(n)</span>        | <span style="color:orange">Ω(n log(n))</span>    | <span style="color:orange">Ω(n log(n))</span>    | <span style="color:yellow">O(n)</span>          |
| Heap Sort      | <span style="color:orange">Ω(n log(n))</span> | <span style="color:orange">Ω(n log(n))</span>    | <span style="color:orange">Ω(n log(n))</span>    | <span style="color:green"> O(1) </span>          |
| Bubble Sort    | <span style="color:yellow">Ω(n)</span>        | <span style="color:red"> Θ(n^2)  </span>         | <span style="color:red">O(n^2)</span>         | <span style="color:green"> O(1) </span>          |
| Insertion Sort | <span style="color:yellow">Ω(n)</span>        | <span style="color:red">O(n^2)</span>         | <span style="color:red">O(n^2)</span>         | <span style="color:green"> O(1) </span>          |
| Selection Sort | <span style="color:red">O(n^2)</span>      | <span style="color:red">O(n^2)</span>         | <span style="color:red">O(n^2)</span>         | <span style="color:green"> O(1) </span>          |
| Tree Sort      | <span style="color:orange">Ω(n log(n))</span> | <span style="color:orange">Ω(n log(n))</span>    | <span style="color:red">O(n^2)</span>         | <span style="color:yellow">O(n)</span>          |
| Shell Sort     | <span style="color:orange">Ω(n log(n))</span> | <span style="color:red">O(n(log(n))^2) </span> | <span style="color:red">O(n(log(n))^2) </span> | <span style="color:green"> O(1) </span>          |
| Bucket Sort    | <span style="color:green"> Θ(n+k) </span>      | <span style="color:green"> Θ(n+k) </span>         | <span style="color:red">O(n^2)</span>         | <span style="color:yellow">O(n)</span>          |
| Radix Sort     | <span style="color:green"> Ω(nk)</span>       | <span style="color:green"> Θ(nk) </span>         | <span style="color:green">O(nk)  </span>         | <span style="color:green">O(n+k)  </span>        |
| Counting Sort  | <span style="color:green"> Θ(n+k) </span>      | <span style="color:green"> Θ(n+k) </span>         | <span style="color:green">O(n+k)  </span>       | <span style="color:yellow">O(k)   </span>         |
| Cubesort       | <span style="color:yellow">Ω(n)</span>        | <span style="color:orange"> Θ(n log(n))  </span>   | <span style="color:orange">O(n log(n))  </span>   | <span style="color:yellow">O(n)</span>          |

### Folder structure

* example_1_timeit
* example_2_cProfile
* example_3_memory_profile
* example_4_line_profile


