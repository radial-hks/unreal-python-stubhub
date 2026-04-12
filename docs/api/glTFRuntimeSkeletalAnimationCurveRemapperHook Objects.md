## glTFRuntimeSkeletalAnimationCurveRemapperHook Objects

```python
class glTFRuntimeSkeletalAnimationCurveRemapperHook(StructBase)
```

Gl TFRuntime Skeletal Animation Curve Remapper Hook

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``context`` (Object):  [Read-Write]
- ``remapper`` (glTFRuntimeAnimationCurveRemapper):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationCurveRemapperHook.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        remapper:
    glTFRuntimeAnimationCurveRemapper = glTFRuntimeAnimationCurveRemapper(),
        context: Object = None) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationCurveRemapperHook.remapper"></a>

#### remapper

```python
@property
def remapper() -> glTFRuntimeAnimationCurveRemapper
```

(glTFRuntimeAnimationCurveRemapper):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationCurveRemapperHook.remapper"></a>

#### remapper

```python
@remapper.setter
def remapper(value: glTFRuntimeAnimationCurveRemapper) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationCurveRemapperHook.context"></a>

#### context

```python
@property
def context() -> Object
```

(Object):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationCurveRemapperHook.context"></a>

#### context

```python
@context.setter
def context(value: Object) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook"></a>