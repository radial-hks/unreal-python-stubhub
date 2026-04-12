## glTFRuntimeSkeletonBoneRemapperHook Objects

```python
class glTFRuntimeSkeletonBoneRemapperHook(StructBase)
```

Gl TFRuntime Skeleton Bone Remapper Hook

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``context`` (Object):  [Read-Write]
- ``remapper`` (glTFRuntimeBoneRemapper):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonBoneRemapperHook.__init__"></a>

#### \_\_init\_\_

```python
def __init__(remapper: glTFRuntimeBoneRemapper = glTFRuntimeBoneRemapper(),
             context: Object = None) -> None
```

<a id="unreal.glTFRuntimeSkeletonBoneRemapperHook.remapper"></a>

#### remapper

```python
@property
def remapper() -> glTFRuntimeBoneRemapper
```

(glTFRuntimeBoneRemapper):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonBoneRemapperHook.remapper"></a>

#### remapper

```python
@remapper.setter
def remapper(value: glTFRuntimeBoneRemapper) -> None
```

<a id="unreal.glTFRuntimeSkeletonBoneRemapperHook.context"></a>

#### context

```python
@property
def context() -> Object
```

(Object):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletonBoneRemapperHook.context"></a>

#### context

```python
@context.setter
def context(value: Object) -> None
```

<a id="unreal.glTFRuntimeSkeletonConfig"></a>