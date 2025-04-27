## AvaRadialArrangement Objects

```python
class AvaRadialArrangement(EnumBase)
```

Specifies how child elements will be arranged radially.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaRadialArrangeModifier.h

<a id="unreal.AvaRadialArrangement.MONOSPACE"></a>

#### MONOSPACE

0: Each radial ring will contain the same number of elements.
The space between elements in the outer rings will be greater than the inner rings.

<a id="unreal.AvaRadialArrangement.EQUAL"></a>

#### EQUAL

1: All elements in all radial rings have the same spacing between them.
The number of elements in the inner rings will be greater than the outer rings.

<a id="unreal.AvaRadialArrangePlane"></a>