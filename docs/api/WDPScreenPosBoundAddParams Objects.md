## WDPScreenPosBoundAddParams Objects

```python
class WDPScreenPosBoundAddParams(ParamsBase)
```

WDPScreen Pos Bound Add Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpScreenPosBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_change_notify`` (Array[bool]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``locations`` (Array[Vector]):  [Read-Write]

<a id="unreal.WDPScreenPosBoundAddParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(locations: Array[Vector] = [],
             enable_change_notify: Array[bool] = []) -> None
```

<a id="unreal.WDPScreenPosBoundAddParams.locations"></a>

#### locations

```python
@property
def locations() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.WDPScreenPosBoundAddParams.locations"></a>

#### locations

```python
@locations.setter
def locations(value: Array[Vector]) -> None
```

<a id="unreal.WDPScreenPosBoundAddParams.enable_change_notify"></a>

#### enable\_change\_notify

```python
@property
def enable_change_notify() -> Array[bool]
```

(Array[bool]):  [Read-Write]

<a id="unreal.WDPScreenPosBoundAddParams.enable_change_notify"></a>

#### enable\_change\_notify

```python
@enable_change_notify.setter
def enable_change_notify(value: Array[bool]) -> None
```

<a id="unreal.WDPUpdateScreenPosBoundParams"></a>