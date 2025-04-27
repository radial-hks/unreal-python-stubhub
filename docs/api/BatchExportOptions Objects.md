## BatchExportOptions Objects

```python
class BatchExportOptions(Object)
```

settings object used in details view of the batch retarget window

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRigEditor
- **File**: SRetargetAnimAssetsWindow.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``include_referenced_assets`` (bool):  [Read-Write] Duplicates and retargets any animation assets referenced by the input assets. For example, sequences in an animation blueprint or blendspace.
- ``overwrite_existing_files`` (bool):  [Read-Write] Any files with the same name will be overwritten instead of creating a new file with a numeric suffix.
  This is useful when iterating on a batch process.
- ``retain_additive_flags`` (bool):  [Read-Write] If retargeting additive animations, they will have their additive settings reset so that the retargeter evaluates the motion in a non-additive way.
  Setting this flag to true will ensure that the resulting animation sequences will retain their additive settings after the retarget operation.

<a id="unreal.BatchExportOptions.include_referenced_assets"></a>

#### include_referenced_assets

```python
@property
def include_referenced_assets() -> bool
```

(bool):  [Read-Write] Duplicates and retargets any animation assets referenced by the input assets. For example, sequences in an animation blueprint or blendspace.

<a id="unreal.BatchExportOptions.include_referenced_assets"></a>

#### include_referenced_assets

```python
@include_referenced_assets.setter
def include_referenced_assets(value: bool) -> None
```

<a id="unreal.BatchExportOptions.retain_additive_flags"></a>

#### retain_additive_flags

```python
@property
def retain_additive_flags() -> bool
```

(bool):  [Read-Write] If retargeting additive animations, they will have their additive settings reset so that the retargeter evaluates the motion in a non-additive way.
Setting this flag to true will ensure that the resulting animation sequences will retain their additive settings after the retarget operation.

<a id="unreal.BatchExportOptions.retain_additive_flags"></a>

#### retain_additive_flags

```python
@retain_additive_flags.setter
def retain_additive_flags(value: bool) -> None
```

<a id="unreal.BatchRetargetSettings"></a>