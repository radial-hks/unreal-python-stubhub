## VictoryBPFunctionLibrary Objects

```python
class VictoryBPFunctionLibrary(BlueprintFunctionLibrary)
```

Victory to You! <3 Rama

**C++ Source:**

- **Plugin**: VictoryBPLibrary
- **Module**: VictoryBPLibrary
- **File**: VictoryBPFunctionLibrary.h

<a id="unreal.VictoryBPFunctionLibrary.world_type_in_pie_world"></a>

#### world\_type\_in\_pie\_world

```python
@classmethod
def world_type_in_pie_world(cls, world_context_object: Object) -> bool
```

X.world_type_in_pie_world(world_context_object) -> bool
Is this game logic running in the PIE world?

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.world_type_in_game_instance_world"></a>

#### world\_type\_in\_game\_instance\_world

```python
@classmethod
def world_type_in_game_instance_world(cls,
                                      world_context_object: Object) -> bool
```

X.world_type_in_game_instance_world(world_context_object) -> bool
Is this game logic running in an actual independent game instance?

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.world_type_in_editor_world"></a>

#### world\_type\_in\_editor\_world

```python
@classmethod
def world_type_in_editor_world(cls, world_context_object: Object) -> bool
```

X.world_type_in_editor_world(world_context_object) -> bool
Is this game logic running in the Editor world?

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.widget_get_parent_of_class"></a>

#### widget\_get\_parent\_of\_class

```python
@classmethod
def widget_get_parent_of_class(cls, child_widget: Widget,
                               widget_class: Class) -> UserWidget
```

X.widget_get_parent_of_class(child_widget, widget_class) -> UserWidget
Recurses up the list of parents until it finds a widget of WidgetClass.

Args:
    child_widget (Widget): 
    widget_class (type(Class)): 

Returns:
    UserWidget: widget that is Parent of ChildWidget that matches WidgetClass.

<a id="unreal.VictoryBPFunctionLibrary.widget_get_children_of_class"></a>

#### widget\_get\_children\_of\_class

```python
@classmethod
def widget_get_children_of_class(cls, parent_widget: Widget,
                                 widget_class: Class,
                                 immediate_only: bool) -> Array[UserWidget]
```

X.widget_get_children_of_class(parent_widget, widget_class, immediate_only) -> Array[UserWidget]
Widget Get Children Of Class

Args:
    parent_widget (Widget): 
    widget_class (type(Class)): 
    immediate_only (bool): 

Returns:
    Array[UserWidget]: 

    child_widgets (Array[UserWidget]):

<a id="unreal.VictoryBPFunctionLibrary.viewport_position_deproject"></a>

#### viewport\_position\_deproject

```python
@classmethod
def viewport_position_deproject(
        cls, world_context_object: Object,
        viewport_position: Vector2D) -> Optional[Tuple[Vector, Vector]]
```

X.viewport_position_deproject(world_context_object, viewport_position) -> (out_world_origin=Vector, out_world_direction=Vector) or None
Transforms the viewport position into a world space origin and direction.

Args:
    world_context_object (Object): World context.
    viewport_position (Vector2D): Local space of viewport from GetViewportPosition() or similar.

Returns:
    tuple or None: false if something went wrong during the deproject process.

    out_world_origin (Vector): Corresponding 3D location in world space.

    out_world_direction (Vector): World space direction vector away from the camera at the given 2d point.

<a id="unreal.VictoryBPFunctionLibrary.viewport_set_mouse_position"></a>

#### viewport\_set\_mouse\_position

```python
@classmethod
def viewport_set_mouse_position(cls, the_pc: PlayerController, pos_x: float,
                                pos_y: float) -> bool
```

X.viewport_set_mouse_position(the_pc, pos_x, pos_y) -> bool
SET the Mouse Position! Returns false if the operation could not occur

Args:
    the_pc (PlayerController): 
    pos_x (float): 
    pos_y (float): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.viewport_get_mouse_position"></a>

#### viewport\_get\_mouse\_position

```python
@classmethod
def viewport_get_mouse_position(
        cls, the_pc: PlayerController) -> Optional[Tuple[float, float]]
```

X.viewport_get_mouse_position(the_pc) -> (pos_x=float, pos_y=float) or None
Get the Cursor Position within the Player's Viewport. This will return a result consistent with SET Mouse Position Returns false if the operation could not occur

Args:
    the_pc (PlayerController): 

Returns:
    tuple or None: 

    pos_x (float): 

    pos_y (float):

<a id="unreal.VictoryBPFunctionLibrary.viewport_get_center_of_viewport"></a>

#### viewport\_get\_center\_of\_viewport

```python
@classmethod
def viewport_get_center_of_viewport(
        cls, the_pc: PlayerController) -> Optional[Tuple[float, float]]
```

X.viewport_get_center_of_viewport(the_pc) -> (pos_x=float, pos_y=float) or None
Get the coordinates of the center of the player's screen / viewport. Returns false if the operation could not occur

Args:
    the_pc (PlayerController): 

Returns:
    tuple or None: 

    pos_x (float): 

    pos_y (float):

<a id="unreal.VictoryBPFunctionLibrary.victory_sort_string_array"></a>

#### victory\_sort\_string\_array

```python
@classmethod
def victory_sort_string_array(
        cls, string_array: Array[str]) -> Tuple[Array[str], Array[str]]
```

X.victory_sort_string_array(string_array) -> (string_array=Array[str], string_array_ref=Array[str])
Sort a string array alphabetically!

Args:
    string_array (Array[str]): 

Returns:
    tuple: 

    string_array (Array[str]): 

    string_array_ref (Array[str]):

<a id="unreal.VictoryBPFunctionLibrary.victory_sort_int_array"></a>

#### victory\_sort\_int\_array

```python
@classmethod
def victory_sort_int_array(
        cls, int_array: Array[int]) -> Tuple[Array[int], Array[int]]
```

X.victory_sort_int_array(int_array) -> (int_array=Array[int32], int_array_ref=Array[int32])
Sort an integer array, smallest value will be at index 0 after sorting. Modifies the input array, no new data created. <3 Rama

Args:
    int_array (Array[int32]): 

Returns:
    tuple: 

    int_array (Array[int32]): 

    int_array_ref (Array[int32]):

<a id="unreal.VictoryBPFunctionLibrary.victory_sort_float_array"></a>

#### victory\_sort\_float\_array

```python
@classmethod
def victory_sort_float_array(
        cls, float_array: Array[float]) -> Tuple[Array[float], Array[float]]
```

X.victory_sort_float_array(float_array) -> (float_array=Array[float], float_array_ref=Array[float])
Sort a float array, smallest value will be at index 0 after sorting. Modifies the input array, no new data created.

Args:
    float_array (Array[float]): 

Returns:
    tuple: 

    float_array (Array[float]): 

    float_array_ref (Array[float]):

<a id="unreal.VictoryBPFunctionLibrary.victory_simulate_mouse_wheel"></a>

#### victory\_simulate\_mouse\_wheel

```python
@classmethod
def victory_simulate_mouse_wheel(cls, delta: float) -> None
```

X.victory_simulate_mouse_wheel(delta) -> None
Victory Simulate Mouse Wheel

Args:
    delta (float):

<a id="unreal.VictoryBPFunctionLibrary.victory_simulate_key_press"></a>

#### victory\_simulate\_key\_press

```python
@classmethod
def victory_simulate_key_press(cls, the_pc: PlayerController, key: Key,
                               event_type: InputEventType) -> None
```

X.victory_simulate_key_press(the_pc, key, event_type) -> None
Victory Simulate Key Press

Args:
    the_pc (PlayerController): 
    key (Key): 
    event_type (InputEventType):

<a id="unreal.VictoryBPFunctionLibrary.victory_set_custom_config_var_vector2d"></a>

#### victory\_set\_custom\_config\_var\_vector2d

```python
@classmethod
def victory_set_custom_config_var_vector2d(cls, section_name: str,
                                           variable_name: str,
                                           value: Vector2D) -> None
```

X.victory_set_custom_config_var_vector2d(section_name, variable_name, value) -> None
Set Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 
    value (Vector2D):

<a id="unreal.VictoryBPFunctionLibrary.victory_set_custom_config_var_vector"></a>

#### victory\_set\_custom\_config\_var\_vector

```python
@classmethod
def victory_set_custom_config_var_vector(cls, section_name: str,
                                         variable_name: str,
                                         value: Vector) -> None
```

X.victory_set_custom_config_var_vector(section_name, variable_name, value) -> None
Set Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 
    value (Vector):

<a id="unreal.VictoryBPFunctionLibrary.victory_set_custom_config_var_string"></a>

#### victory\_set\_custom\_config\_var\_string

```python
@classmethod
def victory_set_custom_config_var_string(cls, section_name: str,
                                         variable_name: str,
                                         value: str) -> None
```

X.victory_set_custom_config_var_string(section_name, variable_name, value) -> None
Set Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 
    value (str):

<a id="unreal.VictoryBPFunctionLibrary.victory_set_custom_config_var_rotator"></a>

#### victory\_set\_custom\_config\_var\_rotator

```python
@classmethod
def victory_set_custom_config_var_rotator(cls, section_name: str,
                                          variable_name: str,
                                          value: Rotator) -> None
```

X.victory_set_custom_config_var_rotator(section_name, variable_name, value) -> None
Set Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 
    value (Rotator):

<a id="unreal.VictoryBPFunctionLibrary.victory_set_custom_config_var_int"></a>

#### victory\_set\_custom\_config\_var\_int

```python
@classmethod
def victory_set_custom_config_var_int(cls, section_name: str,
                                      variable_name: str, value: int) -> None
```

X.victory_set_custom_config_var_int(section_name, variable_name, value) -> None
Set Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 
    value (int32):

<a id="unreal.VictoryBPFunctionLibrary.victory_set_custom_config_var_float"></a>

#### victory\_set\_custom\_config\_var\_float

```python
@classmethod
def victory_set_custom_config_var_float(cls, section_name: str,
                                        variable_name: str,
                                        value: float) -> None
```

X.victory_set_custom_config_var_float(section_name, variable_name, value) -> None
Set Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 
    value (float):

<a id="unreal.VictoryBPFunctionLibrary.victory_set_custom_config_var_color"></a>

#### victory\_set\_custom\_config\_var\_color

```python
@classmethod
def victory_set_custom_config_var_color(cls, section_name: str,
                                        variable_name: str,
                                        value: LinearColor) -> None
```

X.victory_set_custom_config_var_color(section_name, variable_name, value) -> None
Set Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 
    value (LinearColor):

<a id="unreal.VictoryBPFunctionLibrary.victory_set_custom_config_var_bool"></a>

#### victory\_set\_custom\_config\_var\_bool

```python
@classmethod
def victory_set_custom_config_var_bool(cls, section_name: str,
                                       variable_name: str,
                                       value: bool) -> None
```

X.victory_set_custom_config_var_bool(section_name, variable_name, value) -> None
Set Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 
    value (bool):

<a id="unreal.VictoryBPFunctionLibrary.victory_is_application_running"></a>

#### victory\_is\_application\_running

```python
@classmethod
def victory_is_application_running(cls, process_id: int) -> bool
```

X.victory_is_application_running(process_id) -> bool
You can obtain ProcessID from processes you initiate via VictoryCreateProc

Args:
    process_id (int32): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.victory_int_plus_equals"></a>

#### victory\_int\_plus\_equals

```python
@classmethod
def victory_int_plus_equals(cls, int: int, add: int) -> Tuple[int, int]
```

X.victory_int_plus_equals(int, add) -> (int=int32, int_out=int32)
Easily add to an integer! <3 Rama

Args:
    int (int32): 
    add (int32): 

Returns:
    tuple: 

    int (int32): 

    int_out (int32):

<a id="unreal.VictoryBPFunctionLibrary.victory_int_minus_equals"></a>

#### victory\_int\_minus\_equals

```python
@classmethod
def victory_int_minus_equals(cls, int: int, sub: int) -> Tuple[int, int]
```

X.victory_int_minus_equals(int, sub) -> (int=int32, int_out=int32)
Easily subtract from an integer! <3 Rama

Args:
    int (int32): 
    sub (int32): 

Returns:
    tuple: 

    int (int32): 

    int_out (int32):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_custom_config_var_vector2d"></a>

#### victory\_get\_custom\_config\_var\_vector2d

```python
@classmethod
def victory_get_custom_config_var_vector2d(
        cls, section_name: str, variable_name: str) -> Tuple[Vector2D, bool]
```

X.victory_get_custom_config_var_vector2d(section_name, variable_name) -> (Vector2D, is_valid=bool)
Victory Get Custom Config Var Vector 2D

Args:
    section_name (str): 
    variable_name (str): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_custom_config_var_vector"></a>

#### victory\_get\_custom\_config\_var\_vector

```python
@classmethod
def victory_get_custom_config_var_vector(
        cls, section_name: str, variable_name: str) -> Tuple[Vector, bool]
```

X.victory_get_custom_config_var_vector(section_name, variable_name) -> (Vector, is_valid=bool)
Get Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_custom_config_var_string"></a>

#### victory\_get\_custom\_config\_var\_string

```python
@classmethod
def victory_get_custom_config_var_string(
        cls, section_name: str, variable_name: str) -> Tuple[str, bool]
```

X.victory_get_custom_config_var_string(section_name, variable_name) -> (str, is_valid=bool)
Get Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_custom_config_var_rotator"></a>

#### victory\_get\_custom\_config\_var\_rotator

```python
@classmethod
def victory_get_custom_config_var_rotator(
        cls, section_name: str, variable_name: str) -> Tuple[Rotator, bool]
```

X.victory_get_custom_config_var_rotator(section_name, variable_name) -> (Rotator, is_valid=bool)
Get Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_custom_config_var_int"></a>

#### victory\_get\_custom\_config\_var\_int

```python
@classmethod
def victory_get_custom_config_var_int(cls, section_name: str,
                                      variable_name: str) -> Tuple[int, bool]
```

X.victory_get_custom_config_var_int(section_name, variable_name) -> (int32, is_valid=bool)
Get Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_custom_config_var_float"></a>

#### victory\_get\_custom\_config\_var\_float

```python
@classmethod
def victory_get_custom_config_var_float(
        cls, section_name: str, variable_name: str) -> Tuple[float, bool]
```

X.victory_get_custom_config_var_float(section_name, variable_name) -> (float, is_valid=bool)
Get Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_custom_config_var_color"></a>

#### victory\_get\_custom\_config\_var\_color

```python
@classmethod
def victory_get_custom_config_var_color(
        cls, section_name: str,
        variable_name: str) -> Tuple[LinearColor, bool]
```

X.victory_get_custom_config_var_color(section_name, variable_name) -> (LinearColor, is_valid=bool)
Get Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_custom_config_var_bool"></a>

#### victory\_get\_custom\_config\_var\_bool

```python
@classmethod
def victory_get_custom_config_var_bool(cls, section_name: str,
                                       variable_name: str) -> Optional[bool]
```

X.victory_get_custom_config_var_bool(section_name, variable_name) -> bool or None
Get Custom Config Var! These are stored in Saved/Config/Windows/Game.ini

Args:
    section_name (str): 
    variable_name (str): 

Returns:
    bool or None: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_application_name"></a>

#### victory\_get\_application\_name

```python
@classmethod
def victory_get_application_name(cls, process_id: int) -> str
```

X.victory_get_application_name(process_id) -> str
You can obtain ProcessID from processes you initiate via VictoryCreateProc

Args:
    process_id (int32): 

Returns:
    str:

<a id="unreal.VictoryBPFunctionLibrary.victory_float_plus_equals"></a>

#### victory\_float\_plus\_equals

```python
@classmethod
def victory_float_plus_equals(cls, float: float,
                              add: float) -> Tuple[float, float]
```

X.victory_float_plus_equals(float, add) -> (float=float, float_out=float)
Easily add to a float! <3 Rama

Args:
    float (float): 
    add (float): 

Returns:
    tuple: 

    float (float): 

    float_out (float):

<a id="unreal.VictoryBPFunctionLibrary.victory_float_minus_equals"></a>

#### victory\_float\_minus\_equals

```python
@classmethod
def victory_float_minus_equals(cls, float: float,
                               sub: float) -> Tuple[float, float]
```

X.victory_float_minus_equals(float, sub) -> (float=float, float_out=float)
Easily subtract from a float! <3 Rama

Args:
    float (float): 
    sub (float): 

Returns:
    tuple: 

    float (float): 

    float_out (float):

<a id="unreal.VictoryBPFunctionLibrary.victory_create_proc"></a>

#### victory\_create\_proc

```python
@classmethod
def victory_create_proc(
        cls,
        full_path_of_program_to_run: str,
        commandline_args: Array[str],
        detach: bool,
        hidden: bool,
        priority: int = 0,
        optional_working_directory: str = "",
        read_pipe_object: RamaVictoryPluginCreateProcessPipe = None) -> int
```

X.victory_create_proc(full_path_of_program_to_run, commandline_args, detach, hidden, priority=0, optional_working_directory="", read_pipe_object=None) -> int32
Launch a new process, if it is not set to be detached, UE4 will not fully close until the other process completes.

The new process id is returned!

Args:
    full_path_of_program_to_run (str): 
    commandline_args (Array[str]): 
    detach (bool): Ensure completion before UE4 closes or not? Detach = UE4 can close and process will keep going / possibly never stop running as there is no one left to stop the process now ♥ Rama
    hidden (bool): 
    priority (int32): Priority options: -2 idle, -1 low, 0 normal, 1 high, 2 higher
    optional_working_directory (str): 
    read_pipe_object (RamaVictoryPluginCreateProcessPipe): Construct a new object of class URamaVictoryPluginCreateProcessPipe if you want to capture the output (STDOUT or STDERR) of this process! ♥♥♥ Yes ♥♥♥ !!!! (call ReadFromPipe on the object over time, in a timer, after creating the procedure, remember to nullptr Your Object Reference after closing the pipe, so that UE4 will garbage-collect the object! ) ♥ Rama

Returns:
    int32: 

    process_id (int32):

<a id="unreal.VictoryBPFunctionLibrary.victory_set_time_stamp"></a>

#### victory\_set\_time\_stamp

```python
@classmethod
def victory_set_time_stamp(cls, file: str, time_stamp: DateTime) -> None
```

X.victory_set_time_stamp(file, time_stamp) -> None
Victory Set Time Stamp

Args:
    file (str): 
    time_stamp (DateTime):

<a id="unreal.VictoryBPFunctionLibrary.victory_save_string_to_os_clipboard"></a>

#### victory\_save\_string\_to\_os\_clipboard

```python
@classmethod
def victory_save_string_to_os_clipboard(cls, to_clipboard: str) -> None
```

X.victory_save_string_to_os_clipboard(to_clipboard) -> None
Victory Save String to OSClipboard

Args:
    to_clipboard (str):

<a id="unreal.VictoryBPFunctionLibrary.victory_save_pixels"></a>

#### victory\_save\_pixels

```python
@classmethod
def victory_save_pixels(cls, full_file_path: str, width: int, height: int,
                        image_pixels: Array[LinearColor], save_as_bmp: bool,
                        s_rgb: bool) -> Optional[str]
```

X.victory_save_pixels(full_file_path, width, height, image_pixels, save_as_bmp, s_rgb) -> str or None
Save an array of pixels to disk as a PNG! It is very important that you supply the curret width and height of the image! Returns false if Width * Height != Array length or file could not be saved to the location specified. I return an ErrorString to clarify what the exact issue was. -Rama
              CommunityTip from DarkFlash007: Make sure “Mip Gen Setting” is set to “Nomipmaps”

Args:
    full_file_path (str): 
    width (int32): 
    height (int32): 
    image_pixels (Array[LinearColor]): 
    save_as_bmp (bool): 
    s_rgb (bool): 

Returns:
    str or None: 

    error_string (str):

<a id="unreal.VictoryBPFunctionLibrary.victory_load_texture2d_from_file_by_extension"></a>

#### victory\_load\_texture2d\_from\_file\_by\_extension

```python
@classmethod
def victory_load_texture2d_from_file_by_extension(
        cls, full_file_path: str,
        image_format: JoyImageFormats) -> Tuple[Texture2D, bool, int, int]
```

X.victory_load_texture2d_from_file_by_extension(full_file_path, image_format) -> (Texture2D, is_valid=bool, width=int32, height=int32)
Load a Texture2D from a JPG,PNG,BMP,ICO,EXR,ICNS file! IsValid tells you if file path was valid or not. Enjoy! -Rama

Args:
    full_file_path (str): 
    image_format (JoyImageFormats): 

Returns:
    tuple: 

    is_valid (bool): 

    width (int32): 

    height (int32):

<a id="unreal.VictoryBPFunctionLibrary.victory_load_texture2d_from_file_pixels"></a>

#### victory\_load\_texture2d\_from\_file\_pixels

```python
@classmethod
def victory_load_texture2d_from_file_pixels(
    cls, full_file_path: str, image_format: JoyImageFormats
) -> Tuple[Texture2D, bool, int, int, Array[LinearColor]]
```

X.victory_load_texture2d_from_file_pixels(full_file_path, image_format) -> (Texture2D, is_valid=bool, width=int32, height=int32, out_pixels=Array[LinearColor])
Load a Texture2D from a JPG,PNG,BMP,ICO,EXR,ICNS file! IsValid tells you if file path was valid or not. Enjoy! -Rama
              CommunityTip from DarkFlash007: Make sure “Mip Gen Setting” is set to “Nomipmaps”

Args:
    full_file_path (str): 
    image_format (JoyImageFormats): 

Returns:
    tuple: 

    is_valid (bool): 

    width (int32): 

    height (int32): 

    out_pixels (Array[LinearColor]):

<a id="unreal.VictoryBPFunctionLibrary.victory_load_texture2d_from_file"></a>

#### victory\_load\_texture2d\_from\_file

```python
@classmethod
def victory_load_texture2d_from_file(
        cls, full_file_path: str) -> Tuple[Texture2D, bool, int, int]
```

X.victory_load_texture2d_from_file(full_file_path) -> (Texture2D, is_valid=bool, width=int32, height=int32)
Load a Texture2D from a JPG,PNG,BMP,ICO,EXR,ICNS file! IsValid tells you if file path was valid or not. The image type is assumed from an extension such as .jpg, .png, .bmp. Enjoy! -Rama

Args:
    full_file_path (str): 

Returns:
    tuple: 

    is_valid (bool): 

    width (int32): 

    height (int32):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_string_from_os_clipboard"></a>

#### victory\_get\_string\_from\_os\_clipboard

```python
@classmethod
def victory_get_string_from_os_clipboard(cls) -> str
```

X.victory_get_string_from_os_clipboard() -> str
Victory Get String from OSClipboard

Returns:
    str: 

    from_clipboard (str):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_pixels_array_from_t2d"></a>

#### victory\_get\_pixels\_array\_from\_t2d

```python
@classmethod
def victory_get_pixels_array_from_t2d(
        cls, t2d: Texture2D) -> Optional[Tuple[int, int, Array[LinearColor]]]
```

X.victory_get_pixels_array_from_t2d(t2d) -> (texture_width=int32, texture_height=int32, pixel_array=Array[LinearColor]) or None
This will modify the original T2D to remove sRGB and change compression to VectorDisplacementMap to ensure accurate pixel reading. -Rama
              CommunityTip from DarkFlash007: Make sure “Mip Gen Setting” is set to “Nomipmaps”//, DeprecatedFunction, DeprecationMessage="This function will not work until I figure out how to update it to 4.25, if you need it urgently, please post in my ue4 forum thread for this plugin"))

Args:
    t2d (Texture2D): 

Returns:
    tuple or None: 

    texture_width (int32): 

    texture_height (int32): 

    pixel_array (Array[LinearColor]):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_pixel_from_t2d"></a>

#### victory\_get\_pixel\_from\_t2d

```python
@classmethod
def victory_get_pixel_from_t2d(cls, t2d: Texture2D, x: int,
                               y: int) -> Optional[LinearColor]
```

X.victory_get_pixel_from_t2d(t2d, x, y) -> LinearColor or None
This will modify the original T2D to remove sRGB and change compression to VectorDisplacementMap to ensure accurate pixel reading. -Rama
              CommunityTip from DarkFlash007: Make sure “Mip Gen Setting” is set to “Nomipmaps” //, DeprecatedFunction, DeprecationMessage="This function will not work until I figure out how to update it to 4.25, if you need it urgently, please post in my ue4 forum thread for this plugin"))

Args:
    t2d (Texture2D): 
    x (int32): 
    y (int32): 

Returns:
    LinearColor or None: 

    pixel_color (LinearColor):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_file_time_stamp"></a>

#### victory\_get\_file\_time\_stamp

```python
@classmethod
def victory_get_file_time_stamp(cls, file: str) -> DateTime
```

X.victory_get_file_time_stamp(file) -> DateTime
Victory Get File Time Stamp

Args:
    file (str): 

Returns:
    DateTime:

<a id="unreal.VictoryBPFunctionLibrary.victory_get_files_in_root_and_all_sub_folders"></a>

#### victory\_get\_files\_in\_root\_and\_all\_sub\_folders

```python
@classmethod
def victory_get_files_in_root_and_all_sub_folders(
        cls, root_folder_full_path: str, ext: str) -> Optional[Array[str]]
```

X.victory_get_files_in_root_and_all_sub_folders(root_folder_full_path, ext) -> Array[str] or None
Obtain all files in a provided root directory, including all subdirectories, with optional extension filter. All files are returned if Ext is left blank. The full file path is returned because the file could be in any subdirectory. Returns false if operation could not occur.

Args:
    root_folder_full_path (str): 
    ext (str): 

Returns:
    Array[str] or None: 

    files (Array[str]):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_files"></a>

#### victory\_get\_files

```python
@classmethod
def victory_get_files(cls, root_folder_full_path: str,
                      ext: str) -> Optional[Array[str]]
```

X.victory_get_files(root_folder_full_path, ext) -> Array[str] or None
Obtain all files in a provided directory, with optional extension filter. All files are returned if Ext is left blank. Returns false if operation could not occur.

Args:
    root_folder_full_path (str): 
    ext (str): 

Returns:
    Array[str] or None: 

    files (Array[str]):

<a id="unreal.VictoryBPFunctionLibrary.victory_get_pixel"></a>

#### victory\_get\_pixel

```python
@classmethod
def victory_get_pixel(cls, pixels: Array[LinearColor], image_height: int,
                      x: int, y: int) -> Optional[LinearColor]
```

X.victory_get_pixel(pixels, image_height, x, y) -> LinearColor or None
Retrieve a pixel color value given the pixel array, the image height, and the coordinates. Returns false if the coordinates were not valid. Pixel coordinates start from upper left corner as 0,0. X= horizontal, Y = vertical
              CommunityTip from DarkFlash007: Make sure “Mip Gen Setting” is set to “Nomipmaps”

Args:
    pixels (Array[LinearColor]): 
    image_height (int32): 
    x (int32): 
    y (int32): 

Returns:
    LinearColor or None: 

    found_color (LinearColor):

<a id="unreal.VictoryBPFunctionLibrary.utc_to_local"></a>

#### utc\_to\_local

```python
@classmethod
def utc_to_local(cls, utc_time: DateTime) -> DateTime
```

X.utc_to_local(utc_time) -> DateTime
UTCTo Local

Args:
    utc_time (DateTime): 

Returns:
    DateTime: 

    local_time (DateTime):

<a id="unreal.VictoryBPFunctionLibrary.text_to_int"></a>

#### text\_to\_int

```python
@classmethod
def text_to_int(cls, text: Text, use_dot_for_thousands: bool = False) -> int
```

X.text_to_int(text, use_dot_for_thousands=False) -> int32
Text to Int

Args:
    text (Text): 
    use_dot_for_thousands (bool): 

Returns:
    int32:

<a id="unreal.VictoryBPFunctionLibrary.text_to_float"></a>

#### text\_to\_float

```python
@classmethod
def text_to_float(cls,
                  text: Text,
                  use_dot_for_thousands: bool = False) -> float
```

X.text_to_float(text, use_dot_for_thousands=False) -> float
Text to Float

Args:
    text (Text): 
    use_dot_for_thousands (bool): 

Returns:
    float:

<a id="unreal.VictoryBPFunctionLibrary.string_combine_strings_multi"></a>

#### string\_combine\_strings\_multi

```python
@classmethod
def string_combine_strings_multi(cls, a: str, b: str) -> str
```

X.string_combine_strings_multi(a, b) -> str
Separator is always a space

Args:
    a (str): 
    b (str): 

Returns:
    str:

<a id="unreal.VictoryBPFunctionLibrary.string_combine_strings"></a>

#### string\_combine\_strings

```python
@classmethod
def string_combine_strings(cls,
                           string_first: str,
                           string_second: str,
                           separator: str = "",
                           string_first_label: str = "",
                           string_second_label: str = "") -> str
```

X.string_combine_strings(string_first, string_second, separator="", string_first_label="", string_second_label="") -> str
Combines two strings together! The Separator and the Labels are optional

Args:
    string_first (str): 
    string_second (str): 
    separator (str): 
    string_first_label (str): 
    string_second_label (str): 

Returns:
    str:

<a id="unreal.VictoryBPFunctionLibrary.server_travel"></a>

#### server\_travel

```python
@classmethod
def server_travel(cls,
                  world_context_object: Object,
                  map_name: str,
                  skip_notify_players: bool = False) -> None
```

X.server_travel(world_context_object, map_name, skip_notify_players=False) -> None
Server Travel! This is an async load level process which allows you to put up a UMG widget while the level loading occurs!

Args:
    world_context_object (Object): 
    map_name (str): 
    skip_notify_players (bool):

<a id="unreal.VictoryBPFunctionLibrary.remove_all_widgets_of_class"></a>

#### remove\_all\_widgets\_of\_class

```python
@classmethod
def remove_all_widgets_of_class(cls, world_context_object: Object,
                                widget_class: Class) -> None
```

X.remove_all_widgets_of_class(world_context_object, widget_class) -> None
Remove all widgets of a certain class from viewport!

Args:
    world_context_object (Object): 
    widget_class (type(Class)):

<a id="unreal.VictoryBPFunctionLibrary.load_string_from_file"></a>

#### load\_string\_from\_file

```python
@classmethod
def load_string_from_file(cls,
                          full_file_path: str = "Enter Full File Path"
                          ) -> Optional[str]
```

X.load_string_from_file(full_file_path="Enter Full File Path") -> str or None
Load a text file to a single string that you can use ParseIntoArray on newline characters if you want same format as LoadStringArrayFromFile. This version supports unicode characters!

Args:
    full_file_path (str): 

Returns:
    str or None: 

    result (str):

<a id="unreal.VictoryBPFunctionLibrary.load_string_array_from_file"></a>

#### load\_string\_array\_from\_file

```python
@classmethod
def load_string_array_from_file(
        cls,
        full_file_path: str = "Enter Full File Path",
        exclude_empty_lines: bool = False) -> Optional[Tuple[Array[str], int]]
```

X.load_string_array_from_file(full_file_path="Enter Full File Path", exclude_empty_lines=False) -> (string_array=Array[str], array_size=int32) or None
Loads a text file from hard disk and parses it into a String array, where each entry in the string array is 1 line from the text file. Option to exclude lines that are only whitespace characters or '\n'. Returns the size of the final String Array that was created. Returns false if the file could be loaded from hard disk.

Args:
    full_file_path (str): 
    exclude_empty_lines (bool): 

Returns:
    tuple or None: 

    string_array (Array[str]): 

    array_size (int32):

<a id="unreal.VictoryBPFunctionLibrary.load_object_from_asset_path"></a>

#### load\_object\_from\_asset\_path

```python
@classmethod
def load_object_from_asset_path(cls, object_class: Class,
                                path: Name) -> Tuple[Object, bool]
```

X.load_object_from_asset_path(object_class, path) -> (Object, is_valid=bool)
The FName that is expected is the exact same format as when you right click on asset -> Copy Reference! You can directly paste copied references into this node! IsValid lets you know if the path was correct or not and I was able to load the object. MAKE SURE TO SAVE THE RETURNED OBJECT AS A VARIABLE. Otherwise your shiny new asset will get garbage collected. I recommend you cast the return value to the appropriate object and then promote it to a variable :)  -Rama

Args:
    object_class (type(Class)): 
    path (Name): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.is_widget_of_class_in_viewport"></a>

#### is\_widget\_of\_class\_in\_viewport

```python
@classmethod
def is_widget_of_class_in_viewport(cls, world_context_object: Object,
                                   widget_class: Class) -> bool
```

X.is_widget_of_class_in_viewport(world_context_object, widget_class) -> bool
Is Widget Of Class in Viewport

Args:
    world_context_object (Object): 
    widget_class (type(Class)): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.is_alpha_numeric"></a>

#### is\_alpha\_numeric

```python
@classmethod
def is_alpha_numeric(cls, string: str) -> bool
```

X.is_alpha_numeric(string) -> bool
OS

Args:
    string (str): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.has_substring"></a>

#### has\_substring

```python
@classmethod
def has_substring(cls,
                  search_in: str,
                  substring: str,
                  search_case: SearchCase = SearchCase.IGNORE_CASE,
                  search_dir: SearchDir = SearchDir.FROM_START) -> bool
```

X.has_substring(search_in, substring, search_case=SearchCase.IGNORE_CASE, search_dir=SearchDir.FROM_START) -> bool
Returns whether or not the SearchIn string contains the supplied Substring.
     Ex: "cat" is a contained within "concatenation" as a substring.

Args:
    search_in (str): The string to search within
    substring (str): The string to look for in the SearchIn string
    search_case (SearchCase): 
    search_dir (SearchDir): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.get_widget_from_name"></a>

#### get\_widget\_from\_name

```python
@classmethod
def get_widget_from_name(cls, parent_user_widget: UserWidget,
                         name: Name) -> Widget
```

X.get_widget_from_name(parent_user_widget, name) -> Widget
Get Widget from Name

Args:
    parent_user_widget (UserWidget): 
    name (Name): 

Returns:
    Widget:

<a id="unreal.VictoryBPFunctionLibrary.get_utc_from_unix_time_stamp"></a>

#### get\_utc\_from\_unix\_time\_stamp

```python
@classmethod
def get_utc_from_unix_time_stamp(cls, unix_time_stamp: int) -> DateTime
```

X.get_utc_from_unix_time_stamp(unix_time_stamp) -> DateTime
Blueprints does not support int64 so at some pt in future int32 will not be enough, probably by then dolphins will rule the world, or UE4 BP will support int64, or both!  <3 Rama

Args:
    unix_time_stamp (int64): 

Returns:
    DateTime: 

    utc_time (DateTime):

<a id="unreal.VictoryBPFunctionLibrary.get_unix_time_stamp"></a>

#### get\_unix\_time\_stamp

```python
@classmethod
def get_unix_time_stamp(cls, utc_time: DateTime) -> int
```

X.get_unix_time_stamp(utc_time) -> int64
Blueprints does not support int64 so at some pt in future int32 will not be enough, probably by then dolphins will rule the world, or UE4 BP will support int64, or both!  <3 Rama

Args:
    utc_time (DateTime): 

Returns:
    int64:

<a id="unreal.VictoryBPFunctionLibrary.get_static_mesh_vertex_locations"></a>

#### get\_static\_mesh\_vertex\_locations

```python
@classmethod
def get_static_mesh_vertex_locations(
        cls,
        comp: StaticMeshComponent,
        lod_index: int = 0) -> Optional[Array[Vector]]
```

X.get_static_mesh_vertex_locations(comp, lod_index=0) -> Array[Vector] or None
Obtain the scaled,rotated, and translated vertex positions for any static mesh! Returns false if operation could not occur because the comp or static mesh asset was invalid. <3 Rama

Args:
    comp (StaticMeshComponent): 
    lod_index (int32): 

Returns:
    Array[Vector] or None: 

    vertex_positions (Array[Vector]):

<a id="unreal.VictoryBPFunctionLibrary.get_object_path"></a>

#### get\_object\_path

```python
@classmethod
def get_object_path(cls, obj: Object) -> Name
```

X.get_object_path(obj) -> Name
Uses the same format as I use for LoadObjectFromAssetPath! Use this node to get the asset path of objects in the world! -Rama

Args:
    obj (Object): 

Returns:
    Name:

<a id="unreal.VictoryBPFunctionLibrary.get_names_of_loaded_levels"></a>

#### get\_names\_of\_loaded\_levels

```python
@classmethod
def get_names_of_loaded_levels(cls,
                               world_context_object: Object) -> Array[str]
```

X.get_names_of_loaded_levels(world_context_object) -> Array[str]
Get the names of all currently loaded and visible levels!

Args:
    world_context_object (Object): 

Returns:
    Array[str]: 

    names_of_loaded_levels (Array[str]):

<a id="unreal.VictoryBPFunctionLibrary.get_first_widget_of_class"></a>

#### get\_first\_widget\_of\_class

```python
@classmethod
def get_first_widget_of_class(cls, world_context_object: Object,
                              widget_class: Class,
                              top_level_only: bool) -> UserWidget
```

X.get_first_widget_of_class(world_context_object, widget_class, top_level_only) -> UserWidget
Find first widget of a certain class and return it.

Args:
    world_context_object (Object): 
    widget_class (type(Class)): The widget class to filter by.
    top_level_only (bool): Only a widget that is a direct child of the viewport will be returned.

Returns:
    UserWidget:

<a id="unreal.VictoryBPFunctionLibrary.get_closest_actor_of_class_in_radius_of_location"></a>

#### get\_closest\_actor\_of\_class\_in\_radius\_of\_location

```python
@classmethod
def get_closest_actor_of_class_in_radius_of_location(
        cls, world_context_object: Object, actor_class: Class, center: Vector,
        radius: float) -> Tuple[Actor, bool]
```

X.get_closest_actor_of_class_in_radius_of_location(world_context_object, actor_class, center, radius) -> (Actor, is_valid=bool)
AI

Args:
    world_context_object (Object): 
    actor_class (type(Class)): 
    center (Vector): 
    radius (float): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.get_closest_actor_of_class_in_radius_of_actor"></a>

#### get\_closest\_actor\_of\_class\_in\_radius\_of\_actor

```python
@classmethod
def get_closest_actor_of_class_in_radius_of_actor(
        cls, world_context_object: Object, actor_class: Class,
        actor_center: Actor, radius: float) -> Tuple[Actor, bool]
```

X.get_closest_actor_of_class_in_radius_of_actor(world_context_object, actor_class, actor_center, radius) -> (Actor, is_valid=bool)
Get Closest Actor Of Class in Radius Of Actor

Args:
    world_context_object (Object): 
    actor_class (type(Class)): 
    actor_center (Actor): 
    radius (float): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.VictoryBPFunctionLibrary.get_all_bone_names_below_bone"></a>

#### get\_all\_bone\_names\_below\_bone

```python
@classmethod
def get_all_bone_names_below_bone(
        cls, skeletal_mesh_comp: SkeletalMeshComponent,
        starting_bone_name: Name) -> Tuple[int, Array[Name]]
```

X.get_all_bone_names_below_bone(skeletal_mesh_comp, starting_bone_name) -> (int32, bone_names=Array[Name])
Get All Bone Names Below Bone, requires a physics asset, by Rama

Args:
    skeletal_mesh_comp (SkeletalMeshComponent): 
    starting_bone_name (Name): The name of the bone to find all bones below.

Returns:
    Array[Name]: total number of bones found

    bone_names (Array[Name]): , all of the bone names below the starting bone.

<a id="unreal.VictoryBPFunctionLibrary.generate_unique_content_relative_file_name"></a>

#### generate\_unique\_content\_relative\_file\_name

```python
@classmethod
def generate_unique_content_relative_file_name(
        cls,
        content_relative_file_path: str,
        create_folder_tree: bool = True) -> Optional[Tuple[str, str]]
```

X.generate_unique_content_relative_file_name(content_relative_file_path, create_folder_tree=True) -> (content_relative_new_file_name=str, absolute_path=str) or None

CreateFolderTree: I make sure the path you have supplied, relative to Project Content Folder, is created if you set this to true! ♥ Rama

Args:
    content_relative_file_path (str): 
    create_folder_tree (bool): 

Returns:
    tuple or None: false if Folder Tree could not be created, see "AbsolutePath" to see what folder tree structure was attempted. Creates an unused filename, Given a basefile name that is relative to Content Folder of Project (So if you supply "YourFolder/BaseFile.EXT", this file would be actually be located in YourProjectFolder/Content/YourFolder/BaseFile.EXT), adding a number BaseFile1, BaseFile2, BaseFile3, as needed until a unique filename is generated!

    content_relative_new_file_name (str): 

    absolute_path (str):

<a id="unreal.VictoryBPFunctionLibrary.flash_game_on_task_bar"></a>

#### flash\_game\_on\_task\_bar

```python
@classmethod
def flash_game_on_task_bar(cls,
                           pc: PlayerController,
                           flash_continuous: bool = False,
                           max_flash_count: int = 3,
                           flash_frequency_milliseconds: int = 500) -> None
```

X.flash_game_on_task_bar(pc, flash_continuous=False, max_flash_count=3, flash_frequency_milliseconds=500) -> None
Flashes the game on the windows OS task bar! Please note this won't look the best in PIE, flashing is smoother in Standalone or packaged game. You can use GameWindowIsForeGroundInOS to see if there is a need to get the user's attention! <3 Rama

Args:
    pc (PlayerController): 
    flash_continuous (bool): 
    max_flash_count (int32): 
    flash_frequency_milliseconds (int32):

<a id="unreal.VictoryBPFunctionLibrary.file_io_save_string_text_to_file"></a>

#### file\_io\_save\_string\_text\_to\_file

```python
@classmethod
def file_io_save_string_text_to_file(cls,
                                     save_directory: str,
                                     joyful_file_name: str,
                                     save_text: str,
                                     allow_over_writing: bool = False,
                                     allow_append: bool = False) -> bool
```

X.file_io_save_string_text_to_file(save_directory, joyful_file_name, save_text, allow_over_writing=False, allow_append=False) -> bool
Saves text to filename of your choosing, make sure include whichever file extension you want in the filename, ex: SelfNotes.txt . Make sure to include the entire file path in the save directory, ex: C:\MyGameDir\BPSavedTextFiles

Args:
    save_directory (str): 
    joyful_file_name (str): 
    save_text (str): 
    allow_over_writing (bool): 
    allow_append (bool): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.file_io_save_string_array_to_file"></a>

#### file\_io\_save\_string\_array\_to\_file

```python
@classmethod
def file_io_save_string_array_to_file(cls,
                                      save_directory: str,
                                      joyful_file_name: str,
                                      save_text: Array[str],
                                      allow_over_writing: bool = False,
                                      allow_append: bool = False) -> bool
```

X.file_io_save_string_array_to_file(save_directory, joyful_file_name, save_text, allow_over_writing=False, allow_append=False) -> bool
Saves multiple Strings to filename of your choosing, with each string on its own line! Make sure include whichever file extension you want in the filename, ex: SelfNotes.txt . Make sure to include the entire file path in the save directory, ex: C:\MyGameDir\BPSavedTextFiles

Args:
    save_directory (str): 
    joyful_file_name (str): 
    save_text (Array[str]): 
    allow_over_writing (bool): 
    allow_append (bool): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.create_static_mesh_asset_from_dynamic_mesh"></a>

#### create\_static\_mesh\_asset\_from\_dynamic\_mesh

```python
@classmethod
def create_static_mesh_asset_from_dynamic_mesh(
    cls, content_folder_path: str, dynamic_mesh_comp: DynamicMeshComponent
) -> Tuple[StaticMesh, str, str, bool]
```

X.create_static_mesh_asset_from_dynamic_mesh(content_folder_path, dynamic_mesh_comp) -> (StaticMesh, status=str, new_asset_file_path=str, success=bool)
Yes!!! For Real!!!
                      ♥ Rama
              PS: If you find the new asset has a pivot point far from itself, I recommend moving the mesh to world origin (0,0,0) in level viewport before saving

              PSS: Only works in Editor Builds by the way, see UE5 C++ Source file:
                      UE_5.0\Engine\Plugins\Runtime\MeshModelingToolset\Source\ModelingComponentsEditorOnly\PublicEditorModelingObjectsCreationAPI.h
                              for more info!

Args:
    content_folder_path (str): If this is just a name (there is no need to add a ".uasset" file extension to the name), the Static Mesh Asset will be created in your game's Content root directory (folder)! If the path is YourFolder/YourAssetName, then the asset will be created in your chosen folder (within Content Folder), I create the folder if necessary, using GenericPlatformFile::CreateDirectoryTree, my very first UE Engine Github C++ code gifts! ♥ Rama
    dynamic_mesh_comp (DynamicMeshComponent): 

Returns:
    tuple: 

    status (str): more info about reason for operation not succeeding, or a special Success Message!

    new_asset_file_path (str): 

    success (bool):

<a id="unreal.VictoryBPFunctionLibrary.closest_points_on_two_lines"></a>

#### closest\_points\_on\_two\_lines

```python
@classmethod
def closest_points_on_two_lines(
        cls, line_point1: Vector, line_vec1: Vector, line_point2: Vector,
        line_vec2: Vector) -> Optional[Tuple[Vector, Vector]]
```

X.closest_points_on_two_lines(line_point1, line_vec1, line_point2, line_vec2) -> (closest_point_line1=Vector, closest_point_line2=Vector) or None
* Calculate the closest points between two infinitely long lines.
* If lines are intersecting (not parallel) it will return false! Use Line To Line Intersection instead.
*

Args:
    line_point1 (Vector): Line point of the first line. *
    line_vec1 (Vector): Line direction (normal) of the first line. Should be a normalized vector. *
    line_point2 (Vector): Line point of the second line. *
    line_vec2 (Vector): Line direction (normal) of the second line. Should be a normalized vector. *

Returns:
    tuple or None: true if lines are parallel, false otherwise.

    closest_point_line1 (Vector): The closest point of line1 to line2. Returns zero if the lines intersect. *

    closest_point_line2 (Vector): The closest point of line2 to line1. Returns zero if the lines intersect. *

<a id="unreal.VictoryBPFunctionLibrary.closest_points_of_line_segments"></a>

#### closest\_points\_of\_line\_segments

```python
@classmethod
def closest_points_of_line_segments(
        cls, line1_start: Vector, line1_end: Vector, line2_start: Vector,
        line2_end: Vector) -> Tuple[Vector, Vector]
```

X.closest_points_of_line_segments(line1_start, line1_end, line2_start, line2_end) -> (line_point1=Vector, line_point2=Vector)
Find closest points between 2 line segments.

Args:
    line1_start (Vector): 
    line1_end (Vector): 
    line2_start (Vector): 
    line2_end (Vector): 

Returns:
    tuple: 

    line_point1 (Vector): Closest point on segment 1 to segment 2.

    line_point2 (Vector): Closest point on segment 2 to segment 1.

<a id="unreal.VictoryBPFunctionLibrary.client_window_game_window_is_fore_ground_in_os"></a>

#### client\_window\_game\_window\_is\_fore\_ground\_in\_os

```python
@classmethod
def client_window_game_window_is_fore_ground_in_os(cls) -> bool
```

X.client_window_game_window_is_fore_ground_in_os() -> bool
Is the Current Game Window the Foreground window in the OS, or in the Editor? This will be accurate in standalone running of the game as well as in the editor PIE

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.capture_component2d_save_image"></a>

#### capture\_component2d\_save\_image

```python
@classmethod
def capture_component2d_save_image(cls, target: SceneCaptureComponent2D,
                                   image_path: str,
                                   clear_colour: LinearColor) -> bool
```

X.capture_component2d_save_image(target, image_path, clear_colour) -> bool
I highly recommend that your Texture Render Target Format be "RTF RGB8 SRGB" both so it is compatible, and so it looks the same as in-game
        <3 Rama.

Make sure to include the appropriate image extension in your file path! Recommended: .bmp, .jpg, .png. Contributed by Community Member Kris!

Args:
    target (SceneCaptureComponent2D): 
    image_path (str): 
    clear_colour (LinearColor): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.capture_component2d_project"></a>

#### capture\_component2d\_project

```python
@classmethod
def capture_component2d_project(cls, target: SceneCaptureComponent2D,
                                location: Vector) -> Optional[Vector2D]
```

X.capture_component2d_project(target, location) -> Vector2D or None
Contributed by Community Member Kris!

Args:
    target (SceneCaptureComponent2D): 
    location (Vector): 

Returns:
    Vector2D or None: 

    out_pixel_location (Vector2D):

<a id="unreal.VictoryBPFunctionLibrary.capture2d_save_image"></a>

#### capture2d\_save\_image

```python
@classmethod
def capture2d_save_image(cls, target: SceneCapture2D, image_path: str,
                         clear_colour: LinearColor) -> bool
```

X.capture2d_save_image(target, image_path, clear_colour) -> bool
I highly recommend that your Texture Render Target Format be "RTF RGB8 SRGB" both so it is compatible, and so it looks the same as in-game
        <3 Rama.

Make sure to include the appropriate image extension in your file path! Recommended: .bmp, .jpg, .png. Contributed by Community Member Kris!

Args:
    target (SceneCapture2D): 
    image_path (str): 
    clear_colour (LinearColor): 

Returns:
    bool:

<a id="unreal.VictoryBPFunctionLibrary.capture2d_project"></a>

#### capture2d\_project

```python
@classmethod
def capture2d_project(cls, target: SceneCapture2D,
                      location: Vector) -> Optional[Vector2D]
```

X.capture2d_project(target, location) -> Vector2D or None
Contributed by Community Member Kris!

Args:
    target (SceneCapture2D): 
    location (Vector): 

Returns:
    Vector2D or None: 

    out_pixel_location (Vector2D):

<a id="unreal.VictoryBPFunctionLibrary.append_multiple"></a>

#### append\_multiple

```python
@classmethod
def append_multiple(cls, a: str, b: str) -> str
```

X.append_multiple(a, b) -> str
Addition of strings (A + B) with pins. Contributed by KeyToTruth

Args:
    a (str): 
    b (str): 

Returns:
    str:

<a id="unreal.VictoryBPFunctionLibrary.animation_get_aim_offsets_from_rotation"></a>

#### animation\_get\_aim\_offsets\_from\_rotation

```python
@classmethod
def animation_get_aim_offsets_from_rotation(
        cls, anim_bp_owner: Actor,
        the_rotation: Rotator) -> Optional[Tuple[float, float]]
```

X.animation_get_aim_offsets_from_rotation(anim_bp_owner, the_rotation) -> (pitch=float, yaw=float) or None
AnimBPOwner - Must be a Character, Conversion Internally For Convenience.\n\nRetrieves the Aim Offsets Pitch & Yaw for the AnimBPOwner Based On the supplied Rotation.\n\nThe Pitch and Yaw are meant to be used with a Blend Space going from -90,-90 to 90,90.\n    Returns true if function filled the pitch and yaw vars successfully

Args:
    anim_bp_owner (Actor): 
    the_rotation (Rotator): 

Returns:
    tuple or None: 

    pitch (float): 

    yaw (float):

<a id="unreal.VictoryBPFunctionLibrary.animation_get_aim_offsets"></a>

#### animation\_get\_aim\_offsets

```python
@classmethod
def animation_get_aim_offsets(
        cls, anim_bp_owner: Actor) -> Optional[Tuple[float, float]]
```

X.animation_get_aim_offsets(anim_bp_owner) -> (pitch=float, yaw=float) or None
AnimBPOwner - Must be a Character, Conversion Internally For Convenience.\n\nRetrieves the Aim Offsets Pitch & Yaw Based On the Rotation of the Controller of The Character Owning The Anim Instance.\n\nThe Pitch and Yaw are meant to be used with a Blend Space going from -90,-90 to 90,90.\n   Returns true if function filled the pitch and yaw vars successfully

Args:
    anim_bp_owner (Actor): 

Returns:
    tuple or None: 

    pitch (float): 

    yaw (float):

<a id="unreal.VictoryBPFunctionLibrary.accessor_get_player_controller"></a>

#### accessor\_get\_player\_controller

```python
@classmethod
def accessor_get_player_controller(
        cls, the_character: Actor) -> Tuple[PlayerController, bool]
```

X.accessor_get_player_controller(the_character) -> (PlayerController, is_valid=bool)
Get Player Character's Player Controller. Requires: The Passed in Actor must be a character and it must be a player controlled character. IsValid will tell you if the return value is valid, make sure to do a Branch to confirm this!

Args:
    the_character (Actor): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.UrbanDataBPLibrary"></a>