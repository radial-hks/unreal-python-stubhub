## WDPScreenPosBoundChange Objects

```python
class WDPScreenPosBoundChange(StructBase)
```

WDPScreen Pos Bound Change

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpScreenPosBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``id`` (Guid):  [Read-Write]
- ``location`` (Vector):  [Read-Write]

<a id="unreal.WDPScreenPosBoundChange.__init__"></a>

#### \_\_init\_\_

```python
def __init__(id: Guid = [],
             location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.WDPScreenPosBoundChange.id"></a>

#### id

```python
@property
def id() -> Guid
```

(Guid):  [Read-Write]

<a id="unreal.WDPScreenPosBoundChange.id"></a>

#### id

```python
@id.setter
def id(value: Guid) -> None
```

<a id="unreal.WDPScreenPosBoundChange.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WDPScreenPosBoundChange.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.WDPScreenPosBoundChangeEventArgs"></a>