## TraceQueryTestResultsInnerMost Objects

```python
class TraceQueryTestResultsInnerMost(StructBase)
```

Trace Query Test Results Inner Most

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: TraceQueryTestResults.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``multi_hits`` (Array[HitResult]):  [Read-Write] Result from doing a multi sweep
- ``multi_names`` (Array[TraceQueryTestNames]):  [Read-Write] Names found from doing a multi sweep
- ``multi_result`` (bool):  [Read-Write] The true/false value returned from the multi sweep
- ``single_hit`` (HitResult):  [Read-Write] Result from doing a single sweep
- ``single_names`` (TraceQueryTestNames):  [Read-Write] Names found from doing a single sweep
- ``single_result`` (bool):  [Read-Write] The true/false value returned from the single sweep

<a id="unreal.TraceQueryTestResultsInnerMost.__init__"></a>

#### __init__

```python
def __init__(single_hit: HitResult = [
    False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0, 0,
    [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
],
             single_names: TraceQueryTestNames = ["None", "None", "None"],
             single_result: bool = False,
             multi_hits: Array[HitResult] = [],
             multi_names: Array[TraceQueryTestNames] = [],
             multi_result: bool = False) -> None
```

<a id="unreal.TraceQueryTestResultsInnerMost.single_hit"></a>

#### single_hit

```python
@property
def single_hit() -> HitResult
```

(HitResult):  [Read-Write] Result from doing a single sweep

<a id="unreal.TraceQueryTestResultsInnerMost.single_hit"></a>

#### single_hit

```python
@single_hit.setter
def single_hit(value: HitResult) -> None
```

<a id="unreal.TraceQueryTestResultsInnerMost.single_names"></a>

#### single_names

```python
@property
def single_names() -> TraceQueryTestNames
```

(TraceQueryTestNames):  [Read-Write] Names found from doing a single sweep

<a id="unreal.TraceQueryTestResultsInnerMost.single_names"></a>

#### single_names

```python
@single_names.setter
def single_names(value: TraceQueryTestNames) -> None
```

<a id="unreal.TraceQueryTestResultsInnerMost.single_result"></a>

#### single_result

```python
@property
def single_result() -> bool
```

(bool):  [Read-Write] The true/false value returned from the single sweep

<a id="unreal.TraceQueryTestResultsInnerMost.single_result"></a>

#### single_result

```python
@single_result.setter
def single_result(value: bool) -> None
```

<a id="unreal.TraceQueryTestResultsInnerMost.multi_hits"></a>

#### multi_hits

```python
@property
def multi_hits() -> Array[HitResult]
```

(Array[HitResult]):  [Read-Write] Result from doing a multi sweep

<a id="unreal.TraceQueryTestResultsInnerMost.multi_hits"></a>

#### multi_hits

```python
@multi_hits.setter
def multi_hits(value: Array[HitResult]) -> None
```

<a id="unreal.TraceQueryTestResultsInnerMost.multi_names"></a>

#### multi_names

```python
@property
def multi_names() -> Array[TraceQueryTestNames]
```

(Array[TraceQueryTestNames]):  [Read-Write] Names found from doing a multi sweep

<a id="unreal.TraceQueryTestResultsInnerMost.multi_names"></a>

#### multi_names

```python
@multi_names.setter
def multi_names(value: Array[TraceQueryTestNames]) -> None
```

<a id="unreal.TraceQueryTestResultsInnerMost.multi_result"></a>

#### multi_result

```python
@property
def multi_result() -> bool
```

(bool):  [Read-Write] The true/false value returned from the multi sweep

<a id="unreal.TraceQueryTestResultsInnerMost.multi_result"></a>

#### multi_result

```python
@multi_result.setter
def multi_result(value: bool) -> None
```

<a id="unreal.TraceQueryTestResultsInner"></a>