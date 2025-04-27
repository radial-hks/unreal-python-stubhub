## DeterminismTestResult Objects

```python
class DeterminismTestResult(StructBase)
```

Determinism Test Result

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDeterminismTestsCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_details`` (Array[str]):  [Read-Write] A mapping of [test name : additional details]
- ``data_types_tested`` (PCGDataType):  [Read-Write] BitFlags for which data types were tested
- ``flag_raised`` (bool):  [Read-Write] T/F whether a flag has been raised on this node's tests (for UI)
- ``index`` (int64):  [Read-Only] The test result index.
- ``seed`` (int32):  [Read-Write]
- ``test_result_name`` (str):  [Read-Only] The node's name
- ``test_result_title`` (Name):  [Read-Only] The node's title
- ``test_results`` (Map[Name, DeterminismLevel]):  [Read-Write] A mapping of [test names : test results]

<a id="unreal.DeterminismTestResult.__init__"></a>

#### __init__

```python
def __init__(index: int = 0,
             test_result_title: Name = "None",
             test_result_name: str = "",
             seed: int = 0,
             data_types_tested: PCGDataType = 0,
             test_results: Map[Name, DeterminismLevel] = {},
             additional_details: Array[str] = [],
             flag_raised: bool = False) -> None
```

<a id="unreal.DeterminismTestResult.index"></a>

#### index

```python
@property
def index() -> int
```

(int64):  [Read-Only] The test result index.

<a id="unreal.DeterminismTestResult.test_result_title"></a>

#### test_result_title

```python
@property
def test_result_title() -> Name
```

(Name):  [Read-Only] The node's title

<a id="unreal.DeterminismTestResult.test_result_name"></a>

#### test_result_name

```python
@property
def test_result_name() -> str
```

(str):  [Read-Only] The node's name

<a id="unreal.DeterminismTestResult.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write]

<a id="unreal.DeterminismTestResult.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.DeterminismTestResult.data_types_tested"></a>

#### data_types_tested

```python
@property
def data_types_tested() -> PCGDataType
```

(PCGDataType):  [Read-Write] BitFlags for which data types were tested

<a id="unreal.DeterminismTestResult.data_types_tested"></a>

#### data_types_tested

```python
@data_types_tested.setter
def data_types_tested(value: PCGDataType) -> None
```

<a id="unreal.DeterminismTestResult.test_results"></a>

#### test_results

```python
@property
def test_results() -> Map[Name, DeterminismLevel]
```

(Map[Name, DeterminismLevel]):  [Read-Write] A mapping of [test names : test results]

<a id="unreal.DeterminismTestResult.test_results"></a>

#### test_results

```python
@test_results.setter
def test_results(value: Map[Name, DeterminismLevel]) -> None
```

<a id="unreal.DeterminismTestResult.additional_details"></a>

#### additional_details

```python
@property
def additional_details() -> Array[str]
```

(Array[str]):  [Read-Write] A mapping of [test name : additional details]

<a id="unreal.DeterminismTestResult.additional_details"></a>

#### additional_details

```python
@additional_details.setter
def additional_details(value: Array[str]) -> None
```

<a id="unreal.DeterminismTestResult.flag_raised"></a>

#### flag_raised

```python
@property
def flag_raised() -> bool
```

(bool):  [Read-Write] T/F whether a flag has been raised on this node's tests (for UI)

<a id="unreal.DeterminismTestResult.flag_raised"></a>

#### flag_raised

```python
@flag_raised.setter
def flag_raised(value: bool) -> None
```

<a id="unreal.StaticMeshReductionSettings"></a>