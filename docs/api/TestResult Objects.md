## TestResult Objects

```python
class TestResult(StructBase)
```

定义一个结构体来存储测试结果

**C++ Source:**

- **Plugin**: RuntimeDebugTool
- **Module**: RuntimeDebugGui
- **File**: PerformanceTestLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration_ms`` (float):  [Read-Write]
- ``status`` (str):  [Read-Write] 持续时间，毫秒
- ``test_name`` (str):  [Read-Write]

<a id="unreal.TestResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(test_name: str = "",
             duration_ms: float = 0.000000,
             status: str = "") -> None
```

<a id="unreal.TestResult.test_name"></a>

#### test\_name

```python
@property
def test_name() -> str
```

(str):  [Read-Only]

<a id="unreal.TestResult.duration_ms"></a>

#### duration\_ms

```python
@property
def duration_ms() -> float
```

(float):  [Read-Only]

<a id="unreal.TestResult.status"></a>

#### status

```python
@property
def status() -> str
```

(str):  [Read-Only] 持续时间，毫秒

<a id="unreal.DCPAssetLoadParam"></a>