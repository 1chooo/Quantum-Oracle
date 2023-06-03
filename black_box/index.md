# Algorithmics (演算法) 2022 - Midterm Project

##### Tags: `Quantum-Computing`, `black-box`, `Algorithmics`, `uni-project`, `Deutsch`

> Course: CE3005 - Algorithmics  
> Dept: ATM  
> Name: Hugo ChunHo Lin  
> Student Number: 109601003

Programming Deutsch Algorithm and Running it on a Quantum Computer Simulator or a Real IBM Q Computer (請參考練習 5.5)

### pre-analyzing

![analyze](img/analyze.jpg)

## Four statuses

### Constant: Output equal 0.
欲使任何輸入（q0不論是0或1）至函數中且全部結果（q1）為0，也就代表q1之值不會受q0所影響，所以神諭（Oracle）選用I閘，如此q1便不受q0影響，且從量子電腦模擬以及量子電腦的執行結果，結果為 |0> 的機率都接近100%；|1> 的機率都接近0%，因此此黑箱函數為常數函數。

|       What I have done        |        Plot Display         |
| :---------------------------: | :-------------------------: |
|    Create quantum circuit     | ![prog1_1](img/prog1-1.png) |
|   prove through histogram.    | ![prog1_2](img/prog1-2.png) |
| Also prove in IBM Q Computer. | ![prog1_3](img/prog1-3.png) |

### Constant: Output equal 1
欲使任何輸入（q0不論是0或1）至函數中且全部結果（q1）為1，也就代表q1之值不會受q0所影響，所以神諭（Oracle）選用X閘，如此q1便不受q0影響，並且全都會變成1，且從量子電腦模擬以及量子電腦的執行結果，結果為 |0> 的機率都接近100%；|1> 的機率都接近0%，因此此黑箱函數為常數函數。

|       What I have done        |        Plot Display         |
| :---------------------------: | :-------------------------: |
|    Create quantum circuit     | ![prog2_1](img/prog2-1.png) |
|   prove through histogram.    | ![prog2_2](img/prog2-2.png) |
| Also prove in IBM Q Computer. | ![prog2_3](img/prog2-3.png) |


### Balanced: Input equal Output.
欲使函數為平衡函數，因而挑選CNOT閘，並且讓q0為控制位元；q1為目標位元，當啟動CNOT閘時，q1會從0轉至1；不啟動CNOT閘時，q1會從1轉至0；進而做出輸出與輸入相等，且從量子電腦模擬以及量子電腦的執行結果，結果為 |1> 的機率都接近100%；|0> 的機率都接近0%，因此此黑箱函數為平衡函數。

|       What I have done        |        Plot Display         |
| :---------------------------: | :-------------------------: |
|    Create quantum circuit     | ![prog3_1](img/prog3-1.png) |
|   prove through histogram.    | ![prog3_2](img/prog3-2.png) |
| Also prove in IBM Q Computer. | ![prog3_3](img/prog3-3.png) |

### Balanced: Input not equal Output.
欲使函數為平衡函數，因而挑選CNOT閘，並且讓q0為控制位元；q1為目標位元，但是當啟動CNOT閘前，q1會先經過X閘所以所以q1會先經過轉至，q1會從0轉至1；1轉至0，接著透過CNOT閘，進而做出輸出與輸入相反，且從量子電腦模擬以及量子電腦的執行結果，結果為 |1> 的機率都接近100%；|0> 的機率都接近0%，因此此黑箱函數為平衡函數。

|       What I have done        |        Plot Display         |
| :---------------------------: | :-------------------------: |
|    Create quantum circuit     | ![prog4_1](img/prog4-1.png) |
|   prove through histogram.    | ![prog4_2](img/prog4-2.png) |
| Also prove in IBM Q Computer. | ![prog4_3](img/prog4-3.png) |

## Reference
- [Introduction to quantum computing: The Deutsch algorithm.](https://akyrillidis.github.io/notes/quant_post_8)