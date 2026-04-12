## EmbankEntityInfo Objects

```python
class EmbankEntityInfo(StructBase)
```

Embank Entity Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``ways`` (Array[EmbankWayInfo]):  [Read-Write]

<a id="unreal.EmbankEntityInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             ways: Array[EmbankWayInfo] = []) -> None
```

<a id="unreal.EmbankEntityInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.EmbankEntityInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.EmbankEntityInfo.ways"></a>

#### ways

```python
@property
def ways() -> Array[EmbankWayInfo]
```

(Array[EmbankWayInfo]):  [Read-Write]

<a id="unreal.EmbankEntityInfo.ways"></a>

#### ways

```python
@ways.setter
def ways(value: Array[EmbankWayInfo]) -> None
```

<a id="unreal.SamplerMeshSettingInfo"></a>