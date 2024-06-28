from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clip_info import ClipInfo
    from ..models.clip_metadata import ClipMetadata


T = TypeVar("T", bound="AudioResult")


@_attrs_define
class AudioResult:
    """The result of generated audios

    Attributes:
        id (str): Generation request id.
        status (str): The generated states include submitted, queue, streaming, complete.
        metadata (ClipMetadata): Metadata of the audio clip.
        created_at (str): Create time
        clips (Union[Unset, List['ClipInfo']]):
    """

    id: str
    status: str
    metadata: "ClipMetadata"
    created_at: str
    clips: Union[Unset, List["ClipInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        status = self.status

        metadata = self.metadata.to_dict()

        created_at = self.created_at

        clips: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.clips, Unset):
            clips = []
            for clips_item_data in self.clips:
                clips_item = clips_item_data.to_dict()
                clips.append(clips_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "metadata": metadata,
                "created_at": created_at,
            }
        )
        if clips is not UNSET:
            field_dict["clips"] = clips

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.clip_info import ClipInfo
        from ..models.clip_metadata import ClipMetadata

        d = src_dict.copy()
        id = d.pop("id")

        status = d.pop("status")

        metadata = ClipMetadata.from_dict(d.pop("metadata"))

        created_at = d.pop("created_at")

        clips = []
        _clips = d.pop("clips", UNSET)
        for clips_item_data in _clips or []:
            clips_item = ClipInfo.from_dict(clips_item_data)

            clips.append(clips_item)

        audio_result = cls(
            id=id,
            status=status,
            metadata=metadata,
            created_at=created_at,
            clips=clips,
        )

        audio_result.additional_properties = d
        return audio_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
