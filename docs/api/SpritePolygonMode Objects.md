## SpritePolygonMode Objects

```python
class SpritePolygonMode(EnumBase)
```

Method of specifying polygons for a sprite's render or collision data

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: SpriteEditorOnlyTypes.h

<a id="unreal.SpritePolygonMode.SOURCE_BOUNDING_BOX"></a>

#### SOURCE_BOUNDING_BOX

0: Use the bounding box of the source sprite (no optimization)

<a id="unreal.SpritePolygonMode.TIGHT_BOUNDING_BOX"></a>

#### TIGHT_BOUNDING_BOX

1: Tighten the bounding box around the sprite to exclude fully transparent areas (the default)

<a id="unreal.SpritePolygonMode.SHRINK_WRAPPED"></a>

#### SHRINK_WRAPPED

2: Shrink-wrapped geometry

<a id="unreal.SpritePolygonMode.FULLY_CUSTOM"></a>

#### FULLY_CUSTOM

3: Fully custom geometry; edited by hand

<a id="unreal.SpritePolygonMode.DICED"></a>

#### DICED

4: Diced (split up into smaller squares, including only non-empty ones in the final geometry).  This option is only supported for Render geometry and will be ignored for Collision geometry.

<a id="unreal.PCGKernelAttributeType"></a>