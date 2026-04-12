## AesFacadeModuleData Objects

```python
class AesFacadeModuleData(StructBase)
```

立面模块数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesFacadeAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``length`` (float):  [Read-Write]
- ``module_ref`` (AesAssetMetaData):  [Read-Write]
- ``position_offset`` (Vector3f):  [Read-Write]
- ``use_as_placeholder`` (bool):  [Read-Write]
- ``use_custom_length`` (bool):  [Read-Write]
- ``variations`` (Map[Name, float]):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.AesFacadeModuleData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(module_ref: AesAssetMetaData = [
    "None", 0, 0, "None", False, {}, "", [""]
],
             use_custom_length: bool = False,
             length: float = 0.000000,
             weight: float = 0.000000,
             use_as_placeholder: bool = False,
             position_offset: Vector3f = [0.000000, 0.000000, 0.000000],
             variations: Map[Name, float] = {}) -> None
```

<a id="unreal.AesFacadeModuleData.module_ref"></a>

#### module\_ref

```python
@property
def module_ref() -> AesAssetMetaData
```

(AesAssetMetaData):  [Read-Write]

<a id="unreal.AesFacadeModuleData.module_ref"></a>

#### module\_ref

```python
@module_ref.setter
def module_ref(value: AesAssetMetaData) -> None
```

<a id="unreal.AesFacadeModuleData.use_custom_length"></a>

#### use\_custom\_length

```python
@property
def use_custom_length() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesFacadeModuleData.use_custom_length"></a>

#### use\_custom\_length

```python
@use_custom_length.setter
def use_custom_length(value: bool) -> None
```

<a id="unreal.AesFacadeModuleData.length"></a>

#### length

```python
@property
def length() -> float
```

(float):  [Read-Write]

<a id="unreal.AesFacadeModuleData.length"></a>

#### length

```python
@length.setter
def length(value: float) -> None
```

<a id="unreal.AesFacadeModuleData.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write]

<a id="unreal.AesFacadeModuleData.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.AesFacadeModuleData.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@property
def use_as_placeholder() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesFacadeModuleData.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@use_as_placeholder.setter
def use_as_placeholder(value: bool) -> None
```

<a id="unreal.AesFacadeModuleData.position_offset"></a>

#### position\_offset

```python
@property
def position_offset() -> Vector3f
```

(Vector3f):  [Read-Write]

<a id="unreal.AesFacadeModuleData.position_offset"></a>

#### position\_offset

```python
@position_offset.setter
def position_offset(value: Vector3f) -> None
```

<a id="unreal.AesFacadeModuleData.variations"></a>

#### variations

```python
@property
def variations() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write]

<a id="unreal.AesFacadeModuleData.variations"></a>

#### variations

```python
@variations.setter
def variations(value: Map[Name, float]) -> None
```

<a id="unreal.AesFacadeLevelData"></a>