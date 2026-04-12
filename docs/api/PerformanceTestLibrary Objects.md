## PerformanceTestLibrary Objects

```python
class PerformanceTestLibrary(BlueprintFunctionLibrary)
```

Performance Test Library

**C++ Source:**

- **Plugin**: RuntimeDebugTool
- **Module**: RuntimeDebugGui
- **File**: PerformanceTestLibrary.h

<a id="unreal.PerformanceTestLibrary.run_single_thread_test"></a>

#### run\_single\_thread\_test

```python
@classmethod
def run_single_thread_test(cls,
                           matrix_size: int = 512,
                           iterations: int = 5) -> TestResult
```

X.run_single_thread_test(matrix_size=512, iterations=5) -> TestResult

brief: 运行单线程 CPU 性能测试

Args:
    matrix_size (int32): 矩阵的维度（例如：1000 表示 1000x1000 矩阵）
    iterations (int32): 运行测试的次数

Returns:
    TestResult: FTestResult 包含测试名称和持续时间的结果结构体

<a id="unreal.PerformanceTestLibrary.run_multi_thread_test"></a>

#### run\_multi\_thread\_test

```python
@classmethod
def run_multi_thread_test(cls,
                          matrix_size: int = 512,
                          iterations: int = 5) -> TestResult
```

X.run_multi_thread_test(matrix_size=512, iterations=5) -> TestResult

brief: 运行多线程 CPU 性能测试

Args:
    matrix_size (int32): 矩阵的维度
    iterations (int32): 运行测试的次数

Returns:
    TestResult: FTestResult 包含测试名称和持续时间的结果结构体

<a id="unreal.PerformanceTestTool"></a>