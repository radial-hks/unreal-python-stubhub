## SetVisibleParams Objects

```python
class SetVisibleParams(ParamsBase)
```

Set Visible Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[str]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.SetVisibleParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[str] = [], visible: bool = False) -> None
```

<a id="unreal.SetVisibleParams.eids"></a>

#### eids

```python
@property
def eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.SetVisibleParams.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[str]) -> None
```

<a id="unreal.SetVisibleParams.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SetVisibleParams.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.GeoLayerEntityJson"></a>