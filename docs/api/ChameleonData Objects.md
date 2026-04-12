## ChameleonData Objects

```python
class ChameleonData(Object)
```

Chameleon Data

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: ChameleonData.h

<a id="unreal.ChameleonData.unbind_uobject_to_browser"></a>

#### unbind\_uobject\_to\_browser

```python
def unbind_uobject_to_browser(aka_name: Name,
                              name: str,
                              object: Object,
                              is_permanent: bool = True) -> None
```

x.unbind_uobject_to_browser(aka_name, name, object, is_permanent=True) -> None
Remove an existing script binding registered by BindUObject. Properties and Functions will be accessible from JavaScript side.
note: Supported widgets: SWebBrowser only.
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget
    name (str): The name of the object to remove.
    object (Object): The object will only be removed if it is the same object as the one passed in.
    is_permanent (bool): Must match the bIsPermanent argument passed to BindUObject.

<a id="unreal.ChameleonData.stop_load_page"></a>

#### stop\_load\_page

```python
def stop_load_page(aka_name: Name) -> None
```

x.stop_load_page(aka_name) -> None
Stop loading the page in SWebBrowser.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

<a id="unreal.ChameleonData.spawn_to_graph_by_class"></a>

#### spawn\_to\_graph\_by\_class

```python
def spawn_to_graph_by_class(aka_name: Name,
                            node_class: Class,
                            update: bool = True) -> EdGraphNode
```

x.spawn_to_graph_by_class(aka_name, node_class, update=True) -> EdGraphNode
Spawn a new node in SGraphPanel.
note: add in v1.2.0(Experimental)

Args:
    aka_name (Name): The aka name of the SGraphPanel
    node_class (type(Class)): 
    update (bool): Whether update the graph panel after spawn the new node

Returns:
    EdGraphNode: the added new node

<a id="unreal.ChameleonData.spawn_function_to_graph_with_spawner"></a>

#### spawn\_function\_to\_graph\_with\_spawner

```python
def spawn_function_to_graph_with_spawner(
        aka_name: Name, bp_function_spawner: Object) -> EdGraphNode
```

x.spawn_function_to_graph_with_spawner(aka_name, bp_function_spawner) -> EdGraphNode
Spawn a specified function of a module in SGraphPanel through a BPFunctionSpawner.
note: add in v1.2.0(Experimental)

Args:
    aka_name (Name): The aka name of the SGraphPanel
    bp_function_spawner (Object): The BPFunctionSpawner of the function

Returns:
    EdGraphNode: the added new node

<a id="unreal.ChameleonData.spawn_function_to_graph"></a>

#### spawn\_function\_to\_graph

```python
def spawn_function_to_graph(aka_name: Name, module: Class,
                            function_name: str) -> EdGraphNode
```

x.spawn_function_to_graph(aka_name, module, function_name) -> EdGraphNode
Spawn a specified function of a module in SGraphPanel.
note: add in v1.2.0(Experimental)

Args:
    aka_name (Name): The aka name of the SGraphPanel
    module (type(Class)): The module of the function
    function_name (str): The name of the function

Returns:
    EdGraphNode: the added new node

<a id="unreal.ChameleonData.snapshot_sketch"></a>

#### snapshot\_sketch

```python
@classmethod
def snapshot_sketch(cls,
                    override_window_size: Vector2D = [0.000000, 0.000000],
                    image_file_path: str = "") -> str
```

X.snapshot_sketch(override_window_size=[0.000000, 0.000000], image_file_path="") -> str
Snapshot the Sketch Window, and save it to an image file.
note: added in v1.0.10

Args:
    override_window_size (Vector2D): Override size of the window.
    image_file_path (str): The output file path

Returns:
    str: ImageFilePath if succeed or Empty string

<a id="unreal.ChameleonData.snapshot_chameleon_window"></a>

#### snapshot\_chameleon\_window

```python
@classmethod
def snapshot_chameleon_window(cls,
                              tools_path: str,
                              override_window_size: Vector2D = [
                                  0.000000, 0.000000
                              ],
                              image_file_path: str = "") -> str
```

X.snapshot_chameleon_window(tools_path, override_window_size=[0.000000, 0.000000], image_file_path="") -> str
Snapshot the chameleon Window, and save it to an image file. This function can save the whole UI, even it is bigger than the screen. or in a ScrollBox
note: added in v1.0.8

Args:
    tools_path (str): The relative JSON path of Chameleon tool in Python folder.
    override_window_size (Vector2D): Override size of the window.
    image_file_path (str): The output file path

Returns:
    str: ImageFilePath if succeed or Empty string

<a id="unreal.ChameleonData.set_visibility"></a>

#### set\_visibility

```python
def set_visibility(aka_name: Name, visibility_str: str) -> bool
```

x.set_visibility(aka_name, visibility_str) -> bool
Set the widget's visibility

Args:
    aka_name (Name): The aka name of the widget
    visibility_str (str): The Options: "Visible"/"Collapsed"/"Hidden"/"HitTestInvisible"/"SelfHitTestInvisible"

Returns:
    bool:

<a id="unreal.ChameleonData.set_tree_view_items"></a>

#### set\_tree\_view\_items

```python
def set_tree_view_items(aka_name: Name, str_array: Array[str],
                        parent_indices: Array[int]) -> None
```

x.set_tree_view_items(aka_name, str_array, parent_indices) -> None
Set the source items of SListView.
note: Supported widgets: SListView.
note: "TreeItemParentIndices" : [-1, 0, 0, 2, 1, 1].
note: A
note: |─B
note: | └─E
note: | └─F
note: └─C
note: └─D

Args:
    aka_name (Name): The aka name of the widget
    str_array (Array[str]): Flatten list of items tree.
    parent_indices (Array[int32]): Each item's parent index

<a id="unreal.ChameleonData.set_tool_tip_text"></a>

#### set\_tool\_tip\_text

```python
def set_tool_tip_text(aka_name: Name, tool_tip_text: str) -> None
```

x.set_tool_tip_text(aka_name, tool_tip_text) -> None
Set the ToolTip Text of Widget
note: Supported widgets: SWidget.

Args:
    aka_name (Name): The aka name of the widget
    tool_tip_text (str): The Tool Tip Text.

<a id="unreal.ChameleonData.set_text_read_only"></a>

#### set\_text\_read\_only

```python
def set_text_read_only(aka_name: Name, read_only: bool) -> None
```

x.set_text_read_only(aka_name, read_only) -> None
Set the text of widget Read Only or not.
note: Supported widgets: SEditableText/SEditableTextBox/SMultiLineEditableText/SMultiLineEditableTextBox etc.

Args:
    aka_name (Name): The aka name of the widget
    read_only (bool): Is Read Only

<a id="unreal.ChameleonData.set_text"></a>

#### set\_text

```python
def set_text(aka_name: Name, text: str) -> None
```

x.set_text(aka_name, text) -> None
Set the text of widget:
note: Supported widgets: SEditableText/SEditableTextBox/SMultiLineEditableText/SMultiLineEditableTextBox/SButton etc.

Args:
    aka_name (Name): The aka name of the widget
    text (str): The text content.

<a id="unreal.ChameleonData.set_scroll_box_offset"></a>

#### set\_scroll\_box\_offset

```python
def set_scroll_box_offset(aka_name: Name, offset: float) -> bool
```

x.set_scroll_box_offset(aka_name, offset) -> bool
Set the Offset Text of ScrollBox
note: Supported widgets: SScrollBox.

Args:
    aka_name (Name): The aka name of the widget
    offset (float): The offset value of ScrollBox

Returns:
    bool:

<a id="unreal.ChameleonData.set_python_flag"></a>

#### set\_python\_flag

```python
@classmethod
def set_python_flag(cls, is_ready: bool) -> None
```

X.set_python_flag(is_ready) -> None
Set python is ready flag

Args:
    is_ready (bool): Is ready or not

<a id="unreal.ChameleonData.set_progress_bar_percent"></a>

#### set\_progress\_bar\_percent

```python
def set_progress_bar_percent(aka_name: Name, percent: float) -> None
```

x.set_progress_bar_percent(aka_name, percent) -> None
Set the Percent of SProgressBar
note: Supported widgets: SProgressBar.

Args:
    aka_name (Name): The aka name of the widget
    percent (float): The Percent value.

<a id="unreal.ChameleonData.set_object"></a>

#### set\_object

```python
def set_object(aka_name: Name, object: Object) -> None
```

x.set_object(aka_name, object) -> None
Set the showing object of SDetailsView
note: added in v1.0.9

Args:
    aka_name (Name): The aka name of the widget
    object (Object): The Object for SDetailsView

<a id="unreal.ChameleonData.set_min_aspect_ratio"></a>

#### set\_min\_aspect\_ratio

```python
def set_min_aspect_ratio(aka_name: Name, min_aspect_ratio: float) -> None
```

x.set_min_aspect_ratio(aka_name, min_aspect_ratio) -> None
Set the MinAspectRatio of SBox
note: Supported widgets: SBox.
note: added in v1.0.11

Args:
    aka_name (Name): The aka name of the widget
    min_aspect_ratio (float): The MinAspectRatio value.

<a id="unreal.ChameleonData.set_menu_item_can_execute"></a>

#### set\_menu\_item\_can\_execute

```python
@classmethod
def set_menu_item_can_execute(cls, id: int, can_execute: bool) -> None
```

X.set_menu_item_can_execute(id, can_execute) -> None
Set Menu Item executable.

Args:
    id (int32): 
    can_execute (bool):

<a id="unreal.ChameleonData.set_max_aspect_ratio"></a>

#### set\_max\_aspect\_ratio

```python
def set_max_aspect_ratio(aka_name: Name, max_aspect_ratio: float) -> None
```

x.set_max_aspect_ratio(aka_name, max_aspect_ratio) -> None
Set the MaxAspectRatio of SBox
note: Supported widgets: SBox.
note: added in v1.0.11

Args:
    aka_name (Name): The aka name of the widget
    max_aspect_ratio (float): The MaxAspectRatio value.

<a id="unreal.ChameleonData.set_list_view_selections"></a>

#### set\_list\_view\_selections

```python
def set_list_view_selections(aka_name: str, indexes: Array[int]) -> None
```

x.set_list_view_selections(aka_name, indexes) -> None
Set the selections of SListView.
note: Supported widgets: SListView.

Args:
    aka_name (str): The aka name of the widget
    indexes (Array[int32]): The indexes of selected items.

<a id="unreal.ChameleonData.set_list_view_multi_column_selections"></a>

#### set\_list\_view\_multi\_column\_selections

```python
def set_list_view_multi_column_selections(aka_name: Name,
                                          indexes: Array[int]) -> None
```

x.set_list_view_multi_column_selections(aka_name, indexes) -> None
Set the selections of SListView.
note: Supported widgets: SListView.

Args:
    aka_name (Name): The aka name of the widget
    indexes (Array[int32]): The indexes of selected items.

<a id="unreal.ChameleonData.set_list_view_multi_column_line"></a>

#### set\_list\_view\_multi\_column\_line

```python
def set_list_view_multi_column_line(aka_name: Name, line_index: int,
                                    line_content_array: Array[str],
                                    rebuild_list: bool) -> None
```

x.set_list_view_multi_column_line(aka_name, line_index, line_content_array, rebuild_list) -> None
Set one line items to specified MultiColumn SListView.
note: Supported widgets: SListView<MultiColumn>.

Args:
    aka_name (Name): The aka name of the widget
    line_index (int32): The index of line.
    line_content_array (Array[str]): The content of line.
    rebuild_list (bool): Rebuild the list or not.

<a id="unreal.ChameleonData.set_list_view_multi_column_items"></a>

#### set\_list\_view\_multi\_column\_items

```python
def set_list_view_multi_column_items(aka_name: Name,
                                     flattened_str_array: Array[str],
                                     column_count: int) -> None
```

x.set_list_view_multi_column_items(aka_name, flattened_str_array, column_count) -> None
Set the source items to specified MultiColumn SListView.
note: Supported widgets: SListView<MultiColumn>.

Args:
    aka_name (Name): The aka name of the widget
    flattened_str_array (Array[str]): The flatten items list for Multi column SListView.
    column_count (int32): The number of column.

<a id="unreal.ChameleonData.set_list_view_items"></a>

#### set\_list\_view\_items

```python
def set_list_view_items(aka_name: Name, str_array: Array[str]) -> None
```

x.set_list_view_items(aka_name, str_array) -> None
Set items for specified SListView.
note: Supported widgets: SListView.

Args:
    aka_name (Name): The aka name of the widget
    str_array (Array[str]): The list of items.

<a id="unreal.ChameleonData.set_is_expanded"></a>

#### set\_is\_expanded

```python
def set_is_expanded(aka_name: Name,
                    expanded: bool,
                    animated: bool = False) -> None
```

x.set_is_expanded(aka_name, expanded, animated=False) -> None
Set the Expanded state of Specified SExpandableArea
note: Supported widgets: SExpandableArea.
note: added in v1.0.4

Args:
    aka_name (Name): The aka name of the widget
    expanded (bool): Is Expanded or not.
    animated (bool): Expanded with animation or not.

<a id="unreal.ChameleonData.set_is_checked"></a>

#### set\_is\_checked

```python
def set_is_checked(aka_name: Name, checked: bool) -> None
```

x.set_is_checked(aka_name, checked) -> None
Set the Checked state of Specified SCheckBox
note: Supported widgets: SCheckBox.

Args:
    aka_name (Name): The aka name of the widget
    checked (bool): Is Checked or not.

<a id="unreal.ChameleonData.set_int_value"></a>

#### set\_int\_value

```python
def set_int_value(aka_name: Name, value: int) -> None
```

x.set_int_value(aka_name, value) -> None
Set integer value to widget: SSpinBox<int32>.
note: Supported widgets: SSpinBox<int32>.

Args:
    aka_name (Name): The aka name of the widget
    value (int32): The value to set.

<a id="unreal.ChameleonData.set_image_pixels"></a>

#### set\_image\_pixels

```python
def set_image_pixels(aka_name: Name, pixel_colors: Array[LinearColor],
                     width: int, height: int) -> None
```

x.set_image_pixels(aka_name, pixel_colors, width, height) -> None
Set SImage's Image content with Linear Colors.

Args:
    aka_name (Name): The aka name of the widget
    pixel_colors (Array[LinearColor]): The pixel list of image, len(PixelColors) == Height * Width
    width (int32): Width of Image.
    height (int32): Height of Image.

<a id="unreal.ChameleonData.set_image_from_path"></a>

#### set\_image\_from\_path

```python
def set_image_from_path(
        aka_name: Name,
        image_file_path: str,
        brush_width: int = 256,
        brush_height: int = 256,
        tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
        tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
```

x.set_image_from_path(aka_name, image_file_path, brush_width=256, brush_height=256, tint=[1.000000, 1.000000, 1.000000, 1.000000], tiling=SlateBrushTileType.NO_TILE) -> None
Set SImage's Image content from local path the resource folder of this plug-in.
note: The base folder is the Resources folder of this plug-in

Args:
    aka_name (Name): The aka name of the widget
    image_file_path (str): The absolute path of the image. If a relative path is provided, it is relative to the Resource directory in the Plugin directory.
    brush_width (int32): Brush's width.
    brush_height (int32): Brush's height.
    tint (LinearColor): The Tint of the image, default is White
    tiling (SlateBrushTileType): The Tiling of the image, default is NoTile

<a id="unreal.ChameleonData.set_image_from"></a>

#### set\_image\_from

```python
def set_image_from(
        aka_name: Name,
        image_file_path: str,
        brush_width: int = 256,
        brush_height: int = 256,
        tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
        tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
```

x.set_image_from(aka_name, image_file_path, brush_width=256, brush_height=256, tint=[1.000000, 1.000000, 1.000000, 1.000000], tiling=SlateBrushTileType.NO_TILE) -> None
Set SImage's Image content with Linear Colors.
note: If the ImageFilePath is a relative path, it will combined with the folder of chameleon tools's JSON path.

Args:
    aka_name (Name): The aka name of the widget
    image_file_path (str): The image path in resource folder.
    brush_width (int32): Brush's width.
    brush_height (int32): Brush's height.
    tint (LinearColor): The Tint of the image, default is White
    tiling (SlateBrushTileType): The Tiling of the image, default is NoTile

<a id="unreal.ChameleonData.set_image_data_from_texture2d"></a>

#### set\_image\_data\_from\_texture2d

```python
def set_image_data_from_texture2d(
        aka_name: Name,
        texture2d: Texture2D,
        mip_level: int = 0,
        ignore_alpha: bool = False,
        tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
        tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> bool
```

x.set_image_data_from_texture2d(aka_name, texture2d, mip_level=0, ignore_alpha=False, tint=[1.000000, 1.000000, 1.000000, 1.000000], tiling=SlateBrushTileType.NO_TILE) -> bool
Set SImage's Image content with Texture2D.

Args:
    aka_name (Name): The aka name of the widget
    texture2d (Texture2D): The source Texture2D
    mip_level (int32): The MipLevel of the image
    ignore_alpha (bool): Ignore the alpha channel or not.
    tint (LinearColor): The Tint of the image, default is White
    tiling (SlateBrushTileType): The Tiling of the image, default is NoTile

Returns:
    bool:

<a id="unreal.ChameleonData.set_image_data_from_memory"></a>

#### set\_image\_data\_from\_memory

```python
def set_image_data_from_memory(
        aka_name: Name,
        address: int,
        length: int,
        width: int,
        height: int,
        channel_num: int = 4,
        bgr: bool = True,
        tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
        tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
```

x.set_image_data_from_memory(aka_name, address, length, width, height, channel_num=4, bgr=True, tint=[1.000000, 1.000000, 1.000000, 1.000000], tiling=SlateBrushTileType.NO_TILE) -> None
Set SImage's Image content with memory address.

Args:
    aka_name (Name): The aka name of the widget
    address (int64): The memory address of the image.
    length (int64): The length of the image.
    width (int32): Width of Image.
    height (int32): Height of Image.
    channel_num (int32): Channel number of the RawData
    bgr (bool): Is the image channel order is Blue, Green, Red, (Alpha) or RGB(A)
    tint (LinearColor): The Tint of the image, default is White
    tiling (SlateBrushTileType): The Tiling of the image, default is NoTile

<a id="unreal.ChameleonData.set_image_data_base64"></a>

#### set\_image\_data\_base64

```python
def set_image_data_base64(
        aka_name: Name,
        base64_string: str,
        width: int,
        height: int,
        channel_num: int = 4,
        bgr: bool = True,
        tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
        tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
```

x.set_image_data_base64(aka_name, base64_string, width, height, channel_num=4, bgr=True, tint=[1.000000, 1.000000, 1.000000, 1.000000], tiling=SlateBrushTileType.NO_TILE) -> None
Set SImage's Image content with Base64 string.

Args:
    aka_name (Name): The aka name of the widget
    base64_string (str): The Base64 string of the image.
    width (int32): Width of Image.
    height (int32): Height of Image.
    channel_num (int32): Channel number of the image
    bgr (bool): Is the image channel order is Blue, Green, Red, (Alpha) or RGB(A)
    tint (LinearColor): The Tint of the image, default is White
    tiling (SlateBrushTileType): The Tiling of the image, default is NoTile

<a id="unreal.ChameleonData.set_image_data"></a>

#### set\_image\_data

```python
def set_image_data(
        aka_name: Name,
        raw_data: Array[int],
        width: int,
        height: int,
        channel_num: int = 4,
        bgr: bool = True,
        tint: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
        tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE) -> None
```

x.set_image_data(aka_name, raw_data, width, height, channel_num=4, bgr=True, tint=[1.000000, 1.000000, 1.000000, 1.000000], tiling=SlateBrushTileType.NO_TILE) -> None
Set SImage's Image content with Raw data.(R, G, B, A：uint8)
note: Add zlib compressed data support in v1.2.0
note: The order of RawData is row first. Upper left corner is the first pixel, and lower right is the last. Which is different with RenderTexture2D

Args:
    aka_name (Name): The aka name of the widget
    raw_data (Array[uint8]): The flatten raw data of image, len(RawDataIn) == Height * Width * ChannelNum, Or use the zlib compressed data of the image
    width (int32): Width of Image.
    height (int32): Height of Image.
    channel_num (int32): Channel number of the RawData
    bgr (bool): Is the RawData Channel Order is Blue, Green, Red, (Alpha) or RGB(A)
    tint (LinearColor): The Tint of the image, default is White
    tiling (SlateBrushTileType): The Tiling of the image, default is NoTile

<a id="unreal.ChameleonData.set_grid_panel_column_fill"></a>

#### set\_grid\_panel\_column\_fill

```python
def set_grid_panel_column_fill(aka_name: Name, index: int,
                               value: float) -> None
```

x.set_grid_panel_column_fill(aka_name, index, value) -> None
Set the ColumnFill value of SGridPanel.
note: Supported widgets: SGridPanel.

Args:
    aka_name (Name): The aka name of the widget
    index (int32): The index of column.
    value (float): The column fill value.

<a id="unreal.ChameleonData.set_graph_panel_content_from_json"></a>

#### set\_graph\_panel\_content\_from\_json

```python
def set_graph_panel_content_from_json(aka_name: Name,
                                      json_content: str) -> bool
```

x.set_graph_panel_content_from_json(aka_name, json_content) -> bool
Set the content of SGraphPanel from JSON string.
note: add in v1.2.0

Args:
    aka_name (Name): The aka name of the SGraphPanel
    json_content (str): The JSON string content of the SGraphPanel.

Returns:
    bool: succeed or not

<a id="unreal.ChameleonData.set_float_value"></a>

#### set\_float\_value

```python
def set_float_value(aka_name: Name, value: float) -> None
```

x.set_float_value(aka_name, value) -> None
Set integer value to widget: SSpinBox<float>.
note: Supported widgets: SSpinBox<float>.

Args:
    aka_name (Name): The aka name of the widget
    value (float): The value to set.

<a id="unreal.ChameleonData.set_dpi_scale"></a>

#### set\_dpi\_scale

```python
def set_dpi_scale(aka_name: Name, value: float) -> bool
```

x.set_dpi_scale(aka_name, value) -> bool
Set the DPI scale value of SDPIScaler
note: Supported widgets: SDPIScaler.

Args:
    aka_name (Name): The aka name of the widget
    value (float): The value of DPI scale.

Returns:
    bool:

<a id="unreal.ChameleonData.set_desired_size_override"></a>

#### set\_desired\_size\_override

```python
def set_desired_size_override(aka_name: Name,
                              desired_size_override: Vector2D) -> None
```

x.set_desired_size_override(aka_name, desired_size_override) -> None
Set SImage's Brush Size.
note: "DesiredSizeOverride" is alias of "BrushSize", "BrushSize" is deprecated

Args:
    aka_name (Name): The aka name of the widget
    desired_size_override (Vector2D): The desired size of the image brush.

<a id="unreal.ChameleonData.set_content_from_json"></a>

#### set\_content\_from\_json

```python
def set_content_from_json(aka_name: Name, json_content: str) -> bool
```

x.set_content_from_json(aka_name, json_content) -> bool
Set sub widget through the content of the JSON string. It's for the widget which has only one child.
note: add in v1.1
note: Supported widgets: 'SBox', 'SBorder', 'SCheckBox', 'SBox' and 'SButton'.

Args:
    aka_name (Name): The aka name of the Parent widget
    json_content (str): The JSON string content of the new widget.

Returns:
    bool: succeed or not

<a id="unreal.ChameleonData.set_combo_box_selected_item"></a>

#### set\_combo\_box\_selected\_item

```python
def set_combo_box_selected_item(aka_name: Name, index: int) -> bool
```

x.set_combo_box_selected_item(aka_name, index) -> bool
Set the selection of SComboBox.
note: Supported widgets: SComboBox.

Args:
    aka_name (Name): The aka name of the widget
    index (int32): The index of item for select.

Returns:
    bool:

<a id="unreal.ChameleonData.set_combo_box_items"></a>

#### set\_combo\_box\_items

```python
def set_combo_box_items(aka_name: Name, str_array: Array[str]) -> bool
```

x.set_combo_box_items(aka_name, str_array) -> bool
Set SComboBox's content list.
note: Supported widgets: SComboBox.

Args:
    aka_name (Name): The aka name of the widget
    str_array (Array[str]): The string list for SComboBox's content.

Returns:
    bool:

<a id="unreal.ChameleonData.set_column_lable"></a>

#### set\_column\_lable

```python
def set_column_lable(aka_name: Name, index: int, label: str) -> None
```

x.set_column_lable(aka_name, index, label) -> None
Set the label of SHeaderRow
note: Supported widgets: SHeaderRow.

Args:
    aka_name (Name): The aka name of the widget
    index (int32): The index of HeaderRow.
    label (str): The Label of column.

<a id="unreal.ChameleonData.set_color_and_opacity"></a>

#### set\_color\_and\_opacity

```python
def set_color_and_opacity(aka_name: Name, color: LinearColor) -> None
```

x.set_color_and_opacity(aka_name, color) -> None
Set widget's color and opacity.
note: Supported widgets: SButton, SImage, STextBlock, SEditableText and other 18 SCompoundWidgetNames

Args:
    aka_name (Name): The aka name of the widget
    color (LinearColor): The FLinear Color value.

<a id="unreal.ChameleonData.set_color"></a>

#### set\_color

```python
def set_color(aka_name: Name, color: LinearColor) -> bool
```

x.set_color(aka_name, color) -> bool
Set color of the specified SColorBlock Widget
note: Supported widgets: SColorBlock
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SColorBlock widget
    color (LinearColor): New Color.

Returns:
    bool:

<a id="unreal.ChameleonData.set_collapsed"></a>

#### set\_collapsed

```python
def set_collapsed(aka_name: Name, collapsed: bool) -> None
```

x.set_collapsed(aka_name, collapsed) -> None
Set the widget's visibility collapsed or not.

Args:
    aka_name (Name): The aka name of the widget
    collapsed (bool): Collapsed or not, True for EVisibility::Collapsed, False for EVisibility::Visible

<a id="unreal.ChameleonData.set_chameleon_window_size"></a>

#### set\_chameleon\_window\_size

```python
@classmethod
def set_chameleon_window_size(cls, tools_path: str,
                              new_size: Vector2D) -> bool
```

X.set_chameleon_window_size(tools_path, new_size) -> bool
Set the window size of the Chameleon Tool
note: added in v1.0.8

Args:
    tools_path (str): The relative JSON path of Chameleon tool in Python folder. For instance, the gallery tool's path is "ChameleonGallery/ChameleonGallery.json"
    new_size (Vector2D): The new size of window

Returns:
    bool: True if succeed

<a id="unreal.ChameleonData.set_chameleon_window_position"></a>

#### set\_chameleon\_window\_position

```python
@classmethod
def set_chameleon_window_position(cls, tools_path: str,
                                  new_position: Vector2D) -> bool
```

X.set_chameleon_window_position(tools_path, new_position) -> bool
Set the window position of the Chameleon Tool
note: added in v1.0.8

Args:
    tools_path (str): The relative JSON path of Chameleon tool in Python folder. For instance, the gallary tool's path is "ChameleonGallery/ChameleonGallery.json"
    new_position (Vector2D): 

Returns:
    bool: True if succeed

<a id="unreal.ChameleonData.set_button_color_and_opacity"></a>

#### set\_button\_color\_and\_opacity

```python
def set_button_color_and_opacity(aka_name: Name, color: LinearColor) -> None
```

x.set_button_color_and_opacity(aka_name, color) -> None
Set SButton's color and opacity.
note: Supported widgets: SButton.

Args:
    aka_name (Name): The aka name of the widget
    color (LinearColor): The FLinear Color value.

<a id="unreal.ChameleonData.scroll_to"></a>

#### scroll\_to

```python
def scroll_to(aka_name: Name, line_index: int = 0, offset: int = 0) -> bool
```

x.scroll_to(aka_name, line_index=0, offset=0) -> bool
Scroll to the Line Inex in SMultiLineEditableTextBox widget
note: Supported widgets: SMultiLineEditableTextBox.

Args:
    aka_name (Name): The aka name of the widget
    line_index (int32): LineIndex of TextLocation, max index is line count-1.  Scroll to end of document if LineIndex == -1
    offset (int32): Offset of TextLocation

Returns:
    bool:

<a id="unreal.ChameleonData.request_close_modal_window"></a>

#### request\_close\_modal\_window

```python
@classmethod
def request_close_modal_window(cls, tools_path: str) -> bool
```

X.request_close_modal_window(tools_path) -> bool
Request close specified Modal Window.

Args:
    tools_path (str): The JSON path of Modal window.

Returns:
    bool: succeed or not

<a id="unreal.ChameleonData.request_close"></a>

#### request\_close

```python
@classmethod
def request_close(cls, tools_path: str = "") -> bool
```

X.request_close(tools_path="") -> bool
Request close specified chameleon tools.

Args:
    tools_path (str): The JSON path of Chameleon tool.

Returns:
    bool: succeed or not

<a id="unreal.ChameleonData.remove_widget_at"></a>

#### remove\_widget\_at

```python
def remove_widget_at(aka_name: Name, index: int) -> bool
```

x.remove_widget_at(aka_name, index) -> bool
Remove a child widget at Specified slot or widget.
note: add in v1.1
note: Supported widgets: 'SHorizontalBox', 'SVerticalBox', 'SScrollBox', 'SGridPanel', 'SUniformGridPanel', 'SUniformWrapPanel', 'SOverlay', 'SCanvas', 'SSplitter' 'SBox', 'SBorder', 'SCheckBox', 'SBox' and 'SButton'.

Args:
    aka_name (Name): The aka name of the Parent widget
    index (int32): The slot index of the new widget, and will be ignored with 'SBox', 'SBorder', 'SCheckBox', 'SBox' and 'SButton'.

Returns:
    bool: succeed or not

<a id="unreal.ChameleonData.reload_page"></a>

#### reload\_page

```python
def reload_page(aka_name: Name) -> None
```

x.reload_page(aka_name) -> None
Reload the current page in SWebBrowser.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

<a id="unreal.ChameleonData.push_breadcrumb_string"></a>

#### push\_breadcrumb\_string

```python
def push_breadcrumb_string(aka_name: Name, crumb_text: str,
                           new_crumb_data: str) -> None
```

x.push_breadcrumb_string(aka_name, crumb_text, new_crumb_data) -> None
Set item to SBreadcrumbTrail.
note: Supported widgets: SBreadcrumbTrail.

Args:
    aka_name (Name): The aka name of the widget
    crumb_text (str): New item for display .
    new_crumb_data (str): New item for push.

<a id="unreal.ChameleonData.pop_breadcrumb_string"></a>

#### pop\_breadcrumb\_string

```python
def pop_breadcrumb_string(aka_name: Name) -> str
```

x.pop_breadcrumb_string(aka_name) -> str
Pop a item from SBreadcrumbTrail.
note: Supported widgets: SBreadcrumbTrail.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    str: The Popped item.

<a id="unreal.ChameleonData.modal_window"></a>

#### modal\_window

```python
@classmethod
def modal_window(cls, tools_path: str) -> bool
```

X.modal_window(tools_path) -> bool
Launch specified Modal window tools.

Args:
    tools_path (str): The JSON path of Modal window.

Returns:
    bool: succeed or not

<a id="unreal.ChameleonData.log_all_saved_detail_customization"></a>

#### log\_all\_saved\_detail\_customization

```python
@classmethod
def log_all_saved_detail_customization(cls) -> None
```

X.log_all_saved_detail_customization() -> None
Log all saved DetailCustomization
note: added in v1.2.3

<a id="unreal.ChameleonData.load_url"></a>

#### load\_url

```python
def load_url(aka_name: Name, new_url: str) -> None
```

x.load_url(aka_name, new_url) -> None
Load the specified URL in SWebBrowser widget.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget
    new_url (str): New URL to load.

<a id="unreal.ChameleonData.load_page_from_string"></a>

#### load\_page\_from\_string

```python
def load_page_from_string(aka_name: Name, contents: str,
                          dummy_url: str) -> None
```

x.load_page_from_string(aka_name, contents, dummy_url) -> None
Load a string as data to create a web page in SWebBrowser widget.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget
    contents (str): String to load.
    dummy_url (str): Dummy URL for the page.

<a id="unreal.ChameleonData.launch_chameleon_tool"></a>

#### launch\_chameleon\_tool

```python
@classmethod
def launch_chameleon_tool(cls, tools_path: str = "") -> bool
```

X.launch_chameleon_tool(tools_path="") -> bool
Launch specified chameleon tools.

Args:
    tools_path (str): The JSON path of Chameleon tool.

Returns:
    bool: succeed or not

<a id="unreal.ChameleonData.is_page_loading"></a>

#### is\_page\_loading

```python
def is_page_loading(aka_name: Name) -> bool
```

x.is_page_loading(aka_name) -> bool
Whether the document is currently being loaded.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

Returns:
    bool:

<a id="unreal.ChameleonData.is_page_loaded"></a>

#### is\_page\_loaded

```python
def is_page_loaded(aka_name: Name) -> bool
```

x.is_page_loaded(aka_name) -> bool
Whether the document finished loading.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

Returns:
    bool:

<a id="unreal.ChameleonData.insert_slot_from_json"></a>

#### insert\_slot\_from\_json

```python
def insert_slot_from_json(aka_name: Name, json_content: str,
                          index: int) -> bool
```

x.insert_slot_from_json(aka_name, json_content, index) -> bool
Add a child widget at Specified slot through the content of the JSON string.
note: add in v1.1
note: Supported widgets: 'SHorizontalBox', 'SVerticalBox'.

Args:
    aka_name (Name): The aka name of the Parent widget
    json_content (str): The JSON string content of the new widget.
    index (int32): The slot index of the new widget

Returns:
    bool: succeed or not

<a id="unreal.ChameleonData.hatch_egg"></a>

#### hatch\_egg

```python
@classmethod
def hatch_egg(cls, object: Object) -> bool
```

X.hatch_egg(object) -> bool
Hatch Egg

Args:
    object (Object): 

Returns:
    bool:

<a id="unreal.ChameleonData.go_forward"></a>

#### go\_forward

```python
def go_forward(aka_name: Name) -> None
```

x.go_forward(aka_name) -> None
Navigate forwards..
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

<a id="unreal.ChameleonData.go_back"></a>

#### go\_back

```python
def go_back(aka_name: Name) -> None
```

x.go_back(aka_name) -> None
Navigate backwards.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

<a id="unreal.ChameleonData.get_widget_path_from_aka"></a>

#### get\_widget\_path\_from\_aka

```python
def get_widget_path_from_aka(aka_name: Name) -> str
```

x.get_widget_path_from_aka(aka_name) -> str
Return the current widget path of the named widget.
note: The path will change if the add or remove widget dynamically.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    str: Current widget path of the named widget.

<a id="unreal.ChameleonData.get_widget_path"></a>

#### get\_widget\_path

```python
def get_widget_path(aka_name: Name) -> str
```

x.get_widget_path(aka_name) -> str
Get the Slate path of widget.
note: add in v1.1

Args:
    aka_name (Name): The aka name of the widget

Returns:
    str: the full path of the widget

<a id="unreal.ChameleonData.get_visibility"></a>

#### get\_visibility

```python
def get_visibility(aka_name: Name) -> str
```

x.get_visibility(aka_name) -> str
Get the widget's visibility

Args:
    aka_name (Name): The aka name of the widget

Returns:
    str: The visibility of the named widget in string

<a id="unreal.ChameleonData.get_url"></a>

#### get\_url

```python
def get_url(aka_name: Name) -> str
```

x.get_url(aka_name) -> str
Gets the currently loaded URL.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

Returns:
    str: The URL, or empty string if no document is loaded.

<a id="unreal.ChameleonData.get_tree_view_items"></a>

#### get\_tree\_view\_items

```python
def get_tree_view_items(
        aka_name: Name) -> Optional[Tuple[Array[str], Array[int]]]
```

x.get_tree_view_items(aka_name) -> (out_str_array=Array[str], out_item_stats=Array[int32]) or None
Set the source items of SListView.
note: Supported widgets: SListView.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    tuple or None: 

    out_str_array (Array[str]): Flatten list of items tree.

    out_item_stats (Array[int32]): Each item's selection status.

<a id="unreal.ChameleonData.get_top_scroll_box_offsets"></a>

#### get\_top\_scroll\_box\_offsets

```python
def get_top_scroll_box_offsets(tools_path: str) -> Map[str, float]
```

x.get_top_scroll_box_offsets(tools_path) -> Map[str, float]
Get the  Offset, ScrollOffsetOfEnd, ViewFraction, ViewOffsetFraction values in Map from the top ScrollBox of Chameleon Tool
note: added in v1.0.11

Args:
    tools_path (str): The relative JSON path of Chameleon tool in Python folder. For instance, the gallery tool's path is "ChameleonGallery/ChameleonGallery.json"

Returns:
    Map[str, float]: Offset, ScrollOffsetOfEnd, ViewFraction, ViewOffsetFraction values in Map.

<a id="unreal.ChameleonData.get_title_text_of_page"></a>

#### get\_title\_text\_of\_page

```python
def get_title_text_of_page(aka_name: Name) -> str
```

x.get_title_text_of_page(aka_name) -> str
Get the current title of the web page.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

Returns:
    str:

<a id="unreal.ChameleonData.get_text"></a>

#### get\_text

```python
def get_text(aka_name: Name) -> Optional[str]
```

x.get_text(aka_name) -> str or None
Get the text of widget.
note: Supported widgets: SEditableText/SEditableTextBox/SMultiLineEditableText/SMultiLineEditableTextBox etc.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    str or None: 

    out_text (str):

<a id="unreal.ChameleonData.get_scroll_box_offsets"></a>

#### get\_scroll\_box\_offsets

```python
def get_scroll_box_offsets(aka_name: Name) -> Map[str, float]
```

x.get_scroll_box_offsets(aka_name) -> Map[str, float]
Get the Offset, ScrollOffsetOfEnd, ViewFraction, ViewOffsetFraction values in Map.
note: Supported widgets: SScrollBox.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    Map[str, float]:

<a id="unreal.ChameleonData.get_python_flag"></a>

#### get\_python\_flag

```python
@classmethod
def get_python_flag(cls) -> bool
```

X.get_python_flag() -> bool
Get python is ready flag

Returns:
    bool: Is ready or not

<a id="unreal.ChameleonData.get_list_view_multi_column_selection"></a>

#### get\_list\_view\_multi\_column\_selection

```python
def get_list_view_multi_column_selection(
        aka_name: Name) -> Optional[Array[int]]
```

x.get_list_view_multi_column_selection(aka_name) -> Array[int32] or None
Get the selected indices of Slistview.
note: Supported widgets: SListView<MultiColumn>.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    Array[int32] or None: The selected indices of Slistview, Array[int32] or None

    out_selected_indices (Array[int32]):

<a id="unreal.ChameleonData.get_list_view_multi_column_items"></a>

#### get\_list\_view\_multi\_column\_items

```python
def get_list_view_multi_column_items(aka_name: Name) -> Tuple[Array[str], int]
```

x.get_list_view_multi_column_items(aka_name) -> (out_str_array=Array[str], column_count=int32)
Get the source items from specified MultiColumn SListView.
note: Supported widgets: SListView<MultiColumn>.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    tuple: 

    out_str_array (Array[str]): The flatten items list from Multi column SListView.

    column_count (int32): The number of column.

<a id="unreal.ChameleonData.get_list_view_items"></a>

#### get\_list\_view\_items

```python
def get_list_view_items(aka_name: Name) -> Tuple[Array[str], Array[int]]
```

x.get_list_view_items(aka_name) -> (out_str_array=Array[str], out_item_stats=Array[int32])
Get items from specified SListView.
note: Supported widgets: SListView.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    tuple: 

    out_str_array (Array[str]): The items source of SListView.

    out_item_stats (Array[int32]): The selection status of each items. (1 for selected)

<a id="unreal.ChameleonData.get_is_expanded"></a>

#### get\_is\_expanded

```python
def get_is_expanded(aka_name: Name) -> bool
```

x.get_is_expanded(aka_name) -> bool
Get the Expanded state of Specified SExpandableArea
note: Supported widgets: SExpandableArea.
note: added in v1.0.4

Args:
    aka_name (Name): The aka name of the widget

Returns:
    bool: Is Expanded or not.

<a id="unreal.ChameleonData.get_is_checked"></a>

#### get\_is\_checked

```python
def get_is_checked(aka_name: Name) -> bool
```

x.get_is_checked(aka_name) -> bool
Get the Checked state of Specified SCheckBox
note: Supported widgets: SCheckBox.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    bool: Is Checked or not.`

<a id="unreal.ChameleonData.get_int_value"></a>

#### get\_int\_value

```python
def get_int_value(aka_name: Name) -> Optional[int]
```

x.get_int_value(aka_name) -> int32 or None
Get integer value from widget: SSpinBox<int32>.
note: Supported widgets: SSpinBox<int32>.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    int32 or None: The integer value of SSpinBox

    out_text (int32):

<a id="unreal.ChameleonData.get_graph_selected_node"></a>

#### get\_graph\_selected\_node

```python
def get_graph_selected_node(aka_name: Name) -> Array[EdGraphNode]
```

x.get_graph_selected_node(aka_name) -> Array[EdGraphNode]
Get the selected nodes in SGraphPanel.
note: add in v1.2.0(Experimental)

Args:
    aka_name (Name): The aka name of the SGraphPanel

Returns:
    Array[EdGraphNode]: the array of selected nodes

<a id="unreal.ChameleonData.get_graph_panel_nodes"></a>

#### get\_graph\_panel\_nodes

```python
def get_graph_panel_nodes(aka_name: Name) -> Array[EdGraphNode]
```

x.get_graph_panel_nodes(aka_name) -> Array[EdGraphNode]
Get all nodes in SGraphPanel.
note: add in v1.2.0(Experimental)

Args:
    aka_name (Name): The aka name of the SGraphPanel

Returns:
    Array[EdGraphNode]: the array of nodes

<a id="unreal.ChameleonData.get_graph_panel_content_as_json"></a>

#### get\_graph\_panel\_content\_as\_json

```python
def get_graph_panel_content_as_json(aka_name: Name) -> str
```

x.get_graph_panel_content_as_json(aka_name) -> str
Get the content of SGraphPanel as JSON string.
note: add in v1.2.0(Experimental)

Args:
    aka_name (Name): The aka name of the SGraphPanel

Returns:
    str: the JSON string of the SGraphPanel

<a id="unreal.ChameleonData.get_float_value"></a>

#### get\_float\_value

```python
def get_float_value(aka_name: Name) -> Optional[float]
```

x.get_float_value(aka_name) -> float or None
Get integer value from widget: SSpinBox<int32>.
note: Supported widgets: SSpinBox<float>.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    float or None: The float value of SSpinBox

    out_text (float):

<a id="unreal.ChameleonData.get_detail_panel_customized_class_names"></a>

#### get\_detail\_panel\_customized\_class\_names

```python
@classmethod
def get_detail_panel_customized_class_names(cls) -> Array[Name]
```

X.get_detail_panel_customized_class_names() -> Array[Name]
UFUNCTION(BlueprintCallable, meta = (Keywords = "Python Editor"), Category = "PythonEditor")
static UWorld* GetWorldFromEgg(FString JsonPath);

Returns:
    Array[Name]:

<a id="unreal.ChameleonData.get_customized_object"></a>

#### get\_customized\_object

```python
@classmethod
def get_customized_object(cls, unique_id: int) -> Object
```

X.get_customized_object(unique_id) -> Object
Get CustomizedObject by UniqueID
note: added in v1.2.3

Args:
    unique_id (int32): The UniqueID of the object

Returns:
    Object: The CustomizedObject

<a id="unreal.ChameleonData.get_context_strings"></a>

#### get\_context\_strings

```python
def get_context_strings() -> str
```

x.get_context_strings() -> str
Get Context Strings

Returns:
    str:

<a id="unreal.ChameleonData.get_combo_box_selected_item"></a>

#### get\_combo\_box\_selected\_item

```python
def get_combo_box_selected_item(aka_name: Name) -> Optional[str]
```

x.get_combo_box_selected_item(aka_name) -> str or None
Get the selection of SComboBox.
note: Supported widgets: SComboBox.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    str or None: 

    out_item (str): The current selection of SComboBox.

<a id="unreal.ChameleonData.get_combo_box_items"></a>

#### get\_combo\_box\_items

```python
def get_combo_box_items(aka_name: Name) -> Optional[Array[str]]
```

x.get_combo_box_items(aka_name) -> Array[str] or None
Get SComboBox's content list.
note: Supported widgets: SComboBox.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    Array[str] or None: 

    out_str_array (Array[str]): The string list for SComboBox's content.

<a id="unreal.ChameleonData.get_chameleon_window_size"></a>

#### get\_chameleon\_window\_size

```python
@classmethod
def get_chameleon_window_size(cls,
                              tools_path: str,
                              client_size_in_screen: bool = False) -> Vector2D
```

X.get_chameleon_window_size(tools_path, client_size_in_screen=False) -> Vector2D
Get the window size of the Chameleon Tool
note: added in v1.0.8

Args:
    tools_path (str): The relative JSON path of Chameleon tool in Python folder. For instance, the gallery tool's path is "ChameleonGallery/ChameleonGallery.json"
    client_size_in_screen (bool): Get ClientSize or not

Returns:
    Vector2D: The  size of window

<a id="unreal.ChameleonData.get_chameleon_window_position"></a>

#### get\_chameleon\_window\_position

```python
@classmethod
def get_chameleon_window_position(cls, tools_path: str) -> Vector2D
```

X.get_chameleon_window_position(tools_path) -> Vector2D
Get the window position of the Chameleon Tool
note: added in v1.0.8

Args:
    tools_path (str): The relative JSON path of Chameleon tool in Python folder.

Returns:
    Vector2D: The position of window

<a id="unreal.ChameleonData.get_chameleon_desired_size"></a>

#### get\_chameleon\_desired\_size

```python
@classmethod
def get_chameleon_desired_size(cls, tools_path: str) -> Vector2D
```

X.get_chameleon_desired_size(tools_path) -> Vector2D
Get the desired size of the Chameleon Tool
note: added in v1.2.1

Args:
    tools_path (str): The relative JSON path of Chameleon tool in Python folder. For instance, the gallery tool's path is "ChameleonGallery/ChameleonGallery.json"

Returns:
    Vector2D: The desired size of window

<a id="unreal.ChameleonData.get_breadcrumbs_count_string"></a>

#### get\_breadcrumbs\_count\_string

```python
def get_breadcrumbs_count_string(aka_name: Name) -> int
```

x.get_breadcrumbs_count_string(aka_name) -> int32
Get items's count from SBreadcrumbTrail.
note: Supported widgets: SBreadcrumbTrail.

Args:
    aka_name (Name): The aka name of the widget

Returns:
    int32: The number of crumbs.

<a id="unreal.ChameleonData.get_all_widgets_paths"></a>

#### get\_all\_widgets\_paths

```python
def get_all_widgets_paths() -> Array[str]
```

x.get_all_widgets_paths() -> Array[str]
Get all widgets' paths in the current tool.

Returns:
    Array[str]: the array of widget paths

<a id="unreal.ChameleonData.get_all_akas"></a>

#### get\_all\_akas

```python
def get_all_akas() -> Array[str]
```

x.get_all_akas() -> Array[str]
Get the Slate path of widget.
note: add in v1.1

Returns:
    Array[str]: the full path of the widget

<a id="unreal.ChameleonData.flash_chameleon_window"></a>

#### flash\_chameleon\_window

```python
@classmethod
def flash_chameleon_window(cls, tools_path: str) -> bool
```

X.flash_chameleon_window(tools_path) -> bool
Flash the  Chameleon Tool
note: added in v1.0.8

Args:
    tools_path (str): The relative JSON path of Chameleon tool in Python folder.

Returns:
    bool: The position of window

<a id="unreal.ChameleonData.clear_graph_panel"></a>

#### clear\_graph\_panel

```python
def clear_graph_panel(aka_name: Name) -> int
```

x.clear_graph_panel(aka_name) -> int32
Clear all nodes in SGraphPanel.
note: add in v1.2.0(Experimental)

Args:
    aka_name (Name): The aka name of the SGraphPanel

Returns:
    int32: the number of nodes cleared

<a id="unreal.ChameleonData.clear_detail_customization"></a>

#### clear\_detail\_customization

```python
@classmethod
def clear_detail_customization(cls) -> None
```

X.clear_detail_customization() -> None
Clear all DetailCustomization.
note: added in v1.2.3

<a id="unreal.ChameleonData.clear_breadcrumbs_string"></a>

#### clear\_breadcrumbs\_string

```python
def clear_breadcrumbs_string(aka_name: Name,
                             pop_all_crumbs_to_clear: bool = False) -> None
```

x.clear_breadcrumbs_string(aka_name, pop_all_crumbs_to_clear=False) -> None
Clear all items from SBreadcrumbTrail.
note: Supported widgets: SBreadcrumbTrail.

Args:
    aka_name (Name): The aka name of the widget
    pop_all_crumbs_to_clear (bool): Pop All Crumbs or not.

<a id="unreal.ChameleonData.can_go_forward"></a>

#### can\_go\_forward

```python
def can_go_forward(aka_name: Name) -> bool
```

x.can_go_forward(aka_name) -> bool
Returns true if the browser can navigate forwards.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

Returns:
    bool:

<a id="unreal.ChameleonData.can_go_back"></a>

#### can\_go\_back

```python
def can_go_back(aka_name: Name) -> bool
```

x.can_go_back(aka_name) -> bool
Returns true if the browser can navigate backwards.
note: Supported widgets: SWebBrowser only
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget

Returns:
    bool:

<a id="unreal.ChameleonData.bind_uobject_to_browser"></a>

#### bind\_uobject\_to\_browser

```python
def bind_uobject_to_browser(aka_name: Name,
                            name: str,
                            object: Object,
                            is_permanent: bool = True) -> None
```

x.bind_uobject_to_browser(aka_name, name, object, is_permanent=True) -> None
Expose a UObject instance to the browser runtime. Properties and Functions will be accessible from JavaScript side.
note: Supported widgets: SWebBrowser only. When I get the property value from the Java script Promise object, the values are always empty, it's weird.
note: added in v1.0.10

Args:
    aka_name (Name): The aka name of the SWebBrowser widget
    name (str): The name of the object.The object will show up as window.ue.{Name} on the Java script side.Note: All object names, function names, and property names will be converted to lower case when bound on the javascript side.If there is an existing object of the same name, this object will replace it.If bIsPermanent is false and there is an existing permanent binding, the permanent binding will be restored when the temporary one is removed.
    object (Object): The object instance.
    is_permanent (bool): If true, the object will be visible to all pages loaded through this browser widget, otherwise, it will be deleted when navigating away from the current page.Non - permanent bindings should be registered from inside an OnLoadStarted event handler in order to be available before JS code starts loading.

<a id="unreal.ChameleonData.append_slot_from_json"></a>

#### append\_slot\_from\_json

```python
def append_slot_from_json(aka_name: Name,
                          json_content: str,
                          column: int = -1,
                          row: int = -1) -> bool
```

x.append_slot_from_json(aka_name, json_content, column=-1, row=-1) -> bool
Add a child widget through the content of the JSON string. It's for the widget which has 'Slots'.
note: add in v1.1
note: Supported widgets: 'SHorizontalBox', 'SVerticalBox', 'SScrollBox', 'SGridPanel', 'SUniformGridPanel', 'SUniformWrapPanel', 'SOverlay', 'SCanvas', 'SSplitter'.

Args:
    aka_name (Name): The aka name of the Parent widget
    json_content (str): The JSON string content of the new widget.
    column (int32): The index of the column in Grid widget. It's for 'SGridPanel' and 'SUniformGridPanel', and will be ignored in others.
    row (int32): The index of the Row in Grid widget. It's for 'SGridPanel' and 'SUniformGridPanel', and will be ignored in others.

Returns:
    bool: succeed or not

<a id="unreal.ChameleonData.add_detail_customization"></a>

#### add\_detail\_customization

```python
@classmethod
def add_detail_customization(cls, object: Object, tools_path: str) -> bool
```

X.add_detail_customization(object, tools_path) -> bool
Add DetailCustomization for specified object.
note: added in v1.2.3

Args:
    object (Object): The object to add DetailCustomization.
    tools_path (str): The JSON path of Chameleon tool.

Returns:
    bool:

<a id="unreal.ChameleonData.add_column"></a>

#### add\_column

```python
def add_column(aka_name: Name, label: str) -> None
```

x.add_column(aka_name, label) -> None
Add a column to SHeaderRow
note: Supported widgets: SHeaderRow.

Args:
    aka_name (Name): The aka name of the widget
    label (str): The Label of new column.

<a id="unreal.PythonBPAssetLib"></a>