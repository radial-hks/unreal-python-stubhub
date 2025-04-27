## ComposureLibrary Objects

```python
class ComposureLibrary(BlueprintFunctionLibrary)
```

Composure Blueprint Library

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: ComposureBlueprintLibrary.h

<a id="unreal.ComposureLibrary.set_uv_map_settings_to_material_parameters"></a>

#### set_uv_map_settings_to_material_parameters

```python
@classmethod
def set_uv_map_settings_to_material_parameters(
        cls, uv_map_settings: ComposureUVMapSettings,
        material: MaterialInstanceDynamic) -> None
```

X.set_uv_map_settings_to_material_parameters(uv_map_settings, material) -> None
Sets parameters of a material that uses Composure's MF_UVMap_SampleLocation material function.

Args:
    uv_map_settings (ComposureUVMapSettings): 
    material (MaterialInstanceDynamic):

<a id="unreal.ComposureLibrary.request_redraw_composure_viewport"></a>

#### request_redraw_composure_viewport

```python
@classmethod
def request_redraw_composure_viewport(cls) -> None
```

X.request_redraw_composure_viewport() -> None
Request redrawing the compositing editor viewport  if it is valid.
If it is invalid, this function will create a new view port client.

<a id="unreal.ComposureLibrary.rename_composure_element"></a>

#### rename_composure_element

```python
@classmethod
def rename_composure_element(cls, original_element_name: Name,
                             new_element_name: Name) -> bool
```

X.rename_composure_element(original_element_name, new_element_name) -> bool
Rename a specific composure element

Args:
    original_element_name (Name): The name of the composure element that we want to rename.
    new_element_name (Name): The new name for the composure element.

Returns:
    bool: bool                     Whether the renaming operation is successful or not.

<a id="unreal.ComposureLibrary.refresh_composure_element_list"></a>

#### refresh_composure_element_list

```python
@classmethod
def refresh_composure_element_list(cls) -> None
```

X.refresh_composure_element_list() -> None
Re-queries the scene for element actors and rebuilds the authoritative list used by the editor.

<a id="unreal.ComposureLibrary.is_composure_element_drawing"></a>

#### is_composure_element_drawing

```python
@classmethod
def is_composure_element_drawing(cls,
                                 comp_element: CompositingElement) -> bool
```

X.is_composure_element_drawing(comp_element) -> bool
Determines if the specified element is being rendered by the hidden compositing viewport.

Args:
    comp_element (CompositingElement): The element actor you're querying for

Returns:
    bool: True if the game-thread is in the middle of queuing the specified element.

<a id="unreal.ComposureLibrary.invert_uv_displacement_map_encoding_parameters"></a>

#### invert_uv_displacement_map_encoding_parameters

```python
@classmethod
def invert_uv_displacement_map_encoding_parameters(cls,
                                                   in_: Vector2D) -> Vector2D
```

X.invert_uv_displacement_map_encoding_parameters(in_) -> Vector2D
Converts displacement encoding parameters to decoding parameters.
Can also be used to convert displacement decoding parameters to encoding parameters.

Args:
    in_ (Vector2D): 

Returns:
    Vector2D: 

    out (Vector2D):

<a id="unreal.ComposureLibrary.get_red_green_uv_factors_from_chromatic_aberration"></a>

#### get_red_green_uv_factors_from_chromatic_aberration

```python
@classmethod
def get_red_green_uv_factors_from_chromatic_aberration(
        cls, chromatic_aberration_amount: float) -> Vector2D
```

X.get_red_green_uv_factors_from_chromatic_aberration(chromatic_aberration_amount) -> Vector2D
Returns the red and green channel factors from percentage of chromatic aberration.

Args:
    chromatic_aberration_amount (float): 

Returns:
    Vector2D: 

    red_green_uv_factors (Vector2D):

<a id="unreal.ComposureLibrary.get_projection_matrix_from_post_move_settings"></a>

#### get_projection_matrix_from_post_move_settings

```python
@classmethod
def get_projection_matrix_from_post_move_settings(
        cls, post_move_settings: ComposurePostMoveSettings,
        horizontal_fov_angle: float, aspect_ratio: float) -> Matrix
```

X.get_projection_matrix_from_post_move_settings(post_move_settings, horizontal_fov_angle, aspect_ratio) -> Matrix
Returns a non-centered projection matrix.

Args:
    post_move_settings (ComposurePostMoveSettings): 
    horizontal_fov_angle (float): The desired horizontal FOV in degrees.
    aspect_ratio (float): The desired aspect ratio.

Returns:
    Matrix: 

    projection_matrix (Matrix):

<a id="unreal.ComposureLibrary.get_player_display_gamma"></a>

#### get_player_display_gamma

```python
@classmethod
def get_player_display_gamma(
        cls, player_camera_manager: PlayerCameraManager) -> float
```

X.get_player_display_gamma(player_camera_manager) -> float
Returns display gamma of a given player camera manager, or 0 if no scene viewport attached.

Args:
    player_camera_manager (PlayerCameraManager): 

Returns:
    float: 

    display_gamma (float):

<a id="unreal.ComposureLibrary.get_cropping_uv_transformation_matrix_from_post_move_settings"></a>

#### get_cropping_uv_transformation_matrix_from_post_move_settings

```python
@classmethod
def get_cropping_uv_transformation_matrix_from_post_move_settings(
        cls, post_move_settings: ComposurePostMoveSettings,
        aspect_ratio: float) -> Tuple[Matrix, Matrix]
```

X.get_cropping_uv_transformation_matrix_from_post_move_settings(post_move_settings, aspect_ratio) -> (croping_uv_transformation_matrix=Matrix, uncroping_uv_transformation_matrix=Matrix)
Returns UV transformation matrix and its inversed to crop.

Args:
    post_move_settings (ComposurePostMoveSettings): 
    aspect_ratio (float): The desired aspect ratio.

Returns:
    tuple: 

    croping_uv_transformation_matrix (Matrix): 

    uncroping_uv_transformation_matrix (Matrix):

<a id="unreal.ComposureLibrary.get_composure_element"></a>

#### get_composure_element

```python
@classmethod
def get_composure_element(cls, element_name: Name) -> CompositingElement
```

X.get_composure_element(element_name) -> CompositingElement
Get a specific composure element

Args:
    element_name (Name): The name of the composure element that we want to get.

Returns:
    CompositingElement: CompositingElement      The composure element found. It can be nullptr if there is no composure element matches the input name.

<a id="unreal.ComposureLibrary.delete_composure_element_and_children"></a>

#### delete_composure_element_and_children

```python
@classmethod
def delete_composure_element_and_children(cls,
                                          element_to_delete: Name) -> None
```

X.delete_composure_element_and_children(element_to_delete) -> None
Delete a specific composure element without evoking prompt window. Will delete all of its children as well.

Args:
    element_to_delete (Name): The name of the composure element that we want to delete.

<a id="unreal.ComposureLibrary.create_player_compositing_target"></a>

#### create_player_compositing_target

```python
@classmethod
def create_player_compositing_target(
        cls, world_context_object: Object) -> ComposurePlayerCompositingTarget
```

X.create_player_compositing_target(world_context_object) -> ComposurePlayerCompositingTarget
Creates a Player Compositing Target which you can modify during gameplay.

Args:
    world_context_object (Object): 

Returns:
    ComposurePlayerCompositingTarget:

<a id="unreal.ComposureLibrary.create_composure_element"></a>

#### create_composure_element

```python
@classmethod
def create_composure_element(
        cls,
        element_name: Name,
        class_type: Class,
        level_context: Actor = None) -> CompositingElement
```

X.create_composure_element(element_name, class_type, level_context=None) -> CompositingElement
Create a new Composure in the level without any parenting relationship.

Args:
    element_name (Name): The name for the newly created composure element
    class_type (type(Class)): The type for the new composure element
    level_context (Actor): The level context of current level. Default value is nullptr.

Returns:
    CompositingElement: CompositingElement      The created composure element.

<a id="unreal.ComposureLibrary.copy_camera_settings_to_scene_capture"></a>

#### copy_camera_settings_to_scene_capture

```python
@classmethod
def copy_camera_settings_to_scene_capture(
        cls,
        src_camera: CameraComponent,
        dst_capture_component: SceneCaptureComponent2D,
        original_focal_length: float,
        overscan_factor: float = 1.000000) -> None
```

X.copy_camera_settings_to_scene_capture(src_camera, dst_capture_component, original_focal_length, overscan_factor=1.000000) -> None
Copy Camera Settings to Scene Capture

Args:
    src_camera (CameraComponent): 
    dst_capture_component (SceneCaptureComponent2D): 
    original_focal_length (float): 
    overscan_factor (float):

<a id="unreal.ComposureLibrary.attach_composure_element"></a>

#### attach_composure_element

```python
@classmethod
def attach_composure_element(cls, parent_name: Name, child_name: Name) -> bool
```

X.attach_composure_element(parent_name, child_name) -> bool
Attach one composure element as the child to another composure element in the scene.

Args:
    parent_name (Name): The name of the parent composure element.
    child_name (Name): The name of the child composure element.

Returns:
    bool: bool                     Whether the attaching process is successful or not.

<a id="unreal.ComposureGameSettings"></a>