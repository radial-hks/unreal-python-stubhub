## MeasureLoopEventArgs Objects

```python
class MeasureLoopEventArgs(EventArgsBase)
```

Measure Loop Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpMeasureAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area`` (str):  [Read-Write]
- ``distances`` (Array[str]):  [Read-Write]
- ``points`` (Array[str]):  [Read-Write]

<a id="unreal.MeasureLoopEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(points: Array[str] = [],
             distances: Array[str] = [],
             area: str = "") -> None
```

<a id="unreal.MeasureLoopEventArgs.points"></a>

#### points

```python
@property
def points() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.MeasureLoopEventArgs.points"></a>

#### points

```python
@points.setter
def points(value: Array[str]) -> None
```

<a id="unreal.MeasureLoopEventArgs.distances"></a>

#### distances

```python
@property
def distances() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.MeasureLoopEventArgs.distances"></a>

#### distances

```python
@distances.setter
def distances(value: Array[str]) -> None
```

<a id="unreal.MeasureLoopEventArgs.area"></a>

#### area

```python
@property
def area() -> str
```

(str):  [Read-Write]

<a id="unreal.MeasureLoopEventArgs.area"></a>

#### area

```python
@area.setter
def area(value: str) -> None
```

<a id="unreal.NodeSelectionParams"></a>