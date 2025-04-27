## UsdPrimPathList Objects

```python
class UsdPrimPathList(StructBase)
```

Simple wrapper because we're not allowed to have TMap properties with TArray<FString> as values

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``prim_paths`` (Array[str]):  [Read-Write]

<a id="unreal.UsdPrimPathList.__init__"></a>

#### __init__

```python
def __init__(prim_paths: Array[str] = []) -> None
```

<a id="unreal.UsdPrimPathList.prim_paths"></a>

#### prim_paths

```python
@property
def prim_paths() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.UsdPrimPathList.prim_paths"></a>

#### prim_paths

```python
@prim_paths.setter
def prim_paths(value: Array[str]) -> None
```

<a id="unreal.UsdMetadataValue"></a>