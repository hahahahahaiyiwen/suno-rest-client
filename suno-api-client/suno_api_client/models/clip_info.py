from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clip_metadata import ClipMetadata


T = TypeVar("T", bound="ClipInfo")


@_attrs_define
class ClipInfo:
    """Info about the audio clip.

    Attributes:
        id (str): audio id
        created_at (str): Create time
        status (str): The generated states include submitted, queued, streaming, complete.
        metadata (ClipMetadata): Metadata of the audio clip.
        title (Union[Unset, str]): music title
        audio_url (Union[Unset, str]): music download url
        image_url (Union[Unset, str]): music cover image
        video_url (Union[Unset, str]): Music video download link, can be used to share
        model_name (Union[Unset, str]): suno model name, chirp-v3
    """

    id: str
    created_at: str
    status: str
    metadata: "ClipMetadata"
    title: Union[Unset, str] = UNSET
    audio_url: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    video_url: Union[Unset, str] = UNSET
    model_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        created_at = self.created_at

        status = self.status

        metadata = self.metadata.to_dict()

        title = self.title

        audio_url = self.audio_url

        image_url = self.image_url

        video_url = self.video_url

        model_name = self.model_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "status": status,
                "metadata": metadata,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if audio_url is not UNSET:
            field_dict["audio_url"] = audio_url
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if model_name is not UNSET:
            field_dict["model_name"] = model_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.clip_metadata import ClipMetadata

        d = src_dict.copy()
        id = d.pop("id")

        created_at = d.pop("created_at")

        status = d.pop("status")

        metadata = ClipMetadata.from_dict(d.pop("metadata"))

        title = d.pop("title", UNSET)

        audio_url = d.pop("audio_url", UNSET)

        image_url = d.pop("image_url", UNSET)

        video_url = d.pop("video_url", UNSET)

        model_name = d.pop("model_name", UNSET)

        clip_info = cls(
            id=id,
            created_at=created_at,
            status=status,
            metadata=metadata,
            title=title,
            audio_url=audio_url,
            image_url=image_url,
            video_url=video_url,
            model_name=model_name,
        )

        clip_info.additional_properties = d
        return clip_info

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
