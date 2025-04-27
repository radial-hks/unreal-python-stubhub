## TraceQueryTestResultsInner Objects

```python
class TraceQueryTestResultsInner(StructBase)
```

Trace Query Test Results Inner

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: TraceQueryTestResults.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box_results`` (TraceQueryTestResultsInnerMost):  [Read-Write] The results associated with the box
- ``capsule_results`` (TraceQueryTestResultsInnerMost):  [Read-Write] The results associated with the capsule
- ``line_results`` (TraceQueryTestResultsInnerMost):  [Read-Write] The results associated with the line trace
- ``sphere_results`` (TraceQueryTestResultsInnerMost):  [Read-Write] The results associated with the sphere

<a id="unreal.TraceQueryTestResultsInner.__init__"></a>

#### __init__

```python
def __init__(
    line_results: TraceQueryTestResultsInnerMost = [[
        False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0,
        0, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
    ], ["None", "None", "None"], False, [], [], False],
    sphere_results: TraceQueryTestResultsInnerMost = [[
        False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0,
        0, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
    ], ["None", "None", "None"], False, [], [], False],
    capsule_results: TraceQueryTestResultsInnerMost = [[
        False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0,
        0, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
    ], ["None", "None", "None"], False, [], [], False],
    box_results: TraceQueryTestResultsInnerMost = [[
        False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0,
        0, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
    ], ["None", "None", "None"], False, [], [], False]
) -> None
```

<a id="unreal.TraceQueryTestResultsInner.line_results"></a>

#### line_results

```python
@property
def line_results() -> TraceQueryTestResultsInnerMost
```

(TraceQueryTestResultsInnerMost):  [Read-Write] The results associated with the line trace

<a id="unreal.TraceQueryTestResultsInner.line_results"></a>

#### line_results

```python
@line_results.setter
def line_results(value: TraceQueryTestResultsInnerMost) -> None
```

<a id="unreal.TraceQueryTestResultsInner.sphere_results"></a>

#### sphere_results

```python
@property
def sphere_results() -> TraceQueryTestResultsInnerMost
```

(TraceQueryTestResultsInnerMost):  [Read-Write] The results associated with the sphere

<a id="unreal.TraceQueryTestResultsInner.sphere_results"></a>

#### sphere_results

```python
@sphere_results.setter
def sphere_results(value: TraceQueryTestResultsInnerMost) -> None
```

<a id="unreal.TraceQueryTestResultsInner.capsule_results"></a>

#### capsule_results

```python
@property
def capsule_results() -> TraceQueryTestResultsInnerMost
```

(TraceQueryTestResultsInnerMost):  [Read-Write] The results associated with the capsule

<a id="unreal.TraceQueryTestResultsInner.capsule_results"></a>

#### capsule_results

```python
@capsule_results.setter
def capsule_results(value: TraceQueryTestResultsInnerMost) -> None
```

<a id="unreal.TraceQueryTestResultsInner.box_results"></a>

#### box_results

```python
@property
def box_results() -> TraceQueryTestResultsInnerMost
```

(TraceQueryTestResultsInnerMost):  [Read-Write] The results associated with the box

<a id="unreal.TraceQueryTestResultsInner.box_results"></a>

#### box_results

```python
@box_results.setter
def box_results(value: TraceQueryTestResultsInnerMost) -> None
```

<a id="unreal.OverlayItem"></a>