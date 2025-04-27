## UsdReferenceOptions Objects

```python
class UsdReferenceOptions(Object)
```

Options to display when adding a reference or a payload for a prim

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDReferenceOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``internal_reference`` (bool):  [Read-Write] When enabled, the reference/payload will target a prim on this stage
- ``target_file`` (FilePath):  [Read-Write] File to use as the reference
- ``target_prim_path`` (str):  [Read-Write] Use a specific prim of the target stage as the referenced/payload prim
- ``time_code_offset`` (float):  [Read-Write] Offset to apply to the referenced/payload prim's time sampled attributes
- ``time_code_scale`` (float):  [Read-Write] TimeCode scaling factor to apply to the referenced/payload prim's time sampled attributes
- ``use_default_prim`` (bool):  [Read-Write] Use the default prim of the target stage as the referenced/payload prim

<a id="unreal.UsdReferenceOptions.internal_reference"></a>

#### internal_reference

```python
@property
def internal_reference() -> bool
```

(bool):  [Read-Write] When enabled, the reference/payload will target a prim on this stage

<a id="unreal.UsdReferenceOptions.internal_reference"></a>

#### internal_reference

```python
@internal_reference.setter
def internal_reference(value: bool) -> None
```

<a id="unreal.UsdReferenceOptions.target_file"></a>

#### target_file

```python
@property
def target_file() -> FilePath
```

(FilePath):  [Read-Write] File to use as the reference

<a id="unreal.UsdReferenceOptions.target_file"></a>

#### target_file

```python
@target_file.setter
def target_file(value: FilePath) -> None
```

<a id="unreal.UsdReferenceOptions.use_default_prim"></a>

#### use_default_prim

```python
@property
def use_default_prim() -> bool
```

(bool):  [Read-Write] Use the default prim of the target stage as the referenced/payload prim

<a id="unreal.UsdReferenceOptions.use_default_prim"></a>

#### use_default_prim

```python
@use_default_prim.setter
def use_default_prim(value: bool) -> None
```

<a id="unreal.UsdReferenceOptions.target_prim_path"></a>

#### target_prim_path

```python
@property
def target_prim_path() -> str
```

(str):  [Read-Write] Use a specific prim of the target stage as the referenced/payload prim

<a id="unreal.UsdReferenceOptions.target_prim_path"></a>

#### target_prim_path

```python
@target_prim_path.setter
def target_prim_path(value: str) -> None
```

<a id="unreal.UsdReferenceOptions.time_code_offset"></a>

#### time_code_offset

```python
@property
def time_code_offset() -> float
```

(float):  [Read-Write] Offset to apply to the referenced/payload prim's time sampled attributes

<a id="unreal.UsdReferenceOptions.time_code_offset"></a>

#### time_code_offset

```python
@time_code_offset.setter
def time_code_offset(value: float) -> None
```

<a id="unreal.UsdReferenceOptions.time_code_scale"></a>

#### time_code_scale

```python
@property
def time_code_scale() -> float
```

(float):  [Read-Write] TimeCode scaling factor to apply to the referenced/payload prim's time sampled attributes

<a id="unreal.UsdReferenceOptions.time_code_scale"></a>

#### time_code_scale

```python
@time_code_scale.setter
def time_code_scale(value: float) -> None
```

<a id="unreal.LiveLinkControllerBase"></a>