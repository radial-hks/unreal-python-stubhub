## WdpLocalToGlobalGeoRefParams Objects

```python
class WdpLocalToGlobalGeoRefParams(ParamsBase)
```

Wdp Local to Global Geo Ref Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``from_`` (Array[Vector]):  [Read-Write]
- ``geo_ref_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.WdpLocalToGlobalGeoRefParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(geo_ref_eid: int = 0, from_: Array[Vector] = []) -> None
```

<a id="unreal.WdpLocalToGlobalGeoRefParams.geo_ref_eid"></a>

#### geo\_ref\_eid

```python
@property
def geo_ref_eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.WdpLocalToGlobalGeoRefParams.geo_ref_eid"></a>

#### geo\_ref\_eid

```python
@geo_ref_eid.setter
def geo_ref_eid(value: int) -> None
```

<a id="unreal.WdpLocalToGlobalGeoRefParams.from_"></a>

#### from\_

```python
@property
def from_() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.WdpLocalToGlobalGeoRefParams.from_"></a>

#### from\_

```python
@from_.setter
def from_(value: Array[Vector]) -> None
```

<a id="unreal.WdpLocalToGlobalGeoRefResult"></a>