## StartCompassParams Objects

```python
class StartCompassParams(ParamsBase)
```

Start Compass Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CompassAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display`` (CompassDisplay):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``source`` (CompassSource):  [Read-Write]

<a id="unreal.StartCompassParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    source: CompassSource = ["", ""],
    display: CompassDisplay = [[300.000000, 100.000000], 300,
                               "leftTop"]) -> None
```

<a id="unreal.StartCompassParams.source"></a>

#### source

```python
@property
def source() -> CompassSource
```

(CompassSource):  [Read-Write]

<a id="unreal.StartCompassParams.source"></a>

#### source

```python
@source.setter
def source(value: CompassSource) -> None
```

<a id="unreal.StartCompassParams.display"></a>

#### display

```python
@property
def display() -> CompassDisplay
```

(CompassDisplay):  [Read-Write]

<a id="unreal.StartCompassParams.display"></a>

#### display

```python
@display.setter
def display(value: CompassDisplay) -> None
```

<a id="unreal.CreateMoveAlongPathParams"></a>