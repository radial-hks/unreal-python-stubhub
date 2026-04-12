## WDPScreenPosBoundRemoveParams Objects

```python
class WDPScreenPosBoundRemoveParams(ParamsBase)
```

WDPScreen Pos Bound Remove Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpScreenPosBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``ids`` (Array[Guid]):  [Read-Write]

<a id="unreal.WDPScreenPosBoundRemoveParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(ids: Array[Guid] = []) -> None
```

<a id="unreal.WDPScreenPosBoundRemoveParams.ids"></a>

#### ids

```python
@property
def ids() -> Array[Guid]
```

(Array[Guid]):  [Read-Write]

<a id="unreal.WDPScreenPosBoundRemoveParams.ids"></a>

#### ids

```python
@ids.setter
def ids(value: Array[Guid]) -> None
```

<a id="unreal.WDPScreenPosBoundAddResult"></a>