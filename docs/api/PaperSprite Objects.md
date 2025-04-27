## PaperSprite Objects

```python
class PaperSprite(Object)
```

Sprite Asset

Stores the data necessary to render a single 2D sprite (from a region of a texture)
Can also contain collision shapes for the sprite.
see: UPaperSpriteComponent

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperSprite.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_source_textures`` (Array[Texture]):  [Read-Write] Additional source textures for other slots
- ``alternate_material`` (MaterialInterface):  [Read-Write] The alternate material to use on a sprite instance if not overridden (this is only used for Diced render geometry, and will be the opaque material in that case, slot 1)
- ``atlas_group`` (PaperSpriteAtlas):  [Read-Write] Spritesheet group that this sprite belongs to
- ``body_setup`` (BodySetup):  [Read-Write] Baked physics data.
- ``collision_geometry`` (SpriteGeometryCollection):  [Read-Write] Custom collision geometry polygons (in texture space)
- ``collision_thickness`` (float):  [Read-Write] The extrusion thickness of collision geometry when using a 3D collision domain
- ``custom_pivot_point`` (Vector2D):  [Read-Write] Custom pivot point (relative to the sprite rectangle)
- ``default_material`` (MaterialInterface):  [Read-Write] The material to use on a sprite instance if not overridden (this is the default material when only one is being used, and is the translucent/masked material for Diced render geometry, slot 0)
- ``origin_in_source_image_before_trimming`` (Vector2D):  [Read-Write] Origin within SourceImage, prior to atlasing
- ``pivot_mode`` (SpritePivotMode):  [Read-Write] Pivot mode
- ``pixels_per_unreal_unit`` (float):  [Read-Write] The scaling factor between pixels and Unreal units (cm) (e.g., 0.64 would make a 64 pixel wide sprite take up 100 cm)
- ``render_geometry`` (SpriteGeometryCollection):  [Read-Write] Custom render geometry polygons (in texture space)
- ``rotated_in_source_image`` (bool):  [Read-Write] This texture is rotated in the atlas
- ``snap_pivot_to_pixel_grid`` (bool):  [Read-Write] Should the pivot be snapped to a pixel boundary?
- ``sockets`` (Array[PaperSpriteSocket]):  [Read-Write] List of sockets on this sprite
- ``source_dimension`` (Vector2D):  [Read-Write] Dimensions within SourceTexture (in pixels)
- ``source_image_dimension_before_trimming`` (Vector2D):  [Read-Write] Dimensions of SourceImage
- ``source_texture`` (Texture2D):  [Read-Write] The source texture that the sprite comes from
- ``source_texture_dimension`` (Vector2D):  [Read-Write] Dimension of the texture when this sprite was created
  Used when the sprite is resized at some point
- ``source_uv`` (Vector2D):  [Read-Write] Position within SourceTexture (in pixels)
- ``sprite_collision_domain`` (SpriteCollisionMode):  [Read-Write] Collision domain (no collision, 2D, or 3D)
- ``trimmed_in_source_image`` (bool):  [Read-Write] This texture is trimmed, consider the values above

<a id="unreal.PaperSprite.default_material"></a>

#### default_material

```python
@property
def default_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] The material to use on a sprite instance if not overridden (this is the default material when only one is being used, and is the translucent/masked material for Diced render geometry, slot 0)

<a id="unreal.PaperSprite.alternate_material"></a>

#### alternate_material

```python
@property
def alternate_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] The alternate material to use on a sprite instance if not overridden (this is only used for Diced render geometry, and will be the opaque material in that case, slot 1)

<a id="unreal.PaperSpriteActor"></a>