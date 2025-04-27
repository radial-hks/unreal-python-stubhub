## LensFile Objects

```python
class LensFile(Object)
```

A Lens file containing calibration mapping from FIZ data

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensFile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only] Importing data and options used for importing ulens files.
- ``camera_feed_info`` (CameraFeedInfo):  [Read-Write] Camera feed information
- ``data_mode`` (LensDataMode):  [Read-Write] Type of data used for lens mapping
- ``lens_info`` (LensInfo):  [Read-Write] Lens information
- ``simulcam_info`` (SimulcamInfo):  [Read-Only] Simulcam information
- ``user_metadata`` (Map[str, str]):  [Read-Write] Metadata user could enter for its lens

<a id="unreal.LensFile.lens_info"></a>

#### lens_info

```python
@property
def lens_info() -> LensInfo
```

(LensInfo):  [Read-Write] Lens information

<a id="unreal.LensFile.lens_info"></a>

#### lens_info

```python
@lens_info.setter
def lens_info(value: LensInfo) -> None
```

<a id="unreal.LensFile.camera_feed_info"></a>

#### camera_feed_info

```python
@property
def camera_feed_info() -> CameraFeedInfo
```

(CameraFeedInfo):  [Read-Write] Camera feed information

<a id="unreal.LensFile.camera_feed_info"></a>

#### camera_feed_info

```python
@camera_feed_info.setter
def camera_feed_info(value: CameraFeedInfo) -> None
```

<a id="unreal.LensFile.simulcam_info"></a>

#### simulcam_info

```python
@property
def simulcam_info() -> SimulcamInfo
```

(SimulcamInfo):  [Read-Only] Simulcam information

<a id="unreal.LensFile.data_mode"></a>

#### data_mode

```python
@property
def data_mode() -> LensDataMode
```

(LensDataMode):  [Read-Write] Type of data used for lens mapping

<a id="unreal.LensFile.data_mode"></a>

#### data_mode

```python
@data_mode.setter
def data_mode(value: LensDataMode) -> None
```

<a id="unreal.LensFile.user_metadata"></a>

#### user_metadata

```python
@property
def user_metadata() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] Metadata user could enter for its lens

<a id="unreal.LensFile.user_metadata"></a>

#### user_metadata

```python
@user_metadata.setter
def user_metadata(value: Map[str, str]) -> None
```

<a id="unreal.LensFile.remove_zoom_point"></a>

#### remove_zoom_point

```python
def remove_zoom_point(data_category: LensDataCategory, focus: float,
                      zoom: float) -> None
```

x.remove_zoom_point(data_category, focus, zoom) -> None
Removes a zoom point

Args:
    data_category (LensDataCategory): 
    focus (float): 
    zoom (float):

<a id="unreal.LensFile.remove_focus_point"></a>

#### remove_focus_point

```python
def remove_focus_point(data_category: LensDataCategory, focus: float) -> None
```

x.remove_focus_point(data_category, focus) -> None
Removes a focus point

Args:
    data_category (LensDataCategory): 
    focus (float):

<a id="unreal.LensFile.merge_focus_point"></a>

#### merge_focus_point

```python
def merge_focus_point(data_category: LensDataCategory, src_focus: float,
                      dest_focus: float,
                      replace_existing_zoom_points: bool) -> None
```

x.merge_focus_point(data_category, src_focus, dest_focus, replace_existing_zoom_points) -> None
Merges the contents of one focus point into another focus point

Args:
    data_category (LensDataCategory): 
    src_focus (float): 
    dest_focus (float): 
    replace_existing_zoom_points (bool):

<a id="unreal.LensFile.has_zoom_point"></a>

#### has_zoom_point

```python
def has_zoom_point(data_category: LensDataCategory, focus: float,
                   zoom: float) -> bool
```

x.has_zoom_point(data_category, focus, zoom) -> bool
Removes a zoom point

Args:
    data_category (LensDataCategory): 
    focus (float): 
    zoom (float): 

Returns:
    bool:

<a id="unreal.LensFile.has_samples"></a>

#### has_samples

```python
def has_samples(data_category: LensDataCategory) -> bool
```

x.has_samples(data_category) -> bool
Returns whether a category has data samples

Args:
    data_category (LensDataCategory): 

Returns:
    bool:

<a id="unreal.LensFile.has_iris_encoder_mapping"></a>

#### has_iris_encoder_mapping

```python
def has_iris_encoder_mapping() -> bool
```

x.has_iris_encoder_mapping() -> bool
Whether iris encoder mapping is configured

Returns:
    bool:

<a id="unreal.LensFile.has_focus_point"></a>

#### has_focus_point

```python
def has_focus_point(data_category: LensDataCategory, focus: float) -> bool
```

x.has_focus_point(data_category, focus) -> bool
Checks to see if there is a focal point for the specified focus in the data category

Args:
    data_category (LensDataCategory): 
    focus (float): 

Returns:
    bool:

<a id="unreal.LensFile.has_focus_encoder_mapping"></a>

#### has_focus_encoder_mapping

```python
def has_focus_encoder_mapping() -> bool
```

x.has_focus_encoder_mapping() -> bool
Whether focus encoder mapping is configured

Returns:
    bool:

<a id="unreal.LensFile.get_total_point_num"></a>

#### get_total_point_num

```python
def get_total_point_num(data_category: LensDataCategory) -> int
```

x.get_total_point_num(data_category) -> int32
Returns total number of the points for given category

Args:
    data_category (LensDataCategory): 

Returns:
    int32:

<a id="unreal.LensFile.get_st_map_points"></a>

#### get_st_map_points

```python
def get_st_map_points() -> Array[STMapPointInfo]
```

x.get_st_map_points() -> Array[STMapPointInfo]
Gets all ST Map points struct with focus, zoom and info

Returns:
    Array[STMapPointInfo]:

<a id="unreal.LensFile.get_st_map_point"></a>

#### get_st_map_point

```python
def get_st_map_point(focus: float, zoom: float) -> Optional[STMapInfo]
```

x.get_st_map_point(focus, zoom) -> STMapInfo or None
Gets a ST Map point by given focus and zoom, if point does not exists returns false

Args:
    focus (float): 
    zoom (float): 

Returns:
    STMapInfo or None: 

    out_st_map_info (STMapInfo):

<a id="unreal.LensFile.get_nodal_offset_points"></a>

#### get_nodal_offset_points

```python
def get_nodal_offset_points() -> Array[NodalOffsetPointInfo]
```

x.get_nodal_offset_points() -> Array[NodalOffsetPointInfo]
Gets all Nodal Offset points struct with focus, zoom and info

Returns:
    Array[NodalOffsetPointInfo]:

<a id="unreal.LensFile.get_nodal_offset_point"></a>

#### get_nodal_offset_point

```python
def get_nodal_offset_point(focus: float,
                           zoom: float) -> Optional[NodalPointOffset]
```

x.get_nodal_offset_point(focus, zoom) -> NodalPointOffset or None
Gets a Nodal Offset point by given focus and zoom, if point does not exists returns false

Args:
    focus (float): 
    zoom (float): 

Returns:
    NodalPointOffset or None: 

    out_nodal_point_offset (NodalPointOffset):

<a id="unreal.LensFile.get_image_center_points"></a>

#### get_image_center_points

```python
def get_image_center_points() -> Array[ImageCenterPointInfo]
```

x.get_image_center_points() -> Array[ImageCenterPointInfo]
Gets all Image Center points struct with focus, zoom and info

Returns:
    Array[ImageCenterPointInfo]:

<a id="unreal.LensFile.get_image_center_point"></a>

#### get_image_center_point

```python
def get_image_center_point(focus: float,
                           zoom: float) -> Optional[ImageCenterInfo]
```

x.get_image_center_point(focus, zoom) -> ImageCenterInfo or None
Gets a Image Center point by given focus and zoom, if point does not exists returns false

Args:
    focus (float): 
    zoom (float): 

Returns:
    ImageCenterInfo or None: 

    out_image_center_info (ImageCenterInfo):

<a id="unreal.LensFile.get_focal_length_points"></a>

#### get_focal_length_points

```python
def get_focal_length_points() -> Array[FocalLengthPointInfo]
```

x.get_focal_length_points() -> Array[FocalLengthPointInfo]
Gets all Focal Length points struct with focus, zoom and info

Returns:
    Array[FocalLengthPointInfo]:

<a id="unreal.LensFile.get_focal_length_point"></a>

#### get_focal_length_point

```python
def get_focal_length_point(focus: float,
                           zoom: float) -> Optional[FocalLengthInfo]
```

x.get_focal_length_point(focus, zoom) -> FocalLengthInfo or None
Gets a Focal Length point by given focus and zoom, if point does not exists returns false

Args:
    focus (float): 
    zoom (float): 

Returns:
    FocalLengthInfo or None: 

    out_focal_length_info (FocalLengthInfo):

<a id="unreal.LensFile.get_distortion_points"></a>

#### get_distortion_points

```python
def get_distortion_points() -> Array[DistortionPointInfo]
```

x.get_distortion_points() -> Array[DistortionPointInfo]
Gets all Distortion points struct with focus, zoom and info

Returns:
    Array[DistortionPointInfo]:

<a id="unreal.LensFile.get_distortion_point"></a>

#### get_distortion_point

```python
def get_distortion_point(focus: float,
                         zoom: float) -> Optional[DistortionInfo]
```

x.get_distortion_point(focus, zoom) -> DistortionInfo or None
Gets a Distortion point by given focus and zoom, if point does not exists returns false

Args:
    focus (float): 
    zoom (float): 

Returns:
    DistortionInfo or None: 

    out_distortion_info (DistortionInfo):

<a id="unreal.LensFile.evaluate_normalized_iris"></a>

#### evaluate_normalized_iris

```python
def evaluate_normalized_iris(normalized_value: float) -> float
```

x.evaluate_normalized_iris(normalized_value) -> float
Returns interpolated iris based on input normalized value and mapping

Args:
    normalized_value (float): 

Returns:
    float:

<a id="unreal.LensFile.evaluate_normalized_focus"></a>

#### evaluate_normalized_focus

```python
def evaluate_normalized_focus(normalized_value: float) -> float
```

x.evaluate_normalized_focus(normalized_value) -> float
Returns interpolated focus based on input normalized value and mapping

Args:
    normalized_value (float): 

Returns:
    float:

<a id="unreal.LensFile.evaluate_nodal_point_offset"></a>

#### evaluate_nodal_point_offset

```python
def evaluate_nodal_point_offset(focus: float,
                                zoom: float) -> Optional[NodalPointOffset]
```

x.evaluate_nodal_point_offset(focus, zoom) -> NodalPointOffset or None
Returns interpolated nodal point offset based on input focus and zoom

Args:
    focus (float): 
    zoom (float): 

Returns:
    NodalPointOffset or None: 

    out_evaluated_value (NodalPointOffset):

<a id="unreal.LensFile.evaluate_image_center_parameters"></a>

#### evaluate_image_center_parameters

```python
def evaluate_image_center_parameters(focus: float,
                                     zoom: float) -> Optional[ImageCenterInfo]
```

x.evaluate_image_center_parameters(focus, zoom) -> ImageCenterInfo or None
Returns interpolated image center parameters based on input focus and zoom

Args:
    focus (float): 
    zoom (float): 

Returns:
    ImageCenterInfo or None: 

    out_evaluated_value (ImageCenterInfo):

<a id="unreal.LensFile.evaluate_focal_length"></a>

#### evaluate_focal_length

```python
def evaluate_focal_length(focus: float,
                          zoom: float) -> Optional[FocalLengthInfo]
```

x.evaluate_focal_length(focus, zoom) -> FocalLengthInfo or None
Returns interpolated focal length

Args:
    focus (float): 
    zoom (float): 

Returns:
    FocalLengthInfo or None: 

    out_evaluated_value (FocalLengthInfo):

<a id="unreal.LensFile.evaluate_distortion_parameters"></a>

#### evaluate_distortion_parameters

```python
def evaluate_distortion_parameters(focus: float,
                                   zoom: float) -> Optional[DistortionInfo]
```

x.evaluate_distortion_parameters(focus, zoom) -> DistortionInfo or None
Returns interpolated distortion parameters

Args:
    focus (float): 
    zoom (float): 

Returns:
    DistortionInfo or None: 

    out_evaluated_value (DistortionInfo):

<a id="unreal.LensFile.evaluate_distortion_data"></a>

#### evaluate_distortion_data

```python
def evaluate_distortion_data(
        focus: float, zoom: float, filmback: Vector2D,
        lens_handler: LensDistortionModelHandlerBase) -> bool
```

x.evaluate_distortion_data(focus, zoom, filmback, lens_handler) -> bool
Draws the distortion map based on evaluation point

Args:
    focus (float): 
    zoom (float): 
    filmback (Vector2D): 
    lens_handler (LensDistortionModelHandlerBase): 

Returns:
    bool:

<a id="unreal.LensFile.clear_data"></a>

#### clear_data

```python
def clear_data(data_category: LensDataCategory) -> None
```

x.clear_data(data_category) -> None
Removes table associated to data category

Args:
    data_category (LensDataCategory):

<a id="unreal.LensFile.clear_all"></a>

#### clear_all

```python
def clear_all() -> None
```

x.clear_all() -> None
Removes all points of all tables

<a id="unreal.LensFile.change_zoom_point"></a>

#### change_zoom_point

```python
def change_zoom_point(data_category: LensDataCategory, focus: float,
                      existing_zoom: float, new_zoom: float) -> None
```

x.change_zoom_point(data_category, focus, existing_zoom, new_zoom) -> None
Changes the value of a zoom point

Args:
    data_category (LensDataCategory): 
    focus (float): 
    existing_zoom (float): 
    new_zoom (float):

<a id="unreal.LensFile.change_focus_point"></a>

#### change_focus_point

```python
def change_focus_point(data_category: LensDataCategory, existing_focus: float,
                       new_focus: float) -> None
```

x.change_focus_point(data_category, existing_focus, new_focus) -> None
Changes the value of a focus point

Args:
    data_category (LensDataCategory): 
    existing_focus (float): 
    new_focus (float):

<a id="unreal.LensFile.add_st_map_point"></a>

#### add_st_map_point

```python
def add_st_map_point(new_focus: float, new_zoom: float,
                     new_point: STMapInfo) -> None
```

x.add_st_map_point(new_focus, new_zoom, new_point) -> None
Adds an STMap point in our map. If a point already exist at the location, it is updated

Args:
    new_focus (float): 
    new_zoom (float): 
    new_point (STMapInfo):

<a id="unreal.LensFile.add_nodal_offset_point"></a>

#### add_nodal_offset_point

```python
def add_nodal_offset_point(new_focus: float, new_zoom: float,
                           new_point: NodalPointOffset) -> None
```

x.add_nodal_offset_point(new_focus, new_zoom, new_point) -> None
Adds an NodalOffset point in our map. If a point already exist at the location, it is updated

Args:
    new_focus (float): 
    new_zoom (float): 
    new_point (NodalPointOffset):

<a id="unreal.LensFile.add_image_center_point"></a>

#### add_image_center_point

```python
def add_image_center_point(new_focus: float, new_zoom: float,
                           new_point: ImageCenterInfo) -> None
```

x.add_image_center_point(new_focus, new_zoom, new_point) -> None
Adds an ImageCenter point in our map. If a point already exist at the location, it is updated

Args:
    new_focus (float): 
    new_zoom (float): 
    new_point (ImageCenterInfo):

<a id="unreal.LensFile.add_focal_length_point"></a>

#### add_focal_length_point

```python
def add_focal_length_point(new_focus: float, new_zoom: float,
                           new_focal_length: FocalLengthInfo) -> None
```

x.add_focal_length_point(new_focus, new_zoom, new_focal_length) -> None
Adds a focal length point in our map. If a point already exist at the location, it is updated

Args:
    new_focus (float): 
    new_zoom (float): 
    new_focal_length (FocalLengthInfo):

<a id="unreal.LensFile.add_distortion_point"></a>

#### add_distortion_point

```python
def add_distortion_point(new_focus: float, new_zoom: float,
                         new_point: DistortionInfo,
                         new_focal_length: FocalLengthInfo) -> None
```

x.add_distortion_point(new_focus, new_zoom, new_point, new_focal_length) -> None
Adds a distortion point in our map. If a point already exist at the location, it is updated

Args:
    new_focus (float): 
    new_zoom (float): 
    new_point (DistortionInfo): 
    new_focal_length (FocalLengthInfo):

<a id="unreal.SphericalLensDistortionModelHandler"></a>