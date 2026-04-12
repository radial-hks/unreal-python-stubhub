## WDPUpdateScreenPosBoundParams Objects

```python
class WDPUpdateScreenPosBoundParams(ParamsBase)
```

WDPUpdate Screen Pos Bound Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpScreenPosBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_change_notify`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``id`` (Guid):  [Read-Write]
- ``location`` (Vector):  [Read-Write]

<a id="unreal.WDPUpdateScreenPosBoundParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(id: Guid = [],
             enable_change_notify: bool = False,
             location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.WDPUpdateScreenPosBoundParams.id"></a>

#### id

```python
@property
def id() -> Guid
```

(Guid):  [Read-Write]

<a id="unreal.WDPUpdateScreenPosBoundParams.id"></a>

#### id

```python
@id.setter
def id(value: Guid) -> None
```

<a id="unreal.WDPUpdateScreenPosBoundParams.enable_change_notify"></a>

#### enable\_change\_notify

```python
@property
def enable_change_notify() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WDPUpdateScreenPosBoundParams.enable_change_notify"></a>

#### enable\_change\_notify

```python
@enable_change_notify.setter
def enable_change_notify(value: bool) -> None
```

<a id="unreal.WDPUpdateScreenPosBoundParams.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WDPUpdateScreenPosBoundParams.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.WDPScreenPosBoundRemoveParams"></a>