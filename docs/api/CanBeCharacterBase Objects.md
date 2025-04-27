## CanBeCharacterBase Objects

```python
class CanBeCharacterBase(EnumBase)
```

Determines whether a Character can attempt to step up onto a component when they walk in to it.

**C++ Source:**

- **Module**: Engine
- **File**: PrimitiveComponent.h

<a id="unreal.CanBeCharacterBase.ECB_NO"></a>

#### ECB_NO

0: Character cannot step up onto this Component.

<a id="unreal.CanBeCharacterBase.ECB_YES"></a>

#### ECB_YES

1: Character can step up onto this Component.

<a id="unreal.CanBeCharacterBase.ECB_OWNER"></a>

#### ECB_OWNER

2: Owning actor determines whether character can step up onto this Component (default true unless overridden in code).
see: AActor::CanBeBaseForCharacter()

<a id="unreal.RayTracingGroupCullingPriority"></a>