## PCGDispatchThreadCount Objects

```python
class PCGDispatchThreadCount(EnumBase)
```

Total number of threads that will be dispatched for this kernel.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCustomHLSL.h

<a id="unreal.PCGDispatchThreadCount.FROM_FIRST_OUTPUT_PIN"></a>

#### FROM_FIRST_OUTPUT_PIN

0: One thread per pin data element.

<a id="unreal.PCGDispatchThreadCount.FIXED"></a>

#### FIXED

1

<a id="unreal.PCGDispatchThreadCount.FROM_PRODUCT_OF_INPUT_PINS"></a>

#### FROM_PRODUCT_OF_INPUT_PINS

2: Dispatches a thread per element in the product of one or more pins. So if there are 4 data elements in pin A and 6 data elements in pin B, 24 threads will be dispatched.

<a id="unreal.PCGDifferenceDensityFunction"></a>