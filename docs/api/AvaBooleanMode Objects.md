## AvaBooleanMode Objects

```python
class AvaBooleanMode(EnumBase)
```

EAva Boolean Mode

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaBooleanModifier.h

<a id="unreal.AvaBooleanMode.NONE"></a>

#### NONE

0: Does not apply any mode, but get affected by other geometry modes

<a id="unreal.AvaBooleanMode.SUBTRACT"></a>

#### SUBTRACT

1: Subtract this geometry from the one it is colliding with

<a id="unreal.AvaBooleanMode.INTERSECT"></a>

#### INTERSECT

2: Only keep the intersecting geometry from the two colliding geometry

<a id="unreal.AvaBooleanMode.UNION"></a>

#### UNION

3: Merges the two colliding geometry together

<a id="unreal.AvaDynamicMeshConverterModifierType"></a>