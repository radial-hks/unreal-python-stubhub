## PythonBPLib Objects

```python
class PythonBPLib(BlueprintFunctionLibrary)
```

Python BPLib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonBPLib.h

<a id="unreal.PythonBPLib.viewport_redraw"></a>

#### viewport\_redraw

```python
@classmethod
def viewport_redraw(cls) -> None
```

X.viewport_redraw() -> None
Redraw the first active viewport
note: added in v1.0.4

<a id="unreal.PythonBPLib.update_reflection_capture_preview_shape"></a>

#### update\_reflection\_capture\_preview\_shape

```python
@classmethod
def update_reflection_capture_preview_shape(
        cls, capture_component: ReflectionCaptureComponent) -> None
```

X.update_reflection_capture_preview_shape(capture_component) -> None
Update Reflection Capture Preview Shape

Args:
    capture_component (ReflectionCaptureComponent):

<a id="unreal.PythonBPLib.sync_to_assets"></a>

#### sync\_to\_assets

```python
@classmethod
def sync_to_assets(cls,
                   asset_data_list: Array[AssetData],
                   allow_locked_browsers: bool = False,
                   focus_content_browser: bool = True) -> None
```

X.sync_to_assets(asset_data_list, allow_locked_browsers=False, focus_content_browser=True) -> None
Sync Assets in Content Browser.

Args:
    asset_data_list (Array[AssetData]): Asset Data list
    allow_locked_browsers (bool): Allow Sync in Locked Browsers
    focus_content_browser (bool): Set focus to the content browser

<a id="unreal.PythonBPLib.spawn_actor_from_object"></a>

#### spawn\_actor\_from\_object

```python
@classmethod
def spawn_actor_from_object(cls,
                            obj_to_use: Object,
                            location: Vector,
                            rotation: Rotator = [0.000000, 0.000000, 0.000000],
                            transient: bool = False,
                            select_actors: bool = False) -> Actor
```

X.spawn_actor_from_object(obj_to_use, location, rotation=[0.000000, 0.000000, 0.000000], transient=False, select_actors=False) -> Actor
Create an actor and place it in the world editor. The Actor can be created from a Factory, Archetype, Blueprint, Class or an Asset.
The actor will be created in the current level and will be selected.
note: This is alternative version of EditorLevelLibaray.SpawnActorFromObject, and fixed the memory leak issus in before UE 4.27

Args:
    obj_to_use (Object): 
    location (Vector): Location of the new actor.
    rotation (Rotator): 
    transient (bool): 
    select_actors (bool): 

Returns:
    Actor: The created actor.

<a id="unreal.PythonBPLib.spawn_actor_from_class"></a>

#### spawn\_actor\_from\_class

```python
@classmethod
def spawn_actor_from_class(cls,
                           actor_class: Class,
                           location: Vector,
                           rotation: Rotator = [0.000000, 0.000000, 0.000000],
                           transient: bool = False,
                           select_actors: bool = False) -> Actor
```

X.spawn_actor_from_class(actor_class, location, rotation=[0.000000, 0.000000, 0.000000], transient=False, select_actors=False) -> Actor
Create an actor and place it in the world editor. Can be created from a Blueprint or a Class.
The actor will be created in the current level and will be selected.
note: This is alternative version of EditorLevelLibaray.SpawnActorFromClass, and fixed the memory leak issus in before UE 4.27

Args:
    actor_class (type(Class)): Asset to attempt to use for an actor to place.
    location (Vector): Location of the new actor.
    rotation (Rotator): 
    transient (bool): 
    select_actors (bool): 

Returns:
    Actor: The created actor.

<a id="unreal.PythonBPLib.snapshot_details"></a>

#### snapshot\_details

```python
@classmethod
def snapshot_details(cls,
                     start_from_docking: bool,
                     override_window_size: Vector2D = [0.000000, 0.000000],
                     image_file_path: str = "") -> Array[str]
```

X.snapshot_details(start_from_docking, override_window_size=[0.000000, 0.000000], image_file_path="") -> Array[str]
Take a snapshot of the details panel and save it to a file.
note: added in v1.0.10

Args:
    start_from_docking (bool): Whether to start from docking or not.
    override_window_size (Vector2D): Override the window size.
    image_file_path (str): The path of image file to save.

Returns:
    Array[str]: The path of image file saved.

<a id="unreal.PythonBPLib.set_vector_property"></a>

#### set\_vector\_property

```python
@classmethod
def set_vector_property(cls, object: Object, property_name: str,
                        new_value: Vector) -> bool
```

X.set_vector_property(object, property_name, new_value) -> bool
Set the value of a named Vector property on the given object. Only for the property that cannot be set with 'SetEditorProperty'
note: added in v1.0.9

Args:
    object (Object): The object you want to set a property value on.
    property_name (str): The name of the object's int property.
    new_value (Vector): The new Vector value

Returns:
    bool: Whether the property was set.

<a id="unreal.PythonBPLib.set_string_property"></a>

#### set\_string\_property

```python
@classmethod
def set_string_property(cls, object: Object, property_name: str,
                        new_value: str) -> bool
```

X.set_string_property(object, property_name, new_value) -> bool
Set the value of a named FString property on the given object. Only for the property that cannot be set with 'SetEditorProperty'

Args:
    object (Object): The object you want to set a property value on.
    property_name (str): The name of the object's FString property.
    new_value (str): The new FString value

Returns:
    bool: Whether the property was set.

<a id="unreal.PythonBPLib.set_static_mesh_lod_material_id"></a>

#### set\_static\_mesh\_lod\_material\_id

```python
@classmethod
def set_static_mesh_lod_material_id(cls,
                                    mesh: StaticMesh,
                                    lod_level: int,
                                    section_index: int,
                                    id_in_mesh_static_material: int,
                                    modify_immediately: bool = True) -> None
```

X.set_static_mesh_lod_material_id(mesh, lod_level, section_index, id_in_mesh_static_material, modify_immediately=True) -> None
Assign the specified section material in Mesh

Args:
    mesh (StaticMesh): The mesh component.
    lod_level (int32): Specified LOD.
    section_index (int32): The Section ID in mesh.
    id_in_mesh_static_material (int32): The Material Index in mesh's material slots.
    modify_immediately (bool): Modify Immediately or not.

<a id="unreal.PythonBPLib.set_selected_folder_path"></a>

#### set\_selected\_folder\_path

```python
@classmethod
def set_selected_folder_path(cls, path: Name) -> None
```

X.set_selected_folder_path(path) -> None
Sets the folder path for all the selected actors.

Args:
    path (Name): The folder path name in World Outliner.

<a id="unreal.PythonBPLib.set_selected_folder"></a>

#### set\_selected\_folder

```python
@classmethod
def set_selected_folder(cls, folders: Array[str]) -> None
```

X.set_selected_folder(folders) -> None
Select specified folder in content browser.

Args:
    folders (Array[str]):

<a id="unreal.PythonBPLib.set_selected_assets_by_paths"></a>

#### set\_selected\_assets\_by\_paths

```python
@classmethod
def set_selected_assets_by_paths(cls, paths: Array[str]) -> None
```

X.set_selected_assets_by_paths(paths) -> None
Select specified assets in content browser.

Args:
    paths (Array[str]): The assets paths that will be selected, if empty, deselected current selection.

<a id="unreal.PythonBPLib.set_preview_platform"></a>

#### set\_preview\_platform

```python
@classmethod
def set_preview_platform(cls, material_quality_platform: Name,
                         feature_level_name: str) -> None
```

X.set_preview_platform(material_quality_platform, feature_level_name) -> None
Set MaterialQualityPlatform, and FeatureLevel

Args:
    material_quality_platform (Name): Contains various settings used to initialize the notification
    feature_level_name (str): Level of the Message, 0: Log, 1: warning, 2: Error

<a id="unreal.PythonBPLib.set_object_property"></a>

#### set\_object\_property

```python
@classmethod
def set_object_property(cls, object: Object, property_name: str,
                        new_value: Object) -> bool
```

X.set_object_property(object, property_name, new_value) -> bool
Set the value of a named object property on the given object. Only for the property that cannot be set with 'SetEditorProperty'

Args:
    object (Object): The object you want to set a property value on.
    property_name (str): The name of the object's UObject property.
    new_value (Object): The new object value

Returns:
    bool: Whether the property was set.

<a id="unreal.PythonBPLib.set_level_viewport_real_time"></a>

#### set\_level\_viewport\_real\_time

```python
@classmethod
def set_level_viewport_real_time(cls, realtime: bool) -> None
```

X.set_level_viewport_real_time(realtime) -> None
Set the viewport real-time state.

Args:
    realtime (bool): Whether real-time or not

<a id="unreal.PythonBPLib.set_level_viewport_locked"></a>

#### set\_level\_viewport\_locked

```python
@classmethod
def set_level_viewport_locked(cls, locked: bool) -> None
```

X.set_level_viewport_locked(locked) -> None
Set Whether showing the exact camera view when locking a viewport to a camera.

Args:
    locked (bool): Game view locked state.

<a id="unreal.PythonBPLib.set_level_viewport_is_in_game_view"></a>

#### set\_level\_viewport\_is\_in\_game\_view

```python
@classmethod
def set_level_viewport_is_in_game_view(cls, game_view: bool) -> None
```

X.set_level_viewport_is_in_game_view(game_view) -> None
Set IsInGameView of level view.

Args:
    game_view (bool): Is game view.

<a id="unreal.PythonBPLib.set_level_viewport_camera_speed"></a>

#### set\_level\_viewport\_camera\_speed

```python
@classmethod
def set_level_viewport_camera_speed(cls, speed: int) -> None
```

X.set_level_viewport_camera_speed(speed) -> None
Set the speed setting(1-8) of level viewport camera
note: added in v1.0.9

Args:
    speed (int32): Speed value of level viewport camera. 1 <= Speed <=8

<a id="unreal.PythonBPLib.set_level_viewport_camera_info"></a>

#### set\_level\_viewport\_camera\_info

```python
@classmethod
def set_level_viewport_camera_info(cls, camera_location: Vector,
                                   camera_rotation: Rotator) -> None
```

X.set_level_viewport_camera_info(camera_location, camera_rotation) -> None
Set the location and rotation of level viewport camera

Args:
    camera_location (Vector): Location of level viewport camera
    camera_rotation (Rotator): Rotation of level viewport camera

<a id="unreal.PythonBPLib.set_level_viewport_camera_fov"></a>

#### set\_level\_viewport\_camera\_fov

```python
@classmethod
def set_level_viewport_camera_fov(cls, fov: float) -> bool
```

X.set_level_viewport_camera_fov(fov) -> bool
Set the fov of level viewport camera
note: added in v1.2.0

Args:
    fov (float): Fov value of level viewport camera.

Returns:
    bool: True if fov is set successfully.

<a id="unreal.PythonBPLib.set_int_property"></a>

#### set\_int\_property

```python
@classmethod
def set_int_property(cls, object: Object, property_name: str,
                     new_value: int) -> bool
```

X.set_int_property(object, property_name, new_value) -> bool
Set the value of a named int property on the given object. Only for the property that cannot be set with 'SetEditorProperty'

Args:
    object (Object): The object you want to set a property value on.
    property_name (str): The name of the object's int property.
    new_value (int32): The new int value

Returns:
    bool: Whether the property was set.

<a id="unreal.PythonBPLib.set_folder_color"></a>

#### set\_folder\_color

```python
@classmethod
def set_folder_color(cls, folder_path: str, color: LinearColor) -> None
```

X.set_folder_color(folder_path, color) -> None
Set the of specified folder's color in content browser.

Args:
    folder_path (str): The folder path in project. For example: "/Game/StarterContent"
    color (LinearColor): The color of folder.

<a id="unreal.PythonBPLib.set_float_property"></a>

#### set\_float\_property

```python
@classmethod
def set_float_property(cls, object: Object, property_name: str,
                       new_value: float) -> bool
```

X.set_float_property(object, property_name, new_value) -> bool
Set the value of a named float property on the given object. Only for the property that cannot be set with 'SetEditorProperty'

Args:
    object (Object): The object you want to set a property value on.
    property_name (str): The name of the object's float property.
    new_value (float): The new float value

Returns:
    bool: Whether the property was set.

<a id="unreal.PythonBPLib.set_clipboard_content"></a>

#### set\_clipboard\_content

```python
@classmethod
def set_clipboard_content(cls, str: str) -> None
```

X.set_clipboard_content(str) -> None
Set the string content to clipboard

Args:
    str (str): Text to paste

<a id="unreal.PythonBPLib.set_bool_property"></a>

#### set\_bool\_property

```python
@classmethod
def set_bool_property(cls, object: Object, property_name: str,
                      new_value: bool) -> bool
```

X.set_bool_property(object, property_name, new_value) -> bool
Set the value of a named bool property on the given object. Only for the property that cannot be set with 'SetEditorProperty'

Args:
    object (Object): The object you want to set a property value on.
    property_name (str): The name of the object's bool property.
    new_value (bool): The new bool value

Returns:
    bool: Whether the property was set.

<a id="unreal.PythonBPLib.set_anim_blueprint"></a>

#### set\_anim\_blueprint

```python
@classmethod
def set_anim_blueprint(cls, mesh_component: SkeletalMeshComponent,
                       anim_blueprint: AnimBlueprint) -> None
```

X.set_anim_blueprint(mesh_component, anim_blueprint) -> None
Assign the animBlueprint to the SkeletalMeshComponent, this will clear and re-initializes the anim instance with the new class and sets animation mode to 'AnimationBlueprint'
deprecated: Use the function in PythonMeshLib instead.

Args:
    mesh_component (SkeletalMeshComponent): Skeletal mesh component
    anim_blueprint (AnimBlueprint): The new AnimBlueprint

<a id="unreal.PythonBPLib.select_none"></a>

#### select\_none

```python
@classmethod
def select_none(cls,
                note_selection_change: bool = True,
                deselect_bsp_surfs: bool = True) -> None
```

X.select_none(note_selection_change=True, deselect_bsp_surfs=True) -> None
De-select all actors.  Does nothing if GEdSelectionLock is true.

Args:
    note_selection_change (bool): If true, call NoteSelectionChange().
    deselect_bsp_surfs (bool): If true, also deselected all BSP surfaces.

<a id="unreal.PythonBPLib.select_named_actor"></a>

#### select\_named\_actor

```python
@classmethod
def select_named_actor(cls, name: str, clear_selected: bool = True) -> Actor
```

X.select_named_actor(name, clear_selected=True) -> Actor
Select actor by name(ID Name)

Args:
    name (str): The ID Name of actor, not the label name.
    clear_selected (bool): If true, deselected before select new actor.

Returns:
    Actor: A pointer to the named actor or NULL if not found.

<a id="unreal.PythonBPLib.select_component"></a>

#### select\_component

```python
@classmethod
def select_component(cls,
                     component: ActorComponent,
                     selected: bool,
                     notify: bool = True) -> None
```

X.select_component(component, selected, notify=True) -> None
Select specified component of current actor

Args:
    component (ActorComponent): The Component to be selected.
    selected (bool): Select or deSelect.
    notify (bool): Notify or not.

<a id="unreal.PythonBPLib.select_actor"></a>

#### select\_actor

```python
@classmethod
def select_actor(cls,
                 actor: Actor,
                 selected: bool,
                 notify: bool,
                 select_even_if_hidden: bool = False,
                 force_refresh: bool = False) -> None
```

X.select_actor(actor, selected, notify, select_even_if_hidden=False, force_refresh=False) -> None
Select specified actor.

Args:
    actor (Actor): The Actor to be selected.
    selected (bool): Select or deSelect.
    notify (bool): Notify or not.
    select_even_if_hidden (bool): If True, actor will be selected even it's hidden
    force_refresh (bool): Force Refresh or not

<a id="unreal.PythonBPLib.save_thumbnail"></a>

#### save\_thumbnail

```python
@classmethod
def save_thumbnail(cls, object_path: str, output_path: str) -> None
```

X.save_thumbnail(object_path, output_path) -> None
Save the Thumbnail of assets to disc.

Args:
    object_path (str): The specified path of asset
    output_path (str): Thumbnail output path

<a id="unreal.PythonBPLib.save_file_dialog"></a>

#### save\_file\_dialog

```python
@classmethod
def save_file_dialog(cls, dialog_title: str, default_path: str,
                     default_file: str, file_types: str) -> Array[str]
```

X.save_file_dialog(dialog_title, default_path, default_file, file_types) -> Array[str]
Open a save file dialog.
DefaultFile: Default file name of dialog
FileTypes: File types filter
OutFilenames: The picked files path

Args:
    dialog_title (str): Text of dialog title
    default_path (str): Default path of dialog
    default_file (str): 
    file_types (str): 

Returns:
    Array[str]: 

    out_filenames (Array[str]):

<a id="unreal.PythonBPLib.sample_heights"></a>

#### sample\_heights

```python
@classmethod
def sample_heights(cls, context_obj: Object, center: Vector, width: float,
                   height: float, grid_size: float, trace_depth: float,
                   profile_name: Name, draw_debug_type: DrawDebugTrace,
                   draw_time: float,
                   default_height: float) -> Tuple[int, int, Array[Vector]]
```

X.sample_heights(context_obj, center, width, height, grid_size, trace_depth, profile_name, draw_debug_type, draw_time, default_height) -> (out_x_count=int32, out_y_count=int32, out_hit_locs=Array[Vector])
Trace rays against the world using a specific profile in a gird and return the first blocking hits,

Args:
    context_obj (Object): World Content Object
    center (Vector): Center of the ray trace gird
    width (float): Width of the grid
    height (float): The height of ray trace start point
    grid_size (float): The ray trace interval size
    trace_depth (float): Distance from trace start point to the end point
    profile_name (Name): The 'profile' used to determine which components to hit
    draw_debug_type (DrawDebugTrace): Draw Debug Type: unreal.DrawDebugTrace.FOR_DURATION, FOR_ONE_FRAME, NONE, PERSISTENT
    draw_time (float): Debug line display duration
    default_height (float): The 'default height' when trace has no result

Returns:
    tuple: 

    out_x_count (int32): The count of trace point in axis-x

    out_y_count (int32): The count of trace point in axis-y

    out_hit_locs (Array[Vector]): The locations of hit result.

<a id="unreal.PythonBPLib.request_viewport_focus_on_selection"></a>

#### request\_viewport\_focus\_on\_selection

```python
@classmethod
def request_viewport_focus_on_selection(cls,
                                        context_obj: Object = None) -> None
```

X.request_viewport_focus_on_selection(context_obj=None) -> None
Move the editor camera in front of selection.

Args:
    context_obj (Object): Context Object for get the world.

<a id="unreal.PythonBPLib.rename_folder_in_world"></a>

#### rename\_folder\_in\_world

```python
@classmethod
def rename_folder_in_world(cls, world: World, old_path: Name,
                           new_path: Name) -> bool
```

X.rename_folder_in_world(world, old_path, new_path) -> bool
Rename the specified path to a new name.

Args:
    world (World): World Context
    old_path (Name): Old Folder Path
    new_path (Name): New Folder Path

Returns:
    bool:

<a id="unreal.PythonBPLib.project_world_to_view"></a>

#### project\_world\_to\_view

```python
@classmethod
def project_world_to_view(cls, world_position: Vector,
                          view_projection_matrix: Matrix) -> Optional[Vector]
```

X.project_world_to_view(world_position, view_projection_matrix) -> Vector or None
Project world position to view position.
note: added in v1.2.0

Args:
    world_position (Vector): The world position.
    view_projection_matrix (Matrix): The ViewProjection Matrix.

Returns:
    Vector or None: Pos in view space or not.

    out_view_pos (Vector): The view position.

<a id="unreal.PythonBPLib.pilot_level_actor"></a>

#### pilot\_level\_actor

```python
@classmethod
def pilot_level_actor(cls, actor_to_pilot: Actor) -> None
```

X.pilot_level_actor(actor_to_pilot) -> None
Moves the viewport camera according to the actors location and rotation

Args:
    actor_to_pilot (Actor): The actor to pilot

<a id="unreal.PythonBPLib.open_pick_path_dialog"></a>

#### open\_pick\_path\_dialog

```python
@classmethod
def open_pick_path_dialog(cls,
                          dialog_title: str = "Pick Path",
                          default_path: str = "/Game/") -> str
```

X.open_pick_path_dialog(dialog_title="Pick Path", default_path="/Game/") -> str
Open A 'UE style' Pick Path Dialog
note: The DefaultPaht should starts with '/Game', and ends with '/' if pick a folder in 'Content'; 'Engine Content/some_folder' for folder in 'Engine Content'

Args:
    dialog_title (str): The Title for Dialog
    default_path (str): Default Folder, should ends with '/'.

Returns:
    str:

<a id="unreal.PythonBPLib.open_new_asset_path_dialog"></a>

#### open\_new\_asset\_path\_dialog

```python
@classmethod
def open_new_asset_path_dialog(cls,
                               dialog_title: str = "Pick Asset Path",
                               default_path: str = "",
                               allow_read_only_folders: bool = True) -> str
```

X.open_new_asset_path_dialog(dialog_title="Pick Asset Path", default_path="", allow_read_only_folders=True) -> str
Open A 'UE style' Pick Asset Path Dialog
note: The DefaultPaht should starts with '/Game'

Args:
    dialog_title (str): The Title for Dialog
    default_path (str): Default path and name for new asset path.
    allow_read_only_folders (bool): 

Returns:
    str:

<a id="unreal.PythonBPLib.open_file_dialog"></a>

#### open\_file\_dialog

```python
@classmethod
def open_file_dialog(cls, dialog_title: str, default_path: str,
                     default_file: str, file_types: str) -> Array[str]
```

X.open_file_dialog(dialog_title, default_path, default_file, file_types) -> Array[str]
Open a files picker dialog.
DefaultFile: Default file name of dialog
FileTypes: File types filter. For example: "Saved JSON (*.json)|*.json"
OutFilenames: The picked files paths

Args:
    dialog_title (str): Text of dialog title
    default_path (str): Default path of dialog
    default_file (str): 
    file_types (str): 

Returns:
    Array[str]: 

    out_filenames (Array[str]):

<a id="unreal.PythonBPLib.open_directory_dialog"></a>

#### open\_directory\_dialog

```python
@classmethod
def open_directory_dialog(cls, dialog_title: str,
                          default_path: str) -> Optional[str]
```

X.open_directory_dialog(dialog_title, default_path) -> str or None
Open a directory picker dialog.
OutFolderName: The picked folder path

Args:
    dialog_title (str): Text of dialog title
    default_path (str): Default path of dialog

Returns:
    str or None: 

    out_folder_name (str):

<a id="unreal.PythonBPLib.notification"></a>

#### notification

```python
@classmethod
def notification(cls,
                 message: str,
                 info_level: int = 0,
                 expire_duration: float = 5.000000,
                 width_override: float = -1.000000,
                 log_to_console: bool = True,
                 hyperlink_text: str = "",
                 on_hyperlink_click_command: str = "") -> None
```

X.notification(message, info_level=0, expire_duration=5.000000, width_override=-1.000000, log_to_console=True, hyperlink_text="", on_hyperlink_click_command="") -> None
log: 0, warning: 1, Error 2 ||-1

Args:
    message (str): 
    info_level (int32): 
    expire_duration (float): 
    width_override (float): 
    log_to_console (bool): 
    hyperlink_text (str): 
    on_hyperlink_click_command (str):

<a id="unreal.PythonBPLib.multi_line_trace_at_once_by_profile"></a>

#### multi\_line\_trace\_at\_once\_by\_profile

```python
@classmethod
def multi_line_trace_at_once_by_profile(
        cls, context_obj: Object, start_locs: Array[Vector],
        end_locs: Array[Vector], profile_name: Name,
        draw_debug_type: DrawDebugTrace,
        draw_time: float) -> Tuple[Array[bool], Array[Vector]]
```

X.multi_line_trace_at_once_by_profile(context_obj, start_locs, end_locs, profile_name, draw_debug_type, draw_time) -> (out_is_hit=Array[bool], out_hit_locs=Array[Vector])
Trace Multi rays against the world using a specific profile in a gird and return the first blocking hits,

Args:
    context_obj (Object): World Content Object
    start_locs (Array[Vector]): Center of the ray trace gird
    end_locs (Array[Vector]): Width of the grid
    profile_name (Name): The 'profile' used to determine which components to hit
    draw_debug_type (DrawDebugTrace): Draw Debug Type: unreal.DrawDebugTrace.FOR_DURATION, FOR_ONE_FRAME, NONE, PERSISTENT
    draw_time (float): Debug line display duration

Returns:
    tuple: 

    out_is_hit (Array[bool]): 

    out_hit_locs (Array[Vector]): The locations of hit result.

<a id="unreal.PythonBPLib.message_dialog"></a>

#### message\_dialog

```python
@classmethod
def message_dialog(cls, message: str, dialog_title: str) -> None
```

X.message_dialog(message, dialog_title) -> None
Open a modal message box dialog
para: DialogTitle             Text of title in dialog

Args:
    message (str): Text of message to show
    dialog_title (str):

<a id="unreal.PythonBPLib.list_assets_by_class"></a>

#### list\_assets\_by\_class

```python
@classmethod
def list_assets_by_class(cls, paths_folders: Array[str],
                         class_names: Array[Name]) -> Array[Name]
```

X.list_assets_by_class(paths_folders, class_names) -> Array[Name]
Get asset paths（assetData.ObjectPath）for the specified folders and types.

Args:
    paths_folders (Array[str]): Array of target folders.
    class_names (Array[Name]): Specified class types.

Returns:
    Array[Name]: 

    out_object_path (Array[Name]): Result of asset paths.

<a id="unreal.PythonBPLib.guid_from_string"></a>

#### guid\_from\_string

```python
@classmethod
def guid_from_string(cls, guid_str: str) -> Guid
```

X.guid_from_string(guid_str) -> Guid
Generate a Guid instance from Guid value string. The new Guid's value will to the input guid string.
note: added in v1.0.4

Args:
    guid_str (str): string of guid value, the length should equal 32.

Returns:
    Guid: Guid

<a id="unreal.PythonBPLib.get_viewport_pixels_as_texture"></a>

#### get\_viewport\_pixels\_as\_texture

```python
@classmethod
def get_viewport_pixels_as_texture(cls) -> Texture2D
```

X.get_viewport_pixels_as_texture() -> Texture2D
Get the content of first active viewport as Texture2D
note: added in v1.2.0
note: need UE5.0+

Returns:
    Texture2D: Texture2D of viewport's content

<a id="unreal.PythonBPLib.get_viewport_pixels_as_data"></a>

#### get\_viewport\_pixels\_as\_data

```python
@classmethod
def get_viewport_pixels_as_data(cls) -> Tuple[Array[int], IntPoint]
```

X.get_viewport_pixels_as_data() -> (Array[uint8], out_size_xy=IntPoint)
Get the raw pixels from first active viewport as RawData
note: added in v1.2.0

Returns:
    IntPoint: RawData(uint8) Array, and the size of image(FIntPoint)

    out_size_xy (IntPoint):

<a id="unreal.PythonBPLib.get_viewport_pixels"></a>

#### get\_viewport\_pixels

```python
@classmethod
def get_viewport_pixels(cls) -> Tuple[Array[Color], IntPoint]
```

X.get_viewport_pixels() -> (Array[Color], out_size_xy=IntPoint)
Get the raw pixels from first active viewport
note: added in v1.0.4

Returns:
    IntPoint: Pixel Color Array, and the size of image in FIntPoint

    out_size_xy (IntPoint):

<a id="unreal.PythonBPLib.get_viewport_linear_color_pixels"></a>

#### get\_viewport\_linear\_color\_pixels

```python
@classmethod
def get_viewport_linear_color_pixels(cls,
                                     remove_alpha: bool = True
                                     ) -> Tuple[Array[LinearColor], IntPoint]
```

X.get_viewport_linear_color_pixels(remove_alpha=True) -> (Array[LinearColor], out_size_xy=IntPoint)
Get the raw linear color pixels from first active viewport
note: added in v1.0.11

Args:
    remove_alpha (bool): 

Returns:
    IntPoint: Pixel Color Array, and the size of image

    out_size_xy (IntPoint):

<a id="unreal.PythonBPLib.get_vector_property"></a>

#### get\_vector\_property

```python
@classmethod
def get_vector_property(cls, object: Object, property_name: str) -> Vector
```

X.get_vector_property(object, property_name) -> Vector
Get the value of a named Vector property on the given object. Only for the property that cannot be get with 'GetEditorProperty'
note: added in v1.0.9

Args:
    object (Object): The object you want to retrieve a property value from.
    property_name (str): The name of the object's int property.

Returns:
    Vector: The Vector value of property.

<a id="unreal.PythonBPLib.get_unreal_version"></a>

#### get\_unreal\_version

```python
@classmethod
def get_unreal_version(cls) -> Map[str, int]
```

X.get_unreal_version() -> Map[str, int32]
Get the Version of Unreal Engine in a map(dict). The keys: ["Major", "Minor", "Patch"]
note: added in v1.0.4

Returns:
    Map[str, int32]: The versions of current engine.

<a id="unreal.PythonBPLib.get_unique_id"></a>

#### get\_unique\_id

```python
@classmethod
def get_unique_id(cls, object: Object) -> int
```

X.get_unique_id(object) -> int64
Get the UniqueID of the object, which is the InternalIndex in UObjectBase.
note: added in v1.2.3

Args:
    object (Object): The object to get UniqueID.

Returns:
    int64: The UniqueID of the object in int64.

<a id="unreal.PythonBPLib.get_ta_python_version"></a>

#### get\_ta\_python\_version

```python
@classmethod
def get_ta_python_version(cls) -> Map[str, int]
```

X.get_ta_python_version() -> Map[str, int32]
Get the Version of TAPython in a map(dict). The keys: ["Major", "Minor", "Patch"]
note: added in v1.0.9

Returns:
    Map[str, int32]: The versions of current engine.

<a id="unreal.PythonBPLib.get_string_property"></a>

#### get\_string\_property

```python
@classmethod
def get_string_property(cls, object: Object, property_name: str) -> str
```

X.get_string_property(object, property_name) -> str
Get the value of a named FString property on the given object. Only for the property that cannot be get with 'GetEditorProperty'

Args:
    object (Object): The object you want to retrieve a property value from.
    property_name (str): The name of the object's FString property.

Returns:
    str: The string value of property.

<a id="unreal.PythonBPLib.get_static_mesh_section_info"></a>

#### get\_static\_mesh\_section\_info

```python
@classmethod
def get_static_mesh_section_info(cls, mesh: StaticMesh,
                                 lod_level: int) -> Array[int]
```

X.get_static_mesh_section_info(mesh, lod_level) -> Array[int32]
Get the material indexes of specified LOD in static mesh

Args:
    mesh (StaticMesh): The mesh component
    lod_level (int32): Specified LOD

Returns:
    Array[int32]: 

    out_material_indexs (Array[int32]): Result Material Indexes array

<a id="unreal.PythonBPLib.get_static_mesh_data_key"></a>

#### get\_static\_mesh\_data\_key

```python
@classmethod
def get_static_mesh_data_key(cls, mesh: StaticMesh) -> Optional[str]
```

X.get_static_mesh_data_key(mesh) -> str or None
Get the static mesh Data key(guid in ddc)

Args:
    mesh (StaticMesh): The mesh for query.

Returns:
    str or None: 

    out_data_key (str): The generated guid return Succeed or not

<a id="unreal.PythonBPLib.get_soft_object_path_sub_path"></a>

#### get\_soft\_object\_path\_sub\_path

```python
@classmethod
def get_soft_object_path_sub_path(cls,
                                  soft_object_path: SoftObjectPath) -> str
```

X.get_soft_object_path_sub_path(soft_object_path) -> str
GetSoftObjectPathSubPath

Args:
    soft_object_path (SoftObjectPath): 

Returns:
    str:

<a id="unreal.PythonBPLib.get_soft_object_path_asset_path"></a>

#### get\_soft\_object\_path\_asset\_path

```python
@classmethod
def get_soft_object_path_asset_path(cls,
                                    soft_object_path: SoftObjectPath) -> str
```

X.get_soft_object_path_asset_path(soft_object_path) -> str
GetSoftObjectPathAssetPath

Args:
    soft_object_path (SoftObjectPath): 

Returns:
    str:

<a id="unreal.PythonBPLib.get_selected_folder"></a>

#### get\_selected\_folder

```python
@classmethod
def get_selected_folder(cls) -> Array[str]
```

X.get_selected_folder() -> Array[str]
Get the selected folder's paths in content browser.

Returns:
    Array[str]: The paths of current selected folders.

<a id="unreal.PythonBPLib.get_selected_components"></a>

#### get\_selected\_components

```python
@classmethod
def get_selected_components(cls) -> Array[ActorComponent]
```

X.get_selected_components() -> Array[ActorComponent]
Get selected components in World Outliner.

Returns:
    Array[ActorComponent]: The selected actor components.

<a id="unreal.PythonBPLib.get_selected_assets_paths"></a>

#### get\_selected\_assets\_paths

```python
@classmethod
def get_selected_assets_paths(cls) -> Array[str]
```

X.get_selected_assets_paths() -> Array[str]
Get the selected assets paths in content browser

Returns:
    Array[str]: The paths of selected assets.

<a id="unreal.PythonBPLib.get_resource_size"></a>

#### get\_resource\_size

```python
@classmethod
def get_resource_size(cls, object: Object, exclusive: bool) -> int
```

X.get_resource_size(object, exclusive) -> int32
Get the size of the object/resource for use in memory tools
This is the simple version which just returns the total number of bytes used by this object.
note: Exclusive: Only include memory used by non-UObject resources that are directly owned by this UObject. This is used to show memory actually used at runtime, otherwise include exclusive resources and UObject serialized memory for this and all child UObjects, but not memory for external referenced assets or editor only members. This is used in the editor to estimate maximum required memory. Detail sea EResourceSizeMode

Args:
    object (Object): The object you want to query.
    exclusive (bool): Exclusive or not

Returns:
    int32: The cumulative size of this object in memory

<a id="unreal.PythonBPLib.get_redirectors_destination_object"></a>

#### get\_redirectors\_destination\_object

```python
@classmethod
def get_redirectors_destination_object(cls, redirector_obj: Object) -> Object
```

X.get_redirectors_destination_object(redirector_obj) -> Object
Get the destination object of the Redirector.

Args:
    redirector_obj (Object): the Redirector Object.

Returns:
    Object: a pointer to the Redirector's destination object.

<a id="unreal.PythonBPLib.get_plugin_base_dir"></a>

#### get\_plugin\_base\_dir

```python
@classmethod
def get_plugin_base_dir(cls, plugin_name: str) -> str
```

X.get_plugin_base_dir(plugin_name) -> str
Get the base directory of named plug-in.

Args:
    plugin_name (str): Name of the plug-in

Returns:
    str:

<a id="unreal.PythonBPLib.get_pilot_level_actor"></a>

#### get\_pilot\_level\_actor

```python
@classmethod
def get_pilot_level_actor(cls) -> Actor
```

X.get_pilot_level_actor() -> Actor
Get the Pilot actor of current Active viewport

Returns:
    Actor: The pilot actor

<a id="unreal.PythonBPLib.get_objects_by_class"></a>

#### get\_objects\_by\_class

```python
@classmethod
def get_objects_by_class(cls, world: World,
                         object_class: Class) -> Array[Object]
```

X.get_objects_by_class(world, object_class) -> Array[Object]
Get all specified class's UObjects in the 'world'.

Args:
    world (World): The world owned the actors.
    object_class (type(Class)): The specified of classes for query.

Returns:
    Array[Object]: 

    out_objects (Array[Object]): The UObjects of specified class in the world.

<a id="unreal.PythonBPLib.get_object_property"></a>

#### get\_object\_property

```python
@classmethod
def get_object_property(cls, object: Object, property_name: str) -> Object
```

X.get_object_property(object, property_name) -> Object
Get the value of a named UObject property on the given object. Only for the property that cannot be get with 'GetEditorProperty'

Args:
    object (Object): The object you want to retrieve a property value from.
    property_name (str): The name of the object's UObject property.

Returns:
    Object: The UObject value of property.

<a id="unreal.PythonBPLib.get_object_flags"></a>

#### get\_object\_flags

```python
@classmethod
def get_object_flags(cls, object: Object) -> int
```

X.get_object_flags(object) -> int32
Get actors that in specified folder, in World Outliner.
note: added in v1.0.4. The Result can be better displayed with the Utilities.Utils.EObjectFlags(IntFlag)

Args:
    object (Object): The object you want to get the EObjectFlags.

Returns:
    int32: The flag values in int32

<a id="unreal.PythonBPLib.get_module_names"></a>

#### get\_module\_names

```python
@classmethod
def get_module_names(cls,
                     game_module_only: bool = False,
                     log_to_console: bool = False) -> Map[Name, str]
```

X.get_module_names(game_module_only=False, log_to_console=False) -> Map[Name, str]
Get the module names and their corresponding dll paths.
note: added in v1.2.4

Args:
    game_module_only (bool): Only get the game module or not.
    log_to_console (bool): Log the result to console or not.

Returns:
    Map[Name, str]: The module names and their corresponding dll paths in a map.

<a id="unreal.PythonBPLib.get_modifier_keys_state"></a>

#### get\_modifier\_keys\_state

```python
@classmethod
def get_modifier_keys_state(cls) -> Map[str, bool]
```

X.get_modifier_keys_state() -> Map[str, bool]
Get the modifier keys state in TMap. Control/Alt/Shift/Command/CapsLock etc.
note: added in v1.0.10

Returns:
    Map[str, bool]: Modifier keys state in TMap<FString, bool>. Keys: "AnyModifiersDown", "IsShiftDown", "IsLeftShiftDown", "IsRightShiftDown", "IsControlDown", "IsLeftControlDown", "IsRightControlDown", "IsAltDown", "IsLeftAltDown", "IsRightAltDown", "IsAltDown", "IsLeftControlDown", "IsRightControlDown", "IsCommandDown", "IsLeftCommandDown", "AreCapsLocked", "IsRightCommandDown"

<a id="unreal.PythonBPLib.get_level_viewport_size"></a>

#### get\_level\_viewport\_size

```python
@classmethod
def get_level_viewport_size(cls) -> IntPoint
```

X.get_level_viewport_size() -> IntPoint
Get the size of level viewport
note: added in v1.2.0

Returns:
    IntPoint: The size(FIntPoint) of viewport

<a id="unreal.PythonBPLib.get_level_viewport_camera_speed"></a>

#### get\_level\_viewport\_camera\_speed

```python
@classmethod
def get_level_viewport_camera_speed(cls) -> int
```

X.get_level_viewport_camera_speed() -> int32
Get the speed setting(1-8) of level viewport camera
note: added in v1.0.9

Returns:
    int32: the speed setting of viewport's camera

<a id="unreal.PythonBPLib.get_level_viewport_camera_info"></a>

#### get\_level\_viewport\_camera\_info

```python
@classmethod
def get_level_viewport_camera_info(cls) -> Optional[Tuple[Vector, Rotator]]
```

X.get_level_viewport_camera_info() -> (camera_location=Vector, camera_rotation=Rotator) or None
Get the location and rotation of level viewport camera

Returns:
    tuple or None: 

    camera_location (Vector): Location of level viewport camera

    camera_rotation (Rotator): Rotation of level viewport camera

<a id="unreal.PythonBPLib.get_level_viewport_camera_fov"></a>

#### get\_level\_viewport\_camera\_fov

```python
@classmethod
def get_level_viewport_camera_fov(cls) -> float
```

X.get_level_viewport_camera_fov() -> float
Get the fov of level viewport camera

Returns:
    float: The fov of camera in degree.

<a id="unreal.PythonBPLib.get_level_viewport_camera_aspect"></a>

#### get\_level\_viewport\_camera\_aspect

```python
@classmethod
def get_level_viewport_camera_aspect(cls) -> float
```

X.get_level_viewport_camera_aspect() -> float
Get the aspect of level viewport camera
note: added in v1.2.0

Returns:
    float: The aspect of camera.

<a id="unreal.PythonBPLib.get_latest_context_object"></a>

#### get\_latest\_context\_object

```python
@classmethod
def get_latest_context_object(cls) -> ToolMenuContext
```

X.get_latest_context_object() -> ToolMenuContext
UFUNCTION(BlueprintCallable, meta = (Keywords = "Python Editor"), Category = "PythonEditor")
static void GetContext(FName NameIn, UClass* InClass);

Returns:
    ToolMenuContext:

<a id="unreal.PythonBPLib.get_int_property"></a>

#### get\_int\_property

```python
@classmethod
def get_int_property(cls, object: Object, property_name: str) -> int
```

X.get_int_property(object, property_name) -> int32
Get the value of a named int property on the given object. Only for the property that cannot be get with 'GetEditorProperty'

Args:
    object (Object): The object you want to retrieve a property value from.
    property_name (str): The name of the object's int property.

Returns:
    int32: The int value of property.

<a id="unreal.PythonBPLib.get_hit_result_location"></a>

#### get\_hit\_result\_location

```python
@classmethod
def get_hit_result_location(cls, hit_result: HitResult) -> Vector
```

X.get_hit_result_location(hit_result) -> Vector
临时，之后用反射做

- LEGACY, HIDE IN DOCUMENT -

Args:
    hit_result (HitResult): 

Returns:
    Vector:

<a id="unreal.PythonBPLib.get_folder_picker_path"></a>

#### get\_folder\_picker\_path

```python
@classmethod
def get_folder_picker_path(cls) -> str
```

X.get_folder_picker_path() -> str
Open A 'UE style' Pick Path Dialog

Returns:
    str:

<a id="unreal.PythonBPLib.get_float_property"></a>

#### get\_float\_property

```python
@classmethod
def get_float_property(cls, object: Object, property_name: str) -> float
```

X.get_float_property(object, property_name) -> float
Get the value of a named float property on the given object.  Only for the property that cannot be get with 'GetEditorProperty'

Args:
    object (Object): The object you want to retrieve a property value from.
    property_name (str): The name of the object's float property.

Returns:
    float: The float value of property.

<a id="unreal.PythonBPLib.get_editor_mode_names"></a>

#### get\_editor\_mode\_names

```python
@classmethod
def get_editor_mode_names(cls, visible_only: bool = True) -> Array[str]
```

X.get_editor_mode_names(visible_only=True) -> Array[str]
Get the names of editor modes.
note: added in v1.2.4

Args:
    visible_only (bool): Only get the visible editor mode or not.

Returns:
    Array[str]: The names of editor modes in a array.

<a id="unreal.PythonBPLib.get_editor_mode_ids"></a>

#### get\_editor\_mode\_ids

```python
@classmethod
def get_editor_mode_ids(cls, visible_only: bool = True) -> Array[Name]
```

X.get_editor_mode_ids(visible_only=True) -> Array[Name]
Get the name of editor mode IDs.
note: added in v1.2.4

Args:
    visible_only (bool): Only get the visible editor mode or not.

Returns:
    Array[Name]: The name of editor mode IDs in a array.

<a id="unreal.PythonBPLib.get_clipboard_content"></a>

#### get\_clipboard\_content

```python
@classmethod
def get_clipboard_content(cls) -> str
```

X.get_clipboard_content() -> str
Get the string content From clipboard

Returns:
    str: 

    dest (str):

<a id="unreal.PythonBPLib.get_class_path_name"></a>

#### get\_class\_path\_name

```python
@classmethod
def get_class_path_name(cls, asset: Object) -> str
```

X.get_class_path_name(asset) -> str
Get the ClassPathName of the asset.
note: added in v1.0.11, need UE5.0+

Args:
    asset (Object): The asset to get ClassPathName.

Returns:
    str: The ClassPathName of the asset.

<a id="unreal.PythonBPLib.get_chameleon_data"></a>

#### get\_chameleon\_data

```python
@classmethod
def get_chameleon_data(
        cls,
        tools_json_path: str,
        detail_customization_unique_id: int = -1) -> ChameleonData
```

X.get_chameleon_data(tools_json_path, detail_customization_unique_id=-1) -> ChameleonData
Get the chameleonData by JSON file path

Args:
    tools_json_path (str): Path of the JSON file path, which was binded when create the widget
    detail_customization_unique_id (int32): 

Returns:
    ChameleonData:

<a id="unreal.PythonBPLib.get_bp_class_hierarchy_package"></a>

#### get\_bp\_class\_hierarchy\_package

```python
@classmethod
def get_bp_class_hierarchy_package(cls,
                                   class_: Class) -> Optional[Array[Package]]
```

X.get_bp_class_hierarchy_package(class_) -> Array[Package] or None
Get the classes hierarchy of the blueprint instance class.

Args:
    class_ (type(Class)): The blueprint instance class you want to query.

Returns:
    Array[Package] or None: Whether Retrieve the BP hierarchy succeeded.

    out_bpg_classes_package (Array[Package]): Array of classes hierarchy. 0th = this

<a id="unreal.PythonBPLib.get_bool_property"></a>

#### get\_bool\_property

```python
@classmethod
def get_bool_property(cls, object: Object, property_name: str) -> bool
```

X.get_bool_property(object, property_name) -> bool
Get the bool value of a named bool property on the given object.  Only for the property that cannot be get with 'GetEditorProperty'

Args:
    object (Object): The object you want to retrieve a property value from.
    property_name (str): The name of the object's bool property.

Returns:
    bool: The bool value of property.

<a id="unreal.PythonBPLib.get_blueprint_generated_class"></a>

#### get\_blueprint\_generated\_class

```python
@classmethod
def get_blueprint_generated_class(cls, blueprint: Blueprint) -> Object
```

X.get_blueprint_generated_class(blueprint) -> Object
Get the generated class of the Blueprint
deprecated: Use blueprint.generated_class() instead

Args:
    blueprint (Blueprint): The blueprint instance you want to query. return a Pointer to the 'most recent' fully generated class

Returns:
    Object:

<a id="unreal.PythonBPLib.get_assets_data_by_package_names"></a>

#### get\_assets\_data\_by\_package\_names

```python
@classmethod
def get_assets_data_by_package_names(
        cls, package_names: Array[str]) -> Array[AssetData]
```

X.get_assets_data_by_package_names(package_names) -> Array[AssetData]
Gets asset data for the assets in the packages
note: This is 'batch' version of  unreal.AssetRegistry.get_assets_by_package_name(...)

Args:
    package_names (Array[str]): the package names for the requested assets (eg, /Game/MyFolder/MyAsset)

Returns:
    Array[AssetData]: 

    out_asset_datas (Array[AssetData]):

<a id="unreal.PythonBPLib.get_assets_data_by_class"></a>

#### get\_assets\_data\_by\_class

```python
@classmethod
def get_assets_data_by_class(cls, paths_folders: Array[str],
                             class_names: Array[Name]) -> Array[AssetData]
```

X.get_assets_data_by_class(paths_folders, class_names) -> Array[AssetData]
Get AssetDatas for the assets in specified folders and types.

Args:
    paths_folders (Array[str]): Array of target folders.
    class_names (Array[Name]): Specified class types. For example, ["World", "MaterialInstance", "StaticMesh", and so on..]

Returns:
    Array[AssetData]: 

    out_asset_datas (Array[AssetData]): Result of AssetDatas.

<a id="unreal.PythonBPLib.get_anim_blueprint_generated_class"></a>

#### get\_anim\_blueprint\_generated\_class

```python
@classmethod
def get_anim_blueprint_generated_class(cls,
                                       anim_blueprint: AnimBlueprint) -> Class
```

X.get_anim_blueprint_generated_class(anim_blueprint) -> type(Class)
Get the generated class of the animBlueprint

Args:
    anim_blueprint (AnimBlueprint): Skeletal mesh component return a Pointer to the 'most recent' fully generated class

Returns:
    type(Class):

<a id="unreal.PythonBPLib.get_all_worlds"></a>

#### get\_all\_worlds

```python
@classmethod
def get_all_worlds(cls) -> Array[World]
```

X.get_all_worlds() -> Array[World]
Get all 'worlds' in editor。

Returns:
    Array[World]: 

    out_worlds (Array[World]): The worlds in the editor.

<a id="unreal.PythonBPLib.get_all_refs"></a>

#### get\_all\_refs

```python
@classmethod
def get_all_refs(cls,
                 package_path: Name,
                 recursive: bool,
                 dependency_type: int = 3) -> Tuple[Array[str], Array[int]]
```

X.get_all_refs(package_path, recursive, dependency_type=3) -> (out_refs_wf=Array[str], parent_index=Array[int32])
Get all referencers of specified package path

Args:
    package_path (Name): the name of the package for which to gather references.
    recursive (bool): recursive or not
    dependency_type (int32): which kinds of dependency to include in the output list. For example: 3: package (Soft|Hard), 18: manage(SoftManager|HardManage) ,25: all

Returns:
    tuple: 

    out_refs_wf (Array[str]): a list of packages that reference the package whose path is PackageName, wide first

    parent_index (Array[int32]): a list of index of OutRefsWF element's parent

<a id="unreal.PythonBPLib.get_all_property_names"></a>

#### get\_all\_property\_names

```python
@classmethod
def get_all_property_names(cls, class_: Class, flag: int = -1) -> Array[str]
```

X.get_all_property_names(class_, flag=-1) -> Array[str]
Get All Property Names

Args:
    class_ (type(Class)): 
    flag (int32): 

Returns:
    Array[str]:

<a id="unreal.PythonBPLib.get_all_objects"></a>

#### get\_all\_objects

```python
@classmethod
def get_all_objects(cls, world: World, include_dead: bool) -> Array[Object]
```

X.get_all_objects(world, include_dead) -> Array[Object]
Get all UObject in the 'world'.

Args:
    world (World): The world owned the UObjects.
    include_dead (bool): Whether include the 'dead' (PendingKill | Unreachable) UObject or not.

Returns:
    Array[Object]: 

    out_objects (Array[Object]): The All UObject in the world.

<a id="unreal.PythonBPLib.get_all_deps"></a>

#### get\_all\_deps

```python
@classmethod
def get_all_deps(cls,
                 package_path: Name,
                 recursive: bool,
                 dependency_type: int = 3) -> Tuple[Array[str], Array[int]]
```

X.get_all_deps(package_path, recursive, dependency_type=3) -> (out_dps_wf=Array[str], parent_indexs=Array[int32])
Get all dependencies of specified package path.

Args:
    package_path (Name): the name of the package for which to gather dependencies.
    recursive (bool): recursive or not.
    dependency_type (int32): Which kinds of dependency to include in the output list. For example: 3: package (Soft|Hard), 18: manage(SoftManager|HardManage), 25: all

Returns:
    tuple: 

    out_dps_wf (Array[str]): a list of packages that are referenced by the package whose path is PackageName, wide first.

    parent_indexs (Array[int32]):

<a id="unreal.PythonBPLib.get_all_chameleon_data_paths"></a>

#### get\_all\_chameleon\_data\_paths

```python
@classmethod
def get_all_chameleon_data_paths(cls) -> Array[str]
```

X.get_all_chameleon_data_paths() -> Array[str]
Get the chameleonData by JSON file path

Returns:
    Array[str]: All path of current Chameleon Tools's JSON file paths.

<a id="unreal.PythonBPLib.get_actors_from_folder"></a>

#### get\_actors\_from\_folder

```python
@classmethod
def get_actors_from_folder(cls, world: World, path: str) -> Array[Actor]
```

X.get_actors_from_folder(world, path) -> Array[Actor]
Get actors that in specified folder, in World Outliner.
note: added in v1.0.4

Args:
    world (World): World Context
    path (str): The folder path name in World Outliner.

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]):

<a id="unreal.PythonBPLib.gc"></a>

#### gc

```python
@classmethod
def gc(cls, keep_flags: int, perform_full_purge: bool = True) -> None
```

X.gc(keep_flags, perform_full_purge=True) -> None
Deletes all unreferenced objects, keeping objects that have any of the passed in KeepFlags set. Will wait for other threads to unlock GC.

Args:
    keep_flags (int32): objects with those flags will be kept regardless of being referenced or not
    perform_full_purge (bool): if true, perform a full purge after the mark pass

<a id="unreal.PythonBPLib.frustum_trace"></a>

#### frustum\_trace

```python
@classmethod
def frustum_trace(cls, world: World, view_info: MinimalViewInfo, x_steps: int,
                  y_steps: int, include_border: bool, trace_distance: float,
                  profile_name: Name,
                  debug_draw: bool) -> Array[TAPythonPrimitiveHitResult]
```

X.frustum_trace(world, view_info, x_steps, y_steps, include_border, trace_distance, profile_name, debug_draw) -> Array[TAPythonPrimitiveHitResult]
Trace rays against the world using a specific profile in a gird in Frustum and return the hits.
note: added in v1.2.0
note: need UE5.0+

Args:
    world (World): The world to trace in.
    view_info (MinimalViewInfo): The ViewInfo of the camera.
    x_steps (int32): The count of trace point in frustum axis-x
    y_steps (int32): The count of trace point in frustum axis-y
    include_border (bool): Include the border of frustum or not.
    trace_distance (float): Distance from trace start point to the end point
    profile_name (Name): The 'profile' used to determine which components to hit
    debug_draw (bool): Debug draw or not.

Returns:
    Array[TAPythonPrimitiveHitResult]: 

    primitive_hit_results (Array[TAPythonPrimitiveHitResult]):

<a id="unreal.PythonBPLib.fix_up_redirectors_in_folder"></a>

#### fix\_up\_redirectors\_in\_folder

```python
@classmethod
def fix_up_redirectors_in_folder(
        cls,
        folder_paths: Array[str],
        allowed_to_prompt_to_load_assets: bool = True) -> bool
```

X.fix_up_redirectors_in_folder(folder_paths, allowed_to_prompt_to_load_assets=True) -> bool
Fixup all redirector In specified folders
note: Param FolderPaths

Args:
    folder_paths (Array[str]): The folder paths array for fixup redirectors.
    allowed_to_prompt_to_load_assets (bool): 

Returns:
    bool: Whether fixup task succeeded.

<a id="unreal.PythonBPLib.fix_up_redirectors"></a>

#### fix\_up\_redirectors

```python
@classmethod
def fix_up_redirectors(cls, redirector_objs: Array[Object]) -> bool
```

X.fix_up_redirectors(redirector_objs) -> bool
Fix up specified redirectors.

Args:
    redirector_objs (Array[Object]): The redirector objects to be fixed.

Returns:
    bool: Whether fix up task succeeded

<a id="unreal.PythonBPLib.find_actors_by_label_name"></a>

#### find\_actors\_by\_label\_name

```python
@classmethod
def find_actors_by_label_name(cls,
                              name: str,
                              world: World = None,
                              include_dead: bool = True) -> Array[Actor]
```

X.find_actors_by_label_name(name, world=None, include_dead=True) -> Array[Actor]
Get actor by Label name(display Name) in specified World
note: added in v1.0.3

Args:
    name (str): Name(Label Name) of actor
    world (World): World Context
    include_dead (bool): 

Returns:
    Array[Actor]: A pointer to the named actor or NULL if not found.

<a id="unreal.PythonBPLib.find_actor_by_name"></a>

#### find\_actor\_by\_name

```python
@classmethod
def find_actor_by_name(cls,
                       name: str,
                       world: World = None,
                       include_dead: bool = True) -> Actor
```

X.find_actor_by_name(name, world=None, include_dead=True) -> Actor
Get actor by name(ID Name) in specified World

Args:
    name (str): Name(ID Name) of actor
    world (World): World Context
    include_dead (bool): Include dead object or not

Returns:
    Actor: A pointer to the named actor or NULL if not found.

<a id="unreal.PythonBPLib.export_map"></a>

#### export\_map

```python
@classmethod
def export_map(cls, actor: Actor, filename: str,
               export_selected_actors_only: bool) -> None
```

X.export_map(actor, filename, export_selected_actors_only) -> None
Exports the specified actor mesh to .obj file.
note: Useful when export landscape to mesh obj.

Args:
    actor (Actor): The actor to be export.
    filename (str): Filename to export to.
    export_selected_actors_only (bool): If true, export only the selected actors.

<a id="unreal.PythonBPLib.execute_console_command"></a>

#### execute\_console\_command

```python
@classmethod
def execute_console_command(cls, console_command: str) -> None
```

X.execute_console_command(console_command) -> None
Execute Console Command

Args:
    console_command (str): The console command

<a id="unreal.PythonBPLib.exec_python_command"></a>

#### exec\_python\_command

```python
@classmethod
def exec_python_command(cls,
                        python_command: str,
                        force_game_thread: bool = False) -> None
```

X.exec_python_command(python_command, force_game_thread=False) -> None
Execute Python Command if Python is available

Args:
    python_command (str): The python command
    force_game_thread (bool): Force running python command in GameThread. For example modify the UI in a thread.

<a id="unreal.PythonBPLib.enable_world_composition"></a>

#### enable\_world\_composition

```python
@classmethod
def enable_world_composition(cls, world: World, enable: bool) -> bool
```

X.enable_world_composition(world, enable) -> bool
Enable World Composition in current level.

Args:
    world (World): The World context.
    enable (bool): Enable the World Composition option or not.

Returns:
    bool:

<a id="unreal.PythonBPLib.eject_pilot_level_actor"></a>

#### eject\_pilot\_level\_actor

```python
@classmethod
def eject_pilot_level_actor(cls) -> None
```

X.eject_pilot_level_actor() -> None
Eject the viewport camera

<a id="unreal.PythonBPLib.diff_assets"></a>

#### diff\_assets

```python
@classmethod
def diff_assets(cls, asset_a: Object, asset_b: Object) -> None
```

X.diff_assets(asset_a, asset_b) -> None
Compare assets by 3rd compare tools, for instance: p4merge etc..

Args:
    asset_a (Object): 
    asset_b (Object):

<a id="unreal.PythonBPLib.delete_folder"></a>

#### delete\_folder

```python
@classmethod
def delete_folder(cls, world: World, folder_to_delete: Name) -> None
```

X.delete_folder(world, folder_to_delete) -> None
Delete specified folder in World Outliner.

Args:
    world (World): 
    folder_to_delete (Name): The name of folder path which need to be deleted.

<a id="unreal.PythonBPLib.delete_asset"></a>

#### delete\_asset

```python
@classmethod
def delete_asset(cls,
                 asset_path_to_delete: str,
                 show_confirmation: bool = True) -> bool
```

X.delete_asset(asset_path_to_delete, show_confirmation=True) -> bool
Delete the asset in path.
note: This can't undo.

Args:
    asset_path_to_delete (str): The Component type.
    show_confirmation (bool): Show confirmation dialog or not.

Returns:
    bool:

<a id="unreal.PythonBPLib.create_folder_in_outliner"></a>

#### create\_folder\_in\_outliner

```python
@classmethod
def create_folder_in_outliner(cls, world: World,
                              new_folder_name: Name) -> None
```

X.create_folder_in_outliner(world, new_folder_name) -> None
Create new folder in World Outliner.

Args:
    world (World): World Context.
    new_folder_name (Name): The name of new folder.

<a id="unreal.PythonBPLib.confirm_dialog"></a>

#### confirm\_dialog

```python
@classmethod
def confirm_dialog(cls,
                   message: str,
                   dialog_title: str,
                   with_cancel_button: bool = False) -> bool
```

X.confirm_dialog(message, dialog_title, with_cancel_button=False) -> bool
Open a modal message box dialog with Yes/No/Cancel button.

Args:
    message (str): Text of message to show.
    dialog_title (str): Text of title in dialog.
    with_cancel_button (bool): Show cancel button or not.

Returns:
    bool:

<a id="unreal.PythonBPLib.close_editor_for_assets"></a>

#### close\_editor\_for\_assets

```python
@classmethod
def close_editor_for_assets(cls, assets: Array[Object]) -> None
```

X.close_editor_for_assets(assets) -> None
Close all active editors for the supplied asset.
note: Also can use unreal.get_editor_subsystem(unreal.AssetEditorSubsystem).close_all_editors_for_asset(assets) instead

Args:
    assets (Array[Object]): Array of assets that will be closed.

<a id="unreal.PythonBPLib.clear_folder_color"></a>

#### clear\_folder\_color

```python
@classmethod
def clear_folder_color(cls, folder_path: str) -> None
```

X.clear_folder_color(folder_path) -> None
Clear the of specified folder's color in content browser.

Args:
    folder_path (str): The folder path in project. For example: "/Game/StarterContent"

<a id="unreal.PythonBPLib.clear_flag"></a>

#### clear\_flag

```python
@classmethod
def clear_flag(cls, object: Object, object_flags_value: int) -> None
```

X.clear_flag(object, object_flags_value) -> None
Clear EObjectFlags of UObject. Do not use unless you know what you are doing.

Args:
    object (Object): The object you want to set a EObjectFlags value on.
    object_flags_value (int32): ObjectFlagsValue

<a id="unreal.PythonBPLib.change_editor_mode"></a>

#### change\_editor\_mode

```python
@classmethod
def change_editor_mode(cls, editor_mode_name: str = "EM_Default") -> bool
```

X.change_editor_mode(editor_mode_name="EM_Default") -> bool
Change the editor mode to the specified mode.
note: The default editor mode is "EM_Default", which is the default editor mode.
note: added in v1.2.4

Args:
    editor_mode_name (str): The name of the editor mode.

Returns:
    bool: True if the editor mode is changed successfully.

<a id="unreal.PythonBPLib.call_function"></a>

#### call\_function

```python
@classmethod
def call_function(cls, object: Object, functio_name_and_args: str) -> bool
```

X.call_function(object, functio_name_and_args) -> bool
Calling a function by name on given object.
deprecated: Use obj.call_method instead

Args:
    object (Object): The object you want to call the function.
    functio_name_and_args (str): The function name and the args.

Returns:
    bool: Whether the function was called.

<a id="unreal.PythonBPLib.calculate_vp_matrix"></a>

#### calculate\_vp\_matrix

```python
@classmethod
def calculate_vp_matrix(cls,
                        view_location: Vector,
                        view_rotation: Rotator,
                        horz_fov_degrees: float,
                        near_plane: float = 1.000000) -> Matrix
```

X.calculate_vp_matrix(view_location, view_rotation, horz_fov_degrees, near_plane=1.000000) -> Matrix
Calculate the ViewProjection Matrix by ViewLocation, ViewRotation, HorzFOVDegrees and NearPlane.
note: added in v1.2.0

Args:
    view_location (Vector): The ViewLocation.
    view_rotation (Rotator): The ViewRotation.
    horz_fov_degrees (float): The horizontal fov in degree.
    near_plane (float): The near plane.

Returns:
    Matrix: The ViewProjection Matrix.

<a id="unreal.PythonBPLib.calculate_view_matrix"></a>

#### calculate\_view\_matrix

```python
@classmethod
def calculate_view_matrix(cls, view_location: Vector,
                          view_rotation: Rotator) -> Matrix
```

X.calculate_view_matrix(view_location, view_rotation) -> Matrix
Calculate the View Matrix by ViewLocation and ViewRotation.
note: added in v1.2.0

Args:
    view_location (Vector): The ViewLocation.
    view_rotation (Rotator): The ViewRotation.

Returns:
    Matrix: The View Matrix.

<a id="unreal.PythonBPLib.calculate_projection_matrix"></a>

#### calculate\_projection\_matrix

```python
@classmethod
def calculate_projection_matrix(cls,
                                horz_fov_degrees: float,
                                near_plane: float = 1.000000) -> Matrix
```

X.calculate_projection_matrix(horz_fov_degrees, near_plane=1.000000) -> Matrix
Calculate the Projection Matrix by fov and near plane.
note: added in v1.2.0

Args:
    horz_fov_degrees (float): The horizontal fov in degree.
    near_plane (float): The near plane.

Returns:
    Matrix: The Projection Matrix.

<a id="unreal.PythonBPLib.calculate_inv_view_projection_matrix"></a>

#### calculate\_inv\_view\_projection\_matrix

```python
@classmethod
def calculate_inv_view_projection_matrix(cls, view_location: Vector,
                                         view_rotation: Rotator,
                                         horz_fov_degrees: float,
                                         near_plane: float) -> Matrix
```

X.calculate_inv_view_projection_matrix(view_location, view_rotation, horz_fov_degrees, near_plane) -> Matrix
Calculate the inverse ViewProjection Matrix by ViewLocation, ViewRotation, HorzFOVDegrees and NearPlane.
note: added in v1.2.0

Args:
    view_location (Vector): The ViewLocation.
    view_rotation (Rotator): The ViewRotation.
    horz_fov_degrees (float): The horizontal fov in degree.
    near_plane (float): The near plane.

Returns:
    Matrix: The inverse ViewProjection Matrix.

<a id="unreal.PythonBPLib.break_soft_object"></a>

#### break\_soft\_object

```python
@classmethod
def break_soft_object(cls, soft_object_path: SoftObjectPath) -> Array[str]
```

X.break_soft_object(soft_object_path) -> Array[str]
Break the SoftObject content into Array:  [AssetPathString, SubPathString]
note: added in v1.0.4

Args:
    soft_object_path (SoftObjectPath): 

Returns:
    Array[str]: AssetPathString and SubPathString of the SoftObect in a array.

<a id="unreal.PythonBPLib.apply_instance_changes_to_blueprint"></a>

#### apply\_instance\_changes\_to\_blueprint

```python
@classmethod
def apply_instance_changes_to_blueprint(cls, actor: Actor) -> int
```

X.apply_instance_changes_to_blueprint(actor) -> int32
Apply Instance Changes To Blueprint

Args:
    actor (Actor): The target actor

Returns:
    int32: Changed Properties count

<a id="unreal.PythonBPLib.add_flag"></a>

#### add\_flag

```python
@classmethod
def add_flag(cls, object: Object, object_flags_value: int) -> None
```

X.add_flag(object, object_flags_value) -> None
Add EObjectFlags of UObject. Do not use unless you know what you are doing.

Args:
    object (Object): The object you want to set a EObjectFlags value on.
    object_flags_value (int32): ObjectFlagsValue

<a id="unreal.PythonBPLib.add_component"></a>

#### add\_component

```python
@classmethod
def add_component(cls,
                  component_class: Class,
                  actor: Actor,
                  parent_component: SceneComponent,
                  name: Name = "None") -> ActorComponent
```

X.add_component(component_class, actor, parent_component, name="None") -> ActorComponent
Create a specified Component for actor.

Args:
    component_class (type(Class)): The Component type.
    actor (Actor): The actor owner the created component.
    parent_component (SceneComponent): The parent component for created component.The root component will be used when null.
    name (Name): The Name for the created Component

Returns:
    ActorComponent: The created component.

<a id="unreal.PythonControlRigLib"></a>