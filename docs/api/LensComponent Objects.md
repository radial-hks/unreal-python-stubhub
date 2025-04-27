## LensComponent Objects

```python
class LensComponent(ActorComponent)
```

Component for applying a post-process lens distortion effect to a CineCameraComponent on the same actor

**C++ Source:**

- **Plugin**: LensComponent
- **Module**: LensComponent
- **File**: LensComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_distortion`` (bool):  [Read-Write] Whether or not to apply distortion to the target camera component
- ``apply_nodal_offset_on_tick`` (bool):  [Read-Write] If checked, nodal offset will be applied automatically when this component ticks.
  Set to false if nodal offset needs to be manually applied at some other time (via Blueprints).
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``cropped_filmback`` (CameraFilmbackSettings):  [Read-Write] Cropped filmback to use if the filmback override settings are set to use it
- ``distortion_rendering_mode`` (DistortionRenderingMode):  [Read-Write] Specifies how the distortion should be rendered in the post-processing pipeline
- ``distortion_source`` (DistortionHandlerPicker):  [Read-Write]
  deprecated: This property has been deprecated. Use GetDistortionSource() and SetDistortionSource() instead.
- ``distortion_state`` (LensDistortionState):  [Read-Write] The current distortion state
- ``distortion_state_source`` (DistortionSource):  [Read-Write] Specifies from where the distortion state information comes
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``eval_inputs`` (LensFileEvaluationInputs):  [Read-Write] Inputs to LensFile evaluation
- ``evaluation_mode`` (FIZEvaluationMode):  [Read-Write] Specify how the Lens File should be evaluated
- ``filmback_override`` (FilmbackOverrideSource):  [Read-Write] Controls whether this component can override the camera's filmback, and if so, which override to use
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``lens_file_picker`` (LensFilePicker):  [Read-Write] Lens File used to drive distortion with current camera settings
- ``lens_model`` (type(Class)):  [Read-Write] The current lens model used for distortion
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``original_tracked_component_location`` (Vector):  [Read-Write] * Location and Rotation of the TrackedComponent prior to nodal offset being applied
  * Note: These are marked Interp so that they will be recorded in a level sequence to support re-applying nodal offset
  * However, recording of FTransform properties is not currently supported by the transform track recorder.
  * FRotator and FQuat are also not supported by the basic property track recorder, but FVector is, so we use that for both location and rotation.
- ``original_tracked_component_rotation`` (Vector):  [Read-Write]
- ``original_tracked_component_transform`` (Transform):  [Read-Only] Serialized transform of the TrackedComponent prior to nodal offset being applied
- ``override_camera_overscan`` (bool):  [Read-Write] If checked, the camera's overscan value will be driven by the lens component to automatically compensate for distortion.
  The camera's overscan crop property will also be driven based on the distortion rendering mode:
    Disabled for Post Process Material
    Enabled for Scene View Extension
  Note: The camera's overscan properties will not be automatically reset when the "Apply Distortion" or "Override Camera Overscan" properties are disabled
- ``overscan_multiplier`` (float):  [Read-Write] The percentage of the computed overscan that should be applied to the target camera
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``scale_overscan`` (bool):  [Read-Write] Whether to scale the computed overscan by the overscan percentage
- ``target_camera_component`` (ComponentReference):  [Read-Write] The CineCameraComponent on which to apply the post-process distortion effect

<a id="unreal.LensComponent.apply_distortion"></a>

#### apply_distortion

```python
@property
def apply_distortion() -> bool
```

(bool):  [Read-Write] Whether or not to apply distortion to the target camera component

<a id="unreal.LensComponent.apply_distortion"></a>

#### apply_distortion

```python
@apply_distortion.setter
def apply_distortion(value: bool) -> None
```

<a id="unreal.LensComponent.override_camera_overscan"></a>

#### override_camera_overscan

```python
@property
def override_camera_overscan() -> bool
```

(bool):  [Read-Write] If checked, the camera's overscan value will be driven by the lens component to automatically compensate for distortion.
The camera's overscan crop property will also be driven based on the distortion rendering mode:
  Disabled for Post Process Material
  Enabled for Scene View Extension
Note: The camera's overscan properties will not be automatically reset when the "Apply Distortion" or "Override Camera Overscan" properties are disabled

<a id="unreal.LensComponent.override_camera_overscan"></a>

#### override_camera_overscan

```python
@override_camera_overscan.setter
def override_camera_overscan(value: bool) -> None
```

<a id="unreal.LensComponent.distortion_state"></a>

#### distortion_state

```python
@property
def distortion_state() -> LensDistortionState
```

(LensDistortionState):  [Read-Write] The current distortion state

<a id="unreal.LensComponent.distortion_state"></a>

#### distortion_state

```python
@distortion_state.setter
def distortion_state(value: LensDistortionState) -> None
```

<a id="unreal.LensComponent.scale_overscan"></a>

#### scale_overscan

```python
@property
def scale_overscan() -> bool
```

(bool):  [Read-Write] Whether to scale the computed overscan by the overscan percentage

<a id="unreal.LensComponent.scale_overscan"></a>

#### scale_overscan

```python
@scale_overscan.setter
def scale_overscan(value: bool) -> None
```

<a id="unreal.LensComponent.overscan_multiplier"></a>

#### overscan_multiplier

```python
@property
def overscan_multiplier() -> float
```

(float):  [Read-Write] The percentage of the computed overscan that should be applied to the target camera

<a id="unreal.LensComponent.overscan_multiplier"></a>

#### overscan_multiplier

```python
@overscan_multiplier.setter
def overscan_multiplier(value: float) -> None
```

<a id="unreal.LensComponent.original_tracked_component_location"></a>

#### original_tracked_component_location

```python
@property
def original_tracked_component_location() -> Vector
```

(Vector):  [Read-Write] * Location and Rotation of the TrackedComponent prior to nodal offset being applied
* Note: These are marked Interp so that they will be recorded in a level sequence to support re-applying nodal offset
* However, recording of FTransform properties is not currently supported by the transform track recorder.
* FRotator and FQuat are also not supported by the basic property track recorder, but FVector is, so we use that for both location and rotation.

<a id="unreal.LensComponent.original_tracked_component_location"></a>

#### original_tracked_component_location

```python
@original_tracked_component_location.setter
def original_tracked_component_location(value: Vector) -> None
```

<a id="unreal.LensComponent.original_tracked_component_rotation"></a>

#### original_tracked_component_rotation

```python
@property
def original_tracked_component_rotation() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.LensComponent.original_tracked_component_rotation"></a>

#### original_tracked_component_rotation

```python
@original_tracked_component_rotation.setter
def original_tracked_component_rotation(value: Vector) -> None
```

<a id="unreal.LensComponent.original_tracked_component_transform"></a>

#### original_tracked_component_transform

```python
@property
def original_tracked_component_transform() -> Transform
```

(Transform):  [Read-Only] Serialized transform of the TrackedComponent prior to nodal offset being applied

<a id="unreal.LensComponent.distortion_source"></a>

#### distortion_source

```python
@property
def distortion_source() -> DistortionHandlerPicker
```

(DistortionHandlerPicker):  [Read-Write]
deprecated: This property has been deprecated. Use GetDistortionSource() and SetDistortionSource() instead.

<a id="unreal.LensComponent.distortion_source"></a>

#### distortion_source

```python
@distortion_source.setter
def distortion_source(value: DistortionHandlerPicker) -> None
```

<a id="unreal.LensComponent.was_nodal_offset_applied_this_tick"></a>

#### was_nodal_offset_applied_this_tick

```python
def was_nodal_offset_applied_this_tick() -> bool
```

x.was_nodal_offset_applied_this_tick() -> bool
Returns true if nodal offset was applied during the current tick, false otherwise

Returns:
    bool:

<a id="unreal.LensComponent.was_distortion_evaluated"></a>

#### was_distortion_evaluated

```python
def was_distortion_evaluated() -> bool
```

x.was_distortion_evaluated() -> bool
Returns true if distortion was evaluated this tick

Returns:
    bool:

<a id="unreal.LensComponent.should_apply_nodal_offset_on_tick"></a>

#### should_apply_nodal_offset_on_tick

```python
def should_apply_nodal_offset_on_tick() -> bool
```

x.should_apply_nodal_offset_on_tick() -> bool
Returns true if nodal offset will be automatically applied during this component's tick, false otherwise

Returns:
    bool:

<a id="unreal.LensComponent.should_apply_distortion"></a>

#### should_apply_distortion

```python
def should_apply_distortion() -> bool
```

x.should_apply_distortion() -> bool
Whether distortion should be applied to the target camera

Returns:
    bool:

<a id="unreal.LensComponent.set_overscan_multiplier"></a>

#### set_overscan_multiplier

```python
def set_overscan_multiplier(multiplier: float) -> None
```

x.set_overscan_multiplier(multiplier) -> None
Set the LensFile used by this component

Args:
    multiplier (float):

<a id="unreal.LensComponent.set_lens_model"></a>

#### set_lens_model

```python
def set_lens_model(model: Class) -> None
```

x.set_lens_model(model) -> None
Set the current lens model

Args:
    model (type(Class)):

<a id="unreal.LensComponent.set_lens_file_picker"></a>

#### set_lens_file_picker

```python
def set_lens_file_picker(lens_file: LensFilePicker) -> None
```

x.set_lens_file_picker(lens_file) -> None
Set the LensFile picker used by this component

Args:
    lens_file (LensFilePicker):

<a id="unreal.LensComponent.set_lens_file_evaluation_inputs"></a>

#### set_lens_file_evaluation_inputs

```python
def set_lens_file_evaluation_inputs(focus: float, zoom: float) -> None
```

x.set_lens_file_evaluation_inputs(focus, zoom) -> None
Set the data used by this component to evaluate the LensFile

Args:
    focus (float): 
    zoom (float):

<a id="unreal.LensComponent.set_lens_file"></a>

#### set_lens_file

```python
def set_lens_file(lens_file: LensFile) -> None
```

x.set_lens_file(lens_file) -> None
Set the LensFile used by this component

Args:
    lens_file (LensFile):

<a id="unreal.LensComponent.set_fiz_evaluation_mode"></a>

#### set_fiz_evaluation_mode

```python
def set_fiz_evaluation_mode(mode: FIZEvaluationMode) -> None
```

x.set_fiz_evaluation_mode(mode) -> None
Set the evaluation mode used to evaluate the LensFile

Args:
    mode (FIZEvaluationMode):

<a id="unreal.LensComponent.set_filmback_override_setting"></a>

#### set_filmback_override_setting

```python
def set_filmback_override_setting(setting: FilmbackOverrideSource) -> None
```

x.set_filmback_override_setting(setting) -> None
Set the filmback override setting

Args:
    setting (FilmbackOverrideSource):

<a id="unreal.LensComponent.set_distortion_state"></a>

#### set_distortion_state

```python
def set_distortion_state(state: LensDistortionState) -> None
```

x.set_distortion_state(state) -> None
Set the current distortion state

Args:
    state (LensDistortionState):

<a id="unreal.LensComponent.set_distortion_source"></a>

#### set_distortion_source

```python
def set_distortion_source(source: DistortionSource) -> None
```

x.set_distortion_source(source) -> None
Set the distortion source setting

Args:
    source (DistortionSource):

<a id="unreal.LensComponent.set_cropped_filmback"></a>

#### set_cropped_filmback

```python
def set_cropped_filmback(filmback: CameraFilmbackSettings) -> None
```

x.set_cropped_filmback(filmback) -> None
Set the cropped filmback (only relevant if the filmback override setting is set to use the CroppedFilmback

Args:
    filmback (CameraFilmbackSettings):

<a id="unreal.LensComponent.set_apply_nodal_offset_on_tick"></a>

#### set_apply_nodal_offset_on_tick

```python
def set_apply_nodal_offset_on_tick(apply_nodal_offset: bool) -> None
```

x.set_apply_nodal_offset_on_tick(apply_nodal_offset) -> None
Set whether nodal offset should be automatically applied during this component's tick

Args:
    apply_nodal_offset (bool):

<a id="unreal.LensComponent.set_apply_distortion"></a>

#### set_apply_distortion

```python
def set_apply_distortion(apply: bool) -> None
```

x.set_apply_distortion(apply) -> None
Set whether distortion should be applied to the target camera

Args:
    apply (bool):

<a id="unreal.LensComponent.get_overscan_multiplier"></a>

#### get_overscan_multiplier

```python
def get_overscan_multiplier() -> float
```

x.get_overscan_multiplier() -> float
Get the evaluation mode used to evaluate the LensFile

Returns:
    float:

<a id="unreal.LensComponent.get_original_focal_length"></a>

#### get_original_focal_length

```python
def get_original_focal_length() -> float
```

x.get_original_focal_length() -> float
Get the original (not adjusted for overscan) focal length of the camera

Returns:
    float:

<a id="unreal.LensComponent.get_lens_model"></a>

#### get_lens_model

```python
def get_lens_model() -> Class
```

x.get_lens_model() -> type(Class)
Get the current lens model

Returns:
    type(Class):

<a id="unreal.LensComponent.get_lens_file_picker"></a>

#### get_lens_file_picker

```python
def get_lens_file_picker() -> LensFilePicker
```

x.get_lens_file_picker() -> LensFilePicker
Get the LensFile picker used by this component

Returns:
    LensFilePicker:

<a id="unreal.LensComponent.get_lens_file_evaluation_inputs"></a>

#### get_lens_file_evaluation_inputs

```python
def get_lens_file_evaluation_inputs() -> LensFileEvaluationInputs
```

x.get_lens_file_evaluation_inputs() -> LensFileEvaluationInputs
Get the data used by this component to evaluate the LensFile

Returns:
    LensFileEvaluationInputs:

<a id="unreal.LensComponent.get_lens_file"></a>

#### get_lens_file

```python
def get_lens_file() -> LensFile
```

x.get_lens_file() -> LensFile
Get the LensFile used by this component

Returns:
    LensFile:

<a id="unreal.LensComponent.get_lens_distortion_handler"></a>

#### get_lens_distortion_handler

```python
def get_lens_distortion_handler() -> LensDistortionModelHandlerBase
```

x.get_lens_distortion_handler() -> LensDistortionModelHandlerBase
Returns the LensDistortionHandler in use for the current LensModel

Returns:
    LensDistortionModelHandlerBase:

<a id="unreal.LensComponent.get_fiz_evaluation_mode"></a>

#### get_fiz_evaluation_mode

```python
def get_fiz_evaluation_mode() -> FIZEvaluationMode
```

x.get_fiz_evaluation_mode() -> FIZEvaluationMode
Get the evaluation mode used to evaluate the LensFile

Returns:
    FIZEvaluationMode:

<a id="unreal.LensComponent.get_filmback_override_setting"></a>

#### get_filmback_override_setting

```python
def get_filmback_override_setting() -> FilmbackOverrideSource
```

x.get_filmback_override_setting() -> FilmbackOverrideSource
Get the filmback override setting

Returns:
    FilmbackOverrideSource:

<a id="unreal.LensComponent.get_distortion_state"></a>

#### get_distortion_state

```python
def get_distortion_state() -> LensDistortionState
```

x.get_distortion_state() -> LensDistortionState
Get the current distortion state

Returns:
    LensDistortionState:

<a id="unreal.LensComponent.get_distortion_source"></a>

#### get_distortion_source

```python
def get_distortion_source() -> DistortionSource
```

x.get_distortion_source() -> DistortionSource
Get the distortion source setting

Returns:
    DistortionSource:

<a id="unreal.LensComponent.get_cropped_filmback"></a>

#### get_cropped_filmback

```python
def get_cropped_filmback() -> CameraFilmbackSettings
```

x.get_cropped_filmback() -> CameraFilmbackSettings
Get the cropped filmback (only relevant if the filmback override setting is set to use the CroppedFilmback

Returns:
    CameraFilmbackSettings:

<a id="unreal.LensComponent.clear_distortion_state"></a>

#### clear_distortion_state

```python
def clear_distortion_state() -> None
```

x.clear_distortion_state() -> None
Reset the distortion state to defaults to represent "no distortion"

<a id="unreal.LensComponent.apply_nodal_offset"></a>

#### apply_nodal_offset

```python
def apply_nodal_offset(component_to_offset: SceneComponent,
                       use_manual_inputs: bool = False,
                       manual_focus_input: float = 0.000000,
                       manual_zoom_input: float = 0.000000) -> None
```

x.apply_nodal_offset(component_to_offset, use_manual_inputs=False, manual_focus_input=0.000000, manual_zoom_input=0.000000) -> None
Manually apply nodal offset to the specified component.
If bUseManualInputs is true, the input Focus and Zoom values will be used to evaluate the LensFile .
If bUseManualInputs is false, the LensFile be will evaluated based on the Lens Component's evaluation mode.

Args:
    component_to_offset (SceneComponent): 
    use_manual_inputs (bool): 
    manual_focus_input (float): 
    manual_zoom_input (float):

<a id="unreal.ComposurePipelineBaseActor"></a>