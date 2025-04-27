## BatchRetargetSettings Objects

```python
class BatchRetargetSettings(Object)
```

settings object used in details view of the batch retarget window

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRigEditor
- **File**: SRetargetAnimAssetsWindow.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_generate_retargeter`` (bool):  [Read-Write] When true, the system will attempt to generate an IK Retargeter compatible with the supplied source and target skeletal meshes.
  If the skeletons are successfully characterized, it will align the retarget poses automatically.
  Automatic retargeting is currently limited to common, predefined skeleton types that Unreal knows about (see documentation for full list).
  If you attempt to use a skeletal mesh that is not compatible with a predefined template, warnings will be displayed in the output log and the
  export button will be disabled. In that case, you must supply a custom retargeter asset.
- ``retarget_asset`` (IKRetargeter):  [Read-Write] You may also supply a custom IK Retargeter if needed.
- ``source_skeletal_mesh`` (SkeletalMesh):  [Read-Write] The skeletal mesh with the proportions you want to copy animation FROM.
- ``target_skeletal_mesh`` (SkeletalMesh):  [Read-Write] The skeletal mesh with the proportions you want to copy animation TO.

<a id="unreal.BatchRetargetSettings.source_skeletal_mesh"></a>

#### source_skeletal_mesh

```python
@property
def source_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write] The skeletal mesh with the proportions you want to copy animation FROM.

<a id="unreal.BatchRetargetSettings.source_skeletal_mesh"></a>

#### source_skeletal_mesh

```python
@source_skeletal_mesh.setter
def source_skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.BatchRetargetSettings.target_skeletal_mesh"></a>

#### target_skeletal_mesh

```python
@property
def target_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write] The skeletal mesh with the proportions you want to copy animation TO.

<a id="unreal.BatchRetargetSettings.target_skeletal_mesh"></a>

#### target_skeletal_mesh

```python
@target_skeletal_mesh.setter
def target_skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.BatchRetargetSettings.auto_generate_retargeter"></a>

#### auto_generate_retargeter

```python
@property
def auto_generate_retargeter() -> bool
```

(bool):  [Read-Write] When true, the system will attempt to generate an IK Retargeter compatible with the supplied source and target skeletal meshes.
If the skeletons are successfully characterized, it will align the retarget poses automatically.
Automatic retargeting is currently limited to common, predefined skeleton types that Unreal knows about (see documentation for full list).
If you attempt to use a skeletal mesh that is not compatible with a predefined template, warnings will be displayed in the output log and the
export button will be disabled. In that case, you must supply a custom retargeter asset.

<a id="unreal.BatchRetargetSettings.auto_generate_retargeter"></a>

#### auto_generate_retargeter

```python
@auto_generate_retargeter.setter
def auto_generate_retargeter(value: bool) -> None
```

<a id="unreal.BatchRetargetSettings.retarget_asset"></a>

#### retarget_asset

```python
@property
def retarget_asset() -> IKRetargeter
```

(IKRetargeter):  [Read-Write] You may also supply a custom IK Retargeter if needed.

<a id="unreal.BatchRetargetSettings.retarget_asset"></a>

#### retarget_asset

```python
@retarget_asset.setter
def retarget_asset(value: IKRetargeter) -> None
```

<a id="unreal.IKRetargetAnimInstance"></a>