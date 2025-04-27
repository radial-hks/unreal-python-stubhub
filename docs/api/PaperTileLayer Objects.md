## PaperTileLayer Objects

```python
class PaperTileLayer(Object)
```

This class represents a single layer in a tile map.  All layers in the map must have the size dimensions.

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperTileLayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_offset_override`` (float):  [Read-Write] The override offset of the collision for this layer (when bOverrideCollisionOffset is set)
  Note: This is measured in Unreal Units (cm) from the center of the tile map component, not from the previous layer.
- ``collision_thickness_override`` (float):  [Read-Write] The override thickness of the collision for this layer (when bOverrideCollisionThickness is set)
- ``hidden_in_editor`` (bool):  [Read-Write] Is this layer currently hidden in the editor?
- ``hidden_in_game`` (bool):  [Read-Write] Should this layer be hidden in the game?
- ``layer_collides`` (bool):  [Read-Write] Should this layer generate collision?
  Note: This only has an effect if the owning tile map has collision enabled
- ``layer_color`` (LinearColor):  [Read-Write] The color of this layer (multiplied with the tile map color and passed to the material as a vertex color)
- ``layer_height`` (int32):  [Read-Write] Height of the layer (in tiles)
- ``layer_name`` (Text):  [Read-Write] Name of the layer
- ``layer_width`` (int32):  [Read-Write] Width of the layer (in tiles)
- ``override_collision_offset`` (bool):  [Read-Write] Should this layer use a custom offset for generated collision instead of the layer drawing offset?
- ``override_collision_thickness`` (bool):  [Read-Write] Should this layer use a custom thickness for generated collision instead of the thickness setting in the tile map?

<a id="unreal.PaperTileLayer.layer_name"></a>

#### layer_name

```python
@property
def layer_name() -> Text
```

(Text):  [Read-Only] Name of the layer

<a id="unreal.PaperTileLayer.layer_width"></a>

#### layer_width

```python
@property
def layer_width() -> int
```

(int32):  [Read-Only] Width of the layer (in tiles)

<a id="unreal.PaperTileLayer.layer_height"></a>

#### layer_height

```python
@property
def layer_height() -> int
```

(int32):  [Read-Only] Height of the layer (in tiles)

<a id="unreal.PaperTileLayer.hidden_in_game"></a>

#### hidden_in_game

```python
@property
def hidden_in_game() -> bool
```

(bool):  [Read-Only] Should this layer be hidden in the game?

<a id="unreal.PaperTileLayer.layer_collides"></a>

#### layer_collides

```python
@property
def layer_collides() -> bool
```

(bool):  [Read-Only] Should this layer generate collision?
Note: This only has an effect if the owning tile map has collision enabled

<a id="unreal.PaperTileLayer.override_collision_thickness"></a>

#### override_collision_thickness

```python
@property
def override_collision_thickness() -> bool
```

(bool):  [Read-Only] Should this layer use a custom thickness for generated collision instead of the thickness setting in the tile map?

<a id="unreal.PaperTileLayer.override_collision_offset"></a>

#### override_collision_offset

```python
@property
def override_collision_offset() -> bool
```

(bool):  [Read-Only] Should this layer use a custom offset for generated collision instead of the layer drawing offset?

<a id="unreal.PaperTileLayer.collision_thickness_override"></a>

#### collision_thickness_override

```python
@property
def collision_thickness_override() -> float
```

(float):  [Read-Only] The override thickness of the collision for this layer (when bOverrideCollisionThickness is set)

<a id="unreal.PaperTileLayer.collision_offset_override"></a>

#### collision_offset_override

```python
@property
def collision_offset_override() -> float
```

(float):  [Read-Only] The override offset of the collision for this layer (when bOverrideCollisionOffset is set)
Note: This is measured in Unreal Units (cm) from the center of the tile map component, not from the previous layer.

<a id="unreal.PaperTileLayer.layer_color"></a>

#### layer_color

```python
@property
def layer_color() -> LinearColor
```

(LinearColor):  [Read-Only] The color of this layer (multiplied with the tile map color and passed to the material as a vertex color)

<a id="unreal.PaperTileMap"></a>