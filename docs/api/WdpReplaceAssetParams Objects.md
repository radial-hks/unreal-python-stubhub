## WdpReplaceAssetParams Objects

```python
class WdpReplaceAssetParams(ParamsBase)
```

Wdp Replace Asset Params

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: WdpAssetAPI
- **File**: WdpAssetAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[int64]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``seed_id`` (str):  [Read-Write]

<a id="unreal.WdpReplaceAssetParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[int] = [], seed_id: str = "") -> None
```

<a id="unreal.WdpReplaceAssetParams.eids"></a>

#### eids

```python
@property
def eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.WdpReplaceAssetParams.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[int]) -> None
```

<a id="unreal.WdpReplaceAssetParams.seed_id"></a>

#### seed\_id

```python
@property
def seed_id() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpReplaceAssetParams.seed_id"></a>

#### seed\_id

```python
@seed_id.setter
def seed_id(value: str) -> None
```

<a id="unreal.WdpReplaceAssetResult"></a>